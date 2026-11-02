# A golden-ratio kurtosis boundary for intermittent run-and-rest motion

## Finding

For a stationary three-velocity, one-dimensional run-and-rest Markov particle, the fourth displacement cumulant has a complete sign classification at **every positive observation time**. Let \(\alpha,\beta,v>0\) denote the rate of leaving either moving state, the total rate of leaving the resting state, and the moving speed. Write \(r=\alpha/\beta\), \(\varphi=(1+\sqrt5)/2\), and let \(\kappa_4(t)=\mathbb E[X_t^4]-3(\mathbb E[X_t^2])^2\). Then, for all \(t>0\):

* If \(0<r\le\varphi\), then \(\kappa_4(t)<0\).
* If \(\varphi<r<2\), there is exactly one time \(t_*>0\) at which \(\kappa_4(t_*)=0\); it is negative for \(t<t_*\) and positive for \(t>t_*\).
* If \(r\ge2\), then \(\kappa_4(t)>0\).

Define the convolution kernel on \(t\ge0\)
\[
H(t)=\bigl[t\,\mathbf1_{t\ge0}\bigr]*\bigl[t e^{-\alpha t}\mathbf1_{t\ge0}\bigr]*\bigl[e^{-(\alpha+\beta)t}\mathbf1_{t\ge0}\bigr]*\bigl[e^{-2\alpha t}\mathbf1_{t\ge0}\bigr].
\]
Its Laplace transform is \(1/[s^2(s+\alpha)^2(s+\alpha+\beta)(s+2\alpha)]\). The exact, non-asymptotic cumulant formula is
\[
\boxed{\displaystyle \kappa_4(t)=\frac{24\beta v^4}{(\alpha+\beta)^2}\left[(\alpha-2\beta)H'(t)+2(\alpha^2-\alpha\beta-\beta^2)H(t)\right].}
\]
In the crossover regime, \(t_*\) is characterized uniquely by
\[
\frac{H'(t_*)}{H(t_*)}=\frac{2(\alpha^2-\alpha\beta-\beta^2)}{2\beta-\alpha}.
\]
For example, \(\alpha=1.8\), \(\beta=v=1\) gives \(t_*\approx0.854478454\).

## Assumptions and scope

The internal stationary continuous-time Markov chain \(S_t\in\{+,0,-\}\) has transition generator (rows/columns ordered \(+\), \(0\), \(-\))
\[
Q=\begin{pmatrix}-\alpha&\alpha&0\\ \beta/2&-\beta&\beta/2\\0&\alpha&-\alpha\end{pmatrix},
\quad \pi=\frac1{2(\alpha+\beta)}(\beta,2\alpha,\beta).
\]
Each moving state jumps to rest at rate \(\alpha\); rest jumps to each moving state at rate \(\beta/2\). The internal state starts in \(\pi\). Define \(\sigma(+)=1\), \(\sigma(0)=0\), \(\sigma(-)=-1\) and \(X_t=v\int_0^t\sigma(S_u)\,du\). The ensemble displacement is symmetric, so its mean is zero and the fourth cumulant has the stated centered form. No other translational diffusion, spatial confinement, aging, interactions, or forcing is present. All claims quantify over \(\alpha,\beta,v>0\) and \(t>0\).

## Proof

**Step 1: correlation functions.** Put \(p=\beta/(\alpha+\beta)\) and \(d=\alpha+\beta\). As functions of the Markov state, \(Q\sigma=-\alpha\sigma\) and \(Q\sigma^2=\beta-d\sigma^2\). Stationarity therefore gives
\[
\mathbb E[\sigma(S_0)\sigma(S_t)]=p e^{-\alpha t}.
\]
For ordered \(t_1<t_2<t_3<t_4\), with \(x=t_2-t_1\), \(y=t_3-t_2\), \(z=t_4-t_3\), successive conditioning gives
\[
\mathbb E[\sigma_1\sigma_2\sigma_3\sigma_4]
=p e^{-\alpha(x+z)}\left[p+(1-p)e^{-dy}\right].
\]
Here \(\sigma_j=\sigma(S_{t_j})\). Subtracting the three products of pairwise correlations (the fourth joint cumulant) yields
\[
\operatorname{cum}(\sigma_1,\sigma_2,\sigma_3,\sigma_4)
=\frac{\beta}{d^2}e^{-\alpha(x+z)}
\left[\alpha e^{-dy}-2\beta e^{-2\alpha y}\right].
\]
The formula extends to coincident times by continuity, although such coincidences have zero measure in the integral below.

**Step 2: integrate the connected correlation.** Multilinearity of joint cumulants and boundedness of the velocity allow Fubini integration over four times. Time permutation symmetry gives a factor \(4!=24\). For the three ordered gaps, the first time runs over an interval of length \(t-x-y-z\) when \(x+y+z\le t\). Thus
\[
\kappa_4(t)=\frac{24\beta v^4}{d^2}
\int_{x,y,z\ge0\atop x+y+z\le t}
(t-x-y-z)e^{-\alpha(x+z)}
\left[\alpha e^{-dy}-2\beta e^{-2\alpha y}\right]dx\,dy\,dz.
\]
Taking a Laplace transform in \(t\), each gap integrates independently and the time weight contributes \(s^{-2}\):
\[
\mathcal L\{\kappa_4\}(s)
=\frac{24\beta v^4}{d^2}\frac{1}{s^2(s+\alpha)^2}
\left(\frac{\alpha}{s+d}-\frac{2\beta}{s+2\alpha}\right)
=\frac{24\beta v^4}{d^2}\frac{(\alpha-2\beta)s+2(\alpha^2-\alpha\beta-\beta^2)}{s^2(s+\alpha)^2(s+d)(s+2\alpha)}.
\]
Inverting the last rational expression proves the claimed formula with \(H\) and its derivative. There are no unproved uniqueness or analyticity assumptions about inversion: the positive convolution has the displayed transform, is smooth for \(t>0\), and vanishes sufficiently fast at \(0\) that differentiating its Laplace transform adds no boundary term.

**Step 3: the sign and uniqueness lemma.** The four causal factors defining \(H\) are log-concave on their supports: the logarithms of the two polynomial–exponential factors have strictly negative second derivatives, and the other two factors have affine logarithms. Convolution preserves log-concavity (Prékopa's convolution theorem); equivalently one may multiply the nonintegrable first factor by \(e^{-\varepsilon t}\) and pass to the limit \(\varepsilon\downarrow0\) on compact time intervals. Consequently \(H\) is log-concave. Positivity of each factor, plus the factor \(t\), shows \(H(t)>0\) and \(H'(t)>0\) for \(t>0\). The rational Laplace transform shows \(H\) is real analytic for positive times. Its endpoint expansions are
\[
H(t)=\frac{t^5}{120}+O(t^6)\quad (t\downarrow0),
\qquad
H(t)=\frac{t}{2\alpha^3(\alpha+\beta)}+O(1)\quad (t\to\infty).
\]
Thus \(\ell(t)=H'(t)/H(t)\) is nonincreasing, with \(\ell(t)\to\infty\) as \(t\downarrow0\) and \(\ell(t)\to0\) as \(t\to\infty\). It is *strictly* decreasing: equality at two distinct times for a nonincreasing analytic function would make it constant on an interval and hence, by analyticity, everywhere, contradicting its endpoint limits. Therefore \(\ell\) maps \((0,\infty)\) bijectively and decreasingly to \((0,\infty)\).

Finally, \(\alpha^2-\alpha\beta-\beta^2\) is nonpositive exactly for \(r\le\varphi\), while \(\alpha-2\beta\) is nonnegative exactly for \(r\ge2\). The two coefficients in the positive \(H,H'\) expansion are both strictly or weakly negative for \(r\le\varphi\), both strictly or weakly positive for \(r\ge2\), and have opposite signs for \(\varphi<r<2\). In the latter interval the cumulant has the sign of \(2(\alpha^2-\alpha\beta-\beta^2)-(2\beta-\alpha)\ell(t)\), which increases strictly through zero exactly once. This proves all three alternatives including both boundary ratios.

**Step 4: normalization and limiting checks.** Integrating the stationary velocity autocorrelation yields the exact variance
\[
\operatorname{Var}(X_t)=\frac{2\beta v^2}{\alpha(\alpha+\beta)}\left(t-\frac{1-e^{-\alpha t}}{\alpha}\right)>0.
\]
Consequently the standardized excess kurtosis and \(\kappa_4\) have exactly the same signs. The small- and long-time limits are
\[
\kappa_4(t)=\frac{\beta v^4(\alpha-2\beta)}{(\alpha+\beta)^2}t^4+O(t^5),
\qquad
\lim_{t\to\infty}\frac{\kappa_4(t)}t=
\frac{24\beta v^4(\alpha^2-\alpha\beta-\beta^2)}{\alpha^3(\alpha+\beta)^3}.
\]
These limits alone would *not* prove the uniqueness of the crossover, which is supplied by the log-concavity argument.

## Verification

The standalone `check_three_state.py` supplies two distinct finite-dimensional representations of the same quantity: a \(15\times15\) Feynman–Kac moment lift of the three-state generator, and a \(6\times6\) positive linear cascade for \(H,H'\). It checks \(567\) assertions across rates, speeds, observation times, sign regimes, six crossover solutions, and asymptotic limits. Run `python check_three_state.py` with Python, NumPy and SciPy installed. These numerical comparisons corroborate the exact formulas; they do not replace the all-parameter analytic proof.

## Relationship to prior work

Angelani, *Averaged run-and-tumble walks* (public online 2013-05-03), treats a broad class of run–tumble processes and supplies a Laplace–Fourier propagator and mean-square displacement. This is important directly relevant prior framework. Its publisher page, abstract and first-page preview were accessible, but complete text could not be inspected; its coverage of higher cumulants and this exact phase diagram remains an explicit priority uncertainty. Access was also attempted through arXiv, lawful open-access outlets and institutional retrieval without full text. No claim is made that its general transform is independent of the present moment computation.

Rukolaine (2017) analyzes intermittent active/passive kinetic transport and a quasi-steady-state approximation. Basu and collaborators (2019) analyze the stationary position distribution of a three-internal-state particle in a harmonic trap, not free finite-time displacement cumulants. Villa-Torrealba and collaborators (2020) analyze non-Gaussian displacement, including kurtosis behavior, for other run-and-tumble swimming strategies; they do not directly furnish the two-rate rest/move golden-ratio and two-threshold theorem stated here. Shaebani and Rieger (2021) study transient anomalous diffusion in a different two-motility-state model. A previously available two-speed telegraph result treats speed refresh at reversals and long-time kurtosis rather than the present resting Markov state and full-time sign classification.

The proposed contribution is the exact all-time \(\kappa_4\) expression with a positive log-concave kernel and its sharp complete sign/unique-crossing classification, **not** the underlying telegraph-process machinery, general propagators, or kurtosis as a diagnostic. Historical priority has not been independently certified.

## Limitations

The result assumes an equilibrated, exactly three-state, spatially homogeneous velocity Markov chain with symmetric departure from rest, exponential holding times, and no independent translational diffusion. It does not address nonstationary initial populations, nonexponential rests, biased re-launch, continuous reorientation, nonlinear interactions, or higher cumulants. The focal 2013 paper's inaccessible complete text creates a material residual novelty risk; this mathematical analysis does not resolve it. No independent audit has been performed.

## References

1. L. Angelani (2013), *Averaged run-and-tumble walks*, EPL **102**, 20004; DOI: https://doi.org/10.1209/0295-5075/102/20004 (published online May 3, 2013).
2. S. A. Rukolaine (2017), *A mean-field model of intermittent particle transport and its quasi-steady-state approximation*, https://arxiv.org/abs/1710.07947.
3. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr (2019), *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, https://arxiv.org/abs/1910.10083.
4. A. Villa-Torrealba, C. Chávez-Raby, P. de Castro, R. Soto (2020), *Run-and-tumble bacteria slowly approaching the diffusive regime*, https://arxiv.org/abs/2002.02872; DOI: https://doi.org/10.1103/PhysRevE.101.062607.
5. M. R. Shaebani, H. Rieger (2021), *Transient anomalous diffusion in run-and-tumble dynamics*, https://arxiv.org/abs/2107.07329.
6. A. Prékopa (1973), *On logarithmic concave measures and functions*, Acta Scientiarum Mathematicarum **34**, 335–343 (standard log-concavity preservation under convolution).
