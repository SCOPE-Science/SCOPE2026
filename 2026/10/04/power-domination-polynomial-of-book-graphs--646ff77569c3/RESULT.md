# Power domination polynomial of book graphs
## Finding
For every integer \(r\ge2\), let \(B_r\) be the book graph formed from \(r\) copies of \(C_4\) sharing one common edge \(xy\); write the two non-spine vertices on page \(i\) as \(a_i,b_i\). A set \(S\subseteq V(B_r)\) is power dominating exactly when either \(S\cap\{x,y\}\ne\varnothing\), or \(S\) meets at least \(r-1\) of the page pairs \(\{a_i,b_i\}\). Consequently, with \(q(x)=x(x+2)=(1+x)^2-1\), \[\mathcal P(B_r;x)=q(x)(1+x)^{2r}+q(x)^r+r q(x)^{r-1}.\] Hence the total number of power dominating sets is \[\mathcal P(B_r;1)=3\cdot4^r+(r+3)3^{r-1}.\] Also \(\gamma_P(B_r)=1\); for \(r\ge3\) the only minimum power dominating sets are \(\{x\}\) and \(\{y\}\), while for \(r=2\) every singleton is power dominating.

## Assumptions and scope
All graphs are finite, simple, and undirected. For \(r\ge2\), let \(B_r\) be the book graph obtained by bonding \(r\) copies of \(C_4\) along one common edge \(xy\). On page \(i\), write the remaining two vertices as \(a_i,b_i\), with cycle
\[
x a_i b_i y x.
\]

A set \(S\subseteq V(G)\) is power dominating if the domination step colors \(N[S]\), after which repeated zero-forcing steps color every remaining vertex.

## Proof
If \(x\in S\), then after the domination step the vertices \(x,y,a_1,\ldots,a_r\) are colored. Each \(a_i\) then has at most one uncolored neighbor, namely \(b_i\), so the pages are forced one by one. The same argument applies when \(y\in S\). Thus every set meeting the spine \(\{x,y\}\) is power dominating.

Now assume \(S\cap\{x,y\}=\varnothing\). Call page \(i\) touched when \(S\cap\{a_i,b_i\}\ne\varnothing\).

If every page is touched, then the domination step colors both internal vertices of every page. At least one of \(x,y\) is colored immediately; if the other is not, an already colored internal page vertex has it as a unique uncolored neighbor and forces it. Hence the graph is fully colored.

If exactly one page \(j\) is untouched, then after the domination step and, if necessary, one force across a touched page, both spine vertices are colored and every touched page is fully colored. The only uncolored vertices are \(a_j,b_j\). Since \(x\) then has \(a_j\) as its unique uncolored neighbor, it forces \(a_j\), which in turn forces \(b_j\). Thus such a set is power dominating.

Conversely, suppose at least two pages \(i,j\) are untouched. After the domination step, both vertices on each untouched page remain uncolored. Even if both spine vertices are colored, \(x\) has at least the two uncolored neighbors \(a_i,a_j\), and \(y\) has at least the two uncolored neighbors \(b_i,b_j\). No forcing step can enter an untouched page, so the process stalls. Therefore a spine-free set is power dominating exactly when at most one page is untouched.

For enumeration, sets meeting the spine contribute
\[
\big((1+x)^2-1\big)(1+x)^{2r}
=
q(x)(1+x)^{2r}.
\]
A spine-free set touching every page contributes
\[
q(x)^r,
\]
because each page contributes one nonempty subset of its two internal vertices. A spine-free set touching exactly \(r-1\) pages contributes
\[
r q(x)^{r-1},
\]
since the unique untouched page can be chosen in \(r\) ways. These classes are disjoint, giving
\[
\mathcal P(B_r;x)=q(x)(1+x)^{2r}+q(x)^r+r q(x)^{r-1}.
\]

At \(x=1\), this becomes
\[
3\cdot4^r+(r+3)3^{r-1}.
\]
The degree-one coefficient is \(6\) when \(r=2\), and \(2\) when \(r\ge3\), yielding the stated minimum-set classification.

## Verification
The included checker constructs \(B_r\) directly for every \(2\le r\le8\), enumerates every vertex subset, applies the domination step and then the forcing rule exactly, and compares the outcome with the page-intersection characterization above.

It also computes every coefficient independently from the structural formula and checks the total number of power dominating sets and the minimum-set count.

## Relationship to prior work
The 2018 paper introducing the power domination polynomial defines the invariant, develops structural and decomposition results, and computes it for several standard graph families. Targeted full-text searches of the accessible primary text found no book-graph treatment.

A 2025 paper on domination and power-domination entropies explicitly defines the \(r\)-book graph, but its book-graph section concerns domination entropy. Its power-domination-polynomial section lists complete, path, cycle, wheel, star, windmill, friendship, double-fan, cone, and fan families, not book graphs. The same paper concludes by suggesting derivation of domination and power domination polynomials for further similar graph structures.

## Limitations
The theorem covers \(r\ge2\). The boundary case \(B_1=C_4\) has
\[
\mathcal P(B_1;x)=(1+x)^4-1.
\]
No claim is made for triangular books or books whose pages are longer cycles. The finite exhaustive verification is corroborative only; the all-\(r\) theorem follows from the proof.

## References
1. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, “Power domination polynomials of graphs,” arXiv:1805.10984v1, 28 May 2018.
2. K. Geethu, A. Parthiban, “On Graph Entropy Measures Based on the Number of Dominating and Power Dominating Sets,” Malaysian Journal of Mathematical Sciences 19(1) (2025), 269–287, DOI 10.47836/mjms.19.1.14.
