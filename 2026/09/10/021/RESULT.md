# Reflected Lascoux expansion of the minimal non-vexillary permutation w* = 2143

## Context

Lascoux polynomials $\mathfrak L_\alpha$ are inhomogeneous analogues of key
polynomials. Setiabrata-St. Dizier (arXiv:2410.08038) prove, via double
orthodontia, that for vexillary (2143-avoiding) permutations $w$ the reflected
double Schubert polynomial
$x_1^n \cdots x_n^n \, \mathfrak S_w(x_n^{-1},\dots,x_1^{-1};1,\dots,1)$
is a graded nonnegative sum of Lascoux polynomials (Theorem 1.2 /
Corollary 1.3), and conjecture the same for all $w$ (Conjecture 1.4, following
from the product Conjecture 1.5). Their text exhibits no expansion for the
forbidden pattern itself, $w^\star=2143$, the canonical first case beyond the
proven domain. This record certifies exactly that base case.

## Definitions

Work in $S_4$ with $x=(x_1,x_2,x_3,x_4)$, $y=(y_1,y_2,y_3,y_4)$.
For $i=1,2,3$: $\partial_i(f)=(f-s_if)/(x_i-x_{i+1})$,
$\bar\partial_i(f)=\partial_i((1-x_{i+1})f)$,
$\bar\pi_i(f)=\bar\partial_i(x_i f)$.
Double Schubert: $\mathfrak S_{w_0}=\prod_{i+j\le 4}(x_i-y_j)$ for $w_0=4321$,
$\mathfrak S_v=\partial_i\mathfrak S_w$ when $v=ws_i$, $\ell(v)=\ell(w)-1$.
Lascoux: $\mathfrak L_\alpha=x^\lambda$ if $\alpha=\lambda$ weakly decreasing,
$\mathfrak L_\alpha=\bar\pi_i\mathfrak L_{\alpha\cdot s_i}$ if
$\alpha_i<\alpha_{i+1}$ (well defined by braid relations).
Reflected: $R_w(x)=x_1^4x_2^4x_3^4x_4^4\,
\mathfrak S_w(x_4^{-1},x_3^{-1},x_2^{-1},x_1^{-1};1,1,1,1)$.
A sum $\sum c_\alpha\mathfrak L_\alpha$ is graded nonnegative if every
$c_\alpha\ge 0$ and the sign $(-1)^{|\alpha|-d_0}$ is constant on each degree,
$d_0$ the lowest total degree.

## Result

Let $w^\star=2143$ and $d_0=14$. Then

$$R_{2143} = (\mathfrak L_{4343}+\mathfrak L_{4442})
-(\mathfrak L_{4344}+2\,\mathfrak L_{4443})+\mathfrak L_{4444},$$

i.e. $(\alpha,c_\alpha)$: $(4343,1)$, $(4442,1)$, $(4344,1)$, $(4443,2)$,
$(4444,1)$, all $c_\alpha$ positive integers, graded signs $+,-,+$ on degrees
$14,15,16$.

## Proof / evidence

Exact machine-verified computation from the definitions:

1. Descending divided differences from $\mathfrak S_{4321}$ give
$\mathfrak S_{2143}=x_1^2+x_1x_2+x_1x_3-2x_1y_1-x_1y_2-x_1y_3-x_2y_1-x_3y_1
+y_1^2+y_1y_2+y_1y_3$, so at $y=1$:
$x_1^2+x_1x_2+x_1x_3-4x_1-x_2-x_3+3$.
2. Simultaneous reflection $x_i\mapsto x_{5-i}^{-1}$ times
$x_1^4x_2^4x_3^4x_4^4$ gives the 7-term
$R_{2143}=3x^{4444}-4x^{4443}+x^{4442}-x^{4434}+x^{4433}-x^{4344}+x^{4343}$.
3. Demazure-Lascoux recursion gives:
$\mathfrak L_{4343}=x^{4433}-x^{4443}+x^{4343}$,
$\mathfrak L_{4442}=x^{4442}$,
$\mathfrak L_{4344}=-2x^{4444}+x^{4443}+x^{4434}+x^{4344}$,
$\mathfrak L_{4443}=x^{4443}$, $\mathfrak L_{4444}=x^{4444}$.
4. Subtracting the graded combination from $R_{2143}$ gives the zero
polynomial (exact cancellation of all 7 monomials); lowest degree
$d_0=14$; degree-14 atoms enter with $+$, degree-15 with $-$, degree-16
with $+$, all $c_\alpha\in\{1,2\}$.

The independent checker `artifacts/verify.py` recomputes steps 1-4 from the
definitions (stdlib + SymPy) and prints `VERIFY_OK`. Audit re-ran it:
`VERIFY_OK`, and cross-checked double-at-$y=0$ against the ordinary Schubert
chain (both $x_1^2+x_1x_2+x_1x_3$) plus descent-path consistency.

Orthodontia audit trail: $D(2143)=\{(1,1),(3,3)\}$; staged reflection replay
reconstructs the same $R_{2143}$, with the second $\varphi_3$ step outside the
vexillary Proposition 4.11 hypothesis — context only, not load-bearing.

## Limitations

Proves only the $w^\star=2143$ base case, not the full single-2143 cell
theorem (all exactly-one-2143 $w$), which remains open; documented blockers
include a false generic commutation identity and sort-predecessor leakage out
of the cell. The $S_5$ graded-peeling solves for all 11 single-2143
permutations are supporting evidence only.

## Reproducibility

`python3 artifacts/verify.py` prints `VERIFY_OK` (SymPy required; seconds).

## References

- L. Setiabrata, A. St. Dizier, Double orthodontia formulas and Lascoux positivity, arXiv:2410.08038.
- Y. Chen, N. J. Y. Fan, Z. Ye, Zero-one Grothendieck Polynomials, arXiv:2405.05483.
- G. Orelowitz, T. Yu, Lascoux expansion of the product of a Lascoux and a stable Grothendieck, arXiv:2312.01647.
