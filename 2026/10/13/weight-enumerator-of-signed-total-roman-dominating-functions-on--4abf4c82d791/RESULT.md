# Weight enumerator of signed total Roman dominating functions on complete multipartite graphs

## Finding

Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a connected complete multipartite graph with
\[
r\ge2.
\]
For a labeling
\[
f:V(G)\to\{-1,1,2\},
\]
let
\[
a_i=\bigl|\{v\in V_i:f(v)=-1\}\bigr|,
\]
\[
b_i=\bigl|\{v\in V_i:f(v)=1\}\bigr|,
\]
\[
c_i=\bigl|\{v\in V_i:f(v)=2\}\bigr|.
\]
Write
\[
s_i=-a_i+b_i+2c_i,
\qquad
W=\sum_{i=1}^r s_i,
\qquad
C=\sum_{i=1}^r c_i.
\]

Then \(f\) is a signed total Roman dominating function if and only if
\[
\boxed{
W-s_i\ge1
\quad\text{for every }i
}
\]
and
\[
\boxed{
a_i>0\Longrightarrow C-c_i\ge1
\quad\text{for every }i.
}
\]

Thus signed total Roman feasibility on a complete multipartite graph depends only on the three label counts in each part.

Define the weight enumerator
\[
\mathcal R_{stR}(G;x)
=
\sum_{f\text{ STRD}}x^{\omega(f)}.
\]
Then
\[
\boxed{
\mathcal R_{stR}(G;x)=
\sum_{\substack{
a_i+b_i+c_i=n_i\\
W-s_i\ge1\ \forall i\\
a_i>0\Rightarrow C-c_i\ge1\ \forall i
}}
\left(
\prod_{i=1}^r
\binom{n_i}{a_i,b_i,c_i}
\right)x^W.
}
\]

Every exponent appearing in this polynomial is at least \(2\). Its least exponent is the signed total Roman domination number, and the coefficient of that least exponent counts all minimum-weight signed total Roman dominating functions.

## Assumptions and scope

All graphs are finite, simple, undirected, and connected. A signed total Roman dominating function is a map
\[
f:V(G)\to\{-1,1,2\}
\]
such that every vertex \(v\) satisfies
\[
\sum_{u\in N(v)}f(u)\ge1,
\]
and every vertex labeled \(-1\) has a neighbor labeled \(2\).

The theorem classifies and enumerates all such functions on arbitrary connected complete multipartite graphs. It does not address signed total Roman domatic families, whose feasibility imposes additional coordinatewise constraints between several functions.

## Proof

Fix a part \(V_i\). Every vertex of \(V_i\) is adjacent to every vertex outside \(V_i\) and to no vertex of \(V_i\). Therefore every vertex \(v\in V_i\) has the same open-neighborhood sum:
\[
\sum_{u\in N(v)}f(u)
=
\sum_{j\ne i}s_j
=
W-s_i.
\]
Hence the neighborhood-sum condition is equivalent to
\[
W-s_i\ge1
\]
for every part \(i\).

Now consider a vertex labeled \(-1\) in \(V_i\). It is adjacent precisely to vertices outside \(V_i\). Thus it has a neighbor labeled \(2\) if and only if at least one \(2\)-label occurs outside \(V_i\), equivalently
\[
C-c_i\ge1.
\]
If \(a_i=0\), no Roman-defender condition is imposed by part \(V_i\). This proves the exact feasibility criterion.

For fixed count triples
\[
(a_i,b_i,c_i)
\]
satisfying
\[
a_i+b_i+c_i=n_i,
\]
the number of vertex labelings realizing those counts is
\[
\prod_{i=1}^r
\binom{n_i}{a_i,b_i,c_i}.
\]
All such labelings have weight
\[
W=\sum_i(-a_i+b_i+2c_i).
\]
Summing over exactly the feasible count arrays yields the displayed weight enumerator.

Finally, summing the neighborhood inequalities over all parts gives
\[
\sum_{i=1}^r(W-s_i)\ge r.
\]
Since
\[
\sum_i(W-s_i)=(r-1)W,
\]
one obtains
\[
(r-1)W\ge r.
\]
Because \(W\) is an integer and \(r\ge2\),
\[
W\ge2.
\]
Thus the enumerator is an ordinary polynomial with no negative exponent.

## Verification

The accompanying script `artifacts/verify.py` enumerates every nondecreasing multipartite part-size profile of total order \(2\) through \(8\). For every profile it checks all
\[
3^N
\]
labelings directly from adjacency.

The direct test computes every open-neighborhood sum and checks every \(-1\)-vertex for a neighboring \(2\). Independently, the script evaluates the part-sum criterion and separately expands the multinomial enumerator. The three descriptions agree coefficientwise.

Replay output:

`ALL CHECKS PASSED; profiles=58; labelings_checked=177534; orders=2..8`

The finite check is corroborative only. The arbitrary-order statement follows from the part-neighborhood identities in the proof.

## Relationship to prior work

Koster, Volkmann, and Wehrmann study signed total Roman domination and domatic numbers in complete multipartite graphs in a 2026 preprint. Their abstract states that they determine the signed total Roman domination number and signed total Roman domatic number on this family. The present result refines the scalar domination number by classifying every signed total Roman dominating function and giving the exact weight distribution.

The closest published-result database item concerns signed Roman domination on complete multipartite graphs, where the neighborhood condition is taken over closed neighborhoods rather than open neighborhoods. That distinction changes the partwise inequality: signed total Roman domination depends on
\[
W-s_i,
\]
whereas signed Roman domination also includes the label of the tested vertex. Hence that enumerator does not imply the present one.

Earlier signed total Roman work includes general bounds, complexity, complete graphs, complete bipartite graphs, and graph modifications. Those results determine minima or domatic parameters rather than the complete weight distribution on arbitrary complete multipartite graphs.

## Limitations

The directly accessible material for the 2026 complete-multipartite preprint consisted of its arXiv metadata and abstract-level mirrors. The arXiv PDF transport was unavailable in this run, and the institutional fallback required an interactive step that could not be completed in this non-interactive execution. Thus the originality comparison to that paper is based on its stated scope rather than page-by-page full-text inspection.

This access limitation is a residual originality risk: the paper could contain an intermediate part-count lemma close to the criterion above even though its stated results concern the minimum and domatic numbers. No searched source stated the all-function weight enumerator.

## References

1. A. M. C. A. Koster, L. Volkmann, and M. Wehrmann, “Signed Total Roman Domination and Domatic Numbers: Degree Three and Complete Multipartite Graphs,” arXiv:2606.27175v1, first public June 25, 2026.
2. Y. Guo, L. Volkmann, and Y. Wang, “Signed total Roman domination and domatic numbers in graphs,” Applied Mathematics and Computation 487 (2025), 129074, DOI 10.1016/j.amc.2024.129074.
3. S. Kosari, Y. Rao, Z. Shao, J. Amjadi, and R. Khoeilar, “Complexity of signed total \(k\)-Roman domination problem in graphs,” AIMS Mathematics 6 (2021), 952–961, DOI 10.3934/math.2021057.
