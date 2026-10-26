# Unique five-good obstruction to maximin-share allocation for three agents

## Finding
Let \(M\) contain exactly five indivisible goods. For each of three agents, choose an unordered partition \(P_i\) of \(M\) into three nonempty blocks. A *disjoint transversal* consists of blocks \(B_i\in P_i\), one for each agent, with \(B_i\cap B_j=\varnothing\) whenever \(i\ne j\).

**Classification theorem.** A disjoint transversal fails to exist **if and only if** the following three conditions all hold:

1. Every \(P_i\) has block sizes \((1,2,2)\).
2. Their singleton blocks coincide, say \(\{e\}\).
3. The remaining pairs in the three partitions are the three distinct perfect matchings of the four-element set \(M\setminus\{e\}\).

Among the \(25^3=15{,}625\) ordered triples of three-part partitions of a labeled five-good set, exactly \(30\) have no disjoint transversal, and all \(30\) are equivalent under relabeling goods and agents.

**Consequences for monotone maximin-share allocation.** Consider three agents with normalized, nonnegative, monotone set valuations on five goods. If no allocation gives every agent their full maximin share (MMS), then **every** triple of MMS-attaining three-block partitions has precisely the exceptional pattern above. Such failure is possible using binary monotone valuations, and no failure is possible with four or fewer goods. This is a necessary structural characterization of arbitrary nonexistence instances, **not** a claim that the existence of one exceptional triple suffices for nonexistence under general valuations.

## Assumptions and scope
A partition here is an *unordered* family of three pairwise disjoint nonempty subsets whose union is the ground set. The agent triple is ordered; goods are labeled for the counting statement. All valuations \(v_i:2^M\to\mathbb R_{\ge0}\) are normalized, \(v_i(\varnothing)=0\), and monotone under inclusion. Agent \(i\)'s MMS is
\[
\mu_i=\max_{(Q_1,Q_2,Q_3)\text{ partition of }M}\min_{j=1,2,3}v_i(Q_j).
\]
An MMS allocation is a disjoint covering allocation \((A_1,A_2,A_3)\) with \(v_i(A_i)\ge\mu_i\) for every agent. No additivity, submodularity, or continuity assumption is imposed.

## Proof
**1. Singleton structure.** Every three-block partition of five goods has either size profile \((1,1,3)\), called type A, or \((1,2,2)\), called type B. A type A partition has exactly two singleton blocks, while a type B partition has exactly one. Write \(S_i\) for the set of goods occurring in singleton blocks of \(P_i\).

**2. Two type B partitions with the same singleton, but no triple coincidence.** Suppose two type B partitions have common singleton \(\{e\}\), and the third partition has a singleton \(\{f\}\) with \(f\ne e\). Give \(\{e\}\) to the first type B agent and \(\{f\}\) to the third agent. One of the two disjoint pair blocks of the second type B agent avoids \(f\) and also avoids \(e\). The three chosen blocks are disjoint. Thus, a failing triple in which two type B singletons coincide must have all three partitions of type B with common singleton.

**3. Remaining singleton configurations.** Otherwise no two type B singletons coincide. If \(|S_1\cup S_2\cup S_3|\ge3\), Hall's marriage condition holds for the three singleton-choice sets: each set is nonempty; any two have a union of size at least two (two type A sets have size two, and two type B singletons are distinct); and the union of all three has size at least three. Choose three distinct singleton blocks and obtain a transversal.

If instead their union has size at most two, it must consist of exactly two goods \(\{a,b\}\), since any type A partition already supplies two distinct singletons; three distinct type B singletons would give union of size three. At least one partition is type A, and every type A partition has exactly the singleton blocks \(\{a\}\), \(\{b\}\) and the complementary triple \(M\setminus\{a,b\}\). Choose an agent with a type A partition to receive that complementary triple. The other two agents can receive the two singleton blocks \(\{a\}\), \(\{b\}\): any type B agents among them have distinct respective singletons, and type A agents accept either singleton. Thus a transversal exists.

**4. Three coincident type B singletons.** Suppose all three partitions have unique singleton \(\{e\}\). Any three pairwise disjoint nonempty blocks selected from these partitions have combined cardinality at most five; hence at least one is a singleton. The singleton must be \(\{e\}\). The other two selected blocks must therefore be complementary pairs on \(M\setminus\{e\}\). For two perfect matchings of a four-element set, a pair in one is complementary to a pair in the other exactly when the two matchings coincide. Hence a transversal exists if two of the three matchings agree; it fails precisely when all three are distinct.

**5. Counting and symmetry.** There are \(\bigl\{\begin{smallmatrix}5\\3\end{smallmatrix}\bigr\}=25\) partitions into three nonempty unordered blocks. Choose the common singleton in five ways. The four remaining goods have exactly three perfect matchings; assign these three different matchings to the three labeled agents in \(3!=6\) ways. Therefore there are exactly \(5\cdot6=30\) failures. Permutations of the four nonsingleton goods act as the full symmetric group on the three matchings, and the singleton can be relabeled freely, proving a single relabeling class.

**6. MMS consequences and sharpness.** Every agent has an MMS-attaining partition with three nonempty blocks: when their MMS is positive, any maximizing partition has nonempty blocks by normalization; when it is zero, any partition into three nonempty blocks attains the zero MMS by nonnegativity. If the chosen nonempty partitions admit a disjoint transversal, allocate each agent their selected block and distribute leftover goods arbitrarily; monotonicity preserves each agent's MMS. Thus the absence of an MMS allocation forces every selected triple to be exceptional by the classification above.

For a witness take \(M=\{e,1,2,3,4\}\), and give each agent one of the three distinct matchings on \(\{1,2,3,4\}\):
\[
\{12\mid34\},\qquad\{13\mid24\},\qquad\{14\mid23\}.
\]
Define \(v_i(B)=1\) if \(e\in B\) or \(B\) contains one of the two pairs in agent \(i\)'s matching, and define \(v_i(B)=0\) otherwise. These valuations are normalized, binary, and monotone. For each agent, the singleton \(\{e\}\) and their two matched pairs form an MMS-attaining partition, so \(\mu_i=1\). An allocation satisfying all three agents would choose for each agent a qualifying subset, which can be reduced to one of the three blocks of this partition; these would be disjoint, contradicting step 4. Therefore no MMS allocation exists.

For four goods, every three-part partition has size profile \((1,1,2)\). If three agents' sets of singleton goods have union size at least three, Hall's condition yields a distinct-singleton transversal. Otherwise, the three sets are the same two goods \(\{a,b\}\); give their singleton blocks to two agents and the complementary pair to the third. Three goods are immediate. Hence all normalized monotone three-agent instances with at most four goods admit an MMS allocation (zero-MMS agents pose no obstruction).

## Verification
The standalone Python file `VERIFY.py` enumerates all partitions of three, four, and five goods, checks the disjoint-transversal condition for all \(25^3\) ordered five-good triples, independently recognizes the stated exceptional structure, confirms that both predicates agree on every triple, and verifies the \(30\)-exception count. It also examines all \(3^5=243\) allocations of the explicit binary-valuation witness and confirms that none satisfies all agents. The classification and general valuation statements are proved analytically above; finite enumeration is a reproducibility check rather than a substitute for the proof.

## Relationship to prior work
Uriel Feige, *On MMS allocations with few items* (arXiv:2610.06125, first public October 5, 2026), supplies a broader hypergraph/rainbow-matching framework for exact MMS and **already constructs a family of monotone MMS counterexamples** whose three-agent, five-good specialization supplies the nonexistence witness. Neither the existence of that witness nor the four-good existence assertion is claimed as an independent new construction. The result here is the converse *structural necessity and uniqueness*: among all possible triples of five-good MMS partitions, the known mechanism is the only obstruction, with exactly \(30\) labeled triples in one symmetry class. The construction and the classification are logically distinct.

Additive valuation results, such as Feige, Sapir, and Tauber, *A tight negative example for MMS fair allocations* (arXiv:2104.04977), concern a narrower valuation class; they do not establish the classification for arbitrary monotone valuations.

## Limitations
The classification concerns three agents, five indivisible goods, and nonempty three-partitions; it is not an enumeration of all monotone valuation functions or of all inequivalent non-MMS valuation instances. It does not claim that one exceptional MMS-partition triple is sufficient for failure for an arbitrary valuation profile. The count \(30\) uses **labeled goods and agents** and **unordered blocks within each partition**. Novelty is qualified by possible unindexed or uninspected equivalent work. Independent validation has not been performed.

## References
1. U. Feige, *On MMS allocations with few items*, arXiv:2610.06125, first posted October 5, 2026. https://arxiv.org/abs/2610.06125 .
2. U. Feige, A. Sapir, and L. Tauber, *A tight negative example for MMS fair allocations*, arXiv:2104.04977. https://arxiv.org/abs/2104.04977 .
