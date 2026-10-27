# Necklace, ideal and symmetry spectra of looped cyclic evolution algebras

## Finding

For every field \(K\) and integer \(n\ge3\), consider the nonassociative commutative evolution algebras \(E(\mathbf a,\mathbf b)\) with natural basis indexed by \(\mathbb Z/n\mathbb Z\) and multiplication
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=a_i e_i+b_i e_{i+1},\qquad a_i,b_i\in K^\times.
\]
Associate the *normalized necklace* \(\mathbf c=(c_i)_{i\in\mathbb Z/n\mathbb Z}\), where
\[
c_i=\frac{b_i a_{i+1}}{a_i^2}\in K^\times.
\]
Then two such algebras are isomorphic as unrestricted \(K\)-linear algebras if and only if their normalized necklaces differ by a cyclic rotation. If the smallest positive rotation fixing \(\mathbf c\) is \(m\mid n\), the full ordinary automorphism group is cyclic of order \(n/m\), over \(K\) **and over every field extension**.

Put \(s=(-1)^n\in K\). The algebra is absolutely simple exactly when
\[
\prod_{i=0}^{n-1}c_i\ne s.
\]
When equality holds, it has precisely three ideals: \(0\), the unique nonzero proper ideal \(E^2\) of dimension \(n-1\), and \(E\). In particular the nonperfect locus has a fixed, sharp codimension-one ideal structure rather than uncontrolled degeneration.

For \(K=\mathbb F_q\), write \(Q=q-1\), let \(\varphi\) denote Euler's totient, and let \(\mu\) denote the Möbius function. The exact number of isomorphism classes in this *entire nonzero two-support looped-cycle family* is
\[
N_{\rm all}(n,q)=\frac1n\sum_{e\mid n}\varphi(e)Q^{n/e}.
\]
Exactly
\[
N_{\rm sing}(n,q)=\frac1n\sum_{e\mid n}\varphi(e)\gcd(e,Q)Q^{n/e-1}
\]
of these classes have a proper nonzero ideal, and the remaining \(N_{\rm all}-N_{\rm sing}\) classes are absolutely simple.

More precisely, for each divisor \(m\mid n\), the numbers of absolutely simple and nonsimple isomorphism classes with automorphism group of order \(n/m\) are, respectively,
\[
\frac{A_m-B_m}{m}\quad\text{and}\quad\frac{B_m}{m},
\]
where
\[
A_m=\sum_{d\mid m}\mu(m/d)Q^d,\qquad
B_m=\sum_{d\mid m}\mu(m/d)Q^{d-1}\gcd(n/d,Q).
\]
In particular, the number of absolutely simple classes with full cyclic symmetry \(C_n\) is exactly \(Q-\gcd(n,Q)\). Such a maximally symmetric absolutely simple member exists if and only if \(q-1\nmid n\). For instance, \(\mathbb F_3\) admits an absolutely simple member with full automorphism group \(C_n\) in every odd dimension \(n\ge3\), despite its very small multiplicative group.

## Assumptions and scope

Every field characteristic is permitted, including \(2\), and all coefficients \(a_i,b_i\) are nonzero. Indices are taken modulo \(n\). The condition \(n\ge3\) is essential to the pairwise-independence argument; the two-vertex case is excluded. An automorphism is an ordinary invertible linear map preserving multiplication, not a semilinear automorphism or a statement about all automorphism-group schemes. The family is specified by one loop and one directed successor edge per vertex: no claim is made for arbitrary evolution algebras, zero coefficients, or unrelated support digraphs. Over a finite field, the isomorphism census counts unmarked algebra classes, not labelled multiplication tables.

## Proof

**1. Scalar normalization and rank.** Set \(f_i=a_i^{-1}e_i\). Then
\[
f_i f_j=0\quad(i\ne j),\qquad f_i^2=f_i+c_i f_{i+1},
\]
with \(c_i=b_i a_{i+1}/a_i^2\). Hence every algebra has a normalized representative \(E(\mathbf c)\) with all loop coefficients exactly one. The normalized structure matrix is \(I+\operatorname{diag}(\mathbf c)P\), where \(P\) is the cyclic shift, and its determinant is \(1-(-1)^n\prod_i c_i\). If this determinant vanishes, the equations for a linear dependence among the squares are \(\lambda_i+c_{i-1}\lambda_{i-1}=0\). Every nonzero solution has all coordinates nonzero, and the solution space is one-dimensional. Thus the rank of the space spanned by the squares is either \(n\) or \(n-1\), and **in both cases every two distinct natural-basis squares are linearly independent** because \(n\ge3\).

**2. Isomorphism rigidity.** All basis squares are nonzero, so the algebra is nondegenerate. The preceding pairwise independence verifies Property \((2\mathrm{LI})\). By Boudi--Cabrera Casado--Siles Molina, Corollary 2.7 (2020), any isomorphism between two such algebras must map one natural basis to a rescaled permutation of the other. For completeness, there is a direct rank argument: if \(x\) occurs in any natural basis, its multiplication map \(L_x:y\mapsto xy\) has rank one because \(x^2\ne0\) while \(x\) annihilates the other \(n-1\) basis vectors. In the displayed natural basis, however, \(\operatorname{im}L_x=\operatorname{span}\{f_i^2:x_i\ne0\}\). Pairwise independence makes this image have rank at least two whenever \(x\) has support of size at least two. Thus every vector of the new natural basis has exactly one nonzero coordinate. Consequently write an isomorphism as \(\Phi(f_i)=d_i g_{\sigma(i)}\) with \(d_i\ne0\). The square \(\Phi(f_i^2)\) has support precisely \(\{\sigma(i),\sigma(i+1)\}\), whereas \(\Phi(f_i)^2\) has support precisely \(\{\sigma(i),\sigma(i)+1\}\). As \(n\ge3\), necessarily \(\sigma(i+1)=\sigma(i)+1\), so \(\sigma\) is a cyclic rotation. Comparing the loop terms gives \(d_i=d_i^2\), hence \(d_i=1\) over every field. Comparing successor terms then gives \(c_i=c'_{\sigma(i)}\). Conversely, each rotation matching the necklaces is an isomorphism. The subgroup of such rotations is cyclic of order \(n/m\), where \(m\) is the least period; the argument is unchanged by any field extension.

**3. Complete ideal lattice.** Let \(I\) be a nonzero ideal and choose \(x\in I\setminus\{0\}\) with \(i\)-th coordinate nonzero. Multiplying by \(f_i\) shows \(f_i^2\in I\). Multiplying this element by \(f_{i+1}\) gives \(c_i f_{i+1}^2\in I\). Iterating around the directed cycle yields \(E^2=\operatorname{span}\{f_j^2:0\le j<n\}\subseteq I\). In the nonsingular determinant case, \(E^2=E\), so \(E\) is simple over all extensions. In the singular case, \(E^2\) is a proper ideal of codimension one, and the inclusion just established means there are no other nonzero proper ideals, over any extension. This proves the absolute-simplicity criterion and complete ideal lattice.

**4. Finite-field necklaces.** The normalization of step 1 produces every \(\mathbf c\in(\mathbb F_q^\times)^n\), and step 2 identifies isomorphism classes with orbits of the cyclic rotation group. A rotation with \(m\) cycles of length \(e=n/m\) fixes exactly \(Q^m\) words; there are \(\varphi(e)\) such rotations. Burnside's lemma gives \(N_{\rm all}\).

For a rotation with these parameters, each fixed word repeats a block of length \(m\) exactly \(e\) times. Its total coordinate product equals \(s=(-1)^n\) exactly when the block product \(u\in\mathbb F_q^\times\) satisfies \(u^e=s\). This equation is always solvable: if \(n\) is even take \(u=1\); if \(n\) is odd, then \(e\) is odd and take \(u=-1\). In the cyclic group \(\mathbb F_q^\times\) of order \(Q\), the equation has exactly \(\gcd(e,Q)\) solutions. Each chosen block product allows exactly \(Q^{m-1}\) blocks. Therefore this rotation fixes exactly \(Q^{m-1}\gcd(e,Q)\) singular words. Burnside gives \(N_{\rm sing}\), with no parity exception even in characteristic two.

**5. Full automorphism-order refinement.** Every word has a unique minimal positive period \(m\mid n\) and precisely \(m\) distinct cyclic shifts. Let \(A_m\) and \(B_m\) count, respectively, all length-\(n\) words and singular length-\(n\) words with *minimal* period \(m\). Words with period dividing \(d\mid n\) number \(Q^d\); singular such words number \(Q^{d-1}\gcd(n/d,Q)\) by the previous root count. Möbius inversion on divisors of \(m\) yields the displayed formulas for \(A_m,B_m\). Division by the orbit size \(m\) gives the claimed number of classes with automorphism group \(C_{n/m}\). For \(m=1\), the singular constant necklaces correspond to the \(\gcd(n,Q)\) solutions of \(c^n=s\), leaving exactly \(Q-\gcd(n,Q)\) simple constant necklaces. Finally, \(\gcd(n,Q)<Q\) exactly when \(Q\nmid n\).

## Verification

Run `python3 verify.py` from the directory containing the accompanying verifier. It independently enumerates cyclic word-orbits for \(22\) prime-field parameter pairs, verifies the exact total/singularity and automorphism-order formulas, checks rank and normalization for all nonzero coefficient choices in dimensions three over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and exhaustively searches every \(3\times3\) linear matrix over \(\mathbb F_2\) and \(\mathbb F_3\) for automorphisms of every normalized three-dimensional algebra. The executed verifier printed `VERIFY_OK`. The matrix search does not assume that automorphisms are monomial. Finite tests corroborate, but cannot prove, the all-fields and all-dimensions result.

Example checks: for \(q=3,n=3\), there are \(4\) isomorphism classes, \(2\) simple and \(2\) singular; for \(q=3,n=4\), there are \(6\) classes, \(2\) simple and \(4\) singular. For \(q=4,n=3\) there are \(11\) classes, \(6\) simple and \(5\) singular; this last count is an evaluation of the general formula rather than a direct extension-field computation.

## Relationship to prior work

Elduque and Labra (2019, Theorem 3.2) describe automorphism-group schemes of **perfect** evolution algebras through their directed graphs. In particular the cyclic-rotation symmetry of the perfect subclass is not a newly discovered general phenomenon; the present result makes the coefficient-dependent rotation stabilizer explicit and extends the complete class/ideal census to singular members. Boudi, Cabrera Casado, and Siles Molina (2020, Corollary 2.7) established the \((2\mathrm{LI})\) criterion for unique natural bases; it is used and credited, not claimed as new. Costoya, Muñoz, Tocino, and Viruel (2022, Theorem A and Section 4) construct absolutely simple Cayley evolution algebras realizing finite automorphism groups over sufficiently large fields. The constant-neighbor coefficients form a particularly sparse cyclic example; the exact finite-field threshold and the complete varying-coefficient necklace/ideal/symmetry census here are not stated by their theorem.

Previously analyzed *loop-free*, weighted permutation evolution algebras have multiplication \(e_i^2=w_i e_{i+1}\), rather than the present two-term \(e_i^2=a_i e_i+b_i e_{i+1}\). Their diagonal-rescaling rules and determinant/singularity behavior differ, so their weighted-cycle invariants do not imply these formulas. The underlying Burnside and Möbius enumeration tools are classical and not presented as new methods.

## Limitations

The classification is restricted to \(n\ge3\), nonzero loop and successor weights, and ordinary linear algebra isomorphisms; it does not cover the two-vertex case, arbitrary support patterns, or all possible realization algebras for a group. The formulas use the known unique-natural-basis theorem and elementary finite-group orbit-counting. A broader monomial-orbit classification under another name could subsume the result; exhaustive publication-priority verification is not claimed. The finite checks do not establish infinite quantifiers.

## References

1. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191v1 (first public 2019-02-06), Sections 2--3, especially Theorem 3.2. https://arxiv.org/abs/1902.02191
2. N. Boudi, Y. Cabrera Casado, and M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460v1 (first public 2020-06-25), Section 2, Corollary 2.7 and Definition 2.8. https://arxiv.org/abs/2006.14460
3. C. Costoya, V. Muñoz, A. Tocino, and A. Viruel, *Automorphism groups of Cayley evolution algebras*, arXiv:2207.01335v1 (first public 2022-07-04), Theorem A and Section 4. https://arxiv.org/abs/2207.01335
