# Exact clique partitions for joins of repeated graph copies

## Statement

For a finite simple graph \(H\), write \(v=|V(H)|\), \(m=|E(H)|\), and let \(\chi'(H)\) be its edge-chromatic number. For a positive integer \(a\), let \(aH\) denote the disjoint union of \(a\) copies of \(H\), and let \(G\vee F\) denote the graph join.

**Theorem.** Let \(a,b\ge1\), and suppose
\[
\min\{a,b\}\ge \chi'(H).
\]
Then
\[
\boxed{
\operatorname{cp}\bigl((aH)\vee(bH)\bigr)
=abv^2-\bigl(a+b+\min\{a,b\}\bigr)m.
}
\]
Here \(\operatorname{cp}(G)\) is the minimum number of cliques whose edge sets partition \(E(G)\).

Thus the Erdős--Faudree--Ordman cut lower bound is attained exactly by an explicit construction throughout this chromatic-index-controlled regime.

## Proof

By symmetry assume \(a\le b\), so the claimed value is
\[
abv^2-(2a+b)m.
\tag{1}
\]
Let \(A\) be the vertex set of the \(aH\) side and \(B\) the vertex set of the \(bH\) side. There are
\[
s=abv^2
\]
edges crossing \((A,B)\), while the two sides contain respectively
\[
u=am,\qquad w=bm
\]
internal edges. The Erdős--Faudree--Ordman cut inequality gives
\[
\operatorname{cp}(G)\ge s-u-w-\min\{u,w\}
=abv^2-(2a+b)m.
\tag{2}
\]

For completeness, the cut inequality follows from a pointwise clique estimate. If a clique meets the two sides in \(p\) and \(q\) vertices, assume \(1\le p\le q\). It contains \(pq\) crossing edges and \(\binom p2,\binom q2\) internal edges, and
\[
pq-1\le 2\binom p2+\binom q2.
\]
Indeed, after multiplying the difference between the right and left sides by two and writing \(q=p+d\), the difference is
\[
(p-1)(p-2)+d(d-1)\ge0.
\]
Summing over a clique partition gives (2).

It remains to attain (1). Put \(q=\chi'(H)\), and fix a proper edge-colouring
\[
E(H)=M_0\dot\cup\cdots\dot\cup M_{q-1}
\]
into matchings. Label the copies on the two sides by
\[
A_0,\ldots,A_{a-1},\qquad B_0,\ldots,B_{b-1},
\]
and identify each copy with \(H\).

First treat \(B_0,\ldots,B_{a-1}\). For every \(i\) and every colour \(r\), pair each edge of the copy of \(M_r\) in \(A_i\) with the corresponding edge of the copy of \(M_r\) in \(B_{i+r\pmod a}\). The four endpoints induce a \(K_4\), which is placed in the partition. Because \(a\ge q\), the ordered copy-pairs \((A_i,B_{i+r})\) are distinct as \(r\) varies. Inside a fixed copy-pair, each colour class is a matching, so the resulting \(K_4\)'s use disjoint crossing edges. Consequently every internal edge of the \(a\) copies on each side is covered exactly once, and no crossing edge is repeated.

There are \(am\) such \(K_4\)'s. They use \(4am\) crossing edges. Covering the remaining crossing edges between these first \(a\) copies on each side individually by \(K_2\)'s gives
\[
a^2v^2-3am
\tag{3}
\]
cliques.

Now let \(B_j\) be one of the remaining \(b-a\) copies. Since \(a\ge q\), assign the colour classes \(M_0,\ldots,M_{q-1}\) to distinct copies \(A_0,\ldots,A_{q-1}\). Fix one vertex \(x_r\in A_r\) for each colour \(r\). For each edge \(yz\in M_r\) inside \(B_j\), place the triangle \(x_ryz\) in the partition. Because \(M_r\) is a matching, no crossing edge incident with \(x_r\) is repeated; different colours use different \(A\)-copies. Hence all \(m\) internal edges of \(B_j\) are covered, using \(2m\) crossing edges, and all remaining crossing edges to \(B_j\) may be taken as \(K_2\)'s. This contributes
\[
m+(av^2-2m)=av^2-m
\tag{4}
\]
cliques per extra \(B\)-copy.

Combining (3) and (4), the partition has
\[
a^2v^2-3am+(b-a)(av^2-m)
=abv^2-(2a+b)m
\]
cliques, matching the lower bound (2).

## Complete-cluster corollary

Take \(H=K_k\). Since
\[
\chi'(K_k)=
\begin{cases}
k-1,&k\text{ even},\\ k,&k\text{ odd},\end{cases}
\]
we obtain the following exact three-parameter family.

**Corollary.** If \(a,b,k\ge1\) and
\[
\min\{a,b\}\ge \chi'(K_k),
\]
then
\[
\boxed{
\operatorname{cp}\bigl((aK_k)\vee(bK_k)\bigr)
=abk^2-\bigl(a+b+\min\{a,b\}\bigr)\binom{k}{2}.
}
\]
Moreover
\[
\boxed{
\operatorname{cc}\bigl((aK_k)\vee(bK_k)\bigr)=ab.
}
\]
Indeed, the \(ab\) sets \(A_i\cup B_j\) form a clique cover. Conversely, choosing one representative from every cluster produces an induced \(K_{a,b}\), and any clique covers at most one of its edges.

Hence the spread \(\sigma=\operatorname{cp}-\operatorname{cc}\) is
\[
\boxed{
\sigma\bigl((aK_k)\vee(bK_k)\bigr)
=ab(k^2-1)-\bigl(a+b+\min\{a,b\}\bigr)\binom{k}{2}.
}
\]

For \(a=b=h\) and even \(k\), this reduces to Bo Ning's 2026 formula
\[
\operatorname{cp}((hK_k)\vee(hK_k))
=h^2k^2-3h\binom{k}{2},
\]
proved there under \(h\ge k-1\). The corollary simultaneously allows unequal cluster counts and removes the parity restriction, with the natural sufficient condition \(\min(a,b)\ge\chi'(K_k)\).

For fixed \(k\) and fixed total number \(a+b\) of clusters within the admissible regime, the displayed spread is maximized when \(|a-b|\le1\). This follows by assuming \(a\le b\), writing \(b=M-a\), and observing that the discrete increment in the spread is
\[
(M-2a-1)(k^2-1)-\binom{k}{2},
\]
which is positive up to the balanced endpoint when \(k\ge2\). When \(k=1\), the spread is identically zero, so a balanced choice is still a maximizer.

## Context

Ning's 2026 preprint *On the difference between clique partition and clique covering numbers* determines both clique parameters for
\[
G_{h,k}=(hK_k)\vee(hK_k)
\]
when \(k\) is even and \(h\ge k-1\), using a one-factorization of \(K_k\). That construction is central to the paper's \(\Theta(n^{4/3})\) determination of the deficit from the maximal clique-cover/partition spread.

The argument above shows that the mechanism is not tied to complete graphs or one-factorizations. A proper edge-colouring of an arbitrary graph \(H\) supplies exactly the matchings needed for a \(K_4\)-packing across matched copies, while the excess copies are absorbed by triangles. The controlling threshold is therefore \(\chi'(H)\), and the classical cut lower bound becomes exact for the whole family \((aH)\vee(bH)\).

A related one-sided identity was used by Rohatgi, Urschel, and Wellens: if \(\ell\ge\chi'(H)\), then the clique partition number of the join of \(H\) with an independent set of size \(\ell\) is \(\ell|V(H)|-|E(H)|\). The extra-copy triangle step above is consistent with that mechanism, while the paired-copy \(K_4\) layer is what attains the stronger two-sided cut bound.

## Verification

The theorem is proved symbolically and does not depend on computation. The accompanying script constructs an optimal partition from an exact edge-colouring for representative graphs \(P_4,C_5,K_3,K_4,K_5\), checks that every graph edge occurs exactly once, and checks the claimed clique count.

## Limitations

The condition \(\min\{a,b\}\ge\chi'(H)\) is sufficient for the exact formula; no necessity claim is made. Outside this regime the cut lower bound can fail to be attainable. The theorem concerns clique **edge partitions**, not vertex clique partitions. The complete-cluster formula gives an exact spread only because the covering number can additionally be determined there.

Originality is to the best of our knowledge. Searches using the join formulation, repeated-copy formulation, cluster-graph terminology, chromatic-index formulation, and the explicit polynomial formulas found the balanced even-\(k\) result above and the one-sided independent-set join identity, but not this two-sided repeated-graph theorem or its asymmetric/parity-free complete-cluster corollary. Very recent or poorly indexed equivalent formulations remain a residual risk.

## References

1. B. Ning, *On the difference between clique partition and clique covering numbers*, arXiv:2609.20305 (2026). https://arxiv.org/abs/2609.20305
2. P. Erdős, R. Faudree, and E. T. Ordman, *Clique partitions and clique coverings*, Discrete Mathematics 72 (1988), 93--101. https://doi.org/10.1016/0012-365X(88)90197-5
3. D. Rohatgi, J. C. Urschel, and J. Wellens, *Regarding two questions about clique and biclique partitions*, Electronic Journal of Combinatorics 28(4) (2021), P4.53. https://doi.org/10.37236/9564
4. L. Caccetta, P. Erdős, E. T. Ordman, and N. J. Pullman, *The difference between the clique numbers of a graph*, Ars Combinatoria 19A (1985), 97--106. https://www.renyi.hu/~p_erdos/1985-35.pdf
