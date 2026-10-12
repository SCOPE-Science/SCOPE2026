# Center of every finite Nottingham truncation
## Finding
Let \(p\) be a prime and \(n\ge2\). Let \(G_n(p)\) be the finite Nottingham truncation consisting of
\[
f(x)=x+a_2x^2+\cdots+a_nx^n\qquad(a_i\in\mathbf F_p),
\]
with multiplication by substitution modulo \(x^{n+1}\). For \(1\le r<n\), let \(H_r\) be the image of the filtration subgroup of series congruent to \(x\) modulo \(x^{r+1}\). Then
\[
Z(G_n(p))=
\begin{cases}
H_{n-2},& p\mid(n-3),\\
H_{n-1},& p\nmid(n-3).
\end{cases}
\]
Equivalently, the center has order \(p^2\) exactly when \(n\equiv3\pmod p\), and otherwise it has order \(p\). In the congruence case the center contains exactly the two highest coefficient layers; otherwise it contains only the highest layer.

## Assumptions and scope
The statement is for every prime \(p\) and every integer \(n\ge2\). The indexing is normalized so that \(H_r\) consists of truncated series whose first possible nonlinear term has degree \(r+1\). No restriction on odd characteristic is used. The case \(n=2\) gives the cyclic group of order \(p\), and the case \(n=3\) gives an abelian group of order \(p^2\), both consistent with the formula.

## Proof
Take two nonidentity filtered series with first nonlinear terms
\[
f=x+a_rx^r+O(x^{r+1}),\qquad g=x+b_sx^s+O(x^{s+1}),
\]
where \(r,s\ge2\) and \(a_rb_s\ne0\). Expanding the two compositions through degree \(r+s-1\) gives
\[
f\circ g-g\circ f=(r-s)a_rb_sx^{r+s-1}+O(x^{r+s}).
\]
Passing from this difference to the group commutator gives the same first nonzero coefficient, so
\[
[f,g]=x+(r-s)a_rb_sx^{r+s-1}+O(x^{r+s}).
\]
This reconstructs the filtration commutator formula used in the recent power-commutator analysis.

First, \(H_{n-1}\) is central because every commutator with a series beginning in degree \(n\) starts beyond degree \(n\). Now suppose \(p\mid(n-3)\). If \(h\in H_{n-2}\), its only potentially visible interaction comes from a degree-\(n-1\) leading term against a degree-\(2\) leading term; its degree-\(n\) coefficient is a scalar multiple of \(n-3\), hence vanishes in \(\mathbf F_p\). All other possible commutator terms have degree at least \(n+1\). Therefore \(H_{n-2}\subseteq Z(G_n(p))\).

Conversely, let \(f\notin H_{n-2}\), and let \(r\le n-2\) be the degree of its first nonlinear term. If \(p\nmid(r-2)\), compare \(f\) with \(x+x^2\); the commutator has nonzero degree-\(r+1\) coefficient \((r-2)a_r\). If \(p\mid(r-2)\), compare instead with \(x+x^3\); the degree-\(r+2\) coefficient is \((r-3)a_r=-a_r\ne0\), and \(r+2\le n\). Thus no element below \(H_{n-2}\) is central.

Finally suppose \(p\nmid(n-3)\). Any element of \(H_{n-2}\setminus H_{n-1}\) has a nonzero degree-\(n-1\) coefficient; commuting it with \(x+x^2\) produces the nonzero degree-\(n\) coefficient \((n-3)a_{n-1}\). Hence only \(H_{n-1}\) remains central. This proves the formula in all cases.

## Verification
The symbolic proof is uniform in \(p\) and \(n\); finite computation is used only as an independent sanity check. The accompanying exact enumerator constructs the substitution law directly and exhaustively computes centers for \(p=2\) with \(2\le n\le7\), \(p=3\) with \(2\le n\le6\), and \(p=5\) with \(2\le n\le5\). Every case agrees with the theorem, including each congruence jump, and the replay ends with `CHECK_OK`.

## Relationship to prior work
Szechtman's recent preprint introduces the same groups \(G_n(p)\), gives the leading commutator coefficient used above, and determines a power-commutator presentation through the truncation level \(15\). The paper does not state the center formula above. Earlier work of Johnson studies the lower central series and nilpotency class, while Sangroniz and Pálfy study conjugacy classes in natural Nottingham quotients and Klopsch studies normal subgroups of substitution groups. Searches for the exact center formula and its congruence jump did not locate a covering statement. A nearby result on the natural truncated Nottingham brace computes its socle filtration; that invariant is different and does not imply the center formula, since when \(n\equiv3\pmod p\) the multiplicative center has two coefficient layers rather than one.

## Limitations
The result concerns the finite truncations over prime fields, not the center of the full pro-\(p\) Nottingham group or truncations over arbitrary finite coefficient fields. The literature comparison included the recent source in full and targeted searches of older Nottingham-quotient literature, but one plausible older conjugacy-class source and one normal-subgroup source were not available as full text during the comparison. The exact center statement may therefore have an unlocated older equivalent formulation; this is the principal residual originality risk.

## References
1. Fernando Szechtman, *A power-commutator presentation for the group of truncated polynomials under substitution*, arXiv:2610.01469v1, first public 2026-10-01. Primary MSC 20D15.
2. D. L. Johnson, *The group of formal power series under substitution*, Journal of the Australian Mathematical Society 45 (1988), 296–302.
3. J. Sangroniz, *Conjugacy classes and characters in some quotients of the Nottingham group*, Journal of Algebra 211 (1999), 26–41, DOI 10.1006/jabr.1998.7588.
4. P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, Proceedings of the Edinburgh Mathematical Society 41 (1998), 369–384, DOI 10.1017/S0013091500019714.
5. B. Klopsch, *Normal subgroups in substitution groups of formal power series*, Journal of Algebra 228 (2000), 91–106, DOI 10.1006/jabr.1999.8219.
