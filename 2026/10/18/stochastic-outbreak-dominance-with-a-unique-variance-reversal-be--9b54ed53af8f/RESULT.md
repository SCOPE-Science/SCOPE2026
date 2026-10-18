# Stochastic outbreak dominance with a unique variance reversal between the first two cubic contact networks

## Finding

Let \(G=K_{3,3}\) and let \(H=C_3\square K_2\) be the triangular-prism graph. Both are simple, connected, 3-regular graphs on six vertices, and together they are **all** such graphs up to isomorphism. In each graph, independently retain each of its nine edges with probability \(p\in(0,1)\), choose an initial vertex (any vertex), and let \(X_G\) and \(X_H\) denote the sizes of its open connected component. This is also the final outbreak size in a homogeneous independent-edge Reed–Frost epidemic starting from that vertex.

**Exact dominance.** For every \(p\in(0,1)\), the variable \(X_G\) strictly first-order stochastically dominates \(X_H\):

\[
\Pr(X_G\ge k)-\Pr(X_H\ge k)=
\begin{cases}
0,&k=1,2,3,\\
p^3(1-p)^3(4-3p),&k=4,\\
p^4(1-p)^3(5-4p),&k=5,\\
p^5(1-p)^3(6-5p),&k=6.
\end{cases}
\]

In particular, \(\mathbb E[X_G]>\mathbb E[X_H]\) for every interior transmissibility. Nevertheless, there is exactly one \(p_*\in(0,1)\) at which their variances agree. More precisely,

\[
\operatorname{Var}(X_G)-\operatorname{Var}(X_H)=p^3(1-p)^3Q(p),
\]
where
\[
\begin{aligned}
Q(p)={}&245p^{12}-1123p^{11}+1717p^{10}-823p^9+168p^8-832p^7+596p^6\\
&+248p^5-26p^4-161p^3-34p^2-4p+20.
\end{aligned}
\]
The polynomial \(Q\) has exactly one root in \((0,1)\), lying in \((479/1000,480/1000)\), numerically \(p_*\approx0.47924529478\). The variance is **greater** for the triangle-free \(G\) when \(0<p<p_*\) and **smaller** when \(p_*<p<1\), even though \(G\)'s mean remains greater. Thus, at sufficiently high transmissibility the graph with two triangles has lower expected outbreak size yet higher outbreak-size variance.

Among connected *simple cubic* contact graphs, six vertices is the smallest order at which there are two nonisomorphic networks to compare; \(K_4\) is the unique four-vertex case.

## Assumptions and scope

The network is static, undirected, simple and connected; every vertex has degree three. Each edge is open independently with common probability \(p\), and all six vertices are initially susceptible except for one chosen seed. The vertex-transitivity of both graphs makes the size distribution independent of seed choice; it is equally valid for a uniform random seed. The order comparison concerns the **entire finite outbreak distribution**, not an infinite-network epidemic threshold. The two graphs share the same vertex count, edge count and degree sequence, separating this finite structural comparison from degree heterogeneity.

## Proof

**Graph classification.** A simple 3-regular graph has even order at least four. The four-vertex case is \(K_4\). For order six, the complement is a 2-regular simple graph on six vertices, hence either a six-cycle or two disjoint triangles. The complements are respectively the triangular prism and \(K_{3,3}\). Both are connected and vertex-transitive.

**Exact cluster law.** Write \(E_J\) for the nine edges of \(J\in\{G,H\}\) and \(C_J(r,F)\) for the component of root \(r\) in \((V(J),F)\). For \(k\in\{1,\ldots,6\}\), complete finite enumeration gives the *exact identity*
\[
\Pr(X_J\ge k)=\sum_{F\subseteq E_J}\mathbf1_{\{|C_J(r,F)|\ge k\}}
 p^{|F|}(1-p)^{9-|F|}.
\]
The table records, for every open-edge count \(j\), the difference between the numbers of \(j\)-edge subsets satisfying \(|C(r,F)|\ge k\) in \(G\) and \(H\). A fixed root is used; vertex-transitivity makes the counts seed-independent.

| \(j\) | \(k=4\) | \(k=5\) | \(k=6\) |
|---:|---:|---:|---:|
| 0,1,2 | 0 | 0 | 0 |
| 3 | 4 | 0 | 0 |
| 4 | 9 | 5 | 0 |
| 5 | 6 | 6 | 6 |
| 6 | 1 | 1 | 1 |
| 7,8,9 | 0 | 0 | 0 |

For \(k=1,2,3\) every corresponding difference is zero, for each \(j\). Summing the table against \(p^j(1-p)^{9-j}\) and factoring gives the three stated tail-difference polynomials. Each is strictly positive for \(0<p<1\), proving first-order stochastic dominance.

**First and second moments.** For any integer-valued \(X\in\{1,\ldots,6\}\),
\[
\mathbb E[X]=\sum_{k=1}^{6}\Pr(X\ge k),\qquad
\mathbb E[X^2]=\sum_{k=1}^{6}(2k-1)\Pr(X\ge k).
\]
Consequently,
\[
\mathbb E[X_G]-\mathbb E[X_H]
=p^3(1-p)^3(4+2p+2p^2-5p^3)>0.
\]
The cubic factor is positive because it is at least \(4-3p+2p^2>0\) on \((0,1)\). The corresponding second-moment difference is \(p^3(1-p)^3(28+24p+30p^2-55p^3)\). Subtracting the squared means, whose exact integer-polynomial expansions are independently reconstructed by the included verifier, gives the displayed variance polynomial.

**Exactly one crossing.** Substitute \(t=p/(1-p)\) and multiply by \((1+t)^{12}\). In ascending powers of \(t\), the coefficients of \((1+t)^{12}Q(t/(1+t))\) are
\[
(20,236,1242,3679,6235,4684,-2428,-8366,-7038,-3191,-870,-135,-9).
\]
They have exactly one sign change. Descartes' rule gives at most one positive root, counting multiplicity. As \(Q(0)=20>0\) and \(Q(1)=-9<0\), the intermediate value theorem gives exactly one root in \((0,1)\). Exact rational substitution shows \(Q(479/1000)>0>Q(480/1000)\). The variance signs follow from the positive prefactor \(p^3(1-p)^3\).

## Verification

Run `python3 verify.py` using Python's standard library. The program traverses all \(2^9\) possible edge states for each graph and all six roots (\(6144\) rooted states), checks breadth-first traversal against an independent union-find computation, verifies all root distributions coincide, reconstructs the exact integer-polynomial tail, mean, second moment and variance identities, checks the transformed coefficient list and both rational brackets, and independently enumerates all labeled six-vertex cubic graphs (ten with no triangle and sixty with two triangles). It also verifies the exact rational values at \(p=1/2\):
\[
\mathbb E[X_G]=2229/512,\qquad \mathbb E[X_H]=1095/256,
\]
\[
\operatorname{Var}(X_G)=847367/262144,\qquad
\operatorname{Var}(X_H)=213327/65536.
\]
The algebraic uniqueness proof uses Descartes' rule; enumeration is finite and exhaustive only for the stated six-vertex graph class. All claimed assertions are finite or exact polynomial identities.

## Relationship to prior work

Clustering effects on epidemics and bond-percolation component sizes were studied by Newman (2003), Miller (2008/2009), and Gleeson, Melnik and Hackett (2009/2010). In particular, Miller's full open-access analysis explicitly studies how triangles can impede epidemic spread at matched degree distribution, chiefly via large-network growth, outbreak probability and attack rate. House, Ross and Sirl (2012/2013) survey finite-population outbreak-size distribution methods. Those approaches motivate the matched-degree comparison, but the specific *complete six-vertex cubic classification*, all-order stochastic tail dominance and unique variance crossover are not results identified in the examined sources. A broad general formula for a final-size distribution does not by itself establish these two exact graph comparisons or the global uniqueness of the variance sign switch.

## Limitations

The graphs are idealized six-node contacts, not empirically calibrated communities, and no claim is made that triangle count alone orders arbitrary cubic graphs. The conclusion depends on independent identically distributed bond transmission; it does not automatically apply to heterogeneous infectious periods that correlate transmissions from a node, dynamic contacts, larger degree sequences or site percolation. The exact all-\(p\) comparison is specific to these two graph isomorphism types. The literature search cannot exclude an unpublished or unindexed equivalent exact comparison; independent review remains necessary.

## References

- Newman, M. E. J. (2003), *Properties of highly clustered networks*, Physical Review E 68, 026121. https://doi.org/10.1103/PhysRevE.68.026121
- Miller, J. C. (2008 preprint; 2009 journal), *Spread of infectious diseases through clustered populations*, arXiv:0806.2888, Journal of the Royal Society Interface 6, 1121–1134. https://arxiv.org/abs/0806.2888 ; https://doi.org/10.1098/rsif.2008.0524
- Miller, J. C. (2009), *Percolation in clustered networks*, arXiv:0904.3253; journal version *Percolation and epidemics in random clustered networks*, Physical Review E 80, 020901(R). https://arxiv.org/abs/0904.3253 ; https://doi.org/10.1103/PhysRevE.80.020901
- Gleeson, J. P., Melnik, S., and Hackett, A. (2009 preprint; 2010 journal), *How clustering affects the bond percolation threshold in complex networks*, arXiv:0912.4204, Physical Review E 81, 066114. https://arxiv.org/abs/0912.4204
- House, T., Ross, J. V., and Sirl, D. (2012 online; 2013 journal), *How big is an outbreak likely to be? Methods for epidemic final-size calculation*, Proceedings of the Royal Society A 469, 20120436. https://doi.org/10.1098/rspa.2012.0436
