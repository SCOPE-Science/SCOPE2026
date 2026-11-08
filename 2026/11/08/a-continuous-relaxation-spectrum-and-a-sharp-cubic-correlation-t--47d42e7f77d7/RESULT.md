# A continuous relaxation spectrum and a sharp cubic correlation tail for a reset-cooled granular gas

## Finding

**Theorem (spectral edge of Poisson-reset Haff cooling).** Fix a reset rate \(r>0\), cooling time \(\tau>0\), initial temperature \(T_0>0\), and cooling exponent \(q>0\). At each point of a stationary rate-\(r\) Poisson process, set the temperature to \(T_0\); between those points let the temperature at age \(u\ge0\) be
\[
g(u)=T_0(1+u/\tau)^{-q}.
\]
Let \(\mathcal T_t\) denote this stationary temperature process, let \(C(t)=\operatorname{Cov}(\mathcal T_0,\mathcal T_t)\) for \(t\ge0\), and let
\[
m(r)=\mathbb E\mathcal T_0
    =r\int_0^\infty e^{-ru}g(u)\,du.
\]
The following statements hold for **every** such choice of positive parameters.

1. \(C\) is strictly completely monotone: \((-1)^n C^{(n)}(t)>0\) for every integer \(n\ge0\) and \(t\ge0\). It has an absolutely continuous, strictly positive exponential-mixture measure on precisely the rate interval \((r,\infty)\), with no atom at \(r\).
2. The spectral density at rate \(r+s\), for \(s>0\), is
\[
\mathcal W(r+s)=T_0^2w_q(s)\int_0^\infty w_q(u)
\frac{r s u}{(r+s+u)(r+s)(r+u)}\,du,
\qquad
w_q(u)=\frac{\tau^q}{\Gamma(q)}u^{q-1}e^{-\tau u}.
\]
In particular, with the strictly positive derivative \(m'(r)\),
\[
\mathcal W(r+s)\sim\frac{T_0\tau^q m'(r)}{\Gamma(q)}s^q
\qquad(s\downarrow0),
\]
and the **sharp** stationary covariance tail is
\[
\boxed{\displaystyle C(t)\sim qT_0\tau^q m'(r)\,e^{-rt}t^{-(q+1)} }
\qquad(t\to\infty).
\]
3. The effective relaxation rate \(\Lambda(t)=-C'(t)/C(t)\) is strictly decreasing, exceeds \(r\) at every finite \(t\ge0\), and obeys
\[
\Lambda(t)=r+\frac{q+1}{t}+O(t^{-2})
\qquad(t\to\infty).
\]
Hence the asymptotic exponential rate and the cooling exponent are identifiable from the exact covariance curve via \(r=\lim_{t\to\infty}\Lambda(t)\) and \(q=\lim_{t\to\infty}t(\Lambda(t)-r)-1\).

For ordinary Haff cooling \(q=2\), put \(x=r\tau\) and \(E_1(x)=\int_x^\infty e^{-u}du/u\). Then the result specializes to
\[
\boxed{\displaystyle
C(t)\sim 2T_0^2\tau^3\bigl[1+x-(x^2+2x)e^xE_1(x)\bigr]
\frac{e^{-rt}}{t^3}. }
\]
The coefficient in square brackets is strictly positive for all \(x>0\).

## Assumptions and scope

The temperature is a **scalar idealized cooling observable**, not an individual particle velocity or a fluctuating finite-particle kinetic energy. Resets occur at all points of an independent two-sided homogeneous Poisson process of rate \(r\). Every reset fixes the whole scalar temperature at \(T_0\). Between resets cooling is deterministic with the displayed Haff-type law; the other parameters are held fixed and positive. Stationarity means the two-sided Poisson construction, so that the elapsed time \(A\) since the last reset at an arbitrary time has the exponential distribution with rate \(r\). No singular limit with parameters varying alongside \(t\) is asserted.

## Proof

**Step 1: renewal covariance.** Let \(A\sim\operatorname{Exp}(r)\) be the stationary age at time zero, independent of future Poisson points. If there is no reset in \((0,t]\), an event of probability \(e^{-rt}\), then \((\mathcal T_0,\mathcal T_t)=(g(A),g(A+t))\). If there is a reset, the new value \(\mathcal T_t\) depends only on post-zero Poisson points and is independent of \(A\). Subtracting the product of stationary means therefore gives the exact identity
\[
C(t)=e^{-rt}\operatorname{Cov}(g(A),g(A+t)),
\qquad t\ge0.\tag{1}
\]
The two functions of \(A\) in (1) are strictly decreasing. An independent-copy identity for covariance gives strict positivity of their covariance.

**Step 2: a positive exponential spectral mixture.** The cooling function is a Gamma mixture of exponentials:
\[
g(a)=T_0\int_0^\infty w_q(s)e^{-sa}\,ds,
\qquad
w_q(s)=\frac{\tau^q s^{q-1}e^{-\tau s}}{\Gamma(q)}.
\]
Because \(\mathbb E e^{-zA}=r/(r+z)\), for \(s,u>0\),
\[
\operatorname{Cov}(e^{-sA},e^{-uA})
=\frac{r}{r+s+u}-\frac{r^2}{(r+s)(r+u)}
=\frac{r s u}{(r+s+u)(r+s)(r+u)}>0.\tag{2}
\]
Tonelli's theorem applied to (1) and (2) yields
\[
C(t)=\int_r^\infty e^{-\lambda t}\mathcal W(\lambda)\,d\lambda,
\]
with the stated \(\mathcal W\). It is strictly positive for each \(\lambda>r\), vanishes outside this interval, and has finite moments of every order by the exponential factor in \(w_q\). Differentiation under the integral proves strict complete monotonicity at all nonnegative times. The rate spectrum is continuous: the phrase *spectrum* here denotes this specific exponential-mixture measure, not a claim of a self-adjoint Markov generator.

**Step 3: edge coefficient and long-time limit.** Differentiating the mean under its convergent integral and using the Gamma representation gives
\[
m'(r)=T_0\int_0^\infty w_q(u)\frac{u}{(r+u)^2}\,du>0.\tag{3}
\]
For fixed \(u>0\), the fraction in (2), divided by \(s\), tends to \(u/(r+u)^2\) as \(s\downarrow0\); a constant-times-integrable bound permits dominated convergence over \(u\). Together with \(w_q(s)\sim\tau^q s^{q-1}/\Gamma(q)\), this proves the stated spectral-edge equivalence. The rational kernel and the factor \(e^{-\tau s}\) are smooth near \(s=0\), permitting one additional relative \(O(s)\) term. Laplace scaling, \(\int_0^\infty e^{-st}s^qds=\Gamma(q+1)t^{-(q+1)}\), then gives
\[
C(t)=qT_0\tau^q m'(r)e^{-rt}t^{-(q+1)}[1+O(t^{-1})].\tag{4}
\]
This argument controls the entire tail by exponential domination away from \(s=0\). It does not use numerical extrapolation.

An independent check of the leading coefficient follows directly from (1): as \(t\to\infty\), a first-order Taylor expansion in \((A+\tau)/t\), with a remainder bounded by a constant times \((A+\tau)^2/t^2\), yields
\[
\operatorname{Cov}(g(A),g(A+t))
=-qT_0\tau^q\operatorname{Cov}(g(A),A)t^{-(q+1)}
+O(t^{-(q+2)}).
\]
Differentiating the exponential-age expectation shows \(\operatorname{Cov}(g(A),A)=-m'(r)\), recovering (4).

**Step 4: strict rate monotonicity.** Define a probability measure by normalizing \(e^{-\lambda t}\mathcal W(\lambda)d\lambda\) with \(C(t)\). Then
\[
\Lambda(t)=\mathbb E_t[\lambda],
\qquad
\Lambda'(t)=-\operatorname{Var}_t(\lambda)<0.
\]
The variance is strictly positive because the density is positive throughout \((r,\infty)\). Thus \(\Lambda(t)>r\). The edge expansion in Step 3 also gives, by applying the same Laplace estimate to \((\lambda-r)\mathcal W(\lambda)\),
\[
\Lambda(t)-r=\frac{q+1}{t}+O(t^{-2}).
\]
Both identification limits follow.

**Step 5: physical Haff exponent.** For \(q=2\), integration by parts gives
\[
m(r)=T_0x[1-xe^xE_1(x)],\qquad x=r\tau.
\]
Consequently,
\[
m'(r)=T_0\tau[1+x-(x^2+2x)e^xE_1(x)].
\]
Substitution in (4) proves the displayed cubic prefactor. Its positivity is already guaranteed by (3), without relying on potentially ill-conditioned subtraction of special-function values.

## Verification

`checker.py` uses only the Python standard library. Running `python3 checker.py` from the extracted package performs 40 numerical assertions: independent single-age and double-Gamma spectral integrations, the source's stationary variance identity, derivative-sign finite differences, strict effective-rate ordering, the exact \(q=2\) special-function coefficient, asymptotic-ratio tests, and positivity for noninteger exponents. The full mathematical claims are justified by the preceding proof, not by the finite set of numerical checks.

## Relationship to prior work

Bodrova, Chechkin, and Dubey (arXiv:2403.18974; first public version 2024-03-27), in their Eqs. (11)--(21) and (27), supply the power-law cooling model, Poisson renewal setting, stationary **one-time** temperature distribution, mean, and variance. These ingredients are credited; the article's inspected theory, simulation, and conclusions sections do not state the stationary two-time covariance, its positive continuous spectral density, the sharp \(e^{-rt}t^{-(q+1)}\) tail, or the strictly decreasing effective relaxation rate. The source's fixed-parameter one-time formulas alone do not assert any of these dynamical properties.

Rose, Touchette, Lesanovsky, and Garrahan (arXiv:1806.01298) study general shifts of Markov-generator eigenvalues under resetting; this supports expecting the exponential reset scale but does not state the model-specific positive covariance density and its spectral-edge coefficient. Stojkoski, Sandev, Kocarev, and Pal (arXiv:2107.11686) investigate two-time correlations for freely diffusing or drift-diffusing reset processes, whose reset-free trajectories are not deterministic Haff cooling. Brey and Ruiz-Montero (arXiv:1501.04757) study **velocity** correlations in freely cooling granular fluids, not temperature-memory correlations under externally imposed Poisson resetting. These comparisons distinguish the statements rather than merely their titles. The broader sources were compared through accessible abstracts and descriptions, so unindexed or differently formulated coverage remains possible.

## Limitations

This is an exact theorem for the scalar, fully renewed deterministic cooling model, not for the microscopic finite-particle hard-sphere simulation with residual kinetic-energy fluctuations, incomplete velocity reassignment, collision-induced memory, or colored/reset-dependent heating. The covariance is a stationary ensemble quantity; no claim is made about finite-window estimation or practical numerical stability of the two large-lag identification limits. Nor is the exponential-mixture representation claimed to be the operator spectrum of a reversible process. Publication-priority comparison is necessarily limited to the accessible sources described above. No independent scientific validation has been performed.

## References

1. A. S. Bodrova, A. V. Chechkin, and A. K. Dubey, *Granular gases under resetting*, arXiv:2403.18974 (first public version 2024-03-27), https://arxiv.org/abs/2403.18974 ; Phys. Rev. E 111, 015405 (2025).
2. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018), https://arxiv.org/abs/1806.01298 .
3. V. Stojkoski, T. Sandev, L. Kocarev, and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686 (2021), https://arxiv.org/abs/2107.11686 .
4. J. J. Brey and M. J. Ruiz-Montero, *Power-law decay of the velocity autocorrelation function of a granular fluid in the homogeneous cooling state*, arXiv:1501.04757 (2015), https://arxiv.org/abs/1501.04757 .
