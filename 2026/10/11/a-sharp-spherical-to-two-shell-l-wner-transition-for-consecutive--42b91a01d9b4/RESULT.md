# A sharp spherical-to-two-shell Löwner transition for consecutive-layer hypersimplices

## Finding
Fix an integer \(n\ge2\) and integers \(0\le a<b\le n\). Define the consecutive-layer \(S\)-hypersimplex
\[P_{n;a,b}=[0,1]^n\cap\left\{x:a\le\sum_{i=1}^n x_i\le b\right\}.\]
Write \(H=\mathbf1\mathbf1^{\mathsf T}/n\) and \(D=(n/2-a)(b-n/2)\). Its unique smallest-volume enclosing Euclidean ellipsoid has a sharp two-phase classification.

**Spherical phase.** If \(D\ge n/4\), the ellipsoid is
\[\mathcal E_{n;a,b}=\left\{x:\|x-\tfrac12\mathbf1\|_2^2\le\tfrac n4\right\}.\]
Every one of its \(\sum_{k=a}^b\binom nk\) binary vertices contacts the ellipsoid. Its volume equals \(\kappa_n(\sqrt n/2)^n\), where \(\kappa_n=\pi^{n/2}/\Gamma(n/2+1)\).

**Two-shell phase.** If \(D<n/4\), write \(A_a=a(n-a)\), \(A_b=b(n-b)\), \(\Delta=A_b-A_a\), and let \(p\in(0,1)\) uniquely maximize \(p(1-p)(A_a+p\Delta)^{n-1}\). Equivalently \(p\) is the unique interior solution of
\[A_a+(n\Delta-2A_a)p-(n+1)\Delta p^2=0.\]
Define \(\mu=a+p(b-a)\), \(V=p(1-p)(b-a)^2\), and \(R=(1-p)A_a+pA_b\). Then
\[\boxed{\mathcal E_{n;a,b}=\left\{x:\frac{\|H(x-\mu\mathbf1/n)\|_2^2}{V}+\frac{(n-1)\|(I-H)x\|_2^2}{R}\le1\right\}.}\]
Its semiaxis in direction \(\mathbf1\) is \(\sqrt V\), and each of its \(n-1\) transverse semiaxes is \(\sqrt{R/(n-1)}\). Its Euclidean volume is \(\kappa_n\sqrt V(R/(n-1))^{(n-1)/2}\). Exactly \(\binom na+\binom nb\) vertices contact it, namely the binary vectors of cardinalities \(a\) and \(b\). For \(a+b=n\), the spherical phase occurs if and only if \((b-a)^2\ge n\); below that threshold the center is \(\mathbf1/2\), while the longitudinal/transverse squared semiaxes are \((b-a)^2/4\) and \((n^2-(b-a)^2)/(4(n-1))\), respectively.

## Assumptions and scope
All norms, volumes, and ellipsoids use the ambient standard Euclidean metric. The integers obey \(n\ge2\) and \(0\le a<b\le n\), ensuring full dimension. The only counted contacts are vertices of the polytope; strict convexity of an ellipsoid excludes further contact points on nontrivial polytope faces. The source-defined family of \(S\)-hypersimplices is the scientific object, not a claim about arbitrary sliced prisms with fractional bounds.

## Proof
**1. Vertices.** The vertices of \(P_{n;a,b}\) are exactly the binary vectors of weights \(a,a+1,\ldots,b\). Indeed, two fractional coordinates can be perturbed oppositely, and a single fractional coordinate cannot be a vertex: if the cardinality sum is at an integer endpoint it must be integral, while otherwise that coordinate can be perturbed. The binary vectors satisfying the bounds are vertices because they are vertices of the cube.

**2. A global ellipsoid certificate.** Let \(X\) be a finitely supported probability on the vertices, with mean \(m\) and positive-definite covariance \(\Sigma\). If \(\mathbb E[(X-m)^{\mathsf T}\Sigma^{-1}(X-m)]=n\) and every vertex obeys \((x-m)^{\mathsf T}\Sigma^{-1}(x-m)\le n\), the ellipsoid defined by that inequality is the *unique* smallest-volume enclosing ellipsoid. To see this, let any competing enclosing ellipsoid have center \(z\) and positive shape \(B\), defined by \((x-z)^{\mathsf T}B^{-1}(x-z)\le n\). Taking expectation yields
\[n\ge\operatorname{tr}(B^{-1}\Sigma)+(m-z)^{\mathsf T}B^{-1}(m-z)\ge n\left(\frac{\det\Sigma}{\det B}\right)^{1/n}.\]
Hence \(\det B\ge\det\Sigma\); equality requires \(z=m\) and \(B=\Sigma\) by arithmetic–geometric mean, proving uniqueness. The resulting ellipsoid's shape in conventional unit-level notation is \(n\Sigma\).

**3. Symmetric covariance and the spherical phase.** Sample a random cardinality \(K\) in \(\{a,\ldots,b\}\), then sample a uniformly random binary vector of weight \(K\). Let \(\mu=\mathbb E K\), \(V=\operatorname{Var}K\), and \(R=\mathbb E[K(n-K)]\). Then \(m=\mu\mathbf1/n\) and
\[\Sigma=\frac Vn H+\frac{R}{n(n-1)}(I-H).\]
If \(D\ge n/4\), necessarily \(a<n/2<b\). Among distributions supported on \(a,b\) with mean \(n/2\), the variance is \(D\). The distribution supported on the closest integer(s) to \(n/2\), with mean \(n/2\), has variance either \(0\) or \(1/4\). Thus a convex mixture has mean \(n/2\) and variance exactly \(n/4\). Since \(\mathbb E[K(n-K)]=n^2/4-\operatorname{Var}K\), it has \(R=n(n-1)/4\) and hence \(\Sigma=I/4\). Every cube vertex satisfies \(\|x-\mathbf1/2\|_2^2=n/4\). The certificate of Step 2 establishes optimality, uniqueness, and all contacts.

**4. Endpoint covariance in the two-shell phase.** Let \(K=a\) with probability \(1-p\), and \(K=b\) with probability \(p\), with \(0<p<1\). Then \(V=p(1-p)(b-a)^2\) and \(R=A_a+p\Delta\). Both are positive. The log determinant of \(\Sigma\), up to constant terms, is
\[\log[p(1-p)]+(n-1)\log(A_a+p\Delta).\]
This function is strictly concave on \((0,1)\), diverges to minus infinity at both endpoints, and has the stated unique stationary point. Its derivative is the difference of the two squared covariance-Mahalanobis norms at weights \(b\) and \(a\), so stationarity makes them equal. Their weighted average is \(\operatorname{tr}(\Sigma^{-1}\Sigma)=n\); therefore both equal \(n\).

For a binary vector of weight \(k\), its squared covariance-Mahalanobis norm is
\[q(k)=\frac{(k-\mu)^2}{V}+\frac{(n-1)k(n-k)}{R}.\]
Consequently \(q(a)=q(b)=n\) and
\[q(k)-n=\eta(k-a)(k-b),\qquad \eta=\frac1V-\frac{n-1}{R}.\]
It remains to prove \(\eta>0\) throughout \(D<n/4\). The stationarity equation in terms of \(\mu\) is
\[(a+b-2\mu)R+(n-1)(n-a-b)V=0,\]
and \(R=(n-a-b)\mu+ab\). Rearranging yields
\[(n-2\mu)R=(n-a-b)\bigl(R-(n-1)V\bigr).\]
If \(a+b=n\), then \(\mu=n/2\), \(V=D\), and \(R-(n-1)V=n(n/4-D)>0\). Otherwise reflect \(x\mapsto\mathbf1-x\) if needed, so assume \(a+b<n\). When \(b\le n/2\), automatically \(\mu<n/2\). When \(a<n/2<b\), evaluate the derivative of \(\log[V R^{n-1}]\) at \(\mu=n/2\), where \(V=D>0\) and \(R=n^2/4-D\). That derivative is
\[\frac{n(n-a-b)(D-n/4)}{D(n^2/4-D)}<0.\]
By strict concavity, its maximizer has \(\mu<n/2\). Therefore the rearranged stationarity identity gives \(R-(n-1)V>0\) in either case and \(\eta>0\).

Since \((k-a)(k-b)\le0\) for every allowed integer \(k\), all vertices satisfy \(q(k)\le n\), with equality only at the endpoint weights. Step 2 now proves exact global optimality and uniqueness, while the two covariance eigenspaces give the claimed shape, semiaxes, volume, and contact count.

## Verification
The standalone standard-library verifier `verify_loewner_slab.py` checks algebraic root positivity, all layer inequalities, exact contact behavior, and balanced-phase relations for all \(27{,}719\) integer triples with \(2\le n\le54\). An independent numerical D-optimal-design optimizer `independent_optimizer.py` uses SciPy's SLSQP to compare the formula against unconstrained probability mixtures over all integer weight layers for all \(559\) triples with \(2\le n\le14\), from three initializations; the observed maximum objective discrepancy was below \(10^{-12}\). These experiments are finite corroboration only: Steps 1–4 establish the stated all-parameter theorem.

## Relationship to prior work
Manecke, Sanyal, and So introduced the general \(S\)-hypersimplex family and studied its faces, pulling triangulations, and monotone paths [1]. Ferroni and McGinnis analyzed the Ehrhart theory of related prism slices [2]; Ferroni studied Ehrhart positivity for hypersimplices and matroid polytopes [3]. These combinatorial and lattice statements do not supply the Euclidean minimum-volume enclosing ellipsoid, which is not preserved by arbitrary lattice equivalence. Previously obtained minimum-enclosing-*sphere* formulas for consecutive layers likewise do not imply minimum-volume ellipsoid optimality: the two-shell phase generally has unequal axes. The proof uses a self-contained covariance/trace certificate, which avoids reliance on general unproved optimality assumptions.

## Limitations
The classification applies to the coordinate realization above, integer slab endpoints, and the standard ambient Euclidean metric. It does not classify arbitrary affine deformations or nonuniform slice inequalities. Literature searches and inspected primary texts did not find identical statements, but they do not establish absolute priority; an equivalent result in optimal-design or ellipsoid terminology could remain unrecognized. Numerical verification is not a substitute for the proof. No independent external audit has been performed.

## References
[1] S. Manecke, R. Sanyal, J. So, *\(S\)-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491v1 (first public 2018-12-18), https://arxiv.org/abs/1812.07491.

[2] L. Ferroni, D. McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808v1 (first public 2022-02-23), https://arxiv.org/abs/2202.11808.

[3] L. Ferroni, *Ehrhart positivity of hypersimplices*, arXiv:2012.04711v1 (2020), https://arxiv.org/abs/2012.04711.
