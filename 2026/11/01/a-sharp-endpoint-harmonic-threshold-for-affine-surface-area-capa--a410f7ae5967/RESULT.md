# A sharp endpoint harmonic threshold for affine-surface-area/capacity counterexample certificates

## Finding

Fix an integer \(n\ge2\). For \(1<p<n\), set \(\delta=p-1\), \(k=n-p\), and, for integers \(j\ge1\), define
\[
\lambda_j=2j(2j+n-2),\qquad
 a_j(n,p)=\prod_{r=0}^{j-1}\frac{p-2r}{n+p+2r},\qquad
 D_j(n,p)=\frac{2\lambda_j}{k+\sqrt{k^2+4\delta\lambda_j}}.
\]
Consider the sufficient second-variation coefficient
\[
 B_j(n,p)=\frac{p\delta}{2}D_j(n,p)^2-
 \frac{n+p}{2p}(\lambda_j-k)^2a_j(n,p)^2.
\]
Let \(j_*(n,p)=\min\{j\ge1:B_j(n,p)>0\}\). This index exists by the large-even-degree argument of Feng and Zhang [1]. It measures the **first degree certified by their explicit sufficient coefficient**, not the first degree of any possible counterexample.

Define the positive, dimension-dependent constants
\[
 c_n=\frac{\Gamma((n+1)/2)}{2\sqrt\pi},\qquad
 T_n=(n+1)(n-1)^2c_n^2
 =\frac{(n+1)(n-1)^2\Gamma((n+1)/2)^2}{4\pi}.
\]
Then the exact endpoint spectral onset is
\[
 \boxed{\lim_{p\downarrow1}(p-1)^{1/(n+2)}j_*(n,p)
       =T_n^{1/(n+2)}.}
\]
Thus the lowest even spherical-harmonic degree certified by this mechanism has asymptotic size \(2(T_n/(p-1))^{1/(n+2)}\).

There is a sharper **one-parameter crossover**. For every sequence of integers \(j\to\infty\) and exponents \(p=1+\delta\downarrow1\) satisfying \(\delta j^{n+2}\to\tau\in(0,\infty)\),
\[
 \boxed{\lim\frac{j^{n-2}}8 B_j(n,1+\delta)
 =\frac{\tau-T_n}{(n-1)^2}.}
\]
In particular, when the limiting scale \(\tau\) is strictly below or strictly above \(T_n\), the certificate is eventually respectively negative or positive. No assertion about the limiting sign at equality, nor about all counterexamples outside the sufficient certificate, is made.

For example, \(T_2=3/16\) and \(T_3=4/\pi\).

## Assumptions and scope

The dimension \(n\ge2\) remains fixed as \(p\downarrow1\). All spherical harmonics considered have even degree \(2j\ge2\). The quantities above use the normalizations of Feng and Zhang [1, equations (3.1), (3.4), (3.14)]; the harmonic eigenvalue \(\lambda_j\) is the positive eigenvalue of the negative spherical Laplacian. The coefficient \(B_j\) is one half of the bracket in their equation (3.14).

For a fixed nonzero even spherical harmonic \(Y_{2j}\), the function \(h_\varepsilon(u)=1+\varepsilon Y_{2j}(u)\) is the support function of a smooth strictly convex origin-symmetric body for sufficiently small nonzero \(\varepsilon\). Equation (3.14) of [1] supplies
\[
 \Phi_p(K_\varepsilon)-\gamma_{n,p}C_p(K_\varepsilon)
 \ge \varepsilon^2 B_j(n,p)
 \int_{S^{n-1}}Y_{2j}(u)^2\,d\sigma(u)+o(\varepsilon^2),
 \qquad \gamma_{n,p}=\left(\frac{p-1}{n-p}\right)^{p-1}.
\]
Consequently \(B_j>0\) rigorously yields a geometric counterexample to the proposed upper comparison of integral affine surface area and variational capacity. The remainder is controlled only for each **fixed** \((n,p,j)\) before \(\varepsilon\to0\); the endpoint theorem makes no uniform-in-degree assertion about the admissible amplitude \(\varepsilon\).

## Proof

**1. Exact coefficient and positive-ratio formulation.** By [1, equations (3.1), (3.4), (3.14)], the displayed formula for \(B_j\) is the coefficient of its proven lower bound. Write \(\lambda=\lambda_j\) and \(D=D_j\). Since \(\lambda>k>0\), \(D>0\). When \(p\) is sufficiently close to \(1\), none of the factors in \(a_j\) vanishes. Define
\[
 R_j(n,p)=\frac{(n+p)(\lambda-k)^2a_j(n,p)^2}{p^2\delta D^2}
 =\frac{n+p}{p^2\delta}\left(1-\frac{k}{\lambda}\right)^2
  \left(\frac{k+\sqrt{k^2+4\delta\lambda}}2\right)^2a_j(n,p)^2.
\]
Then \(B_j>0\) if and only if \(R_j<1\).

**2. Uniform Gamma and capacity factors.** For \(p\) near \(1\), the exact Gamma-function expression of [1, after (3.14)] is
\[
 |a_j(n,p)|=\left|\frac{\Gamma((n+p)/2)}{\Gamma(-p/2)}\right|
       \frac{\Gamma(j-p/2)}{\Gamma(j+(n+p)/2)}.
\]
By the standard Gamma-ratio expansion, uniformly for \(p\) in a compact neighborhood of \(1\),
\[
 |a_j(n,p)|=c_n j^{-(n+2)/2}
  \left(1+O_n(1/j+\delta\log j+\delta)\right)
\]
whenever \(j\to\infty\) and \(\delta\log j\to0\). The constant is indeed
\(\Gamma((n+1)/2)/|\Gamma(-1/2)|=c_n\), using \(\Gamma(-1/2)=-2\sqrt\pi\).
Furthermore,
\[
 \lambda=4j^2\left(1+O_n(1/j)\right),\qquad
 D=\frac{\lambda}{n-1}\left(1+O_n(\delta+\delta j^2)\right)
\]
provided \(\delta j^2\to0\). The second expansion follows by rationalizing the defining quadratic root and using \(k=n-1-\delta\).

**3. The crossover limit.** Suppose \(\delta j^{n+2}\to\tau\in(0,\infty)\). Since \(n\ge2\), it follows that \(\delta j^2\to0\) and \(\delta\log j\to0\). The two nonnegative terms in \(B_j\) are therefore
\[
 \frac{p\delta}{2}D^2
   =\frac{8\delta j^4}{(n-1)^2}(1+o(1)),
 \qquad
 \frac{n+p}{2p}(\lambda-k)^2a_j^2
   =8(n+1)c_n^2j^{2-n}(1+o(1)).
\]
Multiplying their difference by \(j^{n-2}/8\) yields \((\tau-T_n)/(n-1)^2\), as claimed.

**4. Sharp first-certified-degree asymptotic.** Set \(J_\delta=(T_n/\delta)^{1/(n+2)}\). For each fixed \(\eta\in(0,1)\), take \(j_+=\lceil(1+\eta)J_\delta\rceil\). Since \(\delta j_+^{n+2}\to T_n(1+\eta)^{n+2}>T_n\), step 3 proves \(B_{j_+}>0\) for sufficiently small \(\delta\). Thus \(j_*\le(1+\eta)J_\delta+1\).

For the lower bound, suppose along some \(\delta\downarrow0\) there is an integer \(j\le(1-\eta)J_\delta\) with \(B_j>0\), equivalently \(R_j<1\). If \(j\) stays bounded, then the exact ratio in step 1 tends to \(+\infty\) like \(\delta^{-1}\) because the fixed-degree limit of \(a_j\) is nonzero. Otherwise pass to a subsequence with \(j\to\infty\). Uniformly throughout \(j\le(1-\eta)J_\delta\), both \(\delta j^2\) and \(\delta\log j\) tend to zero. The uniform estimates in step 2 give
\[
 R_j(n,1+\delta)=\frac{T_n}{\delta j^{n+2}}(1+o(1))
 \ge\frac{1+o(1)}{(1-\eta)^{n+2}}>1,
\]
a contradiction. Consequently \(j_*>(1-\eta)J_\delta\). Letting \(\eta\downarrow0\) proves the first boxed limit. This argument does not assume monotonicity of the individual signs over all harmonic degrees.

## Verification

Run `python3 check_spectral_onset.py` with the Python standard library. The accompanying script independently compares Gamma ratios to their finite-product expressions, verifies signs using two algebraically equivalent coefficient formulas, enumerates the first certified indices at four dimensions and three small exponents, and tests the crossover numerically away from its sign boundary. The initial package execution reported **176 passed finite diagnostic assertions**. A diagnostic is not a substitute for the Gamma-ratio proof or the positivity implication in [1].

## Relationship to prior work

Feng and Zhang [1, Proposition 3.3] proved that for every fixed \(1<p<n\), all sufficiently high even spherical-harmonic degrees produce counterexamples, and gave exactly the coefficient and Gamma-product formulas used here. The new assertion is a **joint limit**, not a new second-variation formula: it quantifies the first sufficient harmonic index as \(p\downarrow1\), identifies its exact dimension-dependent leading constant, and proves a sharp crossover for the sufficient certificate. Their fixed-\(p\), high-degree asymptotic does not imply the result by interchanging limits, because \(p-1\) simultaneously tends to zero.

Ludwig, Xiao, and Zhang [2] established the convex Lorentz–Sobolev framework and the ball-normalized comparisons separately for \(L_p\)-surface area versus capacity and affine surface area. These do not give the relative spectral threshold derived here. No claim is made to supersede these earlier inequalities.

## Limitations

The threshold \(j_*\) concerns the **explicit sufficient lower-bound coefficient** from [1], not the true least unstable harmonic degree, nor the size of the counterexample perturbation. A nonpositive \(B_j\) cannot establish that the original functional inequality holds or that a perturbation fails. All estimates take fixed dimension and \(p\to1\), not a simultaneous high-dimensional limit. At the precise double-scale boundary \(\tau=T_n\), the leading term vanishes and does not determine the sign. Priority is qualified by the possibility of an equivalent unindexed endpoint analysis; no independent audit has been performed.

## References

[1] Y. Feng and D. Zhang, *\(L_p\)-Integral Affine Surface Area–Variational Capacity Inequalities*, arXiv:2610.13957v1, publicly submitted 2026-08-22, especially Lemmas 3.1–3.2, Proposition 3.3, and equations (3.1), (3.4), (3.14). https://arxiv.org/abs/2610.13957

[2] M. Ludwig, J. Xiao, and G. Zhang, *Sharp convex Lorentz–Sobolev inequalities*, especially Section 2 and Lemma 1. https://dmg.tuwien.ac.at/ludwig/LXZ.pdf
