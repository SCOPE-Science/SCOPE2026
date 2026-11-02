# Nyquist-mode softening of the cubically weighted Bergman pole Hessian

## Finding
For every integer \(N\ge2\), put \(\theta_j^\star=2\pi j/N\) and define the squared weighted Bergman norm
\[
\mathcal E_N(\boldsymbol\theta)=\frac4\pi\int_{|z|<1}\left|\sum_{j=0}^{N-1}\frac1{z-e^{i\theta_j}}\right|^2(1-|z|^2)^3\,dA(z).
\]
At the regular configuration \(\boldsymbol\theta^\star\), its real angle Hessian \(H_N\) is a circulant matrix. Define
\[
a_m=\frac{24m}{(m+1)(m+2)(m+3)},\quad
A_{0,N}=\sum_{\ell\ge1}a_{\ell N},\quad
A_{k,N}=\sum_{\ell\ge0}a_{\ell N+k}\quad(1\le k<N).
\]
Its complete Fourier spectrum is
\[
\lambda_{0,N}=0,\qquad
\boxed{\lambda_{k,N}=N\big(A_{k,N}+A_{N-k,N}-2A_{0,N}\big)}\qquad(1\le k<N).
\]
Every nonrotational eigenvalue is strictly positive. More precisely, the smallest eigenvalue is attained **exactly** at the central frequencies \(k=\lfloor N/2\rfloor,\lceil N/2\rceil\) (a single frequency if \(N\) is even), and nowhere else. Its sharp large-\(N\) expansion is
\[
\boxed{\lambda_{\min}(N)=\frac{16\pi^2}{N}-\frac{1728\zeta(3)}{N^2}+O(N^{-3})}.
\]
Consequently, for fixed \(N\), if \(\varepsilon_j^\circ=\varepsilon_j-N^{-1}\sum_l\varepsilon_l\), the precise local quadratic lower bound is
\[
\mathcal E_N(\boldsymbol\theta^\star+\boldsymbol\varepsilon)-\mathcal E_N(\boldsymbol\theta^\star)
\ge\frac{\lambda_{\min}(N)}2\sum_j|\varepsilon_j^\circ|^2
+o\!\left(\sum_j|\varepsilon_j^\circ|^2\right).
\]
The coefficient cannot be increased. Unlike the critically weighted case, where the lowest-curvature mode is the first Fourier harmonic and its eigenvalue grows linearly with \(N\), the cubically weighted lowest-curvature mode lies at the Nyquist end and has eigenvalue of order \(N^{-1}\).

## Assumptions and scope
The radial exponent is exactly \(\alpha=3\); planar area \(dA\) is unnormalized and the factor \(4/\pi\) makes constants have norm one. Each of the \(N\) boundary poles has residue one. Angles are real variables in radians, and perturbations are sufficiently small that poles remain distinct. The Hessian is taken with respect to the standard Euclidean metric on the \(N\) angle variables. The zero Fourier mode represents joint rotation. All statements concern this precisely normalized squared norm, not its unsquared square root or an arbitrary \(L^p\) functional. The primary classification is MSC2020 \(30\mathrm H20\).

## Proof
**Exact moment identity.** For any integer \(m\ge1\), direct beta integration gives
\[
\frac4\pi\int_{|z|<1}|z|^{2m-2}(1-|z|^2)^3\,dA(z)
=\frac{24}{m(m+1)(m+2)(m+3)}=:w_m.
\]
Inside the disk,
\[
\sum_j(z-e^{i\theta_j})^{-1}
=-\sum_{m=1}^{\infty}z^{m-1}\sum_j e^{-im\theta_j}.
\]
By angular orthogonality and norm convergence,
\[
\mathcal E_N(\boldsymbol\theta)=\sum_{m\ge1}w_m\left|\sum_j e^{im\theta_j}\right|^2.
\]
Since \(\sum m^2w_m<\infty\), this energy is twice continuously differentiable in every angle; differentiating twice termwise is justified uniformly. Cyclic symmetry and rotation invariance imply that \(\boldsymbol\theta^\star\) is stationary.

**Second variation.** Put \(S_m=\sum_j e^{im\theta_j}\). At \(\boldsymbol\theta^\star\), \(S_m=N\) when \(N\mid m\) and \(S_m=0\) otherwise. For a real perturbation \(\boldsymbol\varepsilon\), differentiation of the exact squared modulus gives
\[
D^2\mathcal E_N[\boldsymbol\varepsilon,\boldsymbol\varepsilon]
=2\sum_{\substack{m\ge1\\N\nmid m}}a_m\left|\sum_j\varepsilon_j e^{2\pi i mj/N}\right|^2
+2\sum_{\substack{m\ge1\\N\mid m}}a_m
\left[\left(\sum_j\varepsilon_j\right)^2-N\sum_j\varepsilon_j^2\right].
\]
Define the unnormalized discrete transform \(\widehat\varepsilon_k=\sum_j\varepsilon_j e^{-2\pi i jk/N}\). Parseval gives \(N\sum_j\varepsilon_j^2=\sum_{k=0}^{N-1}|\widehat\varepsilon_k|^2\); therefore
\[
D^2\mathcal E_N[\boldsymbol\varepsilon,\boldsymbol\varepsilon]
=2\sum_{k=1}^{N-1}(A_{k,N}-A_{0,N})|\widehat\varepsilon_k|^2.
\]
The transform of a **real** vector satisfies \(|\widehat\varepsilon_k|=|\widehat\varepsilon_{N-k}|\), so pairing conjugate frequencies shows that the real symmetric circulant Hessian has eigenvalues \(\lambda_{k,N}=N(A_{k,N}+A_{N-k,N}-2A_{0,N})\). This conjugate-pairing factor is essential: the individual residue sums need not agree.

**Discrete convexity forces positivity and the central minimum.** Direct rational simplification for every integer \(m\ge1\) gives
\[
a_m-a_{m+1}=\frac{24(2m-1)}{(m+1)(m+2)(m+3)(m+4)}>0,
\]
\[
a_m-2a_{m+1}+a_{m+2}
=\frac{144(m-1)}{(m+1)(m+2)(m+3)(m+4)(m+5)}\ge0,
\]
with strict second difference for \(m\ge2\). For \(1\le k<N\), regroup the absolutely convergent sums as
\[
A_{k,N}+A_{N-k,N}-2A_{0,N}
=a_k+\sum_{\ell\ge1}\left(a_{\ell N-k}+a_{\ell N+k}-2a_{\ell N}\right).
\]
Every bracket is nonnegative by discrete convexity, and \(a_k>0\), proving strict positivity.

For fixed \(N\), let \(B_k=A_{k,N}+A_{N-k,N}\). Then \(B_k=B_{N-k}\) and \(B_k=a_k+\sum_{\ell\ge1}(a_{\ell N-k}+a_{\ell N+k})\). Its second finite difference on \(k=2,\ldots,N-2\) is nonnegative termwise and strictly positive because at least one summand uses a second difference centered at an index \(\ge2\). Therefore \(B_k\) is strictly convex and symmetric on \(\{1,\ldots,N-1\}\). Its only minimizing index or pair of indices is the center \(\lfloor N/2\rfloor,\lceil N/2\rceil\). For \(N=2,3\) the conclusion follows immediately from symmetry. Subtracting the constant \(2A_{0,N}\) preserves the minimizers.

**Sharp two-term asymptotic.** As \(m\to\infty\), uniformly with an absolute remainder constant,
\[
a_m=\frac{24}{m^2}-\frac{144}{m^3}+O(m^{-4}).
\]
For \(k=\lfloor N/2\rfloor\) and \(u=k/N=1/2+O(N^{-1})\), writing the residue sums through Hurwitz zeta functions gives
\[
B_k=\frac{24}{N^2}\bigl[\zeta(2,u)+\zeta(2,1-u)\bigr]
-\frac{144}{N^3}\bigl[\zeta(3,u)+\zeta(3,1-u)\bigr]+O(N^{-4}),
\]
\[
2A_{0,N}=\frac{48\zeta(2)}{N^2}-\frac{288\zeta(3)}{N^3}+O(N^{-4}).
\]
The symmetric Hurwitz-zeta combinations are twice differentiable near \(u=1/2\), symmetric there, and thus vary by only \(O(N^{-2})\) when \(u=1/2+O(N^{-1})\). Since \(\zeta(s,1/2)=(2^s-1)\zeta(s)\), subtraction yields
\[
B_k-2A_{0,N}=\frac{96\zeta(2)}{N^2}-\frac{1728\zeta(3)}{N^3}+O(N^{-4}).
\]
Multiplication by \(N\) and \(\zeta(2)=\pi^2/6\) gives the asserted expansion, with parity effects absorbed in \(O(N^{-3})\).

**Optimal local coefficient.** The spectral theorem and rotation invariance imply
\[
\mathcal E_N(\boldsymbol\theta^\star+\boldsymbol\varepsilon)-\mathcal E_N(\boldsymbol\theta^\star)
=\tfrac12\boldsymbol\varepsilon^{\circ T}H_N\boldsymbol\varepsilon^\circ+o(\|\boldsymbol\varepsilon^\circ\|_2^2).
\]
The coefficient \(\lambda_{\min}(N)/2\) follows. Choosing a real sine or cosine at a minimizing central frequency gives equality at quadratic order, so it is sharp. This is only a *local* stability statement; no global quadratic modulus is asserted.

## Verification
The standalone reproducibility script `check_hessian.py` uses only the Python standard library. Running `python3 check_hessian.py` verifies exact first- and second-difference rational identities for 34 successive positive indices, independently checks the minimum Fourier mode for each \(N=2,\ldots,18\), and compares direct perturbations of the original weighted Bergman series against the spectral second derivative at four sizes. Its output is `PASS: 68 exact difference identities; central modes N=2..18; 4 direct-energy curvature tests`. The infinite-dimensional and all-\(N\) conclusions are established by the algebraic convexity proof and convergent series, not by these samples.

## Relationship to prior work
Corbett (2026, Sections 2.3 and 3) proves the global regular-polygon minimization property for power weights, but studies Hessian positivity through angular convexity only in the range \(0<\alpha\le1\); the \(\alpha=3\) Fourier spectrum and softening asymptotic do not follow from its global inequality. Abakumov, Borichev, and Fedorovskiy (2020, Lemma 12) identify the failure of global angular pair-convexity beyond the critical weight, and prove global results for concave weights, but do not determine this supercritical local Hessian. The published *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles* (2026) is restricted to \(\alpha=1\), for which the first Fourier mode is least-curved and its eigenvalue is asymptotic to \(N\), unlike the central-frequency order-\(N^{-1}\) mode proved here. Bezrukov (2026) proves generalized global minimization but the available description provides no explicit sharp supercritical Hessian spectrum. No claim is made that global minimization is new.

## Limitations
The weight is fixed to the cubic exponent, and all poles have unit residues. A classification across other supercritical weights is not established. The lower bound is local for each fixed \(N\); uniform radii of perturbation or a global stability inequality are not proved. Older unindexed work could contain equivalent spectral calculations. The elementary verification script does not constitute an independent mathematical audit.

## References
1. Georgia Corbett, *Two new proofs of Chui's Conjecture in Weighted Bergman Spaces*, arXiv:2609.21121v1, first public 2026-09-17, https://arxiv.org/abs/2609.21121 (Sections 2.3 and 3).
2. Evgeny Abakumov, Alexander Borichev, Konstantin Fedorovskiy, *Chui's conjecture in Bergman spaces*, arXiv:2009.01898v1, first public 2020-09-03, https://arxiv.org/html/2009.01898v1 (Theorems 1 and 6 and Lemma 12).
3. *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles*, published 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-full-fourier-hessian-spectrum-and-sharp-local-stability-for-equi--9aca32c3cb4f (critically weighted case only).
4. Egor Bezrukov, *Proof of the generalized Chui conjecture*, arXiv:2609.03134v1, first public 2026-09-02, https://arxiv.org/abs/2609.03134.
