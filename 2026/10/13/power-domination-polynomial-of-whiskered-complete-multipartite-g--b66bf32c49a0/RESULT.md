# Power-domination polynomial of whiskered complete multipartite graphs

## Finding

**Theorem (complete set characterization and enumerator).** Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\) and \(n_i\ge2\) for all parts. Set \(N=\sum_{i=1}^r n_i\). Write \(H=G\circ K_1\) for the graph obtained by attaching one private leaf to each of the \(N\) original (core) vertices. Define \(\mathcal P(H;x)=\sum_{S\subseteq V(H),\ S\text{ power dominating}}x^{|S|}\).

Put
\[
T=x^2+2x,\qquad U_i=(1+x)^{2n_i}-(1+x)^{n_i},\qquad W_i=(1+x)^{N-n_i},\qquad E_2=\sum_{1\le i<j\le r}n_i n_j.
\]
Then the complete, all-cardinality polynomial is
\[
\boxed{\begin{aligned}
\mathcal P(H;x)={}&(1+x)^{2N}-(1+x)^N-\sum_{i=1}^r U_iW_i\\
&+x^N+Nx^{N-1}+E_2x^{N-2}\\
&+\sum_{i=1}^r\left[(T^{n_i}-x^{n_i})W_i+n_i(T^{n_i-1}-x^{n_i-1})(W_i-1)\right].
\end{aligned}}
\]
Every coefficient counts actual subsets of the graph's \(2N\) distinctly identified vertices, without identifying symmetric choices.

**Sharp minimum and multiplicity.** Let \(t_2=|\{i:n_i=2\}|\). Then
\[
\gamma_P(H)=2,\qquad [x^2]\mathcal P(H;x)=E_2+(2N-1)t_2+4\mathbf1_{N=4}.
\]
For example, when \(G=K_{2,2}\), the two-sensor multiplicity is \(22\), while for \(G=K_{3,3}\) it is \(9\).

## Assumptions and scope

A **power-dominating set** \(S\subseteq V(H)\) observes initially the union of the closed neighborhoods of its vertices. Thereafter an observed vertex having exactly one unobserved neighbor causes that neighbor to be observed. The set \(S\) is power dominating precisely when all vertices eventually become observed. Observation/forcing is a monotone process on a finite graph. We use the univariate polynomial with a separate variable \(x\) recording the number of initially selected vertices.

Label the core parts of \(G\) as \(V_1,\ldots,V_r\); the private leaf adjacent to core vertex \(v\) is \(v'\). Relative to a chosen \(S\), a part is **strong** if it contains a core vertex in \(S\), and a core--leaf pair \(\{v,v'\}\) is **vacant** if it is disjoint from \(S\). Let \(a_i\) be the number of vacant pairs whose cores lie in \(V_i\). There is no restriction on the selected leaf status when a core is itself selected.

The following cases are exhaustive and mutually exclusive. **(A)** At least two parts are strong: \(S\) power dominates. **(B)** Exactly one part \(V_i\) is strong: \(S\) power dominates exactly if \(a_i=0\), or if \(a_i=1\) and some leaf belonging to a core outside \(V_i\) is selected. **(C)** No part is strong: \(S\) power dominates precisely when the total number of vacant pairs is at most one, or it is exactly two and the vacant cores lie in different parts. All quantifiers range over the specified finite graphs; the lower bound \(n_i\ge2\) is used in case (C).

## Proof

**A. At least two strong parts.** A selected core in one part observes every core in any different part. With two distinct strong parts, every core is therefore observed immediately. Any remaining unobserved vertex is a private leaf, whose core now has that leaf as its sole unobserved neighbor, so it is forced. This proves A.

**B. Exactly one strong part.** Suppose only \(V_i\) contains selected cores. Every core outside \(V_i\) is initially observed. A core inside \(V_i\) is initially observed exactly when its own core--leaf pair is not vacant: a selected core observes itself, and a selected leaf observes its core. Thus the initially unobserved core vertices are precisely the \(a_i\) vacant cores inside \(V_i\). Their private leaves are unobserved as well. An observed vertex inside \(V_i\) has no core neighbor inside \(V_i\), so cannot force them. Every outside core is adjacent to all \(a_i\) vacant cores. If \(a_i\ge2\), no outside core can start forcing one of these cores; none of their private leaves can start a force. The process cannot complete.

If \(a_i=0\), all cores are already observed and the remaining private leaves force immediately. If \(a_i=1\), an outside core with its own selected leaf has its own leaf observed and sees precisely one unobserved neighbor (the unique vacant core in \(V_i\)), and so forces it; all cores then force outstanding leaves. Conversely, when no outside leaf is selected, each outside core has its own unobserved leaf *and* the vacant core as two unobserved neighbors, and no force can begin. This proves B.

**C. No strong parts.** Here every selected vertex is a private leaf. Initially, a core is observed exactly if its leaf is selected. The only initially unobserved cores are the vacant cores. An observed core in part \(V_i\) sees all vacant cores outside \(V_i\), but no vacant core inside \(V_i\); its own private leaf is already selected, hence observed. Every vacant core has an unobserved private leaf. If there are no vacancies, the process is done. With exactly one vacant core, select an observed core in a different part (possible since all parts have size at least two); it forces the vacant core, which then forces its leaf. With exactly two vacant cores in different parts, each of those parts contains another core with selected leaf because every part size is at least two; an observed core in each part forces the lone vacant core in the other part. Both private leaves then force.

For the converse, suppose at least two vacant cores lie in one part. Every observed core outside that part has at least those two unobserved neighbors, while observed cores inside it have no edges to them. Hence neither can be the first to force either of these two cores, even if other forces occurred elsewhere; both remain unobserved. If no part has multiple vacancies but there are at least three vacant cores, those cores occupy distinct parts. Every observed core then has at least two vacant neighbors outside its own part (and every vacant core is unobserved), so no first force is possible. Thus C is necessary as well as sufficient.

**Count the three types.** Any core--leaf pair has the four subset states: vacant (weight \(1\)); leaf only (weight \(x\)); core only (weight \(x\)); both (weight \(x^2\)). For a part of size \(n_i\), the generating polynomial of all assignments with at least one selected core is \(U_i\); for a part with no selected core it is \((1+x)^{n_i}\). Consequently the generating polynomial for at least two strong parts is the all-set polynomial \((1+x)^{2N}\) minus the zero-strong polynomial \((1+x)^N\) minus the exactly-one-strong polynomial \(\sum_iU_iW_i\).

With no strong parts, case C consists of exactly zero vacant pairs (one subset with weight \(x^N\)), exactly one vacant pair (\(N\) subsets of weight \(x^{N-1}\)), and exactly two vacant pairs in different parts (\(E_2\) subsets of weight \(x^{N-2}\)). With exactly one strong part \(V_i\), either all \(n_i\) local pairs are nonvacant (polynomial \(T^{n_i}\)) but not all are leaf-only (subtract \(x^{n_i}\)); all outside leaves may be selected arbitrarily (factor \(W_i\)). Alternatively, exactly one local pair is vacant (\(n_i\) choices), every other local pair nonvacant but not all leaf-only (factor \(T^{n_i-1}-x^{n_i-1}\)), and at least one outside leaf selected (factor \(W_i-1\)). These disjoint cases give precisely the boxed polynomial.

**Minimum.** No singleton set succeeds: one selected core leaves at least one unobserved core in its own part and no outside selected leaf (case B), while one selected leaf leaves \(N-1\ge3\) vacant pairs (case C). Two selected cores from different parts always succeed (case A). For a successful two-set, case A contributes \(E_2\). In case B, the sole strong part must have size exactly two, and for each such part the successful choices are: both cores (one choice); one core and the other local leaf (two choices); or one local core and one external leaf (\(2(N-2)\) choices), totaling \(2N-1\). Case C contributes only when \(N=4\), necessarily with two size-two parts; the two chosen leaves must have cores in different parts, giving \(4\) choices. The displayed minimum and multiplicity follow.

## Verification

The included standalone Python 3 standard-library checker builds each graph's adjacency sets from the definition, enumerates all \(2^{2N}\) initial subsets for seven part profiles, simulates the closed-neighborhood step and one-white-neighbor propagation, and independently compares the result with the structural classification and coefficients of the boxed polynomial. The profiles are \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), and \((2,2,2,2)\). In total **156,928 subsets** were checked. The output records zero classification mismatches and exact coefficient agreement for all profiles. Execute \(\texttt{python3 verify_power_corona.py}\) using only a Python 3 standard library. The all-orders proof is combinatorial and does not rely on finite enumeration.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana, and Teich introduced the power-domination polynomial and computed coronas with attached \(K_k\) for \(k>1\); their 2018 Question 3 explicitly asks for efficient computation of \(\mathcal P(H\circ K_1;x)\) for arbitrary bases. The present theorem resolves this question on the distinct and natural class of complete multipartite bases with every part size at least two, but does not assert an algorithm for arbitrary bases. Their Theorem 19 requires non-endpoint identification for path attachments and does not imply this result for attached \(K_1\). Bjorkman, Brennan, Flagg, and Koch (2023) relate full-observation reliability to the power-domination polynomial generally and analyze complete multipartite graphs *without* this private-leaf attachment; neither calculation supplies the above closed corona enumerator. Their Observation 4.2 implies that for independent failure probability \(q\), complete installation on every vertex of \(H\) has full-observation probability \(q^{2N}\mathcal P(H;(1-q)/q)\) for \(0<q<1\). This is an application of their established transformation, not a separate new claim.

The literature comparison included published mathematical results on minimum power domination of threshold graphs and fragile-PMU placement on complete multipartite bases. Those results address different base families/parameters and do not imply a complete all-subset enumeration on the whiskered complete multipartite graphs. Searching available published records and primary literature did not identify an exact antecedent, but absence from search results alone does not establish absolute originality.

## Limitations

The exact characterization uses \(r\ge2\) and \(n_i\ge2\); no assertion is made for singleton parts, arbitrary base graphs, directed observation, multisets of initial sensors, expected partially observed vertex count, or proof of uniqueness relative to all existing literature. The script checks only seven small part profiles, although the theorem is proved for all admissible part sizes. Prior results on the invariant and on generic full-observation reliability are not reclaimed. The literature search may have missed unpublished, unindexed, or later equivalent results. Independent audit has not been performed.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (first public version 2018-05-28), especially Theorem 19, Proposition 20, and Question 3. https://arxiv.org/html/1805.10984v1
2. B. Bjorkman, Z. Brennan, M. Flagg, J. Koch, *Power domination with random sensor failure*, arXiv:2312.12259v1 (first public version 2023-12-19), especially Observation 4.2 and Section 5.3. https://arxiv.org/html/2312.12259v1
