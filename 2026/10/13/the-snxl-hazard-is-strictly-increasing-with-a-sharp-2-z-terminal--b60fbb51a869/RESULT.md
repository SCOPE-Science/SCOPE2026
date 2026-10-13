# The SNXL hazard is strictly increasing with a sharp \(2/z\) terminal gap
## Finding
For the Sine New X–Lindley distribution with parameter \\(\\xi>0\\), its hazard \\(h_\\xi(z)\\) is strictly increasing on \\((0,\\infty)\\). More precisely,
\\[
h_\\xi(0+)=\\frac{\\pi\\xi}{4},
\\qquad
\\frac{\\pi\\xi}{4}<h_\\xi(z)<2\\xi \\quad(z>0),
\\]
and the approach to the terminal level has the sharp first-order law
\\[
\\lim_{z\\to\\infty}z\\bigl(2\\xi-h_\\xi(z)\\bigr)=2.
\\]

The proof comes from a general preservation law for the classical Sin-G transform. Let a baseline distribution have cdf \\(F\\), survival \\(S=1-F\\), positive density \\(f\\), and hazard \\(h_0=f/S\\). Its Sin-G transform
\\[
F_S(x)=\\sin\\!\\left(\\frac{\\pi}{2}F(x)\\right)
\\]
has hazard
\\[
h_S(x)=h_0(x)\\,\\Phi(S(x)),
\\qquad
\\Phi(s)=\\frac{\\pi s}{2}\\cot\\!\\left(\\frac{\\pi s}{4}\\right).
\\]
The multiplier \\(\\Phi\\) is strictly decreasing in \\(s\\), so \\(\\Phi(S(x))\\) is strictly increasing in \\(x\\). Hence every positive-density baseline with nondecreasing hazard is sent to a strictly increasing-hazard distribution.

For the New X–Lindley baseline this gives the claimed SNXL law directly. The 2019 Sin-G paper already records the weaker general tail equivalence \\(h_S\\sim2h_0\\) as \\(F\\to1\\); therefore the terminal value \\(2\\xi\\) alone is not claimed as new. The new refinement is the global monotonicity/preservation result together with the exact \\(2/z\\) first-order gap.

## Assumptions and scope
For the general preservation statement, assume an absolutely continuous baseline on an interval with survival \\(S(x)>0\\), positive density \\(f(x)>0\\), and nondecreasing hazard \\(h_0(x)=f(x)/S(x)\\). Positivity of \\(f\\) makes \\(S\\) strictly decreasing.

For the SNXL specialization, \\(z>0\\) and \\(\\xi>0\\). The New X–Lindley baseline used by the source has
\\[
S_0(z)=e^{-\\xi z}\\left(1+\\frac{\\xi z}{2}\\right),
\\qquad
f_0(z)=\\frac{\\xi}{2}(1+\\xi z)e^{-\\xi z}.
\\]
No numerical shape inspection is used to infer monotonicity.

## Proof
For a general baseline, write \\(S=1-F\\). Since
\\[
F_S=\\sin\\!\\left(\\frac{\\pi F}{2}\\right)
=\\cos\\!\\left(\\frac{\\pi S}{2}\\right),
\\]
the transformed survival and density are
\\[
S_S=1-\\cos\\!\\left(\\frac{\\pi S}{2}\\right),
\\qquad
g_S=\\frac{\\pi}{2}f\\sin\\!\\left(\\frac{\\pi S}{2}\\right).
\\]
Using \\(\\sin a/(1-\\cos a)=\\cot(a/2)\\),
\\[
h_S
=\\frac{g_S}{S_S}
=\\frac{\\pi}{2}f\\cot\\!\\left(\\frac{\\pi S}{4}\\right)
=h_0\\,\\Phi(S),
\\]
where
\\[
\\Phi(s)=\\frac{\\pi s}{2}\\cot\\!\\left(\\frac{\\pi s}{4}\\right).
\\]
Put \\(y=\\pi s/4\\). Then \\(\\Phi(s)=2y\\cot y\\) and
\\[
\\frac{d}{dy}(2y\\cot y)
=\\frac{2(\\sin y\\cos y-y)}{\\sin^2 y}<0
\\]
for \\(0<y\\le\\pi/4\\), because \\(\\sin(2y)<2y\\). Thus \\(\\Phi\\) strictly decreases with \\(s\\). Since \\(S\\) strictly decreases with \\(x\\), \\(\\Phi(S(x))\\) strictly increases. If \\(h_0\\) is positive and nondecreasing, the product \\(h_0(x)\\Phi(S(x))\\) is strictly increasing.

Also,
\\[
\\Phi(1)=\\frac{\\pi}{2},
\\qquad
\\lim_{s\\downarrow0}\\Phi(s)=2,
\\]
so \\(\\pi/2\\le\\Phi(s)<2\\) on \\((0,1]\\).

For the New X–Lindley baseline, set \\(t=\\xi z\\). Its hazard is
\\[
h_0(z)=\\xi\\frac{1+t}{2+t},
\\qquad
h_0'(z)=\\frac{\\xi^2}{(2+t)^2}>0,
\\]
with limits \\(h_0(0+)=\\xi/2\\) and \\(h_0(\\infty)=\\xi\\). The preservation result therefore proves strict increase of the SNXL hazard and gives the endpoint values and upper bound.

For the sharper terminal rate, put
\\[
s(t)=e^{-t}\\left(1+\\frac{t}{2}\\right),
\\qquad
A(t)=\\frac{1+t}{2+t}.
\\]
Then
\\[
\\frac{h_\\xi(z)}{\\xi}=A(t)\\Phi(s(t)).
\\]
The cotangent expansion at zero gives
\\[
2-\\Phi(s)=\\frac{\\pi^2}{24}s^2+O(s^4).
\\]
Hence
\\[
2-\\frac{h_\\xi(z)}{\\xi}
=\\frac{2}{t+2}+A(t)\\{2-\\Phi(s(t))\\}.
\\]
Because \\(t\\,s(t)^2\\to0\\), multiplication by \\(t=\\xi z\\) yields
\\[
z\\{2\\xi-h_\\xi(z)\\}
=t\\left[\\frac{2}{t+2}+A(t)\\{2-\\Phi(s(t))\\}\\right]\\longrightarrow2.
\\]

## Verification
The proof is analytic. The bundled checker independently evaluates the exact factorization, verifies positivity of the derivative on a deterministic grid for several \\(\\xi\\), checks the endpoint bounds, and confirms numerically that \\(z(2\\xi-h_\\xi(z))\\) approaches \\(2\\). These computations are supplementary and are not used as a proof of the infinite-domain statements.

The critical nonstandard comparison was made against the actual 2026 source formula for the SNXL hazard and its Remark 2.4. That remark explicitly states that monotonicity and a finite positive horizontal asymptote require separate establishment. The 2019 Sin-G primary paper was also inspected: it gives the general hazard formula, a critical-point derivative expression, and the asymptotic relation \\(R_G(x)\\sim2g(x)/(1-G(x))\\) as \\(G(x)\\to1\\), but does not state IFR preservation.

## Relationship to prior work
Souza et al. (2019) define the classical Sin-G class \\(F_S=\\sin(\\pi F/2)\\), give its hazard formula, and analyze critical points. They also prove the asymptotic relation \\(h_S\\sim2h_0\\) near the right tail. That prior result already implies \\(h_\\xi(z)\\to2\\xi\\) for the New X–Lindley baseline, so the terminal level by itself is covered prior work.

Muse et al. (2025) use the same Sine-G family as baseline hazards in Bayesian survival models and emphasize the family's ability to exhibit varied hazard shapes. Their full text gives the general hazard construction and studies several examples graphically; it does not state that the transform preserves increasing failure rate for every positive IFR baseline.

Nedjar, Zeghdoudi, and Alqifari (2026) introduce the SNXL model, give the exact hazard, prove \\(h_\\xi(0+)=\\pi\\xi/4\\), and obtain the survival-tail rate. Their Remark 2.4 explicitly leaves monotonicity and a finite positive horizontal asymptote to be established separately. The present result closes the monotonicity question and sharpens the tail description from a limiting level to the first-order gap \\(2/z\\).

Focused statement-level searches using IFR, increasing-failure-rate, hazard-ratio, cotangent-multiplier, SNXL monotonicity, and sharp terminal-gap aliases did not locate an equivalent published theorem or correction.

## Limitations
The preservation theorem is one-directional: an IFR baseline produces a strictly IFR Sin-G transform. No converse is claimed, and the transform can produce many nonmonotone shapes from non-IFR baselines.

The asymptotic statement concerns the SNXL hazard itself and does not supply finite-sample inference for \\(\\xi\\) or uncertainty bands for a fitted hazard. The older general Sin-G tail equivalence is acknowledged as prior coverage of the zeroth-order limit.

An unindexed note or differently phrased reliability theorem may contain the same IFR-preservation observation; this remains the principal originality risk.

## References
1. S. Nedjar, H. Zeghdoudi, and H. N. Alqifari, “Statistical properties of the Sine New X–Lindley distribution: fuzzy reliability analysis and applications,” AIMS Mathematics 11 (2026), 11924–11947. DOI: 10.3934/math.2026489.
2. L. Souza, W. R. de O. Júnior, C. C. R. de Brito, C. Chesneau, T. A. E. Ferreira, and L. G. M. Soares, “On the Sin-G class of distributions: theory, model and application,” Journal of Mathematical Modeling 7 (2019), 357–379. DOI: 10.22124/jmm.2019.13502.1278.
3. A. H. Muse, A. Almohaimeed, H. N. Alqifari, and C. Chesneau, “Sine-G family of distributions in Bayesian survival modeling: A baseline hazard approach for proportional hazard regression with application to right-censored oncology datasets using R and STAN,” PLOS ONE 20 (2025), e0307410. DOI: 10.1371/journal.pone.0307410.
