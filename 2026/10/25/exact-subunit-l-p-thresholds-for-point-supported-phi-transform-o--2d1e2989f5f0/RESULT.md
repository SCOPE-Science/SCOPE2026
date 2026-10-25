# Exact subunit-\(L^p\) thresholds for point-supported \(\phi\)-transform obstructions

## Finding

Fix integers \(n\ge1\) and \(m\ge1\). There exists a nonnegative \(\phi\in C_c^\infty(\mathbb R^n)\) with \(\int\phi=1\), \(\phi(0)>0\), and \(\phi\) constant on a neighborhood of \(0\), such that \(\partial_1^m\phi\not\equiv0\). For \(f=\partial_1^m\delta_0\), define its distributional \(\phi\)-transform by

\[
F(x,t)=\langle f(x+t\,\cdot),\phi\rangle
=(-1)^m t^{-n-m}(\partial_1^m\phi)(-x/t),\qquad t>0.
\]

Then \(F(\cdot,t)\to f\) in distributions as \(t\downarrow0\), while \(F(x,t)\to0\) pointwise for every \(x\in\mathbb R^n\). Moreover,

\[
\int_{\mathbb R^n}|F(x,t)|^p\,dx
=C_{\phi,p,m}\,t^{n-(n+m)p},\qquad
C_{\phi,p,m}=\int_{\mathbb R^n}|\partial_1^m\phi(y)|^p\,dy>0.
\]

Consequently, on every compact set the \(L^p\) quasi-norm is uniformly bounded for \(0<t\le1\) when \(0<p\le n/(n+m)\). On any compact neighborhood of the origin it is unbounded when \(p>n/(n+m)\). This is the exact threshold for this point-supported family.

## Assumptions and scope

The dimension \(n\) and derivative order \(m\) are positive integers. The kernel \(\phi\) is smooth, compactly supported, nonnegative, has integral one, and is constant and strictly positive near the origin. The transform is the general distributional \(\phi\)-transform, not necessarily one of the specific Abel, Cesàro, or Gauss--Weierstrass Fourier-inversion means. For every fixed \(p<1\), choosing \(m=1\) and then \(n\ge p/(1-p)\) gives a counterexample to a dimension-independent subunit-\(L^p\) support-exclusion statement in this general class.

## Proof

Choose a product bump \(\phi(x)=c\prod_{j=1}^n\eta(x_j)\), where \(\eta\in C_c^\infty(\mathbb R)\) is nonnegative, constant and positive near zero, and not constant globally; choose it so \(\eta^{(m)}\not\equiv0\), and select \(c>0\) to normalize the integral to one. Set \(\rho_t(x)=t^{-n}\phi(-x/t)\). Then \(\rho_t\) is a reflected approximate identity, so \(\rho_t\to\delta_0\) in distributions. Differentiation is continuous on distributions and

\[
F(x,t)=\partial_1^m\rho_t(x)=(-1)^m t^{-n-m}(\partial_1^m\phi)(-x/t),
\]

hence \(F(\cdot,t)\to\partial_1^m\delta_0\).

Since \(\phi\) is constant near zero, \(\partial_1^m\phi(0)=0\), so \(F(0,t)=0\). For each fixed \(x\ne0\), the point \(-x/t\) eventually lies outside the compact support of \(\partial_1^m\phi\), hence \(F(x,t)=0\) for all sufficiently small \(t\). This proves pointwise convergence to zero at every point.

For \(0<p<1\), a change of variables \(y=-x/t\) gives

\[
\int_{\mathbb R^n}|F(x,t)|^p\,dx
=t^{n-(n+m)p}\int_{\mathbb R^n}|\partial_1^m\phi(y)|^p\,dy.
\]

The constant is finite and positive. The exponent is nonnegative exactly when \(p\le n/(n+m)\). Any compact set has integral no larger than the full-space integral; if the compact set contains a neighborhood of zero, the shrinking support of \(F(\cdot,t)\) lies inside it for all sufficiently small \(t\), so the full-space identity also proves divergence above the threshold. These arguments establish the stated exact threshold.

## Verification

The proof uses only the approximate-identity limit, continuity of distributional differentiation, pointwise support geometry, and a change of variables. The normalization is \(\int\phi=1\); no Fourier-transform convention affects the scaling exponent. At the endpoint \(p=n/(n+m)\), the full-space \(p\)-integral is constant in \(t\). For smaller positive \(p\), it tends to zero. For larger \(p\), it diverges on any compact neighborhood of the origin.

## Relationship to prior work

Graham's 2008 support paper records a pointwise failure example using \(\delta'_0\) and an even test function. Vindas and Estrada's 2010 paper proves support exclusion for the general distributional \(\phi\)-transform under local \(L^p\) boundedness for \(p\ge1\), with \(\phi\ge0\) and \(\phi(0)>0\). The present calculation preserves those kernel conditions and gives an exact dimension/order-dependent local \(L^p\) threshold below one for point-supported derivatives. It does not replace or contradict the cited theorem in its stated range.

## Limitations

The result gives an exact obstruction profile for point-supported derivatives, not a classification of all distributions whose \(\phi\)-transforms are pointwise zero. For a fixed dimension and order, it does not decide whether a support-exclusion theorem might hold for all exponents between \(n/(n+m)\) and \(1\). It also does not establish counterexamples for each of the specific Fourier-inversion means (Abel, Cesàro, or Gauss--Weierstrass); the claim is restricted to the general \(\phi\)-transform class. The construction is an explicit scaling refinement of a known pointwise obstruction, so priority beyond the stated quantitative profile is not claimed.

## References

1. C. C. Graham, “The support of tempered distributions,” *Mathematical Proceedings of the Cambridge Philosophical Society* 144 (2008), 495–498. DOI: 10.1017/S030500410700103X. First published online 2008-02-07.
2. J. Vindas and R. Estrada, “On the support of tempered distributions,” *Proceedings of the Edinburgh Mathematical Society* (2) 53 (2010), 255–270. DOI: 10.1017/S0013091508000102. The public full text defines the \(\phi\)-transform, proves its distributional convergence, and states the local-\(L^p\) support theorem for \(p\ge1\).
