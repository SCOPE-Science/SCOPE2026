# Closed single-element extension cell over the rank-4 binary cube A8, with Crapo beta and internal-4-connectivity verdicts

## Context

Seymour's Splitter Theorem, the Strong Splitter Theorem, the Chain theorem, and the
Geelen–Gerards–Whittle internally-4-connected program make single-element
extensions/coextensions at the 3-connected vs internally-4-connected transition the
recognized inductive progress unit for binary matroids. A fixed extremal binary anchor
with per-orbit beta invariants and separator verdicts is therefore a directly
retrievable classification datum.

## Definitions

Let **A8** be the binary matroid given by the explicit GF(2) matrix with 8 columns
$(1,x)$ for $x \in \mathrm{GF}(2)^3$:

| pt | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|----|---|---|---|---|---|---|---|---|
| r0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| r1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| r2 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| r3 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |

i.e. columns `0001,0011,0101,0111,1001,1011,1101,1111` (bit order r3r2r1r0).
This is the rank-4 binary affine cube AG(3,2) (8 points). Verified: rank 4,
56 bases out of C(8,4)=70, 3-connected, Crapo beta 6.
Its setwise stabilizer in GL(4,2) has order 1344 (= |AGL(3,2)|).

A rank-4 single-element extension adjoins one column $v \in \mathrm{GF}(2)^4$.
A literal rank-5 single-element coextension is $N(c) = [[A8\ 0];[c\ 1]]$ with
$c \in \mathrm{GF}(2)^8$, satisfying $N(c)/8 = A8$.
Crapo beta is $\beta = [x^1]T$ (coefficient of $x$ in the Tutte polynomial).
A matroid is internally 4-connected if it is 3-connected and has no 3-separation
$(X,Y)$ with $\min(|X|,|Y|) \ge 4$ (equivalently no violation with both sides $\ge 4$).
Here $\lambda(X)=r(X)+r(E\setminus X)-r(E)$.

## Result

Up to isomorphism there are exactly three rank-4 single-element extensions of A8 to
9 elements (three cocircuit-signature orbits), with representatives obtained by
adjoining:

- (E0) `0000` — loop orbit;
- (E2) `0001` — parallel (cube-vector) orbit;
- (E1) `0010` — simple (off-cube) orbit.

| orbit | new col | rank | #bases = T(1,1) | loops / parallel pairs | beta | 3-connected? | #3-sep violations (sides ≥3, λ<3) | internally 4-connected? |
|---|---|---|---|---|---|---|---|---|
| E0_loop | 0000 | 4 | 56 | loop {8} / — | 0 | NO (1-sep) | 42 | NO |
| E2_parallel | 0001 | 4 | 84 | — / (0,8) | 6 | NO (2-sep) | 14 | NO |
| E1_simple | 0010 | 4 | 88 | — / — (simple) | 7 | YES | 10 | NO |

In particular **no** single-element extension of A8 in this binary cell is internally
4-connected. E0 fails 3-connectivity via the 1-separation $\{0,\dots,7\}|\{8\}$;
E2 fails via the 2-separation $\{1,\dots,7\}|\{0,8\}$ ($\lambda=1$).
E1 is 3-connected but carries ten $\lambda$-2 3-separations: six genuine with both
sides $\ge 4$ (type 4|5) and four trivial with a 3-side (type 3|6), e.g.
$X=\{0,1,2,3\}\mid Y=\{4,5,6,7,8\}$ ($\lambda=2$, $r(X)=r(Y)=3$) and
$X=\{6,7,8\}\mid Y=\{0,\dots,5\}$ ($\lambda=2$, $r(X)=2$, $r(Y)=4$).

Literal rank-5 picture: contraction $N(c)/8=A8$ holds for all 256 $c$; row-equivalence
leaves 16 cosets; the Aut(A8)-action has exactly 3 orbits of sizes 1/8/7 with
per-orbit (bases, beta, connectivity) $(56,0$, not 3-connected$)$,
$(84,6$, not 3-connected$)$, $(88,7$, 3-connected with ten $\lambda$-2 3-separations$)$.
Hence no literal coextension is internally 4-connected either.

## Proof / evidence

- Base: subset-rank enumeration gives 56 bases, no 1- or 2-separation, beta 6.
- Stabilizer: exhaustive enumeration of GL(4,2) (20160 matrices) gives stabilizer
  order 1344; its orbits on GF(2)^4 are exactly $\{0\}$ (size 1), the 8 cube columns
  (size 8), and the 7 off-cube nonzero vectors with $r_0=0$ (size 7), with explicit
  transitivity witnesses. Hence exactly three column-addition signatures.
- Beta: memoized deletion–contraction Tutte evaluation (213/266/261 states for
  E0/E2/E1), cross-checked by $\beta=(-1)^{r+1}\chi'(1)$ via the subset Möbius sum
  and by $T(1,1)=\#\text{bases}$; independently re-verified by a rank-generating-function
  Tutte expansion giving beta 0/6/7 and T(1,1) 56/84/88.
- Connectivity: exhaustive $2^9$-subset separation scans give violation counts
  (1,8,42), (0,1,14), (0,0,10) for 1-seps, 2-seps, 3-seps respectively; non-isomorphism
  follows from (loops, parallel pairs, #bases, beta) profiles.
- Literal coextensions: all 256 contractions checked equal to A8; 16 row-cosets and
  3 Aut-orbits of sizes 1/8/7 re-enumerated; per-orbit Tutte/beta and separator scans
  match the rank-4 table.
- Reproduce: `python3 output/artifacts/verify_cell.py` prints `VERIFY_OK`;
  `python3 output/artifacts/verify_coext.py` prints `VERIFY_COEXT_OK`.

## Limitations

- Enumeration is within binary single-element extensions (as the target specifies:
  "to 9-element binary matroids"); non-binary extensions of A8 are out of scope.
- Internal-4-connectivity uses the standard definition (3-connected plus no
  3-separation with both sides $\ge 4$); the "10 violations" count for E1 includes
  four trivial 3|6 separations, but six genuine 4|5 violations sustain the verdict.
- The admission label "AG(3,2) minus a point" is a naming slip; the audited object is
  the explicit 8-point AG(3,2) matrix above. Cite the matrix, not the label.

## Reproducibility

`output/artifacts/verify_cell.py` recomputes bases, beta via deletion–contraction
with chi-prime check, 3-connectivity and internal-4-connectivity verdicts, and orbit
completeness, rewriting `orbit_table.json` and deletion–contraction logs.
`output/artifacts/verify_coext.py` recomputes the rank-5 picture, rewriting
`coext_table.json`. Standard-library Python only.

## References

- D. Mayhew, G. Royle, Matroids with nine elements, arXiv:math/0702316.
- S. R. Kingan, M. Lemos, Strong Splitter Theorem, arXiv:1201.4427.
- C. Chun, D. Mayhew, J. Oxley, Towards a splitter theorem for internally
  4-connected binary matroids VIII: small matroids, arXiv:1501.00327.
