# Fibonacci-optimal circular covers of the golden-mean language: a rigid factor-multiplicity law

## Finding

Let \(k\ge 2\) be an integer, and let \(\mathcal F_k\) be the set of binary words of length \(k\) with no adjacent \(1\)s. A *circular cover* of \(\mathcal F_k\) is a nonempty cyclic binary word \(C\) containing no cyclic occurrence of \(11\), in which each element of \(\mathcal F_k\) occurs as a cyclic factor of length \(k\) at least once. Every starting position, including those whose factors wrap around, counts as one occurrence. Write \(\nu_C(w)\) for this count. Fibonacci numbers satisfy \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\).

**Theorem.** The least possible length of a circular cover is

\[
\boxed{L_k=F_{k+2}+F_k-1.}
\]

Moreover, every minimum-length circular cover has *exactly the same* cyclic length-\(k\) factor multiplicities:

\[
\boxed{\nu_C(w)=1+\mathbf 1_{\{w_1=w_k=0,\;w\ne 0^k\}}\quad(w\in\mathcal F_k).}
\]

In particular, precisely \(F_k-1\) different allowed factors occur twice; all others occur once; no allowed factor occurs three times. This is uniqueness of the factor-multiplicity profile, **not** uniqueness of the optimal cyclic word up to rotation. The theorem includes \(k=2\), where no factor repeats and the optimum has length three.

## Assumptions and scope

The alphabet is \(\{0,1\}\), the sole forbidden adjacent pair is \(11\), the length-\(k\) factors must be covered **cyclically**, and the covering word itself also avoids \(11\) at the wraparound boundary. Arbitrary allowed factors may repeat. Only \(k\ge2\) is asserted. No claim is made about linear shortest superstrings, other forbidden sets, or the number of distinct optimal circular covers.

## Proof

**1. Directed factor graph.** Construct the directed graph \(G_k\) whose vertices are allowed binary words of length \(k-1\) and whose edges are the allowed words \(w=w_1\cdots w_k\in\mathcal F_k\), directed from the prefix \(w_1\cdots w_{k-1}\) to the suffix \(w_2\cdots w_k\). The classical two-state recursion gives \(|E(G_k)|=|\mathcal F_k|=F_{k+2}\). This graph is strongly connected: from any vertex, append zeros until the all-zero vertex is reached; from that vertex, append the digits of any desired allowed vertex. Every circular cover corresponds to a closed walk using every edge at least once, and conversely a closed walk covering every edge spells such a circular cover. The number of walk edges equals the number of cyclic positions. Denote the extra traversal count of edge \(w\) by \(x_w=\nu_C(w)-1\ge0\).

**2. Candidate augmentation and its feasibility.** Put

\[
 x_w^*=\mathbf 1_{\{w_1=w_k=0,\;w\ne0^k\}}.
\]

There are precisely \(F_k-1\) such edges: delete the two bounding zeros to obtain a nonzero binary word of length \(k-2\) avoiding \(11\). For any nonzero vertex \(v\) of length \(k-1\), its original outdegree and indegree are, respectively,

\[
 d^+(v)=1+\mathbf1_{\{v_{k-1}=0\}},\qquad
 d^-(v)=1+\mathbf1_{\{v_1=0\}}.
\]

The proposed extra outgoing and incoming multiplicities are, respectively,

\[
 e^+(v)=\mathbf1_{\{v_1=0\}},\qquad
 e^-(v)=\mathbf1_{\{v_{k-1}=0\}}.
\]

Thus \(d^+(v)+e^+(v)=d^-(v)+e^-(v)\). At the all-zero vertex both extra multiplicities are zero and the original degrees are two. Hence the augmented directed multigraph is balanced and strongly connected. By the Euler-circuit theorem it has a closed Eulerian traversal, proving that a circular cover of length \(F_{k+2}+F_k-1\) exists with exactly the proposed multiplicities.

**3. A sharp lower bound.** For a vertex \(v\), let \(h(v)\) be the one-based position of its rightmost \(1\), or zero if it has none. For every directed edge \(u\to v\), shifting one position to the left and appending a bit gives

\[
 h(u)-h(v)\le1.
\]

Equality holds precisely when the appended bit is \(0\) and the source vertex contains a \(1\). In particular, each edge used as an extra traversal in step 2 satisfies equality.

Because the extra traversals of **any** circular cover rebalance the original edges, their net degree imbalance is independent of the cover. Therefore their total weighted potential difference is fixed:

\[
 \sum_{w\in\mathcal F_k}x_w\bigl(h(\operatorname{pre}(w))-h(\operatorname{suf}(w))\bigr)
 =-\sum_{w\in\mathcal F_k}\bigl(h(\operatorname{pre}(w))-h(\operatorname{suf}(w))\bigr).
\]

Using the explicitly balanced augmentation from step 2 and the equality of its potential differences to one, the common value of the left side is \(F_k-1\). Since each summand's potential difference is at most one and \(x_w\ge0\), every cover has \(\sum_w x_w\ge F_k-1\). Its length is consequently at least \(F_{k+2}+F_k-1\). The construction attains this bound.

**4. Rigidity of the optimum.** If a cover attains the bound, then every edge with positive extra multiplicity must satisfy \(h(\operatorname{pre}(w))-h(\operatorname{suf}(w))=1\). All such *tight* edges point from a vertex of strictly larger \(h\) to one of strictly smaller \(h\), so their directed graph is acyclic. Suppose two optimal extra-multiplicity vectors existed. Their difference would be a signed circulation supported on the tight-edge graph. This particular tight-edge graph has no nonzero signed circulation: at a source vertex the conservation law forces its outgoing coefficients to sum to zero, and every vertex has **at most one outgoing tight edge** (the edge obtained by appending zero), so its coefficient itself must vanish; iterating in topological order eliminates every coefficient. Equivalently, in this particular graph, the tight-edge incidence columns are independent. Thus the two vectors coincide. As the explicit \(x^*\) is optimal, it is the unique optimal extra-edge multiplicity vector, establishing the claimed complete profile. \(\square\)

*Technical note on the last step.* Each vertex has at most one tight outgoing edge because equality requires appending \(0\) and a nonzero source. Thus there are no parallel outgoing tight edges that could cancel in a signed circulation. The resulting directed forest structure is stronger than mere acyclicity and suffices for the uniqueness argument.

## Verification

Run `python verify.py` with Python 3 and only the standard library. The verifier enumerates every allowed factor for \(2\le k\le14\), checks the Fibonacci edge count, the proposed extra multiplicities, all vertex degree balances, the potential-difference identity, and an explicitly constructed Hierholzer Eulerian circular cover. It checks that the literal cyclic factor histogram of each construction matches the theorem exactly. For \(k=2,3,4\) it also enumerates all shorter binary cycles and proves none is a cover by exhaustive finite search; for \(k=2,3,4,5\) it enumerates optimal-length cycles and verifies that every realizable cover has the asserted unique histogram. Output:

`VERIFY_OK k=2..14 factor_edges=2579 vertices=1594 produced_positions=3551 exhaustive_short_lengths=16 optimal_linear_representatives_k2to5=131`

These finite checks corroborate but do not replace the all-\(k\) proof. The graph argument supplies the infinite theorem, including the uniqueness statement.

The first optimal lengths, for \(k=2,\ldots,8\), are \(3,6,10,17,28,46,75\). For example, \(k=3\) requires exactly one second occurrence, of the factor `010`; the other four allowed triples each occur once.

## Relationship to prior work

Chee, Etzion, Kiah, Vardy, Vu, and Yaakobi (2020, arXiv:2005.03102) study *constrained de Bruijn codes*. In their Definition 2, a \((b,k)\)-constrained word has no repeated length-\(k\) substring within a specified short sliding interval. This differs from covering **all** words avoiding the fixed forbidden pair `11`, and it does not state the present minimum length or rigid factor multiplicities.

Bernardini et al. (2022, *On Strings Having the Same Length-k Substrings*, DOI 10.4230/LIPIcs.CPM.2022.16) analyze a broad shortest-string problem using Eulerian walks and directed Chinese postman algorithms. Their framework encompasses a general optimization interpretation, but their proved general algorithm and asymptotic bounds do not themselves specify the closed Fibonacci optimum or unique optimal traversal-count vector for this forbidden-pair family. Bernardini et al. (2022, *Making de Bruijn Graphs Eulerian*, DOI 10.4230/LIPIcs.CPM.2022.12) address general graph completion, including edge additions, rather than this explicit already-strongly-connected constrained family. The claimed contribution is the special-family formula and rigid equality classification, not the known graph-model reduction.

## Limitations

This is a self-contained proof for circular binary covers subject to a particular length-two forbidden word. Other forbidden patterns may have disconnected factor graphs or more than one optimal repetition profile; no claim of generalization is made. Equivalent enumerations could exist under alternate terminology for Fibonacci or golden-mean walks. Exhaustive checks terminate at the reported finite ranges and are not proofs of the infinite statements. No independent review or external certification has been performed.

## References

1. Y. M. Chee, T. Etzion, H. M. Kiah, A. Vardy, V. K. Vu, E. Yaakobi, *Constrained de Bruijn Codes: Properties, Enumeration, Constructions, and Applications* (2020), arXiv:2005.03102, https://arxiv.org/abs/2005.03102 .
2. G. Bernardini et al., *On Strings Having the Same Length-k Substrings* (2022), DOI:10.4230/LIPIcs.CPM.2022.16, https://doi.org/10.4230/LIPIcs.CPM.2022.16 .
3. G. Bernardini et al., *Making de Bruijn Graphs Eulerian* (2022), DOI:10.4230/LIPIcs.CPM.2022.12, https://doi.org/10.4230/LIPIcs.CPM.2022.12 .
