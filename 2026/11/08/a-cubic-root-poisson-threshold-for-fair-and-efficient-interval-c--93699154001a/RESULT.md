# A cubic-root Poisson threshold for fair and efficient interval committees

## Finding

Let \(m\ge4\) candidates be ordered \(c_1,\ldots,c_m\), with exactly \(m-1\) voters: voter \(i\) approves precisely \(\{c_i,c_{i+1}\}\). For every \(1\le k\le m\), draw a size-\(k\) committee \(W\) uniformly from the \(\binom{m}{k}\) possibilities. Write \(x_j=\mathbf 1_{\{c_j\in W\}}\) and \(t=m-k\).

**Exact finite classification.** A committee is Pareto optimal (PO) if and only if
\[
x_1\le x_2,\qquad x_m\le x_{m-1}.
\]
All three standard proportionality notions JR, PJR and EJR coincide on this profile. For \(\lceil(m-1)/2\rceil\le k\le m-2\), they hold if and only if the binary committee word has **no run of three consecutive zeros**. For all other permitted \(k\), every committee satisfies all three notions.

Define the four states \(\mathcal S=\{00,01,10,11\}\), the initial polynomial row \(u(z)=(1,z,0,z^2)\), and the terminal column \(v=(1,0,1,1)^{\mathsf T}\), in this state order. Put
\[
h_{m,k}=\mathbf 1_{\{\lceil(m-1)/2\rceil\le k\le m-2\}}
\]
and let the transition matrix \(M_h(z)\) have entry \(z^c\) from state \(ab\) to state \(bc\), with \(a,b,c\in\{0,1\}\), except that transition \(00\to00\) is forbidden when \(h=1\); all other entries vanish. Then the **exact number** of size-\(k\) committees simultaneously satisfying PO and EJR (equivalently PO and JR/PJR) is
\[
N_{m,k}=[z^k]\,u(z)M_{h_{m,k}}(z)^{m-2}v.
\]
This is computable by a four-state dynamic program in \(O(mk)\) arithmetic operations. Independently, the number of Pareto-optimal committees is
\[
\binom mk-2\binom{m-2}{k-1}+\binom{m-4}{k-2},
\]
with out-of-range binomial coefficients interpreted as zero.

**Sharp sparse-deficit reliability window.** If \(m\to\infty\), \(1\le k=k(m)\le m\), and \(t/m^{2/3}\to\lambda\in[0,\infty)\), then
\[
\Pr(W\text{ satisfies PO and EJR})\longrightarrow
\exp(-\lambda^3).
\]
If instead \(t/m^{2/3}\to\infty\) while \(t=o(m)\), this probability tends to zero. Thus the transition from high to low simultaneous fairness/efficiency probability occurs at a deficit of order \(m^{2/3}\).

## Assumptions and scope

Voters are distinct, one per adjacent pair; approval utilities count selected approved candidates, and there are no other voters. Committee size is fixed and candidates are labeled by position. Pareto dominance compares every voter's count \(|A_i\cap W|\), requiring weak improvement for all and strict improvement for some. JR uses the standard Hare quota \(n/k=(m-1)/k\). PJR and EJR use the standard \(\ell\)-cohesive-group definitions. The probability statement concerns a uniformly random size-\(k\) committee, not random ballots or an adaptive allocation rule. The asymptotic statements have the quantifiers above and do not cover arbitrary interval profiles.

## Proof

**1. Pareto optimality.** The sum of all voters' approval counts in \(W\) equals
\[
\sum_{i=1}^{m-1}(x_i+x_{i+1})=2k-x_1-x_m.
\]
Any strictly Pareto-improving size-\(k\) committee must decrease the number of elected endpoints. If \(x_1=1\) and \(x_2=0\), swapping \(c_1\) for \(c_2\) preserves voter 1's utility and increases voter 2's, leaving every other voter unaffected. The symmetric claim holds at the right endpoint. Conversely, if \(x_1=x_2=1\), removing \(c_1\) strictly reduces voter 1's approval count, since \(c_2\) is already elected; such a removal cannot be part of any Pareto improvement. The analogous fact holds for \(x_{m-1}=x_m=1\). If neither endpoint can be removed, the total approval sum cannot increase, ruling out strict Pareto dominance. This proves the two local conditions.

For counting PO committees alone, exclude the bad left-end pattern \(10\) and right-end pattern \(01\). Inclusion–exclusion gives the stated three-term formula.

**2. JR and the stronger axioms.** For an unelected candidate \(c_j\), let \(d_j\) be the number of unrepresented voters who approve it. Every voter approving \(c_j\) is one of its at most two adjacent edge-voters, and \(d_j\) is the number of its neighboring candidates that are also unelected. By the definition of JR, a violation occurs exactly when \(d_j\ge(m-1)/k\) for some unelected \(c_j\).

If \((m-1)/k>2\), violation is impossible. If \(1<(m-1)/k\le2\), a violation occurs exactly at a \(000\) substring centered at \(j\). If \((m-1)/k\le1\), then \(k\ge m-1\), so at most one candidate is unelected and no voter is unrepresented. This establishes the precise range and forbidden-run characterization.

Each voter approves two adjacent candidates and the intersection of any two distinct voters' approval sets has size at most one. For \(m\ge4\) and \(k\le m\), every \(\ell\)-cohesive group with \(\ell\ge2\) would have at least two voters (because \(\ell(m-1)/k>1\)) and would need at least two commonly approved candidates. Such groups do not exist. Therefore the \(\ell\ge2\) clauses of PJR and EJR are vacuous, while their \(\ell=1\) clause is exactly JR.

**3. Exact count.** A word satisfying PO must start with one of \(00,01,11\), with respective weights \(1,z,z^2\), and end with one of \(00,10,11\). Appending a bit \(c\) to a pair \(ab\) contributes a factor \(z^c\) and advances the state to \(bc\). When the Hare quota makes JR nonvacuous, the only forbidden local transition is \(00\to00\); otherwise all transitions are permitted. The resulting transfer matrix enumerates each admissible binary committee word once, and coefficient extraction fixes the committee cardinality. Truncating the polynomials at degree \(k\) uses four states over \(m\) steps, taking \(O(mk)\) arithmetic operations.

**4. Poisson window.** Let \(X_m\) count positions \(j=1,\ldots,m-2\) for which \(x_j=x_{j+1}=x_{j+2}=0\). Under the uniform size-\(k\) model, the zero set is a uniformly random \(t\)-subset, so for each fixed set of \(r\) positions the probability that all are zeros is \((t)_r/(m)_r\), where \((a)_r=a(a-1)\cdots(a-r+1)\). In particular,
\[
\mathbb E X_m=(m-2)\frac{(t)_3}{(m)_3}\sim\frac{t^3}{m^2}
\]
when \(t\to\infty\) and \(t=o(m)\).

If \(t/m^{2/3}\to\lambda\in(0,\infty)\), calculate the factorial moments \(\mathbb E(X_m)_r\) by summing over ordered distinct triples. Nonoverlapping triples contribute asymptotically \((t^3/m^2)^r\to\lambda^{3r}\). In any overlapping connected cluster of \(s\ge2\) triples, the cluster specifies at least \(s+2\) zeros and has only \(O(m)\) possible placements, so its contribution is \(O(m(t/m)^{s+2})=o(1)\). Grouping configurations into connected clusters shows all contributions containing an overlap vanish. Thus the factorial moments tend to those of \(\operatorname{Poisson}(\lambda^3)\), proving \(X_m\) converges to that law. If \(\lambda=0\), the expectation tends to zero directly by Markov's inequality.

In both cases \(t=o(m)\), so the probability that either PO endpoint obstruction occurs is at most
\[
2\frac{k\,t}{m(m-1)}\le\frac{2t}{m-1}\longrightarrow0.
\]
For sufficiently large \(m\) with \(t\to\infty\) and \(t=o(m)\), JR/EJR is exactly the event \(X_m=0\). Consequently the joint success probability tends to \(e^{-\lambda^3}\), and the same conclusion \(1\) holds for \(t=o(m^{2/3})\), including bounded \(t\).

If \(t/m^{2/3}\to\infty\) with \(t=o(m)\), then \(\mathbb E X_m\to\infty\). Indicators for disjoint triples are nonpositively correlated under uniform fixed-cardinality sampling. Overlapping pairs number \(O(m)\) and contribute \(O(m(t/m)^4)\), giving
\[
\operatorname{Var}(X_m)\le\mathbb E X_m+O(m(t/m)^4)
=o((\mathbb E X_m)^2).
\]
Chebyshev's inequality implies \(\Pr(X_m=0)\to0\), and joint PO/EJR success is no larger. This proves sharpness.

## Verification

The standalone `VERIFY.py` uses exact integer arithmetic to compare the local PO and JR conditions with literal committee comparisons on all \(2{,}032\) nonempty binary profiles of lengths three through ten. It independently checks EJR versus JR by enumerating cohesive voter groups on all \(498\) nonempty profiles of lengths three through eight. It compares the four-state recurrence against explicit admissible-word enumeration for all \(75\) pairs \((m,k)\) with \(3\le m\le12\) and \(1\le k\le m\). All tests pass. These checks do not establish the asymptotic law; the factorial-moment and variance arguments above do.

Run with Python 3 standard library: `python VERIFY.py`.

## Relationship to prior work

Dong (2026) proves general NP-hardness of jointly computing JR and PO; that result motivates tractable, quantified subclasses but does not count committees or give a random-committee threshold. Schünke (2026) proves Single Dominance Only for Candidate Interval elections, which already implies the present local PO criterion after specialization, and provides a general construction of PO plus a stronger fairness property; those are acknowledged prior results, not claims of novelty here. Bredereck et al. (2019) study random JR/PJR/EJR committees experimentally and establish general counting hardness, but do not give this adjacent-pair fixed-size exact enumeration or the cubic-root success law. Classical Poisson approximations for rare runs (e.g. Godbole, 1991) anticipate the probabilistic ingredient. The contribution is the combined exact electoral characterization, count and critical law for a fixed-cardinality random committee—not a new universal Poisson theorem. Related indexed and accessible research records were also compared; unindexed equivalent derivations remain a possibility.

## Limitations

The theorem is confined to a canonical length-two Candidate Interval profile with one voter per adjacent pair and uniform sampling of committee subsets. It does not characterize arbitrary interval elections, algorithmic complexity on unbounded domains, or EJR+. The Poisson statement is asymptotic, not a finite-sample error bound. Mathematical correctness is supported by a complete analytic proof and finite checks; no independent audit has been conducted.

## References

1. C. Dong, *Jointly Satisfying Pareto Optimality and Justified Representation is NP-Hard in Approval-Based Multiwinner Voting* (first publicly submitted 2026-09-08), https://arxiv.org/abs/2609.08357.
2. J. Schünke, *Pareto Optimality in Approval-Based Multiwinner Voting* (first publicly submitted 2026-05-28), https://arxiv.org/abs/2605.30490.
3. R. Bredereck, P. Faliszewski, A. Kaczmarczyk, R. Niedermeier, *An Experimental View on Committees Providing Justified Representation* (2019), https://doi.org/10.24963/ijcai.2019/16.
4. A. P. Godbole, *Poisson Approximations for Runs and Patterns of Rare Events* (1991), https://doi.org/10.2307/1427680.
