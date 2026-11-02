# Universal Bergman norm and capacity defect on polynomial-lemniscate shells

## Finding
Let \(P\in\mathbb C[z]\) be **monic of degree** \(d\ge1\), and fix \(0\le r<R<\infty\). Consider the compact polynomial-lemniscate shell
\[
K_{r,R}(P)=\{z\in\mathbb C:r\le |P(z)|\le R\}.
\]
For **every** integer \(k\ge1\), put \(N=dk\). The unique monic polynomial of degree \(N-1\) orthogonal to every polynomial of smaller degree with respect to **unnormalized planar area** \(dA=dx\,dy\) restricted to \(K_{r,R}(P)\) is
\[
Q_{k,P}(z)=\frac{P'(z)P(z)^{k-1}}d,
\qquad
\int_{K_{r,R}(P)}|Q_{k,P}(z)|^2\,dA(z)
=\frac{\pi}{dk}(R^{2k}-r^{2k}).
\]
For the least-squares capacity bound of Ransford, define
\[
b_n(K)=\frac1{\sqrt{\pi n}}\inf_{p\text{ monic of degree }n}\|p'\|_{L^2(K)}.
\]
Then the polynomial-lemniscate shell obeys the **exact universal capacity-defect law**
\[
\boxed{\quad b_{dk}(K_{r,R}(P))=\sqrt{R^{2k}-r^{2k}},\qquad
\frac{b_{dk}(K_{r,R}(P))}{\operatorname{cap}(K_{r,R}(P))^{dk}}
=\sqrt{1-(r/R)^{2k}}.\quad}
\]
In particular, the bound is attained at every degree divisible by \(d\) when \(r=0\), for *every* monic polynomial \(P\), and becomes strictly deficient when \(0<r<R\). For \(0<r<R\) this deficit is exactly
\[
1-\frac{b_{dk}(K_{r,R}(P))}{\operatorname{cap}(K_{r,R}(P))^{dk}}
=\frac12(r/R)^{2k}+O((r/R)^{4k})\qquad(k\to\infty).
\]
The error is thus exponentially small, with a coefficient and exponent independent of the polynomial geometry. If \(\gamma_{dk-1}^{\rm shell}\) and \(\gamma_{dk-1}^{\rm filled}\) are the positive leading coefficients of the orthonormal area Bergman polynomials on the shell and filled set respectively, then
\[
\frac{\gamma_{dk-1}^{\rm shell}}{\gamma_{dk-1}^{\rm filled}}
=\left(1-(r/R)^{2k}\right)^{-1/2}.
\]

## Assumptions and scope
The polynomial \(P\) is monic, with arbitrary complex coefficients and any repeated critical points. Both radius levels may pass through critical values. The shell is understood as a closed set and is equipped with two-dimensional Lebesgue area; all asserted Hilbert-space orthogonality refers to the finite-dimensional polynomial subspaces of \(L^2(K_{r,R}(P),dA)\). Since \(r<R\) and \(P\) is nonconstant, the shell has positive area. There is no assumed connectedness or rotational symmetry; the preimage may contain several islands and holes. All formulas are exact for each \(k\ge1\).

## Proof
**1. Degree and monicity.** The leading terms of \(P\) and \(P'\) are respectively \(z^d\) and \(d z^{d-1}\). Hence \(Q_{k,P}=P^{k-1}P'/d\) is monic of degree \(dk-1\).

**2. Orthogonality.** First choose \(r,R\) so that their positive level curves contain no critical point of \(P\); the case \(r=0\) follows by a limit. For any polynomial \(f\) with \(\deg f\le dk-2\), complex Green's formula and the identity \(\partial_{\bar z}\overline{P(z)^k}=k\overline{P(z)^{k-1}P'(z)}\) give
\[
\int_{K_{r,R}(P)} f\,\overline{Q_{k,P}}\,dA
=\frac{1}{2i dk}\int_{\partial K_{r,R}(P)}f(z)\overline{P(z)^k}\,dz.
\]
At a level curve \(|P|=t>0\), one has \(\overline{P}^{\,k}=t^{2k}/P^k\). For the sublevel set \(E_t=\{|P|\le t\}\), the total positively oriented boundary integral therefore equals
\[
\int_{\partial E_t}\frac{f(z)}{P(z)^k}\,dz.
\]
All poles of this rational function lie inside \(E_t\), and it is \(O(z^{-2})\) at infinity because \(\deg f\le dk-2\). The residue at infinity is therefore zero, so the sum of its finite residues, and hence the boundary integral, is zero. Subtracting the two level contributions proves the asserted orthogonality. Arbitrary critical levels follow by approximating the levels with regular values, noting that the corresponding characteristic functions converge almost everywhere and all polynomial integrands are bounded on one fixed compact set. Thus the orthogonality is valid for all permitted \(r,R\).

**3. Norm by the polynomial area formula.** For every integrable radial function \(\varphi(w)=\varphi(|w|)\), the holomorphic polynomial \(P\) is \(d\)-to-one counting multiplicity at almost every target value; the real Jacobian is \(|P'|^2\). Consequently,
\[
\int_{K_{r,R}(P)}|P'(z)|^2|P(z)|^{2k-2}\,dA(z)
=d\int_{r\le|w|\le R}|w|^{2k-2}\,dA(w)
=\frac{d\pi}{k}(R^{2k}-r^{2k}).
\]
Dividing by \(d^2\) gives the norm of \(Q_{k,P}\). Since monic polynomials of each degree have a unique least-area-norm representative (positive definite Gram matrix), this orthogonal \(Q_{k,P}\) is precisely the minimizer.

**4. Least-squares index and capacity.** If \(n\ge1\), differentiation maps monic degree-\(n\) polynomials onto \(n\) times monic degree-\(n-1\) polynomials. Hence
\[
b_n(K)^2=\frac n\pi\inf_{q\text{ monic of degree }n-1}\int_K|q|^2\,dA.
\]
With \(n=dk\), the exact norm found above yields \(b_{dk}(K)^2=R^{2k}-r^{2k}\). The polynomial hull of \(K_{r,R}(P)\) is the filled outer lemniscate \(\{|P|\le R\}\), since the bounded complementary components are exactly those with \(|P|<r\); a polynomial lemniscate of monic degree \(d\) and level \(R\) has logarithmic capacity \(R^{1/d}\), by its exterior Green function \((\log|P(z)|-\log R)/d\). This proves the capacity identity and normalized ratio. The leading-coefficient comparison is the reciprocal norm comparison. Finally, \(1-\sqrt{1-u}=u/2+O(u^2)\) at \(u=(r/R)^{2k}\) proves the stated exponential defect. All statements also hold for \(d=1\).

## Verification
The argument is exact and does not rely on finite experiments. The standalone `CHECK.py` verifies polynomial monicity/degree and exact rational norm/capacity identities on finite representative families, including the circular special case. Its finite checks are supplementary; universal orthogonality is proved by residues, and universal norm normalization by the holomorphic change-of-variables formula. The formulas remain valid at critical levels by the indicated continuity argument.

## Relationship to prior work
Ransford (2026, Theorem 1.1) proved the general least-squares bound \(b_n(K)\le\operatorname{cap}(K)^n\) and described disk equality, but not the exact polynomial-shell norm and universal defect. Gustafsson–Putinar–Saff–Stylianopoulos (2008/2009, Proposition 7.2) identified a monic Bergman polynomial for the special **filled**, rotationally symmetric family \(|z^m-1|<r^m\); the formula above allows **every** monic \(P\) and both level boundaries. Saff–Stahl–Stylianopoulos–Totik (2014/2015, Theorem 2.1) proved asymptotic insensitivity of leading Bergman coefficients under removal of interior lakes; the exact ratio here refines that asymptotic in the natural nested-lemniscate case. Simanek (2013/2015) studied the Bergman shift and polynomial lemniscates, but its complete text was not retrievable for comparison; it is an explicit residual priority risk. These are statement-level comparisons, not assertions of exhaustive uniqueness.

## Limitations
The explicit identities hold on precisely nested polynomial-level shells and at degrees \(dk-1\) for the Bergman polynomial or \(dk\) for the capacity functional. Nothing is established for intermediate degrees, arbitrary excised holes, or general multiply connected domains. Reusing the polynomial-map change-of-variables argument in other classical orthogonal polynomial settings might reproduce analogous identities. The work is not independently validated, and originality remains subject to comparison with inaccessible older polynomial-lemniscate literature.

## References
1. T. Ransford, *A least-squares lower bound for capacity*, arXiv:2610.24702v1 (first public October 17, 2026), Theorems 1.1 and 1.2.
2. B. Gustafsson, M. Putinar, E. B. Saff and N. Stylianopoulos, *Bergman polynomials on an archipelago: Estimates, zeros and shape reconstruction*, arXiv:0811.1715v1 (November 11, 2008), Proposition 7.2.
3. E. B. Saff, H. Stahl, N. Stylianopoulos and V. Totik, *Orthogonal polynomials for area-type measures and image recovery*, arXiv:1403.6456v1 (March 25, 2014), Theorem 2.1.
4. B. Simanek, *The Bergman shift operator on polynomial lemniscates*, arXiv:1307.1941v2 (2013), abstract available; full text not inspected.
