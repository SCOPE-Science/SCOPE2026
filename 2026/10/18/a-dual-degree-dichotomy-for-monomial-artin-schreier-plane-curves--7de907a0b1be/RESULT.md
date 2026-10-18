# A dual-degree dichotomy for monomial Artin--Schreier plane curves

## Finding
Let \(k\) be algebraically closed of characteristic \(p>0\), with \(p\) prime, and let \(m>p\) be coprime to \(p\). The integral plane curve \(C_{p,m}\) defined by
\[Y^pZ^{m-p}-YZ^{m-1}-X^m=0\]
has projective dual degree
\[\boxed{\deg C_{p,m}^{\vee}=\begin{cases}m,&m\equiv1\pmod p,\\pm,&m\not\equiv1\pmod p.\end{cases}}\]
Its Gauss map has degree \(p\), purely inseparable, in the first case and degree \(1\), separable, in the second. In particular, \((p,m)=(3,5)\) has dual degree \(15\), whereas \((3,7)\) has dual degree \(7\), despite both arising from monomial Artin--Schreier covers.

## Assumptions and scope
All curves and duals are geometric, over the algebraically closed field \(k\). The dual means the reduced closure of tangent lines to the smooth locus. The affine chart \(Z=1\) is \(y^p-y=x^m\). The hypotheses \(m>p\) and \(p\nmid m\) are essential to the plane model and proof below. We do not claim a classification for arbitrary Artin--Schreier polynomials or the scheme structure of the dual.

## Proof
**Irreducibility and points at infinity.** The rational function \(x^m\) has a pole of order \(m\) at infinity on \(\mathbb P^1\). Because \(p\nmid m\), it cannot equal \(h^p-h\) for \(h\in k(x)\): the pole order of any such difference is either zero or divisible by \(p\). Thus \(T^p-T-x^m\) is irreducible over \(k(x)\) by Artin--Schreier theory; the projective curve is integral. Its affine portion is smooth, since the derivative with respect to \(y\) is \(-1\). The only point at infinity is \([0:1:0]\).

**The polar contribution at infinity.** Work in the chart \(Y=1\) with coordinates \(x=X/Y\), \(z=Z/Y\), and write \(a=m-p\ge1\). The germ has equation
\[f=z^a-z^{m-1}-x^m=z^a(1-z^{p-1})-x^m.\]
The factor in parentheses is a unit. Since \(\gcd(a,m)=\gcd(p,m)=1\), this is a unibranch germ with normalization valuations \(\operatorname{ord}(x)=a\) and \(\operatorname{ord}(z)=m\). For \(a=1\) the point is smooth. The projective derivatives in this chart are
\[F_X=-m x^{m-1},\quad F_Y=-z^{m-1},\quad F_Z=a z^{a-1}-(m-1)z^{m-2}.\]
A generic polar is \(\lambda F_X+\mu F_Y+\nu F_Z\) with \(\nu\ne0\). Its pullback to the normalization has smallest order \(m(a-1)\): this is the leading term \(\nu a z^{a-1}\) of \(F_Z\), while the orders of \(F_X\) and \(F_Y\) are \(a(m-1)\) and \(m(m-1)\), both strictly larger for \(p>0\). Consequently its intersection multiplicity with \(C\) at infinity is \(m(m-p-1)\). There are no other singular points or polar base points. A general polar has degree \(m-1\), so Bézout gives the generic polar divisor on the affine smooth locus degree
\[m(m-1)-m(m-p-1)=mp.\]
By the projection formula for the Gauss map, this equals \(\deg(\gamma)\deg(C^\vee)\).

**The Gauss degree.** On \(Z=1\), use affine coordinates on the dual chart given by
\[u=F_X/F_Y=m x^{m-1},\qquad v=-F_Z/F_Y=y+m x^m.\]
Differentiating \(y^p-y=x^m\) yields \(dy=-m x^{m-1}dx\), hence
\[du=m(m-1)x^{m-2}dx,\qquad dv=m(m-1)x^{m-1}dx.\]
If \(m\not\equiv1\pmod p\), the differential \(du\) is nonzero and \(dv/du=x\). This derivative lies in the function field \(k(u,v)\), so \(x\in k(u,v)\) and then \(y=v-mx^m\in k(u,v)\). Thus the Gauss map is separable and birational.

If \(m\equiv1\pmod p\), write \(m=kp+1\). Then in characteristic \(p\), the same coordinates become
\[u=(x^k)^p,\qquad v=y+x^m=y^p.\]
The rational map \((x,y)\mapsto(x^k,y)\) is birational onto its image: \(x=(y^p-y)/(x^k)^p\). Therefore the Gauss map is its composition with the absolute Frobenius on an integral curve, and has purely inseparable degree exactly \(p\). Dividing the polar degree \(mp\) by the corresponding Gauss degree proves the displayed dual-degree formula.

## Verification
An independent exact symbolic check of the small cases is provided as `verify_as_dual.py`. It eliminates the parameter \(x\) from the affine Gauss coordinates over prime fields and checks the resultant's total degree. In the inseparable cases it verifies the predicted Frobenius powers. The test cases are \((p,m)=(2,5),(3,5),(3,7)\), with dual degrees \(5,15,7\), respectively. These computations corroborate, but do not replace, the all-parameter valuation and function-field proof.

## Relationship to prior work
Artin--Schreier covers and their genus and ramification structure are classical; Pries--Zhu study their moduli and \(p\)-rank strata. General positive-characteristic Gauss-map duality is studied by Furukawa. Fukasawa--Miura study Galois points on plane curves and their duals in characteristic zero, a distinct comparison. Komeda studies inseparable Gauss maps of a different family of smooth degree-\(q^2+q+1\) curves. The present calculation combines the explicit singular polar contribution of the monomial plane model with a sharp, congruence-controlled inseparable Gauss degree. It does not claim that the generic polar-degree identity or Frobenius factorization is new in isolation. Equivalent formulations in other plane-curve or Artin--Schreier literature remain a risk.

## Limitations
The conclusion is about the **reduced projective dual**. No claim is made about the scheme of inflectionary tangents, dual singularities, \(p\)-rank, supersingularity, or finite-field rational points. The case \(p\mid m\) is excluded: the plane equation then changes its Artin--Schreier normal form. The calculation does not establish novelty against every uncatalogued source.

## References
1. R. Pries and H. J. Zhu, *The p-rank stratification of Artin--Schreier curves*, arXiv:math/0609657 (first public 2006-09-22), https://arxiv.org/abs/math/0609657.
2. K. Furukawa, *Duality with expanding maps and shrinking maps, and its applications to Gauss maps*, arXiv:1110.4841 (first public 2011-10-21), https://arxiv.org/abs/1110.4841.
3. S. Fukasawa and K. Miura, *Galois points for a plane curve and its dual curve*, Rend. Sem. Mat. Univ. Padova 132 (2014), 61--74, DOI:10.4171/RSMUP/132-5.
4. K. Komeda, *Singularities of the dual curve of a certain plane curve in positive characteristic*, arXiv:2002.10691 (2020; a supporting comparison, not an archive anchor), https://arxiv.org/abs/2002.10691.
