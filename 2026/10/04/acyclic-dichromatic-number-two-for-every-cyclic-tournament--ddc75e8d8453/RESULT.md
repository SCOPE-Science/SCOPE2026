# Acyclic dichromatic number two for every cyclic tournament
## Finding
For every integer \(m\ge 1\), let \(T_{2m+1}\) be the cyclic tournament on \(\mathbb Z_{2m+1}\) in which \(i\to j\) exactly when the residue \(j-i\pmod{2m+1}\) lies in \(\{1,\ldots,m\}\). Then
\[
\vec{\chi}_a(T_{2m+1})=2.
\]
Here an acyclic dicolouring means a vertex partition for which every colour class induces an acyclic digraph and every bipartite subdigraph between two colour classes is acyclic.

## Assumptions and scope
The theorem concerns the standard cyclic tournament of every odd order at least three. It is stronger than the ordinary statement that this tournament has dichromatic number two, because acyclic dicolouring also forbids alternating directed cycles between distinct colour classes.

## Proof
Write \(A=\{a_0,\ldots,a_m\}\) with \(a_i=i\), and \(B=\{b_0,\ldots,b_{m-1}\}\) with \(b_j=m+1+j\). Inside \(A\), if \(i<j\) then \(1\le j-i\le m\), so \(a_i\to a_j\); hence \(T_{2m+1}[A]\) is transitive in increasing order. Inside \(B\), the same difference calculation shows that \(b_i\to b_j\) for \(i<j\), so \(T_{2m+1}[B]\) is also transitive.

For a cross pair \(a_i,b_j\), one has \(a_i\to b_j\) exactly when
\[
1\le m+1+j-i\le m,
\]
which is equivalent to \(i\ge j+1\). Thus \(b_j\to a_i\) exactly when \(i\le j\). Consequently every cross arc points forward in the linear order
\[
a_m,b_{m-1},a_{m-1},b_{m-2},\ldots,a_1,b_0,a_0.
\]
Therefore the bipartite subdigraph \(T_{2m+1}[A,B]\) is acyclic. The two sets \(A,B\) are hence an acyclic two-dicolouring.

Finally, \(0\to m\), \(m\to2m\), and \(2m\to0\), because the corresponding forward residues are \(m,m,1\). Thus \(T_{2m+1}\) is not acyclic, so one colour is impossible. This proves \(\vec{\chi}_a(T_{2m+1})=2\).

## Verification
The included verifier constructs the tournament from the defining residue rule, checks the displayed two colour classes and the displayed cross-part topological order, and checks the explicit directed triangle for every \(1\le m\le200\). It is a finite stress test only; the universal statement follows from the proof above.

## Relationship to prior work
Liu, Yang, and Zhang define the same acyclic dichromatic number and determine the first critical orders \(m(3)=5\) and \(m(4)=7\). Their appendix observes the order-five cyclic tournament as an acyclic two-dicolourable case, but does not state or prove the all-orders cyclic-tournament formula. Bang-Jensen, Picasarri-Arrieta, and Yeo introduced the parameter and showed that acyclic dichromatic number can exceed ordinary dichromatic number by an arbitrarily large amount even among tournaments of ordinary dichromatic number two, so ordinary two-dicolourability does not imply this theorem. Javier and Llano study ordinary dichromatic numbers of cyclic and one-jump-reversed circulant tournaments; those ordinary results do not control the extra bichromatic acyclicity condition proved here.

## Limitations
The proof uses the consecutive-jump set \(\{1,\ldots,m\}\) essentially. It does not claim that arbitrary circulant tournaments, or the one-jump-reversed families studied for ordinary dichromatic number, have acyclic dichromatic number two.

## References
1. Y. Liu, Z. Yang, Y. Zhang, *Acyclic Dicolourings of Oriented Graphs: Paths, Random Tournaments, and Critical Orders*, arXiv:2609.22931, 2026.
2. J. Bang-Jensen, L. Picasarri-Arrieta, A. Yeo, *Acyclic dichromatic number of oriented graphs*, arXiv:2511.20246, 2025.
3. N. Javier, B. Llano, *The dichromatic number of infinite families of circulant tournaments*, Discussiones Mathematicae Graph Theory 37 (2017), 221–238, doi:10.7151/dmgt.1930.
