# Edge-version metric and double metric bases of friendship graphs
## Finding
For every integer \(r\ge2\), let \(F_r\) be the friendship graph formed from \(r\) triangles sharing one common center \(c\). On page \(i\), write
\[
x_i=ca_i,\qquad y_i=cb_i,\qquad z_i=a_ib_i.
\]
Then
\[
\dim_E(F_r)=2r-1
\]
for the edge-version metric dimension and
\[
\psi_E(F_r)=2r
\]
for the edge-version doubly resolving number.

Moreover, the edge-version metric bases are exactly the sets that choose two edges from every page except one page, on which they choose exactly one of the two center-incident edges. Their number is
\[
2r\,3^{r-1}.
\]

The minimum edge-version doubly resolving sets are exactly the sets that choose two of the three edges from every page. Their number is
\[
3^r.
\]

Thus this family realizes the strict relation
\[
\dim_E(F_r)<\psi_E(F_r)
\]
with a constant gap of one for every \(r\ge2\).

## Assumptions and scope
All graphs are finite, simple, and connected. Edge distance means graph distance in the line graph. Thus the edge-version metric dimension of a graph \(G\) is the ordinary metric dimension of \(L(G)\), with landmarks corresponding to edges of \(G\). Similarly, an edge set \(D\) is edge-version doubly resolving when, for every distinct edges \(e,f\), the difference vector
\[
\bigl(d_E(e,d)-d_E(f,d):d\in D\bigr)
\]
is not constant.

For \(F_r\), the line graph has vertices
\[
x_1,y_1,z_1,\ldots,x_r,y_r,z_r.
\]
All \(2r\) spoke vertices \(x_i,y_i\) form a clique. Each \(z_i\) is adjacent exactly to \(x_i\) and \(y_i\). Hence
\[
d_E(z_i,x_i)=d_E(z_i,y_i)=1,
\]
\[
d_E(z_i,s)=2
\]
for every spoke \(s\) from a different page, and
\[
d_E(z_i,z_j)=3
\]
for \(i\ne j\).

## Proof
First consider ordinary edge-version resolving sets.

For every page \(i\), the two spoke vertices \(x_i,y_i\) have equal distance to every vertex of the line graph outside \(\{x_i,y_i\}\). Therefore any resolving set must contain at least one of \(x_i,y_i\).

Suppose two distinct pages \(i,j\) each contribute only one landmark. On either such page the unique landmark must be a spoke, because choosing only \(z_i\) would leave \(x_i,y_i\) unresolved. Let the chosen spokes be \(x_i,x_j\), after relabeling within pages. Then the unchosen spokes \(y_i,y_j\) have identical distance to every landmark: distance \(1\) to every selected spoke, and distance \(2\) to every selected rim edge on a third page. Thus at most one page can contribute only one landmark. Every other page contributes at least two, giving
\[
|D|\ge1+2(r-1)=2r-1.
\]

Now choose an exceptional page \(i\), choose exactly one of \(x_i,y_i\), and choose any two edges on every other page. This set resolves \(L(F_r)\). Two selected edges are separated by their zero coordinates. It remains only to compare omitted edges. A full page from which a spoke is omitted contains the other spoke and the rim edge as landmarks, and these distinguish that omitted spoke from every vertex on another page. A full page from which the rim edge is omitted contains both spokes; its omitted rim has distance \(1\) to them, whereas a rim on another page has distance \(2\), and any omitted spoke on another page is distinguished on its own page. Finally, on the exceptional page the omitted spoke and omitted rim have equal distance \(1\) to the single local landmark, but any full page distinguishes them: at a selected spoke their distances are \(1\) and \(2\), while at a selected rim they are \(2\) and \(3\). Hence every such set is resolving.

There are \(r\) choices of exceptional page, \(2\) choices of its selected spoke, and \(3\) choices of the omitted edge on each of the other \(r-1\) pages. Therefore
\[
\dim_E(F_r)=2r-1
\]
and the number of metric bases is
\[
2r\,3^{r-1}.
\]

Now consider edge-version doubly resolving sets. Fix a page \(i\). If a candidate set contains neither \(x_i\) nor \(y_i\), then \(x_i,y_i\) have identical distance to every landmark and are not even resolved. If the page contributes exactly one edge and that edge is a spoke, say \(x_i\), then the pair \(x_i,z_i\) is not doubly resolved: for the landmark \(x_i\),
\[
d_E(x_i,x_i)-d_E(z_i,x_i)=-1,
\]
and for every landmark outside page \(i\), the same difference is again \(-1\). Therefore every doubly resolving set contains at least two edges from each page, so
\[
\psi_E(F_r)\ge2r.
\]

Conversely, let \(D\) choose exactly two edges from every page. We verify that every pair is doubly resolved.

If both edges under comparison lie in \(D\), using the two edges themselves gives opposite nonzero distance differences. If \(u\in D\) and \(v\notin D\) lie on the same page, the landmark \(u\) gives difference \(-1\), while the other selected edge of that page gives difference \(0\). If \(u\in D\) and \(v\notin D\) lie on different pages, compare the landmark \(u\) with a selected spoke on the page of \(v\); the corresponding distance differences are distinct.

It remains to compare two omitted edges on different pages. If one omitted edge is a spoke, then on its page the selected spoke and selected rim give two different distance differences against the other omitted edge. If both omitted edges are rims, the two selected spokes on the first page give difference \(-1\), while the selected spokes on the second page give difference \(1\). Hence \(D\) is doubly resolving.

Thus
\[
\psi_E(F_r)=2r.
\]
A minimum set omits exactly one edge from every page, independently, so there are
\[
3^r
\]
minimum edge-version doubly resolving sets.

## Verification
The included verifier constructs the friendship graph, builds its line graph, computes all edge distances by breadth-first search, and tests the two definitions directly.

For every \(2\le r\le6\), it exhaustively checks every smaller landmark set, every candidate edge-version metric basis of size \(2r-1\), and every candidate edge-version doubly resolving basis of size \(2r\). It then compares the complete minimum-set families with the two structural classifications above.

## Relationship to prior work
The edge-version doubly resolving framework was made public in 2018 and later published with exact results for sunlet and prism families. Its inspected full text defines the same line-graph distance model and contains no friendship or windmill treatment.

A 2024 continuation studies the same edge-based doubly resolving notion on the circulant networks \(C_n(1,2)\) and lists MSC 05C12. Its inspected full text contains no friendship or windmill theorem.

There is also a 2019 theorem giving a quantity called the edge metric dimension of friendship graphs. That paper uses the different, now standard edge-metric model in which vertices are landmarks resolving edges. The present \(\dim_E\) instead uses edges as landmarks and is the metric dimension of the line graph, exactly as in the edge-version doubly resolving literature. Therefore the 2019 value does not imply either theorem here.

## Limitations
The theorem is for friendship graphs with at least two triangular pages. It does not determine the corresponding parameters for generalized windmills with larger clique blades, Dutch windmills, or other wheel-related families. The exhaustive computation is corroborative only; the all-\(r\) result follows from the line-graph proof.

## References
1. M. Ahmad, Z. Zahid, S. Zafar, “On minimal edge version of doubly resolving sets of a graph,” arXiv:1807.02365v1, 6 July 2018; Journal of Combinatorial Mathematics and Combinatorial Computing 119 (2024), 175–184, DOI 10.61091/jcmcc119-18.
2. R. Nasir, M. Ahmad, Z. Zahid, S. A. Bajri, H. A. E.-W. Khalifa, “Characterizing edge-based doubly resolving sets within circulant networks \(C_n(1,2)\),” AIMS Mathematics 9(6) (2024), 15857–15874, DOI 10.3934/math.2024766.
3. B. Yang, M. Rafiullah, H. M. A. Siddiqui, S. Ahmad, “On resolvability parameters of some wheel-related graphs,” Journal of Chemistry (2019), Article 9259032, DOI 10.1155/2019/9259032.
