# Sharp density-dependent reversal between two-node randomly pivoted Cholesky and iid kernel quadrature

## Finding

For the real, rank-three first-harmonic kernel on the unit circle,
\[
k_b(\theta,\varphi)=1+b\cos(\theta-\varphi),\qquad b>0,
\]
compare two samples drawn sequentially by randomly pivoted Cholesky (RPCholesky) against two independent uniform samples. In either scheme, calculate the **unrestricted optimal real quadrature weights** after choosing the two sites. For each first-harmonic target \(g(\theta)=a+u\cos\theta+v\sin\theta\), denote the mean *squared worst-case RKHS integration error* by \(R_{\rm RP}\) and \(R_{\rm iid}\), respectively. Then
\[
R_{\rm RP}=\frac{b}{b+4}\left(a^2+\frac{u^2+v^2}{2}\right),
\qquad
R_{\rm iid}=\left(1-\frac1{\sqrt{1+b}}\right)a^2+
\frac{b(u^2+v^2)}{8\sqrt{1+b}}.
\]
In particular, the exact difference factors as
\[
\boxed{R_{\rm RP}-R_{\rm iid}
=\frac{(\sqrt{1+b}-1)(\sqrt{1+b}-3)}
{\sqrt{1+b}(b+4)}
\left(a^2-\frac b8(u^2+v^2)\right).}
\]
Thus there is a **sharp kernel-amplitude threshold** at \(b=8\). For every probability density
\[
g_{t,\phi}(\theta)=1+t\cos(\theta-\phi),\qquad 0\le t\le1,
\]
RPCholesky has strictly lower expected squared worst-case error for \(0<b<8\). For \(b=8\), the two risks are equal for *every* first-harmonic target. For \(b>8\), iid strictly wins if \(0\le t<\sqrt{8/b}\), RPCholesky strictly wins if \(\sqrt{8/b}<t\le1\), and equality holds at \(t=\sqrt{8/b}\). The bounds are strict as stated for \(b>0\); no assertion of stochastic ordering of the full error distributions is made.

## Assumptions and scope

Take the unit circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), equipped with the normalized measure \(d\mu(\theta)=d\theta/(2\pi)\). Fix any real \(b>0\). The positive-semidefinite kernel \(k_b\) induces a real RKHS \(H_b\), identified through the feature map
\[
\Phi_b(\theta)=(1,\sqrt b\cos\theta,\sqrt b\sin\theta)\in\mathbb R^3,
\qquad k_b(\theta,\varphi)=\Phi_b(\theta)\cdot\Phi_b(\varphi).
\]
For any two distinct sites \(S=(\theta_1,\theta_2)\), define the objective and its optimal weights by
\[
\operatorname{Err}(S;g)^2
=\inf_{w\in\mathbb R^2}\ \sup_{\substack{f\in H_b\\\|f\|_{H_b}\le1}}
\left|\int_{\mathbb T}f(\theta)g(\theta)\,d\mu(\theta)
-\sum_{j=1}^2 w_j f(\theta_j)\right|^2.
\]
No positivity or sum-to-one constraint is placed on \(w\); these are the optimal *kernel quadrature* weights, not ordinary Monte Carlo weights. Under RPCholesky, draw the first site proportional to the original diagonal \(k_b(\theta,\theta)\), then draw the second proportional to the one-step Schur-complement residual diagonal. Under iid, draw both sites independently from \(\mu\). Identical sites have probability zero. The target function \(g\) need not be positive for the general formula, whereas the explicit density comparison uses nonnegative \(g_{t,\phi}\), each integrating to one.

## Proof

**1. Orthogonal projection and the conditional error.** Write \(c=\cos((\theta_2-\theta_1)/2)\) and \(\psi=(\theta_1+\theta_2)/2\), with a consistent representative of the difference. An unnormalized normal vector to the two-dimensional span of the site features is
\[
(-\sqrt b\,c,\cos\psi,\sin\psi).
\]
Indeed its scalar product with each \(\Phi_b(\theta_j)\) vanishes by the cosine subtraction identity. Its squared norm is \(1+bc^2\), strictly positive. The kernel mean feature vector for \(g=a+u\cos\theta+v\sin\theta\) is
\[
m_g=\int\Phi_b(\theta)g(\theta)\,d\mu(\theta)
=(a,\sqrt b\,u/2,\sqrt b\,v/2).
\]
Optimal quadrature equals the Euclidean orthogonal projection of \(m_g\) onto the site-feature span. Consequently, the squared integration error is its squared component along the displayed unit normal. Under both sampling laws, rotation invariance makes \(\psi\) uniform conditional on the difference \(\Delta=\theta_2-\theta_1\); the average mixed term vanishes. Thus
\[
\mathbb E[\operatorname{Err}(S;g)^2\mid\Delta]
=\frac{b\left[a^2\cos^2(\Delta/2)+(u^2+v^2)/8\right]}
{1+b\cos^2(\Delta/2)}.
\tag{1}
\]
This identity also covers antipodal sites, which are linearly independent for \(b>0\).

**2. The RPCholesky difference distribution.** The first pivot is uniform because \(k_b(\theta,\theta)=1+b\). The second-pivot residual diagonal, conditional on the first site, is
\[
R_b(\Delta)= (1+b)-\frac{(1+b\cos\Delta)^2}{1+b}.
\]
Its normalizing integral is \(Z_b=b(b+4)/(2(1+b))\). Therefore the law of \(\Delta\), as a density relative to uniform measure on the circle, is
\[
q_b(\Delta)=\frac{R_b(\Delta)}{Z_b}
=\frac{2(1-\cos\Delta)[2+b(1+\cos\Delta)]}{b+4}
=\frac{4(1-\cos\Delta)[1+b\cos^2(\Delta/2)]}{b+4}.
\tag{2}
\]
This joint two-site law is also the continuous volume-sampling law for this *particular* translation-invariant kernel: the common conditional normalizer yields density proportional to the two-by-two Gram determinant. The equivalence and its expected volume-sampling error are subsumed by earlier general volume-sampling theory; they are used as background, not claimed to be new.

**3. Integration for both designs.** From (2), and the uniform averages of \(\cos\Delta\) and \(\cos^2(\Delta/2)\),
\[
\mathbb E_{\rm RP}\!\left[\frac1{1+b\cos^2(\Delta/2)}\right]=\frac4{b+4},\quad
\mathbb E_{\rm RP}\!\left[\frac{b\cos^2(\Delta/2)}{1+b\cos^2(\Delta/2)}\right]=\frac b{b+4}.
\]
For iid differences, the elementary half-angle integral gives
\[
\mathbb E_{\rm iid}\!\left[\frac1{1+b\cos^2(\Delta/2)}\right]=\frac1{\sqrt{1+b}},\quad
\mathbb E_{\rm iid}\!\left[\frac{b\cos^2(\Delta/2)}{1+b\cos^2(\Delta/2)}\right]=1-\frac1{\sqrt{1+b}}.
\]
For example, the first integral follows by applying \(\tan\) on the two half-periods and integrating a rational quadratic denominator. Substitution into (1) proves both risk formulas.

**4. Complete sign classification.** Put \(s=\sqrt{1+b}>1\). The coefficient difference for \(a^2\) equals
\[
\frac b{b+4}-\left(1-\frac1s\right)=\frac{(s-1)(s-3)}{s(b+4)},
\]
while the coefficient difference for \((u^2+v^2)/2\) is its negative multiplied by \(b/4\). This proves the displayed factorization and the exact equality set. When \(g=g_{t,\phi}\), its coefficients satisfy \(a=1\) and \(u^2+v^2=t^2\). Since \(0\le t\le1\), the factor \(1-bt^2/8\) is positive for every \(b<8\); at \(b=8\), \(s-3=0\); and for \(b>8\) it changes sign precisely when \(t=\sqrt{8/b}\). The prefactor is negative for \(0<b<8\) and positive for \(b>8\), giving the complete classification. Rotating \(\phi\) changes neither rate. For any general first-harmonic nonnegative density \(g=a+u\cos+v\sin\) with total mass one, necessarily \(a=1\) and \(u^2+v^2\le1\); hence the same uniform \(b\le8\) conclusion holds, with sharp failure of dominance for \(b>8\).

## Verification

The adjacent standalone `verify.py` checks the source RPCholesky residual density normalization, independently integrates equation (1) under both difference laws, tests the exact formulas and factorization over nine kernel amplitudes and several targets, checks the positive-density sign cases, and tests 3,000 seeded random parameter triples. It uses Python standard-library arithmetic and midpoint quadrature. Run `python verify.py` from the directory containing both files; no external data or packages are required. These tests corroborate, but do not replace, the universal analytical argument above.

## Relationship to prior work

Epperly and Moreno (arXiv:2306.03955, first public June 6, 2023) developed the continuous RPCholesky sampling rule and optimal-weight kernel quadrature, stated general performance bounds, and compared it empirically with iid optimal-weight quadrature. This result applies **their** original rule, not a new sampling scheme. Belhadji, Bardenet and Chainais (arXiv:2002.09677, first public February 22, 2020) proved a general expected squared projection-error formula under continuous volume sampling; that theorem already implies the RP-only expected risk after the kernel's two-point law is identified with volume sampling. The novelty assessed here is instead the **joint exact comparison** with the iid-optimal-weight rule and the sharp sign reversal for nonnegative target densities at \(b=8\), including the density-modulation threshold above it. General sampling/Nyström quadrature work by Hayakawa, Oberhauser and Lyons (arXiv:2301.09517) addresses related approximation objectives without this exact two-node target-dependent comparison.

## Limitations

This theorem is for exactly two sample nodes, a rank-three first-harmonic circle kernel, and optimally chosen *unrestricted* weights. It compares **expected squared worst-case RKHS integration error**, not the expectation of the unsquared error, ordinary Monte Carlo fixed weights, or samplewise dominance. The likelihood that particular applications favor a sampler depends on the kernel and target density, and no higher-rank, arbitrary-kernel, high-dimensional, or asymptotic generalization is asserted. Publication-priority uncertainty remains for equivalent special-case calculations not located in the inspected literature.

## References

1. Ethan N. Epperly and Elvira Moreno, *Kernel Quadrature with Randomly Pivoted Cholesky*, arXiv:2306.03955v1, 2023-06-06; https://arxiv.org/abs/2306.03955; especially Sections 3–5, original sampling and iid comparisons.
2. Ayoub Belhadji, Rémi Bardenet and Pierre Chainais, *Kernel Interpolation with Continuous Volume Sampling*, arXiv:2002.09677v1, 2020-02-22; https://arxiv.org/abs/2002.09677; Definition 1, Theorem 4, and associated proof appendix.
3. Satoshi Hayakawa, Harald Oberhauser and Terry Lyons, *Sampling-based Nyström Approximation and Kernel Quadrature*, arXiv:2301.09517v1, 2023-01-23; https://arxiv.org/abs/2301.09517.
