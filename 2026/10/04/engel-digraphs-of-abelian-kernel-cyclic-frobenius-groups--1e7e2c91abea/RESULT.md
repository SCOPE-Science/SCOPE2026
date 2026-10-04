# Engel digraphs of abelian-kernel cyclic Frobenius groups

## Finding

Let
\[
G=K\rtimes H
\]
be a finite Frobenius group with nontrivial abelian kernel \(K\) and cyclic complement
\[
H\cong C_m,
\qquad m>1.
\]
Put \(k=|K|\). Following Detomi, Lucchini and Nemmi, let \(\Gamma(G)\) be the directed Engel graph on the non-hypercentral elements, with an arc
\[
x\longrightarrow y
\]
when
\[
[x,{}_{n}y]=1
\]
for some integer \(n\ge1\).

Then
\[
Z_\infty(G)=1
\qquad\text{and}\qquad
\boxed{\Gamma(G)=\Gamma_2(G)}.
\]

Let
\[
H_1,\ldots,H_k
\]
be the \(k\) conjugates of \(H\), and write \(X^\#=X\setminus\{1\}\). The vertices admit the disjoint partition
\[
G^\#=K^\#\sqcup H_1^\#\sqcup\cdots\sqcup H_k^\#.
\]
The complete arc description is:

- each of \(K^\#,H_1^\#,\ldots,H_k^\#\) induces a complete bidirected digraph;
- every vertex of every \(H_i^\#\) has an arc to every vertex of \(K^\#\), and each such arc has exact Engel depth \(2\);
- there is no arc from \(K^\#\) to any \(H_i^\#\);
- there is no arc between \(H_i^\#\) and \(H_j^\#\) when \(i\ne j\).

Hence the strong components are exactly
\[
K^\#,H_1^\#,\ldots,H_k^\#,
\]
so there are \(k+1\) of them. The condensation digraph is a directed star: each complement component points to the kernel component and there are no other intercomponent arcs.

The underlying undirected Engel graph is
\[
\boxed{
\mathrm K_{k-1}\vee
\bigl(k\,\mathrm K_{m-1}\bigr),
}
\]
and therefore has diameter \(2\). Its number of directed arcs is
\[
\boxed{
(k-1)(k-2)+k(m-1)(m-2)+k(k-1)(m-1).
}
\]
The indegree and outdegree pairs are
\[
(\deg^-,\deg^+)=(km-2,k-2)
\]
for vertices in \(K^\#\), and
\[
(\deg^-,\deg^+)=(m-2,k+m-3)
\]
for vertices outside \(K\).

Equivalently, if one uses the co-Engel graph and deletes its isolated Fitting-subgroup vertices, the remaining graph is
\[
\boxed{
K_{\underbrace{m-1,\ldots,m-1}_{k\text{ parts}}}.
}
\]

## Assumptions and scope

A Frobenius decomposition \(G=K\rtimes H\) means that every nonidentity element of the complement acts fixed-point-freely on the kernel. The result assumes that \(K\) is abelian and \(H\) is cyclic. The kernel need not be cyclic, elementary abelian, or a \(p\)-group.

The direction convention is the one in the 2022 paper of Detomi, Lucchini and Nemmi: \(x\to y\) when some right-normed Engel commutator \([x,{}_{n}y]\) is trivial. Some later papers use the reverse arrow convention; the structural statement above is tied explicitly to this convention.

## Proof

First \(Z(G)=1\). If \(z\in Z(G)\cap K\), then every element of \(H\) fixes \(z\), so fixed-point-freeness forces \(z=1\). If \(z\notin K\), then \(z\) belongs to a conjugate complement and centralizes no nonidentity element of \(K\), again by the Frobenius property. Thus \(Z(G)=1\), and consequently the upper central series remains trivial:
\[
Z_\infty(G)=1.
\]
So the Engel graph has vertex set \(G^\#\).

The conjugates of a Frobenius complement intersect pairwise trivially, and every element outside the kernel belongs to exactly one conjugate complement. Since \(H\) is cyclic, every \(H_i\) is abelian. Therefore the displayed partition of \(G^\#\) holds and each \(H_i^\#\), as well as \(K^\#\), is a complete bidirected subgraph by ordinary commutativity.

Now take \(x\in G\setminus K\) and \(1\ne y\in K\). The first commutator \([x,y]\) belongs to \(K\). Since \(K\) is abelian,
\[
[x,{}_{2}y]=[[x,y],y]=1.
\]
Moreover \([x,y]\ne1\), because a nonidentity element outside the Frobenius kernel centralizes no nonidentity kernel element. Hence every arc
\[
x\longrightarrow y
\]
from outside the kernel to the kernel has exact Engel depth \(2\).

For the reverse direction, fix \(1\ne x\in K\) and \(y\in G\setminus K\). Conjugation by \(y\) restricts to a fixed-point-free automorphism of the finite abelian group \(K\). Define
\[
\delta_y(a)=[a,y]
\qquad(a\in K).
\]
Because \(K\) is abelian, \(\delta_y\) is an endomorphism of \(K\). Its kernel is \(C_K(y)=1\), so finiteness makes \(\delta_y\) an automorphism. Therefore
\[
[x,{}_{n}y]=\delta_y^{\,n}(x)\ne1
\qquad(n\ge1),
\]
and there is no arc from \(K^\#\) to an outside vertex.

Finally let \(x,y\in G\setminus K\). Since \(G/K\cong H\) is abelian,
\[
[x,y]\in K.
\]
For \(n\ge2\), iteration gives
\[
[x,{}_{n}y]=\delta_y^{\,n-1}([x,y]).
\]
The map \(\delta_y\) is an automorphism, so an Engel commutator can become trivial if and only if \([x,y]=1\). Thus
\[
x\longrightarrow y
\quad\Longleftrightarrow\quad
[x,y]=1.
\]
The centralizer of a nonidentity element \(y\) outside \(K\) is precisely the unique conjugate complement containing \(y\): its kernel intersection is trivial and that complement is abelian. Consequently two outside vertices commute if and only if they lie in the same \(H_i\). This proves the complete arc classification.

Every arc has Engel depth at most \(2\), while every nonarc remains nonadjacent for all Engel depths, so
\[
\Gamma(G)=\Gamma_2(G).
\]
The statements about strong components and the condensation digraph are immediate from the arc partition.

The underlying undirected graph consists of a clique on \(K^\#\), joined to all outside vertices, while the outside vertices form \(k\) disjoint cliques of size \(m-1\). This is
\[
\mathrm K_{k-1}\vee k\,\mathrm K_{m-1}.
\]
Counting ordered arcs inside the \(k+1\) complete bidirected blocks and then the one-way arcs from the outside blocks to the kernel gives
\[
(k-1)(k-2)+k(m-1)(m-2)+k(k-1)(m-1).
\]
The degree formulas follow from the same partition. Taking the complement on the non-Fitting vertices gives the stated complete multipartite co-Engel graph.

## Verification

The included replay constructs six semidirect products directly from their multiplication laws, including cyclic and noncyclic kernels, a non-elementary kernel, and complements of orders \(2,3,4,6\). It computes every iterated Engel commutator for every ordered pair of distinct nonidentity elements until either the identity or a cycle appears.

The examples are
\[
C_3\rtimes C_2,
\quad C_5\rtimes C_4,
\quad C_7\rtimes C_3,
\quad C_9\rtimes C_2,
\quad C_5^2\rtimes C_4,
\quad C_7^2\rtimes C_6,
\]
with fixed-point-free scalar actions. For each example the replay independently reconstructs the conjugate complements, verifies every predicted arc and nonarc, computes the exact Engel depths, recovers all strong components, and checks the arc-count and degree formulas.

For the six examples the total numbers of arcs are respectively
\[
8,\ 102,\ 128,\ 128,\ 2502,\ 14996.
\]
The replay returns `VERIFY_OK`.

Finite enumeration is not used in the universal proof.

## Relationship to prior work

Detomi, Lucchini and Nemmi proved that the Engel graph of every finite group is weakly connected and that a Frobenius group is a fundamental obstruction to strong connectivity. In particular, their Lemma 3.1 proves that no nontrivial kernel element of a Frobenius group has an Engel arc to an element outside the kernel. Their result does not classify the remaining arcs or the strong components of a Frobenius Engel graph.

Cameron, Chakraborty, Nath and Nongsiang later studied Engel and co-Engel graphs in detail. Their explicit co-Engel calculations include ordinary dihedral groups and nonabelian groups of order the product of two primes. For the latter they obtain a complete multipartite co-Engel graph on the non-Fitting elements. Those results agree with the corresponding special cases of the theorem here. The full text inspected does not state the general abelian-kernel, cyclic-complement directed classification, the \(k+1\) strong-component formula, or the equality \(\Gamma(G)=\Gamma_2(G)\) for this whole Frobenius family.

The present result therefore refines the principal Frobenius obstruction from a non-connectivity statement to a complete directed decomposition for all finite Frobenius groups with abelian kernel and cyclic complement. It simultaneously extends the known prime-order and ordinary-dihedral co-Engel patterns to arbitrary finite abelian Frobenius kernels.

## Limitations

The kernel is required to be abelian. For a nonabelian Frobenius kernel, the implication from an outside vertex to a kernel vertex need not have Engel depth \(2\), and the kernel itself need not form a complete bidirected block.

The complement is required to be cyclic. For a nonabelian Frobenius complement, the outside strong components can reflect the complement's own Engel structure rather than being complete bidirected cliques.

The theorem classifies one broad Frobenius family; it does not classify Engel digraphs of arbitrary Frobenius groups.

The literature search cannot exclude an equivalent statement recorded under different terminology for directed Engel relations in metacyclic or affine groups.

## References

1. E. Detomi, A. Lucchini and D. Nemmi, “The Engel graph of a finite group,” arXiv:2202.13737v1, first public version 28 February 2022; *Forum Mathematicum* 35 (2023), 111–122, DOI 10.1515/forum-2022-0070.
2. P. J. Cameron, R. Chakraborty, R. K. Nath and D. Nongsiang, “Co-Engel graphs of certain finite non-Engel groups,” arXiv:2408.03879v1, first public version 7 August 2024; later versions use the title “Engel and co-Engel graphs of finite groups.”
