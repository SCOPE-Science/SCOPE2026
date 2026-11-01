# Integral congruence lattice of the 315 syzygetic tetrads of a plane quartic

## Finding
Let \(C\) be any smooth nonhyperelliptic curve of genus three over an algebraically closed field of characteristic different from \(2\), and let \(B\) be its \(28\) bitangents. Write \(\mathcal T\) for its \(315\) syzygetic tetrads (four bitangents whose eight tangency points lie on a conic). Let \(L\subset\mathbb Z^B\) be the integer span of the incidence vectors \(e_T=\sum_{b\in T}e_b\), for \(T\in\mathcal T\).

Choose an even theta characteristic as origin, and a symplectic coordinate system \(V=\mathbb F_2^6\) so the induced even quadratic form is
\[
q(v)=v_0v_3+v_1v_4+v_2v_5.
\]
The \(28\) odd theta characteristics, hence the bitangents, are indexed by \(B=\{v\in V:q(v)=1\}\). Then
\[
\boxed{L=\left\{z\in\mathbb Z^B:\ \sum_{v\in B}z_v\equiv0\pmod4,\quad \sum_{v\in B}z_vv=0\text{ in }\mathbb F_2^6\right\}.}
\]
In particular,
\[
\boxed{\mathbb Z^B/L\cong\mathbb Z/4\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^6,\qquad
\operatorname{SNF}(I_{28\times315})=\operatorname{diag}(1^{21},2^6,4).}
\]
The index is \(256\). These statements concern the *formal incidence lattice*, not a torsion assertion in the Jacobian or the Picard group.

## Assumptions and scope
The ground field is algebraically closed of characteristic unequal to \(2\). The smooth canonical plane quartic has distinct geometric bitangents corresponding to its \(28\) odd theta characteristics. A choice of an even theta characteristic identifies the affine theta-torsor with the six-dimensional symplectic vector space \(V\); a symplectic basis identifies its quadratic refinement with \(q\) displayed above. A syzygetic tetrad consists of four *distinct* bitangents, and can be recognized combinatorially as four odd vectors whose sum in \(V\) is zero. The resulting lattice is invariant, up to coordinate relabeling, under changes of these auxiliary choices.

## Proof
**(1) Theta-coordinate description.** Fix the quadratic refinement \(q\) of the Weil pairing with Arf invariant zero. There are exactly \(28\) elements \(v\in V\) with \(q(v)=1\). A four-element subset \(\{a,b,c,d\}\subset B\) is syzygetic precisely when \(a+b+c+d=0\). To check that this is the classical totally isotropic affine two-plane condition, write \(b=a+u\), \(c=a+v\), \(d=a+u+v\). Since all four vectors are odd, the polarization formula \(q(x+y)=q(x)+q(y)+\langle x,y\rangle\) gives \(\langle u,v\rangle=0\). Conversely such an odd affine isotropic plane satisfies the four-sum condition. Enumerating the four-subsets of the 28 odd vectors yields precisely 315 tetrads.

**(2) A containing congruence kernel.** Define the homomorphism
\[
\Phi:\mathbb Z^B\longrightarrow\mathbb Z/4\mathbb Z\oplus\mathbb F_2^6,\quad
z\longmapsto\left(\sum_{v\in B}z_v\bmod4,\sum_{v\in B}(z_v\bmod2)v\right).
\]
Every tetrad has four members and vector sum zero, so \(L\subseteq\ker\Phi\). The 28 augmented vectors \((1,v)\in\mathbb F_2^7\), for \(v\in B\), span \(\mathbb F_2^7\): this is verified by binary elimination in `VERIFY.py`, which constructs the entire explicitly specified 28-element set and tests rank seven. To see that this implies **surjectivity of \(\Phi\)**, first solve for an arbitrary prescribed pair consisting of total parity and six binary moments using the seven independent binary rows; then, if the total modulo four has the incorrect lift of its parity, add \(2e_v\) for any \(v\in B\). This shifts the total by two and does not change its binary moments. Hence
\[
[\mathbb Z^B:\ker\Phi]=4\cdot2^6=256.
\]

**(3) A determinant attaining that index.** Number odd vectors by their usual integers \(0,\ldots,63\), with the low three bits representing \(v_0,v_1,v_2\) and the high three bits \(v_3,v_4,v_5\), and sort them increasingly. Enumerate all strictly increasing quadruples of these odd integers lexicographically, retaining exactly those whose bitwise XOR is zero. In that resulting ordered list of 315 tetrads, take the following **zero-based** indices:

`122, 307, 8, 149, 220, 93, 262, 49, 259, 135, 256, 4, 187, 285, 201, 15, 69, 123, 227, 58, 240, 63, 218, 222, 51, 202, 46, 82`.

Place the corresponding 28 incidence vectors in columns, with odd vectors in increasing order as rows. Exact fraction-free integer elimination (fully specified in `VERIFY.py`) gives determinant \(-256\) for this \(28\times28\) submatrix. Its columns generate a full-rank sublattice of index \(256\) contained in \(L\). Combining
\[
L\subseteq\ker\Phi\quad\text{and}\quad
[\mathbb Z^B:\ker\Phi]=256
\quad\text{and}\quad
[\mathbb Z^B:L]\le256
\]
forces \(L=\ker\Phi\).

**(4) Elementary divisors.** The first isomorphism theorem gives \(\mathbb Z^B/L\cong\mathbb Z/4\oplus(\mathbb Z/2)^6\). Since the incidence lattice has full rank \(28\), its integer incidence matrix has Smith factors comprising 21 units, six factors of two and one factor of four.

## Verification
Run `python3 VERIFY.py` using Python 3 standard library only. The program lists all 28 odd vectors and all 315 XOR-zero tetrads, verifies the 2-design parameters \(2\text{-}(28,4,5)\), computes the augmented mod-two rank seven, constructs the specified 28-column witness, and computes its determinant \(-256\) via exact Bareiss elimination. It asserts each numerical identity and prints `VERIFY_OK` only when all checks hold. These finite computations are exhaustive because both index sets are explicitly and completely enumerated; the infinite integer-lattice conclusion follows from the index sandwich in the proof, not from a bounded search over lattice points.

## Relationship to prior work
The bitangent/theta geometry, syzygetic tetrads, and their number \(315\) are classical: see Manivel (2005) and Bergvall (2021). Crnković and Mikulić Crnković (2011) study an isomorphic \(2\text{-}(28,4,5)\) block design from \(\mathrm{Sp}(6,2)\). Those results provide the geometric and combinatorial incidence configuration itself. The present assertion is the *integral span and its exact congruence presentation*, including all Smith invariant factors. This is not a new 315-block enumeration, and the design parameters by themselves do not determine the asserted integral cokernel. Searches and material inspected did not locate the exact integral membership criterion, though older lattice/coding literature may contain an equivalent description.

## Limitations
This is a theorem about a finite integral incidence module attached to geometric bitangents. It does not claim a new classification of syzygetic tetrads, new Picard or Jacobian torsion, or an extension to characteristic two. Historical priority for the exact Smith form has not been independently settled, especially among coding-theoretic or classical design studies. The proof is exact and self-contained conditional only on the standard theta-characteristic/tetrad correspondence explained above.

## References
1. Laurent Manivel, *Configurations of lines and models of Lie algebras*, arXiv:math/0507118v1, first posted 2005-07-06, https://arxiv.org/abs/math/0507118.
2. Olof Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, https://arxiv.org/abs/2106.13072 (preprint), and *European Journal of Mathematics*, DOI:10.1007/s40879-023-00711-3 (section on syzygetic tetrads).
3. Dean Crnković and Vedrana Mikulić Crnković, *On Some Combinatorial Structures Constructed from the Groups L(3, 5), U(5, 2), and S(6, 2)*, *International Journal of Combinatorics* (2011), DOI:10.1155/2011/137356.
