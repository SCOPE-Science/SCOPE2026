# Sharp idempotent splitting degrees and Frobenius zeta functions for binary evolution algebras

## Finding

Let \(E\) be an \(n\)-dimensional evolution algebra over \(\mathbb F_2\), where \(n\ge2\), and let \(A\in M_n(\mathbb F_2)\) be the matrix of its squaring map in a natural basis (columns give the coefficients of the basis squares). Put \(W=\operatorname{im}(A^n)\), \(r=\dim_{\mathbb F_2}W\), and \(B=A|_W\); when \(r>0\), \(B\) is invertible. The formulas below apply equally to any finite-dimensional commutative \(\mathbb F_2\)-algebra, because its squaring map is additive.

**Exact extension-field census and zeta function.** For every integer \(s\ge1\), the number \(N_s\) of idempotents \(x^2=x\) in \(E\otimes_{\mathbb F_2}\mathbb F_{2^s}\), including zero, is
\[
N_s=2^{\dim_{\mathbb F_2}\ker(A^s-I_n)}=2^{\dim_{\mathbb F_2}\ker(B^s-I_W)}.
\]
The finite idempotent scheme is reduced and étale of degree \(2^r\) over \(\mathbb F_2\). Its geometric points are canonically an \(r\)-dimensional \(\mathbb F_2\)-vector space on which arithmetic Frobenius acts as \(B^{-1}\). Let \(L=\operatorname{ord}(B)\) if \(r>0\), and let \(L=1\) otherwise. Then \(\mathbb F_{2^L}\) is the smallest field over which **all** geometric idempotents are rational. For each positive integer \(d\mid L\), the number of closed points of degree \(d\) is
\[
c_d=\frac1d\sum_{e\mid d}\mu(d/e)\,2^{\dim\ker(B^e-I_W)},
\]
and \(c_d=0\) otherwise. Hence the Hasse–Weil zeta function of the zero-dimensional idempotent scheme is the explicit rational function
\[
Z_E(T)=\prod_{d\mid L}(1-T^d)^{-c_d}.
\]
Here \(\mu\) denotes the Möbius function. If \(r=0\), the only geometric idempotent is zero, \(N_s=1\), and \(Z_E(T)=(1-T)^{-1}\).

**Sharp first-appearance theorem.** Suppose \(E\) is *perfect* (its structure matrix \(A\) is invertible). Define
\[
\delta(E)=\min\{s\ge1:\ E\otimes\mathbb F_{2^s}\text{ has a nonzero idempotent}\}.
\]
Then
\[
\boxed{\delta(E)\le 2^n-1.}
\]
Equality holds **if and only if** the characteristic polynomial of \(A\) is primitive irreducible of degree \(n\) over \(\mathbb F_2\). Such perfect evolution algebras exist for every \(n\ge2\) (take the structure matrix to be the companion of a primitive polynomial). In the equality case, the precise extension-field profile is
\[
N_s=\begin{cases}2^n,& (2^n-1)\mid s,\\1,&(2^n-1)\nmid s,\end{cases}
\qquad
Z_E(T)=\frac1{(1-T)(1-T^{2^n-1})}.
\]
Equivalently, the \(2^n-1\) nonzero geometric idempotents comprise exactly **one** Frobenius orbit, of maximum possible degree \(2^n-1\). Thus the first possible nonzero rational idempotent can be exponentially delayed in algebra dimension, with an exact classification of all extremizers.

## Assumptions and scope

An evolution algebra over a field is a commutative, generally nonassociative algebra with a basis \(e_1,\ldots,e_n\) satisfying \(e_ie_j=0\) for \(i\ne j\). The matrix \(A\) is defined by \(e_j^2=\sum_i A_{ij}e_i\). The coefficient field of the original algebra is precisely \(\mathbb F_2\); extensions considered are \(\mathbb F_{2^s}/\mathbb F_2\) for positive integer \(s\). The term *perfect* means \(E^2=E\), equivalent here to invertibility of \(A\). An idempotent is an element \(x\) satisfying \(x^2=x\), not an idempotent multiplication operator. Zeta means the point-counting Hasse–Weil zeta of the finite idempotent locus, not a dynamical zeta for iterated squaring. The stated etaleness refers to this idempotent locus, not to an entire moduli scheme.

## Proof

**1. The squaring operator and stable image.** In characteristic two, commutativity implies \((u+v)^2=u^2+v^2\). Hence algebra squaring is \(\mathbb F_2\)-linear with matrix \(A\). Over an extension \(K\), the idempotent equation becomes \(x=A\sigma(x)\), where \(\sigma\) squares every coefficient. The Fitting decomposition \(\mathbb F_2^n=U\oplus W\), with \(U=\ker(A^n)\), \(W=\operatorname{im}(A^n)\), is \(A\)-invariant; \(A|_U\) is nilpotent and \(B=A|_W\) is invertible. On \(U\), iterating \(x=A\sigma(x)\) exactly \(n\) times gives \(x=A^n\sigma^n(x)=0\). Therefore all idempotents lie in \(W\), where they solve \(x=B\sigma(x)\).

**2. Enumeration and arithmetic Frobenius.** Assume \(r>0\), set \(L=\operatorname{ord}(B)\), and choose a normal basis \(\beta,\beta^2,\ldots,\beta^{2^{L-1}}\) of \(\mathbb F_{2^L}\) over \(\mathbb F_2\). Define an \(\mathbb F_2\)-linear map \(\Phi:\mathbb F_2^r\to\mathbb F_{2^L}^r\) by
\[
\Phi(v)=\sum_{j=0}^{L-1}\beta^{2^j}B^jv.
\]
Since \(B^L=I\), direct cycling of the sum shows \(B\sigma(\Phi(v))=\Phi(v)\). The normal-basis independence shows that \(\Phi\) is injective: if \(\Phi(v)=0\), the coefficient at each normal-basis term is zero, in particular \(v=0\). On the other hand, the ideal of the equations \(x=B\sigma(x)\), equivalently \(x_i^2-(B^{-1}x)_i=0\), has leading monomials \(x_i^2\) under any graded monomial order. These leading monomials are pairwise coprime, so the equations form a Gröbner basis, with quotient coordinate-ring basis the \(2^r\) squarefree monomials. Their Jacobian matrix (for \(x-Bx^{[2]}\)) is the identity in characteristic two; thus all points are simple. There are exactly \(2^r\) geometric points, all listed by \(\Phi\). This also proves the scheme finite étale, including the trivial \(r=0\) case.

For every \(v\), \(\sigma(\Phi(v))=B^{-1}\Phi(v)=\Phi(B^{-1}v)\), since \(B\) commutes with \(\Phi\). The \(s\)-th power of Frobenius thus fixes exactly the vectors \(v\in\ker(B^s-I)\). The same dimension is \(\dim\ker(A^s-I)\), since the nilpotent part has no eigenvalue one for any positive power. This proves the point-count formula. Every geometric point is defined over \(\mathbb F_{2^L}\), and no smaller extension suffices for all points because \(B^{-1}\) has exact order \(L\) as a faithful linear action on this \(2^r\)-point space. The number \(N_s\) is also \(\sum_{d\mid s}d c_d\); Möbius inversion gives the formula for \(c_d\), and the standard Euler product gives \(Z_E\).

**3. First occurrence and extremizers.** In the perfect case \(B=A\) and all eigenvalues of \(A\) are nonzero. The condition \(\ker(A^s-I)\ne0\) holds if and only if at least one eigenvalue \(\lambda\) satisfies \(\lambda^s=1\), even for nonsemisimple \(A\): invertibility is determined by eigenvalues, not Jordan block sizes. Thus \(\delta(E)\) is the least multiplicative order among the eigenvalues of \(A\). Every eigenvalue has minimal polynomial of degree \(d\le n\) over \(\mathbb F_2\), hence lies in \(\mathbb F_{2^d}^{\times}\) and has order at most \(2^d-1\le2^n-1\). Equality forces every eigenvalue to have order \(2^n-1\), so it has degree exactly \(n\) with primitive irreducible minimal polynomial; therefore the full characteristic polynomial of \(A\) equals that polynomial. Conversely, if the characteristic polynomial is primitive irreducible of degree \(n\), every eigenvalue has order \(2^n-1\), proving equality. Existence of primitive irreducible polynomials of every degree gives the extremal evolution algebras, since arbitrary matrices over \(\mathbb F_2\) occur as evolution-algebra structure matrices. An invertible matrix with primitive irreducible polynomial acts regularly on the nonzero vectors of \(\mathbb F_2^n\) (identify the vector space with \(\mathbb F_{2^n}\)), so Frobenius has one orbit of length \(2^n-1\). This yields the asserted \(N_s\) and zeta function.

**Explicit extremizer in dimension three.** Let
\[
e_1^2=e_2,\qquad e_2^2=e_3,\qquad e_3^2=e_1+e_2,
\]
with all mixed basis products zero. Then the binary structure matrix has characteristic polynomial \(t^3+t+1\), primitive of degree three. The algebra has no nonzero idempotent over \(\mathbb F_{2^s}\) unless \(7\mid s\), and exactly seven nonzero idempotents when \(7\mid s\), all in one Frobenius orbit of length seven.

## Verification

The accompanying standalone Python checker uses direct coefficient-field multiplication, original evolution-algebra squares, enumeration of every candidate idempotent, and separate binary matrix-power rank calculations. It exhausts **every** binary structure matrix in dimensions one, two, and three for several extension degrees; it tests the primitive cubic through extension degree seven, a nonsemisimple order-six block, and randomized higher-dimensional singular examples. The record contains **2,208 field/matrix configurations**, all agreeing with the exact census formula. This is finite corroboration; it does not prove arbitrary dimensions or all extension degrees. The general statements are proved algebraically above. Run `python3 check.py` using Python's standard library.

## Relationship to prior work

Casas, Ladra and Rozikov (2010) study idempotent systems in evolution algebras, including dimension-two real-family transitions, without providing the present binary extension tower and extremal splitting-degree classification. Casas, Ladra, Omirov and Rozikov (2012) study nilpotency/dibaricity, a separate structural axis. The 2026 evolution-algebra survey discusses geometric idempotent bounds and a dimension-two Galois criterion; its general length bound already constrains the number of geometric points, but **does not state the sharp exponential first-appearance construction, the primitive-irreducible if-and-only-if characterization, or the exact all-extension zeta/orbit spectrum proved here**. The 2018 study of idempotents for permutation-based evolution algebras concerns a distinct restricted structure-matrix class. The 2023 study of idempotent evolution-algebra isomorphism classes counts algebra classes, rather than elements \(x^2=x\).

There is a previously reported formula for fixed points of iterated squaring in **graphical evolution algebras** (binary symmetric zero-diagonal adjacency matrices). Its one-step specialization already gives the point count above in that restricted subclass; neither the graph-case point count nor the classical normal-basis device is claimed as new. Here the principal advance is the complete Frobenius/closed-point law and the **sharp first-idempotent splitting threshold for arbitrary binary structure matrices, with an iff characterization of extremizers**. Primitive degree-three companion matrices are not graph adjacency matrices, illustrating the essential broader scope. Related prior work proves existence of two-dimensional idempotent-free perfect evolution algebras over finite fields, but does not determine the sharp field-extension delay and complete Galois profile.

## Limitations

The theorem fixes the original coefficient field to \(\mathbb F_2\); the stated matrix-power formula should not be transferred unchanged to arbitrary coefficients in \(\mathbb F_{2^f}\). The first-appearance extremal theorem assumes perfection; for singular algebras the stable-image formula still holds. The finite computations test bounded dimensions/fields and do not constitute an infinite proof. Nonreduced moduli schemes, algebra isomorphism classification, and idempotent counts over odd-characteristic fields are outside the scope. The splitting-degree and zeta statements are formal consequences of the exhibited Frobenius action, but exhaustive historical priority beyond the inspected sources cannot be claimed; in particular, a wider published semilinear-algebra theorem might already imply them. No independent mathematical audit has been performed.

## References

1. J. M. Casas, M. Ladra and U. A. Rozikov, *A chain of evolution algebras*, arXiv:1004.0155 (first posted 2010-03-29), https://arxiv.org/abs/1004.0155.
2. J. M. Casas, M. Ladra, A. K. Omirov and U. A. Rozikov, *On nilpotent index and dibaricity of evolution algebras*, arXiv:1208.1709 (first posted 2012-08-08), https://arxiv.org/abs/1208.1709.
3. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first posted 2026-10-15), https://arxiv.org/abs/2610.22248.
4. I. Narkuziyev, *On absolute nilpotent and idempotent elements in evolution algebras corresponding to permutations*, arXiv:1803.11415 (first posted 2018-03-30), https://arxiv.org/abs/1803.11415.
5. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023), https://arxiv.org/abs/2310.12368.
6. *Exact finite-extension orbit census for graphical evolution-algebra squaring*, publicly indexed research record (special-case prior result; exact title), previously available in the mathematical literature archive.
7. *Every finite field admits a two-dimensional idempotent-free perfect evolution algebra*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-every-finite-field-admits-a-two-dimensional-idempotent-free-perf--fd35382c80da.
