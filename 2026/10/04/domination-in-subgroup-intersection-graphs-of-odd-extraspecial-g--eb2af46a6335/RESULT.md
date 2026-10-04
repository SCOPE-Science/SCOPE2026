# Domination in subgroup intersection graphs of odd extraspecial groups

## Finding

Let \(p\) be an odd prime and let \(G\) be an extraspecial \(p\)-group of order \(p^{1+2n}\), with \(n\ge1\). Let \(\Gamma(G)\) be the intersection graph of the proper nontrivial subgroups of \(G\). If \(\operatorname{exp}(G)=p\), then \[\gamma(\Gamma(G))=\gamma_t(\Gamma(G))=\gamma_{\mathrm{pr}}(\Gamma(G))=p+1.\] If \(\operatorname{exp}(G)=p^2\), then \[\gamma(\Gamma(G))=1,\qquad \gamma_t(\Gamma(G))=\gamma_{\mathrm{pr}}(\Gamma(G))=2.\] Thus the triple of ordinary, total, and paired domination numbers detects the exponent among odd extraspecial groups.

The two exponent types behave for opposite structural reasons. In exponent \(p\), domination becomes a finite-vector-space covering problem and the sharp value is \(p+1\). In exponent \(p^2\), the \(p\)-th-power kernel is a proper subgroup containing every minimal subgroup, so one subgroup already dominates.

## Assumptions and scope

The intersection graph \(\Gamma(G)\) has one vertex for every proper nontrivial subgroup of \(G\); distinct vertices \(H,K\) are adjacent when
\[
H\cap K\ne1.
\]
A total dominating set is a vertex set in which every graph vertex, including every selected vertex, has a selected neighbor. A paired dominating set is a dominating set whose induced subgraph contains a perfect matching.

For an extraspecial \(p\)-group,
\[
Z(G)=G'=\Phi(G),\qquad |Z(G)|=p,
\]
and
\[
V=G/Z(G)
\]
is a \(2n\)-dimensional vector space over \(\mathbb F_p\). For odd \(p\), extraspecial groups of a fixed order have exponent either \(p\) or \(p^2\).

We use the following domination criterion. A collection \(\mathcal D\) of proper nontrivial subgroups dominates \(\Gamma(G)\) exactly when its union contains every minimal subgroup of \(G\). Indeed, if a minimal subgroup \(A\) is dominated by \(H\), then \(A\cap H\ne1\), hence \(A\le H\). Conversely, every nontrivial subgroup contains a minimal subgroup.

## Proof

Assume first that
\[
\operatorname{exp}(G)=p.
\]
Every nonidentity element then has order \(p\). By the criterion above, a family of subgroup vertices dominates exactly when its union is all of \(G\).

Any dominating family can be enlarged, without increasing its cardinality, to a family of maximal subgroups. Since
\[
\Phi(G)=Z(G),
\]
every maximal subgroup contains \(Z(G)\), and the maximal subgroups correspond under the quotient map to the hyperplanes of
\[
V=G/Z(G)\cong\mathbb F_p^{2n}.
\]
Consequently the ordinary domination number is the minimum number of hyperplanes required to cover \(V\).

Let \(d=2n\). Fix one hyperplane \(H_1\). Each further hyperplane contributes at most
\[
p^{d-1}-p^{d-2}
\]
new vectors beyond \(H_1\). Thus the union of \(k\le p\) hyperplanes has size at most
\[
p^{d-1}+(k-1)(p^{d-1}-p^{d-2})
\le
p^{d-2}(p^2-p+1)
< p^d.
\]
Hence at least \(p+1\) hyperplanes are necessary.

For the matching upper bound, choose a codimension-two subspace \(U<V\). The quotient \(V/U\) has dimension two and therefore exactly \(p+1\) one-dimensional subspaces. Their inverse images are \(p+1\) hyperplanes through \(U\), and their union is all of \(V\). Their corresponding maximal subgroups all contain \(Z(G)\), so they form a clique in \(\Gamma(G)\). Since \(p\) is odd, \(p+1\) is even; the clique therefore has a perfect matching. Hence the same \(p+1\) vertices are simultaneously ordinary dominating, total dominating, and paired dominating. Thus
\[
\gamma(\Gamma(G))
=
\gamma_t(\Gamma(G))
=
\gamma_{\mathrm{pr}}(\Gamma(G))
=p+1.
\]

Now assume
\[
\operatorname{exp}(G)=p^2.
\]
Because \(G\) has class two and \(p\) is odd, the standard class-two power identity gives
\[
(xy)^p=x^py^p[y,x]^{p(p-1)/2}=x^py^p,
\]
since every commutator has order dividing \(p\). Thus
\[
\varphi:G\longrightarrow Z(G),\qquad \varphi(x)=x^p,
\]
is a homomorphism. It is nontrivial because the group has exponent \(p^2\), hence it is surjective because \(|Z(G)|=p\). Its kernel
\[
K=\ker\varphi
\]
is therefore a proper subgroup of index \(p\).

Every minimal subgroup of the \(p\)-group \(G\) has order \(p\). Every element of order \(p\) lies in \(K\), so \(K\) contains every minimal subgroup. The domination criterion now gives
\[
\gamma(\Gamma(G))=1.
\]

A total or paired dominating set cannot have one vertex. Since \(Z(G)\le K\), while \(Z(G)\ne K\), the two vertices
\[
\{Z(G),K\}
\]
are adjacent. The vertex \(K\) already dominates the graph, so this adjacent pair is total dominating and its unique edge is a perfect matching. Therefore
\[
\gamma_t(\Gamma(G))
=
\gamma_{\mathrm{pr}}(\Gamma(G))
=2.
\]

The two cases prove the theorem.

## Verification

The accompanying `verify.py` independently constructs the two nonisomorphic extraspecial groups of order \(27\): the Heisenberg group of exponent \(3\) and the modular group of exponent \(9\). It enumerates their complete subgroup lattices, builds the intersection graphs, and exhaustively searches ordinary, total, and paired dominating sets.

The exponent-three graph has \(17\) vertices and yields
\[
(\gamma,\gamma_t,\gamma_{\mathrm{pr}})=(4,4,4),
\]
while the exponent-nine graph has \(8\) vertices and yields
\[
(\gamma,\gamma_t,\gamma_{\mathrm{pr}})=(1,2,2).
\]
The checker also verifies that the cube-map kernel in the exponent-nine group has order \(9\) and contains all elements of order \(3\), and that four lines are necessary and sufficient to cover \(\mathbb F_3^2\).

Exact output:

```text
VERIFY_OK
Heisenberg27_exp3: vertices=17 subgroup_orders={3: 13, 9: 4} gamma=4 gamma_t=4 gamma_pr=4
Modular27_exp9: vertices=8 subgroup_orders={3: 4, 9: 4} gamma=1 gamma_t=2 gamma_pr=2
M27_pth_power_kernel_size=9_contains_all_order3_elements
F3^2_hyperplane_cover_minimum=4
```

These finite computations are corroborative only. The arbitrary-order theorem is proved by the subgroup-cover and power-kernel arguments above.

## Relationship to prior work

Kayacan studied domination in subgroup intersection graphs of finite groups. The paper proves the exact criterion that a dominating family must cover every minimal subgroup and develops classifications and upper bounds for broad group classes. Its first public version was posted on 10 February 2016 and is classified under MSC \(20D15\). It does not specialize the domination problem to extraspecial groups.

For the extraspecial structure used here, later work on special \(p\)-groups records that, for odd \(p\), the map
\[
xZ(G)\longmapsto x^p
\]
is linear on \(G/Z(G)\), and that the two extraspecial isomorphism types of a fixed odd-prime order have exponents \(p\) and \(p^2\), respectively.

A recent paper computes ordinary and total domination for proper commuting graphs of finite groups, including extraspecial families. That graph has noncentral group elements as vertices and joins commuting elements; it is not the subgroup intersection graph considered here and does not imply the present result.

Targeted searches under subgroup-intersection, extraspecial, exponent, ordinary domination, total domination, paired domination, and symplectic or vector-space-cover formulations did not locate the displayed two-case classification.

## Limitations

The theorem is restricted to odd primes. For \(p=2\), extraspecial groups are controlled by a quadratic form rather than by the odd-prime linear \(p\)-power map used above, and the exponent split is different.

No formula is asserted for general special \(p\)-groups with center larger than order \(p\), or for arbitrary class-two groups.

The originality comparison cannot exclude an unindexed specialization of the general subgroup-intersection literature. The strongest same-object source inspected gives the domination criterion and broad bounds but no extraspecial theorem; the strongest same-family domination source found concerns the different proper commuting graph.

## References

1. S. Kayacan, “Dominating Sets in Intersection Graphs of Finite Groups,” arXiv:1602.03537, first posted 10 February 2016; later published in *Rocky Mountain Journal of Mathematics* 48 (2018), 2311–2335.
2. D. Kaur, H. Kishnani, and A. Kulshrestha, “Word Images and Their Impostors in Finite Nilpotent Groups,” arXiv:2205.15369, first posted 30 May 2022.
3. S. Bera, H. K. Dey, and U. Jethva, “Centralizers in finite groups and Domination number of their commuting graphs,” arXiv:2605.04567, first posted 6 May 2026.
