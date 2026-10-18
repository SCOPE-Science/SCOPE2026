# Three singular-stratum families in complete-bipartite stable-set toric varieties

## Finding

**Theorem.** Let \(p,q\ge2\) be integers and \(k\) an algebraically closed field of any characteristic. Let \(P_{p,q}=\operatorname{STAB}(K_{p,q})\subset\mathbb R^{p+q}\), in the standard lattice \(\mathbb Z^{p+q}\), and let \(X_{p,q}\) be the normal projective toric variety of the *normal fan* of \(P_{p,q}\). Then the reduced singular locus has exactly
\[
 p+q+\binom p2\binom q2
\]
irreducible components, precisely the invariant orbit closures corresponding to the following polytope faces:

1. For each left vertex \(i\), the face \(A_i=\{x_i=1\}\cap P_{p,q}\) of dimension \(p-1\), with orbit closure \(Y_i\simeq(\mathbb P^1)^{p-1}\).
2. For each right vertex \(j\), the face \(B_j=\{y_j=1\}\cap P_{p,q}\) of dimension \(q-1\), with orbit closure \(W_j\simeq(\mathbb P^1)^{q-1}\).
3. For each \(I\subset[p]\) and \(J\subset[q]\) of cardinality two, the face
\[
 T_{I,J}=\{x_i+y_j=1\text{ for all }i\in I,\ j\in J\}\cap P_{p,q},
\]
of dimension \(p+q-3\). Its orbit closure \(Z_{I,J}\) is the toric variety of the lattice join of an \((p-2)\)-cube and a \((q-2)\)-cube (a zero-dimensional cube is a point).

The generic transverse affine singularity along \(Y_i\) is the affine cone over the Segre embedding of \((\mathbb P^1)^q\), with embedding dimension \(2^q\) and Hilbert--Samuel multiplicity \(q!\). Along \(W_j\) the corresponding quantities are \(2^p\) and \(p!\). Along \(Z_{I,J}\) the generic transverse model is the three-dimensional ordinary double point \(uv-wz=0\), with multiplicity two. The reduced singular locus is non-equidimensional except when \((p,q)=(2,2)\). Its support equals the non-\(\mathbb Q\)-factorial locus.

For \((p,q)=(2,3)\), there are eight components: two singular lines with transverse multiplicity six, and six singular surfaces with transverse multiplicity two. For \((p,q)=(3,3)\) there are fifteen: six surfaces with transverse multiplicity six and nine threefolds with transverse multiplicity two.

## Assumptions and scope

The coordinates are \((x_1,\ldots,x_p,y_1,\ldots,y_q)\). The stable-set polytope is the convex hull of indicator vectors of subsets contained wholly in the left or the right part. The standard lattice, not an index-changing sublattice, is used throughout. The toric variety uses the normal fan, rather than the fan over faces or an unrelated edge-polytope embedding. A torus orbit of dimension \(d\) corresponds to a polytope face of dimension \(d\). "Generic transverse" means the affine toric factor at the generic point of the orbit of the indicated component. No assertion is made about a scheme-theoretic singular-locus multiplicity or about the transverse type at intersections of components.

## Proof

**1. Facets and lattice normals.** The complete irredundant inequalities of \(P_{p,q}\) are
\[
 x_i\ge0,\qquad y_j\ge0,\qquad x_i+y_j\le1\quad (1\le i\le p,\ 1\le j\le q).
\]
Indeed, any feasible nonnegative point can be written as a convex combination of a point in the left unit cube and one in the right unit cube: set \(a=\max_i x_i\), \(b=\max_j y_j\), so \(a+b\le1\). Conversely both cubes satisfy all inequalities. Each displayed inequality supports a facet when \(p,q\ge2\). Their outward primitive normals, with \(e_i,f_j\) the standard lattice bases, are \(-e_i\), \(-f_j\), and \(e_i+f_j\), respectively.

**2. Smoothness versus cycles.** Form the graph \(H(F)\) on \(\{\star\}\cup\{i\}_{i=1}^p\cup\{j\}_{j=1}^q\): include edge \(\star i\) when \(x_i=0\) identically on \(F\), include \(\star j\) when \(y_j=0\) identically, and include \(ij\) when \(x_i+y_j=1\) identically. Flip the signs of the \(f_j\) coordinates. The preceding normals become signed columns of a graph-incidence matrix with its \(\star\)-row deleted. Every facet normal containing \(F\) spans an extremal ray of the normal cone \(\sigma_F\). Therefore these rays are linearly independent exactly when \(H(F)\) is a forest. Every forest subset of a reduced incidence matrix extends to an integral basis of the ambient lattice (incidence matrices are totally unimodular), so \(\sigma_F\) is smooth exactly when \(H(F)\) is a forest. In particular the non-smooth and non-simplicial cones are identical.

**3. Exhaustion by three families.** If \(H(F)\) contains a simple cycle not through \(\star\), every edge on the cycle is an upper-equality edge. Equalities propagate around this connected bipartite cycle: all left coordinates occurring there have a common value \(t\), and all right coordinates the value \(1-t\). Thus the four upper inequalities for any two of these left and two of these right indices are equalities on \(F\). Hence \(F\subseteq T_{I,J}\) for some two-element \(I,J\).

Suppose a cycle passes through \(\star\). It consists of a path of upper-equality edges between two spokes at \(\star\). If the spokes meet opposite parts, starting with \(x_i=0\) forces every encountered right coordinate to equal one, contradicting the terminal condition \(y_j=0\). If both spokes meet the left part, the path forces its right coordinates to equal one, so \(F\subseteq B_j\) for one of them. If both meet the right part, similarly \(F\subseteq A_i\). This also excludes the apparent triangle consisting of one lower-left, one lower-right and one upper equality. Every non-smooth face is consequently contained in one of the listed faces.

Conversely, at the relative interior of \(A_i\) the active normals are precisely \(-f_j\) and \(e_i+f_j\), \(1\le j\le q\). There are \(2q\) rays in a \((q+1)\)-dimensional cone, so it is nonsimplicial because \(q\ge2\). The analogous cone for \(B_j\) has \(2p\) rays and dimension \(p+1\). At \(T_{I,J}\) the four active normals \(e_i+f_j\) for \(i\in I,j\in J\) span dimension three and obey one square relation, so this cone too is nonsimplicial. These faces are pairwise incomparable under inclusion (check their distinct left- and right-cube vertices). Consequently their orbit closures are exactly the irreducible components of the closed reduced singular locus, with the claimed count.

**4. Component geometry.** The face \(A_i\) is a \((p-1)\)-cube with \(y=0\), so its orbit closure is \((\mathbb P^1)^{p-1}\); similarly for \(B_j\). For \(T_{I,J}\), the four upper equalities impose \(x_i=t\) for \(i\in I\), \(y_j=1-t\) for \(j\in J\), with \(0\le t\le1\). The remaining left coordinates lie in \([0,t]\), the remaining right coordinates in \([0,1-t]\). Thus the face is the lattice join of a \((p-2)\)-cube at \(t=1\) and a \((q-2)\)-cube at \(t=0\), of dimension \(p+q-3\).

**5. Transverse local rings and multiplicity.** Quotient the normal lattice for \(A_i\) by the free tangent coordinates \(e_{i'}\) with \(i'\ne i\). With dual coordinates \((a,b_1,\ldots,b_q)\), the affine semigroup dual to its normal cone is
\[
 S_q=\{(a,c_1,\ldots,c_q)\in\mathbb Z^{q+1}:a\ge0,\ 0\le c_j\le a\},\qquad c_j=-b_j.
\]
It is generated by \((1,\epsilon_1,\ldots,\epsilon_q)\) for binary \(\epsilon_j\), because each \((a,c)\) decomposes into \(a\) such elements by distributing its \(c_j\) ones among \(a\) layers. This is exactly the semigroup of the Segre cone over \((\mathbb P^1)^q\). Its degree-\(a\) piece has dimension \((a+1)^q\), proving embedding dimension \(2^q\) and multiplicity \(q!\). The right-hand family is identical with \(p\) in place of \(q\).

At \(T_{I,J}\), the four primitive normal rays have rank three and, in a saturated rank-three lattice basis, take the form \((1,0,0)\), \((0,1,0)\), \((0,0,1)\), \((-1,1,1)\). Their dual saturated semigroup has four degree-one generators, with the sole relation \(uv=wz\), hence yields the conifold. Its Hilbert--Samuel multiplicity is two.

Because a smooth toric cone is precisely a unimodular simplicial cone and every simplicial cone above is unimodular, the singular and non-\(\mathbb Q\)-factorial supports agree. The component dimensions show that the singular support is equidimensional only at \(p=q=2\). \(\square\)

## Verification

The accompanying standalone program `verify.py` uses exact rational row reduction and exhaustive intersections of the stated facets. For part sizes \((2,2),(2,3),(3,3),(2,4),(3,4)\), it independently determines all faces, tests cone ranks against face codimensions, and identifies the inclusion-maximal nonsmooth faces. It checks equality with exactly the three predicted component families. It separately enumerates the degree-at-most-five binary generator sums for Segre cones with \(q\in\{2,3,4\}\), and checks the primitive square relation for the conifold. Run `python verify.py`; expected final line: `VERIFY_OK`. These finite computations corroborate but do not replace the all-parameter incidence and semigroup proof above.

## Relationship to prior work

Wagner's 1996 projective Hibi-variety work provides a general orbitwise smoothness criterion in terms of poset contractions and discusses local rings; its general criterion is not claimed as new. Lakshmibai--Mukherjee (2007) develop a general method for *affine* Hibi toric varieties and their singular loci. Friedl (2015) identifies projective Hibi varieties with the projective toric varieties of order polytopes and computes their global divisor-class and Picard groups. A coordinate complement in one color class identifies the complete-bipartite stable-set polytope here with the order polytope of the ordinal sum of two antichains. The specific all-parameter three-family component count, dimensions, and two different generic local models are the contribution isolated here, not a new general Hibi smoothness criterion. Literature overlap with earlier computations of this specialization remains possible.

## Limitations

This classifies reduced singular support, not the scheme-theoretic singular subscheme. Transverse models are asserted generically on each component, not at its intersections. The classification concerns the normal-fan toric variety, not necessarily any alternative toric construction on the same graph. Wagner (1996) was available through bibliographic descriptions and abstract but not its complete article; a potentially equivalent explicit worked example therein could not be ruled out. No independent validation has been carried out.

## References

- D. G. Wagner, *Singularities of Toric Varieties Associated with Finite Distributive Lattices*, Journal of Algebraic Combinatorics 5 (1996), 149--165, DOI 10.1023/A:1022469218716.
- V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi Toric Varieties*, arXiv:0706.2686 (public 2007-06-18); especially the introduction and Theorems 6.7--6.9.
- T. Friedl, *Divisors on Projective Hibi Varieties*, arXiv:1506.02407 (public 2015-06-08); especially Proposition 5, Theorem 8 and the introduction.
- H. Ohsugi and T. Hibi, foundational work on stable-set polytopes of perfect graphs, as background for the stable-set viewpoint. No specific first-public date is inferred from this background reference.
