# Symmetric/alternating splitting census for two-row Kronecker squares in S7/S8 with maximal-gap witness

## Context
The Kronecker square $[\lambda]^2$ of a symmetric-group irreducible splits into
symmetric and alternating parts $S^2[\lambda]+A^2[\lambda]$.
Bessenrodt–Bowman (arXiv:2202.03066) establish this splitting program,
prove closed formulas for $[k,k]$, $[k{+}1,k]$, $[k{+}1,k{-}1]$
(Thms 7.8/7.11/7.13), and state conjectures needing exact small-$n$
$(s,a)$ data, with links to 2-modular decomposition numbers, Catalan
combinatorics, and the refined Saxl conjecture.
Plain Kronecker positivity (Pak–Panova–Vallejo; Zhao) does not imply
splitting, which requires $\chi(w^2)$.
No published source gives an exhaustive certified two-row $(s,a)$ census
at S7/S8 with committed $w\mapsto w^2$ logs and a maximal-gap witness.

## Definitions
Let $\chi_\lambda$ be the irreducible complex character of $S_n$ for
$\lambda\vdash n$. For class $C$ let $C^2$ be the class of $w^2$, $w\in C$.
Define
$$\chi_S(C)=(\chi_\lambda(C)^2+\chi_\lambda(C^2))/2,\qquad
  \chi_A(C)=(\chi_\lambda(C)^2-\chi_\lambda(C^2))/2,$$
the characters of $\mathrm{Sym}^2$ and $\mathrm{Alt}^2$, and
$$s(\lambda,\nu)=\langle\chi_S,\chi_\nu\rangle,\quad
  a(\lambda,\nu)=\langle\chi_A,\chi_\nu\rangle,\quad
  g(\lambda,\lambda,\nu)=\langle\chi_\lambda^2,\chi_\nu\rangle,$$
so $s+a=g$. Two-row means $\ell(\lambda)\le 2$.

## Result
(a) Full census: for every two-row $\lambda\vdash 7$ (4 shapes
$[7],[6,1],[5,2],[4,3]$) and every $\nu\vdash 7$ (15 shapes),
and every two-row $\lambda\vdash 8$ (5 shapes
$[8],[7,1],[6,2],[5,3],[4,4]$) and every $\nu\vdash 8$ (22 shapes),
the triple $(s,a,g)$ is exactly as in
`splitting_tworow_S7.csv` (60 rows) and `splitting_tworow_S8.csv`
(110 rows); every entry has $s,a,g\ge 0$ integers with $s+a=g$.

(b) Maximal gap: over the two-row-square family at each $n$,
$\max|s-a|=2$, attained. Lexicographically-first maximizers:
- S7: $(\lambda,\nu)=([5,2],[5,2])$, $(s,a,g)=(2,0,2)$,
  $\sum_C|C|\chi_S\chi_\nu=10080=2\cdot 7!$,
  $\sum_C|C|\chi_A\chi_\nu=0$;
- S8: $(\lambda,\nu)=([5,3],[4,2,2])$, $(s,a,g)=(2,0,2)$,
  $\sum_C|C|\chi_S\chi_\nu=80640=2\cdot 8!$,
  $\sum_C|C|\chi_A\chi_\nu=0$.
Per-class sums are in the two `gap_certificate_*.json` files.
At S8 there are three gap-2 ties
$([5,3],[4,2,2])$, $([5,3],[6,2])$, $([6,2],[6,2])$; the reported
maximizer is the lex-first.

(c) Spot checks: for every two-row $\lambda$ at $n=7,8$,
trivial $[n]$ has $(s,a)=(1,0)$ and sign $[1^n]$ has $(s,a,g)=(0,0,0)$.
Positivity tallies (nonzero-$g$; $s{>}0$; $a{>}0$):
S7 $[4,3]$: 11;7;4. $[5,2]$: 9;6;4. $[6,1]$: 4;3;1. $[7]$: 1;1;0.
S8 $[4,4]$: 7;5;2. $[5,3]$: 14;9;7. $[6,2]$: 10;7;4.
$[7,1]$: 4;3;1. $[8]$: 1;1;0.
Rows $[5,2]$ (S7) and $[6,2]$ (S8), of two-row difference $\ge 3$,
lie outside the Bessenrodt–Bowman $[k,k]$/$[k{+}1,k]$/$[k{+}1,k{-}1]$
closed forms; the S8 $[4,4]$ row matches Thm B $E_4(8)$/$O_4(8)$ exactly.

## Proof / evidence
Finite exact machine-checked computation, independently replayed:
from-scratch Murnaghan–Nakayama tables (15/22 classes), committed
class-squaring map $C\mapsto\mathrm{class}(w^2)$ verified by explicit
permutation squaring, $\chi_S$/$\chi_A$ formation with parity checks,
inner products with integrality/nonnegativity/$s{+}a{=}g$ checks,
dimension-weighted sum rules
$\sum_\nu s\dim\nu=d(d{+}1)/2$, $\sum_\nu a\dim\nu=d(d{-}1)/2$,
row/column orthogonality, hook-dimension column, and independent
CSV-only replay `verify.py` printing `VERIFY_OK`.
Gap certificates verified term-by-term.

## Limitations
Finite census at S7/S8 two-row squares only; no general formula or
conjecture resolution. Maximal gap is small (2). Overlap: the
difference-$\le 2$ rows ($[4,4],[4,3],[5,3]$) fall under published
Bessenrodt–Bowman theorems; novelty of the census rests on the full
170-triple table with power-map logs, the difference-$\ge 3$ rows
$[5,2],[6,2]$, and the cross-family maximality statement.

## Reproducibility
Stdlib-only Python. From the lane directory:
`python3 output/artifacts/verify.py` (expect `VERIFY_OK` plus the two
maxgap lines); regenerate with `python3 output/artifacts/compute.py`
and `diff` the CSVs.

## References
- Bessenrodt–Bowman, Splitting Kronecker squares ...,
  arXiv:2202.03066.
- Pak–Panova–Vallejo, Kronecker products, characters, partitions ...,
  arXiv:1304.0738.
- Zhao, On the Kronecker product of Schur functions of square shapes,
  arXiv:2309.00764.
