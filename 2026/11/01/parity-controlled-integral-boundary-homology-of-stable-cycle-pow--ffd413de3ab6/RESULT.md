# Parity-controlled integral boundary homology of stable cycle-power clique complexes

## Finding
For integers \(m\ge3\) and \(n\ge3m+1\), let \(C_n^m\) be the \(m\)-th graph power of the \(n\)-cycle, let \(M_{n,m}=|\operatorname{Cl}(C_n^m)|\), and let \(B_{n,m}=\partial M_{n,m}\) be its **PL manifold boundary**, equipped with the canonical induced boundary triangulation. Put \(\epsilon_{n,m}=(-1)^{n(m+1)}\). Then:

1. \(M_{n,m}\) is orientable if and only if \(\epsilon_{n,m}=1\), equivalently \(m\) is odd or \(n\) is even. Its boundary \(B_{n,m}\) is connected for every \(m\ge3\).
2. For \(m=3\), \(B_{n,3}\) is PL homeomorphic to the two-dimensional torus \(S^1\times S^1\), for **every** \(n\ge10\).
3. For \(m\ge4\), the complete integral homology of \(B_{n,m}\) is, in the orientable case \(\epsilon_{n,m}=1\),
\[
H_i(B_{n,m};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i\in\{0,1,m-2,m-1\},\\
0,&\text{otherwise},
\end{cases}
\]
and, in the nonorientable case \(\epsilon_{n,m}=-1\),
\[
H_i(B_{n,m};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i\in\{0,1\},\\
\mathbb Z/2\mathbb Z,&i=m-2,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, every even \(m\ge4\) and odd \(n\ge3m+1\) produces a connected, closed, nonorientable PL \((m-1)\)-manifold with a **single integral two-torsion homology group**, in degree \(m-2\), despite the torsion-free circle homotopy type of the bounding manifold.

## Assumptions and scope
Graph powers use shortest-path distance. Vertices are \(\mathbb Z/n\mathbb Z\). For the specified range, the maximal simplices of \(\operatorname{Cl}(C_n^m)\) are the \(n\) cyclic windows \(F_j=\{j,j+1,\ldots,j+m\}\), and the clique complex is a connected triangulated \(m\)-manifold with nonempty boundary, as established by Wani [1]. The fact that the whole clique complex is homotopy equivalent to a circle follows from Adamaszek's girth theorem [2] (alternatively from the induced-complex theorem of [1]). The present theorem uses these two established inputs, and determines the previously unspecified **integral boundary homology and orientation character**. The boundary means the PL manifold boundary, not the boundary of an abstract simplex or the Alexander dual. All homology groups use integral coefficients.

## Proof
**1. Exact orientation character.** Give each oriented maximal simplex \(F_j\) the increasing cyclic-window order \([j,j+1,\ldots,j+m]\), read as integers before reduction modulo \(n\). Since \(n\ge3m+1\), two distinct maximal windows share a codimension-one simplex exactly when their indices differ by one modulo \(n\). Indeed, neighboring windows share exactly their \(m\) middle vertices, while any other pair shares at most \(m-1\). Hence the dual adjacency graph of top-dimensional simplices is precisely the \(n\)-cycle.

The interior codimension-one face shared by \(F_j\) and \(F_{j+1}\) is \([j+1,\ldots,j+m]\). It has incidence sign \(+1\) in the boundary of the oriented \(F_j\) (delete first vertex) and sign \((-1)^m\) in the boundary of the oriented \(F_{j+1}\) (delete last vertex). For a coherent orientation with coefficients \(c_j\in\{+1,-1\}\), interior cancellation therefore requires
\[
 c_{j+1}=(-1)^{m+1}c_j.
\]
Going once around the dual cycle gives \(c_{j+n}=(-1)^{n(m+1)}c_j\). Thus a coherent orientation exists if and only if \(\epsilon_{n,m}=+1\). Because the dual graph is connected, failure of this consistency condition really is nonorientability. This also explicitly determines the orientation local system on the fundamental circle: trivial when \(\epsilon_{n,m}=+1\), and the unique nontrivial sign system when \(\epsilon_{n,m}=-1\).

**2. Relative homology.** Write \(M=M_{n,m}\), \(B=B_{n,m}\), and \(\mathcal O\) for the integral orientation local system on \(M\). The triangulated PL manifold with boundary admits Poincaré–Lefschetz duality with local coefficients:
\[
 H_j(M,B;\mathbb Z)\cong H^{m-j}(M;\mathcal O).
\]
Since \(M\simeq S^1\), cellular cohomology with the pulled-back orientation system is the cohomology of the two-term cochain complex
\[
 \mathbb Z\ \xrightarrow{\ \epsilon_{n,m}-1\ }\ \mathbb Z
\]
in degrees zero and one. Thus if \(\epsilon_{n,m}=+1\), the only nonzero relative groups are \(H_m(M,B)\cong\mathbb Z\) and \(H_{m-1}(M,B)\cong\mathbb Z\). If \(\epsilon_{n,m}=-1\), the only nonzero relative group is \(H_{m-1}(M,B)\cong\mathbb Z/2\mathbb Z\). These statements hold for all \(m\ge3\), with no finite-case extrapolation.

**3. Long exact sequence and connectedness.** The ordinary homology of \(M\simeq S^1\) is \(H_0(M)=H_1(M)=\mathbb Z\), and vanishes above degree one. Because \(m\ge3\), the relative group \(H_1(M,B)\) vanishes. The pair sequence then shows \(H_0(B)\to H_0(M)\) is an isomorphism, proving \(B\) connected.

For \(m\ge4\), the degrees \(1\) and \(m-2\) are distinct, so the long exact sequence gives \(H_1(B)=\mathbb Z\), \(H_{m-1}(B)\cong H_m(M,B)\), and \(H_{m-2}(B)\cong H_{m-1}(M,B)\), with all remaining reduced groups zero. Substitute the groups obtained in step 2 to get the two displayed formulas. When \(m=3\), orientability is automatic; the pair sequence instead gives an extension \(0\to\mathbb Z\to H_1(B)\to\mathbb Z\to0\), which splits because \(\mathbb Z\) is free. Also \(H_2(B)=\mathbb Z\), \(H_0(B)=\mathbb Z\). Thus \(B\) is a connected closed orientable PL surface of genus one by the classification of closed surfaces, and is PL homeomorphic to the torus. All asserted boundary homology groups and the torus conclusion follow.

## Verification
The standalone program `verify.py` constructs every cyclic window and the induced simplicial boundary and computes signed simplicial incidence matrices over the integers. It verifies the number of boundary facets, rational Betti ranks, and nonunit Smith invariant factors of the top incidence matrix for five test pairs: \((n,m)=(10,3),(11,3),(13,4),(14,4),(16,5)\). The odd-order, even-power example \((13,4)\) has a Smith invariant factor \(2\), whereas \((14,4)\) has none. These checks corroborate, but do not prove, the all-parameter statements. The proof uses the cited manifold and circle-homotopy theorems plus an exact orientation computation, duality and the pair sequence.

## Relationship to prior work
Wani [1, Theorem 4.5] establishes that these clique complexes are triangulated manifolds with boundary, and distinguishes annulus from Möbius band for \(m=2\). That paper does not specify the all-parameter orientation character or the integral homology of higher-dimensional boundaries. Adamaszek [2] establishes the ambient clique complex's circle homotopy type in the stable girth range, without computing its manifold boundary. A related published calculation of open-neighborhood complexes of third-power cycles concerns a **different simplicial functor**: its parity-dependent sphere-bundle homology neither identifies nor computes the boundaries considered here. Generic sphere-bundle triangulations are likewise not, without further identification, statements about the boundary of these specific cyclic clique complexes. The new input is the explicit orientation transport around the cyclic facet dual graph and its uniform consequences for the integral topology of the boundary.

## Limitations
The result requires \(n\ge3m+1\) and \(m\ge3\), and its manifold claim relies on [1] while its ambient homotopy claim relies on [2]. It determines integral homology, not the full higher-dimensional PL homeomorphism type or a fiber-bundle structure of the boundary for \(m\ge4\). It does not calculate a dihedral equivariant homology representation. Other unindexed results could provide equivalent information.

## References
[1] B. A. Wani, *Edge ideals of complements of a class of circular interval graphs*, arXiv:2609.31105, first public version 2026-09-25, especially Theorem 4.5. https://arxiv.org/abs/2609.31105

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public version 2011-04-03, especially Proposition 2.2. https://arxiv.org/abs/1104.0433
