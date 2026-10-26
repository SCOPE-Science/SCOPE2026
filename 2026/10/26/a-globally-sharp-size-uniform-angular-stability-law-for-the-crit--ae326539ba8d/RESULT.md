# A globally sharp, size-uniform angular stability law for the critical Bergman pole problem

## Finding
Let \(N\ge2\), and place \(N\) (not necessarily distinct) boundary poles at \(a_j=e^{i\theta_j}\), with ordered real representatives \(\theta_0\le\theta_1\le\cdots\le\theta_{N-1}<\theta_0+2\pi\). Write \(\theta_N=\theta_0+2\pi\), \(d_j=\theta_j-2\pi j/N\), and \(\bar d=N^{-1}\sum_j d_j\). Define the squared weighted Bergman energy
\[
\mathcal E_N(\boldsymbol\theta)=\frac2\pi\int_{|z|<1}\left|\sum_{j=0}^{N-1}\frac1{z-a_j}\right|^2(1-|z|^2)\,dA(z).
\]
For \(\boldsymbol\theta^*=(0,2\pi/N,\ldots,2\pi(N-1)/N)\) and \(c_*=2\log2-1\), the following **global**, **dimension-uniform**, quantitatively sharp inequality holds:
\[
\boxed{\mathcal E_N(\boldsymbol\theta)-\mathcal E_N(\boldsymbol\theta^*)\ge c_*N\sum_{j=0}^{N-1}(d_j-\bar d)^2.}
\]
Equality holds precisely for rotations of regular \(N\)-gons. The coefficient \(c_*\) cannot be increased simultaneously for all \(N\ge2\): it is approached at \(N=2\) by infinitesimal perturbations of antipodal poles.

More precisely, define the even, continuous, \(2\pi\)-periodic potential
\[
\Phi(t)=2\sum_{m=1}^\infty\frac{\cos(mt)}{m(m+1)},\qquad \Phi(0)=2,
\]
and, for \(1\le r<N\), set \(u_r=2\pi r/N\), \(\theta_{j+N}=\theta_j+2\pi\), and \(\sigma_{j,r}=\theta_{j+r}-\theta_j\). There is an exact positive-remainder decomposition
\[
\boxed{\mathcal E_N(\boldsymbol\theta)-\mathcal E_N(\boldsymbol\theta^*)-c_*N\sum_j(d_j-\bar d)^2
=\sum_{r=1}^{N-1}\sum_{j=0}^{N-1}(\sigma_{j,r}-u_r)^2\int_0^1(1-t)\bigl[\Phi''(u_r+t(\sigma_{j,r}-u_r))-c_*\bigr]dt\ge0.}
\]
At endpoints of the angular interval, the integral is interpreted as its convergent improper integral.

## Assumptions and scope
The planar measure \(dA\) is unnormalized Lebesgue area. The weight and factor \(2/\pi\) are part of the normalization; the theorem concerns the Hilbertian weighted Bergman square with weight \(1-|z|^2\), not unweighted \(L^1\) or other exponents. Angles are in radians and their ordered representatives occupy one half-open full turn; repeated poles are allowed. The right-hand side is unchanged under rigid rotation and cyclic relabeling. The ambient measure is finite and all pole fractions belong to this weighted Hilbert space. For \(N=1\) the inequality would be trivial, so sharpness is asserted over \(N\ge2\).

## Proof
**1. Exact Hilbert-to-pair-potential reduction.** For \(m\ge1\), the coefficient of \(z^{m-1}\) in \(\sum_j(z-e^{i\theta_j})^{-1}\) has modulus \(\left|\sum_je^{-im\theta_j}\right|\). Direct polar integration gives
\[
\frac2\pi\int_{|z|<1}|z|^{2m-2}(1-|z|^2)dA(z)=\frac2{m(m+1)}.
\]
Orthogonality of monomials and absolute convergence (since the squared coefficients are at most \(N^2\)) therefore yield
\[
\mathcal E_N(\boldsymbol\theta)=\sum_{m\ge1}\frac2{m(m+1)}\left|\sum_je^{im\theta_j}\right|^2
=2N+\sum_{j\ne k}\Phi(\theta_k-\theta_j).
\]
Every ordered pair \((j,k)\), \(j\ne k\), occurs once as \((j,j+r\bmod N)\) for \(1\le r<N\). By periodicity, the last term equals \(\sum_{r=1}^{N-1}\sum_j\Phi(\sigma_{j,r})\), with \(\sigma_{j,r}\in[0,2\pi]\). At a regular polygon each such arc equals \(u_r\). Thus the energy deficit is the sum over \(r,j\) of \(\Phi(\sigma_{j,r})-\Phi(u_r)\).

**2. Exactly sharp global curvature floor.** The absolutely convergent Fourier series defines a continuous potential. For \(0<t<2\pi\), the identity
\[
\Phi(t)=2\operatorname{Re}\left[1+(e^{-it}-1)\log(1-e^{it})\right]
\]
shows that it is smooth away from the endpoints. Differentiating this expression, or taking Abel limits of its differentiated Fourier series, gives
\[
\Phi''(t)=\int_0^1\frac{1-s^2}{1-2s\cos t+s^2}\,ds.
\]
For every \(s\in(0,1)\), the denominator is bounded above by \((1+s)^2\), with equality precisely at \(t=\pi\). Therefore
\[
\Phi''(t)\ge\int_0^1\frac{1-s^2}{(1+s)^2}\,ds
=\int_0^1\frac{1-s}{1+s}\,ds
=2\log2-1=c_*,
\]
with equality only at \(t=\pi\). In particular, \(t\mapsto\Phi(t)-c_*t^2/2\) is convex on \((0,2\pi)\). Its continuous extension to \([0,2\pi]\) remains convex. The possible logarithmic divergence of \(\Phi''\) at the endpoints is integrable: from the representation, \(\Phi''(t)=O(1+|\log t|+|\log(2\pi-t)|)\) there. Consequently, Taylor's formula with integral remainder extends even to colliding-pole configurations:
\[
\Phi(x)-\Phi(u)-\Phi'(u)(x-u)-\frac{c_*}{2}(x-u)^2
=(x-u)^2\int_0^1(1-t)[\Phi''(u+t(x-u))-c_*]dt.
\]
It is nonnegative and is strictly positive whenever \(x\ne u\) (as the Hessian floor is strict except at a single angular point).

**3. Cyclic arc balancing and exact variance identity.** For fixed \(1\le r<N\), each cyclic gap \(\theta_{j+1}-\theta_j\) contributes to exactly \(r\) of the arcs \(\sigma_{j,r}\). Their sum therefore is \(2\pi r=Nu_r\), so \(\sum_j(\sigma_{j,r}-u_r)=0\). Summing the Taylor formula from Step 2 over \(j\) cancels all first-order terms and gives a lower bound \(\frac{c_*}{2}\sum_j(\sigma_{j,r}-u_r)^2\), as well as the stated positive remainder.

Extend \(d_j\) periodically to every integer using \(d_{j+N}=d_j\). From the lifted-angle convention, \(\sigma_{j,r}-u_r=d_{j+r}-d_j\). Summing squares over all nonzero cyclic steps gives the exact finite identity
\[
\sum_{r=1}^{N-1}\sum_{j=0}^{N-1}(d_{j+r}-d_j)^2
=\sum_{j,k=0}^{N-1}(d_k-d_j)^2
=2N\sum_j(d_j-\bar d)^2.
\]
Combining this identity with the potential-energy reduction gives both the boxed global bound and the full positive-remainder identity.

**4. Equality and optimal universal coefficient.** If the energy deficit equals the lower bound, each nonnegative Taylor remainder in Step 2 vanishes. Since strictness fails only at \(t=\pi\), every \(\sigma_{j,r}=u_r\); in particular, every consecutive gap is \(2\pi/N\). Hence the poles form a rotated regular polygon. The converse is immediate.

To prove optimality, use \(N=2\), \(\theta_0=0\), \(\theta_1=\pi+\varepsilon\), \(|\varepsilon|<\pi\). Then \(d_0=0\), \(d_1=\varepsilon\), so \(N\sum_j(d_j-\bar d)^2=\varepsilon^2\). The pairwise-potential reduction gives
\[
\mathcal E_2(0,\pi+\varepsilon)-\mathcal E_2(0,\pi)=2[\Phi(\pi+\varepsilon)-\Phi(\pi)]
=\Phi''(\pi)\varepsilon^2+o(\varepsilon^2)=c_*\varepsilon^2+o(\varepsilon^2).
\]
No larger constant works uniformly over all \(N\) and configurations, completing the proof.

## Verification
All identities in the proof are exact. Independent numerical consistency diagnostics of the closed-form potential were run over 500 reproducibly seeded randomly sampled pole configurations for each \(N\in\{2,3,4,7,13\}\), including configurations with unequal cyclic gaps; every observed deficit-to-variance ratio exceeded \(2\log2-1\). The three explicit antipodal perturbations of sizes \(10^{-1}\), \(10^{-2}\), and \(10^{-3}\) gave normalized deficit ratios approaching \(c_*\). These finite checks are supplementary and are not used as proofs of the universal inequality or equality characterization. Analytic validity includes coincident poles by continuity and integrable logarithmic endpoint behavior.

## Relationship to prior work
Abakumov, Borichev, and Fedorovskiy (2020/2021) proved that regular polygons uniquely minimize this energy and gave the underlying angular interaction's convexity. Corbett (2026) supplied new calculus and universal-discrete-energy proofs of minimization, including a Hessian-based positivity argument; these are **qualitative minimization** statements. The 2026 mathematical note *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles* gives the **sharp configuration-dependent local Hessian modulus**, valid only for infinitesimal perturbations near each fixed regular polygon. The present statement differs in implication: it provides a **single exact best coefficient for every size and every pole configuration, including collisions**, controls the globally optimal ordered angular discrepancy, and supplies a nonnegative exact global remainder decomposition. Its universal coefficient is independently shown sharp at two poles. The local Hessian formula alone does not imply the global inequality. This work does not claim the earlier minimization theorem, strict convexity, or local Hessian spectrum as new.

## Limitations
The coefficient is sharp **uniformly over all \(N\ge2\)**, not claimed to be sharp separately for each fixed \(N>2\). The method depends on the special critical Hilbert Bergman weight and does not establish any corresponding stability law for the original unweighted \(L^1\) Chui conjecture or arbitrary powers. The discrepancy uses an ordered angular lift, not unordered Euclidean chordal distances. No independent audit has been performed. Earlier unindexed applications of strong convexity to this same quantitative pole discrepancy are a residual priority risk; quantitative stability is a natural consequence of the earlier convexity structure but the precise global optimal bound was not found in the inspected sources.

## References
1. Georgia Corbett, *Two new proofs of Chui's Conjecture in Weighted Bergman Spaces*, arXiv:2609.21121v1, first public 2026-09-17, https://arxiv.org/abs/2609.21121 (Sections 1.1, 2.3, 3).
2. E. Abakumov, A. Borichev, K. Fedorovskiy, *Chui's conjecture in Bergman spaces*, arXiv:2009.01898, first public 2020-09-03, https://arxiv.org/abs/2009.01898 (interaction convexity and equispaced minimization).
3. *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles* (2026), publicly indexed mathematical research note; complete statement and proof consulted, with comparison of local and global implications.
4. E. Bezrukov, *Proof of the generalized Chui conjecture*, arXiv:2609.03134v1, first public 2026-09-02, https://arxiv.org/abs/2609.03134 (broader qualitative minimization).
