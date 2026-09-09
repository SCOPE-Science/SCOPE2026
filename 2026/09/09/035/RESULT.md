# Certified topological-entropy census for all 3-state shifts of finite type, with trace and zeta replay

## Context
Shifts of finite type (SFTs) defined by 0-1 adjacency matrices are a core object
in symbolic dynamics. Their standard invariants include topological entropy
`h = log rho(A)` (Perron-Frobenius spectral radius), periodic-point counts
`tr(A^k)`, and the Artin-Mazur zeta function `zeta(t) = 1/det(I-tA)`.
These feed entropy-rigidity, Williams shift-equivalence, and Krieger embedding
programs. The classical formulas are due to others (Lind-Marcus;
Manning/Artin-Mazur) and are not claimed here. The new content is the closed,
certified table for the first nontrivial window: unlabelled 3-state (0,1)-SFTs.

## Definitions
- Object: `A` ranges over `{0,1\}^{3x3}` (512 labelled matrices).
- Equivalence: `B = P A P^T` for a permutation matrix `P` (simultaneous
  permutation / relabelling of states).
- Canonical representative: `min_{P in S_3} flat(P A P^T)` lexicographically.
- Spectral radius `rho(A)` = largest modulus of a root of
  `chi_A(x) = x^3 + a x^2 + b x + c`.
- Topological entropy `h = log rho` for `rho > 0`; `h = 0` by the finite-shift
  convention for the 6 nilpotent classes (each has `A^3 = 0` verified).
- `Q_A(t) = det(I-tA) = 1 - e_1 t + e_2 t^2 - e_3 t^3`, zeta series
  `zeta_A(t) = 1/Q_A(t)` to order 6.

## Result (headline claim)
The 512 matrices reduce to **104 unlabelled types** with orbit-size histogram
`1:4, 3:28, 6:70, 2:2` (summing to 512; count agrees with OEIS A000595, which
records only the count).

The 104 types collapse to **18 distinct entropy values** (32 distinct
characteristic polynomials; 32 distinct `k <= 6` trace-sequences; every
characteristic-polynomial collision in this window is separated by its
trace-sequence):

| value-group | rho | h | ncl | ncp | ntr | orb |
|---|---|---|---|---|---|---|
| nilpotent (rho=0) | 0 | 0 (finite-shift convention) | 6 | 1 | 1 | 25 |
| R1 (rho=1) | 1 | 0 | 45 | 6 | 6 | 219 |
| plastic `x^3-x-1` | 1.324717957 | 0.281199574 | 1 | 1 | 1 | 6 |
| sqrt2 | 1.414213562 | 0.346573590 | 1 | 1 | 1 | 3 |
| `x^3-x^2-1` | 1.465571232 | 0.382245086 | 1 | 1 | 1 | 6 |
| golden ratio `(1+sqrt5)/2` | 1.618033989 | 0.481211825 | 16 | 3 | 3 | 96 |
| `x^3-2x^2+x-1` | 1.754877666 | 0.562399149 | 1 | 1 | 1 | 6 |
| `x^3-x^2-2x+1` | 1.801937736 | 0.588862606 | 1 | 1 | 1 | 6 |
| tribonacci `x^3-x^2-x-1` | 1.839286755 | 0.609377863 | 2 | 1 | 1 | 12 |
| R2 (rho=2) | 2 | 0.693147181 | 18 | 6 | 6 | 75 |
| `x^3-x^2-2x-1` | 2.147899036 | 0.764490172 | 1 | 1 | 1 | 6 |
| `x^3-2x^2-1` | 2.205569430 | 0.790985721 | 1 | 1 | 1 | 6 |
| `x^3-2x^2-x+1` | 2.246979604 | 0.809586916 | 2 | 1 | 1 | 12 |
| `x^3-3x^2+2x-1` | 2.324717957 | 0.843598723 | 1 | 1 | 1 | 6 |
| `1+sqrt2` | 2.414213562 | 0.881373587 | 4 | 3 | 3 | 18 |
| `(3+sqrt5)/2` | 2.618033989 | 0.962423650 | 1 | 1 | 1 | 6 |
| `1+sqrt3` | 2.732050808 | 1.005052539 | 1 | 1 | 1 | 3 |
| full 3-shift (rho=3) | 3 | 1.098612289 | 1 | 1 | 1 | 1 |

Largest collision classes: `rho=1`: 45 classes / 6 charpolys / 6 trace-seqs;
`rho=2`: 18/6/6; golden ratio: 16/3/3 (three charpolys sharing the factor
`x^2-x-1`); `1+sqrt2`: 4/3/3 (three charpolys sharing `x^2-2x-1`).

Extremal witnesses and gaps:
- Maximum: all-ones matrix `J_3` (orbit size 1), `chi(x)=x^2(x-3)`,
  `rho=3` exactly, `h=log 3 ~= 1.098612289`, `tr(J_3^k)=3^k`,
  `zeta(t)=1/(1-3t)`.
- Second maximum: all-ones except `a_11=0`, `chi(x)=x(x^2-2x-2)`,
  `rho=1+sqrt3 ~= 2.732050808`, `h ~= 1.005052539`,
  traces `(2,8,20,56,152,416)`.
- Minimal positive separations: rho-gap `> 0.037` (nominal `~0.037349`,
  between `x^3-x^2-2x+1` and tribonacci groups); h-gap `> 0.018`
  (nominal `~0.018601`, between `x^3-2x^2-1` and `x^3-2x^2-x+1` groups).

## Proof / evidence
- Exact integer computation: charpolys (trace, principal 2x2 minors,
  determinant), `tr(A^k)` for `k = 1..6`, `Q_A(t)` and zeta series by the
  exact recurrence `a_n = -sum_{k} q_k a_{n-k}`.
- Trace-zeta identity `-Q_A' = Q_A T_A mod t^6` verified exactly on all 104
  classes (equivalently the first six zeta coefficients agree with the trace
  formula).
- Spectral certification in exact `Fraction` arithmetic:
  - Reducible case (93 classes): integer-root deflation; `D<0` pairs have
    modulus `sqrt(q_0)` decided by the integer comparison `r^2 <> q_0` with
    dyadic `[m/2^50,(m+1)/2^50]` certificates; `D>=0` square handled by exact
    rational-root maxima; `D>0` nonsquare by integer-sqrt dyadic enclosures
    (width `< 3e-12`).
  - Irreducible case (11 classes, 9 distinct cubics): rational brackets with
    exact sign change plus derivative-positivity; `D<0` cubics all have
    `c=-1`, so `r|z|^2=1` with `lo>1` gives `rho=r`; `D=49` cubics use
    vertex `-a/3 <= lo` with `p'(lo)>0` to certify the bracketed root is the
    largest root, hence rho. Bisection to width `<= 2^-50` uses sign
    evaluations only.
- Equality of rho across classes only through exact shared-factor identities
  (e.g. `x^2-x-1`, `x^2-2x-1`, shared integral roots for `rho in {1,2,3}`);
  the 18 value-groups have pairwise disjoint rho-enclosures, so no further
  coincidence is possible.
- Entropy: `h=log rho` via the exact series `log x = 2 atanh((x-1)/(x+1))`
  with proven alternating-tail remainder bounds (80 terms), outward-rounded
  (width `< 1e-9`).
- Independent audit replayed enumeration, all exact invariants, enclosure
  side-conditions, maximality by exact deflation, grouping, gaps, and both
  extremal witnesses; `verify.py` prints `VERIFY_OK`.

## Limitations
- Background formulas `h=log rho`, `zeta=1/det(I-tA)` are classical, not new.
- Equal entropy/traces do not imply conjugacy; no shift-equivalence or
  conjugacy classification is claimed. Traces are non-conjugacy
  discriminants only; zeta agreement is a consistency check.
- `h=0` for the six nilpotent types is the stated finite-shift convention
  (`A^3=0` verified); no value is assigned to `log 0`.
- Scope is strictly unlabelled `n=3` (0,1)-matrices with `k<=6` traces; no
  `n>=4` or weighted-alphabet extension is claimed.

## Reproducibility
Run from the workspace root (paths are relative):

```
python3 output/artifacts/verify.py
```

Stdlib only; completes in seconds. Expected output: `VERIFY_OK`.
Artifacts: `output/artifacts/census.json` (104 per-class rows),
`output/artifacts/values.json` (18 value groups with certified bounds),
`output/artifacts/verify.py` (independent replay checker).

## References
- Lind & Marcus, An Introduction to Symbolic Dynamics and Coding.
  https://doi.org/10.1017/CBO9780511626302 (background formulas only)
- Agarwal-Cheriyath-Tikekar, A combinatorial approach to study subshifts
  associated with multigraphs. https://arxiv.org/abs/2211.06068
- Gohlke-Rust-Spindeler, Shifts of finite type and random substitutions.
  https://arxiv.org/abs/1712.05340
- Matsumoto, On the Markov-Dyck shifts of vertex type.
  https://arxiv.org/abs/1405.6443
- OEIS A000595, Number of binary relations on n unlabeled points.
  https://oeis.org/A000595 (count 104 only, not the table)
