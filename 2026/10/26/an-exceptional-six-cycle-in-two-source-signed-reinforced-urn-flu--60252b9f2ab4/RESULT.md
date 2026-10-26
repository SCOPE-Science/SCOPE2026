# An exceptional six-cycle in two-source signed reinforced-urn fluctuations

## Finding
For the balanced, alternating-sign, two-source Bernoulli urn process defined below, every coordinate tends almost surely to \(1/2\). Nevertheless, the leading fluctuation scale has an exceptional arithmetic classification. The ordinary \(\sqrt t\) central limit theorem holds with positive definite covariance exactly for \(d=2\) and \(d=6\). For \(d=4\) and every even \(d\ge8\), an explicitly identified complex eigenprojection has a nonzero random amplitude at the slower, sharp polynomial scale \(t^{-(1-\rho_d)}\), including logarithmic phase rotation when its leading eigenvalue is nonreal. The exact spectral abscissa is
\[
\rho_d=\max_{0\le k<d/2}\frac12\sqrt{\sin(2\pi k/d)\bigl(1-\sin(6\pi k/d)\bigr)}.
\]
In particular, \(\rho_2=0\), \(\rho_6=\sqrt{\sqrt3/8}<1/2\), and \(\rho_d>1/2\) for every other even \(d\ge4\). This is a nonmonotone finite-size phase diagram within one fixed local update rule.

## Assumptions and scope
Fix an even integer \(d\ge2\), with vertex indices in \(\mathbb Z/d\mathbb Z\). At time zero every urn contains one white and one black ball; write \(Z_{t,j}\) for its white fraction at integer time \(t\ge0\). Conditionally on the complete past, \(X_{t+1,j}\), for all \(j\), are independent Bernoulli variables with parameters
\[
p_{t,j}=\frac12+\frac{(-1)^{j-1}}2\bigl(Z_{t,j-1}+Z_{t,j-2}-1\bigr).
\]
They are well-defined probabilities in \([0,1]\), and urn \(j\) receives one new white ball exactly when \(X_{t+1,j}=1\). Thus
\[
Z_{t+1,j}=Z_{t,j}+\frac{X_{t+1,j}-Z_{t,j}}{t+3}.
\]
Define the cyclic permutation matrix \(P\) by \(P_{i,j}=\mathbf1_{j=i+1\ (\mathrm{mod}\ d)}\), and the alternating sign diagonal \(Q=\operatorname{diag}((-1)^j)_{j=0}^{d-1}\). For the row vector \(x_t=(Z_{t,j}-1/2)_j\), its conditional linear drift is \(x_t(B-I)/(t+3)\), where
\[
B=\frac{I+P}{2}\,Q P=\frac Q2(P-P^2).
\]
The latter identity uses \(PQ=-QP\) and is valid only for even \(d\). The model is a minimal two-source extension of signed network reinforcement: sampling averages the current and preceding location before sending the observed colour to the next urn, with alternating preferential and complementary draws. It has no independent noise added after reinforcement.

## Proof
**1. Signed two-tap spectral identity.** The anticommutation relation implies the exact integer-matrix identity
\[
4B^2=P^4-P^2.
\]
For a Fourier mode with \(P\)-eigenvalue \(z=e^{i\theta}\), multiplication by \(Q\) sends it to the mode with eigenvalue \(-z\). Therefore the two-dimensional block has eigenvalues \(\lambda_\pm=\pm\sqrt{(z^4-z^2)/4}\). Take \(\theta=2\pi k/d\) for representatives \(0\le k<d/2\). The blocks at \(z=\pm1\) may be nilpotent; diagonalizability of the full matrix is not assumed. The spectral moduli satisfy \(|\lambda|^2=|\sin\theta|/2\le1/2\). Thus every eigenvalue of \(B\) is strictly inside the unit disk.

The square of the positive real part of the block's square root is
\[
(\operatorname{Re}\lambda_+)^2=\frac{|\lambda_+^2|+\operatorname{Re}\lambda_+^2}{2}
=\frac{\sin\theta(1-\sin3\theta)}4,
\]
because the representative angles lie in \([0,\pi)\). Maximization gives the displayed formula for \(\rho_d\).

**2. Exact finite-size threshold.** For \(d=2\), both Fourier representatives give zero spectral abscissa. For \(d=6\), the nontrivial representatives have \(\theta=\pi/3,2\pi/3\), giving \(\rho_6=\sqrt{\sqrt3/8}<1/2\). For \(d=4\), \(\theta=\pi/2\) gives \(\rho_4=1/\sqrt2>1/2\). For every even \(d\ge8\), choose a grid angle \(\theta\) within \(\pi/d\le\pi/8\) of \(\pi/2\). Then \(\sin\theta\ge\cos(\pi/8)\) and \(\sin3\theta\le-\sin(\pi/8)\). Since
\[
\cos(\pi/8)\bigl(1+\sin(\pi/8)\bigr)>1,
\]
this mode has real part strictly greater than \(1/2\). Equality to the central-limit threshold cannot occur at the spectral maximum in any even size.

**3. Almost-sure deterministic limit.** Put \(\eta_{t+1}=X_{t+1}-\mathbb E[X_{t+1}\mid\mathcal F_t]\) as a row vector. Its components are conditionally independent, centered, bounded by one, and have variances at most \(1/4\). The recursion becomes
\[
x_{t+1}=x_t\left(I+\frac{B-I}{t+3}\right)+\frac{\eta_{t+1}}{t+3}.
\]
All eigenvalues of \(I-B\) have strictly positive real parts by step 1. The corresponding continuous-time Lyapunov equation admits a positive definite solution; applying its quadratic form to the recursion gives a nonnegative almost-supermartingale with a negative drift bounded below by a positive multiple of \(\|x_t\|^2/(t+3)\) and a summable \(O((t+3)^{-2})\) error. The Robbins–Siegmund argument implies \(x_t\to0\) almost surely. In particular, the conditional noise covariance tends almost surely to \(I/4\).

**4. Gaussian sizes.** If \(\rho_d<1/2\), the drift matrix has every eigenvalue with real part less than \(-1/2\). The finite-dimensional martingale stochastic-approximation central limit theorem with step size \((t+3)^{-1}\), bounded conditional moments and limiting noise covariance \(I/4\), applies also to the possible nilpotent zero-eigenvalue block. It gives
\[
\sqrt t\,x_t\ \Longrightarrow\ \mathcal N_d(0,\Sigma_d),\qquad
\Sigma_d=\frac14\int_0^\infty e^{(B^\top-I/2)u}e^{(B-I/2)u}\,du.
\]
The integral is finite because \(\rho_d<1/2\), and strictly positive definite because the integrand at zero is the identity. The sizes are exactly \(d=2,6\) by step 2.

**5. Sharp nondegenerate amplitude at every other even size.** For an eigenvalue \(\lambda\) of \(B\) satisfying \(\operatorname{Re}\lambda=\rho_d>1/2\), choose a nonzero complex column right eigenvector \(u\), and set \(T_t=x_tu\). The exact scalar update is
\[
T_{t+1}=\left(1+\frac{\lambda-1}{t+3}\right)T_t+\frac{\eta_{t+1}u}{t+3}.
\]
Define the nonvanishing deterministic product
\[
\Pi_t=\prod_{j=1}^t\frac{j+1+\lambda}{j+2}
=\frac{\Gamma(3)\Gamma(t+2+\lambda)}{\Gamma(2+\lambda)\Gamma(t+3)}.
\]
Then \(M_t=T_t/\Pi_t\) is an exact complex martingale with square-integrable increments. Their second moments are bounded by a constant times \(t^{-2\operatorname{Re}\lambda}\), a summable sequence. Hence \(M_t\to M_\infty\) almost surely and in \(L^2\). Initially \(T_0=0\); the first update has independent fair Bernoulli innovations, so
\[
\mathbb E|M_\infty|^2\ge\mathbb E|M_1|^2
=\frac{\|u\|_2^2}{4|2+\lambda|^2}>0.
\]
The gamma-ratio asymptotic yields
\[
t^{1-\lambda}T_t\longrightarrow \frac{\Gamma(3)}{\Gamma(2+\lambda)}M_\infty
\quad\text{almost surely and in }L^2.
\]
The complex power includes the logarithmic rotation \(e^{-i\operatorname{Im}\lambda\log t}\). A nonzero second moment makes this scale sharp in probability for that projection: multiplying its magnitude by any further positive power of \(t\) cannot produce convergence to zero in probability.

## Verification
Run the standalone file `verify.py` using Python 3 and NumPy. It checks the exact cyclic anticommutation and polynomial identities for fourteen even ring sizes, tests the finite-dimensional Fourier-root formula and the exceptional threshold, and confirms the analytic uniform inequality. The recorded output is in `verification_stdout.txt`. The proof of the infinite-dimensional-in-time assertions is analytical; finitely many spectral checks are not substituted for it. The positive second moment is proved directly using the first Bernoulli innovation rather than inferred from numerical experiments.

## Relationship to prior work
Dahiya, Kaur and Sahasrabudhe (2026, arXiv:2610.13884v1) introduce the separated sampling/reinforcement model, give general deterministic-regime spectral estimates and central limit principles, and explicitly identify longer-range interaction and incomplete graph-characterization questions. This finding concerns a specific noncommuting two-source kernel and determines its exact exceptional even-size phase diagram together with nondegeneracy of the random leading amplitude. The published general superdiffusive estimate gives an upper rate but not the present positive random amplitude. Kaur and Sahasrabudhe (2023, arXiv:2312.02096v1) classify several one-neighbour signed directed urn networks; their signed-permutation cycles do not have this two-tap averaging kernel. Zhang (2016, arXiv:1602.05708v1) supplies general stochastic approximation results used here in the Gaussian regime, with superdiffusive complex-mode theory as an important precedent; those general theorems are not asserted as new.

## Limitations
The signs alternate exactly, the two sampling inputs have equal weight, the urn totals are initially equal, and the sampled Bernoulli variables are conditionally independent. The classification is only for even ring sizes. The law of the nondegenerate leading amplitude is not explicitly identified; the theorem does not establish Gaussianity or non-Gaussianity of that random amplitude itself. Sharpness concerns a spectral projection, not a pathwise two-sided bound for the entire vector. A different sampling weight or arbitrary sign pattern may change the classification. The scientific literature comparison may miss an equivalent spectral specialization under different terminology. No independent review has been performed.

## References
- Y. Dahiya, G. Kaur and N. Sahasrabudhe, *Interacting Stochastic Systems with Agent-Based Sampling and Connection-Based Reinforcement*, arXiv:2610.13884v1 (2026), https://arxiv.org/html/2610.13884v1 .
- G. Kaur and N. Sahasrabudhe, *Interacting Urns on Directed Networks with Node-Dependent Sampling and Reinforcement*, arXiv:2312.02096v1 (2023), https://arxiv.org/abs/2312.02096 .
- L.-X. Zhang, *Central Limit Theorems of a Recursive Stochastic Algorithm with Applications to Adaptive Designs*, arXiv:1602.05708v1 (2016), https://arxiv.org/abs/1602.05708 .
