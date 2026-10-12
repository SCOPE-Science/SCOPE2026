# Exact misranking probability and sharp sketch budgets for two-mode sketch-power iteration

## Finding
Consider the rank-one **fixed-proxy sketch-power rangefinder** of Chang and Yang: one range sketch is repeatedly multiplied by the *same* independent Gaussian sketch covariance. In the two-singular-mode model specified below, the probability that arbitrarily many iterations select a principal direction with **more energy in the weaker mode** is exactly
\[
 p_{\ell}(\kappa)=I_{1/(1+\kappa^2)}\left(\frac{\ell}{2},\frac{\ell}{2}\right),
 \qquad \kappa>1,\quad \ell\ge2.
\]
Here \(I_z(a,b)=B(a,b)^{-1}\int_0^z t^{a-1}(1-t)^{b-1}\,dt\). The probability lies strictly between zero and one half and decreases strictly with \(\ell\). For \(\kappa=2,\ell=4\), it equals \(13/125\).

The event has an unavoidable approximation consequence: every rank-one reconstruction whose left factor is the limiting sketched range direction has squared Frobenius error strictly greater than \((\kappa^2+1)/2\), versus the optimal rank-one squared error \(1\). With positive probability, continuing power iterations therefore makes the orthogonal-projection approximation strictly *worse* than the unpowered starting sketch.

The exact sample budget
\[
 \ell_\delta(\kappa):=\min\{\ell\in\mathbb Z:\ell\ge2,\ p_\ell(\kappa)\le\delta\}
\]
has two sharp asymptotic regimes:
\[
 \lim_{\delta\downarrow0}\frac{\ell_\delta(\kappa)}{\log(1/\delta)}
   =\frac{1}{\log((\kappa^2+1)/(2\kappa))}\quad(\kappa>1\text{ fixed}),
\]
\[
 \lim_{\kappa\downarrow1}(\kappa-1)^2\ell_\delta(\kappa)
   =\bigl[\Phi^{-1}(1-\delta)\bigr]^2\quad(0<\delta<1/2\text{ fixed}),
\]
where \(\Phi\) is the standard normal cumulative distribution function. Thus a fixed confidence target demands quadratic growth of the sketch dimension as the two singular values merge.

## Assumptions and scope
Fix any integer \(\ell\ge2\), choose an ambient dimension \(N\ge\ell+1\), and fix \(\kappa>1\). Let \(A\in\mathbb R^{N\times N}\) be diagonal with first two diagonal entries \(\kappa,1\) and all others zero. Independently draw \(\Phi\in\mathbb R^{N\times\ell}\) and \(\omega\in\mathbb R^N\) with independent real \(N(0,1)\) entries. Set \(Z=A\Phi\), \(K=ZZ^{\mathsf T}\), \(Y=A\omega\), and
\[
 Q_q=K^qY/\|K^qY\|_2,\qquad q=0,1,2,\ldots.
\]
All quantities are interpreted in exact arithmetic. This is a rank-one sketch-power rangefinder with proxy width \(\ell\) and one range-sketch column; it is a deliberately minimal subspace regime, **not** a theorem about the complete oversampled co-range reconstruction or numerical roundoff. Write \(v\) for a unit leading eigenvector of \(K\), whose sign is immaterial. The misranking event is \(E=\{|v_2|>|v_1|\}\), with components in the two-dimensional singular-mode basis. The event is about the **orientation** of the limiting direction, not a claim that its vector equals the weaker population eigenvector.

## Proof
**1. Exact limiting subspace.** Restrict all vectors to the first two coordinates. Then \(K\) has the real symmetric form
\[
 H=\begin{pmatrix}\kappa^2 U&\kappa T\\\kappa T&V\end{pmatrix},
\quad U=\sum_{j=1}^{\ell}\phi_{1j}^2,\quad
 V=\sum_{j=1}^{\ell}\phi_{2j}^2,\quad
 T=\sum_{j=1}^{\ell}\phi_{1j}\phi_{2j}.
\]
The variables \(U,V\) are independent \(\chi^2_\ell\) variables. Because \(\ell\ge2\), \(H\) is positive definite almost surely; the event of a repeated eigenvalue has probability zero. Conditional on \(H\), the independent Gaussian vector \(Y\) has a nonzero component in the top eigendirection almost surely. Hence ordinary spectral decomposition proves \(Q_q\) converges up to sign to \(v\) as \(q\to\infty\).

**2. Orientation equivalence and exact law.** If \(\lambda_+>\lambda_-\) denote the two eigenvalues of \(H\), the spectral projector onto the leading eigenline is
\[
 vv^{\mathsf T}=\frac{H-\lambda_- I}{\lambda_+-\lambda_-},
\qquad v_1^2-v_2^2
 =\frac{\kappa^2U-V}{\sqrt{(\kappa^2U-V)^2+4\kappa^2T^2}}.
\]
Consequently \(E=\{V>\kappa^2U\}\) almost surely: the random off-diagonal entry does **not** change the sign of the orientation comparison. The gamma-ratio identity yields
\[
 U/(U+V)\sim\operatorname{Beta}(\ell/2,\ell/2),\qquad
 E=\left\{\frac{U}{U+V}<\frac{1}{1+\kappa^2}\right\},
\]
which proves the claimed probability. At \(\kappa=2,\ell=4\), the \(\operatorname{Beta}(2,2)\) CDF is \(3z^2-2z^3\), giving \(13/125\) at \(z=1/5\). For increasing \(\ell\), the ratio of two symmetric beta densities is a positive constant times \([z(1-z)]^c\) with \(c>0\); on \((0,1/2)\) this is strictly increasing. As each density has exactly half its mass on that interval, single crossing proves strict stochastic concentration toward \(1/2\), and hence strict decrease of \(p_\ell(\kappa)\) for \(\kappa>1\).

**3. Reconstruction obstruction.** The limiting orthogonal-projection error is
\[
 \|(I-vv^{\mathsf T})A\|_F^2
 =\kappa^2 v_2^2+v_1^2
 =1+(\kappa^2-1)v_2^2.
\]
On \(E\), \(v_2^2>1/2\), giving the claimed strict lower bound. For every row \(B\in\mathbb R^{1\times N}\), orthogonal Pythagoras yields
\[
 \|A-vB\|_F^2
 =\|(I-vv^{\mathsf T})A\|_F^2+\|v^{\mathsf T}A-B\|_2^2,
\]
so no postprocessed reconstruction confined to that leading line avoids the bound. The Eckart--Young optimal rank-one error for \(A\) is \(1\). Finally, \(E\) has positive probability independently of \(\omega\); a nonempty open set of \(\omega\) makes \(Q_0\) arbitrarily close to the optimal direction \(e_1\). Conditional on such a pair, the limiting error exceeds the initial error, so some finite number of power steps must worsen the error. This establishes a positive-probability strict deterioration without asserting that every sample deteriorates.

**4. Sharp confidence budgets.** Fix \(\kappa>1\), put \(z=(1+\kappa^2)^{-1}<1/2\), and \(a=\ell/2\). Endpoint Laplace asymptotics and Stirling's formula give
\[
 \int_0^z[t(1-t)]^{a-1}\,dt
 \sim\frac{[z(1-z)]^a}{a(1-2z)},\quad
 B(a,a)\sim2\sqrt\pi\,4^{-a}a^{-1/2}.
\]
Thus the exact tail has the stronger equivalent
\[
 p_\ell(\kappa)\sim
 \frac{\kappa^2+1}{\kappa^2-1}
 \frac{1}{\sqrt{2\pi\ell}}
 \left(\frac{2\kappa}{\kappa^2+1}\right)^\ell.
\]
Taking logarithms and inverting the strictly decreasing probability sequence establishes the fixed-gap confidence law. For the merging-gap law, let \(\kappa=1+\varepsilon\) and suppose \(\ell\varepsilon^2\to c\in(0,\infty)\). The chi-square central limit theorem for the independent variables \(U,V\) implies
\[
 \Pr(V>\kappa^2U)\longrightarrow\Phi(-\sqrt c).
\]
Indeed the difference has mean \(-2\varepsilon\ell+o(\varepsilon\ell)\) and asymptotic standard deviation \(2\sqrt\ell\); the centered normalized difference obeys a standard Gaussian limit. Monotonicity in \(\ell\) and sandwiching \(c\) immediately below and above \([\Phi^{-1}(1-\delta)]^2\) prove the second budget law. At \(\delta\ge1/2\), already \(\ell=2\) suffices; this is why the nontrivial merging-gap claim assumes \(\delta<1/2\).

## Verification
Run `python verify.py` in an environment satisfying `requirements.txt`. The checker independently tests 40 exact rational beta-CDF identities, 1,500 eigenvector and residual identities, 11 large-width asymptotic cases, 1,235 exact-CDF monotonicity comparisons, 90,000 Gaussian draws across three parameter sets, and 200 normalized matrix-power trajectories. The analytical argument above, not these finite tests, proves the results for all admissible real \(\kappa\), integers \(\ell\), and confidence levels. Underflowed extreme probability calculations are excluded from asymptotic numerical comparisons.

## Relationship to prior work
Chang and Yang [1] define sketch-power iteration in equation (2.5), analyze finite-step approximation bounds (Theorems 3.1 and 3.2), and explicitly note in Section 7 that unbounded powering selects the top singular subspace of the fixed sketch \(Z\). This limit is **prior knowledge**. The result proved here instead quantifies the exact probability of the *wrong dominant orientation* of that limiting subspace and its sharp sketch-budget laws. Their general theorems do not give this probability; in particular their general-\(q\) theorem has additional oversampling and correlated-start hypotheses not assumed here. Chenakkod and Dereziński [2] study a similar sketched-power form but prove high-probability regularized spectral approximation under large structured sketches, not the exact two-mode Gaussian misranking law. Tropp et al. [3] analyze the underlying one-pass co-range reconstruction and its broad expected Frobenius guarantees, without this fixed-proxy limit risk. The chi-square ratio and beta distribution [4] are classical and not claimed as new. The novelty asserted is the exact algorithm-specific reliability law and two sharp confidence-regime constants, not the underlying beta calculus.

## Limitations
The study concerns a rank-two signal embedded in an arbitrarily large square matrix, a one-column rangefinder, independent real Gaussian sketches, repeated use of a **fixed** proxy, and exact arithmetic. It does not claim a failure probability for independently resampled sketches at every power step, complex Gaussian tests, oversampled multi-column subspaces, the full co-range postprocessing error distribution, finite-precision implementations, or general matrices. The high-power risk event is positive but decreases exponentially with sketch width for a fixed spectral gap. Its practical cost must be weighed against other error mechanisms; classical principal-component/Wishart analyses may contain equivalent descriptions of the same two-mode angular event.

## References
[1] C. Chang and Y. Yang, *Improving Sketching Algorithms for Low-Rank Matrix Approximation via Sketch-Power Iterations*, arXiv:2603.26298v1, 27 March 2026. https://arxiv.org/abs/2603.26298

[2] S. Chenakkod and M. Dereziński, *Accelerating Power Method with Fast Sketching for Stronger Low-Rank Approximation*, arXiv:2605.09755v1, 10 May 2026. https://arxiv.org/abs/2605.09755

[3] J. A. Tropp, A. Yurtsever, M. Udell, and V. Cevher, *Practical Sketching Algorithms for Low-Rank Matrix Approximation*, SIAM Journal on Matrix Analysis and Applications 38 (2017), 1454--1485, DOI 10.1137/17M1111590. https://arxiv.org/abs/1609.00048

[4] NIST/SEMATECH e-Handbook of Statistical Methods, section 1.3.6.6.5, *F Distribution* (classical ratio of independent chi-square variates). https://itl.nist.gov/div898/handbook/eda/section3/eda3665.htm
