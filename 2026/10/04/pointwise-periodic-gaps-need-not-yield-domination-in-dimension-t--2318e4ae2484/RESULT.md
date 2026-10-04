# Pointwise periodic gaps need not yield domination in dimension two
## Finding
Fix the full two-sided shift on two symbols with the standard metric parameter \(0<\theta<1\) and a Hölder exponent \(\alpha>0\). Let \(\varphi=(1+\sqrt5)/2\). For every sufficiently small \(t>0\), the locally constant \(\mathrm{SL}(2,\mathbb R)\)-cocycle defined by \(A(0)=\operatorname{diag}(e^t,e^{-t})\) and \(A(1)=\operatorname{diag}(e^{-\varphi t},e^{\varphi t})\) is strongly bunched, every periodic orbit has two distinct Lyapunov exponents, yet the cocycle has no dominated splitting. Indeed the Bernoulli measure assigning weight \(1/\varphi\) to symbol \(0\) has both Lyapunov exponents equal to zero. Consequently the uniform constant in a periodic Lyapunov-gap criterion cannot be replaced by mere pointwise positivity even for strongly bunched two-dimensional cocycles arbitrarily close to the identity.

## Assumptions and scope
Let \(\Sigma=\{0,1\}^{\mathbb Z}\) be the full two-sided shift with metric \(d_\theta\), where \(0<\theta<1\), and fix \(\alpha>0\). Set \(\varphi=(1+\sqrt5)/2\). Choose
\[
0<t<\frac{-\alpha\log\theta}{2\varphi}.
\]
Define the locally constant cocycle \(A:\Sigma\to\mathrm{SL}(2,\mathbb R)\) by
\[
A(0)=\operatorname{diag}(e^t,e^{-t}),\qquad A(1)=\operatorname{diag}(e^{-\varphi t},e^{\varphi t}).
\]
The claim concerns this explicit family. It does not assert strong irreducibility; the matrices preserve the coordinate axes. It also does not weaken Backes's theorem: Backes assumes a single positive lower bound for all periodic gaps, whereas here the gaps are positive one by one but have infimum zero.

## Proof
In dimension two, Backes's strong-bunching condition is exactly fiber bunching. For a diagonal matrix \(\operatorname{diag}(e^s,e^{-s})\), its bolicity is \(e^{2|s|}\). Hence for the two one-step matrices above,
\[
\sup_{x\in\Sigma}\operatorname{bol}(A(x))\,\theta^\alpha=e^{2\varphi t}\theta^\alpha<1.
\]
Thus the cocycle is fiber-bunched, hence strongly bunched, already with the first iterate.

Let \(p\) be a periodic point of period \(n\), and let \(m\) be the number of zero symbols in one period. Since the two matrices commute,
\[
A^n(p)=\operatorname{diag}(e^s,e^{-s}),\qquad s=t\bigl(m-\varphi(n-m)\bigr).
\]
The two ordered Lyapunov exponents are therefore \(|s|/n\) and \(-|s|/n\), so their gap is \(2|s|/n\). If \(s=0\), then \(m/n=\varphi/(1+\varphi)=1/\varphi\), which is impossible because \(m/n\) is rational and \(1/\varphi\) is irrational. Thus every periodic orbit has a strictly positive gap.

Now let \(\mu\) be the Bernoulli measure for which symbol \(0\) has probability \(1/\varphi\). By the ergodic theorem, the exponent along the first coordinate is
\[
t\left(\frac1\varphi-\varphi\left(1-\frac1\varphi\right)\right)=0,
\]
using \(\varphi-1=1/\varphi\). The second-coordinate exponent is also zero. A dominated splitting would force a uniform positive Lyapunov gap for every ergodic invariant probability measure, so this zero-gap ergodic measure rules out domination.

Finally, rational approximations \(m/n\to1/\varphi\) give periodic gaps tending to zero. Since \(t\) can be chosen arbitrarily small while preserving the displayed bunching inequality, such examples occur arbitrarily close to the identity cocycle.

## Verification
The proof uses only diagonal matrix multiplication, the identity \(\varphi^2=\varphi+1\), the Bernoulli ergodic theorem, and the standard consequence of domination that the relevant Lyapunov gap is bounded below uniformly over ergodic invariant measures. Backes states both the two-dimensional identification of strong bunching with fiber bunching and the required fiber-bunching inequality. His introduction also records the uniform-gap consequence of domination.

## Relationship to prior work
Backes proves that, under strong bunching, a uniform periodic gap \(\lambda_k(p)-\lambda_{k+1}(p)\ge c>0\) forces a dominated splitting. He cites Kassel–Potrie Example 3.8 to show that the uniformity cannot in general be removed; that published example is a locally constant \(\mathrm{GL}(3,\mathbb R)\) cocycle. Kassel–Potrie separately point to finer two-dimensional results of Avila–Bochi–Yoccoz. Sadovskaya discusses two-dimensional nonuniformly hyperbolic cocycles whose periodic exponents can become arbitrarily close, but describes the relevant phenomenon as occurring at almost all periodic points. The explicit family above isolates the sharp lowest-dimensional boundary needed for the recent theorem: every periodic orbit has simple spectrum, the cocycle is strongly bunched and can be made arbitrarily close to the identity, yet an ergodic Bernoulli measure has zero gap and domination fails.

Targeted database and literature searches did not locate this exact two-matrix irrational-diagonal formulation or a stronger statement implying all of its features simultaneously. The construction is elementary, so an unindexed folklore occurrence remains possible.

## Limitations
The example is reducible and commuting, so it does not address the stronger irreducibility question mentioned by Kassel–Potrie. It proves a sharp logical boundary for replacing a uniform periodic gap by pointwise positivity, not a classification of all nondominated two-dimensional cocycles. No claim is made that the construction is the only or most dynamically complicated obstruction.

## References
1. Lucas Backes, From a Gap in the Lyapunov Spectrum to Dominated Splittings, arXiv:2609.28384v1.
2. Fanny Kassel and Rafael Potrie, Eigenvalue gaps for hyperbolic groups and semigroups, arXiv:2002.07015; J. Mod. Dyn. 18 (2022), 161–208.
3. Artur Avila, Jairo Bochi, and Jean-Christophe Yoccoz, Uniformly Hyperbolic Finite-Valued SL(2,R)-Cocycles, arXiv:0808.0133; Comment. Math. Helv. 85 (2010), 813–884.
4. Victoria Sadovskaya, Cohomology of GL(2,R)-valued cocycles over hyperbolic systems, arXiv:1008.2564; Discrete Contin. Dyn. Syst. 33 (2013), 2085–2104.
