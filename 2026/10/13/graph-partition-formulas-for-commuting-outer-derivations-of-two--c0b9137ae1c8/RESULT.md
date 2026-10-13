# Graph-partition formulas for commuting outer derivations of two-arrow quiver algebras

## Finding
Let \(k=\mathbb F_q\), with \(q\) any prime power. Let \(Q\) be a finite loopless quiver in which each nonempty ordered arrow class (fixed source and target) consists of **exactly two parallel arrows**. Put \(A=kQ/J^2\), and regard \(L=\mathrm{HH}^1(A)=\operatorname{Der}_k(A)/\operatorname{Inn}(A)\) as a finite Lie algebra. Form an undirected multigraph \(G\) with the vertices of \(Q\) and one undirected edge for each two-arrow class, retaining edges arising from both opposite directions. Write \(m=|E(G)|\), \(c=\kappa(G)\), and let \(\kappa(S)\) be the number of connected components of the spanning multigraph \((V(G),S)\), including isolated vertices.

The exact probability that two independent uniform elements of \(L\) commute is
\[
\boxed{\Pr_{X,Y\in L}([X,Y]=0)=
\begin{cases}
\displaystyle \left(\frac{q^6+q^5-q^3}{q^8}\right)^m,&\operatorname{char}k\ne2,\\[3mm]
\displaystyle \frac{1}{q^{c+8m}}\sum_{S\subseteq E(G)}q^{\kappa(S)}\,[q^3(q^2-1)]^{m-|S|}\,q^{6|S|},&\operatorname{char}k=2.
\end{cases}}
\]
For \(m=0\), both expressions equal \(1\). The corresponding exact number of ordered commuting pairs is \(q^{2(4m-|V(G)|+c)}\) times the displayed probability.

In characteristic two the answer depends only on the cycle matroid of \(G\), and is a specialization of its multivariate random-cluster (equivalently, Tutte) partition function. In odd characteristic it depends only on \(m\). For example, over \(\mathbb F_2\), an underlying three-edge forest gives probability \(343/4096\), while an underlying triangle gives \(407/8192\), even though both quivers have three two-arrow classes. This is a cycle-sensitive characteristic-two effect in a cohomological Lie-algebra invariant.

## Assumptions and scope
The quiver is finite and loopless; all existing ordered arrow classes have multiplicity exactly two. Oriented cycles, opposite arrow classes, multiple underlying undirected edges, isolated vertices, and disconnected quivers are allowed. The quotient \(J^2\) means the ideal of all paths of length at least two. The Lie bracket on \(L\) is induced by the commutator of derivations. Finite-field cardinality \(q\) includes nonprime prime powers. The formula counts ordered pairs, including zero elements.

## Proof
**1. The Lie quotient.** The vertex subalgebra \(E=\bigoplus_{v\in V(Q)}ke_v\) is separable over \(k\). Every derivation class admits a representative vanishing on \(E\). Such a derivation must send each arrow to a linear combination of arrows with the same source and target: preservation of \(e_uAe_v\), looplessness and \(J^2=0\) exclude vertex and longer-path contributions. Conversely, arbitrary linear maps on each two-dimensional arrow space extend to derivations vanishing on \(E\), because all products of arrows vanish. Therefore normalized derivations form
\[
M=\bigoplus_{e\in E(G)}\mathfrak{gl}_2(k)
\]
with the componentwise matrix commutator. Inner derivations fixing \(E\) are induced by the centralizer of \(E\) in \(A\); looplessness makes this centralizer equal to \(E\). Their action on the arrow class from \(u\) to \(v\) is multiplication by \(\lambda_v-\lambda_u\), times \(I_2\). Thus
\[
L\simeq M/D,\qquad
D=\{((\lambda_v-\lambda_u)I_2)_e:\lambda\in k^{V(G)}\}\subseteq Z(M).
\]
The incidence-map rank is \(|V(G)|-c\), so \(|D|=q^{|V(G)|-c}\) and \(|L|=q^{4m-|V(G)|+c}\).

**2. Scalar commutator fibers of a matrix block.** Let \(C_0\) count \((X,Y)\in M_2(k)^2\) with \([X,Y]=0\). Scalars \(X\) give \(q\cdot q^4\) pairs; each of the \(q^4-q\) nonscalar \(X\) has a two-dimensional centralizer and contributes \(q^2\) choices of \(Y\). Hence
\[C_0=q^6+q^5-q^3.\]
For a fixed nonzero \(t\in k\), let \(C_t\) count pairs with \([X,Y]=tI_2\). When the characteristic is odd, the trace identity gives \(C_t=0\). When the characteristic is two, a scalar \(X\) is impossible. For nonscalar \(X\), the image of \(\operatorname{ad}_X\) is the trace-pairing orthogonal complement of \(\operatorname{span}(I_2,X)\), because the trace pairing is nondegenerate and the kernel of \(\operatorname{ad}_X\) is precisely that span. Thus \(tI_2\) is in the image exactly when \(\operatorname{tr}X=0\). The traceless subspace has \(q^3\) elements, of which \(q\) are scalar, leaving \(q^3-q\) choices of \(X\). Each has \(q^2\) preimages \(Y\). Consequently every nonzero scalar has the same fiber size
\[C_1=q^2(q^3-q)=q^3(q^2-1),\qquad C_0-C_1=q^6.\]
This counting uses ordinary integers for fiber sizes, including in characteristic two.

**3. Passing to the quotient and the graph sum.** A uniform pair in \(L^2\) is the image of a uniform pair in \(M^2\). Its Lie bracket vanishes if and only if its componentwise commutator lies in \(D\). In odd characteristic, any scalar commutator must be zero, so the independent blocks give \((C_0/q^8)^m\).

In characteristic two, the sign in the incidence difference disappears. Each vector of scalar labels in \(D\) has exactly \(q^c\) representing vertex potentials \(\lambda\in k^{V(G)}\), because the kernel is the space of functions constant on graph components. Independence of the \(m\) matrix blocks therefore gives
\[
\Pr([X,Y]=0)
=\frac1{q^{c+8m}}\sum_{\lambda\in k^{V(G)}}
\prod_{e=\{u,v\}\in E(G)}\left(C_1+(C_0-C_1)\mathbf1_{\{\lambda_u=\lambda_v\}}\right).
\]
Expand the product by choosing a subset \(S\) of edges on which equality is enforced. The number of vertex colorings satisfying all those equalities is exactly \(q^{\kappa(S)}\), even for parallel edges and isolated vertices. Using \(C_0-C_1=q^6\) proves the stated finite sum.

**4. Matroid sensitivity.** The subset sum uses only \(m\), \(c\), and \(\kappa(S)\), which are cycle-matroid data (isolated-vertex contributions cancel). For a forest every scalar edge labeling lies in \(D\), giving probability \(((C_0+(q-1)C_1)/q^8)^m\). For the triangle over \(\mathbb F_2\), \(D\) consists of the four even-parity scalar labelings; its weighted count is \(C_0^3+3C_0C_1^2\). Substituting \(C_0=88\), \(C_1=24\) gives the two displayed, unequal fractions. All claims follow.

## Verification
A standalone, standard-library-only checker, `verify.py`, independently enumerates all ordered matrix pairs over fields of orders \(2,3,4,5\), including a genuine degree-two extension field. It checks every scalar commutator fiber against the asserted counts. It then constructs actual quotient Lie-algebra representatives modulo the vertex-scalar coboundaries and enumerates every ordered quotient pair for one-edge quivers over fields of orders \(2,3,4\), and for two-edge paths, three-edge paths, and triangles over \(\mathbb F_2\). Direct quotient counts agree with the forest, cycle and subset-sum predictions. The verified examples include triangle probability \(407/8192\), three-edge forest probability \(343/4096\), and characteristic-two one-edge probability \(7/16\). Run `python3 verify.py` from the directory containing this file and the checker; successful output ends with `VERIFY_OK`. These finite checks do not replace the general proof.

## Relationship to prior work
Strametz (first public preprint 2001-11-06, arXiv:math/0111060) describes \(\mathrm{HH}^1\) of monomial algebras by parallel-path derivations and identifies its Lie bracket. Sánchez-Flores (arXiv:0711.2810, first public 2007-11-18) develops the radical-square-zero Gerstenhaber Lie-module description. These provide structural foundations but do not give the finite-field commuting-pair probability or characteristic-two graph partition formula above. The Feit–Fine enumeration of commuting matrix pairs (1960), reviewed by Fulman–Guralnick (arXiv:1611.05499), covers a single matrix-algebra zero-commutator count; it does not count nonzero scalar commutators surviving in central graph coboundary quotients. Work on solvability of \(\mathrm{HH}^1\), including Rubio y Degrassi–Schroll–Solotar (arXiv:1903.12145), addresses Lie structure rather than this distribution. The new claim is the quotient commuting probability and its graph/characteristic dependence, not the known parallel-arrow Lie description or the classical random-cluster subset expansion in isolation.

## Limitations
The proof does not treat nontrivial loops, arrow multiplicities other than two, or multiplication/commutation in the original associative algebra \(A\). The matroid comparison uses a fixed field and this specific two-arrow family, not arbitrary derived-equivalent algebras. Although relevant accessible manuscripts and indexed scientific records were compared, bibliographic completeness and independent verification are not asserted.

## References
1. C. Strametz, *The Lie algebra structure on the first Hochschild cohomology group of a monomial algebra*, arXiv:math/0111060v1 (2001-11-06), https://arxiv.org/html/math/0111060v2 ; Journal of Algebra and Its Applications 5 (2006), 245–270.
2. S. Sánchez-Flores, *The Lie module structure on the Hochschild cohomology groups of monomial algebras with radical square zero*, arXiv:0711.2810v1 (2007-11-18), https://arxiv.org/html/0711.2810v2 .
3. W. Feit and N. J. Fine, *Pairs of commuting matrices over a finite field*, Duke Mathematical Journal 27 (1960), 91–94.
4. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (2016-11-16), https://arxiv.org/html/1611.05499v1 .
5. L. Rubio y Degrassi, S. Schroll and A. Solotar, *The first Hochschild cohomology as a Lie algebra*, arXiv:1903.12145 (2019-03-28), https://arxiv.org/html/1903.12145v3 .
