# Sharp two-step finite-size law for squared areas of great-circle zero cells

## Finding

Let \(H_1,\ldots,H_n\) be independent, rotation-invariant random great circles of the unit sphere \(\mathbb S^2\), and let \(W_n\) be the almost surely unique cell containing an independent uniformly distributed point of \(\mathbb S^2\). Write \(A_n=\operatorname{area}(W_n)\) for unnormalized spherical area (unit-sphere steradians). Then, for integer \(n\to\infty\),
\[
\boxed{\mathbb E A_n^2=\frac{64\pi^6}{7n^4}\left[1-\frac{10}{n}+\frac{65-28\pi^2/11}{n^2}+O(n^{-3})\right].}
\]
Thus the third raw area power sum over cells obeys
\[
\mathbb E\sum_{C}\operatorname{area}(C)^3
=\frac{256\pi^7}{7n^4}\left[1-\frac{10}{n}+\frac{65-28\pi^2/11}{n^2}+O(n^{-3})\right].
\]
The curvature-specific contribution to the relative second correction is \(-28\pi^2/11\); the other part \(65\) comes from expanding the finite-count no-cut probability. A related consequence is \(\mathbb E A_n\sim2\pi^3/n^2\), so \(\mathbb E A_n^2/(\mathbb E A_n)^2\to16/7\), or a limiting squared coefficient of variation \(9/7\). The displayed second-order expansion, rather than the Poisson-limit scaling alone, is the principal assertion.

## Assumptions and scope

The great circles are unoriented and independently Haar-uniform. They partition the entire unit two-sphere, not a projective hemisphere, into spherical polygonal cells. A fresh Haar point chooses a cell with probability proportional to its area; this is a weighted typical cell, not a uniformly chosen cell. Areas are not divided by \(4\pi\). The assertion is an asymptotic expansion for arbitrary integers \(n\to\infty\), not an identity for fixed finite \(n\). Null events where the probe lies on a cutting circle do not affect the law.

## Proof

**1. An exact three-probe identity.** Fix a north pole \(N\); rotational invariance permits replacing the uniform base point by \(N\). If \(Y,Z\) are independent uniform *area-measure* probes on \(\mathbb S^2\), all three points lie in the same cell precisely when every random cutting circle misses their spherical convex triangle. For almost every triple its short-arc perimeter is
\(P(N,Y,Z)=d(N,Y)+d(Y,Z)+d(Z,N)\). The spherical Crofton formula states that a single independent uniform great circle intersects this triangle with probability \(P/(2\pi)\). Hence, with \(d\sigma\) denoting unnormalized spherical area,
\[
\mathbb E A_n^2=\int_{\mathbb S^2}\!\int_{\mathbb S^2}\left(1-\frac{P(N,Y,Z)}{2\pi}\right)^n\,d\sigma(Y)\,d\sigma(Z).
\tag{1}
\]
The integrand is nonnegative, since spherical triangle perimeters are at most \(2\pi\). The alternative identity \(4\pi\mathbb EA_n^2=\mathbb E\sum_C\operatorname{area}(C)^3\) follows by first conditioning on the tessellation and sampling the base point uniformly.

**2. Local curvature and binomial expansion.** In exponential coordinates at \(N\), put \(Y=\exp_N(u/n)\) and \(Z=\exp_N(v/n)\), with \(u,v\in\mathbb R^2\) and \(|u|,|v|<n\pi\). Write \(a=|u|\), \(b=|v|\), \(c=|u-v|\),
\[
q=\frac{a+b+c}{2\pi},\qquad t=\frac{(u_1v_2-u_2v_1)^2}{12\pi c},
\]
where \(t=0\) at \(c=0\) by continuous extension. The spherical cosine law and the exponential-coordinate area Jacobian give, uniformly on bounded sets,
\[
\frac{P}{2\pi}=\frac qn-\frac{t}{n^3}+O(n^{-5}),\qquad
 d\sigma(Y)d\sigma(Z)=\frac{du\,dv}{n^4}\left[1-\frac{a^2+b^2}{6n^2}+O(n^{-4})\right].
\tag{2}
\]
In (2) each remainder is bounded by a polynomial in \(a+b\) times the stated order on a growing small-coordinate region, and the distance remainder is continuous at \(u=v\). Combining the Taylor series for \(n\log(1-P/(2\pi))\) with (2), the integrand density in (1), times \(n^4\), becomes
\[
 e^{-q}\left\{1-\frac{q^2}{2n}+
\frac{q^4/8-q^3/3+t-(a^2+b^2)/6}{n^2}+O\!\left(\frac{\mathrm{poly}(a+b)}{n^3}\right)\right\}du\,dv.
\tag{3}
\]
For rigor, use the global inequalities \(P\ge2\max\{d(N,Y),d(N,Z)\}\) and \((1-x)^n\le e^{-nx}\) to bound the original rescaled density by \(e^{-\max(a,b)/\pi}\). On \(a+b\le n^{1/12}\), the remainder in the *full density* is bounded by \(n^{-3}\) times a fixed polynomial in \(a+b\) and \(e^{-q/2}\); outside that region the integral is exponentially small. This allows termwise integration of (3), with total \(O(n^{-3})\) error inside the braces after removing \(n^{-4}\). This argument also avoids treating finite sampling or numerical integration as proof of an infinite asymptotic.

**3. Exact planar moments.** Introduce scaled tangent variables \(U=u/(2\pi)\) and \(V=v/(2\pi)\). Let \(L=|U|+|V|+|U-V|\), and integrate with the measure \(e^{-L}dU\,dV\). The following three absolutely convergent integrals are exact:
\[
I_0=\int e^{-L}\,dU\,dV=\frac{4\pi^2}{7},\qquad
I_R=\int (|U|^2+|V|^2)e^{-L}\,dU\,dV=\frac{32\pi^2}{11},
\]
\[
I_T=\int\frac{(U_1V_2-U_2V_1)^2}{|U-V|}e^{-L}\,dU\,dV=\frac{8\pi^2}{11}.
\tag{4}
\]
To verify them directly, set \(a=|U|\), \(b=|V|\), \(c=|U-V|\). For positive nondegenerate triangles with area \(\Delta\), polar-angle reduction gives \(dU\,dV=2\pi abc\,da\,db\,dc/\Delta\). Put \(x=(b+c-a)/2\), \(y=(a+c-b)/2\), \(z=(a+b-c)/2\) so \(\Delta^2=(x+y+z)xyz\) and \(L=2(x+y+z)\). The Jacobian becomes \(4\pi abc/\Delta\,dx\,dy\,dz\). Separating \(s=x+y+z\) and the simplex coordinates \((x,y,z)/s\), the angular moments are Dirichlet moments. If \((X,Y,Z)\) has Dirichlet parameters \((1/2,1/2,1/2)\), then
\[
\mathbb E[(X+Y)(Y+Z)(X+Z)]=\frac4{21},\quad
\mathbb E[(X+Y)(Y+Z)(X+Z)((Y+Z)^2+(X+Z)^2)]=\frac{32}{165}.
\]
For Dirichlet parameters \((3/2,3/2,3/2)\), the additional moment \(\mathbb E[(X+Z)(Y+Z)]=14/33\). The radial gamma integrals \(\int_0^\infty s^k e^{-2s}ds=k!/2^{k+1}\) yield (4). All three rational identities are independently checked by the supplied standard-library verification program.

**4. Coefficients.** Homogeneity on \(\mathbb R^4\) implies that under the normalized planar density proportional to \(e^{-q}\), the scalar \(q\) has gamma distribution with shape \(4\) and rate \(1\). Its moments are \(\mathbb E q^2=20\), \(\mathbb E q^3=120\), and \(\mathbb E q^4=840\). The first correction is \(-20/2=-10\). The noncurvature part of the second correction is \(840/8-120/3=65\). With the normalization in (4), the remaining curvature contribution is
\[
\frac{(2\pi)^2}{6}\frac{I_T-I_R}{I_0}
=\frac{2\pi^2}{3}\left(\frac{14}{11}-\frac{56}{11}\right)
=-\frac{28\pi^2}{11}.
\]
The leading unnormalized integral is \((2\pi)^4I_0=64\pi^6/7\), completing the expansion in (1).

For the first area moment, the two-probe Crofton formula gives the separate exact expression \(\mathbb E A_n=2\pi\int_0^\pi(1-\theta/\pi)^n\sin\theta\,d\theta\). Its leading asymptotic is \(2\pi^3/n^2\), proving the displayed moment ratio.

## Verification

Run `python3 verify.py` with Python's standard library. It reconstructs every Dirichlet polynomial moment in (4) using exact fractions, checks the radial-gamma normalizations, and computes both asymptotic coefficients independently from the moment representation. The expected last line is `ALL_EXACT_MOMENT_IDENTITIES_PASSED`. The exact symbolic checks are a finite subcertificate; the global exponential domination in the proof establishes the asymptotic claim. A separate numerical spherical-angle quadrature was used as a consistency check at \(n=100,200,400\), not as a proof.

## Relationship to prior work

Kabluchko–Thäle (2020), *Faces in random great hypersphere tessellations*, defines the weighted typical spherical cell and determines first-order spherical intrinsic-volume and face-number expectations. Its Theorem 5.13 treats first expectations in the Poisson limit; the cited results do not give this area-square expansion. Hug–Schneider (2015), *Random conical tessellations*, Theorem 8.1 determines second moments of normalized face contents of the **uniformly selected** Schläfli cell. The present observable is a squared area of the **area-biased** cell, which is instead a **third raw area moment** of a uniform cell, so the earlier second-moment theorem does not imply (1). Miles (1971) treats random spherical tessellations and mixed second moments; a complete original copy was not available for line-by-line priority comparison. Richey–Sarkar (2020) recount Goudsmit's earlier planar Poisson-line area-moment calculation and the Crofton scaling connection; these are also not the finite-binomial spherical \(n^{-2}\) correction. The original identities (4) are supplied and evaluated here rather than inferred from a known leading scaling law.

## Limitations

The result requires independent isotropic great-circle cuts and two-dimensional spherical area. It is not about uniform selection among cells, arbitrary directional distributions, spherical Voronoi diagrams or Poisson random cut counts. Higher corrections and an exact finite-\(n\) formula are not asserted. The leading Euclidean limit is closely related to classical Crofton-cell theory; historical originality of the explicit corrections is supported by inspected literature but not exhaustively certified. The 1971 Miles paper remains a specific full-text access risk. No independent mathematical audit is represented.

## References

- Z. Kabluchko and C. Thäle, *Faces in random great hypersphere tessellations*, arXiv:2005.01055v1 (first posted 2020-05-03), especially Sections 2.2, 5.3–5.4; https://arxiv.org/html/2005.01055v1
- D. Hug and R. Schneider, *Random conical tessellations*, arXiv:1508.07768 (2015), Lemma 5.2 and Theorem 8.1; https://arxiv.org/abs/1508.07768
- J. Richey and A. Sarkar, *Intersections of random sets*, arXiv:2006.01323 (2020), Section 6 on Goudsmit's calculation; https://arxiv.org/abs/2006.01323
- R. E. Miles, *Random points, sets and tessellations on the surface of a sphere*, Sankhyā Ser. A 33 (1971), 145–174, JSTOR 25049720; https://www.jstor.org/stable/25049720
- C. Deuß, J. Hörrmann and C. Thäle, *A random cell splitting scheme on the sphere*, arXiv:1511.04232 (2015); https://arxiv.org/abs/1511.04232
