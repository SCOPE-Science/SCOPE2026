# Sharp protective-cost ceiling and singular phase-volume collapse in quorum public goods

## Finding

Consider the three-strategy collective-risk public-goods game with quorum-activated protection of Li, Li, He, Shi, and Szolnoki [1]. The theorem provides a sharp upper bound on the protection-maintenance cost that can be offset by protection, proves deterministic disappearance of the protective strategy beyond this bound, and measures the area of the population-composition region permitting a protective payoff advantage immediately below the bound. The latter region exhibits a singular change of exponent at the complete-risk limit.

Set \(n=N-1\), \(a=M-1\), and \(b=N-M\), with \(N\ge3\) and \(2\le M\le N-1\); thus \(a,b\ge1\) and \(a+b=n\). Let \(x,y,z\) be the ordinary cooperator, defector, and protective cooperator fractions in \(\Delta=\{x,y,z\ge0:x+y+z=1\}\). Let \(L>0\) be the catastrophic loss, \(\omega>0\) protection efficacy, \(k>0\) protective maintenance cost, and \(0\le\rho<1\) the survival parameter for one defector's risk. The underlying published model takes \(\rho=e^{-\gamma}>0\); \(\rho=0\) is explicitly a limiting extension, not an interior source parameter.

For the payoffs of [1], the protective-versus-ordinary-cooperator difference is \(P_S-P_C=-k+L\omega\Psi_\rho(x,z)\), where
\[
\Psi_\rho(x,z)=\binom{n}{a}z^a\Big[(1-z)^b-\big(\rho(1-z)+(1-\rho)x\big)^b\Big].
\]
There is one global maximizer in \(\Delta\), namely \((x,z)=(0,a/n)\), and its value is
\[
\Psi_*(\rho)=(1-\rho^b)\binom{n}{a}\left(\frac an\right)^a\left(\frac bn\right)^b.
\]
Consequently \(k_*=L\omega\Psi_*(\rho)\) is the **sharp global payoff-advantage cutoff**: if \(k\ge k_*\), \(P_S\le P_C\) throughout \(\Delta\); if \(0<k<k_*\), \(P_S>P_C\) on a nonempty open set of interior population compositions. Under the three-strategy continuous-time replicator dynamics, at \(k\ge k_*\) every trajectory beginning with both \(x>0\) and \(z>0\) satisfies \(z(t)\to0\) and
\[
\lim_{t\to\infty}\frac1t\log\frac{z(t)}{x(t)}=-k.
\]
This claim does not assert disappearance from an invariant face lacking ordinary cooperators, nor persistence when \(k<k_*\).

To quantify how the favorable region opens, set \(k=(1-\varepsilon)k_*\), \(0<\varepsilon<1\), and let \(\mathcal A_\rho(\varepsilon)\) be its unnormalized Euclidean coordinate area \(dx\,dz\) within \(x>0,z>0,x+z<1\). Define
\[
D=\frac{n^3}{2ab},\qquad H_\rho=\frac{n(1-\rho)\rho^{b-1}}{1-\rho^b}\quad(0<\rho<1).
\]
Then, **for every fixed \(0<\rho<1\)**,
\[
\boxed{\mathcal A_\rho(\varepsilon)\sim\frac{4}{3H_\rho\sqrt D}\varepsilon^{3/2}.}
\]
For the **complete-risk endpoint \(\rho=0\)**, the different law is
\[
\boxed{\mathcal A_0(\varepsilon)\sim\frac{b}{n\sqrt D}\,B\!\left(\frac12,1+\frac1b\right)\varepsilon^{1/2+1/b},}
\]
where \(B\) is Euler's beta function. When \(b\ge2\), the endpoint exponent \(1/2+1/b\) differs from the fixed-positive-\(\rho\) exponent \(3/2\). At \(b=1\) both laws consistently have exponent \(3/2\).

## Assumptions and scope

Groups are formed independently from an infinite well-mixed population; each focal player has \(n=N-1\) independently sampled partners, with ordinary-cooperator, defector, and protective-cooperator probabilities \(x,y,z\). A group receives effective risk reduction if its count of protective players reaches quorum \(M\). For a group with \(j\) defectors, the catastrophe probability is \(1-\rho^j\). The contribution multiplier and contribution cost in [1] cancel in \(P_S-P_C\), so the threshold concerns the pairwise fitness difference rather than the absolute payoffs or full equilibrium diagram. The analysis applies to \(\rho\in(0,1)\) in the published finite-sensitivity model and continuously extends its payoff formula to \(\rho=0\).

The protective-strategy advantage region is an open subset of the two-dimensional frequency simplex, measured using the coordinates \((x,z)\). Area is not normalized by the full simplex area \(1/2\), and it is not an invariant basin or a measure of long-time prevalence.

## Proof

**1. Pivotality and its closed form.** For a protective rather than ordinary focal individual, the group protection status can change only when exactly \(a=M-1\) of the focal player's \(n\) partners are protective. Conditional on those \(a\) partners, the remaining \(b\) independently have types ordinary cooperator or defector. Write the conditional risk weight as \(1-\rho^J\), where \(J\) is their defector count. Summing the multinomial probabilities gives
\[
\begin{aligned}
\Psi_\rho(x,z)
&=\binom{n}{a}z^a\sum_{j=0}^b\binom bj y^j x^{b-j}(1-\rho^j)\\
&=\binom{n}{a}z^a\big[(x+y)^b-(x+\rho y)^b\big],
\end{aligned}
\]
which is the displayed formula since \(x+y=1-z\) and \(x+\rho y=\rho(1-z)+(1-\rho)x\). The payoff difference is exactly the maintenance cost plus the expected avoided loss on this event, establishing \(P_S-P_C=-k+L\omega\Psi_\rho\).

**2. Unique sharp maximizer.** For every \(z\in(0,1)\) and \(\rho<1\), \(\Psi_\rho(x,z)\) is strictly decreasing in \(x\in[0,1-z]\), because the subtracted \(b\)-th power is strictly increasing (also for \(b>1,\rho=0\), though its derivative may vanish at \(x=0\)). Therefore its maximum for fixed \(z\) occurs uniquely at \(x=0\). There,
\[
\Psi_\rho(0,z)=(1-\rho^b)\binom{n}{a}z^a(1-z)^b.
\]
The derivative of its logarithm is \(a/z-b/(1-z)\), giving the unique maximum \(z_*=a/n\) and the displayed \(\Psi_*\). The maximizer has \(y_*=b/n>0\). The payoff cutoff and the existence of a nonempty interior advantage region when \(k<k_*\) follow from strict maximality and continuity.

**3. Global elimination relative to ordinary cooperation.** Replicator dynamics gives the exact identity
\[
\frac{d}{dt}\log\frac{z}{x}=P_S-P_C=-k+L\omega\Psi_\rho(x,z).
\]
When \(k>k_*\), this is bounded above by a strictly negative constant; consequently \(z/x\to0\), and \(z\to0\). When \(k=k_*\), the ratio \(u(t)=z(t)/x(t)\) is nonincreasing. Suppose it tends to \(u_\infty>0\) but \(z\) does not tend to zero. Smoothness of the replicator field on the compact simplex gives a uniform bound on \(|\dot z|\), and hence infinitely many disjoint time intervals of fixed positive length on which \(z\ge\eta>0\). Since \(u\le u(0)\) there, \(x=z/u\ge\eta/u(0)\). The unique maximizer has \(x=0\), so on this compact subset \(\Psi_\rho\le\Psi_*-\delta\) for some \(\delta>0\). The logarithm of \(u\) therefore drops by a fixed amount on each such interval, contradicting its convergence to the finite value \(\log u_\infty\). Hence \(z\to0\) in all cases. Because \(a\ge1\), \(0\le\Psi_\rho\le\binom{n}{a}z^a\to0\). Integrating the logarithmic-ratio identity and using Cesàro averaging proves its limit \(-k\).

**4. Uniform localization near the maximum.** Put \(z=z_*+h\). For any \(\varepsilon\downarrow0\), the region \(\Psi_\rho>(1-\varepsilon)\Psi_*\) is confined to an arbitrarily small neighborhood of \((x,h)=(0,0)\): the function is continuous on the compact simplex and this point is its unique maximizer. Thus only its local asymptotics determine the leading region area; the nearby constraint \(x+z<1\) is inactive because \(y_*=b/n>0\).

**5. Fixed positive survival.** The Taylor expansion at the maximizer is
\[
\frac{\Psi_\rho(x,z_*+h)}{\Psi_*}=1-H_\rho x-Dh^2+o(x+h^2),\qquad 0<\rho<1,
\]
where \(H_\rho\) follows by differentiating the risk-weighted power in \(x\) and \(D=n^3/(2ab)\) is minus half the second derivative of \(\log[z^a(1-z)^b]\) at \(z_*\). After scaling \(x=\varepsilon X\), \(h=\sqrt\varepsilon Z\), the rescaled admissible region tends to \(X\ge0,\ H_\rho X+DZ^2<1\). To justify passage of area, the displayed expansion can be bounded from both sides using any fixed small relative perturbation of the positive coefficients, yielding compact rescaled domains and squeeze convergence. The limiting area is
\[
\int_{-1/\sqrt D}^{1/\sqrt D}\frac{1-DZ^2}{H_\rho}\,dZ=\frac{4}{3H_\rho\sqrt D}.
\]
The Jacobian contributes \(\varepsilon^{3/2}\).

**6. Complete-risk endpoint.** At \(\rho=0\), the exact formula simplifies to \(\Psi_0(x,z)=\binom na z^a[(1-z)^b-x^b]\). As \((x,h)\to(0,0)\),
\[
\frac{\Psi_0(x,z_*+h)}{\Psi_*(0)}
=1-Dh^2-\left(\frac nb\right)^b x^b+o(h^2+x^b).
\]
Here \(z^a/z_*^a=1+O(h)\), so the cross-term in \(h x^b\) is genuinely lower order; the one-sided \(x\) term vanishes when \(b>1\). Scale \(h=\sqrt\varepsilon Z\), \(x=(b/n)\varepsilon^{1/b}X\). The rescaled region tends to \(X\ge0,\ X^b+DZ^2<1\); the same upper/lower perturbation argument gives area convergence. Integrating its horizontal width yields
\[
\frac bn\int_{-1/\sqrt D}^{1/\sqrt D}(1-DZ^2)^{1/b}dZ
=\frac{b}{n\sqrt D}B\!\left(\frac12,1+\frac1b\right).
\]
The Jacobian contributes \(\varepsilon^{1/2+1/b}\), completing the proof.

## Verification

The standalone \(\texttt{verify.py}\) uses exact rational arithmetic to reconstruct the multinomial sum, compare it with the closed polynomial, check the boundary maximum on rational grids, and test the leading asymptotic constants with numerical area integration. These calculations are independent spot checks, not exhaustive proofs over the continuous simplex. The elimination assertion and phase-volume limits are supported by the arguments above, not by numerical trajectory simulations. Run \(\texttt{python3 verify.py}\) from the directory containing the script; the script requires only the Python standard library.

## Relationship to prior work

Li, Li, He, Shi, and Szolnoki [1] introduce the precise three-strategy quorum-activated protection model. Their pivotality payoff difference, bifurcation analysis, and numerical parameter studies are acknowledged, not presented as new. The present result optimizes the risk-weighted pivotality over the entire two-dimensional population simplex, interprets the resulting sharp cutoff for replicator exclusion, and quantifies the area and exponent of the favorable composition region on either side of the singular complete-risk endpoint.

Nöldeke and Peña [2] analyze a classical two-action binary-contribution threshold game, including standard binomial pivotality and critical participation-cost phenomena. Thus maximization of an *unweighted* binomial pivotality probability and generic cost comparisons are not claimed as new. Their two-strategy participation problem neither contains the catastrophe-risk-weighted two-dimensional protective composition field of [1] nor yields the displayed \(\rho\)-dependent area laws without additional analysis. The novelty claim concerns the **model-specific sharp payoff boundary together with the explicit singular phase-volume scaling**; it is not a claim to having invented the pivotality identity or the general replicator logarithmic-ratio identity.

## Limitations

The new result is a same-model mathematical derivation without independent priority certification. Historical equivalence under alternative evolutionary-games terminology remains a risk. The region \(P_S>P_C\) measures instantaneous relative fitness advantage, **not** evolutionary stability, persistence, equilibrium multiplicity, basin volume, or social welfare. Extinction under \(k\ge k_*\) assumes an initially positive ordinary-cooperator frequency. The distinct endpoint exponent requires \(b\ge2\), and the endpoint \(\rho=0\) is the infinite-risk-sensitivity limit of the original finite-risk-sensitivity model. Fixed-\(\rho\) asymptotics are not uniform as \(\rho\downarrow0\). No significance is claimed for generic textbook binomial maximization alone.

## References

[1] Shulan Li, Xiaogang Li, Jun He, Lei Shi, and Attila Szolnoki, *Bifurcation and Multistability in a Collective-Risk Public Goods Game with Quorum-Activated Protection*, first public arXiv posting September 23, 2026, arXiv:2609.28132, https://arxiv.org/abs/2609.28132.

[2] Georg Nöldeke and Jorge Peña, *Group size and collective action in a binary contribution game*, Journal of Mathematical Economics **88** (2020), 42–51, https://doi.org/10.1016/j.jmateco.2020.02.003; openly accessible author manuscript https://jorgeapenas.github.io/assets/pdf/Noeldeke2020.pdf.
