# Conifold components and path-independence incidence in stable-set toric varieties of paths

## Finding

Let \(P_n\) denote the graph path \(1-2-\cdots-n\), let \(Q_n=\operatorname{STAB}(P_n)\subset\mathbb R^n\), and let \(X_n=X(\Sigma_n)\), where \(\Sigma_n\) is the **normal fan** of \(Q_n\) in the lattice \(N=\mathbb Z^n\). For every \(n\ge3\), over any algebraically closed field \(k\), the reduced singular locus has exactly \(n-2\) irreducible components
\[
\operatorname{Sing}(X_n)_{\mathrm{red}}=\bigcup_{j=2}^{n-1}Y_j.
\]
Here \(Y_j\) is the torus-orbit closure corresponding to the face
\[
F_j=\{x\in Q_n:x_{j-1}=0,\ x_j=1,\ x_{j+1}=0\}.
\]
Every \(Y_j\) has codimension three and admits a toric isomorphism
\[
Y_j\simeq X_{j-2}\times X_{n-j-1},
\]
with \(X_0\) a point, \(X_1\simeq\mathbb P^1\). The generic transverse singularity along \(Y_j\) is \(uv-wz=0\), with Hilbert--Samuel multiplicity two.

For a nonempty set \(S\subseteq\{2,\ldots,n-1\}\), the intersection \(\bigcap_{j\in S}Y_j\) is nonempty **exactly when no two members of \(S\) are consecutive**. Each nonempty intersection is an irreducible torus-invariant subvariety, not generally of fixed dimension as \(S\) varies. Thus the nerve of the irreducible singular components is \(\operatorname{Ind}(P_{n-2})\). In particular the number of nonempty intersections indexed by \(r\)-element subsets is
\[
\binom{n-r-1}{r}\qquad(1\le r\le\lceil(n-2)/2\rceil).
\]
The singular support is precisely the non-\(\mathbb Q\)-factorial locus. For example, \(X_3\) has one isolated conifold point, \(X_4\) has two disjoint singular lines, and \(X_5\) has three two-dimensional singular components, of which exactly the two outer components meet.

## Assumptions and scope

The graph has \(n\ge3\) vertices and edges \(\{i,i+1\}\) for \(1\le i<n\). The polytope \(Q_n\) is the convex hull of the characteristic vectors of independent vertex sets in \(P_n\), in its full lattice \(\mathbb Z^n\). Its irredundant inequality description is
\[
Q_n=\{x\in\mathbb R^n:x_i\ge0\ (1\le i\le n),\quad x_i+x_{i+1}\le1\ (1\le i<n)\}.
\]
The facet inequalities are valid and irredundant; integrality follows from total unimodularity of the signed path-incidence matrix. An empty-path factor means a point. The singular locus is considered with its reduced structure. The statements concern the normal-fan projective toric variety, **not** the affine cone of the homogeneous toric ring.

## Proof

**Facet lattice.** The primitive inward/outward facet-normal rays can be taken, with the outward-normal convention, as
\[
\rho_i=-e_i\ (1\le i\le n),\qquad \eta_i=e_i+e_{i+1}\ (1\le i<n).
\]
Multiplying the \(i\)-th row of the matrix of these vectors by \((-1)^i\) turns every \(\eta_i\) into a signed directed edge-incidence vector and every \(\rho_i\) into a signed root-edge vector. Thus the column configuration is, up to signs, the incidence matrix of the graph formed from a path by adjoining one root vertex adjacent to all path vertices. It is totally unimodular. Consequently every linearly independent set of active primitive facet normals extends to an integral basis of its saturated span, and **every simplicial cone of the normal fan is smooth**.

**Circuits force a three-coordinate singular pattern.** In the graphic matroid of the augmented path, every minimal dependent set is a simple cycle. Such a cycle must use two root edges at indices \(p<q\) and the entire path segment between \(p\) and \(q\). A circuit can occur among the active normals of a face only if \(x_p=x_q=0\) and \(x_i+x_{i+1}=1\) for every \(p\le i<q\). Alternation along this path gives \(x_{p+t}=0\) for even \(t\) and \(1\) for odd \(t\); hence \(q-p\) is even and at least two. In particular \(x_p=0,\ x_{p+1}=1,\ x_{p+2}=0\). Therefore any nonsimplicial normal cone contains the normal cone of some \(F_{p+1}\). Conversely, the face \(F_j\) has precisely the four active facets \(\rho_{j-1},\eta_{j-1},\eta_j,\rho_{j+1}\), forming a dependent rank-three cone. It follows that these \(n-2\) cones are exactly the minimal singular cones of \(\Sigma_n\). Torus-orbit closure reversal of inclusions yields exactly the listed irreducible singular components. Since every simplicial cone is smooth, non-\(\mathbb Q\)-factoriality and singularity have identical support.

**Geometry of each component.** On \(F_j\) the indicated triple is fixed to \(0,1,0\), and the remaining coordinates divide into two independent path blocks \(1,\ldots,j-2\) and \(j+2,\ldots,n\). Hence
\[
F_j\cong Q_{j-2}\times Q_{n-j-1}.
\]
Face-orbit closure geometry identifies \(Y_j\) with the toric variety of the product normal fan. The fixed triple has three independent equations, so \(\operatorname{codim}_{X_n}Y_j=3\). The components are distinct because each has a different coordinate equal to one throughout its face.

**Transverse affine chart.** In coordinates \((j-1,j,j+1)\), the four primitive generators of the transverse normal cone are
\[
(-1,0,0),\quad (0,0,-1),\quad (1,1,0),\quad(0,1,1).
\]
They are primitive, every three form a lattice basis, and the unique circuit is the equality of the sum of the first and third vectors with the sum of the second and fourth vectors. The dual lattice semigroup is
\[
\{(a,b,c)\in\mathbb Z^3:-a\ge0,\ -c\ge0,\ a+b\ge0,\ b+c\ge0\}.
\]
Its Hilbert basis is \((0,1,0),(-1,1,0),(0,1,-1),(-1,1,-1)\), with the single binomial relation pairing the first with the fourth versus the second with the third. Therefore the transverse affine toric variety is
\[
\operatorname{Spec}k[u,v,w,z]/(uv-wz),
\]
a three-dimensional ordinary double point in every characteristic. Its hypersurface multiplicity is two.

**Intersection nerve.** For each center \(j\), membership in \(F_j\) fixes \(x_j=1\), \(x_{j-1}=x_{j+1}=0\). If two centers are consecutive, these prescriptions are incompatible. If no two are consecutive, setting the chosen centers to one and all other coordinates to zero produces a stable-set vertex satisfying every prescription; hence the intersection of the faces is a nonempty face. A nonempty intersection of faces is again a face, so its torus-orbit closure is irreducible, and intersection of the orbit closures has that support. Choosing \(r\) nonconsecutive positions from \(n-2\) successive centers yields \(\binom{n-r-1}{r}\) indexed intersections.

## Verification

The standalone program `verify_path_stable.py` requires only Python's standard library. It independently enumerates all independent-set vertices and all nonempty faces as intersections of facet hyperplanes for \(3\le n\le7\). It computes exact rational ranks of active normal systems, checks that every nonsimplicial face lies in one of the predicted \(F_j\), checks the complete maximal singular-face list and the nonconsecutive-center intersection rule, and tests all primitive determinants of the transverse three-dimensional cone. Its exact output is:

```
3 (5, 19, 1, 1, {0: 1})
4 (8, 51, 2, 6, {0: 4, 1: 2})
5 (13, 139, 3, 22, {1: 10, 0: 9, 2: 3})
6 (21, 379, 4, 73, {0: 17, 1: 32, 2: 20, 3: 4})
7 (34, 1035, 5, 234, {1: 83, 0: 30, 2: 82, 3: 34, 4: 5})
VERIFY_OK
```

Each tuple gives the number of vertices, nonempty faces, maximal singular faces, all singular faces, and singular faces by dimension. The all-\(n\) theorem follows from the circuit proof above; finite testing is not used as an infinite proof.

## Relationship to prior work

The stable-set toric-ring framework, normality and ideal-theoretic results are treated by Matsuda--Ohsugi--Shibata (2016). Stable-set polytopes of bipartite graphs are also chain polytopes of height-two posets, linking the path family to the order/chain-polytope setting of Hibi--Li--Li--Mu--Tsuchiya (2015). Both provide the object and important algebraic background; neither inspected paper supplies the normal-fan singular-component and incidence-nerve classification stated here. Lakshmibai--Mukherjee (2007) determine singular loci of affine Hibi varieties, which are affine cones of order-polytope rings, not the projective varieties of the normal fans studied here. Known toric-cone and total-unimodularity tools are used without novelty claims. The new asserted contribution is the complete singular-component arrangement, generic transverse local form, and its path-independence nerve.

## Limitations

This classifies the **reduced** singular support and generic transverse singularity, not the singular subscheme or the completed local rings at every multiple-component intersection. The theorem concerns path graphs; other trees or cyclic graphs need separate analysis. A search did not identify an equivalent published normal-fan classification, but this does not establish global bibliographic uniqueness. A separate independent audit has not been undertaken.

## References

1. T. Hibi, N. Li, T. X. S. Li, L. Mu, A. Tsuchiya, *Order-Chain Polytopes*, first arXiv submission 2015-04-07, arXiv:1504.01706, https://arxiv.org/abs/1504.01706.
2. K. Matsuda, H. Ohsugi, K. Shibata, *Toric rings and ideals of stable set polytopes*, first arXiv submission 2016-03-06, arXiv:1603.01850, https://arxiv.org/abs/1603.01850.
3. V. Lakshmibai, H. Mukherjee, *Singular Loci of Hibi toric varieties*, first arXiv submission 2007-06-18, arXiv:0706.2686, https://arxiv.org/abs/0706.2686 (related affine order-polytope setting).
