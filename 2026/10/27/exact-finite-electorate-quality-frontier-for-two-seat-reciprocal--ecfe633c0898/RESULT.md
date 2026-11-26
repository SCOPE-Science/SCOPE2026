# Equal optimal reciprocal JR and EJR quality in two-seat elections

## Finding

In a two-seat approval election with candidate qualities in \((0,1]\) and at least one supporter per candidate, imposing reciprocal extended justified representation (rEJR) instead of reciprocal justified representation (rJR) has **no additional optimal-quality cost on any instance**. More precisely:

* If fewer than two unit-quality candidates have unanimous approval, the two axioms have the same feasible committees.
* If at least two unit-quality candidates have unanimous approval, an rJR committee satisfies rEJR exactly when some voter approves both of its members. Both optimum qualities are two. From any rJR-optimal pair, one can keep either member and obtain an rEJR-optimal pair by changing at most the other member.

Consequently the sharp retained-quality fraction for **rEJR** at fixed electorate size \(n\ge2\) is \((3n-2)/(4(n-1))\), the same as the fixed-electorate rJR benchmark. Every unrestricted quality-optimal pair is within one replacement of an rEJR committee meeting this bound. The benchmark for rJR itself is not claimed as a distinct contribution here.

## Assumptions and definitions

There are \(n\ge2\) voters \(V\) and finitely many candidates \(C\) with \(|C|\ge2\). Every candidate is approved by somebody. Voter \(i\) approves the subset \(A_i\subseteq C\). Candidate \(c\) has quality \(0<h_c\le1\), and a pair \(W\) has quality \(h(W)=\sum_{c\in W}h_c\). For a nonempty group \(S\subseteq V\), a nonempty set \(T\subseteq\bigcap_{i\in S}A_i\) is reciprocally affordable if
\[
|S|\ge\frac n2\sum_{c\in T}\frac1{h_c}.
\]
Reciprocal JR demands representation of at least one voter in every group with an affordable set; reciprocal EJR demands \(\max_{i\in S}|A_i\cap W|\ge |T|\) for each affordable pair \((S,T)\). These are the reciprocal-cost axioms of Boehmer, Dong, Kreisel and Utke [1]. The optimum for an axiom is the maximum quality among its feasible pairs.

## Proof of the pointwise comparison

Affordability implies \(|T|\le 2\), since every reciprocal term is at least one. If \(|T|=2\), it also implies \(|S|\ge n\). Hence \(S=V\) and both candidates in \(T\) have unit quality and unanimous approval. Conversely those two candidates yield a two-seat demand by \(V\). A one-seat rEJR demand is exactly the rJR demand for the same voter group. In particular, rJR for a group with a two-seat demand already follows from its affordable singletons.

If there are fewer than two unanimously approved unit-quality candidates, there are no two-seat demands, so rJR and rEJR coincide. Otherwise every two-seat demand is for the group \(V\), and is satisfied precisely when some voter approves both selected candidates. A pair of unanimously approved unit-quality candidates satisfies both axioms and reaches the absolute quality ceiling two. For any rJR-optimal pair, each member has unit quality. Keep either member and use a unanimously approved unit-quality candidate distinct from that member as the other member. The unanimous candidate represents every voter, and a supporter of the retained member approves both selected candidates. The resulting pair satisfies rEJR, attains quality two and differs in at most one member. The same argument works starting from any unrestricted quality-optimal pair in this case.

The feasible sets need not be equal when there is a two-seat demand. For example, two voters can both approve two unit-quality candidates, while each also approves a distinct quality-\(1/2\) candidate. The pair of quality-\(1/2\) candidates represents both voters and satisfies rJR, but neither voter approves both of its members, so it fails rEJR.

## Fixed-electorate consequence

For completeness, the rJR benchmark [2] used in the transfer can be seen directly. Set \(\tau_n=n/[2(n-1)]\) and let \(\{a,b\}\) be any unrestricted quality-optimal pair, with \(\alpha=h_a\ge\beta=h_b\). If it violates rJR, a group \(S\) approving neither member can afford a common candidate \(d\). Every candidate is supported, so \(|S|\le n-1\), and affordability implies \(h_d\ge \tau_n\) and \(|S|\ge n/2\). The pair \(\{a,d\}\) represents everyone in \(S\) and at least one voter outside \(S\) who approves \(a\). It therefore represents a strict majority and satisfies rJR, since any group entitled to representation has size at least \(n/2\). Writing \(\mathrm{OPT}=\alpha+\beta\), the retained fraction is at least
\[
\frac{\alpha+\tau_n}{\alpha+\beta}\ge\frac{1+\tau_n}{2},
\qquad
2(\alpha+\tau_n)-(1+\tau_n)(\alpha+\beta)
=(1-\tau_n)(\alpha-\beta)+2\tau_n(1-\beta)\ge0.
\]
Thus in the case with no two-seat demand the same rJR repair works for rEJR; in the other case the pointwise comparison above gives an optimal rEJR pair by one replacement. If the original pair already satisfies rEJR, no change is required.

The three-candidate witness has qualities \((1,1,\tau_n)\); one voter approves only the two unit candidates and the remaining \(n-1\) voters approve only the third candidate. The latter bloc can afford that candidate at equality, so every fair pair must include it, and either such pair covers all voters. No candidate is unanimously approved, so the feasible sets for rJR and rEJR coincide here. The optimum fraction under either axiom is exactly \((1+\tau_n)/2=(3n-2)/(4(n-1))\). This also holds at \(n=2\), when the fraction is one. For \(n\ge3\) this is the fixed-\(n\) specialization of Example G.1 in [1].

## Relationship to prior work and limits

Theorem 5.5 and Appendix G of [1] give the unrestricted quality bound and Example G.1 gives the attaining profile after fixing \(n\). Equality of two axioms' unrestricted worst-case prices does not entail equality of their optima on each election. Reference [2] concerns only the fixed-\(n\) rJR price and equality necessity for rJR extremizers. The distinct claim here is the pointwise reduction for rEJR under an exact two-seat constraint, not a second derivation of the rJR-only rate or a new extremal profile. The result concerns optima, not a guarantee for every fair output. It does not cover larger committees or variants such as reciprocal threshold-PJR+ or value-EJR. The scope of the literature comparison is limited to inspected sources; absolute publication priority is not asserted.

## Verification

Run `python3 verify.py` for exact finite checks of the committee-level comparison, same-quality conversion, the one-replacement rEJR guarantee from any optimal pair and the sharp profile. The finite checks supplement the proof, not replace it.

## References

1. N. Boehmer, C. Dong, L. Kreisel, and M. Utke, *Approval-Based Multiwinner Voting with Candidate Qualities*, arXiv:2609.08830v1, Definitions 5.1–5.3, Theorem 5.5, Table 9, and Appendix G. https://arxiv.org/abs/2609.08830
2. *Exact finite-electorate quality price for two-seat reciprocal justified representation*. The reference is for statement-level comparison of the shared rJR benchmark, without asserting priority between the two analyses.
