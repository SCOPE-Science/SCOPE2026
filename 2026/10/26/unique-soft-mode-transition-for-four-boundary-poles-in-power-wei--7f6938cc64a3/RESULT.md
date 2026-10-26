# Unique soft-mode transition for four boundary poles in power-weighted Bergman energy

## Finding
For \(\alpha>2\), put
\[
\mathcal E_\alpha(\boldsymbol\theta)=\frac{\alpha+1}{\pi}\int_{|z|<1}
\left|\sum_{j=0}^{3}\frac{1}{z-e^{i\theta_j}}\right|^2
(1-|z|^2)^\alpha\,dA(z),
\]
where \(dA\) is ordinary planar area, and let \(\boldsymbol\theta^\star=(0,\pi/2,\pi,3\pi/2)\). Define positive rational functions for \(0<t<1\) by
\[
A(t)=\frac{1-t}{(1+t)^3},\qquad
B(t)=\frac{4t(1-t^2)}{(1+t^2)^3},
\]
and the real function
\[
F(\alpha)=(\alpha+1)\int_0^1(1-t)^\alpha[A(t)-B(t)]\,dt.
\]
There is exactly one \(\alpha_*\in(2,3)\) with \(F(\alpha_*)=0\) (numerically \(\alpha_*\approx2.727841735935\)). The full real angle Hessian at \(\boldsymbol\theta^\star\) has the rotation eigenvalue \(0\), the eigenvalue
\[
\lambda_1(\alpha)=4(\alpha+1)\int_0^1(1-t)^\alpha[A(t)+B(t)]\,dt>0
\]
of multiplicity two, and the eigenvalue
\[
\lambda_2(\alpha)=8(\alpha+1)\int_0^1(1-t)^\alpha B(t)\,dt>0
\]
of multiplicity one. Their exact difference is \(\lambda_1-\lambda_2=4F(\alpha)\). Thus the least nonrotational eigenvalue is \(\lambda_1\) for \(2<\alpha<\alpha_*\), equals \(\lambda_1=\lambda_2\) at \(\alpha_*\), and is \(\lambda_2\) for \(\alpha>\alpha_*\). At the transition the Hessian is a positive scalar multiple of the identity on the three-dimensional mean-zero angle subspace.

Consequently, for each fixed \(\alpha>2\), the **sharp local quadratic stability coefficient** after quotienting common rotation is \(\tfrac12\min\{\lambda_1(\alpha),\lambda_2(\alpha)\}\). The minimizing perturbation changes from a two-dimensional first-Fourier-mode family to the alternating second-Fourier mode at exactly the unique transition exponent.

## Assumptions and scope
All poles are unit-strength, initially distinct, and constrained to the unit circle. Angles are real and measured in radians. The norm is normalized by \(1/\pi\) so that its monomial moments have no extraneous area factor. The calculation concerns four poles, all \(\alpha>2\), and perturbations sufficiently close to \(\boldsymbol\theta^\star\); it is not a theorem about arbitrary numbers of poles or global quantitative stability. The strict restriction \(\alpha>2\) ensures termwise twice differentiability of the convergent moment series used below.

The first-mode eigenspace is spanned by \((1,0,-1,0)\) and \((0,1,0,-1)\); the alternating eigenspace is spanned by \((1,-1,1,-1)\); the rotation kernel is spanned by \((1,1,1,1)\). These subspaces are orthogonal and exhaust \(\mathbb R^4\).

## Proof
**1. Moment reduction and the complete Hessian.** For \(k\ge1\), let
\[
w_{k-1}(\alpha)=(\alpha+1)\int_0^1t^{k-1}(1-t)^\alpha\,dt
=\frac{\Gamma(\alpha+2)\Gamma(k)}{\Gamma(k+\alpha+1)}.
\]
Expanding \((z-e^{i\theta_j})^{-1}\) into powers of \(z\) inside the disk and integrating the angular Fourier modes gives the exact nonnegative series
\[
\mathcal E_\alpha(\boldsymbol\theta)
=\sum_{k=1}^\infty w_{k-1}(\alpha)
\left|\sum_{j=0}^3e^{ik\theta_j}\right|^2.
\]
Since \(k^2w_{k-1}(\alpha)=O_\alpha(k^{1-\alpha})\), the twice differentiated series converges absolutely and uniformly when \(\alpha>2\). Write \(S_k=\sum_j e^{ik\theta_j^\star}=4\mathbf1_{4\mid k}\) and, for a real perturbation \(u\), write \(U_k=\sum_j u_je^{ik\theta_j^\star}\). Direct differentiation yields
\[
D^2\mathcal E_\alpha(\boldsymbol\theta^\star)[u,u]
=2\sum_{k\ge1}k^2w_{k-1}(\alpha)
\left(|U_k|^2-4\mathbf1_{4\mid k}\sum_{j=0}^3u_j^2\right).
\]
Cyclic symmetry and rotation invariance make the Hessian circulant with a zero rotation mode. Set \(s_r=\sum_{k\ge1,\,k\equiv r\pmod4}k^2w_{k-1}(\alpha)\) for \(r=0,1,2,3\). Substituting the first-Fourier and alternating vectors into the displayed Hessian shows that their Rayleigh eigenvalues are exactly
\[
\lambda_1=4(s_1+s_3-2s_0),\qquad
\lambda_2=8(s_2-s_0).
\]
Together with the rotation mode, these give the entire real spectrum, with multiplicities \(1,2,1\).

**2. Positive integrals.** The generating function
\[
\sum_{k\ge1}k^2t^{k-1}z^k=\frac{z(1+tz)}{(1-tz)^3},\qquad |t|<1,\ |z|=1,
\]
has the two real values
\[
\sum_{k\ge1}k^2t^{k-1}(-1)^k=-A(t),\qquad
\sum_{k\ge1}k^2t^{k-1}\cos(k\pi/2)=-B(t).
\]
The exact residue-class identities
\[
\mathbf1_{k\equiv1,3\,(4)}-2\mathbf1_{k\equiv0\,(4)}
=-\cos(k\pi/2)-\cos(k\pi),
\]
\[
\mathbf1_{k\equiv2\,(4)}-\mathbf1_{k\equiv0\,(4)}=-\cos(k\pi/2)
\]
then yield the two integral formulas in the finding, by exchanging the absolutely convergent sum and the beta integral. Both \(A(t)\) and \(B(t)\) are strictly positive for \(0<t<1\), proving all nonrotational Hessian eigenvalues strictly positive.

**3. One and only one transition.** Their ratio satisfies
\[
R(t)=\frac{B(t)}{A(t)}=\frac{4t(1+t)^4}{(1+t^2)^3},\qquad
\frac{R'(t)}{R(t)}=\frac{(1-t)(t^2+6t+1)}{t(1+t)(1+t^2)}>0.
\]
As \(t\downarrow0\), \(R(t)\to0\), while \(R(t)\to8\) as \(t\uparrow1\). Therefore a unique \(\tau\in(0,1)\) satisfies \(R(\tau)=1\), and \(A-B\) is positive before \(\tau\) and negative after \(\tau\).

Suppose \(F(\alpha_0)=0\) for some \(\alpha_0>2\). If \(\alpha>\alpha_0\), the factor \(q(t)=(1-t)^{\alpha-\alpha_0}\) is strictly decreasing. Subtracting its constant value \(q(\tau)\) under the vanishing \(\alpha_0\)-integral gives
\[
\frac{F(\alpha)}{\alpha+1}=
\int_0^1(1-t)^{\alpha_0}[A(t)-B(t)]
[q(t)-q(\tau)]\,dt>0.
\]
The strict sign follows because the two bracketed factors have the same sign off \(\tau\). For \(\alpha<\alpha_0\) the multiplier is increasing and the sign is negative. Hence there is **at most one** zero, and any zero has the asserted sign transition.

To prove existence, elementary rational partial-fraction integration gives the exact continuous endpoint values
\[
F(2)=24\log2-12-\frac{3\pi}{2}<0,\qquad
F(3)=120\log2+6\pi-102>0.
\]
These inequalities have a standard-library exact-rational certificate in `check_transition.py`: the file verifies the partial fraction identities at twelve distinct rational points (more than the cleared polynomial degree), and encloses \(\pi\) and \(\log2\) in rational intervals using Machin's arctangent identity and the positive artanh series. Continuity supplies a zero strictly between \(2\) and \(3\); uniqueness and its sign pattern follow above. The value at \(2\) is used **only as the continuous endpoint of the integral**, not as a claim of twice termwise differentiability at that endpoint.

**4. Sharpness and isotropy.** Each positive eigenspace gives an actual real perturbation of the four distinct angles. At \(\boldsymbol\theta^\star\), the gradient vanishes by cyclic symmetry and rotation invariance. Twice continuous differentiability supplies
\[
\mathcal E_\alpha(\boldsymbol\theta^\star+u)
-\mathcal E_\alpha(\boldsymbol\theta^\star)
=\frac12\langle Hu^\circ,u^\circ\rangle+o(\|u^\circ\|_2^2),
\]
where \(u^\circ=u-\tfrac14(\sum_j u_j)(1,1,1,1)\). The least nonzero eigenvalue gives the sharp coefficient, attained in the limit along its eigenspace. At \(\alpha_*\), all three nonrotational eigenvalues agree, which is exactly isotropy on the rotation quotient.

## Verification
The standalone standard-library script `check_transition.py` establishes the exact rational partial-fraction identities, rational enclosures for \(\pi\) and \(\log2\), and strict endpoint signs. It additionally prints a **noncertifying** Simpson-quadrature approximation to the unique exponent. The mathematical proof of existence, uniqueness, all positive eigenvalues, and exact mode switching rests on the analytic identities and the monotone single-crossing argument, not on quadrature or finite sampling. The modal formulas were also cross-checked against second central differences of finite Fourier truncations for several exponents; those numerical experiments are not part of the proof.

## Relationship to prior work
Abakumov, Borichev, and Fedorovskiy (2020) establish global equispaced-pole minimization for concave weights and determine when the power-weight interaction is strictly convex; they do not determine the four-pole soft-mode transition in the nonconvex regime \(\alpha>2\). Corbett (2026) supplies an alternative proof and global minimization for all positive power exponents using complete monotonicity, but no exact four-pole Hessian eigenvalue crossover. Bezrukov (2026) proves a broad Chui minimization theorem for radial integral functionals; minimizing locations do not determine these two Hessian eigenvalues or their ordering.

A related published result, *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles* (published-finding corpus, 2026), gives the complete spectrum at the **fixed exponent \(\alpha=1\)** for arbitrary pole number. Its first-Fourier-mode minimum at that weight does not imply a unique transition at \(\alpha_*>2\), nor isotropy of the four-pole transverse Hessian at a nontrivial weight. The present result isolates the smallest pole number with two competing nonrotational symmetry types and classifies the softest mode **over an entire continuous, nonconvex power-weight range**. Search and source comparisons do not exclude unpublished or unindexed equivalents.

## Limitations
Only exactly four unit-strength boundary poles and the displayed radial power weights are treated. The claim classifies an infinitesimal, rotation-quotiented stability coefficient, not any global quantitative estimate, nor other point counts, nor the classical unweighted \(L^1\) Chui functional. The numerical exponent is approximate; its existence and uniqueness are exact. The proof requires \(\alpha>2\) for straightforward absolute termwise Hessian differentiation, and makes no Hessian assertion at \(\alpha=2\). The literature comparison does not establish exhaustive novelty beyond the inspected, indexed sources.

## References
1. G. Corbett, *Two new proofs of Chui's Conjecture in Weighted Bergman Spaces*, arXiv:2609.21121v1, first public 2026-09-17, https://arxiv.org/html/2609.21121, Sections 1.1, 2.3, and 3.
2. E. Abakumov, A. Borichev, K. Fedorovskiy, *Chui's conjecture in Bergman spaces*, arXiv:2009.01898v1 (2020-09-03), https://arxiv.org/html/2009.01898v1, Theorem 1 and Lemma 12.
3. E. Bezrukov, *Proof of the generalized Chui conjecture*, arXiv:2609.03134v1 (2026-09-02), https://arxiv.org/html/2609.03134v1, Theorem 1 and its proof.
4. *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles*, published-finding corpus (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-full-fourier-hessian-spectrum-and-sharp-local-stability-for-equi--9aca32c3cb4f, RESULT.md.
