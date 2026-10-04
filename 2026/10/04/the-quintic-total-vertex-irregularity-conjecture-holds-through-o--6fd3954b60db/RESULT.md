# The quintic total-vertex-irregularity conjecture holds through order ten
## Finding
For every finite simple 5-regular graph \(G\) on at most ten vertices, \(\operatorname{tvs}(G)=\lceil(|V(G)|+5)/6\rceil\). Equivalently, \(\operatorname{tvs}(K_6)=2\), and every 5-regular graph of order \(8\) or \(10\) has total vertex irregularity strength \(3\). Consequently, any counterexample to the regular-graph total-vertex-irregularity conjecture in degree \(5\) has at least \(12\) vertices.

## Assumptions and scope
All graphs are finite, simple, and undirected. A total \(k\)-labeling assigns each vertex and edge a label in \(\{1,\ldots,k\}\); the weight of a vertex is its own label plus the labels of its incident edges. The total vertex irregularity strength \(\operatorname{tvs}(G)\) is the least \(k\) for which all vertex weights are distinct. The result concerns only 5-regular graphs of orders at most ten. By the handshaking lemma, such orders are even, and simplicity forces the order to be at least six, so the only orders in scope are \(6,8,10\).

## Proof
For a 5-regular graph on \(n\) vertices, every total \(k\)-labeling gives vertex weights in the integer interval from \(6\) to \(6k\). Hence \(6k-5\ge n\), and therefore
\[
\operatorname{tvs}(G)\ge \left\lceil\frac{n+5}{6}\right\rceil.
\]

We use the spanning-subgraph criterion proved in the 2026 paper of Shan and Zhong. Put \(s=\lceil(n+5)/6\rceil\) and \(r=s-1\). If \(G\) has a spanning subgraph \(H\) for which every \(H\)-degree class has size at most \(r\), except possibly one class of size \(r+1\), then label the edges of \(H\) by \(s\) and all other edges by \(1\). Vertices of \(H\)-degree \(i\) then have incident-edge sum \(5+ir\), so their possible total weights form
\[
I_i=[6+ir,\,6+(i+1)r].
\]
Consecutive intervals meet at one endpoint. Ordering each degree class, assign consecutive vertex labels beginning at \(1\) through the exceptional class and beginning at \(2\) after it. A nonexceptional class omits the endpoint shared with the next or previous class, while the exceptional class may use both endpoints. Thus all vertex weights are distinct and all labels lie in \(\{1,\ldots,s\}\).

For \(n=8\) and \(n=10\), we have \(s=3\) and \(r=2\). The exhaustive certificate checker `verify.py` enumerates every graph in these two orders after a symmetry normalization. If \(G\) is 5-regular, its complement is respectively 2-regular or 4-regular. Relabeling permits the complement-neighborhood of vertex \(0\) to be fixed as \(\{1,2\}\) for order eight and \(\{1,2,3,4\}\) for order ten. The checker recursively enumerates all simple completions of the residual degree sequence, using only the Erdős--Gallai inequalities as a pruning condition. It obtains exactly \(167\) fixed-neighborhood completions at order eight and \(527481\) at order ten. Every 5-regular graph of the corresponding order is isomorphic to at least one enumerated completion.

For each enumerated graph, the supplied certificate masks define a spanning subgraph \(H=G\cap F\). The checker verifies directly that each \(H\)-degree class has size at most \(2\), with at most one class of size \(3\), constructs the vertex labels by the interval rule above, and recomputes every total weight from the selected edge labels. All completions pass. Therefore every 5-regular graph of order eight or ten has a vertex irregular total 3-labeling, and the lower bound makes \(3\) exact.

For \(n=6\), the only 5-regular simple graph is \(K_6\). Number its vertices \(0,1,2,3,4,5\). Give label \(2\) to the six edges \(01,02,03,04,12,13\), label \(1\) to every other edge, and give vertex labels \(2,2,1,2,1,1\). The resulting weights are \(11,10,8,9,7,6\), all distinct. Hence \(\operatorname{tvs}(K_6)=2\).

Combining the three admissible orders proves the claim. Since a 5-regular simple graph has even order, any degree-five counterexample must therefore have order at least \(12\).

## Verification
Run `python3 verify.py` in the same directory as `cert8.json` and `cert10.json`. The checker uses only the Python standard library. It verifies the explicit \(K_6\) labeling, exhaustively regenerates the two normalized complement censuses, checks their exact completion counts, verifies every certificate subgraph, constructs the resulting total labels, and recomputes all vertex weights. The stored replay output is in `verification_output.txt`.

## Relationship to prior work
Shan and Zhong introduced the present degree-five gap explicitly in their September 2026 paper: they prove the regular conjecture for degrees \(3\) and \(4\), prove it for every fixed degree only when the order is sufficiently large, and state that for every fixed \(d\ge5\) the unrestricted-order problem remains open. Their proof of the asymptotic theorem also supplies the spanning-subgraph criterion used here. The present result does not improve their asymptotic theorem; it supplies an exact finite cutoff for the first unresolved regular degree, showing that a degree-five counterexample cannot occur before order twelve.

Earlier work on dense graphs gives general upper bounds for total vertex irregularity strength, not this exact all-quintic classification at orders eight and ten. The complete graph case at order six is classical coverage and is included only to make the cutoff statement complete.

## Limitations
No claim is made for 5-regular graphs of order at least twelve, nor for regular degree at least six. The finite proof at orders eight and ten is computational, although the enumeration and the labeling verification are exact and use integer arithmetic only. The certificate masks are not asserted to be minimal or canonical. Bibliographic searches cannot establish absolute novelty; a nonindexed specialized source could still contain an equivalent small-order result.

## References
1. S. Shan and Y. Zhong, “Total Vertex Irregularity Strength of Cubic and 4-Regular Graphs,” arXiv:2609.30114v1, first public 24 September 2026. See in particular the proof of Theorem 4.2 and Conjecture 4.3.
2. P. Majerski and J. Przybyło, “Total Vertex Irregularity Strength of Dense Graphs,” Journal of Graph Theory 76 (2014), 34–41, DOI 10.1002/jgt.21748.
