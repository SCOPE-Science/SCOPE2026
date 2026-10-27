# Hidden second-order isotropy under noisy directional resetting

## Finding

Consider planar active Brownian motion whose heading is independently refreshed at Poisson times, but whose position is never reset. For an arbitrary independent reset-angle probability law, exact isotropy of **every positive-lag centered displacement covariance** is equivalent to a cancellation between the first two stationary angular Fourier harmonics. The condition does not require zero mean propulsion or a uniform heading distribution.

For a physically elementary reset protocol that selects either angle \(+\alpha\) or \(-\alpha\) with equal probability, where \(0\leq\alpha\leq\pi/2\), put \(q=r/D_R>0\), with \(r\) the resetting rate and \(D_R\) the rotational diffusivity. The longitudinal and transverse centered displacement variances are equal **for every \(t>0\)** if and only if

\[
\cos^2\alpha=\frac{(q+1)^2}{q^2+2}.
\]

Thus the entire nontrivial isotropy curve is \(0<q<1/2\) and \(\alpha=\arccos((q+1)/\sqrt{q^2+2})\). Its endpoint \((q,\alpha)=(1/2,0)\) is the deterministic-orientation special case already implied by earlier diffusivity formulas. Along the nontrivial curve the particle nevertheless drifts at the strictly positive speed

\[
\frac{\|\mathbb E[X_t-X_0]\|}{t}=\frac{vq}{\sqrt{q^2+2}},
\]

and the stationary orientation law has nonzero first and second angular harmonics. This is isotropy of **centered second moments**, not isotropy of the complete displacement law.

The classification is sharp. If \(0\leq\alpha<\pi/4\), the longitudinal displacement variance is larger for \(0<q<q_c(\alpha)\), equal at the unique positive critical ratio, and smaller for \(q>q_c(\alpha)\), where

\[
q_c(\alpha)=\begin{cases}
\frac{\sqrt{c(3-2c)}-1}{1-c},& 1/2<c<1,\\
\frac12,& c=1,
\end{cases}\qquad c=\cos^2\alpha.
\]

For \(\pi/4\leq\alpha\leq\pi/2\), transverse variance is strictly larger for every \(q>0\). Moreover, randomly selecting between the two directions supplies an additional **positive transverse covariance** relative to averaging the rotated fixed-direction covariance tensors, given explicitly in the proof. This extra term explains why random-angle resetting cannot be replaced by averaging fixed-angle formulas.

## Assumptions and scope

Let \(v>0\), \(D_R>0\), \(r>0\), and \(D_T\geq0\). Let \(\Theta_t\) be Brownian motion on the circle with rotational generator \(D_R\partial_\theta^2\), and at the independent events of a rate-\(r\) Poisson process replace its orientation by a new independent sample \(\Phi\sim\nu\), where \(\nu\) is any Borel probability law on the circle. The reset law and all driving noises are mutually independent. Let \(\Theta_0\) have the unique stationary angular law. Let the displacement process obey

\[
X_t-X_0=v\int_0^t u(\Theta_s)\,ds+\sqrt{2D_T}\,B_t,
\qquad u(\theta)=(\cos\theta,\sin\theta),
\]

with a two-dimensional standard Brownian motion \(B\) independent of the angle process. In particular there is no stationary spatial distribution and no reset of position.

Write \(\mu_n=\int e^{in\phi}\,\nu(d\phi)\), \(a_n=\mathbb E[e^{in\Theta_0}]\), and \(\gamma=r+D_R\). Let \(m=(\Re a_1,\Im a_1)\) and let \(C\) be the stationary covariance matrix of \(u(\Theta_0)\). Define the positive function

\[
H_\gamma(t)=\frac{t}{\gamma}-\frac{1-e^{-\gamma t}}{\gamma^2},\qquad t>0.
\]

## Proof

**1. Stationary angular harmonics.** The angular generator acts on a Fourier mode according to

\[
\mathcal L e^{in\theta}=-(r+n^2D_R)e^{in\theta}+r\mu_n
\quad(n\ne0).
\]

The regeneration at positive rate gives a unique invariant angular law. Integrating this generator identity against that law yields

\[
a_n=\frac{r\mu_n}{r+n^2D_R}\quad(n\ne0).
\]

Independently, the last-reset age is exponentially distributed with rate \(r\), and the conditional Fourier mode decays as \(e^{-n^2D_RA}\), giving the same expression. The first-mode semigroup is

\[
\mathbb E[u(\Theta_t)\mid\Theta_0=\theta]
=m+e^{-\gamma t}(u(\theta)-m).
\]

Consequently the stationary velocity covariance at positive lag is exactly \(e^{-\gamma t}C\). Since \(C\) is symmetric, both time orders have the same matrix.

**2. Exact displacement covariance.** Double integration of this exponential covariance, including the independent translational Brownian part, gives, for every \(t\geq0\),

\[
\mathbb E[X_t-X_0]=vtm,\qquad
\operatorname{Cov}(X_t-X_0)=2D_TtI_2+2v^2H_\gamma(t)C.
\]

The formula is exact rather than merely a large-time expansion. The large-time effective diffusivity tensor is \(D_TI_2+v^2C/\gamma\). Because \(H_\gamma(t)>0\) for \(t>0\) and \(v>0\), the displacement covariance is proportional to \(I_2\) at one positive time if and only if it is proportional to \(I_2\) at every positive time, if and only if \(C\) is proportional to \(I_2\).

**3. General spectral cancellation criterion.** Direct trigonometric identities give

\[
C=\frac{1-|a_1|^2}{2}I_2+
\frac12\begin{pmatrix}
\Re(a_2-a_1^2)&\Im(a_2-a_1^2)\\
\Im(a_2-a_1^2)&-\Re(a_2-a_1^2)
\end{pmatrix}.
\]

The two covariance eigenvalues differ by \(2v^2H_\gamma(t)|a_2-a_1^2|\). Thus the exact general necessary and sufficient condition is

\[
a_2=a_1^2
\quad\Longleftrightarrow\quad
\frac{r}{r+4D_R}\mu_2=
\left(\frac{r}{r+D_R}\right)^2\mu_1^2.
\]

This is a complex equality (both real and imaginary parts), not merely equality of the coordinate variances.

**4. Complete symmetric two-angle classification.** For \(\nu=\tfrac12(\delta_{+\alpha}+\delta_{-\alpha})\), the relevant harmonics are real:

\[
a_1=\frac{q\cos\alpha}{q+1},\qquad
a_2=\frac{q(2\cos^2\alpha-1)}{q+4}.
\]

With \(c=\cos^2\alpha\in[0,1]\), the signed difference between the longitudinal and transverse **instantaneous heading variances** is

\[
C_{xx}-C_{yy}=a_2-a_1^2
=\frac{q\big[c(q^2+2)-(q+1)^2\big]}{(q+4)(q+1)^2}.
\]

The same sign governs the displacement variance difference for every \(t>0\). The polynomial \(G(q)=c(q^2+2)-(q+1)^2\) satisfies \(G'(q)=2(c-1)q-2<0\) for all \(q\geq0\). If \(c\leq1/2\), then \(G(0)\leq0\), hence \(G(q)<0\) for all \(q>0\). If \(c>1/2\), then \(G(0)>0\) and \(G(q)\to-\infty\) as \(q\to\infty\), except that \(G(q)=1-2q\) for \(c=1\), which also has a unique positive root. Solving \(G(q)=0\) gives the stated \(q_c\); it lies strictly between zero and \(1/2\) for \(1/2<c<1\) and equals \(1/2\) when \(c=1\).

Equivalently, for \(q>0\) equality requires \(c=(q+1)^2/(q^2+2)\). Requiring \(c\leq1\) gives \(q\leq1/2\), with nonzero angular aperture precisely when \(0<q<1/2\). On that curve

\[
a_1=\frac{q}{\sqrt{q^2+2}}>0,\quad
a_2=\frac{q^2}{q^2+2}>0,\quad
C=\frac{1}{q^2+2}I_2.
\]

Hence the entire finite-time centered covariance is

\[
\operatorname{Cov}(X_t-X_0)=
\left[2D_Tt+\frac{2v^2}{q^2+2}H_{r+D_R}(t)\right]I_2,
\]

and the drift is \(vt(q/\sqrt{q^2+2},0)\). For example, at \(q=1/4\) and \(\alpha=\arccos(5/\sqrt{33})\), one has \(a_1=1/\sqrt{33}\), \(a_2=1/33\), \(C=(16/33)I_2\), and nonzero mean velocity \(v/\sqrt{33}\) along the horizontal axis.

**5. Why mixing changes the covariance.** Compare the actual random \(\pm\alpha\) protocol with the arithmetic average of covariance tensors for two separate fixed-reset-angle experiments, one at \(+\alpha\), the other at \(-\alpha\), each initialized in its own stationary angle law. Their stationary second trigonometric moments average to the same \(\mathbb E[u u^{\mathsf T}]\) as the mixture, but their means are \((q/(q+1))(\cos\alpha,\pm\sin\alpha)\). Averaging the fixed-angle **centered** covariances subtracts the average of the two outer products of these means. The actual mixture subtracts instead the outer product of their average. The difference is exactly

\[
C_{\rm mixture}-\frac{C_{+}+C_{-}}2
=\left(\frac{q}{q+1}\right)^2\sin^2\alpha\,e_ye_y^{\mathsf T}.
\]

Since all first harmonics decay at rate \(\gamma\), the corresponding finite-time displacement covariance difference is

\[
2v^2H_\gamma(t)\left(\frac{q}{q+1}\right)^2\sin^2\alpha\,e_ye_y^{\mathsf T},
\]

strictly positive in the transverse direction for \(t>0\) and \(\alpha>0\). This is the renewal-direction fluctuation absent from averaging fixed-heading formulas.

## Verification

The accompanying `checker.py` uses Python standard-library rational arithmetic to check the polynomial factorization, angular covariance positivity, exact isotropy curve and uniqueness signs over a parameter grid. It independently compares the angular Fourier modes with numerical integration over exponential last-reset ages, and tests the finite-time isotropic displacement covariance for several positive times and parameters. The executed checker reported **2646 successful assertions**. The infinite-parameter classification and all-time identity follow from the algebraic proof above, not from finite sampling.

To reproduce: `python3 checker.py`.

## Relationship to prior work

Kumar, Sadekar, and Basu (2020, arXiv:2008.03294) studied orientation-only resetting to a *single fixed direction* and gave longitudinal and transverse long-time diffusivities (their Section V, equations 59–60). Their formulas already imply equality at the **single** rate ratio \(q=1/2\). That endpoint is therefore not presented here as an original discovery.

Baouche, Franosch, Meiners, and Kurzthaler (2024, arXiv:2405.06769v1, May 10, 2024) developed renewal equations for angle resetting, stated a general reset-angle distribution in the model, and explicitly evaluated displacements and correlations for resetting to one fixed angle (Section III and Appendix C). Their general framework is an important methodological antecedent. The present exact complex-harmonic criterion, all-positive-time covariance cancellation, full \(\pm\alpha\) phase diagram, and positive mixing correction are not identified in the inspected full text; the new statements concern random reinitialization orientations rather than rotation of a fixed orientation.

Chaki, Olsen, and Löwen (2024, arXiv:2406.17550) analyzed orientation-only resetting of a **passive shape-anisotropic** Brownian particle to one fixed angle; the source has a different noise model and no active drift. Ghosh, Mandal, and Chaki (arXiv:2501.05149v1, January 9, 2025) treated shape-anisotropic active particles, mostly with fixed reset orientation, and mentioned multi-state resetting in Section III; the inspected work does not provide the present two-angle cancellation classification. These comparisons concern mathematical implications, not just titles.

## Limitations

All results refer to the exactly specified Poisson orientation-refresh mechanism and to initial **stationarity of the angular process**. Transient initial angular laws need not have time-homogeneous velocity correlations. The claim is about centered displacement covariance, not a rotationally invariant full probability density, higher cumulants, or spatial stationarity. The broad Fourier criterion requires no symmetry of the reset law, but the explicit single-threshold phase classification assumes equal-probability resets to \(\pm\alpha\) and \(0\leq\alpha\leq\pi/2\). Rates \(r=0\) and rotational diffusivity \(D_R=0\) are excluded. Finite-moment formulas are exact; no finite-sample statistical identification guarantee is supplied. Scholarly priority beyond the inspected sources requires independent assessment.

## References

1. V. Kumar, O. Sadekar, and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, Physical Review E 102, 052129 (2020), arXiv:2008.03294, https://arxiv.org/abs/2008.03294.
2. Y. Baouche, T. Franosch, M. Meiners, and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1 (May 10, 2024), https://arxiv.org/abs/2405.06769.
3. S. Chaki, K. Stølevik Olsen, and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550 (June 25, 2024), https://arxiv.org/abs/2406.17550.
4. A. Ghosh, S. Mandal, and S. Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149v1 (January 9, 2025), https://arxiv.org/abs/2501.05149.
