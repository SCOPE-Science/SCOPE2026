# Sharp random-phase observability tails and the four-sample noise threshold for a planar oscillator

## Finding
For any fixed integer \(m\geq2\), let \(\Theta_1,\ldots,\Theta_m\) be independent projective angles with common continuous probability density \(w\) on \([0,\pi)\), satisfying \(w(0)=w(\pi)\). Form the planar observation matrix \(V\) with rows \((\cos\Theta_j,\sin\Theta_j)\), and its observability Gramian \(G=V^{\mathsf T}V\). Let \(\lambda_-(G)\) be its least eigenvalue. As \(\varepsilon\downarrow0\),
\[
\Pr\{\lambda_-(G)<\varepsilon\}
\sim C_{m,w}\,\varepsilon^{(m-1)/2},\qquad
C_{m,w}=\frac{\sqrt m\,\pi^{(m-1)/2}}{\Gamma((m+1)/2)}
\int_0^\pi w(\phi)^m\,d\phi.
\]
Consequently, for each \(q>0\),
\[
\mathbb E[\lambda_-(G)^{-q}]<\infty
\quad\Longleftrightarrow\quad q<(m-1)/2.
\]
In particular, this classification includes divergence at equality.

With observations \(y=Vx_0+\xi\), where \(x_0\in\mathbb R^2\) is deterministic and the noise \(\xi\sim N(0,\sigma^2I_m)\) is independent of all phases, take the ordinary least-squares estimator \(\widehat x=(V^{\mathsf T}V)^{-1}V^{\mathsf T}y\). For fixed \(\sigma>0\), its Euclidean error \(E=\|\widehat x-x_0\|_2\) obeys the exact tail law
\[
\Pr\{E>t\}\sim C_{m,w}\,\sigma^{m-1}
\frac{2^{(m-1)/2}\Gamma(m/2)}{\sqrt\pi}\,t^{-(m-1)}
\qquad(t\to\infty).
\]
Therefore \(\mathbb E E^q<\infty\) exactly for \(0<q<m-1\). Almost-sure reconstruction needs only two independent observations, whereas **finite unconditional mean-square error requires precisely \(m\geq4\)**.

For every \(m\ge2\), uniform projective sampling \(w\equiv1/\pi\) is the unique continuous sampling density minimizing the leading Gramian lower-tail constant and the Gaussian reconstruction-error tail constant. It need not minimize every nonasymptotic risk.

## Assumptions and scope
The underlying continuous-time oscillator is \(\dot x(t)=\omega Jx(t)\) with \(\omega\ne0\), \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), and scalar output \(y(t)=e_1^{\mathsf T}x(t)\) before measurement noise. Sampling times are such that the observation phases \(\Theta_j=\omega t_j\pmod\pi\) have the specified iid density. Depending on the sign of \(\omega\), the actual observation row is \((\cos\Theta_j,\pm\sin\Theta_j)\), which is an orthogonal reflection of the stated frame and leaves Gramian eigenvalues and Euclidean error norms unchanged. The density is normalized on the projective period, is continuous on the circle, and may vanish at isolated points or intervals; strict positivity is not required. The sample count \(m\) is fixed in all tail limits. Probability and expectation include both sampling and observation noise, where applicable. All matrices are exact real matrices.

## Proof
**1. Exact spectral reduction and almost-sure rank.** Define \(S=\sum_{j=1}^m e^{2i\Theta_j}\). The double-angle identities give
\[
G=\frac{m}{2}I_2+\frac12\begin{pmatrix}
\Re S&\Im S\\ \Im S&-\Re S
\end{pmatrix},\qquad
\lambda_-(G)=\frac{m-|S|}{2},\quad
\lambda_+(G)=\frac{m+|S|}{2}.
\]
Thus \(\lambda_-\ge0\) with equality if and only if all projective phases coincide. Since \(w\) is a Lebesgue density and \(m\ge2\), the equality event has probability zero; \(G\) is invertible almost surely. Also \(\lambda_+(G)\ge m/2\) always.

**2. Localization of near-singularity.** By the Rayleigh principle,
\[
\lambda_-(G)=\min_{\phi\in[0,\pi)}\sum_{j=1}^m\sin^2(\Theta_j-\phi).
\]
If \(\lambda_-<\varepsilon<1/4\), the minimizing direction forces every phase within projective distance \(\arcsin\sqrt\varepsilon\) of \(\phi\). Consequently all phases lie in the same \(O(\sqrt\varepsilon)\) projective neighborhood of \(\Theta_1\). This rules out any other contributing singular configurations. Choose the local wrapped differences \(u_1=0\) and \(u_j=\Theta_j-\Theta_1\pmod\pi\) with \(|u_j|\) small, for \(2\le j\le m\). This change of variables has unit Jacobian in the local chart, without an extra multiplicity factor.

**3. Sharp quadratic geometry.** Since
\[
|S|^2=m^2-4\sum_{1\le i<j\le m}\sin^2(u_i-u_j),
\]
Taylor expansion uniformly in a small fixed neighborhood yields
\[
\lambda_-(G)=\frac1m\sum_{i<j}(u_i-u_j)^2+O(\|u\|^4)
=\sum_{i=1}^m(u_i-\overline u)^2+O(\|u\|^4),
\quad\overline u=m^{-1}\sum_i u_i.
\]
For \(u=(u_2,\ldots,u_m)\in\mathbb R^{m-1}\), write the quadratic form as \(Q(u)=u^{\mathsf T}Au\) with \(A=I_{m-1}-m^{-1}\boldsymbol 1\boldsymbol 1^{\mathsf T}\). This positive definite matrix has eigenvalues \(1\) of multiplicity \(m-2\) and \(1/m\) of multiplicity one, hence determinant \(1/m\). Therefore
\[
\operatorname{vol}_{m-1}\{u:Q(u)<\varepsilon\}
=\sqrt m\,\frac{\pi^{(m-1)/2}}{\Gamma((m+1)/2)}\varepsilon^{(m-1)/2}.
\]
After setting \(u=\sqrt\varepsilon z\), the actual sublevel set converges to \(Q(z)<1\), and the localization above supplies a common bounded domain in \(z\). The joint density in this chart is \(w(\phi)\prod_{j=2}^m w(\phi+u_j)\). By uniform continuity and dominated convergence, integrating over \(\phi\) yields the asserted constant \(C_{m,w}\). The constant is positive: any continuous probability density is positive on some interval. Thus the ratio limit is strict, not just a pair of order bounds.

**4. Singular negative moments.** For a nonnegative random variable \(Z\) supported on a bounded interval, the negative-moment identity reduces behavior near zero to \(q\int_0^{\varepsilon_0}t^{-q-1}\Pr(Z<t)\,dt\), up to finite boundary terms. Inserting the positive leading coefficient above gives convergence exactly when \(q<(m-1)/2\) and logarithmic divergence at equality. Apply this to \(Z=\lambda_-\).

**5. Exact Gaussian estimation-error tail.** Conditionally on \(V\), the error is centered Gaussian with covariance \(\sigma^2 G^{-1}\). Rotational invariance of the independent Gaussian noise permits the unconditional representation
\[
E\ \overset d=\ \sigma\sqrt{Z_1^2/\lambda_-+Z_2^2/\lambda_+},
\]
where \(Z_1,Z_2\) are independent standard normals independent of \(\lambda_-,\lambda_+\). Step 3 makes \(\lambda_-^{-1/2}\) regularly varying with tail index \(m-1\). Conditioning on \(Z_1\), or applying the product-tail lemma with the Gaussian's finite moments of every order, gives
\[
\Pr\{\sigma|Z_1|/\sqrt{\lambda_-}>t\}
\sim C_{m,w}\sigma^{m-1}\mathbb E|Z_1|^{m-1}t^{-(m-1)}.
\]
The remaining term is bounded by \(\sigma\sqrt{2/m}|Z_2|\), which has an exponentially small tail. Upper and lower sandwich bounds for sums of nonnegative random variables show it cannot change the polynomial coefficient. Finally
\(\mathbb E|Z_1|^{m-1}=2^{(m-1)/2}\Gamma(m/2)/\sqrt\pi\), proving the claimed error law. Tail integration proves its exact moment cutoff, including the divergent boundary. Since \(2<m-1\) precisely for \(m\ge4\), that is the mean-square criterion.

**6. Optimal density.** Strict convexity of \(s\mapsto s^m\) for \(m\ge2\) and Jensen's inequality on \([0,\pi)\) give
\[
\int_0^\pi w(\phi)^m\,d\phi\ \ge\ \pi^{1-m},
\]
with equality only when \(w=1/\pi\) almost everywhere, hence everywhere by continuity. The leading error-tail constant has the same density-dependent factor, completing the asserted uniqueness.

## Verification
For uniform \(w\equiv1/\pi\),
\[
C_{m,\mathrm{unif}}=\frac{\sqrt m\,\pi^{(1-m)/2}}{\Gamma((m+1)/2)},
\quad C_{2,\mathrm{unif}}=\frac{2\sqrt2}{\pi},
\quad C_{3,\mathrm{unif}}=\frac{\sqrt3}{\pi},
\quad C_{4,\mathrm{unif}}=\frac8{3\pi^2}.
\]
For two uniform projective angles, the exact elementary law is \(\Pr(\lambda_-\le\varepsilon)=(2/\pi)\arccos(1-\varepsilon)\) for \(0\le\varepsilon\le1\); its small-\(\varepsilon\) expansion matches \(C_{2,\mathrm{unif}}\). For \(m=4\), the Gaussian reconstruction-error tail coefficient is \(16\sqrt2\,\sigma^3/(3\pi^{5/2})\). In the smooth nonuniform family \(w_\rho(\phi)=(1+\rho\cos2\phi)/\pi\), \(|\rho|<1\), the ratio of the leading constants to the uniform constant is exactly
\[
\frac{C_{m,w_\rho}}{C_{m,\mathrm{unif}}}
=\sum_{j=0}^{\lfloor m/2\rfloor}\binom m{2j}\binom{2j}{j}\left(\frac\rho2\right)^{2j}.
\]
The standalone \(\texttt{verify.py}\) checks the exact Gram-ellipsoid matrix identities for thirteen sample counts, the two-sample CDF and parameterized density factors, local fourth-order behavior, and independent Monte Carlo diagnostics for two additional sample counts. It must not be used as a substitute for the analytic probability limit or infinite-moment proof.

## Relationship to prior work
Krauss, Lopez, and Müller [1] give rank-based sample observability criteria, with special treatment of pathological sampling patterns, for discrete-time systems; their observed quantities and sampling theorems do not include a probabilistic least-eigenvalue tail or unconditional Gaussian reconstruction-error moment classification. Kazma, Nugroho, Haber, and Taha [2] study robust observability metrics and sensor selection using averaged Gramians, trace and log-determinant criteria, without the fixed two-dimensional random-phase near-singularity tail addressed here. Classical planar random-walk resultant theory [3] is a relevant precursor: \(\lambda_-=(m-|\sum e^{2i\Theta_j}|)/2\). In particular, some uniform-phase resultant distribution identities are classical and are not claimed as new. The contribution assessed here is the stated continuous-density sharp coefficient, its transfer to noisy state estimation, the exact four-observation mean-square cutoff, and the unique optimal leading-tail sampling density. The complete original text of [3] was not accessible in this review; coverage of a closely related asymptotic remains a publication-priority risk, not a claim that it is absent.

## Limitations
This is a fixed-dimension and fixed-sample-count asymptotic for the planar rotation oscillator with iid continuously distributed projective phases. It does not cover dependent times, deterministic grids, higher-dimensional dynamics, growing sample counts, non-Gaussian noise, non-least-squares estimators, or floating-point error. The minimizing-density statement concerns only the leading asymptotic tail constants, not all finite-error quantiles or every loss function. Scientific correctness is supported by a self-contained proof and reproducibility checks; independent mathematical validation and publication-priority determination have not been performed.

## References
[1] I. Krauss, V. G. Lopez, and M. A. Müller, *Sample-based observability of linear discrete-time systems*, arXiv:2204.06451, first submitted 13 April 2022. https://arxiv.org/abs/2204.06451 ; full text: https://arxiv.org/html/2204.06451v3 .

[2] M. H. Kazma, S. A. Nugroho, A. Haber, and A. F. Taha, *State-Robust Observability Measures for Sensor Selection in Nonlinear Dynamic Systems*, arXiv:2307.07074, first submitted 13 July 2023. https://arxiv.org/html/2307.07074v1 .

[3] J. A. Greenwood and D. Durand, *The Distribution of Length and Components of the Sum of n Random Unit Vectors*, Annals of Mathematical Statistics **26** (1955), 233–246, DOI:10.1214/aoms/1177728540. The full text was not accessible for a decisive theorem-by-theorem comparison; only the abstract and bibliographic record were examined.
