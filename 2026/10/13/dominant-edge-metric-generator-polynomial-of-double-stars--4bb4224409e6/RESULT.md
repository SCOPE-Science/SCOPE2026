# Dominant edge metric generator polynomial of double stars
## Finding
For integers \(p,q\ge1\), let \(S_{p,q}\) be the double star formed from adjacent centers \(u,v\), with leaf sets
\[
A=\{a_1,\ldots,a_p\},\qquad B=\{b_1,\ldots,b_q\},
\]
where every vertex of \(A\) is adjacent only to \(u\) and every vertex of \(B\) is adjacent only to \(v\).

A set \(S\subseteq V(S_{p,q})\) is a dominant edge metric generator exactly when all five conditions hold:

1. at most one vertex of \(A\) is omitted;
2. at most one vertex of \(B\) is omitted;
3. if \(u\notin S\), then \(A\subseteq S\);
4. if \(v\notin S\), then \(B\subseteq S\);
5. at least one of \(u,v\) belongs to \(S\).

Define the dominant edge metric generator polynomial by
\[
\mathcal D_e(S_{p,q};x)=\sum_{S}x^{|S|},
\]
where the sum is over all dominant edge metric generators. Then
\[
\mathcal D_e(S_{p,q};x)
=
x^{p+q}\bigl(x^2+(p+q+2)x+pq+p+q\bigr).
\]
Therefore
\[
\operatorname{Ddim}_e(S_{p,q})=p+q,
\]
and the number of minimum dominant edge metric bases is
\[
pq+p+q=(p+1)(q+1)-1.
\]
The only generator sizes are \(p+q\), \(p+q+1\), and \(p+q+2\), with respective multiplicities
\[
pq+p+q,\qquad p+q+2,\qquad 1.
\]

## Assumptions and scope
For a connected graph \(G\), the distance from a vertex \(z\) to an edge \(e=rs\) is
\[
d(z,e)=\min\{d(z,r),d(z,s)\}.
\]
A set \(S\subseteq V(G)\) is an edge metric generator if distinct edges have distinct vectors of distances to the vertices of \(S\). It is a dominant edge metric generator when it is simultaneously an edge metric generator and a vertex cover. The minimum cardinality is denoted by \(\operatorname{Ddim}_e(G)\).

The theorem covers every nontrivial double star \(S_{p,q}\) with \(p,q\ge1\). The polynomial above is an all-generator enumerator introduced here for this family; it refines the minimum parameter by retaining every feasible cardinality.

## Proof
Let \(S\) be a dominant edge metric generator.

Because \(S\) is a vertex cover, the central edge \(uv\) forces
\[
u\in S\quad\text{or}\quad v\in S.
\]
If \(u\notin S\), then every pendant edge \(ua_i\) must be covered at its leaf endpoint, hence \(A\subseteq S\). Similarly,
\[
v\notin S\Longrightarrow B\subseteq S.
\]

Now suppose two distinct leaves \(a_i,a_j\) are both omitted. For every selected vertex \(z\notin\{a_i,a_j\}\), the two pendant edges \(ua_i\) and \(ua_j\) have the same distance from \(z\): the unique paths from \(z\) to either edge reach the common center \(u\) at the same distance. Hence the two edges have identical edge metric representations, contradicting edge resolution. Thus at most one vertex of \(A\) is omitted. The same argument applies to \(B\). This proves necessity of the five conditions.

Conversely, assume the five conditions. The vertex-cover condition follows immediately from the center rules. We show that every two edges are resolved.

Two distinct \(A\)-pendant edges are separated by a selected leaf endpoint of at least one of them, because at most one \(A\)-leaf is omitted. The same holds for two \(B\)-pendant edges.

An \(A\)-pendant edge and a \(B\)-pendant edge are separated by a selected center: if \(u\in S\), their distances from \(u\) are \(0\) and \(1\); if \(u\notin S\), then \(v\in S\), where the roles are reversed.

Consider the central edge \(uv\) and an \(A\)-pendant edge \(ua_i\). If \(v\in S\), then their distances from \(v\) are \(0\) and \(1\). If \(v\notin S\), then every \(B\)-leaf is selected, and any \(b_j\in B\) has distance \(1\) from \(uv\) and distance \(2\) from \(ua_i\). Thus these edges are separated. The argument for \(uv\) versus a \(B\)-pendant edge is symmetric. Hence the five conditions are sufficient.

It remains only to count. If both centers are selected, the leaf choices contribute
\[
x^2(x^p+p x^{p-1})(x^q+q x^{q-1}).
\]
If only \(u\) is selected, all \(B\)-leaves are forced and the contribution is
\[
x^{q+1}(x^p+p x^{p-1}).
\]
If only \(v\) is selected, the contribution is
\[
x^{p+1}(x^q+q x^{q-1}).
\]
Adding and collecting powers gives
\[
\mathcal D_e(S_{p,q};x)
=x^{p+q}\bigl(x^2+(p+q+2)x+pq+p+q\bigr).
\]
All stated consequences follow from its lowest nonzero coefficient and its three terms.

## Verification
The bundled checker constructs every \(S_{p,q}\) with
\[
1\le p,q\le5
\]
and exhausts every vertex subset. For each subset it independently tests the vertex-cover condition and computes all edge-distance representations. It then compares feasibility with the five-condition characterization and verifies the entire cardinality profile.

Across the tested family the checker examines \(15{,}376\) subsets. This finite computation corroborates the theorem; the arbitrary-parameter result is proved symbolically above.

## Relationship to prior work
Dominant edge metric dimension was introduced by Tavakoli, Korivand, Erfanian, Abrishami, and Baskoro. Their definition is exactly the intersection of vertex-cover feasibility with edge metric resolution. Their Theorem 2.4 proves that a graph with \(m\) pendant vertices has dominant edge metric dimension at least \(m\).

The same paper gives a corona-product formula and, in Example 3.3, obtains
\[
\operatorname{Ddim}_e(T_{l,t})=lt
\]
for the uniform caterpillar \(T_{l,t}=P_l\circ\overline{K_t}\). In particular, taking \(l=2\) covers the scalar value for the balanced double star \(S_{t,t}\): it gives \(\operatorname{Ddim}_e(S_{t,t})=2t\). The present statement does not claim that balanced scalar value as new. Its additional content is the arbitrary unbalanced double-star family, the exact characterization of every dominant edge metric generator, the full three-term enumerator, and the exact count of minimum bases.

Targeted searches under “double star”, “bistar”, the notation \(S_{p,q}\), and dominant-edge-metric generator/enumerator terminology did not locate this all-set classification. A similarly named vertex-edge dominant edge metric parameter in later literature uses a vertex-edge domination condition rather than a vertex cover and is therefore not equivalent.

The earliest verified public full-text date for the introducing paper is 11 April 2023, from an author-uploaded public copy. The journal PDF records Mathematics Subject Classification 05C12, 05C76, and 90C60.

## Limitations
The polynomial concerns dominant edge metric generators, not ordinary edge metric generators or the distinct vertex-edge dominant edge metric parameter.

The balanced scalar subfamily \(S_{t,t}\) is already implied by the published uniform-caterpillar example. Novelty here rests on the complete all-generator classification and enumerator, including arbitrary unequal \(p,q\).

The verifier is exhaustive only for \(1\le p,q\le5\); it is a check of the proof, not the basis for the infinite theorem.

A differently phrased or non-indexed all-set classification may exist despite the targeted searches.

## References
1. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami, E. T. Baskoro, “The dominant edge metric dimension of graphs,” Electronic Journal of Graph Theory and Applications 11 (2023), 197–208, DOI 10.5614/ejgta.2023.11.1.16.
2. A. Kelenc, N. Tratnik, I. G. Yero, “Uniquely identifying the edges of a graph: The edge metric dimension,” Discrete Applied Mathematics 256 (2018), 204–220.
