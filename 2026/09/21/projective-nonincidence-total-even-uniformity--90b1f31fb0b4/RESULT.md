# Projective nonincidence graphs realize every even total-uniformity

## Definitions

A sequence of distinct vertices \(S=(v_1,\ldots,v_t)\) in a graph without isolated vertices is a **total dominating sequence** if
\[
N(v_i)\setminus\bigcup_{j<i}N(v_j)\ne\varnothing
\qquad (1\le i\le t)
\]
and \(\{v_1,\ldots,v_t\}\) is a total dominating set. A graph is **total \(k\)-uniform** if every total dominating sequence has length \(k\), equivalently
\[
\gamma_t(G)=\gamma_{gr}^t(G)=k.
\]

Let \(q\) be a prime power, let \(d\ge2\), and let \(V=\mathbb F_q^d\). Define \(X_{d,q}\) to be the bipartite graph whose left vertices are the one-dimensional subspaces \(P\le V\), whose right vertices are the codimension-one subspaces \(H\le V\), and where
\[
PH\in E(X_{d,q})\quad\Longleftrightarrow\quad P\not\subseteq H.
\]
Thus \(X_{d,q}\) is the point-hyperplane nonincidence graph of \(PG(d-1,q)\).

## Main theorem

For every prime power \(q\) and every integer \(d\ge2\),
\[
\boxed{\gamma_t(X_{d,q})=\gamma_{gr}^t(X_{d,q})=2d.}
\]
In fact, \(X_{d,q}\) is connected, false-twin-free, and \(q^{d-1}\)-regular, with
\[
\boxed{|V(X_{d,q})|=2\frac{q^d-1}{q-1}.}
\]
Hence \(X_{d,q}\) is a connected total \(2d\)-uniform graph.

### Proof: the point subsequence

Consider an arbitrary total dominating sequence of \(X_{d,q}\), and retain only its point vertices, in their original order:
\[
P_1,\ldots,P_t.
\]
Because the graph is bipartite, a previously chosen hyperplane vertex dominates only point vertices. It therefore has no effect on whether a newly chosen point vertex has a fresh hyperplane neighbor. Consequently legality of the point subsequence depends only on the earlier points.

Put
\[
W_i=P_1+\cdots+P_i\le V,
\qquad W_0=\{0\}.
\]
After \(P_1,\ldots,P_{i-1}\) have been chosen, a hyperplane is still undominated from the point side exactly when it contains every \(P_j\), equivalently when it contains \(W_{i-1}\). Thus \(P_i\) is legal exactly when there exists a hyperplane containing \(W_{i-1}\) but not \(P_i\). This is equivalent to
\[
P_i\not\subseteq W_{i-1}.
\]
Therefore every legal point choice increases \(\dim W_i\) by exactly one.

At the end, the chosen points dominate every hyperplane if and only if no hyperplane contains all of them, equivalently if and only if
\[
W_t=V.
\]
It follows that every total dominating sequence contains exactly \(d\) point vertices.

### Proof: the hyperplane subsequence

Now retain only the hyperplane vertices:
\[
H_1,\ldots,H_s,
\]
and put
\[
I_i=H_1\cap\cdots\cap H_i,
\qquad I_0=V.
\]
After \(H_1,\ldots,H_{i-1}\) have been chosen, the point vertices not yet dominated from the hyperplane side are exactly the one-dimensional subspaces contained in \(I_{i-1}\). Hence \(H_i\) is legal exactly when
\[
I_{i-1}\not\subseteq H_i.
\]
Since \(H_i\) has codimension one, every such legal choice gives
\[
\dim I_i=\dim I_{i-1}-1.
\]
The selected hyperplanes dominate every point vertex exactly when \(I_s=\{0\}\). Therefore every total dominating sequence contains exactly \(d\) hyperplane vertices.

Thus every total dominating sequence has length \(2d\). Conversely, a basis \(P_1,\ldots,P_d\) of projective points together with hyperplanes \(\ker f_1,\ldots,\ker f_d\) defined by a dual basis \(f_1,\ldots,f_d\) gives a total dominating sequence of length \(2d\). This proves the displayed equality.

### Regularity, connectedness, and false twins

There are
\[
[d]_q=\frac{q^d-1}{q-1}
\]
hyperplanes of \(V\), and exactly \([d-1]_q\) contain a fixed point. Hence every point has degree
\[
[d]_q-[d-1]_q=q^{d-1},
\]
and duality gives the same degree on the hyperplane side.

For any two projective points \(P,Q\), one can choose a linear functional nonzero on both; its kernel is a common neighboring hyperplane. Every hyperplane has a point outside it, so the graph is connected. Distinct points are separated by a hyperplane containing one but not the other, and dually distinct hyperplanes are separated by a point. Cross-part vertices have nonempty neighborhoods in opposite biparts, so no two vertices are false twins.

## Recursive deletion property

For every edge \(PH\) of \(X_{d,q}\) with \(d\ge3\),
\[
\boxed{X_{d,q}-\bigl(N[P]\cup N[H]\bigr)\cong X_{d-1,q}.}
\]
Indeed, the remaining point vertices are precisely the one-dimensional subspaces of \(H\), while the remaining hyperplane vertices are the hyperplanes \(K\le V\) containing \(P\). Since \(P\not\subseteq H\), we have \(V=P\oplus H\), and
\[
K\longmapsto K\cap H
\]
is a bijection from hyperplanes of \(V\) containing \(P\) to hyperplanes of \(H\). It preserves nonincidence with the remaining points. This also shows that the construction is compatible with the standard two-step reduction for total-uniform graphs.

## Existence spectrum

Bahadır, Gözüpek, and Doğan proved that no total \(k\)-uniform graph exists for odd positive \(k\). They exhibited a connected total 8-uniform graph and explicitly left the existence of connected total \(k\)-uniform graphs for every even \(k\ge10\) as an open direction.

The theorem above closes that existence question. For \(k=2\), \(K_2\) is total 2-uniform. For every even \(k=2d\ge4\), choose any prime power \(q\) and use \(X_{d,q}\). Therefore
\[
\boxed{\text{A connected total }k\text{-uniform graph exists iff }k\text{ is a positive even integer}.}
\]
Moreover, varying \(q\) gives infinitely many pairwise nonisomorphic connected, regular, false-twin-free total \(k\)-uniform graphs for every fixed even \(k\ge4\). Taking \(q=2\) gives the explicit order
\[
2(2^d-1)=2\bigl(2^{k/2}-1\bigr).
\]

The first two projective cases recover known phenomena. For \(d=2\), \(X_{2,q}\) is the crown graph \(K_{q+1,q+1}\) minus a perfect matching, a known total 4-uniform family. For \(d=3\), \(X_{3,q}\) is the point-line nonincidence graph of the Desarguesian projective plane of order \(q\), fitting the earlier finite-projective-plane description of regular bipartite total 6-uniform graphs. The new statement is the uniform construction and proof for arbitrary dimension \(d\), in particular all even parameters beyond 8.

## Relation to prior work and originality boundary

Brešar, Henning, and Rall introduced the Grundy total domination number and its hypergraph edge-covering interpretation. Dravec, Jakovac, Kos, and Marc characterized the bipartite total 4-uniform case and regular bipartite total 6-uniform graphs; their total-6 result is tied to finite projective planes. Bahadır, Gözüpek, and Doğan subsequently proved nonexistence for odd \(k\), constructed a connected total 8-uniform graph, and posed the existence of connected examples for all larger even \(k\) as an ongoing problem.

Point-hyperplane nonincidence graphs of finite projective spaces are themselves classical objects and are not claimed to be new. The new claim is their total \(2d\)-uniformity in arbitrary dimension and the resulting completion of the connected existence spectrum. Searches under total \(k\)-uniform graphs, Grundy total domination, total 10-/12-uniform graphs, projective nonincidence/non-incidence graphs, and the equivalent hypergraph-covering terminology did not locate this general construction or the completed spectrum. Originality is therefore asserted only to the best of our knowledge.

## Verification

`artifacts/verify_prime_fields.py` constructs the nonincidence graphs directly over prime fields and exhaustively checks the key point-side equivalence
\[
\text{selected points dominate all hyperplanes}\iff\text{their vectors span }\mathbb F_p^d,
\]
as well as
\[
\text{adding a point is legal}\iff\text{its addition raises the span dimension}.
\]
It also checks regularity, connectedness, and absence of same-part false twins. By duality the same linear-algebra criterion governs the hyperplane side. The checked cases are \((p,d)=(2,2),(2,3),(2,4),(3,2),(3,3)\), including the first total-8 instance. Expected output is in `artifacts/expected_output.txt`.

These finite checks are corroborative only; the proof above covers every prime power \(q\) and every \(d\ge2\).

## Limitations

- The result gives existence, not a classification of all total \(k\)-uniform graphs.
- No claim is made that the displayed orders or degrees are minimal for a given \(k\).
- The nonincidence graphs themselves are classical; novelty is restricted to the total-uniformity theorem and its consequence for the existence spectrum.
- The verification artifact treats prime fields only, while the proof applies to all finite fields of prime-power order.
- Originality remains to the best of our knowledge. A differently indexed paper, thesis, or proceedings article phrased purely in hypergraph covering language or finite-geometry terminology could contain an equivalent observation.

## References

1. B. Brešar, M. A. Henning, and D. F. Rall, *Total Dominating Sequences in Graphs*, Discrete Mathematics 339 (2016), 1665--1676. arXiv:1601.07525.
2. T. Dravec, M. Jakovac, T. Kos, and T. Marc, *On graphs with equal total domination and Grundy total domination numbers*, Aequationes Mathematicae 96 (2022), 137--146. DOI: 10.1007/s00010-021-00776-z.
3. S. Bahadır, D. Gözüpek, and O. Doğan, *On graphs all of whose total dominating sequences have the same length*, Discrete Mathematics 344 (2021), 112492. DOI: 10.1016/j.disc.2021.112492.
4. C. H. Li, C. E. Praeger, and S. Zhou, *Locally primitive graphs and biquasiprimitive graphs*, Journal of the Australian Mathematical Society 91 (2011), 231--242. DOI: 10.1017/S1446788711001480. This reference includes point-hyperplane incidence and nonincidence graphs of projective geometries as standard examples.
