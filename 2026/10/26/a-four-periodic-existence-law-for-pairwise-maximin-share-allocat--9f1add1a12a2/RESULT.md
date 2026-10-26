# A four-periodic existence law for pairwise maximin-share allocations under common-good padding

## Finding

Consider four agents and indivisible goods drawn from the following classes, where each column gives a value to agents \(1,2,3,4\), respectively:

| Item class | Quantity | Values to agents \(1,2,3,4\) |
| --- | ---: | --- |
| \(A\) | \(3\) | \((81,81,81,81)\) |
| \(B\) | \(5\) | \((100,100,94,94)\) |
| \(C\) | \(5\) | \((94,94,100,100)\) |
| \(D\) | \(p\) | \((101,101,101,101)\) |

Here \(p\) is any nonnegative integer, and goods within a class are distinct but identically valued. An allocation is *pairwise maximin-share fair* (PMMS) if for every ordered pair of distinct agents \(i,j\),
\[
 v_i(X_i)\ge \max_{Y\sqcup Z=X_i\sqcup X_j}\min\{v_i(Y),v_i(Z)\}.
\]

**Theorem.** This family has a PMMS allocation if and only if
\[
 p<15\quad\text{or}\quad (13+p)\not\equiv0\pmod4.
\]
Thus PMMS is impossible precisely for \(p=15,19,23,27,\ldots\). In this explicit four-agent valuation family, the first impossible instance has \(28\) goods; adding just one further universally valued good restores existence, and the obstruction repeats at every subsequent multiple of four. This is a sharp statement *within the stated padding family*, not a universal lower bound on the number of goods or agents for arbitrary PMMS failures.

## Assumptions and scope

Utilities are strictly positive, nonnegative-additive, and identical within each class. An allocation assigns every good to exactly one of four agents. Identical goods are treated as distinguishable in the definition, but allocation feasibility and utility depend only on class counts. All quantities and inequalities are exact integers. The relevant original counterexample has \(p=39\), hence \(52\) goods [1]. The theorem varies only the common class \(D\) and holds for every integer \(p\ge0\).

## Proof

**1. Cardinality forcing.** Write \(c_i(g)=101-v_i(g)\). These deficits vanish for class \(D\), and their total over the thirteen \(A,B,C\) goods is \(100\) for each agent. Therefore, for every subbundle \(S\),
\[
 101|S|-100\le v_i(S)\le101|S|.
\]
If an allocation contains \(|X_j|\ge|X_i|+2\), agent \(i\) can repartition their union into two subbundles, each containing at least \(|X_i|+1\) goods. Both have utility at least \(101(|X_i|+1)-100>101|X_i|\ge v_i(X_i)\). Hence every PMMS allocation has bundle sizes differing by at most one.

**2. Exact pairwise criterion.** Encode agent \(i\)'s rare goods by \(R_i=(a_i,b_i,c_i)\), their own deficit by \(d_i=(20,1,7)\cdot R_i\) for agents \(1,2\) and by \(d_i=(20,7,1)\cdot R_i\) for agents \(3,4\). Let \(s_i=|X_i|\) and \(u=R_i+R_j\). The padding count is \(s_i-a_i-b_i-c_i\), which must be nonnegative.

For equal sizes \(s_i=s_j=k\), a split with unequal sizes cannot improve the minimum utility above the agent's current utility by the \(100\)-deficit bound. The maximin optimum is therefore achieved at an equal-cardinality split. For an integer triple \(t\), let \(c_i(t)\) denote its deficit and put
\[
T_k^{=}(i,u)=\min_{0\le t\le u\atop |t|\le k,\,|u-t|\le k}\max\big\{c_i(t),c_i(u-t)\big\}.
\]
Then the ordered pair condition is exactly \(d_i\le T_k^{=}(i,u)\).

For sizes \(s_i=k\), \(s_j=k+1\), the long-bundle agent \(j\) automatically meets the ordered condition relative to \(i\), because \(v_j(X_j)\ge101(k+1)-100>101k\), while any bipartition has a side containing at most \(k\) goods. The short-bundle agent's maximin optimum is achieved using a partition of sizes \(k,k+1\), and its smaller side in utility is always the \(k\)-item part. Hence its ordered condition is exactly \(d_i\le T_k^{<}(i,u)\), where
\[
T_k^{<}(i,u)=\min_{0\le t\le u\atop |t|\le k,\,|u-t|\le k+1}c_i(t).
\]
The displayed constraints allow padding to complete the two sides. Both criteria are necessary and sufficient; the verifier enumerates every permitted \(t\) exactly.

**3. All equal-size cases.** For total item count \(13+p=4k\), the cardinality lemma forces \(s_i=k\) for all four agents. The number of possible assignments of the \(3\), \(5\), and \(5\) indistinguishable class-counts to four labeled agents is
\[
 \binom{6}{3}\binom{8}{3}^2=62{,}720.
\]
The verifier explicitly enumerates every such integer-count assignment, checks each agent's padding capacity, and applies the exact threshold criterion to all ordered pairs. Numbers of valid PMMS count-allocations are: \(28\) at \(k=4\), \(24\) at \(k=5\), \(8\) at \(k=6\), and **zero for each \(k=7,8,9,10,11,12,13\)**. Counts of capacity-feasible rare allocations in the seven zero cases are, respectively, \(55{,}216\), \(59{,}920\), \(61{,}840\), \(62{,}500\), \(62{,}680\), \(62{,}716\), and \(62{,}720\). These are exhaustive finite certificates implemented in the accompanying standard-library `verify.py`, not extrapolations from sampling.

For \(k\ge13\), any assignment of the thirteen rare goods fits in each agent's bundle. Moreover, *every* split of the rare goods between two \(k\)-item sides can be completed with class-\(D\) goods, because each rare subset has size at most thirteen. Thus \(T_k^{=}(i,u)\) and all comparisons become independent of \(k\) for \(k\ge13\). Exhaustiveness at \(k=13\) therefore rules out all larger equal-size cases.

**4. Existence at every other size.** The verifier supplies, and checks by the *original definition* of PMMS, explicit complete allocations for every \(p=0,1,\ldots,14\). Each certificate specifies the four triples \(R_i\) and four target sizes \(s_i\); each agent receives the unique nonnegative number \(s_i-|R_i|\) of class-\(D\) goods.

It remains to exhibit PMMS allocations at total sizes \(4k+r\) for every \(k\ge7\), \(r=1,2,3\). For \(r=1\) and \(7\le k\le11\), the five explicit witness allocations are supplied in `verify.py`, checked both through the criteria above and by direct exact PMMS evaluation. For \(r=1\), \(k\ge12\), give all thirteen rare goods to agent \(4\), give that agent \(k+1\) goods total, and give only class-\(D\) goods to agents \(1,2,3\), each receiving \(k\). Every short agent's deficit is zero; the long agent meets PMMS automatically against all short agents.

For \(r=2\), assign rare triples
\[
(R_1,R_2,R_3,R_4)=((0,0,0),(0,0,0),(1,4,2),(2,1,3))
\]
with target cardinalities \((k,k,k+1,k+1)\). For \(r=3\), use
\[
(R_1,R_2,R_3,R_4)=((0,0,0),(0,5,0),(1,0,5),(2,0,0))
\]
with cardinalities \((k,k+1,k+1,k+1)\). All classes sum to their specified supplies. The ordered comparisons pass for both templates at \(k=13\) (verified directly). For \(7\le k<13\), every permitted rare-item split is among those permitted at \(k=13\), so the exact PMMS criterion can only be easier to meet; bundle capacities are already sufficient at \(k=7\). For \(k>13\), all thirteen rare goods can fit on either side and the set of permitted rare-item splits is unchanged. The same templates therefore work for every \(k\ge7\).

These cases exhaust all nonnegative \(p\), completing the proof.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. The verifier separately performs (i) the complete \(62{,}720\)-profile class-count enumeration for all equal-size thresholds \(k=4,\ldots,13\), (ii) the explicit witness assertions for \(p=0,\ldots,14\) and larger-size templates, and (iii) a second *direct* computation of the two-bundle maximin benchmark using all four item classes and untransformed integer utilities for each displayed witness. Successful execution prints `ALL EXACT CHECKS PASSED`. Finite enumeration proves the bounded certificates; the cardinality and stabilization arguments extend them to all \(p\ge0\).

## Relationship to prior work

Aziz [1] supplies exactly these rare classes and common padding class, at \(p=39\), as a four-agent PMMS nonexistence counterexample. The new statement concerns the complete infinite padding family: it finds the smaller \(p=15\) obstruction, exactly characterizes existence and nonexistence at every padding count, and establishes repeated recovery and loss of fairness after universally positively valued additions. Gölz [2] and Bei et al. [3] independently supply stronger *unrestricted* small-market nonexistence results, including three-agent/nine-good examples; no such global size priority is claimed here. The original source materials and other publicly accessible mathematical research records inspected for the exact padding family did not present the if-and-only-if periodic classification. This is evidence of a distinction, not a guarantee of historical priority.

## Limitations

The theorem concerns the explicit fixed \(3,5,5,p\) supplies and two agent valuation types. It does not describe arbitrary additive valuations, show a global minimum goods count, or provide efficient algorithms for general PMMS allocation. The exhaustive count stage relies on correctness of a transparent, reproducible finite verifier, and the independent external audit has not been performed. Earlier equivalent mathematical formulations may remain undiscovered.

## References

1. H. Aziz, *Pairwise Maximin Share Allocations Need Not Exist*, arXiv:2609.06282 (first public version September 5, 2026), https://arxiv.org/abs/2609.06282 .
2. P. Gölz, *PMMS Allocations Need Not Exist for 3 Agents with Additive Valuations*, arXiv:2609.08954 (first public version September 8, 2026), https://arxiv.org/abs/2609.08954 .
3. X. Bei, Z. Lin, S. Liu, R. Luan, and B. Tao, *Non-Existence of PMMS Allocations and a 4/3-PMMS Guarantee for Additive Chores*, arXiv:2609.10493 (first public version September 9, 2026), https://arxiv.org/abs/2609.10493 .
