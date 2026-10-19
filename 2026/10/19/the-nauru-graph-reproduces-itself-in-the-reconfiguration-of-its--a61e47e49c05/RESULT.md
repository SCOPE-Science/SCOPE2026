# The Nauru graph reproduces itself in the reconfiguration of its strong metric bases

## Finding

Let \(G=\operatorname{GP}(12,5)\) be the Nauru graph. Its **strong resolving graph** (defined below) is the disjoint union of two \(4\)-by-\(3\) rook graphs:
\[
G_{\mathrm{SR}}\cong 2(K_4\square K_3).
\]
Consequently the strong metric dimension of \(G\) is \(18\), and there are exactly \(576\) strong metric bases. Join two bases if one selected vertex can be replaced by one unselected vertex so that the replacement is again a minimum strong metric basis. The resulting token-jump reconfiguration graph satisfies the **self-product identity**
\[
\boxed{\mathcal R_{\mathrm{sdim}}(G)\cong G\square G.}
\]
In particular, this graph has \(576\) vertices, \(1728\) edges, is connected and \(6\)-regular, and is self-centered with radius and diameter \(8\). The number of bases at reconfiguration distance \(0,1,\ldots,8\) from any fixed basis is respectively
\[
(1,6,21,54,100,138,141,90,25).
\]

## Assumptions and scope

The graph \(G\) is the simple undirected graph on \(\{u_i,v_i:i\in\mathbb Z/12\mathbb Z\}\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+5}\) (indices modulo \(12\)); each undirected edge appears once. For vertices \(x,y,z\), say that \(z\) **strongly resolves** the unordered pair \(\{x,y\}\) if
\[
d(z,x)=d(z,y)+d(x,y)\quad\text{or}\quad d(z,y)=d(z,x)+d(x,y).
\]
A strong resolving set contains a strongly resolving vertex for every distinct pair, and a strong metric basis is a strong resolving set of least cardinality. Two distinct vertices are **mutually maximally distant** (MMD) if each is at least as far from the other as each of its graph neighbors is. The strong resolving graph has vertex set \(V(G)\) and exactly the MMD pairs as edges. Token jumping changes one occupied vertex to a different unoccupied vertex and requires the new set also to be a minimum strong metric basis; no adjacency condition is placed on the exchanged vertices in \(G\).

## Proof

**1. Exact MMD structure.** Distances from \(u_0\) have shells
\[
\begin{array}{c|l}
0&u_0\\
1&u_1,u_{11},v_0\\
2&u_2,u_{10},v_1,v_5,v_7,v_{11}\\
3&u_3,u_5,u_7,u_9,v_2,v_4,v_6,v_8,v_{10}\\
4&u_4,u_6,u_8,v_3,v_9
\end{array}
\]
(the shell profile is \((1,3,6,9,5)\)). The supplied exhaustive distance computation verifies this same profile at all \(24\) roots and checks, directly from the definition, that the \(60\) MMD pairs are **exactly** pairs at distance \(4\). It also verifies the following complete row/column description, using the labels \(0,\ldots,11\) for \(u_i\) and \(12,\ldots,23\) for \(v_i\). One component has its four rows
\[
(0,4,8),\ (2,6,10),\ (13,17,21),\ (15,19,23)
\]
and its three columns
\[
(0,6,15,21),\ (2,8,17,23),\ (4,10,13,19).
\]
Every row intersects every column in one vertex; two vertices within this component are MMD exactly when they lie in a common row or column. The other component is obtained by increasing all indices modulo \(12\), preserving the \(u/v\) label. This exhibits \(2(K_4\square K_3)\). The finite checks reconstruct all graph edges and MMD pairs directly; no graph-database identification is assumed.

**2. Minimum bases and counting.** Every strong resolving set intersects every MMD pair: if \(x,y\) are MMD, a third vertex cannot strongly resolve them (otherwise one shortest path endpoint extension would contradict maximality). Therefore each strong resolving set is a vertex cover of the displayed rook-graph union. In each \(K_4\square K_3\), an independent set contains at most one vertex from each column and from each row, so at most \(3\) vertices. This bound is achieved by choosing three distinct rows, assigned bijectively to the three columns. Its exact count is \(4\cdot3\cdot2=24\). Hence any strong resolving set has at least \(24-(3+3)=18\) vertices. The explicit independent-triple complements furnish \(24^2=576\) size-\(18\) candidates. Direct exhaustive shortest-path verification confirms that **every one** strongly resolves all \(\binom{24}{2}=276\) original vertex pairs, giving equality and a complete description of all minima. This direct verification also supplies sufficiency without relying on an unproved implication about MMD covers.

**3. Exact exchange graph.** A basis is the complement of one independent triple in each rook component. Represent a triple in one component by a permutation \((h,r_1,r_2,r_3)\) of the four row labels: \(h\) is the unused row and \(r_j\) is the selected row in column \(j\). Replacing precisely one selected vertex while maintaining an independent triple must replace its selected row \(r_j\) by the unused row \(h\). Thus the permutation changes by swapping its first entry with exactly one of its other three entries. Conversely, each such swap yields a legal exchange. The one-component move graph is therefore the \(24\)-vertex star-transposition graph on \(S_4\). This graph is explicitly isomorphic to \(G\): number the \(S_4\) permutations lexicographically from \(0\) to \(23\), and map the original vertices \((u_0,\ldots,u_{11},v_0,\ldots,v_{11})\) to indices
\[
(0,6,12,18,4,10,16,22,3,9,15,21,14,19,2,7,17,20,5,8,13,23,1,11).
\]
The supplied isomorphism program checks the complete edge sets under this bijection. A one-vertex basis exchange can alter only one of the two independent triples; hence the full exchange graph is the Cartesian product of the two one-component move graphs, proving \(\mathcal R_{\mathrm{sdim}}(G)\cong G\square G\).

**4. Distances.** Each \(G\) factor has diameter \(4\), with distance distribution \((1,3,6,9,5)\) from every vertex. Cartesian-product distances add. Squaring the associated generating polynomial gives
\[
(1+3z+6z^2+9z^3+5z^4)^2
=1+6z+21z^2+54z^3+100z^4+138z^5+141z^6+90z^7+25z^8.
\]
Thus the product has radius and diameter \(8\). Independently, the supplied direct reconfiguration verifier recomputes all shortest-path histograms from all \(576\) bases.

## Verification

The accompanying standalone Python programs require only Python's standard library and read no downloaded data. Run them from their containing directory using `python3 verify_structure.py`, `python3 verify_reconfiguration.py`, and `python3 verify_product.py`. They deterministically regenerate the corresponding `structural_certificate.json`, `bases_certificate.json`, and `product_isomorphism.json` and print their SHA-256 hashes. `verify_structure.py` checks all graph distances and \(60\) MMD pairs, `verify_reconfiguration.py` independently enumerates all \(576\) bases and all \(1728\) exchanges, directly tests strong resolution of each of the \(276\) pairs for every base, and computes \(576\) all-source distance histograms. `verify_product.py` verifies an explicit \(24\)-vertex Cayley-star isomorphism and all ordered basis-pair exchange comparisons. Full finite certificates and output logs are supplied for byte-identical replay.

## Relationship to prior work

Oellermann and Peters-Fransen (2007) established the strong resolving graph / minimum vertex-cover paradigm. Kratica, Kovačević-Vujčić, and Čangalović (arXiv:1507.00881, first submitted July 3, 2015) studied the strong metric dimension of the **different family** \(\operatorname{GP}(n,2)\). Their general definitions and bounds do not yield the \(\operatorname{GP}(12,5)\) decomposition or the complete exchange-graph identity here. The isomorphism between the Nauru graph and the four-permutation star graph is known; what is established here is the identification of that star graph as the **exchange graph of minimum strong metric bases within each** MMD rook component and the consequent self-product reconfiguration structure.

## Limitations

The proof concerns only the specified \(24\)-vertex graph and the defined token-jump move. It does not assert analogous identities for all generalized Petersen graphs, nor mobility results for nonminimum strong resolving sets or adjacent-token slides. The finite calculations are exhaustive for this finite graph but do not establish publication priority. The accessible literature and mathematical-record searches did not reveal the combined statement; unindexed work or unpublished computations could overlap. Independent external scientific audit has not been performed.

## References

1. O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, Discrete Applied Mathematics 155 (2007), 356–364, https://doi.org/10.1016/j.dam.2006.06.009 .
2. J. Kratica, V. Kovačević-Vujčić, and M. Čangalović, *The strong metric dimension of some generalized Petersen graphs*, arXiv:1507.00881v1 (July 3, 2015), https://arxiv.org/abs/1507.00881 .
3. E. W. Weisstein, *Nauru Graph*, MathWorld, https://mathworld.wolfram.com/NauruGraph.html (records the previously known identification with the permutation star graph of order four).
4. The accessible full primary text for reference 2 treats \(\operatorname{GP}(n,2)\) in its main theorem, rather than \(\operatorname{GP}(12,5)\).
