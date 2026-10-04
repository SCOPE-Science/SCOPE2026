# A single adjacent reversal contracts the cyclic tournament flag complex
## Finding
For every odd integer \(n=2m+1\ge 3\), define the cyclic tournament \(R_n\) on \(\mathbb Z/n\mathbb Z\) by
\[
i\to j\quad\Longleftrightarrow\quad 1\le (j-i)\bmod n\le m.
\]
Let \(R_n^{\mathrm{rev}}\) be obtained by reversing only the edge \(0\to1\). Then
\[
\operatorname{dFl}(R_n^{\mathrm{rev}})\simeq *.
\]
More precisely, if \(K=\operatorname{dFl}(R_n)\), then \(K=\mathcal N(n,m)\), and
\[
\operatorname{dFl}(R_n^{\mathrm{rev}})=K\cup \tau,
\qquad \tau=\{0,1,m+1\}.
\]
Thus the reversal adds exactly one 2-simplex and removes no simplex. Its boundary \(\partial\tau\hookrightarrow K\) is a homotopy equivalence, so filling that boundary makes the whole directed flag complex contractible.

## Assumptions and scope
A tournament has exactly one directed edge between each pair of distinct vertices. The directed flag complex \(\operatorname{dFl}(T)\) of a tournament \(T\) is the ordinary simplicial complex whose simplices are the vertex sets inducing transitive subtournaments. The statement concerns every odd \(n\ge3\), with no probabilistic or genericity assumption.

The notation \(\mathcal N(n,m)\) is the evenly spaced circular-arc nerve: its maximal simplices are the cyclic blocks
\[
B_a=\{a,a+1,\ldots,a+m\}\subset \mathbb Z/n\mathbb Z.
\]
All index arithmetic is modulo \(n\).

## Proof
First identify \(K=\operatorname{dFl}(R_n)\). Every block \(B_a\) is transitive in the cyclic order \(a,a+1,\ldots,a+m\), so every face of \(\mathcal N(n,m)\) is in \(K\). Conversely, if \(S\) is a transitive subtournament of \(R_n\), let \(v\) be its source. Every other vertex of \(S\) is an out-neighbor of \(v\), hence lies among \(v+1,\ldots,v+m\). Therefore \(S\subseteq B_v\). This proves \(K=\mathcal N(n,m)\).

Now reverse \(0\to1\). A face not containing both \(0\) and \(1\) is unchanged. If an old transitive face contains both, it lies in some block \(B_a\) where \(0\) and \(1\) are consecutive in the block's total order. Reversing their mutual edge merely swaps these adjacent entries; every other vertex of the block is before both or after both. Hence no old face is lost.

A genuinely new face must contain \(0\) and \(1\). In \(R_n\), the only vertex \(v\) for which \(\{0,1,v\}\) is a directed 3-cycle is \(v=m+1\): for \(2\le v\le m\), both \(0\) and \(1\) point to \(v\), while for \(m+2\le v\le2m\), \(v\) points to both. Thus the reversal makes exactly the triple \(\tau=\{0,1,m+1\}\) transitive. No larger new face can contain \(\tau\). Indeed, for \(2\le w\le m\), the unchanged triple \(\{0,w,m+1\}\) is the directed cycle \(0\to w\to m+1\to0\); for \(m+2\le w\le2m\), the unchanged triple \(\{1,m+1,w\}\) is the directed cycle \(1\to m+1\to w\to1\). Hence
\[
\operatorname{dFl}(R_n^{\mathrm{rev}})=K\cup\tau.
\]

It remains to identify the attaching loop. Realize \(K=\mathcal N(n,m)\) as the nerve of the circular arcs
\[
A_i=\left[\frac{i}{n},\frac{i+m}{n}\right]_{S^1}.
\]
Since \(m<n/2\), every nonempty finite intersection of these arcs is contractible. The three arcs \(A_0,A_1,A_{m+1}\) already cover \(S^1\): after cutting at \(0=1\), their union is
\[
[0,m/n]\cup[1/n,(m+1)/n]\cup[(m+1)/n,1].
\]
They intersect pairwise but have empty triple intersection, so their nerve is exactly \(\partial\tau\). By the natural form of the nerve theorem for inclusion of a good subcover that covers the same space, the inclusion \(\partial\tau\hookrightarrow K\) is a homotopy equivalence. Simplicial inclusions are cofibrations, so the pushout \(K\cup_{\partial\tau}\tau\) is also the homotopy pushout. Replacing \(K\) by the homotopy-equivalent \(\partial\tau\) identifies this homotopy pushout with the 2-simplex \(\tau\), which is contractible. Therefore \(\operatorname{dFl}(R_n^{\mathrm{rev}})\) is contractible for every odd \(n\ge3\).

## Verification
The accompanying verifier independently reconstructs the tournaments and their directed flag complexes for every odd \(3\le n\le17\). For each such \(n\), it checks that the reversed complex differs from the original by exactly the single triangle \(\{0,1,m+1\}\), verifies the cyclic-block description of every original simplex, and computes mod-2 boundary ranks. In every tested case the reversed complex has Betti vector \((1,0,\ldots,0)\). The finite computation is a regression check; the proof above, not the finite range, establishes the all-\(n\) statement.

Run:
`python3 verify_edge_reversal.py`

A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Govc defines directed flag complexes of tournaments and classifies regular tournaments through 13 vertices. In that census, the unique regular example with circle homotopy agrees with \(\mathcal N(n,(n-1)/2)\), and the paper notes that this complex collapses onto a circle. The present statement instead changes one adjacent tournament outcome and proves, uniformly for every odd order, that this single reversal adds exactly one triangle whose boundary carries the entire circle homotopy, making the complex contractible.

Adamaszek, Adams, Frick, Peterson, and Previte-Johnson define \(\mathcal N(n,k)\) as the nerve of evenly spaced circular arcs and prove \(\mathcal N(n,k)\simeq S^1\) when \(1\le k<n/2\). Their work supplies the circular-arc model used in the proof but does not involve tournament edge reversals.

A later study of sectionable tournaments develops discrete-Morse descriptions around simply disconnected tournaments. Its readily accessible abstract and introductory material are close enough in terminology to remain an originality risk; the full institutional copy was not accessible during this check. No accessible statement located there asserted the one-edge reversal theorem above.

## Limitations
The theorem concerns the specific adjacent edge \(0\to1\) in the cyclic tournament. Cyclic symmetry gives the same conclusion for any translate \(i\to i+1\), but no claim is made for reversing arbitrary longer cyclic edges or several edges. The finite verifier checks only \(n\le17\) and mod-2 homology; it is supplemental to the structural homotopy proof. Literature searching cannot prove absolute novelty, and inaccessible older tournament-topology sources remain a residual originality risk.

## References
1. Dejan Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333v1, 9 June 2020. Primary MSC 55-08.
2. Michał Adamaszek, Henry Adams, Florian Frick, Chris Peterson, Corrine Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336v1, 16 October 2014; Discrete & Computational Geometry 56 (2016/2017), 251-273.
3. Zakir Deniz, *Sectionable Tournaments: Their topology and Coloring*, arXiv:2104.05839; later version dated 20 December 2022.
