# Certified vanishing census and maximal-multiplicity witness for Kronecker coefficients at n=12

## Context

Kronecker coefficients $g(\\lambda,\\mu,\\nu)$ are tensor-product multiplicities for
symmetric-group irreducibles. Deciding positivity is NP-hard
(Ikenmeyer–Mulmuley–Walter), general bounds (Pak–Panova) are rarely shown tight at
fixed $n$, dilated formulas (Baldoni–Vergne–Walter) cover single rays, and Saxl-type
results cover staircase rows. Small-$n$ values are folklore Sage/GAP one-liners
without published certificates. What is missing is exhaustive, independently
replayable ground truth at a non-trivial $n$ where asymptotics are silent.
$n=12$ is chosen as the first $n$ with $p(n)=77>70$, non-triangular (no staircase
partition, since $10<12<15$), where rectangular, self-conjugate, and Durfee-3 shapes
interact.

## Definitions

- Partitions $\\lambda\\vdash 12$ in lexicographic-descending order
  $0=(12),1=(11,1),\\dots,37=(5,3,2,1,1),\\dots,76=(1^{12})$; $p(12)=77$.
- Conjugacy classes $\\alpha\\vdash 12$ (cycle types) with centralizer size
  $z_\\alpha=\\prod_i i^{m_i}m_i!$ and class size $\\mathrm{cl}_\\alpha=12!/z_\\alpha$.
  Min $z=11$, max $z=479001600=12!$, $\\sum\\mathrm{cl}_\\alpha=12!$.
- Irreducible characters $\\chi^\\lambda_\\alpha$ via Murnaghan–Nakayama.
  Dimensions $d_\\lambda=\\chi^\\lambda_{(1^{12})}$ equal hook-formula values;
  max $d=7700$ at $(5,3,2,1,1)$.
- Kronecker coefficient by the exact class sum
  $$g(\\lambda,\\mu,\\nu)=\\sum_{\\alpha\\vdash 12}
    \\chi^\\lambda_\\alpha\\chi^\\mu_\\alpha\\chi^\\nu_\\alpha/z_\\alpha
    =N/12!,\\quad N=\\sum_\\alpha\\chi\\chi\\chi\\cdot\\mathrm{cl}_\\alpha.$$
- $S_3$ orbits under permuting the three arguments: $\\binom{79}{3}=79079$
  unordered representatives ($i\\le j\\le k$); $77^3=456533$ ordered triples.
- Durfee size $d(\\lambda)=\\max\\{d:\\lambda_d\\ge d\\}$; $p(12)$ splits
  $1{:}12$, $2{:}55$, $3{:}10$ (max $\\lfloor\\sqrt{12}\\rfloor=3$).
- Dominance order: $\\lambda\\trianglerighteq\\mu$ if all prefix sums dominate.

## Result (computed theorem, machine-checked)

Up to $S_3$ permutation ($79079$ orbits; $456533$ ordered):

- **Vanishing:** exactly **30336** orbits vanish, **48743** do not
  (vanishing fraction **38.3616%**). Ordered: **176524** zero vs **280009**
  nonzero (**38.6662%**). Every entry is a proven nonnegatively integral
  $N/12!$ ($N\\bmod 12!\\equiv 0$, $g\\ge 0$ on all $79079$).
- **Maximum:** $M(12)=\\mathbf{945}$, attained at a **unique** $S_3$-orbit
  $$T^\\star=((5,3,2,1,1),(5,3,2,1,1),(5,3,2,1,1))\\quad (37,37,37),$$
  the self-conjugate max-dimension ($7700$) Durfee-3 shape cubed.
  Next values: $716$ (2 orbits), $697$ (2 orbits), $550$ (2 orbits),
  $533$ (3 orbits); full top-10 in `artifacts/top10.csv`.
- **Predictor tests:** dominance-comparability counts (comparable unordered pairs
  among the 3): $0{:}433/43$ zero ($9.9\\%$), $1{:}4630/881$ ($19.0\\%$),
  $2{:}19856/7045$ ($35.5\\%$), $3{:}54160/22367$ ($41.3\\%$) — more comparable
  implies *more* likely to vanish here. Example incomparable-yet-nonzero:
  $g((9,1,1,1),(8,3,1),(7,5))=1$ (all three pairs incomparable; 390 such nonzero
  orbits). Durfee-profile breakdown (total/zero): $(1,1,1){:364/228}$,
  $(1,1,2){:4290/3527}$, $(1,1,3){:780/780}$ ($100\\%$),
  $(1,2,2){:18480/11074}$, $(1,2,3){:6600/4464}$, $(1,3,3){:660/216}$,
  $(2,2,2){:29260/7071}$, $(2,2,3){:15400/2835}$, $(2,3,3){:3025/132}$,
  $(3,3,3){:220/9}$. The trivial dimension bound $g\\le d_\\lambda d_\\mu/d_\\nu$
  gives $7700$ at $T^\\star$ vs actual $945$ ($\\sim 12\\%$), so character/dimension
  bounds are far from tight at the maximum.

## Proof / evidence (exact integer certificates)

1. Enumerate 77 partitions/classes; $z_\\alpha,\\mathrm{cl}_\\alpha$ as above.
2. Build $77\\times 77$ characters by Murnaghan–Nakayama (rim-hook removal,
   sign $(-1)^{\\mathrm{height}}$, memoised recursion) in pure-Python stdlib.
3. Compute each $g$ exactly as $N/12!$ with `divmod` remainder check; evaluate
   only $i\\le j\\le k$.
4. Self-checks, all exact: hook dims match (max $7700$); $\\sum d^2=12!$;
   dual-strip-order cross-check $5929/5929$ (auditor's independent build stripping
   smallest part vs candidate stripping largest); row orthogonality $5929/5929$
   and column orthogonality $5929/5929$; float-einsum deviation $1.2\\times10^{-13}$;
   integrality/nonnegativity $79079/79079$; $S_3$ symmetry by construction+verified;
   $\\sum_\\nu g(\\lambda,\\mu,\\nu)d_\\nu=d_\\lambda d_\\mu$ on all $5929$ pairs;
   even-transpose $g(\\lambda^t,\\mu^t,\\nu)=g(\\lambda,\\mu,\\nu)$ on all orbits;
   $T^\\star$ Fraction sum $945$ ($N=452656512000$); CSV spot/full recompute.
5. Certificate `artifacts/certificate_Tstar.csv` lists for each of the 77 classes
   $z_\\alpha,\\mathrm{cl}_\\alpha$, the three (equal) characters, and summand
   $\\chi^3/z_\\alpha$ as an exact reduced fraction; summing gives $945$.
   Any auditor recomputes `sum(Fraction(c1*c2*c3,z))` from the triple alone.
   The auditor's from-scratch reimplementation reproduced the full chartable,
   all census counts, breakdowns, and top-10 exactly.

This is proof conditional on the short MN program, elevated by two independent
builds plus orthogonality/hook/dimension-sum theorems — not trust in one run.
Observed patterns (high-Durfee rarely vanishes; dominance is a weak reversed
predictor; extremal shape is max-dim self-conjugate) are empirical at $n=12$;
no new combinatorial formula or asymptotic bound is claimed.

## Limitations

- Fixed-$n=12$ computational census; identities are machine-checked integers,
  not human-readable combinatorics. A bug common to both MN orderings is
  unlikely but not logically excluded.
- No structural proof of $M(12)=945$ or the $(1,1,3)$ $100\\%$-vanishing pocket;
  proving either is left open. Does not resolve hardness, Saxl, or GCT barriers;
  it supplies ground truth those theories must fit.
- Originality is only the first independently recheckable exhaustive $S_3$-reduced
  census with extremal certificate at $n=12$, not a new method.

## Reproducibility

- `artifacts/replay.py` (stdlib only): standard run ($\\sim 0.2$ s) rebuilds the
  character table, verifies hook/dim-sum/orthogonality, recomputes $T^\\star$
  exactly, spot-checks 20 random orbits, and confirms census counts;
  `python3 replay.py --full` recomputes all $79079$ exactly ($\\sim 0.4$ s).
- `artifacts/certificate_Tstar.csv`: 77-row exact per-class certificate for $T^\\star$.
- `artifacts/top10.csv`: top-10 extremal $S_3$-orbits.
- Full $79079$-row table regenerable via `--full`; partition index is
  lexicographic-descending as above.

## References

- Ikenmeyer–Mulmuley–Walter, On vanishing of Kronecker coefficients,
  https://arxiv.org/abs/1507.02955 (NP-hardness; complementary ground truth).
- Pak–Panova, Bounds on the Kronecker coefficients,
  https://arxiv.org/abs/1406.2988 (bounds tested here for tightness).
- Baldoni–Vergne–Walter, Computation of Dilated Kronecker Coefficients,
  https://arxiv.org/abs/1601.04325 (single-ray symbolic vs full fixed-$n$ cube).
- Ikenmeyer, Saxl Conjecture for triple hooks,
  https://arxiv.org/abs/1811.10967 (staircase rows; $n=12$ non-triangular, disjoint).
- Pak–Panova, Durfee squares, symmetric partitions and bounds,
  https://arxiv.org/abs/2207.02561 (asymptotic Durfee/superexponential bounds).
- Vallejo, On rectangular Kronecker coefficients, https://arxiv.org/abs/0907.3351.
- Ikenmeyer et al., Machine-Learning Kronecker Coefficients,
  https://arxiv.org/abs/2306.04734 (heuristic classifier vs exact certificates here).
