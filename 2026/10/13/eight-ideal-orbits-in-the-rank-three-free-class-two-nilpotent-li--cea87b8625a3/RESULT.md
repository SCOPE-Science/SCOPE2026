# Eight ideal orbits in the rank-three free class-two nilpotent Lie algebra over finite fields

## Finding

For every prime power \(q\), let \(V=\mathbb F_q^3\), \(Z=\bigwedge^2 V\), and let \(L=V\oplus Z\) be the six-dimensional Lie algebra with bracket \([v+z,w+z']=v\wedge w\in Z\). There are **exactly eight ideals up to the full algebra automorphism group**, with complete orbit data in the table below. Set \(Q=q^2+q+1\), choose a basis \(x_1,x_2,x_3\) of \(V\), and write \(z_{ij}=x_i\wedge x_j\).

| \((u,w)\) | Ideal representative | Ideal dimension | Orbit cardinality |
|---|---|---:|---:|
| \((0,0)\) | \(0\) | 0 | 1 |
| \((0,1)\) | \(\langle z_{12}\rangle\) | 1 | \(Q\) |
| \((0,2)\) | \(\langle z_{12},z_{13}\rangle\) | 2 | \(Q\) |
| \((0,3)\) | \(Z\) | 3 | 1 |
| \((1,2)\) | \(\langle x_1,z_{12},z_{13}\rangle\) | 3 | \(qQ\) |
| \((1,3)\) | \(\langle x_1,Z\rangle\) | 4 | \(Q\) |
| \((2,3)\) | \(\langle x_1,x_2,Z\rangle\) | 5 | \(Q\) |
| \((3,3)\) | \(L\) | 6 | 1 |

Here \(u=\dim((I+Z)/Z)\) and \(w=\dim(I\cap Z)\) for the ideal \(I\). In particular, the total number of ideals and the ideal-dimension enumerator are
\[
N_L(q)=q^3+5q^2+5q+7,
\qquad P_L(t)=1+Qt+Qt^2+(1+qQ)t^3+Qt^4+Qt^5+t^6.
\]
The polynomial satisfies \(t^6P_L(t^{-1})=P_L(t)\). Both the orbit classification and its polynomial consequences hold in characteristic two as well as in odd characteristic, and over nonprime finite fields.

## Assumptions and scope

The ground field is an arbitrary finite field of order \(q=p^e\). The bracket is bilinear, alternating, and makes \(Z\) central; no restriction on the characteristic is imposed. Every ideal means an \(\mathbb F_q\)-linear subspace stable under all brackets with \(L\). The action is by the full group of \(\mathbb F_q\)-linear Lie algebra automorphisms, not just graded automorphisms. The pair \((u,w)\) is intrinsic because \(Z=[L,L]\) is characteristic.

## Proof

**1. Automorphisms.** Every automorphism induces an invertible linear map \(g\in\mathrm{GL}(V)\) on \(L/Z\). Since \([v,w]=v\wedge w\), its restriction to \(Z\) is forced to be \(\bigwedge^2g\). Conversely, for every \(g\in\mathrm{GL}(V)\) and every \(T\in\operatorname{Hom}(V,Z)\), the formula
\[
\phi_{g,T}(v+z)=gv+T(v)+(\bigwedge^2g)z
\]
defines an automorphism. Consequently \(\operatorname{Aut}(L)=\operatorname{Hom}(V,Z)\rtimes\mathrm{GL}(V)\) and its order is \(q^9|\mathrm{GL}_3(q)|\).

**2. Ideal parametrization.** For an ideal \(I\), set \(U=(I+Z)/Z\le V\) and \(W=I\cap Z\le Z\). The ideal condition is exactly
\[
V\wedge U\subseteq W.\tag{1}
\]
Conversely, for every pair \((U,W)\) obeying (1), the subspaces \(I\) with those projection and intersection data are graphs of linear maps \(f:U\longrightarrow Z/W\) after choosing a lift, so there are precisely \(q^{u(3-w)}\) of them. The subgroup of central shears \(\phi_{1,T}\) acts transitively on these graphs: a map \(U\to Z/W\) extends to a map \(V\to Z\), which supplies the required shear. Thus the full orbit problem reduces **without losing the nonhomogeneous ideals** to the \(\mathrm{GL}(V)\)-orbits of pairs \((U,W)\) satisfying (1).

**3. The wedge constraint.** If \(U=0\) then (1) imposes no restriction. If \(\dim U=1\), the map \(V\to\bigwedge^2V\), \(v\mapsto v\wedge u\), has kernel precisely \(U\), so \(\dim(V\wedge U)=2\). If \(\dim U\ge2\), choose two independent vectors in \(U\); their wedges with a basis of \(V\) span all three dimensions of \(Z\). Hence \(V\wedge U=Z\). The only possibilities for \((u,w)\) are exactly the eight pairs in the table.

**4. Transitivity and orbit sizes.** The group \(\mathrm{GL}_3(q)\) is transitive on lines and planes of \(V\). The three-dimensional representation \(\bigwedge^2V\) is canonically \(V^*\otimes\det V\), so it is also transitive on lines and planes of \(Z\). When \((u,w)=(1,2)\), the plane \(W=V\wedge U\) is uniquely determined by the line \(U\). Thus for every admissible pair type there is exactly one \(\mathrm{GL}(V)\)-orbit. There are \(Q\) lines and \(Q\) planes in a three-dimensional vector space. Only the \((1,2)\)-stratum has nontrivial graph lifts, namely \(q\) per choice of \(U\). This gives the exact orbit sizes in the table, with every value arising from distinct ideals. Summing the eight orbit sizes yields \(3+(q+4)Q=q^3+5q^2+5q+7\), and sorting the counts by ideal dimension gives \(P_L(t)\).

**5. Dimension symmetry.** Choose a nonzero volume form \(\operatorname{vol}:\bigwedge^3V\to\mathbb F_q\). Define a symmetric nondegenerate bilinear form on \(L\) by
\[
B(v+z,v'+z')=\operatorname{vol}(v\wedge z'+v'\wedge z).
\]
Directly from exterior associativity, \(B([a,b],c)=B(a,[b,c])\) for all \(a,b,c\in L\). The orthogonal complement of any ideal is therefore another ideal, and this involution interchanges dimensions \(d\) and \(6-d\). This independently explains the displayed reciprocity, including in characteristic two.

## Verification

The accompanying dependency-free `verify.py` enumerates **all** \(2825\) linear subspaces of \(\mathbb F_2^6\) and **all** \(56632\) linear subspaces of \(\mathbb F_3^6\) using unique reduced-row-echelon bases. It tests closure under brackets with three generators, determines every \((u,w)\) stratum, and independently constructs the automorphism orbits by breadth-first search with elementary \(\mathrm{GL}_3\) generators and central shears. The respective ideal totals are \(45\) and \(94\); the orbit sizes are \((1,1,1,7,7,7,7,14)\) and \((1,1,1,13,13,13,13,39)\). The script prints `VERIFY_OK` upon success. The symbolic proof above, not the finite computations, establishes the result for all prime powers.

## Relationship to prior work

Kofinas and Papistas (2010) study generators for automorphism groups of relatively free nilpotent Lie algebras over \(\mathbb Q\), establishing historical automorphism context. The full text was not accessible for comparison here, but its published abstract does not assert the present finite-field ideal-orbit classification. Voll (2004/2005), whose open preprint was examined through its introduction, main theorem and proof, computes **normal-subgroup zeta functions** for all finitely generated free class-two nilpotent groups, including rank three, by counting finite-index objects. Thus *aggregate ideal-enumeration questions have substantial prior coverage*. The result claimed here is specifically the uniform **complete automorphism-orbit decomposition** of the finite-field six-dimensional Lie algebra, with each exact orbit size and ideal dimension, not the zeta-function machinery or the existence of polynomial ideal counts. Known methods for enumerating all ideals do not by themselves identify equivalence classes under the full automorphism group.

## Limitations

This is a classification of ideals of the particular six-dimensional Lie algebra \(L\); it does not classify ideals at higher nilpotency class, higher free rank, or arbitrary finite-index lattices over local rings. No uniqueness claim is made against unpublished work or all possible synonyms in the literature. The full text of a relevant automorphism paper was not obtained; overlap with an unlocated equivalent classification remains a bibliographic risk. The checks over two small prime fields do not independently certify the infinite family. 
## References

1. C. E. Kofinas and A. I. Papistas, *Automorphisms of Relatively Free Nilpotent Lie Algebras*, Communications in Algebra **38** (2010), 1575–1593. DOI: `10.1080/00927870903004360`, publicly online 2010-04-07. https://doi.org/10.1080/00927870903004360
2. C. Voll, *Normal subgroup growth in free class-2-nilpotent groups*, arXiv:math/0409383v1 (2004), later Math. Ann. **332** (2005), 67–79. https://arxiv.org/abs/math/0409383
