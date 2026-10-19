# A logarithmic extinction hierarchy at the double-critical two-strain epidemic threshold

## Finding

For the eight-compartment, two-strain SIR system with demographic turnover and partial cross-immunity, both basic reproduction ratios may equal one while the two strains vanish at *different* rates. On a sharp marginal-competition surface, the aggregate infection for one strain decays as \(1/[k t\log t]\), while the other decays as \(1/(a_2t)\). These rates and their coefficients are independent of the strictly positive initial strain prevalences.

Specifically, let \(J_1=I_1+I_{21}\), \(J_2=I_2+I_{12}\) and set
\[
 a_1=\frac{\beta_1^2}{\mu},\quad a_2=\frac{\beta_2^2}{\mu},\quad
 b_{12}=\frac{\beta_1(\beta_2-\sigma_{21}\gamma_2)}{\mu},\quad
 b_{21}=\frac{\beta_2(\beta_1-\sigma_{12}\gamma_1)}{\mu},\quad
 k=a_1-b_{21}.
\]
If \(\beta_i=\mu+\gamma_i\) and \(b_{12}=a_2\), then \(k>0\) and for every physical initial state with \(J_1(0),J_2(0)>0\),
\[
 \lim_{t\to\infty}t\log(t)J_1(t)=\frac1k,
 \qquad \lim_{t\to\infty}tJ_2(t)=\frac1{a_2},
\]
and the first-order correction to the dominant strain is
\[
\lim_{t\to\infty}\log(t)\left[tJ_2(t)-\frac1{a_2}\right]
=-\frac{b_{21}}{a_2k}.
\]

## Assumptions and scope

We use the standard nonnegative eight-compartment state \((S,I_1,I_2,I_{21},I_{12},R_1,R_2,R)\), summing to one. Here \(I_{21}\) is secondary infection with strain one following recovery from strain two, and \(I_{12}\) is secondary infection with strain two following recovery from strain one. Let \(\mu>0\), \(\gamma_1,\gamma_2>0\), \(\beta_i=\mu+\gamma_i\), and \(0<\sigma_{21}\le\sigma_{12}\le1\). This last ordering merely labels the strains. The model equations are
\[
\begin{aligned}
\dot S&=\mu(1-S)-\beta_1 S J_1-\beta_2 S J_2,\\
\dot I_1&=\beta_1 S J_1-\beta_1 I_1,\\
\dot I_2&=\beta_2 S J_2-\beta_2 I_2,\\
\dot I_{21}&=\beta_1\sigma_{21}R_2J_1-\beta_1 I_{21},\\
\dot I_{12}&=\beta_2\sigma_{12}R_1J_2-\beta_2 I_{12},\\
\dot R_1&=\gamma_1 I_1-\beta_2\sigma_{12}R_1J_2-\mu R_1,\\
\dot R_2&=\gamma_2 I_2-\beta_1\sigma_{21}R_2J_1-\mu R_2,\\
\dot R&=\gamma_1 I_{21}+\gamma_2 I_{12}-\mu R.
\end{aligned}
\]
The marginal-competition condition is exactly \(\beta_1(\beta_2-\sigma_{21}\gamma_2)=\beta_2^2\). This is feasible in the stated domain; in particular it forces \(\beta_1>\beta_2\), and therefore \(k=\beta_1(\beta_1-\beta_2)/\mu+\beta_2\sigma_{12}\gamma_1/\mu>0\). The result is for \(t\to\infty\) in the deterministic mean-field system, not for finite-population extinction times.

## Proof

**1. Decay of both infections.** Put \(z=1-S\). Conservation and nonnegativity give \(z-\sigma_{21}R_2\ge J_1\) and \(z-\sigma_{12}R_1\ge J_2\). Adding the primary and secondary equations for each strain and using \(\beta_i=\mu+\gamma_i\) yields the exact relations
\[
\dot J_1=-\beta_1J_1(z-\sigma_{21}R_2),\qquad
\dot J_2=-\beta_2J_2(z-\sigma_{12}R_1).
\]
Thus \(\dot J_i\le-\beta_iJ_i^2\), implying \(0<J_i(t)\le[J_i(0)^{-1}+\beta_i t]^{-1}\). Both infections are \(O(t^{-1})\).

**2. Quantified reduction.** Let \(B=\beta_1J_1+\beta_2J_2\). The exact susceptible-deficit equation is \(\dot z=-\mu z+(1-z)B\). A stable linear-convolution estimate gives \(z=O(t^{-1})\). Consequently \(\dot J_i=O(t^{-2})\) and \(\dot B=O(t^{-2})\). Subtracting \(B/\mu\) from the deficit equation shows
\[
 z=\frac{\beta_1J_1+\beta_2J_2}{\mu}+O(t^{-2}).
\]
The linear secondary-infection equations, with forcing \(R_jJ_i=O(t^{-2})\), give \(I_{21},I_{12}=O(t^{-2})\). The recovered-host equations then give
\[
 R_1=\frac{\gamma_1}{\mu}J_1+O(t^{-2}),\qquad
 R_2=\frac{\gamma_2}{\mu}J_2+O(t^{-2}).
\]
Here the elementary estimate used repeatedly is: if \(E'+\mu E=O(t^{-2})\) with \(\mu>0\), then \(E=O(t^{-2})\), by variation of constants. Substitution into the exact equations gives
\[
\begin{aligned}
\dot J_1&=-J_1\big(a_1J_1+b_{12}J_2+O(t^{-2})\big),\\
\dot J_2&=-J_2\big(b_{21}J_1+a_2J_2+O(t^{-2})\big).
\end{aligned}
\]
The error bounds refer to the **full** eight-dimensional solution, with constants allowed to depend on the fixed initial state.

**3. Marginal competition in logarithmic time.** Write \(s=\log t\), \(u_i(s)=tJ_i(t)\) for \(t>1\). Both \(u_i\) are bounded above by the Riccati estimate. On \(b_{12}=a_2\), their equations become
\[
\begin{aligned}
 u_1'&=u_1[1-a_1u_1-a_2u_2+O(e^{-s})],\\
 u_2'&=u_2[1-b_{21}u_1-a_2u_2+O(e^{-s})].
\end{aligned}
\]
For \(r=u_1/u_2>0\),
\[
 (\log r)'=-k u_1+O(e^{-s}).
\]
Because the error is integrable, \(r\) is bounded above and has a limit. The bound \(u_1\le M u_2\), together with the second equation, supplies a positive uniform lower bound on \(u_2\) for sufficiently large \(s\), by comparison with positive logistic equations. If the limit of \(r\) were positive, \(u_1\) would remain bounded below, forcing \(\log r\to-\infty\), a contradiction. Hence \(u_1\to0\). The second equation is now asymptotically logistic and gives \(u_2\to1/a_2\).

Taking the reciprocal ratio \(v=1/r\), we obtain
\[
 v'=ku_2+O(e^{-s}v).
\]
Variation of constants and integrability of \(e^{-s}\) imply \(v=O(1+s)\); dividing its integral equation by \(s\) gives \(v/s\to k/a_2\). Consequently \(s u_1=s r u_2\to1/k\), proving the two leading limits.

Finally, setting \(w=u_2-1/a_2\) yields
\[
 w'+a_2u_2w=-b_{21}u_1u_2+O(e^{-s}).
\]
As \(a_2u_2\to1\), \(su_1\to1/k\), and \(u_2\to1/a_2\), the stable-convolution asymptotic implies \(sw\to-b_{21}/(a_2k)\). This proves the correction term.

## Verification

Run `python verify.py` with Python 3, NumPy, and SciPy. It checks the marginal-competition algebra with exact rational arithmetic and independently integrates the **entire** normalized eight-compartment system for two parameter choices, one with partial cross-immunity. It verifies conservation, aggregate-infection identities, positivity, and finite-time convergence indicators. These tests are illustrations, not infinite-time proofs. The proof above establishes the asymptotic limits for all stated physical initial conditions.

For example, with \(\mu=1\), \(\gamma_1=3\), \(\gamma_2=1\), and \(\sigma_{21}=\sigma_{12}=1\), the constants are \(a_2=4\) and \(k=14\), so the exact limits are \(1/4\) and \(1/14\). With \(\mu=1\), \(\gamma_1=5/3\), \(\gamma_2=1\), \(\sigma_{21}=1/2\), and \(\sigma_{12}=3/4\), the constants are \(a_2=4\), \(k=77/18\), with limits \(1/4\) and \(18/77\).

## Relationship to prior work

Gavish's December 2024 preprint (later published in August 2026) formulates this same demographic two-strain cross-immunity system and analyzes stability/oscillations of *positive coexistence equilibria* for reproduction numbers greater than one. It does not establish a joint critical threshold decay law, the additional marginal-competition equality, or these logarithmic asymptotic constants. Chung and Lui's 2016 work analyzes local coexistence stability and periodic bifurcation; the current result instead concerns the global approach to the disease-free state at a double-critical boundary. Standard competitive Lotka–Volterra asymptotics motivate the method but do not alone establish the quantified reduction and universal constants for the eight-compartment system.

## Limitations

All three parameter equalities are essential to the stated marginal critical regime; different parameter values can produce different rates. Both aggregate infections must be initially positive; the single-strain invariant boundary has a different asymptotic. Estimates concern deterministic asymptotics as \(t\to\infty\), not stochastic elimination or realistic time windows. No general result for supercritical coexistence, interventions, spatial heterogeneity, or temporal forcing is implied. Literature search does not establish absolute novelty; specialized unindexed general theorems on critical multi-strain systems could subsume the conclusion.

## References

1. N. Gavish, *A new oscillatory regime in two-strain epidemic models with partial cross-immunity*, arXiv:2412.07536v1, first public 2024-12-10. https://arxiv.org/abs/2412.07536 .
2. N. Gavish, *Hidden Oscillations: How Minimal Immunological Interactions Destabilize Two-Strain Epidemic Models*, SIAM Journal on Life Sciences 1 (2026), 420–443. DOI: 10.1137/25M1826160. https://epubs.siam.org/doi/full/10.1137/25M1826160 .
3. K. W. Chung and R. Lui, *Dynamics of two-strain influenza model with cross-immunity and no quarantine class*, J. Math. Biol. 73 (2016), 1467–1489. DOI: 10.1007/s00285-016-1000-x.
4. S. Kadyrov, F. Haydarov, K. Mamayusupov, and K. Mustayev, *Endemic coexistence and competition of virus variants under partial cross-immunity*, Electron. Res. Arch. 33 (2025), 1120–1143. DOI: 10.3934/era.2025050.
