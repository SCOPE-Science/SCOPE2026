# Arithmetic splitting criterion for cyclic automorphism extensions of simple evolution algebras

## Finding

For every integer \(m\ge3\) and \(h\ge2\), put \(M=2^h-1\). Let \(k\) be a field containing a primitive \(M\)-th root of unity \(\xi\). Fix \(0\le r<M\), set \(a=\xi^r\), and assume \(1-(-1)^m a\ne0\). Define a commutative evolution algebra \(E=E(m,h,r;k)\) with natural basis \(\{e_{i,j}:i\in\mathbb Z/m\mathbb Z,\ 0\le j<h\}\) by vanishing products between distinct basis elements and the squares
\[
 e_{i,0}^{2}=e_{i,1}+c_i e_{i+1,1},\qquad
 e_{i,j}^{2}=e_{i,j+1}\quad(1\le j<h-1),\qquad
 e_{i,h-1}^{2}=e_{i,0},
\]
where \(c_{m-1}=a\) and every other \(c_i=1\). All subscripts in the first coordinate are reduced modulo \(m\).

Then \(E\) is simple and perfect. Its full group of ordinary \(k\)-linear algebra automorphisms is abelian of order \(mM\), with exact invariant factors
\[
 \operatorname{Aut}_k(E)\cong C_g\times C_{mM/g},\qquad g=\gcd(m,M,r).
\]
The associated exact sequence between diagonal automorphisms, all automorphisms, and their induced cyclic permutations is
\[
 1\longrightarrow C_M\longrightarrow\operatorname{Aut}_k(E)
 \longrightarrow C_m\longrightarrow1,
\]
and **splits if and only if** \(\gcd(m,M)\mid r\). In particular, when \(r=1\) the group is cyclic \(C_{mM}\) and the extension is nonsplit exactly when \(\gcd(m,M)>1\). For every odd prime \(p\), choosing \(m=p\), \(h=\operatorname{ord}_p(2)\) and \(r=1\) yields a simple perfect nonsplit example.

## Assumptions and scope

The ground field is arbitrary apart from containing the indicated primitive root of unity. The condition \(1-(-1)^m a\ne0\) is essential: it makes the structure matrix invertible. This classification concerns ordinary automorphisms over \(k\), not the entire automorphism group scheme over arbitrary coefficient rings. The integer \(r\) is taken modulo \(M\), and \(m\ge3\), \(h\ge2\) throughout.

## Proof

**1. Perfectness, simplicity, and support graph.** Ordering the natural basis by the first coordinate and then the second, all but one layer of the structure matrix are permutation layers. Their elimination reduces invertibility to that of the cyclic \(m\)-by-\(m\) matrix whose row \(i\) has a \(1\) in column \(i\) and \(c_i\) in column \(i+1\). Its determinant is \(1-(-1)^m\prod_i c_i=1-(-1)^m a\). Thus the squares form a basis and \(E^2=E\).

The support graph has a directed internal cycle of length \(h\) in each block \(i\) and a cross-arrow from its \(j=0\) vertex to the next block's \(j=1\) vertex. It is strongly connected: every block can reach the next block along that cross-arrow and the remaining internal arrows. If a nonzero ideal contains an element with a nonzero coordinate at a vertex, multiplying by that basis vector shows it contains that vertex's square. Multiplying further by the basis vectors occurring in the square follows the outgoing arrows; strong connectivity forces the ideal to contain every basis square, and hence all of \(E\). Therefore \(E\) is simple.

**2. All automorphisms are monomial and induce rotations.** For distinct natural-basis elements \(e_v,e_w\), an automorphism satisfies \(\phi(e_v)\phi(e_w)=0\). Since the family of basis squares is linearly independent, the supports of the column vectors \(\phi(e_v)\) and \(\phi(e_w)\) are disjoint. Invertibility forces each column to have exactly one nonzero entry. Therefore every automorphism is monomial, and its permutation preserves the directed support graph.

Precisely the vertices \((i,0)\) have outdegree two. Each other vertex has outdegree one. The unique directed internal path from \((i,1)\) through \((i,h-1)\) ends at \((i,0)\), while the other outgoing neighbor of \((i,0)\) leads to the next block. Accordingly, a graph automorphism preserves the internal block pairing and the orientation of the induced directed \(m\)-cycle. It is thus a common rotation \((i,j)\mapsto(i+s,j)\), and every \(s\in\mathbb Z/m\mathbb Z\) is a support-graph rotation.

**3. Diagonal kernel and one rotation lift.** Fix a monomial automorphism with block shift \(s\). Write \(\phi(e_{i,j})=t_{i,j}e_{i+s,j}\). The internal-square identities give \(t_{i,j}=t_i^{2^j}\), with \(t_i=t_{i,0}\), and \(t_i^{2^h-1}=t_i^M=1\). The cross-square identities are exactly
\[
 c_i t_{i+1}^{2}=c_{i+s}t_i^2\qquad(i\bmod m).
\]
For \(s=0\), they imply \(t_{i+1}=t_i\), because the squaring map is a bijection on the group \(\mu_M(k)=\langle\xi\rangle\) of odd order \(M\). The diagonal kernel therefore consists precisely of \(d^v(e_{i,j})=\xi^{v2^j}e_{i,j}\), with \(d\) of order \(M\).

Let \(u\) denote the inverse of \(2\) modulo \(M\). A lift of the one-step rotation is
\[
 \phi(e_{i,j})=c_i^{u2^j}e_{i+1,j}.
\]
The displayed cross-square identities hold because \((c_i^u)^2=c_i\). Hence this defines an automorphism, and the image of the permutation map is the entire \(C_m\). The diagonal automorphism \(d\) commutes with \(\phi\). Taking the \(m\)-th power of the lift multiplies the coefficient on \(e_{i,0}\) by \(\prod_i c_i^u=a^u=\xi^{ur}\), whence \(\phi^m=d^{ur}\).

**4. Group structure and splitting.** Every automorphism is uniquely \(d^v\phi^s\), with \(0\le v<M\) and \(0\le s<m\): the one-step lift realizes every shift, and the kernel is generated by \(d\). Therefore
\[
 \operatorname{Aut}_k(E)=\langle d,\phi\mid d^M=1,\ d\phi=\phi d,\ \phi^m=d^{ur}\rangle.
\]
The Smith normal form of the relation matrix has invariants \(g=\gcd(M,m,ur)=\gcd(M,m,r)\) and \(mM/g\), proving the group formula. The quotient extension splits exactly when there exists an order-dividing-\(m\) lift \(d^v\phi\), equivalent to the congruence \(mv+ur\equiv0\pmod M\), which is soluble precisely when \(\gcd(m,M)\mid r\). The prime-family assertion follows because \(p\mid(2^{\operatorname{ord}_p(2)}-1)\) and \(r=1\) makes the invertibility condition automatic.

## Verification

The standalone `verify.py` checks finite prime-field instances using independent structure-matrix rank calculations, every defining multiplication identity for the exhibited rotation, and direct enumeration of all monomial coefficient assignments for the smaller cases. It compares the complete distribution of element orders with the predicted invariant factors. For those cases, a separate graph-isomorphism enumeration checks that the support-graph automorphism group has order \(m\). The tested cases include both split and nonsplit extensions, multiple twists, and \(h=2,3,4\). Its recorded output is in `verify_output.txt` and ends in `VERIFY_OK`. An independent characteristic-two arithmetic implementation in `verify_char2.py` exhaustively verifies the nonsplit case over \(\mathbb F_4\), with output in `verify_char2_output.txt`. These finite tests corroborate, but do not replace, the proof for arbitrary parameters and fields.

## Relationship to prior work

Elduque and Labra established the graph/diagonal exact-sequence framework for perfect evolution algebras; their general results do not provide the arithmetic evaluation of the family here. Cabrera Casado and collaborators studied diagonal and weighted-graph descriptions of automorphism groups and supply a broad approach; the present invariant-factor and splitting formulas are a computation for a concrete weighted family rather than a new general monomiality theorem. Kaygorodov, Martín González, and Viruel gave a single six-dimensional nonsplit \(C_3\)-by-\(C_3\) example in Proposition 21 and explicitly asked for splitting criteria in Question 33. Here, \(m=3,h=2,r=1\) reproduces the same group extension type \(C_9\) (without claiming that the displayed natural-basis presentation equals theirs); the general family supplies arbitrarily many additional group orders and a complete parameterwise criterion.

## Limitations

No claim is made about all perfect evolution algebras, arbitrary graph automorphism groups, or the group scheme over all base rings. The construction requires the stated root of unity and nonvanishing determinant. The split criterion is complete only within this family. Prior literature may contain a more general weighted-graph principle from which the formulas could be derived; the historical priority of the special arithmetic family is not independently established.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first publicly posted 2026-10-15), Proposition 21 and Question 33. https://arxiv.org/abs/2610.22248
2. A. Elduque, A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191v1 (2019). https://arxiv.org/abs/1902.02191
3. Y. Cabrera Casado, M. I. Cardoso Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González, I. Ruiz Campos, *Solenoids in automorphism groups of evolution algebras*, arXiv:2505.14584v1 (2025), Theorem 6.17 and Corollary 6.19. https://arxiv.org/abs/2505.14584
4. C. Costoya, P. Mayorga, A. Viruel, *Permutation representations and automorphisms of evolution algebras*, Mediterranean Journal of Mathematics (2025), DOI:10.1007/s00009-025-02924-0.
