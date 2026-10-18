# Strict all-time coverage-delay ordering for the seven-line Fano design

## Finding

Let \(T_{\mathrm F}\) be the number of independent, uniform line draws from the seven lines of the Fano plane needed to cover all seven points. Let \(T_{\mathrm U}\) be the corresponding number of independent draws when each of the \(\binom{7}{3}=35\) three-point subsets is equally likely. For every integer \(t\geq1\), the exact survival-probability gap is

\[
\Pr(T_{\mathrm F}>t)-\Pr(T_{\mathrm U}>t)
=\frac{21\,5^t-35\,4^t+35}{35^t}.
\]

The two survival probabilities agree at \(t=0,1,2\), while **strict inequality** holds for every integer \(t\geq3\). Thus \(T_{\mathrm F}\) is strictly larger than \(T_{\mathrm U}\) in first-order stochastic order, apart from the unavoidable equal initial tail values. At the first possible completion time,

\[
\Pr(T_{\mathrm F}>3)-\Pr(T_{\mathrm U}>3)=\frac{12}{1225}.
\]

In particular, \(\mathbb E[T_{\mathrm F}]-\mathbb E[T_{\mathrm U}]=7/527\); this last identity recovers the already known expectation comparison, rather than claiming it as a new result.

## Assumptions and scope

The point set is \(V=\mathbb Z/7\mathbb Z\). The Fano lines are the seven translates \(i+\{0,1,3\}\pmod 7\), with \(i\in V\). Every draw selects one entire line, with replacement, uniformly and independently of previous draws. The full model draws uniformly with replacement from every three-element subset of \(V\). Completion is the first **positive** draw count for which the union of selected blocks equals \(V\). The result compares **these two specified mechanisms**, not arbitrary fair mechanisms or larger projective planes.

## Proof

For a family \(\mathcal B\) of \(b\) possible blocks, let \(q(S)=b^{-1}\#\{B\in\mathcal B:B\cap S=\varnothing\}\) for every \(S\subseteq V\). Inclusion-exclusion over the events that a point remains unseen gives, for each integer \(t\geq1\),

\[
\Pr(T\leq t)=\sum_{S\subseteq V}(-1)^{|S|}q(S)^t.
\]

For the Fano lines, every point lies on three lines, every pair of points on exactly one line, and each noncollinear triple has precisely one disjoint line. The only nonzero signed avoidance counts, grouped by \(q(S)\), are \((1,+1)\), \((4/7,-7)\), \((2/7,+21)\), and \((1/7,-21)\). To see the last coefficient, the \(28\) noncollinear three-point sets contribute \(-28\), and the complements of the seven lines contribute \(+7\). All remaining nonempty subsets contribute only to \(q=0\), irrelevant when \(t\geq1\). Hence

\[
\Pr(T_{\mathrm F}>t)
=7\left(\frac47\right)^t-21\left(\frac27\right)^t
 +21\left(\frac17\right)^t.
\]

For the uniform model, the fraction of blocks avoiding a given \(k\)-element set is \(\binom{7-k}{3}/35\), where the binomial coefficient is zero when fewer than three points remain. The nonzero signed groups are \((1,+1)\), \((4/7,-7)\), \((2/7,+21)\), \((4/35,-35)\), and \((1/35,+35)\). Therefore

\[
\Pr(T_{\mathrm U}>t)
=7\left(\frac47\right)^t-21\left(\frac27\right)^t
 +35\left(\frac4{35}\right)^t-35\left(\frac1{35}\right)^t.
\]

Subtracting proves the displayed exact difference. Put \(a_t=(4^t-1)/5^t\). A direct calculation yields

\[
a_1=a_2=\frac35,\qquad
 a_t-a_{t+1}=\frac{4^t-4}{5^{t+1}}>0\quad(t\geq2).
\]

The difference equals \((5/35)^t(21-35a_t)\). It vanishes at \(t=1,2\) and is positive for **every** integer \(t\geq3\), without extrapolation from any finite sample. At \(t=0\), both coverage times are positive, so both survival probabilities are one.

Finally, summing the difference over \(t\geq1\) is justified by geometric convergence and gives

\[
\mathbb E[T_{\mathrm F}]-\mathbb E[T_{\mathrm U}]
=21\frac{1}{6}-35\frac{4}{31}+35\frac{1}{34}
=\frac7{527}.
\]

## Verification

The accompanying standalone `verify.py` uses standard-library exact rational arithmetic to: construct both distinct block families; check each of the \(21\) unordered point pairs lies on exactly one Fano line; independently enumerate all \(128\) absent-point subsets and tally the signed avoidance factors; and compare inclusion-exclusion against a separate exact \(128\)-state covered-subset Markov evolution for every \(0\leq t\leq12\). It confirms the exact gap, the initial equalities, and both expectation values. Run `python3 verify.py` from the directory containing this document. The infinite-horizon inequality is proved by the monotone-ratio argument above, **not** by finite computation.

## Relationship to prior work

Barak-Pelleg and Berend (2026, Theorem 2.1 and Section 3) introduced the Fano example as a counterexample to an **expected** coverage-time maximality conjecture, proving \(\mathbb E[T_{\mathrm F}]=163/30\) and \(\mathbb E[T_{\mathrm U}]=85691/15810\). The present statement upgrades that expectation gap to an explicit **all-horizon stochastic order**. Their Markov stage probabilities determine the Fano law in principle but do not assert or establish the comparison of the entire tails with the full model; proving its sign uniformly in time requires the signed-avoidance cancellation displayed here. Grunbaum and Yaakobi's (2025) general coverage analysis formulates the original expectation-level question, while Berend and Sher's (2025) work concerns other group-drawing expectation comparisons. Neither inspected source provides this exact distributional ordering.

## Limitations

No analogous stochastic ordering is proved here for projective planes of order greater than two, other uniform block families, nonuniform sampling, or non-independent draws. First-order ordering is a statement about marginal completion-time distributions; it does not specify a pathwise coupling of the original drawing processes. The prior-work comparison is a best-knowledge literature assessment, not a proof of absolute uniqueness in all sources. The known expectation difference is not itself a new discovery.

## References

1. D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1, 2026. https://arxiv.org/pdf/2606.28216v1
2. Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1, 2025. https://arxiv.org/html/2510.25305v1
3. D. Berend and T. Sher, *On a Conjecture of Schilling Regarding the Coupon Collector's Problem*, arXiv:2509.17201v1, 2025. https://arxiv.org/html/2509.17201v1
