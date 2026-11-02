# The complete complex and real flex divisor of the Chebyshev plane curves

## Finding

For every integer \(d\ge 4\), set \(f_d(x)=2T_d(x/2)\), the monic Chebyshev polynomial characterized by \(f_0=2\), \(f_1=x\), and \(f_{d+1}=x f_d-f_{d-1}\). Let \(C_d\subset\mathbb P^2_{\mathbb C}\) be the smooth degree-\(d\) plane curve
\[
F_d(X,Y,Z)=Y^d-Z^d f_d(X/Z)=0.
\]
Its complete inflection locus consists of two disjoint classes:

1. The \(d\) points \([\alpha:0:1]\), with \(f_d(\alpha)=0\), are all real and each has tangent-line contact exactly \(d\), hence inflection weight \(d-2\).
2. There are exactly \(2d(d-2)\) further, ordinary inflections. The \(x\)-coordinates of these points are precisely the distinct roots of
\[
G_d(x)=d f_d(x)f_d''(x)-(d-1)f_d'(x)^2.
\]
This is a degree-\(2d-4\) squarefree polynomial, with no real zeros and no common zero with \(f_d\). Over each root of \(G_d\) there are exactly \(d\) points of \(C_d\), all ordinary flexes.

There are no inflections at infinity. In particular, the number of distinct complex inflection points is \(d(2d-3)\), exactly \(d\) of them are real, and the real inflection divisor has weight \(d(d-2)\). The complete complex inflection weight is \(3d(d-2)\).

## Assumptions and scope

All assertions are over \(\mathbb C\), with the displayed real structure and integer \(d\ge4\). An ordinary inflection is a smooth point with tangent contact exactly three; the inflection weight of a point with tangent contact \(m\) is \(m-2\). The model is the canonical plane closure given by \(F_d=0\), not another projective embedding. The polynomial \(f_d\) has exactly \(d\) distinct real roots
\[
\alpha_j=2\cos\!\left(\frac{(2j-1)\pi}{2d}\right),\qquad 1\le j\le d.
\]
The coordinate chart \(Z\ne0\) is identified with \((x,y)=(X/Z,Y/Z)\).

## Proof

**Smoothness and homogeneity.** Since the roots of \(f_d\) are simple, the equation \(y^d=f_d(x)\) is smooth at \(y=0\) by \(F_x=-f_d'(x)\), and elsewhere by \(F_y=d y^{d-1}\). At \(Z=0\), the equation is \(Y^d=X^d\), giving exactly \(d\) distinct points \([1:\zeta:0]\), \(\zeta^d=1\), each smooth because the derivative with respect to \(X\) is nonzero. Thus \(C_d\) is smooth.

**Hessian factorization and degree.** Put \(\Phi_d(X,Z)=Z^d f_d(X/Z)\). Differentiating the binary form gives
\[
\Phi_{XX}\Phi_{ZZ}-\Phi_{XZ}^2=(d-1)Z^{2d-4}\bigl(d f_df_d''-(d-1)(f_d')^2\bigr)(X/Z).
\]
The ternary Hessian determinant of \(F_d=Y^d-\Phi_d\) therefore factors exactly as
\[
\operatorname{Hess}(F_d)=d(d-1)^2Y^{d-2}\,G_d^{\mathrm{hom}}(X,Z),
\qquad G_d^{\mathrm{hom}}=Z^{2d-4}G_d(X/Z).
\]
For \(d\ge4\), the recurrence gives \(f_d(x)=x^d-dx^{d-2}+\cdots\). The coefficient of \(x^{2d-4}\) in \(G_d\) is \(-2d^2\), so \(\deg G_d=2d-4\). In particular, \(G_d^{\mathrm{hom}}(1,0)=-2d^2\ne0\). Because the points of \(C_d\) at infinity also have \(Y\ne0\), the Hessian has no zero there.

**No overlap and no real roots.** If \(\alpha\) is a root of \(f_d\), then \(G_d(\alpha)=-(d-1)f_d'(\alpha)^2\ne0\). For real \(t\) not a root of \(f_d\), write \(u_j=(t-\alpha_j)^{-1}\). Logarithmic differentiation yields
\[
\frac{G_d(t)}{f_d(t)^2}=
\left(\sum_{j=1}^d u_j\right)^2-d\sum_{j=1}^d u_j^2
=-\sum_{1\le i<j\le d}(u_i-u_j)^2<0.
\]
Every pair \(u_i,u_j\) is distinct because the \(\alpha_j\) are. At any \(\alpha_j\), the preceding explicit expression for \(G_d(\alpha_j)\) is negative as well. Hence \(G_d\) has no real root.

**Squarefreeness.** The Chebyshev differential equation and its derivative are
\[
(x^2-4)f_d''+xf_d'-d^2f_d=0,
\qquad
(x^2-4)f_d'''+3xf_d''+(1-d^2)f_d'=0.
\]
Suppose \(a\in\mathbb C\) were a multiple root of \(G_d\). Then \(G_d(a)=G_d'(a)=0\). Write \(u=f_d(a)\), \(v=f_d'(a)\), \(w=f_d''(a)\). Both \(u\) and \(v\) are nonzero: if \(u=0\), the simple-root property gives \(G_d(a)\ne0\); if \(v=0\), then \(G_d(a)=0\) forces \(w=0\), contradicting the differential equation \(d^2u=0\). From \(G_d(a)=0\),
\[
duw=(d-1)v^2.
\]
Differentiation gives \(G_d'(a)=duf_d'''(a)-(d-2)vw=0\). Substitute both Chebyshev equations into this identity after multiplication by \(a^2-4\). Direct cancellation yields
\[
(2d-1)v(du-av)=0.
\]
Thus \(av=du\). Now the first Chebyshev equation yields \((a^2-4)w=d(d-1)u\); combined with \(duw=(d-1)v^2\) it follows that \((a^2-4)v^2=d^2u^2\). But \(av=du\) implies \(a^2v^2=d^2u^2\), hence \(4v^2=0\), a contradiction. Therefore every root of \(G_d\) is simple.

**Inflection weights.** Over a zero \(a\) of \(G_d\), the value \(f_d(a)\ne0\) gives precisely \(d\) distinct points, all with \(y\ne0\); \(x\) is a local parameter at each. The factor \(G_d^{\mathrm{hom}}\) vanishes simply and \(Y^{d-2}\) does not vanish, so the Hessian intersection multiplicity is one. For a smooth complex plane curve, this is the tangent-line contact order minus two. These are therefore ordinary inflections. Over a zero \(\alpha\) of \(f_d\), \(y\) is a local parameter and the Hessian vanishes to order \(d-2\), while the tangent \(x=\alpha\) has intersection multiplicity \(d\), as one sees directly from \(x-\alpha\sim y^d/f_d'(\alpha)\). The remaining infinity points are not Hessian points. The total weight is
\[
 d(d-2)+d(2d-4)=3d(d-2),
\]
in agreement with Bézout's intersection degree of \(C_d\) and its Hessian. The strict negativity of \(G_d\) over \(\mathbb R\) shows that the only real inflections are the \(d\) hyperflexes.

## Verification

The included standard-library script `verify.py` checks, for each integer \(4\le d\le24\), the Chebyshev recurrence, differential equation, degree and leading coefficient of \(G_d\), the coprimality of \(G_d\) with its derivative and \(f_d\) modulo the prime 1,000,003, real negativity at integer test points, and the resulting inflection-count identities. Executing `python verify.py` prints `VERIFY_OK`. The modular gcd checks are only finite consistency tests; the proof above establishes the all-degree squarefreeness over \(\mathbb C\).

## Relationship to prior work

Tafazolian and Top, *Automorphisms of Plane Curves defined from Chebychev polynomials* (arXiv:2505.01216v1, §2, Proposition 2.1), classify **total** inflection points of precisely these plane curves. Their result supplies the already-known \(d\) total inflections over characteristic zero; it does not state the remaining ordinary-inflection count, explicit squarefree Hessian factor, all-nonreal coordinate assertion or complete inflection divisor. The present theorem retains that prior attribution and derives the additional strata.

Cotterill, Darago, Garay López, Han and Shaska, *Arithmetic inflection of superelliptic curves* (arXiv:2110.04813v2), develop general inflection techniques. Their explicit one-point-at-infinity basis in §2.1 assumes the covering exponent and polynomial degree are coprime; here they coincide. Their general framework motivates comparison but does not supply the concrete Chebyshev Hessian root analysis. The global inflection weight \(3d(d-2)\) is classical, not claimed new; only its detailed geometric distribution is assessed here.

## Limitations

The theorem is proved in characteristic zero for this particular smooth plane realization. It does not claim analogous root geometry in positive characteristic, where the Hessian may behave differently, nor classify tangential bitangencies or the full dual-curve singularities. The primary-text comparison and focused literature searches support a provisional novelty assessment, not a proof that no earlier equivalent formulation exists. No independent mathematical review has been carried out.

## References

- S. Tafazolian and J. Top, *Automorphisms of Plane Curves defined from Chebychev polynomials*, arXiv:2505.01216v1 (first public: 2025-05-02), https://arxiv.org/html/2505.01216v1 , especially §2, Proposition 2.1.
- E. Cotterill, I. Darago, C. Garay López, C. Han and T. Shaska, *Arithmetic inflection of superelliptic curves*, arXiv:2110.04813v2, https://arxiv.org/html/2110.04813v2 , especially §2.1 and §3.
- Classical Hessian inflection criterion and Bézout intersection formula for smooth complex plane curves (standard background).
