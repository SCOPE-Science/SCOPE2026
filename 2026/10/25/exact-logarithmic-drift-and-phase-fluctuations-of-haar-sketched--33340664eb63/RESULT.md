# Exact logarithmic drift and phase fluctuations of Haar-sketched Euler rotation

## Finding

For the planar oscillator \(\dot x=\omega Jx\) with \(\omega>0\) and \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), sample an independent uniformly oriented one-dimensional subspace at every step. For step length \(h>0\), gain \(g>0\), and orthogonal projector \(P_k=u_ku_k^{\mathsf T}\), consider
\[
 x_{k+1}=(I+g h\omega P_kJ)x_k,\qquad u_k=(\cos\Theta_k,\sin\Theta_k)^{\mathsf T},\quad \Theta_k\overset{\mathrm{iid}}{\sim}\operatorname{Unif}[0,2\pi).
\]
The choice \(g=1\) is the single-direction Haar right-sketched Euler least-squares update with an identity parameter Jacobian; \(g=2\) compensates its expected half-size increment. Put \(t=g\omega h/2\). For every fixed deterministic \(x_0\ne0\), identify \(x_k\) with \(z_k\in\mathbb C\). There exist independent uniform \(\phi_k\in[0,2\pi)\) such that the **entire finite-step complex law** is
\[
 \frac{z_n}{z_0}\ \overset{d}{=}\ \prod_{k=0}^{n-1}\bigl[1+it(1-e^{i\phi_k})\bigr]. \tag{1}
\]
All factors lie in the closed upper half-plane and are nonzero. Define a continuous, additive unwrapped numerical phase \(\Phi_n=\arg z_0+\sum_{k<n}\arg(z_{k+1}/z_k)\), taking the factor arguments in \([0,\pi)\), and \(R_n=\log(|z_n|/|z_0|)\). Then, with \(q=t^2/(1+t^2)\),
\[
 \begin{split}
 \mathbb E(R_n,\Phi_n-\Phi_0)&=n\bigl(\tfrac12\log(1+t^2),\arctan t\bigr),\\
 \operatorname{Cov}(R_n,\Phi_n-\Phi_0)&=\frac n2\operatorname{Li}_2(q)I_2,\\
 \mathbb E z_n&=(1+it)^n z_0,\qquad
 \mathbb E|z_n|^2=(1+2t^2)^n|z_0|^2.
 \end{split}\tag{2}
\]
Here \(\operatorname{Li}_2(q)=\sum_{j\ge1}q^j/j^2\). For each fixed \(t>0\), the centered two-dimensional pair \((R_n,\Phi_n-\Phi_0)\), divided by \(\sqrt n\), converges to an isotropic Gaussian with covariance \(\tfrac12\operatorname{Li}_2(q)I_2\), while its ratio to \(n\) converges almost surely to the means in (2). Thus the almost-sure radial Lyapunov exponent is **strictly positive** for every positive step length, despite the exact oscillator preserving \(|x|\) and every realized numerical update having determinant one.

For the mean-unbiased choice \(g=2\) and any fixed \(T>0\), take \(n_h=\lfloor T/h\rfloor\). The mean-square error at the actual grid time has the **sharp limit**
\[
 \lim_{h\downarrow0}\frac{\mathbb E|z_{n_h}-e^{i\omega n_hh}z_0|^2}{h}=\omega^2T|z_0|^2.\tag{3}
\]
Moreover, the centered logarithmic radius and unwrapped phase, each divided by \(\sqrt h\), converge jointly to a zero-mean normal vector with covariance \((\omega^2 T/2)I_2\). Thus the compensated scheme has an exact positive leading strong-error constant and a matched radial/phase fluctuation law; neither is supplied by a generic mean-square upper bound.

## Assumptions and scope

Only the real planar, noiseless, constant-frequency oscillator and independently resampled Haar lines are considered. Angles are independently uniform and the initial state is deterministic, nonzero, and independent of the sketches. The scheme uses one Haar line per Euler step and exact arithmetic. The gain \(g\) is fixed; \(g=1\) corresponds to the unmodified least-squares sketch, and \(g=2\) to a rescaling that makes the mean increment equal to the oscillator vector field. Phase is **unwrapped**, not reduced modulo \(2\pi\); its increment is the principal argument of a nonzero complex factor. Every statement is for \(\omega,h,g>0\), \(n\in\mathbb N\) unless the specific limiting regime is stated. The zero initial state remains zero and is excluded from logarithmic statements.

## Proof

**1. Complex reduction and independence.** For \(z=re^{i\psi}\) and \(u=e^{i\Theta}\), the orthogonal projection of \(i z\) onto the real line spanned by \(u\) equals \(r\sin(\Theta-\psi)e^{i\Theta}\). Hence, with \(\alpha=\Theta-\psi\),
\[
 z^+=z+2t r\sin\alpha\,e^{i\Theta}
 =z\,[1+it(1-e^{2i\alpha})].\tag{4}
\]
Conditional on the entire past, \(2(\Theta_k-\psi_k)\pmod{2\pi}\) is uniform; its conditional distribution does not depend on the past. Induction shows that the complex multiplicative factors in (4) are independent and identically distributed. Their circle has center \(c=1+it\) and radius \(t<|c|\), so it never contains zero. Its imaginary part lies in \([0,2t]\), ensuring that the principal logarithm is continuous on this circle and the factor argument lies in \([0,\pi)\).

**2. Exact joint logarithmic moments.** With \(w=it/(1+it)\), one has \(|w|<1\) and, for a uniform angle \(\phi\),
\[
 \log[1+it(1-e^{i\phi})]
 =\log(1+it)-\sum_{j=1}^{\infty}\frac{w^j e^{ij\phi}}{j}.\tag{5}
\]
The expansion is uniform in \(\phi\). Both sides choose the branch continuous on the factor circle, equal to \(\log(1+it)\) on average. Fourier orthogonality gives
\[
 \mathbb E(L-\mathbb EL)=0,\qquad
 \mathbb E\,|L-\mathbb EL|^2=\sum_{j\ge1}\frac{|w|^{2j}}{j^2}=\operatorname{Li}_2(q),\qquad
 \mathbb E(L-\mathbb EL)^2=0.\tag{6}
\]
Writing \(L=X+iY\), the final equality forces \(\operatorname{Var}X=\operatorname{Var}Y\) and \(\operatorname{Cov}(X,Y)=0\). Also \(\operatorname{Re}\log(1+it)=\tfrac12\log(1+t^2)\), \(\operatorname{Im}\log(1+it)=\arctan t\). Summing independent factors yields the first two identities in (2), the strong law, and the ordinary bivariate central limit theorem. The increment is bounded at each fixed \(t\), so all stated moments exist.

**3. Complex and energy moments, and area.** Since \(\mathbb Ee^{i\phi}=0\), \(\mathbb Em=1+it\) and \(\mathbb E|m|^2=|1+it|^2+t^2=1+2t^2\), proving the last two identities in (2) by independence. In fact, the one-step squared amplification has the translated arcsine law supported on
\[
 \left[(\sqrt{1+t^2}-t)^2,(\sqrt{1+t^2}+t)^2\right],\tag{7}
\]
with density \(1/[\pi\sqrt{(v-v_-)(v_+-v)}]\) between its endpoints. The real step matrix is \(M=I+2tuu^{\mathsf T}J\). The matrix determinant lemma gives \(\det M=1+2t u^{\mathsf T}Ju=1\). Nevertheless, \(\tfrac12\log(1+t^2)>0\), showing strict pathwise exponential radial growth for each fixed nonzero initial state on a probability-one event.

**4. Fixed-time error and Gaussian small-step limit.** When \(g=2\), \(t=\omega h\), and the exact oscillator at the grid time is \(e^{i\omega nh}z_0\). Expanding the squared error and taking expectations yields the exact formula
\[
 \frac{\mathbb E|z_n-e^{i\omega nh}z_0|^2}{|z_0|^2}
 =(1+2\omega^2h^2)^n+1
 -2\operatorname{Re}\bigl[(1+i\omega h)^n e^{-i\omega nh}\bigr].\tag{8}
\]
For \(n=n_h\) one has \(nh\to T\). Taylor expansion of \(\log(1+2\omega^2 h^2)\) and \(\log(1+i\omega h)-i\omega h\) gives, respectively, \(2\omega^2Th+o(h)\) and \(\tfrac12\omega^2Th+o(h)\), proving (3). For the centered log-radius/phase triangular array, (6) and \(q=\omega^2h^2+O(h^4)\) give total covariance \(n_h(\omega^2h^2/2+O(h^4))I_2\). Each centered increment is uniformly \(O(h)\), so after division by \(\sqrt h\) it satisfies Lindeberg's condition; the triangular-array central limit theorem gives the stated \((\omega^2T/2)I_2\) limit. No finite-sample simulation is used to infer these limits.

## Verification

The standalone `verify.py` uses only the Python standard library. It compares the Fourier and moment predictions to deterministic angular trapezoidal integration at six strengths (six identities at each strength), validates 400 independently constructed real-vector updates against (4), checks 400 area-preservation determinants, tests 6,000 independent random sample paths against the predicted log-radius mean and variance, and checks four small-step values of (8) against the limit (3). All checks passed. Run `python verify.py`. The program is confirmatory; the analytic derivation above proves the identities for all stated parameters.

## Relationship to prior work

Dong, Schwerdtner and Peherstorfer [1] introduce the Haar/right-sketched least-squares increment and study conditioning, bias, variance and mean-square time-stepping bounds. Equations (36)–(37), Proposition 3 and Theorem 1 of [1] motivate the one-dimensional identity-Jacobian specialization. They do not state the exact complex multiplicative law (1), its joint phase and radius covariance, the strictly positive invariant-area radial drift, or the sharp compensated fixed-time error constant (3). The averaging factor two is a specific transparent correction of the single-direction projection bias, not an attribution of this correction to [1].

Thiffeault [2] studies products of two fixed upper/lower shear generators and gives exponent bounds. The present matrices instead use a continuously Haar-random conjugacy class of rank-one shears; the law of a fixed-vector log increment becomes exactly i.i.d. The general random-matrix framework and selected isotropic ensembles analyzed by Forrester and Zhang [3] provide relevant background but not the specialized phase and radial joint law or numerical-integration error. The broader question of rotationally invariant random-matrix products is also studied by Dong [4]; only its abstract was accessible for direct comparison here. Earlier general random-product limit laws and elementary analytic-logarithm Fourier integrals are not claimed as novel independently; the proposed contribution is their exact joint specialization and sharp numerical-error consequence for the specified sketched oscillator.

## Limitations

The conclusions are specific to one-dimensional independent Haar sketching of a planar linear oscillator with exact arithmetic and fixed positive parameters. The area-preserving updates need not preserve oscillator energy, and positivity of the almost-sure radial rate is not a claim that every direction in the same realized matrix product expands simultaneously. The direct compensated mean-square asymptotic concerns \(n_h=\lfloor T/h\rfloor\), not arbitrary variable step sizes or higher-dimensional conservative systems. Joint log-radius and unwrapped-phase coordinates are not independent; only their covariance is diagonal. No full-text comparison with [4] was possible, leaving a residual priority risk regarding random-matrix specialization, and no independent mathematical audit has occurred.

## References

[1] Y. Dong, P. Schwerdtner and B. Peherstorfer, *Randomized time stepping of nonlinearly parametrized solutions of evolution problems*, arXiv:2512.19009v1, first public 2025-12-22, https://arxiv.org/abs/2512.19009.

[2] J.-L. Thiffeault, *Lyapunov exponents for the random product of two shears*, arXiv:1706.03398v1, https://arxiv.org/abs/1706.03398.

[3] P. J. Forrester and J. Zhang, *Lyapunov exponents for some isotropic random matrix ensembles*, arXiv:1805.05529v1, https://arxiv.org/abs/1805.05529.

[4] Q. Dong, *The Largest Lyapunov exponent for products of rotationally invariant random matrices*, *Statistics & Probability Letters* 234 (2026), 110703, DOI:10.1016/j.spl.2026.110703 (abstract-level evidence only).
