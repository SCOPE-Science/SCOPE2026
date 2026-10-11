# Complex-oriented cohomology blindness of the Gong–Li toric fourfolds
## Finding
Let \(B\) be the smooth projective toric threefold with nine fan rays in Gong and Li, arXiv:2609.39707v1, §2.1. In its integral cohomology ring put
\[
u=D_2-D_4+D_6-2D_7-4D_8-D_9,\qquad
v=-D_2-D_4+D_6+D_8+2D_9.
\]
Write \(L_u,L_v\) for line bundles on \(B\) having these first Chern classes and define the smooth projective toric fourfolds
\[
X=\mathbb P(L_u\oplus L_v),\qquad Y=\mathbb P(\mathcal O_B\oplus L_u\otimes L_v).
\]
For every complex-oriented multiplicative generalized cohomology theory \(E\), the assignment fixing \(E^*(B)\) and sending \(c_1^E(S_X^*)\) to \(c_1^E(S_Y^*)\) defines an isomorphism of graded \(E^*(B)\)-algebras \(E^*(X)\cong E^*(Y)\). It preserves the total \(E\)-Chern classes of the complex tangent bundles. For complex topological \(K\)-theory the degree-zero isomorphism preserves the special \(\lambda\)-ring structure. Nevertheless, \(X\) and \(Y\) are not homotopy equivalent.

The mechanism is general: if a finite CW space \(B'\) has free abelian integral cohomology concentrated in even degrees and \(L,M\) are complex line bundles with \(c_1(L)c_1(M)=0\), the corresponding two projectivizations \(\mathbb P(L\oplus M)\) and \(\mathbb P(\mathcal O\oplus L\otimes M)\) have the same base-relative graded cohomology rings for every complex-oriented theory.

## Assumptions and scope
A complex-oriented theory means a unital multiplicative graded-commutative generalized cohomology theory equipped with a complex orientation, hence a commutative one-dimensional formal group law \(F_E\) and a projective-bundle theorem. We work nonequivariantly. The spaces \(X,Y\) are compact smooth complex manifolds; their topological complex tangent bundles carry the usual complex structures. A complex-oriented Chern class is taken in the chosen orientation of \(E\). There is no claim of equivalence of \(E\)-cohomology *spectra*, of an isomorphism induced by a continuous map, of equivariant oriented cohomology, or of operations outside the asserted degree-zero \(K\)-theory \(\lambda\)-structure.

The construction uses the projectivization convention parametrizing lines, with tautological subline \(S\), and \(x=c_1^E(S^*)\). All equalities involving formal power series are evaluated in the nilpotent first Chern classes on finite CW spaces.

## Proof
**1. Exact ordinary product.** The fan has Stanley–Reisner relations \(D_iD_j=0\) for the nonfaces used below and linear relations
\[
D_1-D_2+D_7+D_8=0,\qquad D_3-D_4+D_7+D_8+D_9=0,\qquad D_5-D_6+D_7+2D_8+D_9=0.
\]
A direct integral certificate in the polynomial ring modulo these linear relations is
\[
\begin{aligned}
uv\equiv{}&-D_1D_2+3D_1D_9+D_2D_7+4D_2D_8+D_3D_4-2D_3D_5\\
&+D_4D_7-2D_4D_9+D_5D_6-2D_5D_7-D_6D_7-3D_6D_8+D_7D_9.
\end{aligned}
\]
Every displayed product is a Stanley–Reisner zero monomial, so \(uv=0\in H^4(B;\mathbb Z)\). The certificate is reproduced by `verify_uv.py`. This also independently checks the relevant input from Gong–Li, Lemma 2.1.

**2. Vanishing in universal complex cobordism.** For any finite CW space \(B'\) with free even integral cohomology, the Atiyah–Hirzebruch spectral sequence for \(MU\) collapses for parity reasons: \(H^*(B';\mathbb Z)\) and the coefficient groups \(MU^*(\mathrm{pt})\) are zero in odd degrees. Its surviving groups and successive filtration quotients are free abelian, so every \(MU^k(B')\) is torsion-free. Rationalization embeds \(MU^*(B')\) into \(MU^*(B')\otimes\mathbb Q\); the multiplicative rational Chern–Dold character identifies the latter with ordinary cohomology with rationalized \(MU\) coefficients. Under this identification, \(c_1^{MU}(L)\) for a line bundle with ordinary first Chern class \(a\) becomes a power series in \(a\) with no constant term, and therefore is divisible by \(a\). Consequently, for ordinary classes \(a,b\) with \(ab=0\),
\[
c_1^{MU}(L)c_1^{MU}(M)=0\in MU^4(B').
\]
The ring map induced by the chosen complex orientation \(MU\to E\) gives, for every complex-oriented \(E\),
\[
U=c_1^E(L),\qquad V=c_1^E(M),\qquad UV=0\in E^4(B').
\]
In particular this holds for the displayed \(B,L_u,L_v\).

**3. Formal-group-law identity and projective bundles.** For every formal group law \(F\) with identity zero, the power series
\[
G(x,U,V)=F(x,U)F(x,V)-xF(x,F(U,V))
\]
vanishes when either \(U=0\) or \(V=0\), because \(F(x,0)=x\). Thus every monomial of \(G\) contains both \(U\) and \(V\); equivalently, \(G\in(UV)\) in the universal formal power-series ring. For \(UV=0\) it follows that
\[
F_E(x,U)F_E(x,V)=xF_E(x,F_E(U,V)).
\]
The rank-two complex-oriented projective-bundle theorem gives free \(E^*(B')\)-modules with basis \(\{1,x\}\), with ring presentations
\[
\begin{aligned}
E^*(\mathbb P(L\oplus M))&\cong E^*(B')\llbracket x\rrbracket/(F_E(x,U)F_E(x,V)),\\
E^*(\mathbb P(\mathcal O\oplus L\otimes M))&\cong E^*(B')\llbracket x\rrbracket/(xF_E(x,F_E(U,V))).
\end{aligned}
\]
The two defining relations are identical, so the base classes and the tautological dual first Chern class identify the rings. This simultaneously proves the all-\(E\) assertion. The formal quotients are well-defined because positive-filtration Chern classes are nilpotent on the finite spaces; the projective-bundle theorem also ensures no hidden further relation.

**4. Complex-oriented tangent Chern classes.** For a rank-two projectivization \(\pi:P(W)\to B\) with tautological subline \(S\), the complex relative tangent line has determinant \(\det W\otimes(S^*)^{\otimes 2}\). Its first \(E\)-Chern class is
\[
F_E\!\bigl(c_1^E(\det W),F_E(x,x)\bigr).
\]
Both \(W=L_u\oplus L_v\) and \(W=\mathcal O\oplus(L_u\otimes L_v)\) have the same determinant. The complex tangent exact sequence gives
\[
c^E(TP(W))=\pi^*c^E(TB)\bigl(1+F_E(F_E(U,V),F_E(x,x))\bigr).
\]
Hence the isomorphism fixes every \(E\)-Chern class of the complex tangent bundles.

**5. The degree-zero \(K\)-theory \(\lambda\)-structure.** The same even-cell argument implies that \(K^0(B)\) is torsion-free. Put \(l=[L_u]\), \(m=[L_v]\). Because the ordinary Chern characters of \(l-1\) and \(m-1\) are divisible by \(u\) and \(v\), respectively, \(uv=0\) gives
\[
(l-1)(m-1)=0\quad\text{in }K^0(B).
\]
Let \(s=[S^*]\) be the class of a tautological dual line. The two projectivization relations in \(K^0\) are
\[
(1-ls)(1-ms)=0,\qquad (1-s)(1-lms)=0.
\]
Their difference is \(s(l-1)(m-1)=0\); therefore, mapping \(s_X\) to \(s_Y\) and fixing \(K^0(B)\) gives a ring isomorphism. It is a special \(\lambda\)-ring isomorphism: the ring is generated by the base \(\lambda\)-ring and a line-element \(s\), with identical \(\lambda\)-operations on those generators. Thus the isomorphism also commutes with Adams operations.

**6. Homotopy inequivalence.** Gong–Li, Theorem 4.1, shows that no map from \(Y\) to \(X\) induces an integral-cohomology ring isomorphism. Their proof combines rigidity of the ordinary cohomology ring isomorphisms with the nonexistence of a nowhere-zero section of \(L_u\oplus L_v\), detected by a spin-signature divisibility obstruction. Consequently no homotopy equivalence exists. This is an externally proved input, not an inference from the oriented-ring calculations above.

## Verification
The supplied `verify_uv.py` uses only Python 3 standard-library integer arithmetic. Executing `python3 verify_uv.py` returns `UV_CERTIFICATE_OK: 13 allowed Stanley--Reisner zero monomials`. The computation verifies the exact integral ordinary divisor-product certificate and is not offered as proof of the formal-group-law identity, whose argument applies to every formal group law. The remaining checks are symbolic: torsion-freeness of complex cobordism from the even-cell Atiyah–Hirzebruch spectral sequence, the rational Chern–Dold map, the rank-two projective-bundle theorem, and the explicit identity modulo the product ideal.

## Relationship to prior work
Gong–Li, arXiv:2609.39707v1, constructs this pair and proves its ordinary integral cohomology rings and ordinary tangent characteristic classes agree, but the spaces are not homotopy equivalent. The paper does not give a comparison of complex cobordism, arbitrary complex-oriented generalized cohomology, or the \(K^0\) special \(\lambda\)-ring structure. Krishna–Uma, arXiv:1011.0573v1, supplies general formal-group-law and toric cobordism presentations, but does not make this particular all-oriented-theory comparison of the Gong–Li pair. The present finding gives a universal reason the newly exhibited non-homotopy equivalence is invisible to this entire nonequivariant family of invariants, not merely to ordinary cohomology and its characteristic classes.

## Limitations
The statement concerns nonequivariant complex-oriented multiplicative theories and the specified projective-bundle pair. It does not say their cohomology isomorphism is induced by a map or that all generalized cohomology operations commute with it. The explicit \(\lambda\)-ring statement is for degree-zero complex topological \(K\)-theory only. Unoriented and real theories, equivariant theories, and homotopy types are outside the claimed equivalence. The general projective-bundle criterion assumes a finite CW base with torsion-free even integral cohomology; no assertion is made for arbitrary bases with torsion.

## References
1. Tao Gong and Yingxin Li, *A Counterexample to Cohomological Rigidity of Toric Manifolds*, arXiv:2609.39707v1, first public 2026-09-30, primary MSC 57S12, especially §2.1, Lemma 2.1, Proposition 2.3 and Theorem 4.1. https://arxiv.org/html/2609.39707v1
2. Amalendu Krishna and V. Uma, *Cobordism ring of toric varieties*, arXiv:1011.0573v1, especially §§2.5, 3.1 and 8. https://arxiv.org/html/1011.0573v1
