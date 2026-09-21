# A point-deletion inertia ladder in the Chen--Li graphs

## Statement

For a graph \(G\), write
\[
\operatorname{In}(G)=(n^+(G),n^0(G),n^-(G))
\]
for the numbers of positive, zero, and negative eigenvalues of its adjacency matrix, counted with multiplicity. A graph is **reduced** if it has no isolated vertices and no two vertices have the same open neighborhood.

For \(k\ge 5\), Chen and Li define a graph \(W_k\) with two vertex classes
\[
A=\{a_1,\ldots,a_k\},\qquad
B=\left\{b_S:S\in\binom{[k]}2\right\}.
\]
The vertices in \(A\) induce \(K_k\); the vertices in \(B\) induce the Kneser graph \(KG(k,2)\), so \(b_Sb_T\) is an edge exactly when \(S\cap T=\varnothing\); and \(a_i b_S\) is an edge exactly when \(i\in S\).

Let \(R\subseteq A\) have size \(t\), where \(0\le t\le k\), and set
\[
G_{k,t}=W_k-R.
\]
By the symmetry of \(W_k\) on \([k]\), the isomorphism type depends only on \(t\).

**Theorem.** For every \(k\ge5\) and \(0\le t\le k\), the graph \(G_{k,t}\) is connected and reduced, and
\[
\boxed{
\operatorname{In}(G_{k,t})=
\left(\binom{k}{2}+1-t,\ 0,\ k-1\right).
}
\]

Thus deleting point vertices from \(W_k\) lowers the positive inertia by exactly one per deletion, while the negative inertia remains fixed.

## Proof

Put \(N=\binom{k}{2}\). Chen and Li proved
\[
\operatorname{In}(W_k)=(N+1,0,k-1).
\]
We first record the inertia of the induced subgraph on \(B\), namely \(KG(k,2)\).

Let \(C\) be the \(k\times N\) point--2-subset incidence matrix. If \(K\) is the adjacency matrix of \(KG(k,2)\), then
\[
CC^{\mathsf T}=(k-2)I+J,
\qquad
K=J+I-C^{\mathsf T}C.
\]
Decompose \(\mathbb R^N\) as
\[
\langle \mathbf 1\rangle
\oplus C^{\mathsf T}(\mathbf 1^\perp)
\oplus \ker C.
\]
The three summands have dimensions \(1\), \(k-1\), and \(N-k\). On them, respectively, \(K\) has eigenvalues
\[
\binom{k-2}{2}>0,\qquad 3-k<0,\qquad 1>0.
\]
Hence
\[
\operatorname{In}(KG(k,2))=(N-k+1,0,k-1).
\tag{1}
\]

Now \(G_{k,t}\) is obtained from \(W_k\) by deleting \(t\) vertices, so Cauchy interlacing gives
\[
n^+(G_{k,t})\ge n^+(W_k)-t=N+1-t,
\qquad
n^-(G_{k,t})\le n^-(W_k)=k-1.
\tag{2}
\]
On the other hand, all vertices of \(B\) remain, and they induce \(KG(k,2)\). Applying interlacing to this principal subgraph and using (1) yields
\[
n^-(G_{k,t})\ge k-1.
\tag{3}
\]
Thus \(n^-(G_{k,t})=k-1\). Since
\[
|V(G_{k,t})|=N+k-t,
\]
there are only
\[
N+k-t-(k-1)=N+1-t
\]
remaining eigenvalue slots. The first inequality in (2) fills all of them with positive eigenvalues. Therefore
\[
n^+(G_{k,t})=N+1-t,\qquad n^0(G_{k,t})=0,
\]
proving the inertia formula.

It remains to verify connectedness and reducedness. The graph \(KG(k,2)\) is connected for \(k\ge5\): two disjoint 2-subsets are adjacent, while if two 2-subsets intersect, their union has size at most three and a 2-subset disjoint from that union gives a common neighbor. Every surviving \(a_i\) has neighbors in \(B\), so \(G_{k,t}\) is connected.

There are no isolated vertices. Distinct surviving point vertices \(a_i,a_j\) have different neighborhoods in \(B\), since the 2-subsets containing \(i\) and \(j\) differ. Distinct \(b_S,b_T\) have different neighborhoods already inside \(B\): choose \(x\in S\setminus T\) (after swapping \(S,T\) if necessary) and choose \(y\notin T\cup\{x\}\); then \(\{x,y\}\) is disjoint from \(T\) but not from \(S\). Finally, a surviving \(a_i\) and a vertex \(b_S\) cannot be twins because their numbers of neighbors inside \(B\) are, respectively,
\[
k-1\quad\text{and}\quad \binom{k-2}{2},
\]
and these integers are unequal for every integer \(k\ge5\). Hence \(G_{k,t}\) is reduced. \(\square\)

## Consequences

Set \(q=k-1\ge4\). As \(t\) ranges from \(0\) to \(k=q+1\), the positive inertia
\[
p=\binom{k}{2}+1-t
\]
runs through every integer in the interval
\[
\boxed{
\binom q2\le p\le \binom{q+1}{2}+1.
}
\]
Consequently, for every \(q\ge4\) and every integer \(p\) in this interval, there is a connected reduced nonsingular graph with inertia \((p,0,q)\).

The case \(t=1\) is especially notable:
\[
\operatorname{In}(G_{k,1})=
\left(\binom{k}{2},0,k-1\right),
\]
so
\[
2n^+(G_{k,1})=n^-(G_{k,1})\bigl(n^-(G_{k,1})+1\bigr).
\]
Thus \(\{G_{k,1}:k\ge5\}\) is an infinite family of reduced equality graphs for the bound proposed by Akbari--Elphick--Kumar--Pragada--Tang. This answers their Problem 3.3, which asked whether an infinite family of reduced equality examples exists. Their paper already lists equality examples for negative inertia \(1,2,3\); together with \(G_{q+1,1}\), equality examples therefore exist for every positive value of the negative inertia.

The endpoints also connect naturally to prior work. At \(t=0\) one recovers the Chen--Li graph \(W_k\), whose positive inertia exceeds the former conjectured bound by one. At \(t=k\), one obtains \(KG(k,2)\).

## Verification evidence

The accompanying script reconstructs \(G_{k,t}\) directly and checks every pair \((k,t)\) with \(5\le k\le10\) and \(0\le t\le k\). It verifies the stated inertia, connectivity, and reducedness for 51 graphs. This finite check is corroborative; the theorem is proved above for all parameters.

## Literature and originality

Akbari, Elphick, Kumar, Pragada, and Tang introduced the proposed inertia inequality and explicitly asked in Problem 3.3 for an infinite family of reduced equality graphs. Chen and Li subsequently disproved the inequality by constructing \(W_k\) with inertia \((\binom{k}{2}+1,0,k-1)\), and they separately analyzed the single deletion \(W_5-a_1\), obtaining inertia \((10,0,4)\) to answer the \(n^-=4\) question.

To the best of our knowledge, the all-\(k\), all-\(t\) point-deletion formula above, the resulting interval realization theorem, and the infinite equality subfamily \(W_k-a_i\) have not previously been stated. Searches included the source papers, point-deletion and vertex-deletion formulations, reduced equality graphs, Kneser/Johnson terminology, and recent work citing the inertia conjectures. A September 2026 paper resolving a different asymptotic problem on non-positive inertia was also checked at the level of its stated results; it does not supply the point-deletion theorem above. Residual uncertainty remains from very recent or differently indexed work.

## Limitations

This result does not determine the maximum possible \(n^+\) for fixed \(n^-\) after the original conjecture was disproved, does not classify all reduced equality graphs, and does not claim that point deletion from the Chen--Li graphs is the unique mechanism producing equality. The originality assessment is to the best of our knowledge.

## References

1. S. Akbari, C. Elphick, H. Kumar, S. Pragada, Q. Tang, *A new conjecture on the inertia of graphs*, Discrete Mathematics 349 (2026), 114953. DOI: https://doi.org/10.1016/j.disc.2025.114953 ; arXiv: https://arxiv.org/abs/2508.01163
2. H. Chen, J. Li, *Counterexamples to a conjecture on graph inertia*, arXiv:2605.07196 (2026). https://arxiv.org/abs/2605.07196
3. C. Elphick, H. Kumar, S. Pragada, T. J. Spier, *Resolution of a problem of Mohar on non-positive inertia*, arXiv:2609.06319 (2026). https://arxiv.org/abs/2609.06319
