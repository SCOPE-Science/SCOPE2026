# A sharp quota-arithmetic threshold for welfare-maximal justified representation under two approvals

## Finding

Let \(n\ge 1\) voters approve nonempty sets of at most two candidates each, and let a committee select exactly three candidates from any finite set of at least three candidates. Put \(q=\lceil n/3\rceil\). **Every** election on \(n\) voters in this class has at least one committee simultaneously maximizing the total number of approvals received by winners and satisfying justified representation (JR) **if and only if**
\[
2n<5\lceil n/3\rceil+3.
\]
If the reverse weak inequality holds, a four-candidate election with a *unique* welfare-maximizing committee that violates JR exists. In particular, failure first occurs at \(n=9\), disappears again at \(n=10,11\), recurs at \(n=12\), and is unavoidable as a possible obstruction for every \(n\ge17\). The set of failing population sizes is exactly: multiples of three at least nine, numbers congruent to two modulo three at least fourteen, and numbers congruent to one modulo three at least nineteen.

The obstruction needs both three seats and two permissible approvals: with two seats, ballot size at most two never forces a conflict, and with any committee size and singleton approval ballots a welfare-optimal JR committee always exists. These auxiliary assertions are part of the result.

## Assumptions and scope

An approval election consists of \(n\) labeled voters, a finite candidate set \(C\) of cardinality \(m\ge3\), and ballots \(A_i\subseteq C\) with \(1\le |A_i|\le2\). A committee \(W\subseteq C\) has size three. Define candidate approval score \(s(c)=|\{i:c\in A_i\}|\), social welfare \(\operatorname{sw}(W)=\sum_{c\in W}s(c)=\sum_i|A_i\cap W|\), and coverage \(\operatorname{cov}(W)=|\{i:A_i\cap W\ne\varnothing\}|\). The welfare maximizers are precisely the size-three subsets of maximum total candidate score.

JR means that no set of at least \(n/3\) voters sharing an approved candidate is entirely unrepresented by \(W\). Equivalently, for every \(x\notin W\), fewer than \(q=\lceil n/3\rceil\) voters both approve \(x\) and have \(A_i\cap W=\varnothing\). This equivalent formulation is used throughout.

The theorem is a **population-wise uniform guarantee**, not a test asserting that each individual profile is compatible exactly when the population inequality holds: in the failing region both compatible and incompatible elections can occur.

## Proof

**Sufficiency.** Fix a population with \(2n<5q+3\). Among welfare-maximizing size-three committees, take \(W=\{a,b,c\}\) with maximum coverage. Suppose JR fails. Then some unselected \(x\) has at least \(q\) approving voters who approve no member of \(W\). Since \(W\) is score-optimal, each member of \(W\) has score at least \(s(x)\ge q\). The at least \(q\) unrepresented voters cannot contribute to the three selected scores, while any other voter contributes at most two. Hence
\[
s(a)+s(b)+s(c)\le2(n-q)<3(q+1).
\]
At least one selected candidate, call it \(c\), therefore has \(s(c)\le q\), and the score ordering forces \(s(c)=s(x)=q\).

Replace \(c\) by \(x\). Welfare remains optimal. The replacement gains representation for at least \(q\) previously unrepresented voters; the only possibly lost voters are those whose *sole* approved winner was \(c\). There are at most \(s(c)=q\) of those. Maximality of the coverage of \(W\) forces exact equality: there are exactly \(q\) sole-\(c\) voters, who exhaust the \(c\)-approvers, and exactly \(q\) formerly unrepresented \(x\)-approvers. These disjoint voter groups contribute no approvals for \(a\) or \(b\). Thus the remaining at most \(n-2q\) voters support both \(a\) and \(b\), whose combined scores are at least \(2q\). Since each remaining voter gives at most two approvals, \(2q\le2(n-2q)\), yielding \(n\ge3q\). But \(q=\lceil n/3\rceil\) implies \(n\le3q\). Equality follows, and the exactly \(q\) remaining voters approve both \(a\) and \(b\). Consequently replacing \(b\), rather than \(c\), by \(x\) is also welfare-preserving (the \(b\) score is exactly \(q\)) and strictly increases coverage: the \(a,b\) group remains represented by \(a\), the sole-\(c\) group by \(c\), and the previously unrepresented group now by \(x\). Contradiction. Thus a welfare-optimal JR committee exists.

**Necessity and sharp construction.** Assume \(2n\ge5q+3\). Set \(r=n-q\), and choose nonnegative integers \(r_1,r_2,r_3\) differing by at most one and summing to \(r\). Use precisely four candidates \(a,b,c,x\). There are \(r_1\) ballots \(\{a,b\}\), \(r_2\) ballots \(\{b,c\}\), \(r_3\) ballots \(\{a,c\}\), and \(q\) singleton ballots \(\{x\}\). The least of the three approval scores for \(a,b,c\) is \(\lfloor2r/3\rfloor\). Since \(2r=2(n-q)\ge3(q+1)\), this minimum is at least \(q+1\), whereas \(s(x)=q\). Therefore \(\{a,b,c\}\) is the *unique* welfare-optimal committee. It leaves all \(q\) voters approving only \(x\) unrepresented, violating JR. This proves both the if-and-only-if statement and the four-candidate sharp obstruction.

The residue description follows by substituting \(n=3t\), \(n=3t+1\), or \(n=3t+2\), with the appropriate ceiling, into \(2n\ge5q+3\). The first obstruction is \(n=9\): two ballots for each of \(\{a,b\},\{b,c\},\{a,c\}\) and three ballots for \(\{x\}\), giving scores \((4,4,4,3)\), welfare \(12\), and best JR welfare \(11\).

**Two-seat boundary.** For a committee of size two and the same ballot restriction, put \(q_2=\lceil n/2\rceil\). Among two highest-scoring candidates \(a,b\), a JR violation witnessed by \(x\) implies \(s(a),s(b)\ge s(x)\ge q_2\). At least \(q_2\) voters approve \(x\) but neither winner. Hence \(2q_2\le s(a)+s(b)\le2(n-q_2)\le2q_2\). Equality forces \(n=2q_2\), both selected scores and \(s(x)\) equal \(q_2\), and every other voter approves *both* \(a,b\). Replacing \(b\) by \(x\) preserves welfare and represents everyone, so a welfare-optimal JR committee always exists. The same reasoning covers a two-candidate election trivially.

**Singleton-approval boundary.** When every voter approves exactly one candidate, a hypothetical JR violation for a score-optimal size-\(k\) committee would supply \(k\) selected candidates with scores at least \(q_k=\lceil n/k\rceil\) and an unselected candidate supported by at least \(q_k\) *disjoint* voters. Thus \((k+1)q_k\le n\), impossible because \(q_k\ge n/k\). Therefore every welfare-optimal committee satisfies JR, provided at least \(k\) candidates are available.

## Verification

The independent standard-library script `verify_sparse_jr.py` exhaustively enumerates anonymous labeled-candidate approval profiles for four candidates through 12 voters and five candidates through six voters, checking every welfare-optimal committee directly against JR. It also checks the two-seat boundary for four candidates through nine voters and five candidates through six voters, the singleton-approval boundary for five candidates through ten voters, and the sharp construction for every population from one through 100. Its successful run ended with `VERIFY_OK anonymous_profiles 850550 witness_range 100`. The finite calculations corroborate the general analytical proof; they are not used to extrapolate beyond the tested sizes.

Reproduce with `python3 verify_sparse_jr.py` using Python 3 standard library. No data files, external services, or nonstandard dependencies are required.

## Relationship to prior work

Aziz et al. introduced JR and established its general attainability. Elkind et al. studied the *price* of imposing JR on approval welfare, with general worst-case bounds and algorithms. Becker, Greger and Peters established existence of core-stable committees, a stronger fairness property, in 2026. These results do not by themselves guarantee that some **unconstrained approval-welfare maximizer** meets JR under a two-approval ballot restriction. The present statement isolates this compatibility question and gives the exact population-dependent answer, including a complete negative construction and the minimality boundaries.

## Limitations

The equivalence is restricted to committees of size three, ballot cardinalities one or two, and binary approval scores. It does not characterize individual compatible profiles in the failing population range, nor quantify the maximum welfare loss beyond showing it can be positive. No claim is made for arbitrary ballot sizes, stronger representation axioms, or other welfare functions. An earlier unindexed derivation of the same threshold or an equivalent restricted-domain result remains a literature-priority possibility. Computational checks establish only their enumerated finite domains.

## References

1. H. Aziz, M. Brill, V. Conitzer, E. Elkind, R. Freeman, and T. Walsh, *Justified Representation in Approval-Based Committee Voting*, AAAI (2015); expanded in *Social Choice and Welfare* 48 (2017), doi:10.1007/s00355-016-1019-3.
2. E. Elkind, P. Faliszewski, A. Igarashi, P. Manurangsi, U. Schmidt-Kraepelin, and W. Suksompong, *The Price of Justified Representation*, arXiv:2112.05994 (first public 2021-12-11), https://arxiv.org/abs/2112.05994.
3. P. Becker, M. Greger, and D. Peters, *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912v1 (first public 2026-09-10), https://arxiv.org/abs/2609.11912.
