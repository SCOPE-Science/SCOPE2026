# Orthogonal Witt-type rank spectra and density thresholds for nilpotent evolution algebra endomorphisms

## Finding

For every odd prime power \(q\), fix an integer \(n\ge2\), an \(n\)-dimensional \(\mathbb F_q\)-space \(V\), and a nondegenerate symmetric bilinear form \(b\). The commutative nilpotent evolution algebra \(E=E(V,b)=V\oplus\mathbb F_qz\) is defined by
\[
(u+az)(v+cz)=b(u,v)z.
\]
Its square and annihilator both equal \(\mathbb F_qz\). We count the ordinary linear ranks of **all** algebra endomorphisms \(E\to E\), including noninvertible ones.

Write \(n=2m+1\) or \(n=2m\). In even dimension define \(\epsilon=\chi((-1)^m\det b)\), where \(\chi\) is the quadratic character of \(\mathbb F_q^\times\). The sign is \(+1\) for the hyperbolic/split form and \(-1\) for the elliptic/nonsplit form. The Witt index is
\[
w=\begin{cases}m,&n\text{ odd or }\epsilon=+1,\\m-1,&n=2m,\ \epsilon=-1.\end{cases}
\]
Set \(P_{n,0}=1\) and, for \(r\ge1\),
\[
P_{n,r}(q)=\prod_{j=0}^{r-1}(q^n-q^j).
\]
For \(0\le r\le w\), let \(I_{n,r}\) count totally \(b\)-isotropic \(r\)-dimensional subspaces of \(V\). Explicitly,
\[
I_{2m+1,r}(q)=\prod_{j=0}^{r-1}\frac{q^{2(m-j)}-1}{q^{j+1}-1},
\quad
I_{2m,r}^{\epsilon}(q)=\prod_{j=0}^{r-1}\frac{(q^{m-j-1}+\epsilon)(q^{m-j}-\epsilon)}{q^{j+1}-1}.
\]
Empty products are one. Define the similitude order
\[
G_{n,q,\epsilon}=\begin{cases}
(q-1)q^{m^2}\prod_{j=1}^{m}(q^{2j}-1),&n=2m+1,\\
2(q-1)q^{m(m-1)}(q^m-\epsilon)\prod_{j=1}^{m-1}(q^{2j}-1),&n=2m.
\end{cases}
\]
In the odd-dimensional line, the symbol \(\epsilon\) has no role. **The complete endomorphism-rank polynomial** is
\[
\boxed{H_{E,q}(T)=q^nG_{n,q,\epsilon}T^{n+1}+\sum_{r=0}^{w}I_{n,r}P_{n,r}(q)\left(q^rT^r+(q^n-q^r)T^{r+1}\right).}
\]
Every rank in \(\{0,1,\ldots,w+1,n+1\}\) occurs, and no other rank occurs. Therefore the maximum rank of a noninvertible endomorphism in even ambient dimension distinguishes the two Witt types. The polynomial also distinguishes those types by its high-rank support.

With fixed \(n\) and fixed Witt type, the automorphism fraction satisfies
\[
\boxed{\lim_{q\to\infty\atop q\,\mathrm{odd}}\frac{|\operatorname{Aut}(E)|}{|\operatorname{End}(E)|}=\begin{cases}
1,&n\in\{2,4\},\ \epsilon=-1,\\
\tfrac12,&n=3\ \text{or }(n,\epsilon)=(2,+1),\\
0,&\text{otherwise.}
\end{cases}}
\]
The limit runs through odd prime powers. For example, at \(q=3\) and \(n=4\) the split form has
\[
H_{+}(T)=1+3920T+549120T^2+3594240T^3+186624T^5,
\]
whereas the nonsplit form has
\[
H_{-}(T)=1+2480T+62400T^2+233280T^5.
\]
A third-rank singular endomorphism occurs in the first case but not the second.

## Assumptions and scope

Fields have odd characteristic and finite cardinality \(q\). The form is nondegenerate and symmetric; no assumption that it is the standard dot product is needed. All ranks refer to the full \((n+1)\)-dimensional regular vector space underlying the algebra. Only algebra endomorphisms are counted, with no orbit quotient or identification of distinct maps. There is no asserted characteristic-two extension: polar spaces and orthogonal groups differ substantially in that characteristic.

## Proof

**1. Exhaustive endomorphism parametrization.** Since \(E^2=\mathbb F_qz\), every endomorphism \(\varphi\) sends \(z\) to \(\lambda z\) for a unique \(\lambda\in\mathbb F_q\). There are unique \(A\in\operatorname{End}_{\mathbb F_q}(V)\) and \(f\in V^*\) such that \(\varphi(u)=Au+f(u)z\). Preservation of every product is equivalent to
\[
b(Au,Av)=\lambda b(u,v)\quad\text{for every }u,v\in V,
\quad\text{or}\quad A^{\mathsf T}BA=\lambda B.
\]
Conversely, any such triple \((A,f,\lambda)\) gives exactly one algebra endomorphism. The full representing matrix relative to \(V\oplus\mathbb F_qz\) is
\[
\begin{pmatrix}A&0\\f&\lambda\end{pmatrix}.
\]
No hidden compatibility condition on \(f\) remains.

**2. Invertible multiplier.** If \(\lambda\ne0\), taking determinants shows \(A\) is invertible, hence the full endomorphism is an automorphism of rank \(n+1\). The possibilities for \(A\) are the general orthogonal similitudes \(GO(V,b)\). Each admits \(q^n\) choices of \(f\), contributing \(q^n|GO(V,b)|T^{n+1}\).

The standard finite orthogonal group orders in odd characteristic are
\[
|O(2m+1,q)|=2q^{m^2}\prod_{j=1}^{m}(q^{2j}-1)
\]
and
\[
|O^{\epsilon}(2m,q)|=2q^{m(m-1)}(q^m-\epsilon)\prod_{j=1}^{m-1}(q^{2j}-1).
\]
For odd \(n\), the determinant identity \((\det A)^2=\lambda^n\det B/\det B=\lambda^n\) forces \(\lambda\) to be a square. Scalar similitudes realize all squares, giving exactly \((q-1)/2\) possible multipliers and the stated odd-dimensional \(G\). For even \(n\), **every** nonzero multiplier occurs: scale one vector in each hyperbolic pair by that multiplier, and on an anisotropic two-plane use multiplication by a field element of prescribed norm in \(\mathbb F_{q^2}^\times\), whose norm map is surjective. The resulting similitudes yield \((q-1)|O^\epsilon(2m,q)|\), proving the even-dimensional \(G\).

**3. Singular multiplier and rank fibers.** If \(\lambda=0\), the condition \(b(Au,Av)=0\) says exactly that \(U=\operatorname{im}A\) is totally isotropic. Set \(r=\dim U\). By Witt theory \(0\le r\le w\). First choose the subspace \(U\) in \(I_{n,r}\) ways, then choose the surjection \(A:V\twoheadrightarrow U\) in \(P_{n,r}(q)\) ways. The rank of the full matrix \(\left(\begin{smallmatrix}A&0\\f&0\end{smallmatrix}\right)\) is \(r\) exactly when \(f|_{\ker A}=0\), i.e. when \(f\) factors through \(A\). This leaves precisely \(q^r\) functionals. The other \(q^n-q^r\) functionals give rank \(r+1\). Multiplying and summing proves the full polynomial with no uncounted cases.

**4. Polar-space factors and nonempty support.** Count totally isotropic flags by their first isotropic line. In an odd \((2m+1)\)-space, the number of isotropic lines is \((q^{2m}-1)/(q-1)\). In an even \(2m\)-space of sign \(\epsilon\), it is \((q^{m-1}+\epsilon)(q^m-\epsilon)/(q-1)\). For each isotropic line \(L\), the quotient \(L^\perp/L\) has dimension two less and the same parity and sign. Double-counting a line contained in an \(r\)-dimensional isotropic space yields a recurrence
\[
I_{n,r}\frac{q^r-1}{q-1}=I_{n,1}I_{n-2,r-1}.
\]
Iteration gives exactly the two products printed above. The Witt decomposition supplies an isotropic \(r\)-space for each \(0\le r\le w\), so all listed \(I_{n,r}\) are positive. Consequently \(P_{n,r}\) and the contributions to ranks \(r\) and \(r+1\) are positive (except the zero-rank term at \(r=0\), which is correctly one). All and only the claimed ranks occur.

**5. Density transition.** For fixed \(m\) and growing odd prime powers \(q\), the automorphism count has leading degree \(2m^2+3m+2\) if \(n=2m+1\), and \(2m^2+m+1\) if \(n=2m\). The singular contribution of maximal isotropic rank has leading degree \((5m^2+7m+2)/2\) for odd dimension, \((5m^2+3m)/2\) for even split dimension, and \((5m^2+m-2)/2\) for even nonsplit dimension. For smaller isotropic ranks the degree strictly decreases, as follows directly from the positive powers in the ratios of successive flag counts and surjection counts. Comparing the exponents leaves ties only for odd \(n=3\) and split \(n=2\). In both ties the leading coefficients of the automorphism and singular counts are equal, giving limit \(1/2\). For nonsplit \(n=2,4\) the automorphism exponent is strictly larger, yielding limit one. In all other dimensions the singular exponent is larger, giving limit zero. This completes the claim.

## Verification

The standalone code `verify_evolution_orthogonal.py` exhaustively enumerates the defining endomorphism equations and the resulting matrix ranks over prime fields, for both Witt classes in dimension two and for dimension three. It separately enumerates totally isotropic subspaces by reduced-row-echelon bases for rank ranges in dimensions four and five. The independent code `verify_orthogonal_gf9.py` performs direct arithmetic in the extension field \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\), checking both two-dimensional Witt classes. Run them with `python3 verify_evolution_orthogonal.py` and `python3 verify_orthogonal_gf9.py`. The terminal markers are `VERIFY_OK_ORTHOGONAL_EVOLUTION_RANK_SPECTRA` and `VERIFY_OK_ORTHOGONAL_EVOLUTION_GF9`. These finite checks validate examples, not the unbounded theorem; the proof above supplies the unrestricted argument.

## Relationship to prior work

Elduque and Labra introduced \(E(U,b)\) and proved its nilpotent evolution-algebra property and its similarity-based isomorphism classification (Definition 4.1, Proposition 4.2, Theorem 4.7(i) of the 2016 preprint). Those results concern algebra structure and isomorphism, not the number of **noninvertible** endomorphisms at each rank or automorphism density. Later work on commutative algebras with one-dimensional square likewise treats forms and structural classification. Classical polar-space and orthogonal-group formulas supply the counting ingredients; the present statement assembles them into a complete rank distribution and a dimension/type-sensitive density transition, rather than claiming the group orders or polar counts are new.

## Limitations

The finite-field characteristic-two case and degenerations of \(b\) are not covered. Every asserted formula is for a fixed quadratic-space isometry class; in odd dimension the scalar similarity of the form removes the square-class distinction from the enumerator. The literature comparison is not a guarantee of historical priority: a mathematically equivalent enumeration under a different term such as orthogonal transformation monoid may exist. No independent mathematical audit has been performed.

## References

1. A. Elduque and A. Labra, *On nilpotent evolution algebras*, arXiv:1602.01590 (first public version 2016-02-04), Definition 4.1, Proposition 4.2, Theorem 4.7(i). https://arxiv.org/abs/1602.01590
2. D. Martín Barquero et al., *Commutative Algebras with One-Dimensional Square*, Mediterranean Journal of Mathematics (2025), DOI:10.1007/s00009-025-02812-7, §4.2. https://doi.org/10.1007/s00009-025-02812-7
3. R. A. Wilson, *Classical Groups*, Chapter 3, §3.4.2, pp. 13–14, orthogonal group orders and isotropic-vector counts, lecture notes: https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes3.pdf . The polar subspace formulas are also derived above from line-flag counting.
