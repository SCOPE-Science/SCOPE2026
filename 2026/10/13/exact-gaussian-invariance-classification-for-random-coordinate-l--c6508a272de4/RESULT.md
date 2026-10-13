# Exact Gaussian-invariance classification for random-coordinate Langevin Euler sampling

## Finding

Let \(d\ge1\), \(H\in\mathbb R^{d\times d}\) be symmetric positive definite, \(h>0\), and \(p_i>0\) with \(\sum_{i=1}^d p_i=1\). Consider the coordinate-noise Euler sampler
\[
 X^{+}=X-\frac{h}{p_I}e_Ie_I^{\mathsf T}HX+\sqrt{\frac{2h}{p_I}}\,e_I\xi,
\qquad \Pr(I=i)=p_i,\quad \xi\sim N(0,1),
\]
where fresh \(I,\xi\) are independent of the present state at each iteration. Form the undirected graph with vertices \(1,\ldots,d\) and edges \(ij\) exactly when \(i\ne j\) and \(H_{ij}\ne0\). Let \(\mathcal C\) be its connected components and define \(T_C=\sum_{i\in C}H_{ii}\), \(P_C=\sum_{i\in C}p_i\).

**Theorem (if and only if).** The discrete-time chain has a stationary Gaussian probability distribution if and only if, for every \(C\in\mathcal C\),
\[
 p_i=\frac{P_C H_{ii}}{T_C}\quad(i\in C),
 \qquad 0<\frac{hT_C}{P_C}<2.
\]
In that case its stationary probability distribution is unique and is the centered Gaussian with block covariance
\[
 \Sigma_{CC}=\gamma_C H_{CC}^{-1},\qquad
 \gamma_C=\left(1-\frac{hT_C}{2P_C}\right)^{-1},
 \qquad \Sigma_{CC'}=0\quad(C\ne C').
\]
Thus for a *connected* precision graph the only Gaussian-preserving coordinate weights are \(p_i=H_{ii}/\operatorname{tr}H\), and they yield the exact scalar temperature inflation
\[
 \gamma=\left(1-\frac{h\operatorname{tr}H}{2}\right)^{-1},
 \qquad 0<h\operatorname{tr}H<2.
\]
This classification concerns the invariant *law*, not just its covariance. In a connected system with weights not proportional to the diagonal, if \(hH_{ii}/p_i<2\) for every coordinate, the chain still has a unique stationary distribution with finite second moment, but it is necessarily **non-Gaussian**.

When the precision graph is connected and the Gaussian-invariance condition holds, relative to the desired target \(\pi=N(0,H^{-1})\), the invariant law \(\pi_\gamma=N(0,\gamma H^{-1})\) has exact errors
\[
 D_{\mathrm{KL}}(\pi_\gamma\|\pi)=\frac d2(\gamma-1-\log\gamma),
 \qquad W_2(\pi_\gamma,\pi)=(\sqrt\gamma-1)\sqrt{\operatorname{tr}(H^{-1})}.
\]
For arbitrary components, the corresponding KL formula sums \(\frac{|C|}{2}(\gamma_C-1-\log\gamma_C)\), and squared \(W_2\) sums \((\sqrt{\gamma_C}-1)^2\operatorname{tr}(H_{CC}^{-1})\).

## Assumptions and scope

All matrices and random variables are real. The precision matrix \(H\) is strictly positive definite, the base timestep \(h\) is positive, and the iid coordinate-choice weights are strictly positive and normalized. Each innovation is an independent standard Gaussian. A stationary Gaussian law is allowed an arbitrary mean and covariance at the outset; the proof shows its mean must be zero. Each connected component is in the sparsity graph of \(H\), not a statistical independence graph defined from a covariance estimate. Since intercomponent precision entries vanish, \(H\) is block diagonal after permuting coordinates. \(H_{CC}^{-1}\) is the inverse of that principal block. No restriction on dimensionality, graph shape, or individual diagonal entries is imposed beyond the displayed hypotheses.

## Proof

**1. Stationary means and Gaussian-mixture rigidity.** Define \(\alpha_i=h/p_i\), \(D_i=I-\alpha_i e_ie_i^{\mathsf T}H\), and \(N_i=2\alpha_i e_ie_i^{\mathsf T}\). The step conditional on \(I=i\) maps \(N(\mu,\Sigma)\) to \(N(D_i\mu,D_i\Sigma D_i^{\mathsf T}+N_i)\). Stationarity of a Gaussian with finite mean forces
\[
 \mu=\sum_i p_iD_i\mu=(I-hH)\mu,
\]
so positive definiteness gives \(\mu=0\). Write \(\Sigma_i=D_i\Sigma D_i^{\mathsf T}+N_i\). If \(\sum_i p_iN(0,\Sigma_i)=N(0,\Sigma)\), then for each \(v\in\mathbb R^d\), the second and fourth centered moments of \(v^{\mathsf T}X\) give
\[
 v^{\mathsf T}\Sigma v=\sum_i p_i v^{\mathsf T}\Sigma_i v,
 \qquad (v^{\mathsf T}\Sigma v)^2
 =\sum_i p_i(v^{\mathsf T}\Sigma_i v)^2.
\]
The weighted variance of the values \(v^{\mathsf T}\Sigma_i v\) is therefore zero. Since all \(p_i>0\), each equals \(v^{\mathsf T}\Sigma v\) for every \(v\), so **each** \(\Sigma_i=\Sigma\). This argument needs no nondegeneracy assumption on the component Gaussians. Indeed, their common stationary covariance is in fact positive definite: from \(\Sigma=\Sigma_i\succeq2lpha_i e_ie_i^{\mathsf T}\) for every \(i\), its range contains every basis vector.

**2. Off-diagonal restrictions.** For a fixed update of coordinate \(i\), preservation of the \((i,j)\) covariance for every \(j\ne i\) yields
\[
 \Sigma_{ij}-\alpha_i(H\Sigma)_{ij}=\Sigma_{ij},
\]
so \((H\Sigma)_{ij}=0\). Repeating for all \(i\) shows \(H\Sigma=D=\operatorname{diag}(\delta_1,\ldots,\delta_d)\). Symmetry of \(\Sigma=H^{-1}D\) gives \(DH=HD\). Hence \((\delta_i-\delta_j)H_{ij}=0\); connectivity forces \(\delta_i=\gamma_C\) for all \(i\in C\). Consequently \(\Sigma_{CC}=\gamma_C H_{CC}^{-1}\) and cross-component blocks vanish. Each \(\gamma_C>0\), as follows already from the variance balance with nonzero noise below (or from positive definiteness of a Gaussian stationary law).

**3. Diagonal restrictions and the boundary.** Preservation of the \((i,i)\) covariance, using \((H\Sigma)_{ii}=\gamma_C\) and \((H\Sigma H)_{ii}=\gamma_CH_{ii}\), gives
\[
 0=-2\alpha_i\gamma_C+\alpha_i^2\gamma_C H_{ii}+2\alpha_i,
 \qquad
 \gamma_C=\frac{1}{1-\alpha_i H_{ii}/2}.
\]
For a finite positive \(\gamma_C\), necessarily \(0<\alpha_iH_{ii}<2\). Constancy of \(\gamma_C\) on \(C\) forces \(hH_{ii}/p_i\) constant for \(i\in C\). Summing the weights yields precisely \(p_i=P_CH_{ii}/T_C\) and the common value \(hT_C/P_C\), strictly below \(2\). Thus every stated condition is necessary, including all boundary strictness.

**4. Sufficiency.** Suppose the displayed conditions hold. Under \(N(0,\Sigma)\), conditional on all other coordinates, \(X_i\) has mean \(-\sum_{j\ne i}H_{ij}X_j/H_{ii}\) and variance \(\gamma_C/H_{ii}\). The coordinate update is an autoregression about that unchanged conditional mean, with multiplier \(r_C=1-hT_C/P_C\). Its innovation variance is \(2h/p_i\). Directly,
\[
 r_C^2\frac{\gamma_C}{H_{ii}}+\frac{2h}{p_i}
 =\frac{\gamma_C}{H_{ii}}.
\]
Every selected-coordinate kernel therefore preserves the full proposed Gaussian law individually. Their mixture does too.

**5. Uniqueness and non-Gaussian alternatives.** Assume the stronger coordinatewise stability condition \(0<\alpha_iH_{ii}<2\), whether or not the probabilities are proportional to the diagonals. Under synchronous coupling of two chains, their difference \(z\) satisfies \(z^+=D_Iz\) and has exact conditional energy decrement
\[
 \mathbb E[\|z^+\|_H^2\mid z]
 =\|z\|_H^2
 -\sum_i h(2-\alpha_iH_{ii})((Hz)_i)^2
 \le(1-\eta\lambda_{\min}(H))\|z\|_H^2,
\]
where \(\eta=\min_i h(2-\alpha_iH_{ii})>0\). This strict mean-square contraction, together with the finite second moment of the Gaussian innovation, gives an invariant probability law in \(\mathcal P_2\) by the contraction theorem and makes it unique there. The same coupling and convergence in probability from any deterministic initial point give uniqueness of an invariant law without a moment assumption, by bounded-continuous test functions. If diagonal weights violate the componentwise criterion, steps 1–3 preclude any Gaussian invariant. Hence whenever coordinatewise stability holds, its unique invariant distribution is non-Gaussian.

The KL formula is the standard trace-and-log-determinant formula for centered Gaussians applied to a scalar covariance inflation. The Wasserstein formula follows from the commuting covariance matrices and Gaussian quadratic transport; with multiple blocks it adds by independence.

## Verification

The standalone script `verify.py` uses exact SymPy rational arithmetic. It verifies coordinatewise covariance preservation for four nontrivial rational precision/probability models, solves their stationary covariance linear equations, and checks covariance iteration. For the connected model
\[
 H=\begin{pmatrix}1&1/2\\1/2&2\end{pmatrix},\qquad h=\frac14,
\]
weights \((1/3,2/3)\) give \(\gamma=8/5\) and exact Gaussian invariance. Uniform weights \((1/2,1/2)\) satisfy strict coordinatewise stability but yield stationary covariance
\[
 \Sigma=\frac1{539}\begin{pmatrix}848&-240\\-240&592\end{pmatrix}.
\]
If one incorrectly assumes this latter stationary law is Gaussian, a single update produces a centered Gaussian mixture whose fourth moment along \(v=(1,1)\) exceeds the fourth moment of \(N(0,v^{\mathsf T}\Sigma v)\) by exactly \(192/5929\). That contradiction is a finite algebraic witness to the non-Gaussian statement. Executing `python verify.py` produced `PASS 144 symbolic stationarity, covariance, and monotonicity checks`. These finite checks verify algebra and examples only; the universal iff classification is proved above.

## Relationship to prior work

Ding, Li, Lu and Wright [1, §§2–4 and Appendix] introduce precisely the coordinate-only Euler/independent Gaussian-noise sampler analyzed here, with \(\alpha_i=h/p_i\), and obtain non-asymptotic Wasserstein convergence bounds and directional-Lipschitz sampling advice. On a quadratic, their suggested sampling probabilities are proportional to \(H_{ii}\). Their actual theorem bounds and Gaussian lower-bound example do not state an iff classification for Gaussian invariant *laws* on correlated precision graphs, exact finite-stepsize invariant temperatures, or the non-Gaussian conclusion for alternate stable weights. Thus a familiar recommendation has a distinct, structural invariant-law characterization.

Ding and Li [2] study a different random-coordinate **gradient estimator with full-dimensional noise at each step**, so its transition kernel is not [1]'s coordinate-only-noise transition. Continuous-time coordinate and block diffusion and the random-coordinate underdamped scheme [3] likewise do not imply this discrete-time Gaussian-mixture iff condition. The published numerical-analysis literature contains Gaussian stationary-covariance calculations for various Langevin integrators and standard Gaussian-mixture identifiability results; neither technique is presented as new in isolation. The claimed contribution is the complete graph-component classification for this named coordinate sampler, together with its exact inflation and rigorous non-Gaussian alternative. A logically equivalent theorem in broader random-scan Gaussian autoregression/conditional-MCMC literature remains a priority risk despite searching equivalent formulations.

## Limitations

The claim concerns an **unadjusted**, exact-arithmetic coordinate Euler discretization with iid coordinate indices and fresh independent normal innovations, on a positive-definite quadratic target. A non-Gaussian invariant may have useful covariance or smaller approximation error under a metric; the theorem does not rank alternate samplers, prove their optimal probabilities, or assert poor efficiency. No corresponding classification is established for general nonlinear potentials, Metropolized samplers, correlated coordinate selections, arbitrary noise scaling, finite-precision arithmetic, or all unstable stepsizes. The Gaussian-invariance condition has a strict stepsize boundary and does not apply at equality. The role of the component graph matters: for disconnected systems, multiple componentwise temperatures can coexist in one Gaussian invariant and coordinate probabilities need not be globally proportional to the diagonal. Originality against all unpublished or unindexed literature cannot be guaranteed.

## References

1. Z. Ding, Q. Li, J. Lu and S. J. Wright, *Random Coordinate Langevin Monte Carlo*, arXiv:2010.01405v1 (first public 2020-10-03), https://arxiv.org/html/2010.01405v1 ; https://arxiv.org/abs/2010.01405 .
2. Z. Ding and Q. Li, *Langevin Monte Carlo: random coordinate descent and variance reduction*, arXiv:2007.14209 (2020), https://arxiv.org/abs/2007.14209 .
3. Z. Ding, Q. Li, J. Lu and S. J. Wright, *Random Coordinate Underdamped Langevin Monte Carlo*, arXiv:2010.11366 (2020), https://arxiv.org/abs/2010.11366 .
4. A. Durmus and É. Moulines, *Nonasymptotic convergence analysis for the unadjusted Langevin algorithm*, Annals of Applied Probability 27 (2017), https://doi.org/10.1214/16-AAP1238 .
