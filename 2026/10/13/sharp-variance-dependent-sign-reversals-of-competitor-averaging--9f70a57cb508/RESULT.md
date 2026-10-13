# Sharp variance-dependent sign reversals of competitor averaging in three-allele Moran fixation

## Finding

Consider a well-mixed population of exactly three individuals carrying three distinct alleles \(A\), \(B\), and \(C\), initially one copy of each. Every allele has a positive constant reproductive fitness, respectively \(a\), \(b\), and \(c\). Each discrete-time Moran update independently chooses one parent with probability proportional to its fitness and chooses one of the three individuals uniformly for replacement. There are no mutations.

Let \(P_A\) denote the probability that eventually all three individuals carry allele \(A\). The two-allele mean-background approximation replaces both competing genotypes with fitness \(m=(b+c)/2\), and keeps the same three-individual Moran birth--death update. Write \(P_{\rm av}\) for its exact target fixation probability from one \(A\).

**Theorem (exact three-allele averaging-bias diagram).** For all \(a,b,c>0\), let \(d=(b-c)/2\). Then \(|d|<m\), and
\[
P_A=\frac{a^2[2a^2+a(b+c)+2bc]}{2(a^2+ab+b^2)(a^2+ac+c^2)},\qquad
P_{\rm av}=\frac{a^2}{a^2+am+m^2}.
\]
Their difference factors exactly as
\[
\boxed{
P_A-P_{\rm av}=\frac{a^2d^2[(m-a)(m+2a)-d^2]}{(a^2+a(m+d)+(m+d)^2)(a^2+a(m-d)+(m-d)^2)(a^2+am+m^2)}.}
\]
Consequently, if \(d\ne0\), the mean-background approximation overestimates fixation for every \(a\ge m\), underestimates fixation for every \(0<a\le m/2\), and for \(m/2<a<m\) underestimates below the **sharp variance boundary** \(d^2=(m-a)(m+2a)\), equals the exact value on that boundary, and overestimates above it. When \(d=0\), aggregation is exact for any \(a>0\).

In particular, at fixed target fitness \(a=2\) and fixed background mean \(m=3\), choosing \((b,c)=(2,4)\) gives \(P_A=3/14>P_{\rm av}=4/19\) with difference \(1/266\), whereas \((b,c)=(1/4,23/4)\) gives \(P_A=3904/18907<4/19\), with difference \(-1452/359233\). The error sign can therefore reverse solely through background dispersion, with all reproductive fitnesses positive.

## Assumptions and scope

The stochastic process is **finite**, mutation-free and frequency-independent. Both parent and death selections are independent; self-replacement is allowed. Fitness is inherited by genotype and fixed over time. All probabilities refer to eventual allele fixation from state \((1,1,1)\), not finite-time prevalence. The mean-background approximation is the **exact two-allele Moran law** with competitor fitness \(m\): it is not Kimura's diffusion probability or the different Wright--Fisher mean-field approximation.

The population size is exactly three, the smallest size admitting three simultaneous alleles. No weak-selection assumption is made. The symmetric variables satisfy \(a>0\), \(m>0\), \(|d|<m\), and \(d=0\) is permitted.

## Proof

**1. Edge fixation probabilities.** In a three-individual two-allele Moran process with target reproductive fitness \(a>0\) and competitor fitness \(z>0\), the ratio of the one-step target-decrease to target-increase probabilities at each nonabsorbing count is \(z/a\). The standard birth--death recurrence gives the target fixation probabilities from one or two copies, respectively:
\[
K_1(a,z)=\frac{a^2}{a^2+az+z^2},\qquad
K_2(a,z)=\frac{a(a+z)}{a^2+az+z^2}.
\]
These are verified directly by the two interior harmonic equations and boundary values zero and one.

**2. The unique three-allele interior state.** At state \((1,1,1)\), write \(F=a+b+c\). A specified allele \(i\) replacing another specified allele \(j\) has probability \(f_i/(3F)\). Since exactly one-third of steps are self-replacements, conditioning on the first state change makes each ordered inter-allele replacement have probability \(f_i/(2F)\). After one change, one allele is extinct and all subsequent dynamics lie on a two-type edge. Events in which either competitor replaces \(A\) contribute zero to its eventual fixation. The other four ordered events therefore give, with no omitted states,
\[
P_A=\frac{aK_2(a,b)+bK_1(a,b)+aK_2(a,c)+cK_1(a,c)}{2(a+b+c)}.
\]
Substituting the edge formulas and simplifying yields
\[
P_A=\frac{a^2[2a^2+a(b+c)+2bc]}{2(a^2+ab+b^2)(a^2+ac+c^2)}.
\]
The finite chain is absorbing almost surely because all fitnesses are positive and every nonabsorbing state has a positive-probability path to a monomorphic state. The first-change conditioning is therefore legitimate.

**3. Exact aggregation and factorization.** For the merged competitor fitness \(m=(b+c)/2\), its two-allele target probability is \(P_{\rm av}=K_1(a,m)=a^2/(a^2+am+m^2)\). Set \(b=m+d\) and \(c=m-d\). Factoring the difference over a common denominator yields
\[
P_A-P_{\rm av}=\frac{a^2d^2[(m-a)(m+2a)-d^2]}{(a^2+a(m+d)+(m+d)^2)(a^2+a(m-d)+(m-d)^2)(a^2+am+m^2)}.
\]
The factors in the denominator are strictly positive for all stated parameters. If \(d\ne0\), the sign is therefore the sign of \((m-a)(m+2a)-d^2\).

**4. Exhaustive parameter classification.** For \(a\ge m\) the term \((m-a)(m+2a)\) is nonpositive, so the sign is strictly negative. If \(0<a\le m/2\), then \((m-a)(m+2a)\ge m^2>d^2\), giving a strictly positive sign. If \(m/2<a<m\), then \(0<(m-a)(m+2a)<m^2\); thus \(|d|=\sqrt{(m-a)(m+2a)}\) lies strictly within the admissible dispersion interval and separates strict positive and negative signs, with equality on the threshold. Finally, \(d=0\) makes the two competitors reproductively identical, giving equality directly.

**5. Exact fixed-mean reversal.** With \(a=2\), \(m=3\), the threshold is \(d^2=7\). The first example has \(|d|=1\), below threshold, and the second has \(|d|=11/4\), above it but less than \(m=3\). Exact substitution gives the two rational differences stated in the theorem. No simulation or continuity extrapolation is used.

## Verification

The included `verify.py` checks the symbolic equality of both closed forms and the variance factorization using SymPy, and **independently** reconstructs the complete three-individual Moran transient transition matrix. A rational Gauss--Jordan solver computes the absorption probability on every transient state for seven rational fitness triples. All samples agree with the closed formula, and the two exact fixed-mean differences are verified. Run `python verify.py` with Python 3 and SymPy available; successful output is `VERIFY_OK`.

The finite rational tests do not prove the formula for arbitrary real fitnesses; that proof is the first-step/edge reduction and algebraic identity above. Nor are these tests a certificate about populations larger than three.

## Relationship to prior work

Yuzbashyan, Feigel and Morozov (2026, arXiv:2610.04090v1) consider multi-allele Wright--Fisher diffusion and benchmark a **Kimura diffusion mean-field** formula based on averaged competitor selection coefficients; the study reports overestimation in its investigated parameter ranges. The theorem here uses a distinct microscopic discrete Moran model and a model-consistent two-type **Moran** approximation, so it neither contradicts their computed diffusion observations nor subsumes their general recursion. It answers the precise sign question in the minimal finite multi-allele setting and shows why a one-sided sign heuristic is not model-universal.

Braga, Wardil and Martinez-Garcia (arXiv:2604.12004v1, Section IV.1, equation (37)) derive the **first-order weak-selection** fixation approximation for constant-fitness multi-allele Moran processes. Their first-order formula depends on mean fitness and contains no exact, finite, arbitrary-fitness signed aggregation-error diagram. The error above is generally at least **third order** in small fitness differences about neutrality, so that earlier first-order result cannot determine its sign.

Ferreira and Neves (arXiv:1811.09552v1, Section 2.3) provide the finite multitype Moran transition equations and general coupling bounds. Their general harmonic system includes this finite process as an instance, but its theorems do not state the explicit competitor-averaging sign classification or the variance-induced reversal at a fixed background mean. The standard two-allele birth--death formula is used rather than claimed as a new result.

Lessard and Lahaie (2009) analyze first-order selection effects in a finite **diploid Wright--Fisher** multiallele model. Rychtář and Taylor (2020) analyze fitness variance **within two genotypes with stochastic reproductive fitness**, not three simultaneously present fixed-fitness genotypes. Their conceptual variance results do not yield the displayed sign identity.

## Limitations

This exact result concerns population size exactly three; it does not establish a corresponding sign law for larger Moran populations, Wright--Fisher models, spatially structured populations, mutation, or time-dependent fitness. The smallest population is a natural minimal testbed, not a realistic large-population prediction. The general model and its finite-state Markov equations are classical; the claimed contribution is only the **complete sharp bias-sign diagram and its fixed-mean variance crossover**. The literature comparison cannot exclude unindexed work or all possible reformulations. Independent external validation has not been performed.

## References

1. E. A. Yuzbashyan, A. Feigel, and A. V. Morozov, *Fluctuation theorems and exact multi-allele fixation probabilities*, arXiv:2610.04090v1, first posted 2 October 2026. https://arxiv.org/html/2610.04090v1
2. I. Braga, L. Wardil, and R. Martinez-Garcia, *Fixation probabilities for multi-allele Moran dynamics with weak selection*, arXiv:2604.12004v1, 13 April 2026. https://arxiv.org/html/2604.12004v1
3. E. M. Ferreira and A. G. M. Neves, *Fixation probabilities for the Moran process with three or more strategies: general and coupling results*, arXiv:1811.09552v1, 23 November 2018. https://arxiv.org/html/1811.09552v1
4. S. Lessard and P. Lahaie, *Fixation probability with multiple alleles and projected average allelic effect on selection*, Theoretical Population Biology 75 (2009), 266--277. https://doi.org/10.1016/j.tpb.2009.01.009
5. J. Rychtář and D. T. Taylor, *Moran process and Wright--Fisher process favor low variability*, Discrete and Continuous Dynamical Systems B 26 (2021), 3491--3504; early access 20 August 2020. https://doi.org/10.3934/dcdsb.2020242
