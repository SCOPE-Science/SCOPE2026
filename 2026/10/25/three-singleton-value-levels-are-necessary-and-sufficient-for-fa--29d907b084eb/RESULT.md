# Three singleton-value levels are necessary and sufficient for failure of ex-ante EF with ex-post EFX and Pareto optimality

## Finding

For complete allocation of indivisible goods under nonnegative additive utilities, consider the property that **some lottery is ex-ante envy-free (EF) and every allocation in its support is simultaneously envy-free up to any positively valued good (EFX) and Pareto optimal among complete integral allocations (PO)**. The universal existence guarantee holds for every number of agents and goods if all singleton values belong to a common set of at most two nonnegative values, by the bi-valued theorem of Bu et al. [1]. It fails with just three distinct positive singleton values. Specifically, there are three agents and four goods with value matrix

\[
\begin{array}{c|rrrr}
& a & b & c & d\\\hline
v_1&4&3&3&1\\
v_2&4&3&3&3\\
v_3&4&4&4&3
\end{array}.
\]

No ex-ante EF lottery on allocations that are both EFX and PO exists for this instance. Thus **three is the sharp global cardinality of the singleton-value alphabet at which the universal existence guarantee can fail**. In this witness only agent \(1\) uses three value levels; each of agents \(2\) and \(3\) uses two.

## Assumptions and scope

An allocation \(A=(A_1,A_2,A_3)\) partitions all four labeled goods. An additive valuation satisfies \(v_i(S)=\sum_{g\in S}v_i(g)\). An allocation is EFX when, for every \(i\ne j\) and each positively valued \(g\in A_j\),
\[
v_i(A_i)\ge v_i(A_j\setminus\{g\}).
\]
All values in the displayed witness are positive, so every good in a rival bundle must be tested. PO means that no **complete integral** allocation gives every agent at least their current own-bundle utility and some agent strictly more. A lottery \(p\) is ex-ante EF when \(\sum_Ap_A[v_i(A_i)-v_i(A_j)]\ge0\) for all ordered pairs of agents; only allocations of positive probability must satisfy EFX and PO. The positive side refers to a **common, across-agent** two-element singleton-value alphabet, not different two-element alphabets for each agent.

## Proof

**Two-level lower boundary.** Bu, Li, Liu, Lu, and Tao [1, Theorem 5.1] prove that for any number of agents with bi-valued additive utilities there is an ex-ante EF lottery whose every support allocation is EFX and even fractionally Pareto optimal. Since fractional PO implies integral PO, no counterexample with a common alphabet of one or two singleton values exists. Their theorem allows nonnegative values; the witness below is strictly positive.

**Exhaustive EFX restriction.** In any EFX allocation here every agent is nonempty. Otherwise four goods go to at most two recipients; a recipient has at least two goods and the empty agent strictly envies after deletion of either, violating EFX. Hence all EFX allocations have bundle-size pattern \((2,1,1)\) in some order. For a pair \(\{g,h\}\) allocated to agent \(k\) and singleton goods \(s_i\) allocated to each other agent \(i\), EFX is *equivalent* to
\[
v_i(s_i)\ge\max\{v_i(g),v_i(h)\}\quad(i\ne k).
\]
There are exactly \(3\binom42 2=36\) pair/singleton configurations to test. Applying this criterion produces exactly the following fourteen EFX allocations. Each triple lists bundles for agents \(1,2,3\), respectively; a dash in the last column indicates PO. If a dominator is listed, its own-utility vector weakly dominates that of the EFX allocation with a strict inequality in at least one coordinate.

| EFX allocation | Own utilities | Integral Pareto dominator if not PO |
|---|---|---|
| \((a,bd,c)\) | \((4,6,4)\) | — |
| \((a,b,cd)\) | \((4,3,7)\) | \((a,d,bc)\), \((4,3,8)\) |
| \((a,cd,b)\) | \((4,6,4)\) | — |
| \((a,c,bd)\) | \((4,3,7)\) | \((a,d,bc)\), \((4,3,8)\) |
| \((a,d,bc)\) | \((4,3,8)\) | — |
| \((bd,a,c)\) | \((4,4,4)\) | \((a,bd,c)\), \((4,6,4)\) |
| \((b,a,cd)\) | \((3,4,7)\) | — |
| \((cd,a,b)\) | \((4,4,4)\) | \((a,bd,c)\), \((4,6,4)\) |
| \((c,a,bd)\) | \((3,4,7)\) | — |
| \((bc,d,a)\) | \((6,3,4)\) | \((ab,d,c)\), \((7,3,4)\) |
| \((bd,c,a)\) | \((4,3,4)\) | \((ab,d,c)\), \((7,3,4)\) |
| \((b,cd,a)\) | \((3,6,4)\) | \((a,bd,c)\), \((4,6,4)\) |
| \((cd,b,a)\) | \((4,3,4)\) | \((ab,d,c)\), \((7,3,4)\) |
| \((c,bd,a)\) | \((3,6,4)\) | \((a,bd,c)\), \((4,6,4)\) |

The five allocations marked PO in the table really are PO: a direct test against all \(3^4=81\) complete allocations certifies that no integral allocation strictly Pareto-dominates any of them. The exhaustive certificate and its entirely self-contained verifier are supplied as `verify.py` and `verification_output.txt`. In particular this is an **exhaustive finite proof about this four-good instance**, not evidence extrapolated from finite sampling to all markets.

**Envy infeasibility certificate.** Denote the five EFX+PO allocations, in table order, by \(P=(a,bd,c)\), \(Q=(a,cd,b)\), \(R=(a,d,bc)\), \(S=(b,a,cd)\), and \(T=(c,a,bd)\). Let their nonnegative lottery probabilities be \(p_P,p_Q,p_R,p_S,p_T\), summing to one. Set
\[
x=p_P+p_Q,\qquad y=p_R,\qquad z=p_S+p_T,
\qquad x+y+z=1.
\]
The following exact envy surpluses are obtained by evaluating \(v_i(A_i)-v_i(A_j)\) on the five outcomes:

\[
\begin{array}{c|rrrrr|c}
(i,j)&P&Q&R&S&T&\text{lottery surplus}\\\hline
(1,2)&0&0&3&-1&-1&3y-z\\
(1,3)&1&1&-2&-1&-1&x-2y-z\\
(3,2)&-3&-3&5&3&3&-3x+5y+3z
\end{array}.
\]
Ex-ante EF requires all three right-column expressions to be nonnegative. However,
\[
3(x-2y-z)+(-3x+5y+3z)=-y\ge0.
\]
Since \(y\ge0\), this forces \(y=0\). The first inequality then gives \(-z\ge0\), hence \(z=0\); the last gives \(-3x\ge0\), hence \(x=0\). This contradicts \(x+y+z=1\). Therefore no such lottery exists. Combining the construction with the published common-two-value existence theorem proves the sharp alphabet boundary.

## Verification

Run `python3 verify.py` in the directory containing the accompanying source and output. The standalone program enumerates all \(3^4=81\) allocations, checks every EFX inequality, compares own-utility vectors against all complete integral allocations, identifies all fourteen EFX cases and five EFX+PO cases, and verifies the three envy-surplus vectors and their exact integer linear combination. Its terminal output is included as `verification_output.txt`. No external libraries, approximation, optimization solver, or unverifiable search certificate is needed. The count and dominance claims can also be checked by hand using the displayed fourteen-row table and the pair/singleton criterion.

## Relationship to prior work

Bu et al. [1] establish existence for *common bi-valued* additive singleton values, with the stronger ex-post fPO requirement. Aziz [2, Theorem 5] establishes three-agent/four-good impossibility for arbitrary strictly positive additive valuations with a displayed witness using the five distinct numbers \(\{1,2,3,4,5\}\). That theorem by itself does not establish that failure is possible with only three singleton values, and its actual witness is not the one given here. The contribution is the exact **valuation-alphabet boundary**, alongside a smaller-value-range counterexample and a short three-inequality obstruction; the three-agent/four-good impossibility itself is **not** claimed as new. Panchapakesan and Vaish [3] develop general subsidy/lottery duality and examples for other valuation classes, without a stated three-level additive boundary in the examined results. Numerical levels matter only as a witness; the claimed sharp parameter is cardinality of the globally shared value alphabet, not minimization of sum or bit-length of entries.

## Limitations

The positive side is a cited published theorem, not independently reproved here. The negative certificate covers the stated strictly positive \(3\)-by-\(4\) additive instance and the stronger requirement of ex-post **EFX+PO**; it does not establish impossibility when EFX is weakened to EF1, when PO is dropped, or when value alphabets vary per agent without a common two-value restriction. The algorithm checks integral PO, not fractional PO. The originality review cannot exclude unpublished examples or equivalent observations outside the examined literature; publication-priority assessment remains open to independent audit. These limitations do not affect the displayed finite contradiction.

## References

[1] Xiaolin Bu, Zihao Li, Shengxin Liu, Xinhang Lu, Biaoshuai Tao, *Best-of-Both-Worlds Fair Allocation of Indivisible and Mixed Goods*, arXiv:2410.06877, initial submission 2024-10-09; especially Theorem 5.1 (bi-valued existence).

[2] Haris Aziz, *Best-of-Both-Worlds Fairness and Pareto Optimality*, arXiv:2608.08966, initial submission 2026-08-10; especially Definitions 2, 4, 7 and Theorem 5, Section 6.

[3] Surya Panchapakesan and Rohit Vaish, *Best-of-Both-Worlds Fair Division via Subsidies*, arXiv:2610.14994, initial submission 2026-10-10; general duality and related counterexamples.
