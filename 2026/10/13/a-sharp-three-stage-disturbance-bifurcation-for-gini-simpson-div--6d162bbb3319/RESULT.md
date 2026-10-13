# A sharp three-stage disturbance bifurcation for Gini–Simpson diversity

## Finding

Consider succession through pioneer, intermediate, and climax stages, with exponential pioneer-to-intermediate transition rate \(a>0\), intermediate-to-climax rate \(b>0\), and independent disturbance resetting an occupied patch to pioneer at rate \(c>0\). Let \(\pi_i\) be the stationary fraction of patches in stage \(i\), and measure diversity of *stages* by the Gini–Simpson index \(D=1-\sum_{i=1}^3\pi_i^2\). Define \(r=b/a\) and \(x=c/a\).

Let \(r_*\) be the **unique positive root** of
\[
P(r)=27r^7+135r^6+540r^5-594r^4+918r^3-252r^2+27r-1.
\]
Then \(r_*=0.0817033790460167\ldots\). The disturbance–diversity curve \(x\mapsto D(x;r)\) has **exactly two strict local maxima separated by a strict local minimum** if and only if \(0<r<r_*\). At \(r=r_*\) there is one strict local maximum and one stationary horizontal-inflection point at a larger disturbance rate; at \(r>r_*\) there is exactly one stationary point, a strict maximum.

For **every** \(r>0\), the global maximizing disturbance rate is unique. It always lies at \(0<x<\sqrt r\). When there are two local peaks, the peak at the *smaller* disturbance rate is strictly higher than the second peak. Equivalently, two peaks occur precisely when the **disturbance-free** mean intermediate-to-climax waiting time \(1/b\) exceeds \(1/r_*=12.239395869\ldots\) times the disturbance-free pioneer-to-intermediate waiting time \(1/a\); the apparent upper-disturbance alternative is never globally optimal in this model. These intrinsic waiting times are not the actual holding times when disturbance resets are active.

The three-stage mechanism is minimal: a two-stage exponential progression with the same resets produces a unimodal Gini–Simpson curve for every positive transition rate.

## Assumptions and scope

An individual patch is a continuous-time Markov chain on \(\{1,2,3\}\). The nontrivial transitions are \(1\to2\) at rate \(a\), \(2\to3\) at rate \(b\), and \(2\to1\), \(3\to1\) at rate \(c\). Disturbances at stage 1 return to the same state and do not change its generator. All rates are strictly positive and constant; stage 3 is terminal until a disturbance. A homogeneous landscape's stationary stage fractions equal this chain's stationary probabilities. No finite-sample expectation of a diversity estimator is asserted. Diversity refers to these three successional-stage fractions, not necessarily to actual species richness within stages.

## Proof

**Stationary distribution.** Stationary flow balance gives \(a\pi_1=(b+c)\pi_2\), \(b\pi_2=c\pi_3\), and \(\sum_i\pi_i=1\). Consequently
\[
(\pi_1,\pi_2,\pi_3)=
\left(\frac{x}{1+x},\frac{x}{(1+x)(r+x)},\frac{r}{(1+x)(r+x)}\right).
\]
Direct substitution yields
\[
D(x;r)=\frac{2x\bigl((x+r)^2+r\bigr)}{(x+r)^2(1+x)^2},\qquad x,r>0.
\]
In particular \(D\to0\) as \(x\to0^+\) or \(x\to\infty\). Differentiating gives
\[
\frac{\partial D}{\partial x}=
-\frac{2F_r(x)}{(x+r)^3(1+x)^3},
\quad
F_r(x)=x^4+(3r-1)x^3+3r^2x^2+r(r-1)^2x-r^2(r+1).
\]
Thus positive roots of the quartic \(F_r\) are precisely the stationary disturbance rates.

**A unique algebraic bifurcation.** The discriminant of the monic quartic is
\[
\operatorname{disc}_x(F_r)=-4r^3P(r).
\]
Here is an exact uniqueness certificate for the positive zero of \(P\). For \(0<r<1/10\), substitute \(r=t/[10(1+t)]\). The coefficients of \((1+t)^7P(t/[10(1+t)])\), in *descending* powers of \(t\), are
\[
\frac{441377}{10000000},\ \frac{20947}{200000},\ -\frac{228}{625},\ -\frac{12937}{5000},\ -\frac{3091}{500},\ -\frac{183}{25},\ -\frac{43}{10},\ -1.
\]
They have exactly one sign change; Descartes' rule gives at most one zero in that interval. Since \(P(0)=-1\) and \(P(1/10)=441377/10000000>0\), there is exactly one.

For \(1/10\le r\le1/5\), write \(r=(1+u)/10\), \(0\le u\le1\), and use the Bernstein expansion
\[
P((1+u)/10)=\sum_{k=0}^7\binom7k B_k u^k(1-u)^{7-k}.
\]
The eight \(B_k\), in increasing order, are
\[
\left(
\frac{441377}{10000000},\frac{641491}{8750000},
\frac{248327}{2500000},\frac{156683}{1093750},
\frac{985589}{4375000},\frac{399257}{1093750},
\frac{318232}{546875},\frac{69952}{78125}
\right).
\]
Every coefficient is strictly positive. For \(r\ge1/5\), the expansion of \(P(v+1/5)\) in powers of \(v\ge0\) has ascending coefficients
\[
\frac{69952}{78125},\ \frac{342864}{15625},\ \frac{633942}{3125},\
\frac{85239}{125},\ \frac{864}{25},\ \frac{18117}{25},\
\frac{864}{5},\ 27,
\]
all strictly positive. Thus \(r_*\) is the only positive discriminant zero.

**Count and character of stationary points.** At \(r=1/100\), the signs of \(F_r\) at \(x=0,1/50,1/5,1\) alternate \(-,+,-,+\); therefore three distinct positive roots exist. At \(r=1\), the quartic is \(x^4+2x^3+3x^2-2\), which has exactly one positive root by Descartes' rule. For \(r>0\), \(F_r(0)=-r^2(r+1)<0\) and the leading coefficient stays one. Simple roots cannot cross zero or escape to infinity at finite positive \(r\). Root counts can change only where the discriminant vanishes. Hence there are exactly three distinct positive roots for \(r<r_*\), and one for \(r>r_*\). The derivative sign alternation makes them maximum–minimum–maximum in increasing order in the first regime, and a maximum in the second.

At \(r=r_*\), the two disappearing positive roots form a double root. A triple root would force a repeated root of \(F_r'\); its cubic discriminant is \(-108r(5r^4+51r^3-50r^2+15r-1)\). The degree-seven polynomial \(P\) and the displayed quartic factor are coprime over the rationals (Euclidean-algorithm certificate in the accompanying checker). Thus no triple root occurs. The remaining positive root is simple, giving one strict maximum plus one stationary horizontal inflection.

**Which peak is truly optimal?** For all \(x,r>0\), direct algebra gives the exact reflection identity
\[
D(r/x;r)-D(x;r)=
\frac{2rx(x^2-r)}{(r+x)^2(1+x)^2}.
\]
Whenever \(x>\sqrt r\), the reflected rate \(r/x<\sqrt r\) has strictly *greater* diversity. Furthermore
\[
F_r(\sqrt r)=r^{5/2}(1+\sqrt r)^2>0.
\]
So no stationary root can cross the separating point \(\sqrt r\). At \(r=1/100\) exactly the first positive root lies below \(\sqrt r\) (the displayed sign intervals and \(F_r(\sqrt r)>0\) show this), and at \(r=1\) the sole positive root is below \(\sqrt r\). Continuity through the unique discriminant event proves that for every \(r>0\) there is exactly one stationary point below \(\sqrt r\), the first local maximum. Since all rates above \(\sqrt r\) are strictly dominated by a reflected rate below it, this first maximum is the **unique global maximizer**.

**Minimality.** With just two successional stages and one forward rate \(a>0\), stationary proportions are \((c/(a+c),a/(a+c))\). Their Gini–Simpson diversity is \(2ac/(a+c)^2\), increasing up to \(c=a\) and decreasing afterwards. Hence no two-stage instance can have two local peaks.

## Verification

The standard-library-only file `verify.py` checks the discriminant identity at nineteen distinct exact rational rates; the degree bound of eighteen makes this an identity certificate. It verifies the exact Descartes and Bernstein coefficients, the all-positive translated coefficients, the coprimality needed to rule out triple roots, the rational sign witnesses at \(r=1/100\), and the stationary and reflection identities on independent exact rational grids. The proof above, not a finite numeric sweep, establishes the statements for every positive real parameter.

To reproduce: run `python verify.py` in a directory containing this report and the script. No network or third-party Python dependency is required.

## Relationship to prior work

Johst and Huth (2005) established that successional-stage diversity–disturbance curves can have two maxima and identified long-lived intermediate stages as a mechanism. Their fully available article describes Markovian and age-structured transitions, illustrates four- and ten-stage examples, and notes qualitatively that analogous conclusions apply to Simpson's index. That qualitative bimodality and the Markovian stage framework are **prior work**. The present exact claim concerns the sharp three-stage Gini–Simpson boundary, its explicit algebraic polynomial, and the strict dominance of the lower-disturbance local maximum—none of which was located as an explicit theorem in the inspected article. The older Horn model motivates Markovian ecological succession; Cadotte (2007) addresses ecological diversity–disturbance effects across spatial scales through a different experimental trade-off mechanism.

## Limitations

The exact constant is model- and index-specific. The theorem does not give the analogous critical ratio for Shannon entropy, deterministic age transitions, more stages, stage-dependent disturbance, correlations between landscape patches, within-stage species diversity, or finite-sample observations. No empirical recommendation about a particular ecosystem is inferred. An equivalent algebraic criterion might exist in earlier literature indexed under another name; literature inspection and mathematical derivation are not independent external novelty certification.

## References

1. K. Johst and A. Huth, “Testing the intermediate disturbance hypothesis: when will there be two peaks of diversity?”, *Diversity and Distributions* 11 (2005), 111–120. First publicly posted January 14, 2005. DOI: 10.1111/j.1366-9516.2005.00133.x.
2. H. S. Horn, “Markovian properties of forest succession,” in *Ecology and Evolution of Communities* (1975), 196–211.
3. M. W. Cadotte, “Competition–colonization trade-offs and disturbance effects at multiple scales,” *Ecology* 88 (2007), 823–829. DOI: 10.1890/06-1117.
