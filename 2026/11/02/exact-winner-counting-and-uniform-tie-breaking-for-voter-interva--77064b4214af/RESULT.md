# Exact winner counting and uniform tie-breaking for voter-interval Chamberlin–Courant

## Finding

For any voter-interval approval election with \(n\ge 1\) voters, \(m\ge 0\) individually labeled candidates, a prescribed committee size \(0\le k\le m\), and arbitrary nonnegative rational voter weights, the number of *all* maximum-weight coverage committees of size exactly \(k\) can be computed exactly with a polynomial number of rational/integer-arithmetic operations. More precisely, \(O(m^3+m^2 k^2+n+m^2)\) operations suffice, with \(O(m)\)-bit counts. An exactly uniform winning committee can be sampled in expected polynomial time using unbiased random bits. Duplicate approval intervals, empty-approval candidates, zero voter weights, and redundant winners are included, without genericity or uniqueness assumptions.

The unweighted version is precisely the approval-based Chamberlin–Courant rule. The counting result is not a statement about arbitrary Thiele scoring rules such as proportional approval voting.

## Assumptions and scope

A known ordering of voters is \(1,\ldots,n\). The support of each candidate is either empty or a closed integer interval \(I_c=[\ell_c,r_c]\) of voters. Candidates with identical supports are *different labeled candidates*. A committee \(W\) has exactly \(k\) candidates and is scored by
\[
 S(W)=\sum_{v=1}^{n} w_v\,\mathbf 1\{v\in \bigcup_{c\in W}I_c\},\qquad w_v\in\mathbb Q_{\ge0}.
\]
Empty supports contribute no coverage, but such candidates may belong to an optimal committee of the required size. All chosen committee subsets, not merely distinct unions or distinct score vectors, are counted.

Group nonempty candidates by their distinct support types \(I_1,\ldots,I_T\), each with labeled multiplicity \(a_i\). Order these types by increasing right endpoint, breaking ties by left endpoint. The ordered sequence of **inclusion-maximal support types present in a committee** has the form \(i_1,\ldots,i_s\) with both endpoints strictly increasing. Set \(I_0=\varnothing\) as a dummy predecessor and put \(r_0=0\).

For a permissible transition \(p\to c\), meaning \(p=0\) or \(\ell_p<\ell_c\) and \(r_p<r_c\), define
\[
 H_{pc}=\sum_{\substack{d\ne c:\ I_d\subsetneq I_c,\\ I_d\nsubseteq I_p}}a_d,
 \qquad
 g_{pc}=\sum_{v=\max\{\ell_c,r_p+1\}}^{r_c}w_v,
\]
where the sum is zero if its lower index exceeds its upper index and \(I_d\nsubseteq I_0\) for nonempty \(I_d\). Define
\[
 B_{pc}(t)=\binom{H_{pc}+a_c}{t}-\binom{H_{pc}}{t},\qquad t\ge1.
\]
Use the conventional value zero for binomial coefficients outside their range. The factor \(B_{pc}(t)\) counts the ways to select exactly \(t\) candidates from the copies of type \(c\) and the \(H_{pc}\) eligible subordinate candidates, *with at least one copy of type \(c\)*.

## Proof

**Unique maximal-support decomposition.** Every nonempty selected support is contained in an inclusion-maximal selected support. After grouping equal support types, these maximal types are pairwise incomparable; interval incomparability forces their left and right endpoints to increase strictly together, giving a unique ordered path. Assign every other selected nonempty candidate to the **first** selected maximal type that contains its interval. For consecutive maxima \(p,c\), a strict subinterval \(I_d\subsetneq I_c\) has first owner \(c\) if and only if \(I_d\nsubseteq I_p\). Indeed, if an earlier maximum \(q\) contained \(I_d\), the endpoint order gives \(\ell_p<\ell_c\le\ell_d\) and \(r_d\le r_q<r_p\); therefore \(I_d\subseteq I_p\). Conversely, containment in the immediately preceding maximum precludes first ownership by \(c\). Thus precisely the \(H_{pc}\) labeled subordinate candidates can be chosen at transition \(p\to c\). A nonempty selection of the copies of type \(c\) is necessary and sufficient for \(c\) to be a maximal type. No chosen subordinate can introduce an additional maximal type. This proves a bijection between committees without empty supports and paths decorated by locally selected labeled candidate subsets counted by \(B_{pc}(t)\).

**Coverage score decomposition.** At a transition \(p\to c\), all previous maximal supports end no later than \(r_p\). If \(\ell_c\le r_p\), the immediately preceding maximal interval already covers all positions from \(\ell_c\) through \(r_p\); if \(\ell_c>r_p\), the entire new interval is uncovered. Therefore the incremental weighted coverage is exactly \(g_{pc}\). Subordinate supports are included in maximal supports and add no score. The total score telescopes as the sum of transition gains.

**Max-plus counting recurrence.** For the dummy state use score \(F(0,0)=0\) and count \(N(0,0)=1\), with all other dummy cardinalities unavailable. For each nonempty type \(c\) and cardinality \(j\), consider every earlier compatible predecessor \(p\) and every integer \(1\le t\le j\) with \(B_{pc}(t)>0\). Each predecessor state contributes the score
\[
 F(p,j-t)+g_{pc}
\]
and multiplicity \(N(p,j-t)B_{pc}(t)\). Let \(F(c,j)\) be the maximum contributed score, and let \(N(c,j)\) be the sum of contributed multiplicities *only over transitions attaining this maximum*. This is exact by induction on the ordered maximal types: future score increments and available subordinates depend only on the immediately previous maximum and committee cardinality. The unique decomposition prevents double counting.

If there are \(z\) empty-support candidates, choose \(e\) of them in \(\binom ze\) ways, and consider every final maximal type with \(j=k-e\), together with the entirely empty path (available only when \(e=k\)). Take the maximum score across these terminal choices, summing \(\binom zeN(c,k-e)\) only for score-maximizing terminals. This yields exactly the number of winning committees of size \(k\). Cases \(k=0\), \(m=0\), all-zero voter weights and all-empty approvals follow from the same terminal rule.

**Complexity and exact sampling.** At most \(m\) types and \(O(m^2)\) compatible transitions exist. Computing subordinate pools naively takes \(O(m^3)\) operations; the cardinality transitions take \(O(m^2k^2)\). Prefix sums calculate coverage gains in constant time per transition after \(O(n)\) preprocessing. All winner counts are at most \(\binom mk\le2^m\), so they have \(O(m)\) bits. Rational-score arithmetic has polynomial bit complexity in the input bit length. To sample a winner, select a maximizing terminal state with probability proportional to its exact contribution count, then select each maximizing predecessor transition in proportion to \(N(p,j-t)B_{pc}(t)\), and finally sample a uniformly random \(t\)-subset of that transition's eligible labels conditional on including at least one type-\(c\) label. Select the prescribed number of empty-support labels uniformly. Each committee is reached with exactly the reciprocal of the total winner count, by the same bijection. Sampling exact finite integer choices by rejection from unbiased random bits uses expected polynomial time.

## Verification

The standalone file `verify.py` implements the recurrence, an independent brute-force evaluator over labeled committees, and the exact weighted-backtracking sampler. Executing `python verify.py` produced:

```
PASS: 1167656 exhaustive profile-size cases; 5000 seeded weighted cases; 7000 valid exact-choice samples; illustrative optimum 9, winner count 7.
```

The exhaustive campaign uses all labeled ordered profiles of up to five interval/empty candidates on each voter line of size one through four and every permissible committee size. The independently generated random campaign additionally includes nonnegative voter weights, duplicate intervals and empty supports. The sampler test checks every sampled committee against the seven actual optimum subsets; finite samples are not a proof of uniformity. The analytical bijection and recurrence prove the universal statement.

For example, take five voter positions with weights \((1,2,1,3,2)\) and six distinct candidate labels having supports \([1,4]\), \([2,3]\), \([3,5]\), \([3,5]\), \([4,4]\), and \(\varnothing\). For \(k=3\), the optimum weighted coverage score is \(9\), attained by exactly \(7\) labeled committees. The nested, duplicated and empty supports genuinely contribute to the winner count.

## Relationship to prior work

Cohen and Gonen (2019) give a polynomial algorithm for *finding an optimal maximum-weight union of given intervals*, eliminating contained intervals in their optimization preprocessing. Their objective coincides with this coverage score, but the elimination loses valid tied committees containing nested or duplicated labels. Their displayed state returns an optimal solution, not the complete count of all labeled optimal fixed-cardinality solutions or an exact sampler.

Janeczko and Faliszewski (2023) introduce the exact number of tied winning committees as a distinct computational problem, show general hardness for Chamberlin–Courant and other rules, and explicitly motivate fair random selection from tied winners. Their interval experiment is empirical, not an interval-domain counting theorem.

Manurangsi and Sornat (2026) and Avramidis et al. (2026) establish polynomial-time winner **determination** for generalized Thiele rules on voter-interval or broader domains; those results do not imply exact counting, and their inspected algorithms do not establish this enumeration. Li et al. (2020) likewise describe a different optimal offline interval-coverage dynamic program without a labeled-optimum counting rule. The contribution here is an explicit canonical maximal-support decomposition, a multiplicity-correct recurrence, and exact uniform reconstruction specifically for weighted approval Chamberlin–Courant on the voter-interval domain.

## Limitations

This theorem counts winning committees only for the binary coverage/approval Chamberlin–Courant objective, not arbitrary concave Thiele rules. It requires a voter ordering certifying the interval property and additive nonnegative rational weights; it does not address circular-arc profiles, arbitrary approval matrices, negative weights, or sampling with nonuniform desired tie-breaking weights. The stated polynomial bound counts integer/rational arithmetic operations; exact rational operation bit costs remain polynomial but are not bounded by the same unit-cost expression. Uniformity is proved for ideal unbiased random bits, not for finite pseudo-random experiments. Priority risk remains that an equivalent optimum-counting recurrence may appear in unindexed interval-optimization or exact-counting literature. No independent audit is claimed.

## References

1. R. Cohen and M. Gonen, *On Interval and Circular-Arc Covering Problems*, Annals of Operations Research 275 (2019), 281–295. https://doi.org/10.1007/s10479-018-3025-6. Author manuscript: https://u.math.biu.ac.il/~cohenr5/publications/interval.pdf
2. Ł. Janeczko and P. Faliszewski, *Ties in Multiwinner Approval Voting* (2023). https://comsoc-community.org/archive/comsoc-2023/comsoc/papers/paper29.pdf
3. P. Manurangsi and K. Sornat, *Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences*, arXiv:2604.05953, first public 2026-04-07. https://arxiv.org/abs/2604.05953
4. D. Avramidis, A. Lassota, U. Schmidt-Kraepelin, and A. Vetta, *Computing Thiele Rules on Interval Elections and their Generalizations*, arXiv:2605.03067 (2026). https://arxiv.org/abs/2605.03067
5. S. Li, M. Li, L. Duan, and V. C. S. Lee, *Online Maximum k-Interval Coverage Problem*, arXiv:2011.10938 (2020). https://arxiv.org/abs/2011.10938
