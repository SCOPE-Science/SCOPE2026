# A middle-tier phase transition for unipotent automorphisms of three-level chain-polytope toric varieties

## Finding

Let \(P=A\oplus C\oplus B\) be the ordinal sum of antichains of sizes \(a,b\ge2\) and \(c\ge1\), where every point of \(A\) precedes every point of \(C\), which precedes every point of \(B\). The connected automorphism groups of their **chain-polytope** toric varieties exhibit a sharp dichotomy. Put \(d=a+b+c\) and denote coordinate characters by \(\varepsilon_z\).

For \(c\ge2\), the complete set of Demazure roots is
\[
\mathcal R=\{-\varepsilon_z:z\in P\}.
\]
Consequently the connected automorphism group has an abelian unipotent radical and is
\[
\operatorname{Aut}(X_{a,c,b})^\circ\cong
\mathbb G_a^{d}\rtimes\mathbb G_m^{d},
\qquad \dim\operatorname{Aut}(X_{a,c,b})^\circ=2d.
\]

For \(c=1\), write \(C=\{q\}\). Then the complete root set is
\[
\mathcal R=\{-\varepsilon_z:z\in A\cup B\}
\cup\{-\varepsilon_q+\sum_{i\in I}\varepsilon_i:I\subseteq A\}
\cup\{-\varepsilon_q+\sum_{j\in J}\varepsilon_j:J\subseteq B\},
\]
where the root indexed by the empty subset belongs to both displayed last sets and is counted once. The unipotent radical \(U\) has an explicit nonabelian split structure
\[
U\cong\mathbb G_a^{2^a+2^b-1}\rtimes\mathbb G_a^{a+b},
\qquad \operatorname{class}(U)=\max(a,b)+1,
\]
so
\[
\operatorname{Aut}(X_{a,1,b})^\circ\cong U\rtimes\mathbb G_m^{a+b+1},
\qquad \dim\operatorname{Aut}(X_{a,1,b})^\circ=2(a+b)+2^a+2^b.
\]
All these Demazure roots are nonsemisimple; both regimes are nonreductive. The middle tier of cardinality one has exponentially many roots and unbounded unipotent nilpotency class; increasing it to two collapses the radical to an abelian group.

## Assumptions and scope

The base field is \(\mathbb C\). The integers satisfy \(a,b\ge2\), \(c\ge1\); no assertion is made for smaller outer tiers. The lattice is \(M=\mathbb Z^P\) with its standard coordinate characters and dual \(N\), with distinguished primitive basis vectors \(e_z\). The chain polytope, in coordinates \(x_z\), is exactly
\[
Q=\bigl\{x_z\ge0,\ x_i+x_j+x_k\le1\quad
(i\in A,\ j\in C,\ k\in B)\bigr\}.
\]
The toric variety \(X_{a,c,b}=X(\Sigma_Q)\) is the complete normal toric variety of its normal fan, using the convention that inward primitive facet normals define fan rays. This is the toric variety attached to \(Q\), not the order-polytope Hibi variety attached to the same poset. The facet inequalities are irredundant: each coordinate inequality is supported by a facet containing the origin, while each maximal-chain inequality supports a facet because all other coordinates may be chosen sufficiently small and positive.

## Proof

**Primitive fan rays.** By the displayed irredundant facets, the rays of \(\Sigma_Q\) are precisely \(e_z\) for \(z\in P\), and
\[
\rho_{ijk}=-e_i-e_j-e_k\qquad(i\in A,j\in C,k\in B).
\]
A Demazure root is a nonzero integral character \(m\) for which exactly one ray \(\rho\) satisfies \(\langle m,\rho\rangle=-1\), and all other rays satisfy nonnegative pairing.

**Roots distinguished by outer coordinate rays.** Suppose \(\rho=e_i\) with \(i\in A\). Then \(m_i=-1\) and every other coordinate of \(m\) is a nonnegative integer. Choose another point \(i'\in A\), which exists because \(a\ge2\), and choose arbitrary \(j\in C,k\in B\). The inequality at the nondistinguished ray \(\rho_{i'jk}\) yields \(m_{i'}+m_j+m_k\le0\). Thus all these entries vanish. Varying \(i',j,k\) shows \(m=-\varepsilon_i\); it satisfies every other ray inequality. The same argument applies to \(i\in B\).

**Middle coordinate rays.** Suppose \(\rho=e_j\) with \(j\in C\). For \(c\ge2\), use a different middle element \(j'\) in the preceding argument to force all other entries to zero, yielding the unique root \(-\varepsilon_j\). When \(c=1\), denote its only middle point by \(q\). We have \(m_q=-1\), all other coordinates nonnegative. Every triple inequality reads \(m_i+m_k\le1\) for \(i\in A,k\in B\). Therefore each outer coordinate is either zero or one and there cannot be positive coordinates on both outer tiers. Conversely, every zero-one subset supported entirely in \(A\) or entirely in \(B\) satisfies all inequalities. This proves exactly the displayed subset-indexed roots, with the empty subset counted once.

**No triple-ray roots.** Suppose a distinguished ray has the form \(\rho_{ijk}\). Every coordinate ray is nondistinguished and forces \(m_z\ge0\) for each \(z\). Since both outer tiers contain at least two points, each coordinate \(z\) occurs in some **other** maximal-chain triple. Its ray inequality is a nonpositive sum \(-m_i-m_j-m_k\ge0\), forcing \(m_z=0\). Hence \(m=0\), contradicting the required distinguished pairing \(-1\). Thus all roots have been found, and no root has its negative also a root.

**Connected group and brackets.** Standard Demazure theory for complete toric varieties identifies the connected automorphism Lie algebra as the torus of dimension \(d\) plus one root space for each Demazure root. As no root is semisimple, its reductive quotient is the torus; the subgroup generated by all root groups is its connected unipotent radical. In the regime \(c\ge2\), all coordinate-negative root derivations commute, giving \(\mathbb G_a^d\).

For \(c=1\), write \(h_i\) for root \(-\varepsilon_i\) on \(A\), \(k_j\) for root \(-\varepsilon_j\) on \(B\), \(f_I\) for \(-\varepsilon_q+\sum_{i\in I}\varepsilon_i\), and \(g_J\) for \(-\varepsilon_q+\sum_{j\in J}\varepsilon_j\), identifying \(f_\varnothing=g_\varnothing\). The Demazure derivation associated with root \(m\) and distinguished ray \(\rho\) acts on torus characters as
\[
D_{m,\rho}(\chi^u)=\langle u,\rho\rangle\chi^{u+m}.
\]
Its commutator gives, up to consistent choices of nonzero root-group scalings,
\[
[h_i,f_I]=f_{I\setminus\{i\}}\ (i\in I),
\qquad [k_j,g_J]=g_{J\setminus\{j\}}\ (j\in J),
\]
with these brackets zero when the indicated element is absent. All brackets among the \(f_I,g_J\) vanish; all among the \(h_i,k_j\) vanish; and the cross-tier brackets \([h_i,g_J]\), \([k_j,f_I]\) vanish. Hence their spans \(F\) and \(H\) are abelian Lie subalgebras of dimensions \(2^a+2^b-1\) and \(a+b\), with \(F\) an ideal. Their corresponding connected unipotent subgroups are vector groups and yield \(U=F\rtimes H\). Repeated commutators delete one subset element at a time, and never increase subset size. A nested commutator starting from \(f_A\) and then using each \(h_i\), \(i\in A\), is nonzero and terminates at \(f_\varnothing\); similarly on \(B\). Therefore the lower-central-series class is exactly \(\max(a,b)+1\). The torus dimensions and asserted group dimensions now follow.

## Verification

The accompanying standalone `check_chain_roots.py` uses only the Python standard library and checks the full integer character box \(\{-1,0,1\}^d\) against the explicitly constructed primitive fan rays for eleven parameter triples. It compares the enumerated roots to the theorem, computes all nonzero root-weight commutators, and verifies the nilpotency class of the finite root Lie algebra. Across these cases it checks exactly \(30{,}861\) bounded vectors. The exact printed results are included in `check_output.txt`; replay with `python3 check_chain_roots.py`. This finite regression does **not** prove that no unbounded root exists; that assertion is proved above from the facet inequalities.

## Relationship to prior work

Stanley's chain polytope and its irredundant facet description are classical. Hibi and Li explain the chain/order-polytope relationship and characterize when they are unimodularly equivalent; in general the two toric models cannot be silently identified. Nill's general Demazure-root theory establishes the root-to-automorphism mechanism; Bruns and Gubeladze give a general related automorphism/column-vector framework. These foundations do not state the explicit three-antichain root systems, the exponential one-middle-element count, or the nilpotency-class transition obtained here. The statement is a specialization worked out directly from the relevant fan and is not claimed as a new general theorem on toric automorphisms.

## Limitations

The classification is restricted to three-level ordinal sums with both outer tiers of size at least two, characteristic zero, and the connected component of the automorphism group. It does not classify disconnected fan symmetries, arbitrary posets, or order-polytope Hibi automorphism groups. Possible equivalent presentations in unindexed literature remain a novelty risk; the checked literature and searches are not a proof of universal priority.

## References

1. Benjamin Nill, *Complete toric varieties with reductive automorphism group*, arXiv:math/0407491v1, submitted 2004-07-28. https://arxiv.org/abs/math/0407491
2. Richard P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry 1 (1986), 9–23.
3. Takayuki Hibi and Nan Li, *Unimodular equivalence of order and chain polytopes*, arXiv:1208.4029v1, first posted 2012-08-20. https://arxiv.org/abs/1208.4029
4. Winfried Bruns and Joseph Gubeladze, *Polytopal linear algebra*, arXiv:math/0002024, first posted 2000-02-03. https://arxiv.org/abs/math/0002024
