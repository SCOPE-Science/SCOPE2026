# Symmetric/alternating splitting of non-hook three-row Kronecker squares in S6–S8

## Context

The Kronecker square of an irreducible complex character $[\lambda]$ of $S_n$
splits into symmetric and alternating parts,
$S^2[\lambda] = \sum_\nu \mathrm{sg}(\lambda,\nu)[\nu]$,
$A^2[\lambda] = \sum_\nu \mathrm{ag}(\lambda,\nu)[\nu]$.
Closed splitting formulas are known for hooks (Mészáros–Wolosz;
Bessenrodt–Bowman §4), for constituents/squares of small depth
(Bessenrodt–Bowman Thm 5.2, Prop 5.4, Thm 5.5 for $[n-3,3]$),
and for 2-part squares $[k,k]$, $[k+1,k]$, $[k+1,k-1]$
(Bessenrodt–Bowman Thms 7.8/7.11/7.13).
The $[n-3,2,1]$-type square is explicitly left open as
"much more involved". Unsplit positivity ($g>0$) for adjacent families
(Pak–Panova–Vallejo; Zhao for square shapes) does not determine the
splitting. The splitting program is motivated by refined-Saxl
Conjecture C, 2-modular decomposition links, multiplicity-free
classification, and Catalan combinatorics (Bessenrodt–Bowman).

## Definitions

A partition $\lambda \vdash n$ is *non-hook three-row* if it has exactly
3 parts and $\lambda_2 \ge 2$ (hence depth $n-\lambda_1 \ge 3$).
For $n=6,7,8$ these are 2+3+4 = 9 partitions:

- n=6: $(3,2,1)$, $(2,2,2)$
- n=7: $(4,2,1)$, $(3,3,1)$, $(3,2,2)$
- n=8: $(5,2,1)$, $(4,3,1)$, $(4,2,2)$, $(3,3,2)$

(The length-3 partitions $(4,1,1)$, $(5,1,1)$, $(6,1,1)$ are hooks and
are excluded by definition; this corrects the brief's conjectured
2+3+5=10 squares / 177 rows to the true 9 squares / 155 rows.)

For $V = S^\lambda$ with character $\chi^\lambda$ and $w \in S_n$ of cycle
type $C$ with class size $|C|$, with $C^2$ the cycle type of $w^2$
(odd $L \mapsto (L)$; even $L \mapsto (L/2,L/2)$):

- $g(\lambda,\lambda,\nu) = \frac{1}{n!}\sum_C |C|\,
  \chi^\lambda(C)^2 \chi^\nu(C)$ (Kronecker coefficient),
- $m(\nu) = \langle \chi^\lambda_{w^2}, \chi^\nu \rangle
  = \frac{1}{n!}\sum_C |C|\, \chi^\lambda(C^2)\chi^\nu(C)$,
- $s(\lambda,\nu) = (g+m)/2$ (multiplicity in $\mathrm{Sym}^2 V$),
- $a(\lambda,\nu) = (g-m)/2$ (multiplicity in $\mathrm{Alt}^2 V$).

## Result

(a) **Census.** All 155 triples $(s,a,g)$ (plus $m$) for the 9 squares
$\times$ all constituents ($22+45+88$ rows) are as tabulated in
`artifacts/splitting_tables.json`. Every row satisfies $s+a=g$ with
$s,a \ge 0$ integers, and per square with $d=\dim\lambda$:
$\sum g\cdot\dim = d^2$,
$\sum s\cdot\dim = d(d+1)/2$,
$\sum a\cdot\dim = d(d-1)/2$.

(b) **Maximal gap.** The maximal symmetric-vs-alternating gap in this
family is $G^* = \max|s-a| = \max|m| = 5$, attained uniquely at
$n=8$, $\lambda=(4,3,1)$, $\nu=(4,2,2)$ with
$(s,a,g,m)=(6,1,7,5)$ and power-map class sum
$\sum_C |C|\chi^{(4,3,1)}(C^2)\chi^{(4,2,2)}(C) = 5\cdot 8! = 201600$.
Per-degree maxima: 3 at n=6 ($((3,2,1),(4,2))=(3,0,3)$);
4 at n=7 ($((4,2,1),(5,2))=(4,0,4)$), each unique in its degree.

(c) **Staircase refined-Saxl row.** $(3,2,1)^2$ contains all 11 irreps
of $S_6$ ($g \ge 1$ throughout), and $s \ge 1$ for all 11 (the symmetric
part alone already contains everything):
$(6)$:$(1,0,1)$; $(5,1)$:$(2,0,2)$; $(4,2)$:$(3,0,3)$;
$(4,1,1)$:$(1,3,4)$; $(3,3)$:$(1,1,2)$; $(3,2,1)$:$(3,2,5)$;
$(3,1^3)$:$(1,3,4)$; $(2^3)$:$(2,0,2)$; $(2^2,1^2)$:$(1,2,3)$;
$(2,1^4)$:$(1,1,2)$; $(1^6)$:$(1,0,1)$.

## Proof / evidence

From-scratch Murnaghan–Nakayama tables for $S_6/S_7/S_8$ (rim-hook
recursion) with hook-length dimension check, $\sum \dim^2 = n!$,
and full row orthogonality (`compute.py`); $g$ by class-algebra inner
product and $m$ by the committed $w \mapsto w^2$ power map, with
integrality, parity, and nonnegativity enforced per row.
Independent replay (`verify.py`): second MN implementation removing
the smallest class part first (different recursion path), exact
divisibility of both class sums by $n!$, full column orthogonality,
transpose symmetry $\chi^{\lambda^t}(C)=\mathrm{sgn}(C)\chi^\lambda(C)$,
and byte-comparison of all 155 $(s,a,g,m)$ rows — ALL VERIFY_OK.
Audit re-ran the replay (22+45+88 VERIFY_OK) and reproduced all rows
plus headline values with a third independent MN implementation.

## Limitations

- Exact census only for $n=6,7,8$ non-hook three-row squares (155 rows);
  no general formula claimed.
- Maximality ($G^*=5$) is within this 9-square family only, not over
  all of $S_8$.
- No 2-modular or multiplicity-free consequences derived; downstream
  use is conjectural.
- Splitting reuses character data shared with unsplit censuses;
  novelty rests on the power-map refinement for this family.

## Reproducibility

- `python3 artifacts/compute.py` — builds tables, derives census,
  writes `splitting_tables.json`.
- `python3 artifacts/verify.py` — independent re-derivation and
  certificate (prints VERIFY_OK lines).

## References

- S. Mészáros, J. Wolosz, Symmetric and Exterior Squares of Hook
  Representations, arXiv:1909.07489.
- C. Bessenrodt, C. Bowman, Splitting Kronecker squares,
  2-decomposition numbers, Catalan Combinatorics, and the Saxl
  conjecture, arXiv:2202.03066.
- I. Pak, G. Panova, E. Vallejo, Kronecker products, characters,
  partitions, and the tensor square conjectures, arXiv:1304.0738.
- C. Zhao, On the Kronecker product of Schur functions of square
  shapes, arXiv:2309.00764.
