# Exact zeta correction and singular-point Frobenius distribution for Howe sextics

## Finding
Let \(k=\mathbb F_q\), where \(q\) is odd. Let \(\phi_1,\phi_2\in k[x]\) be monic squarefree quartics with eight distinct roots between them, and suppose \(h=\phi_1-\phi_2\) has degree \(3\). Write \(C\) for the irreducible plane sextic
\[
 y^4-2(\phi_1(x)+\phi_2(x))y^2+h(x)^2=0
\]
and \(H\) for its smooth genus-five normalization, the fiber product \(u^2=\phi_1(x)\), \(v^2=\phi_2(x)\) with \(y=u+v\). Let \(\mathcal O\) run through Frobenius orbits of **distinct** roots of \(h\) in \(\bar k\). For \(\xi\in\mathcal O\) write \(d_\mathcal O=|\mathcal O|\), and let \(\varepsilon_\mathcal O\in\{\pm1\}\) be the quadratic character of \(\phi_1(\xi)=\phi_2(\xi)\) in \(\mathbb F_{q^{d_\mathcal O}}^\times\). The exact zeta correction is
\[
 \boxed{\frac{Z(C/\mathbb F_q,T)}{Z(H/\mathbb F_q,T)}=(1-T)\prod_{\mathcal O}(1-\varepsilon_\mathcal O T^{d_\mathcal O}).}
\]
This includes repeated-root cubic degenerations without change of formula. In particular, for all \(n\ge1\),
\[
 \#C(\mathbb F_{q^n})-\#H(\mathbb F_{q^n})=-1-\sum_{\mathcal O:\ d_\mathcal O\mid n}d_\mathcal O\varepsilon_\mathcal O^{n/d_\mathcal O}.
\]
In the specialization \(\phi_1=x(x-1)(x-2)(x-5)\), \(\phi_2=(x-3)(x-4)(x-6)(x-7)\), the cubic \(h/4=3x^3-32x^2+110x-126\) has Galois group \(S_3\). Outside finitely many bad primes, the singular plane model has respectively \(1\), \(2\), or \(4\) rational singular points, on sets of rational primes of natural densities \(1/3\), \(1/2\), or \(1/6\).

The analytic ADE classification of the same complex sextics is established in earlier related work and is used below solely to identify the relevant branches; the new conclusion concerns the arithmetic zeta quotient and Frobenius distribution, not a renewed singularity-basket discovery.

## Assumptions and scope
The base field has characteristic different from \(2\). All geometric singularity assertions are after extension to an algebraic closure. The assumptions on the quartics mean their eight roots are pairwise distinct. The condition \(\deg h=3\) is equivalent to the nonvanishing difference of the cubic coefficients of the two monic quartics. In the zeta identity, a Frobenius orbit contains distinct geometric zeros only: multiplicities of roots affect the analytic type, not the number of branches. \(Z(X/\mathbb F_q,T)=\exp(\sum_{n\ge1}\#X(\mathbb F_{q^n})T^n/n)\) denotes the Hasse–Weil zeta function of the indicated (possibly singular) projective curve.

## Proof
**Normalization and integrality.** The square classes of \(\phi_1\) and \(\phi_2\) in \(\bar k(x)^\times/\bar k(x)^{\times2}\) are independent: a zero of one quartic is not a zero of the other and has odd valuation. Their compositum therefore has degree \(4\) over \(\bar k(x)\). For \(y=u+v\), elimination yields the displayed quartic equation in \(y\), and conversely, where \(y\ne0\),
\[
 u=\frac{y^2+h}{2y},\qquad v=\frac{y^2-h}{2y}.
\]
Thus the plane equation is irreducible and its normalization is the smooth model \(H\) of that compositum. In the degree-four cover \(H\to\mathbb P^1\), the eight distinct roots of the two quartics are the only branch values, each contributing total ramification \(2\). Riemann–Hurwitz gives \(2g(H)-2=4(-2)+8\cdot2=8\), hence \(g(H)=5\).

**Finite singular points.** Put \(s=\phi_1+\phi_2\), \(f=y^4-2sy^2+h^2\). Then \(f_y=4y(y^2-s)\). At \(y=0\), \(f=0\) is equivalent to \(h=0\), and both first derivatives vanish. If \(y\ne0\) and \(f_y=0\), then \(y^2=s\). The equation \(f=0\) becomes \(-4\phi_1\phi_2=0\); moreover \(f_x=-4(\phi_1\phi_2)'\) there, nonzero because \(\phi_1\phi_2\) is squarefree. Hence there are no other finite singularities.

At a zero \(\xi\) of \(h\) of multiplicity \(r\), we have \(\phi_1(\xi)=\phi_2(\xi)=a\ne0\). In the completed local ring about \(\xi\), choose square roots \(U_i(x)=\sqrt{\phi_i(x)}\) with common constant \(\sqrt a\). The two roots of the plane quartic in \(y^2\) are \((U_1\pm U_2)^2\). The factor \(y^2-(U_1+U_2)^2\) is a unit at \((\xi,0)\), so the completed plane germ is equivalent to \(y^2-(U_1-U_2)^2\). As \(U_1-U_2=h/(U_1+U_2)\) vanishes to exact order \(r\), a formal coordinate change gives \(Y^2-t^{2r}=0\), namely type \(A_{2r-1}\). Its two normalization branches lie above \((\xi,0)\) at \((u,v)=(\pm\sqrt a,\mp\sqrt a)\).

**Infinity.** Let \(\Phi_i(X,Z)=Z^4\phi_i(X/Z)\) and \(H_3(X,Z)=Z^3h(X/Z)\), with leading coefficient \(c\ne0\). The homogeneous sextic is
\[
 F(X,Y,Z)=Y^4Z^2-2(\Phi_1+\Phi_2)Y^2+H_3^2.
\]
At \(Z=0\), \(F=X^4(c^2X^2-4Y^2)\). The two points \([1:\pm c/2:0]\) are smooth since \(F_Y=-8X^4Y\) there. The remaining point \(Q=[0:1:0]\) is singular. In local coordinates \(u=X/Y,v=Z/Y\), substitute \(v=u^2w\). The quotient \(F(u,1,u^2w)/u^4\) is a formal power series with initial term \(w^2-4\). Hensel's lemma (or the implicit function theorem for formal series) produces two branches \(v=u^2w_\pm(u)\) with \(w_\pm(0)=\pm2\). Both are smooth and rational over \(k\), and their difference has vanishing order exactly \(2\); this is the split tacnode \(A_3\). The four points of \(H\) above \(x=\infty\) are rational, because the quartics are monic, and exactly two lie over \(Q\), the other two mapping to the two smooth infinity points. This exhausts the projective singular locus.

**Finite-field zeta correction.** A rational normalization is an isomorphism away from these finitely many singular points. Above the rational tacnode \(Q\) sit two rational normalization points, giving the zeta quotient factor \((1-T)\). For an orbit \(\mathcal O\) of length \(d\), the singular point has degree \(d\). Its two normalization preimages are split into two degree-\(d\) points when \(\varepsilon_\mathcal O=+1\), and form one degree-\(2d\) point when \(\varepsilon_\mathcal O=-1\). The ratio of closed-point factors is respectively \(1-T^d\) or \(1+T^d\). Multiplication yields the formula; it is insensitive to the multiplicity of the root of \(h\), as required.

**Arithmetic example.** Direct expansion gives \(h=4g\), \(g=3x^3-32x^2+110x-126\). Its discriminant is \(-4460\), not a square, and its reduction modulo \(13\) is irreducible of degree \(3\), so \(\operatorname{Gal}(g/\mathbb Q)=S_3\). At primes outside the finite bad-reduction and discriminant set, the number of rational affine singular points equals the number of fixed roots of the Frobenius permutation in \(S_3\); the rational tacnode contributes one further singular point. Identity, transpositions and three-cycles have \(3\), \(1\) and \(0\) fixed roots and occupy proportions \(1/6\), \(1/2\), \(1/3\), respectively. Chebotarev's theorem proves the densities.

## Verification
The included standalone \(\texttt{verify.py}\) checks exact polynomial expansions, the cubic discriminant, irreducibility modulo \(13\), squarefreeness, and agreement of independent direct counts of the plane curve and the normalized fiber-product curve over nine small good finite fields with the predicted zeta-derived rational-point correction. The local singularity and full zeta identities are established by the written proof for all fields under the hypotheses, not by finite sampling. Run with \(\texttt{python3 verify.py}\); only the Python standard library is needed.

## Relationship to prior work
Kudo's *Explicit construction of a plane sextic model for genus-five Howe curves, II* (arXiv:2401.00760, first public 2024-01-01) derives the same plane equation and establishes geometric singular support, multiplicity two, and a classification by equality roots in the disjoint-branch elliptic construction. Those results do not specify the complete \(A_{2r-1}\) analytic types, the split tacnode branches, the finite-field normalization zeta quotient, or the exhibited \(S_3\) singularity-density specialization. Moriya–Kudo's earlier paper concerns a different genus-two double-cover construction, and generalized Howe Jacobian decompositions concern the smooth normalization rather than the stated correction for the singular plane model. The present contribution is the explicit finite-field branch-splitting zeta identity and the Galois prime-density specialization. The analytic singularity refinement has also been recorded previously and is not claimed as new.

## Limitations
The theorem requires pairwise distinct roots across the two quartics and a nonzero cubic term of their difference. The ADE basket computation in the proof supplies necessary local evidence for the arithmetic correction and is not claimed as new. It does not classify the other degree-of-difference strata or characteristics \(2\). The prime-density statement excludes finitely many bad primes and concerns singular \(\mathbb F_p\)-points of the plane model, not singularities of its normalization. The complete zeta function of the normalization is not evaluated; only its exact quotient with the plane model is determined. No claim of exhaustive bibliographic novelty or independent validation is made.

## References
1. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760, public 2024-01-01, especially its sextic equation and geometric singularity analysis.
2. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993 (different base-cover configuration).
3. T. Katsura and K. Takashima, *Decomposed Richelot isogenies and generalized Howe curves*, arXiv:2108.06936 (normalization-side Jacobian structure).
