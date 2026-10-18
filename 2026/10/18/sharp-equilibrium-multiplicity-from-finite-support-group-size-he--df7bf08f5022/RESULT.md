# Sharp equilibrium multiplicity from finite-support group-size heterogeneity in two-volunteer games

## Finding
For every integer \(m\ge1\), consider a quorum-two public-goods game in which the group size experienced by a focal participant has a distribution with exactly \(m\) distinct values, each at least three. If other individuals cooperate independently with population frequency \(x\), the population follows the two-strategy replicator equation specified below. It has **at most \(2m\) interior equilibrium frequencies, counted with multiplicity**. This bound is sharp for every \(m\): there are strictly positive group-size weights and benefit/cost parameters producing exactly \(2m\) *simple* interior equilibria, of which exactly \(m\) are locally asymptotically attracting. Thus a fixed, minimal nontrivial public-goods quorum can coexist with arbitrarily many distinct stable cooperation levels as the support complexity of experienced group size increases.

The construction is explicit. Given \(m\ge1\), choose
\[
L=16m,\qquad R=L^2,\qquad n_j=R^j+1,\qquad w_j=\frac1m\quad(1\le j\le m),\qquad \frac cB=\frac1{4m}.
\]
All group sizes are finite integers, each weight is positive, and the benefit and volunteering cost are strictly positive.

## Assumptions and scope
A well-mixed infinite population uses two pure strategies, \(V\) (volunteer) and \(D\) (decline). A participant encounters group size \(N\) drawn from a fixed, *experienced* distribution \(\mathbb P(N=n_j)=w_j>0\), with \(\sum_jw_j=1\), pairwise distinct integers \(n_j\ge3\), and finite \(m\ge1\). Conditional on group size, each of the \(N-1\) partners independently volunteers with probability \(x\). The focal individual's decision does not change its group-size distribution. If the group contains at least two volunteers, everyone receives benefit \(B>0\); every volunteer independently pays cost \(c>0\). Interactions are one-shot; benefits are not shared proportionally and no assortment, explicit group-formation feedback, or strategy-dependent sampling is assumed.

Let \(\pi_V(x)\) and \(\pi_D(x)\) denote expected payoffs. When the focal player changes from \(D\) to \(V\), the public good's provision changes only if *exactly one* of the other \(n-1\) group members volunteers. Consequently
\[
\pi_V(x)-\pi_D(x)=B G(x)-c,\qquad
G(x)=x\sum_{j=1}^m w_j(n_j-1)(1-x)^{n_j-2}.
\]
The dynamics are \(\dot x=x(1-x)(BG(x)-c)\). The word *equilibrium* in this finding means an interior root \(x\in(0,1)\) of this ordinary differential equation; boundary equilibria are not counted. Multiplicity means the multiplicity of the root in the nonzero polynomial \(BG(x)-c\).

## Proof
**Universal root bound.** Put \(z=1-x\), \(\lambda=c/B>0\), and \(a_j=w_j(n_j-1)>0\). Then
\[
\frac{\pi_V(1-z)-\pi_D(1-z)}{B}
=-\lambda+\sum_{j=1}^m a_j\bigl(z^{n_j-2}-z^{n_j-1}\bigr).
\]
After collecting equal exponents, the polynomial has at most \(2m+1\) nonzero monomials, including the negative constant, because \(n_j\ge3\). Descartes' rule of signs bounds the number of positive real roots, with multiplicities, by at most the number of sign changes among nonzero coefficients, which in turn is at most \(2m\). Every interior equilibrium corresponds bijectively to a positive root \(0<z<1\), so there are at most \(2m\) such equilibria, counted with multiplicity.

**Sharpness.** Fix \(m\) and take the displayed parameters \(L=16m\), \(R=L^2\), \(n_j=R^j+1\), \(w_j=1/m\), and \(\lambda=1/(4m)\). The normalized pivotality function becomes
\[
G(x)=\frac1m\sum_{j=1}^m R^j x(1-x)^{R^j-1}.
\]
At \(x=0\) and \(x=1\), all terms vanish, so \(G(x)-\lambda<0\). Define the distinct sample points
\[
p_i=R^{-i}\quad(1\le i\le m),\qquad
q_i=(LR^i)^{-1}=R^{-i-1/2}\quad(1\le i<m).
\]
They satisfy the strict order \(0<p_m<q_{m-1}<p_{m-1}<\dots<q_1<p_1<1\).

For any integer \(K\ge2\), \(\log(1-1/K)\ge-1/(K-1)\). Indeed, this follows from \(\log(1-u)\ge-u/(1-u)\) for \(0<u<1\), as can be checked by differentiating. Therefore
\[
G(p_i)\ge\frac1m(1-1/R^i)^{R^i-1}
\ge\frac1{em}>\frac1{4m}=\lambda.
\]
We next prove that every \(q_i\) is a strict valley below \(\lambda\). Write \(t_j=R^jq_i\). If \(j\le i\), then \(0<t_j\le1/L\), so
\[
t_j(1-q_i)^{R^j-1}<1/L.
\]
If \(j\ge i+1\), then \(t_j\ge L\). Using \(\log(1-q_i)\le-q_i\), the same summand satisfies
\[
t_j(1-q_i)^{R^j-1}\le e^{q_i}t_j e^{-t_j}
\le e L e^{-L}<1/L.
\]
Here \(t\mapsto te^{-t}\) decreases for \(t\ge1\), \(q_i<1\), and the last inequality holds for all \(L\ge16\), since \(e^{L-1}>L^2\); the latter is true at \(16\) and its logarithmic difference \(L-1-2\log L\) increases for \(L>2\). Averaging the \(m\) summands gives \(G(q_i)<1/L=1/(16m)<\lambda\).

The signs of \(G(x)-\lambda\) therefore alternate along
\[
0,\ p_m,\ q_{m-1},\ p_{m-1},\ldots,\ q_1,\ p_1,\ 1:
\qquad -,\ +,\ -,\ +,\ldots,\ -,\ +,\ -.
\]
There are exactly \(2m\) disjoint open intervals between consecutive points with opposite signs. By continuity each interval contains at least one equilibrium. The universal Descartes bound prevents additional roots and forces all \(2m\) roots to be simple. Since \(x(1-x)>0\) on \((0,1)\), the signs of the vector field match those of \(G-\lambda\). Consecutive roots alternate from repelling (\(-\) to \(+\)) to attracting (\(+\) to \(-\)); hence exactly \(m\) interior roots are attracting. This includes \(m=1\), where no \(q_i\) is needed.

## Verification
For a considerably smaller two-support example (distinct from the all-\(m\) witness), take \(n_1=101\), \(n_2=10001\), \(w_1=w_2=1/2\), and \(c/B=1/8\). The exact gain expression is
\[
\frac{\pi_V(x)-\pi_D(x)}B
=\frac12\left(100x(1-x)^{99}+10000x(1-x)^{9999}\right)-\frac18.
\]
A self-contained Python program, `verify.py`, performs exact rational comparisons at \(x=0,1/10000,1/1000,1/100,1\). The respective signs are \(-,+,-,+,-\). Thus this modest example has at least four distinct interior equilibria, and the proven \(2m=4\) upper bound makes these the only ones. The program checks the stated polynomial support bound for this example and tests the elementary analytic inequalities used in the construction on a finite range of small \(m\); the all-\(m\) conclusion comes from the proof, not from these finite tests.

To reproduce, extract `verify.py` unmodified into a directory and run `python3 verify.py` using Python's standard library. It has no third-party dependencies, does not use floating-point signs, and prints a short success summary. The proofs of Descartes' upper bound and of all-\(m\) sharpness are mathematical, not exhaustive computations.

## Relationship to prior work
Peña's *Group-size diversity in public goods games* (first public 4 November 2011, published 2012) sets out the exogenous group-size replicator framework and treats the threshold-one volunteer's dilemma, but explicitly notes that intermediate thresholds can produce two interior equilibria and merit separate treatment (Discussion). Archetti and Scheuring (2011) analyze fixed-size quorum public-goods games and their coexistence equilibria. Peña and Nöldeke (2016; public preprint 7 October 2015) study stochastic orders of group-size distributions and equilibrium changes when the gain sequence is convex or concave; their Discussion explicitly identifies nontrivial-threshold games as falling outside those curvature classifications. None of the inspected statements supplies the present finite-support root bound or a family with arbitrarily many stable interior states. Brännström and colleagues (2011) study fluctuating size in a *continuous-strategy* snowdrift framework rather than the binary-action quorum-two game.

The payoff formula, replicator formalism, binomial pivotality probability, and Descartes' rule are standard and are not claimed to be discoveries. The asserted contribution is the **sharp support-complexity law** and the **uniform explicit multi-attractor construction** for quorum two.

## Limitations
The result is a mathematical classification for an exogenous, finite, *focal-experienced* group-size distribution. It does not imply that such widely separated group sizes are common in nature; the explicit construction uses rapidly growing group sizes. Actual distributions of groups rather than those experienced by randomly chosen individuals may involve size bias and need to be translated appropriately. It does not cover thresholds other than two, continuous investment, strategy-dependent group formation, finite-population drift, spatial assortment, repeated interactions, or the effect of evolutionary noise on transitions between attraction basins. The claim of novelty is relative to inspected sources and literature searches; it is not a certification of global priority. Full text for one older related fixed-size threshold-game paper was not obtained; equivalent independent treatments could exist.

## References
1. J. Peña, “Group-size diversity in public goods games,” *Evolution* 66 (2012), 623–636. First published online 4 November 2011. DOI: 10.1111/j.1558-5646.2011.01504.x.
2. J. Peña and G. Nöldeke, “Variability in group size and the evolution of collective action,” *Journal of Theoretical Biology* 389 (2016), 72–82. Public preprint 7 October 2015, DOI: 10.1101/021485; journal DOI: 10.1016/j.jtbi.2015.10.023.
3. M. Archetti and I. Scheuring, “Coexistence of cooperation and defection in public goods games,” *Evolution* 65 (2011), 1140–1148. DOI: 10.1111/j.1558-5646.2010.01185.x.
4. Å. Brännström, T. Gross, B. Blasius, and U. Dieckmann, “Consequences of fluctuating group size for the evolution of cooperation,” *Journal of Mathematical Biology* 63 (2011), 263–281. DOI: 10.1007/s00285-010-0367-3.
5. L. A. Bach, T. Helvik, and F. B. Christiansen, “The evolution of n-player cooperation—threshold games and ESS bifurcations,” *Journal of Theoretical Biology* 238 (2006), 426–434. DOI: 10.1016/j.jtbi.2005.06.007 (full text not inspected).
