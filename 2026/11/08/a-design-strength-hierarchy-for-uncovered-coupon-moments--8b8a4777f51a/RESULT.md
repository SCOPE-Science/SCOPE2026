# A design-strength hierarchy for uncovered-coupon moments

## Finding
Let \(V\) be a set of size \(v\), and let every independent draw be a \(k\)-element subset with an arbitrary common law \(\mu\), where \(1\le k<v\). After \(t\) draws let \(U_t\) count the elements of \(V\) never drawn. Write \((z)_r=z(z-1)\cdots(z-r+1)\) and let \(U_t^{\rm full}\) denote the same count under uniform draws from all \(k\)-subsets.

**Moment-and-design theorem.** For all integers \(t\ge2\) and \(1\le r\le\min(k,v-k)\),
\[
\mathbb E_\mu (U_t)_r\;\ge\; \mathbb E_{\rm full}(U_t^{\rm full})_r
=(v)_r\left(\frac{\binom{v-r}{k}}{\binom vk}\right)^t.
\]
Equality holds if and only if \(\mu\) is a weighted \(r\)-design: for every \(j\) with \(1\le j\le r\), and every \(j\)-set \(J\subset V\),
\[
\Pr_\mu(J\subseteq B)=\frac{\binom{k}{j}}{\binom vj}.
\]
Consequently, for a weighted design of maximal strength \(s<\min(k,v-k)\), the uncovered factorial moments of ranks \(1,\dots,s\) agree with those of the full model at *every* draw count, while rank \(s+1\) strictly exceeds the full-model value at *every* \(t\ge2\). This is a moment-detection characterization, not an ordering of completion times.

**Projective-plane signature.** In any existing finite projective plane of order \(q\ge2\) (not necessarily Desarguesian), sample its lines independently and uniformly, so \(v=q^2+q+1\), \(k=q+1\). For every \(t\ge0\), its uncovered count \(U_t^{\rm PG}\) and the full model have equal first and second factorial moments, hence the same mean and variance. For every integer \(t\ge2\), their third factorial moments differ strictly. With
\[
 f=\frac{q-1}{v-2},\quad a_1=\frac{(q-1)^2-1}{v},\quad a_0=\frac{(q-1)^2}{v},\quad
 a_*= f a_1+(1-f)a_0=\frac{\binom{v-3}{k}}{\binom vk},
\]
that difference is exactly
\[
 \mathbb E(U_t^{\rm PG})_3-\mathbb E(U_t^{\rm full})_3
 =(v)_3\bigl[f a_1^t+(1-f)a_0^t-a_*^t\bigr]>0.
\]
At two draws the exact gap simplifies for every existing order \(q\) to
\[
 \boxed{\;\mathbb E(U_2^{\rm PG})_3-\mathbb E(U_2^{\rm full})_3
 =\frac{q^3(q^2-1)}{(q^2+q+1)(q^2+q-1)}\;}.
\]
For \(q=2,3,5\), respectively, the gap is \(24/35\), \(216/143\), \(3000/899\). These examples are finite checks; the statement for all existing orders follows from the incidence axioms, not extrapolation.

## Assumptions and scope
Every block has the same cardinality \(k\); the draws are independent and identically distributed over the \(k\)-sets. The law may be nonuniform and have zero probabilities. The equality-to-design criterion uses \(r\le\min(k,v-k)\), and moment domination itself holds for all \(1\le r\le v\), with the natural zero convention when \(r>v-k\). No assumptions of fairness or transitivity are needed for the inequality. The term weighted \(r\)-design includes nonuniform probability weights on a family of blocks. A projective plane means an incidence structure of order \(q\) in which each pair of distinct points lies on a unique line and each line contains \(q+1\) points; existence is not assumed for any unsupported \(q\).

## Proof
**1. Exact factorial-moment formula.** For any fixed \(r\)-set \(S\subset V\), put \(a_S=\Pr_\mu(B\cap S=\varnothing)\). The probability that all \(r\) points of \(S\) are unseen after \(t\) independent rounds equals \(a_S^t\). Counting ordered distinct unseen \(r\)-tuples therefore gives
\[
 \mathbb E_\mu(U_t)_r =r!\sum_{|S|=r}a_S^t
 =(v)_r\,\mathbb E_{S\sim\mathrm{Unif}\binom Vr}[a_S^t].
\]
For every deterministic \(k\)-set \(B\), exactly \(\binom{v-k}{r}\) of the \(r\)-sets \(S\) avoid \(B\). Hence, regardless of \(\mu\),
\[
 \mathbb E_S a_S=\frac{\binom{v-k}{r}}{\binom vr}
 =\frac{\binom{v-r}{k}}{\binom vk}=:a_*.
\]
Strict convexity of \(u\mapsto u^t\) on \([0,1]\) for each real \(t>1\) gives \(\mathbb E_Sa_S^t\ge a_*^t\). Equality occurs exactly when \(a_S=a_*\) for every \(r\)-set \(S\). At \(t=1\), equality always holds and no balance conclusion can be drawn. In particular, at \(t=2\) the exact excess is \((v)_r\operatorname{Var}_S(a_S)\).

**2. Equality characterizes design strength.** Assume \(r\le v-k\). Put \(C=V\setminus B\), a random \((v-k)\)-set. Then \(a_S=\Pr(S\subseteq C)\). Suppose all \(r\)-set avoidance probabilities equal \(a_*\). For any fixed \(j\)-subset \(J\), \(0\le j\le r\), double-count the pairs \((S,C)\) with \(J\subseteq S\subseteq C\) and \(|S|=r\):
\[
 \binom{v-k-j}{r-j}\Pr(J\subseteq C)
 = \sum_{\substack{S\supseteq J\\|S|=r}} a_S
 =\binom{v-j}{r-j}a_*.
\]
The leading binomial coefficient is nonzero. Simplification yields \(\Pr(J\subseteq C)=\binom{v-k}{j}/\binom vj\), a number independent of \(J\). Inclusion–exclusion for membership in \(B=V\setminus C\) now yields
\[
 \Pr(J\subseteq B)=\sum_{H\subseteq J}(-1)^{|H|}\Pr(H\subseteq C)
 =\frac{\binom{k}{j}}{\binom vj}.
\]
Thus \(\mu\) has strength \(r\). Conversely, if all inclusion probabilities through rank \(r\) have the displayed uniform values, inclusion–exclusion gives
\(a_S=\sum_{J\subseteq S}(-1)^{|J|}\Pr(J\subseteq B)=a_*\)
for every \(r\)-set \(S\), so equality holds. This establishes both directions and the first-separation assertion.

**3. Projective plane.** Every line contains \(q+1\) points, every point lies on \(q+1\) lines, and each pair of points lies on exactly one line. Consequently the uniform line law is a weighted \(2\)-design, and ranks one and two match the full mechanism for all \(t\). For any three distinct points \(S\), inclusion–exclusion counts the lines meeting \(S\): the number is \(3(q+1)-3+I_S=3q+I_S\), where \(I_S=1\) if the three points are collinear and \(0\) otherwise. Since the plane has \(v\) lines, its avoidance probability \(a_S\) equals \(a_1\) for a collinear triple and \(a_0\) otherwise. Each line contains \(\binom{q+1}{3}\) triples, no triple is on two lines, so the collinear fraction is
\[
 f=\frac{v\binom{q+1}{3}}{\binom v3}=\frac{q-1}{v-2}\in(0,1).
\]
As \(a_1=a_0-1/v\), strict Jensen yields the displayed positive third-moment gap for every \(t\ge2\). At \(t=2\), the difference reduces to \((v)_3f(1-f)/v^2\), and straightforward cancellation yields the stated rational formula. Hence the projective-plane line mechanism has exactly strength two in the permitted range and cannot match the third factorial moment for \(t\ge2\). This holds for every finite projective plane satisfying the axioms.

## Verification
A standalone Python standard-library script, `verify.py`, performs exact rational arithmetic. It constructs projective planes over prime fields of orders \(2,3,5\), evaluates avoidance frequencies over all \(r\)-subsets, and independently enumerates full two- and three-draw outcomes at orders \(2,3\). It also checks the generic inequality and equality/design criterion over multiple deterministic, uniform, cyclic, and biased probability laws on small sets. The script reports 702 successful finite checks. Those tests do not prove the all-order theorem: the proof above uses exact combinatorial identities and strict convexity.

## Relationship to prior work
Barak-Pelleg and Berend (2026) compare *expected completion times* for fair subset-sampling mechanisms and projective planes, proving strict expected-time comparisons for orders \(2,3,4\). Grunbaum and Yaakobi (2025) derive recovery-set formulas and coverage-time bounds; Berend and Sher (2025) study expected-time optimization under nonuniform group draws. These works provide the coverage setting and demonstrate that expected completion time can behave differently from simple moment orderings. The present statement concerns the fixed-time *uncovered-count factorial moments*, their exact equality/design criterion, and their first discrepancy for every existing projective-plane order; it does not modify the earlier completion-time results. The general identities use classical inclusion–exclusion, Jensen's inequality, and standard finite design incidence identities, which are not claimed new in isolation.

## Limitations
Factorial-moment inequalities do not imply stochastic domination, inequalities for the probability of complete coverage, or an ordering of expected completion times. The explicit projective-plane formula requires a projective plane to exist; it does not establish existence for arbitrary integer orders. The higher-order moment hierarchy is proved for independent fixed-size draws, not variable-size or dependent batches. Historical priority for an equivalent general statement in the older design/coverage literature has not been independently certified.

## References
1. D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216, first public version June 26, 2026, https://arxiv.org/abs/2606.28216 .
2. Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305, first public version October 29, 2025, https://arxiv.org/abs/2510.25305 .
3. D. Berend and T. Sher, *On a Conjecture of Schilling Regarding the Coupon Collector's Problem*, arXiv:2509.17201, first public version September 21, 2025, https://arxiv.org/abs/2509.17201 .
