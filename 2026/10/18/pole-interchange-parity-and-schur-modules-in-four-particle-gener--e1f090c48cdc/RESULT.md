# Pole-interchange parity and Schur modules in four-particle generalized-theta homology

## Finding
For every integer \(k\ge 3\), let \(\Theta_k\) be the graph with two vertices joined by \(k\) parallel topological edges. Write \(B_4(\Theta_k)\) for its space of *unordered* configurations of four distinct points and
\[
A_k=\ker\!\left(\mathbb Q^k\xrightarrow{\,\sum\,}\mathbb Q\right).
\]
Permuting the edges and interchanging the two poles gives an action of \(S_k\times C_2\). Denote the trivial and nontrivial rational characters of the pole-interchange factor by \(\mathbf1\) and \(\varepsilon\), respectively. For Schur functors \(\mathbb S_\lambda\), there is an isomorphism of rational \(S_k\times C_2\)-modules
\[
\boxed{H_2(B_4(\Theta_k);\mathbb Q)\cong
\left(\bigwedge^3 A_k\oplus\mathbb S_{(2,1,1)}A_k\right)\boxtimes\mathbf1
\ \oplus\ \mathbb S_{(2,2)}A_k\boxtimes\varepsilon.}
\]
Here a Schur functor whose partition has more than \(k-1\) rows is zero. In particular, putting \(m=k-1\), the dimensions of the pole-even and pole-odd eigenspaces are, respectively,
\[
\binom m3+\frac{m(m+1)(m-1)(m-2)}8,
\qquad\frac{m^2(m^2-1)}{12}.
\]
Thus the pole-even/pole-odd ranks for \(k=3,4,5,6\) are \((0,1)\), \((4,6)\), \((19,20)\), and \((55,50)\). Moreover, the pole-even submodule is exactly the image of all edge-stabilization maps from three-particle degree-two homology, while the pole-odd submodule has zero intersection with the edge-stabilized image. In particular, already for the three-arm theta graph the four-particle second homology is one-dimensional and **pole-odd**, even though its three-particle second homology vanishes.

## Assumptions and scope
The graph may be subdivided without changing its homeomorphism type or the homology of its configuration space. The two distinguished endpoints have valence \(k\); the \(k\) open edges are permuted without orientation signs. Interchanging the endpoints reverses every open edge but does not permute the unordered particles. The coefficient field is \(\mathbb Q\); no integral-torsion or equivariant integral-lattice statement is asserted. The partitions \((2,1,1)\) and \((2,2)\) index polynomial general-linear-group Schur functors evaluated on the \(S_k\)-module \(A_k\), not Specht modules of those partition sizes. The displayed isomorphism concerns exactly four particles and homological degree two.

## Proof
**1. A functorial chain model.** The reduced Świątkowski complex computes graph-configuration homology and is natural for graph isomorphisms. At either pole, its local degree-one half-edge differences form the augmentation module \(U=A_k\). Let \(E=\mathbb Q^k\) with basis the edge variables. A half-edge difference corresponding to \(a\in U\) has differential the linear polynomial \(a\in E\subset\operatorname{Sym}(E)\). The two poles are the only nontrivial local factors. At particle weight four, the chain groups in homological degrees two and one are
\[
C_2=U\otimes U\otimes\operatorname{Sym}^2(E),\qquad
C_1=(U\oplus U)\otimes\operatorname{Sym}^3(E).
\]
There is no degree-three group. Therefore, the desired homology is the *actual kernel* of the degree-two differential, with no quotient by any incoming differential. Up to the unimportant ordering of the two degree-one summands, this differential is the pair of maps
\[
\mu_1(a\otimes b\otimes f)=b\otimes af,\qquad
\mu_2(a\otimes b\otimes f)=a\otimes bf,
\]
with one of the two components carrying the standard Koszul minus sign. Consequently,
\[
H_2(B_4(\Theta_k);\mathbb Q)=\ker\mu_1\cap\ker\mu_2.
\]
The pole-interchange involution is \(-T\), where \(T\) exchanges the first two tensor factors: the negative sign comes from swapping two degree-one half-edge generators.

**2. Split the edge variables equivariantly.** Set \(t=k^{-1}\sum_{i=1}^k e_i\). The invariant decomposition \(E=\mathbb Qt\oplus U\) gives
\[
\operatorname{Sym}^2(E)=\mathbb Qt^2\oplus tU\oplus\operatorname{Sym}^2U.
\]
Since \(\mu_1\) and \(\mu_2\) multiply by elements of \(U\), the three summands contribute independent kernels, distinguished by their exponent of \(t\). On \(U\otimes U\otimes t^2\), either multiplication map is injective and the common kernel is zero.

On \(U\otimes U\otimes tU\), the common kernel is the intersection of the kernels of symmetrization in tensor-factor pairs \((1,3)\) and \((2,3)\). In characteristic zero this is precisely the alternating tensor subspace \(\bigwedge^3U\). Its first-two-factor flip is negative, so pole interchange \(-T\) acts by \(+1\).

**3. Two polarized multiplication maps.** The remaining contribution lies in \(U\otimes U\otimes\operatorname{Sym}^2U\). Splitting the pole factors into \(\operatorname{Sym}^2U\) and \(\bigwedge^2U\) reduces the common-kernel condition to just \(\mu_1=0\) on each flip-eigenspace: applying the flip turns \(\mu_1\) into \(\mu_2\), up to the same eigensign.

Over \(\mathbb Q\), the Littlewood--Richardson decompositions are
\[
\operatorname{Sym}^2U\otimes\operatorname{Sym}^2U
\cong\mathbb S_{(4)}U\oplus\mathbb S_{(3,1)}U\oplus\mathbb S_{(2,2)}U,
\]
\[
\bigwedge^2U\otimes\operatorname{Sym}^2U
\cong\mathbb S_{(3,1)}U\oplus\mathbb S_{(2,1,1)}U,
\]
and the target \(U\otimes\operatorname{Sym}^3U\cong\mathbb S_{(4)}U\oplus\mathbb S_{(3,1)}U\). In the symmetric source, multiplication maps both the \(\mathbb S_{(4)}\) and \(\mathbb S_{(3,1)}\) summands nontrivially onto their respective unique target copies: full symmetrization exhibits the first; a tensor \((a\otimes b+b\otimes a)\otimes c^2\) with independent \(a,b,c\), or the corresponding two-variable polarization, has a nonzero \((3,1)\) projection. The kernel is therefore \(\mathbb S_{(2,2)}U\). In the antisymmetric source, multiplication has zero total symmetrization but has a nonzero \((3,1)\) image, for example \((a\otimes b-b\otimes a)\otimes a^2\) with independent \(a,b\). Its kernel is \(\mathbb S_{(2,1,1)}U\). These statements include \(\dim U=2\), where the length-three Schur functor vanishes and the remaining nonzero maps still have the displayed ranks.

Under \(-T\), the symmetric pole-factor kernel \(\mathbb S_{(2,2)}U\) is odd and the antisymmetric pole-factor kernel \(\mathbb S_{(2,1,1)}U\) is even. Multiplication by the edge variables maps the weight-three classes \(\bigwedge^3U\) to \(t\bigwedge^3U\) and to the image of \(U\otimes\bigwedge^3U\) inside the weight-four symmetric coefficient component. By the Pieri decomposition \(U\otimes\bigwedge^3U\cong\mathbb S_{(2,1,1)}U\oplus\bigwedge^4U\), that image is precisely \(\mathbb S_{(2,1,1)}U\): it is nonzero on the first summand, as is seen by multiplying an alternating three-tensor by one of its coefficient variables, and the pole-even target contains just one such summand. Thus all pole-even classes, and no pole-odd classes, are generated by stabilization from particle weight three. Combining with step 2 proves the claimed \(S_k\times C_2\)-isomorphism. The hook-content formula gives the displayed dimensions for \(m=\dim U=k-1\), proving the formula for all \(k\ge3\).

## Verification
The accompanying self-contained `verify.py` builds the exact integral-coefficient degree-two boundary matrix of the reduced Świątkowski complex in the basis \(e_i-e_0\) at both poles. It computes its rank modulo the prime \(1000003\) for \(k=3,4,5,6\) and at particle weights three and four. At weight four it also computes the boundary restriction to the eigenspaces of \(-T\), independently checking their dimensions against the rational Schur-module formulas. It returns `VERIFY_OK` after all checks. The second standalone script `verify_stabilization.py` constructs alternating weight-three cycles, verifies their boundaries vanish, multiplies them by every edge variable, and checks that their weight-four span has ranks equal to the whole pole-even eigenspace, returning `STABILIZATION_VERIFY_OK`. The finite-field runs are **checks**, not substitutes for the characteristic-zero and unbounded-arm proof above. The theoretical identification rests on the rational quasi-isomorphism and exact polynomial multiplication kernels; it does not infer a rational rank from a modular rank alone.

## Relationship to prior work
Ghrist and Abrams establish foundational configuration-space topology for graphs. An, Drummond-Cole and Knudsen establish the reduced Świątkowski model used in the proof. An and Knudsen's general planar degree-two generation theorem implies that configurations here are built from toric and theta classes, but does not determine their relations or the four-particle \(S_k\times C_2\)-representation. The 4 October 2026 public note *Complete theta-class relations for three-point generalized theta configurations* identifies \(H_2(B_3(\Theta_k);\mathbb Z)\) with \(\bigwedge^3\ker(\mathbb Z^k\to\mathbb Z)\), and gives its complete theta-class relations. The present claim concerns a different particle weight: its whole pole-even summand is edge-stabilized from the three-particle classes, whereas the pole-odd \(\mathbb S_{(2,2)}A_k\) is not. The complete equivariant decomposition measures exactly this new parity phenomenon. Lütgehetmann and Recio-Mitter analyze banana-graph *ordered* configuration spaces principally for topological complexity; their theorem and spectral-sequence computations do not identify the present unordered four-particle representation. Existing general rank or generator bounds alone do not imply the displayed equivariant decomposition.

## Limitations
The result is rational, not integral; it does not address torsion, explicit geometric cycle representatives for every Schur summand, products in cohomology, homotopy type, or arbitrary particle number. The representation is determined as an abstract equivariant rational module rather than a preferred basis of homology. The literature comparison cannot exclude equivalent computations under terminology absent from the inspected sources. All finite computations concern \(3\le k\le6\), while the proof of the infinite family is algebraic.

## References
1. R. Ghrist, *Configuration spaces and braid groups on graphs in robotics*, arXiv:math/9905023, initially public 1999-05-05.
2. A. Abrams, *Configuration spaces and braid groups of graphs*, PhD thesis, UC Berkeley, 2000-05-01.
3. B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351 (2017), especially the reduced Świątkowski quasi-isomorphism.
4. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020), especially Theorem 1.1 and §2.
5. D. Lütgehetmann and D. Recio-Mitter, *Topological complexity of configuration spaces of fully articulated graphs and banana graphs*, arXiv:1806.00659 (2018), §5.
6. *Complete theta-class relations for three-point generalized theta configurations*, public mathematical record, 2026-10-04.
