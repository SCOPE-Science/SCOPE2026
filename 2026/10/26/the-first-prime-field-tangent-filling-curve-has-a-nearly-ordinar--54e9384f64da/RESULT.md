# The first prime-field tangent-filling curve has a nearly ordinary genus-35 normalization

## Finding
Set \(k=\mathbb F_{11}\), and consider the degree-ten plane curve
\[
C: F=X^{10}+Y^{10}+Z^{10}-3(X+Y+Z)^{10}=0\subset\mathbb P^2_k.
\]
Its normalization \(\widetilde C\) is smooth of genus \(35\). Its Jacobian has \(11\)-rank \(34\) and \(a\)-number \(1\). Its Newton slopes are \(0\) (multiplicity \(34\)), \(1/2\) (multiplicity \(2\)), and \(1\) (multiplicity \(34\)). Asgarli and Ghioca prove that this degree-ten curve is geometrically irreducible and tangent-filling, and that its unique singularity is an ordinary double point. The novelty asserted here is the exact arithmetic profile of its normalized Jacobian.

## Assumptions and scope
All statements are over \(k=\mathbb F_{11}\), except that the uniqueness and local type of the geometric singularity are understood over its algebraic closure. The \(p\)-rank is the dimension of the rational \(p\)-torsion of the Jacobian over an algebraic closure. The \(a\)-number is the dimension of the kernel of Cartier acting on regular differentials of the normalization. The Newton slopes refer to the associated height-\(70\) principally polarized \(11\)-divisible group. This is a result about one canonical member of a published infinite family, not a claim of analogous arithmetic behavior for other field sizes.

## Proof
Write \(s=X+Y+Z\). Because \(10=-1\) in \(k\), the three partial derivatives vanish precisely when \(X^9=Y^9=Z^9=3s^9\). If \(s=0\), all projective coordinates vanish, which is impossible. In the affine chart \(s=1\), put \(z=1-x-y\). Buchberger reduction of \(x^9-3\), \(y^9-3\), \((1-x-y)^9-3\) over \(k\) gives the ideal \((x-4,y-4)\). The appended exact polynomial-arithmetic verifier checks the full S-pair criterion and two inclusions of ideals; hence the same radical solution holds over the algebraic closure. It is \([1:1:1]\) in projective coordinates. The quadratic Taylor part in local coordinates near this point is proportional to \(u^2-uv+v^2\); the discriminant is \(-3=8\in k\), a nonsquare, so the point is an ordinary nonsplit node. Thus the genus is \(\binom{9}{2}-1=35\).

Adjunction for the normalization of a nodal degree-ten plane curve represents its regular differentials by degree-seven adjoint forms vanishing at the node. Let \(E\) be the \(36\)-dimensional space with basis \(e_{abc}=X^{a-1}Y^{b-1}Z^{c-1}\), indexed by positive integers \(a+b+c=10\). The regular adjoint subspace is
\[
V=\left\{\sum_{a+b+c=10}h_{abc}e_{abc}:\sum h_{abc}=0\right\},\qquad\dim V=35.
\]
The plane-curve Cartier formula of Stöhr–Voloch (in computational form also stated by Kudo–Harashita) gives the matrix \(M\) on the adjoint differentials, over the prime field:
\[
M_{(a,b,c),(i,j,k)}=[X^{11a-i}Y^{11b-j}Z^{11c-k}]F^{10},
\qquad a+b+c=i+j+k=10,
\]
where the brackets denote coefficient extraction. Its columns sum to \(10\) modulo \(11\), so it preserves \(V\). Take \(e_j-e_{36}\) for \(1\le j\le35\) as a basis of \(V\). Then Cartier has the exact \(35\times35\) matrix \(N\) with entries \(M_{ij}-M_{i,36}\) for \(i,j\le35\). Independent sparse-power and four-factor multinomial coefficient algorithms agree on every entry. Exact Gaussian elimination gives
\[
\operatorname{rank} M=35,\qquad\operatorname{rank} N=34,\qquad\operatorname{rank}N^2=34.
\]
A top-left \(35\times35\) minor of \(M\) has determinant \(10\) modulo \(11\). Its explicit right and left null vectors have nonzero dot product \(8\) modulo \(11\). These certificates and the stable-rank check are reproduced by the accompanying standalone program. Since \(N\) acts on the regular differentials, its nullity \(35-34=1\) is the \(a\)-number. The stabilized rank \(34\), already attained at the second power, is the \(11\)-rank. In genus \(35\), a principally polarized Newton polygon with \(11\)-rank \(34\) has \(34\) slope-zero and \(34\) slope-one factors; the remaining two slopes must both equal \(1/2\), by symmetry and the dimension constraint on a height-two isoclinic factor. This proves the claim.

## Verification
The supplied `check_singularity.py` performs complete Buchberger S-pair verification in \(k[x,y]\) (26 basis polynomials and 325 processed pairs). The independent arithmetic program `verify.py` expands all \(3,234\) nonzero coefficients of \(F^{10}\), computes the \(36\times36\) coefficient matrix by two algebraically distinct expansions, and checks all \(1,296\) entries agree. It constructs and verifies the induced matrix \(N\), its square, full and restricted ranks, a nonzero minor, left/right kernel relations, and their pairing. Run with `python3 check_singularity.py` and `python3 verify.py`. No external packages are required. `CERTIFICATE.json` records the coefficient-matrix digest and finite-field witnesses; it is not a substitute for the full reproducible computation.

## Relationship to prior work
Asgarli and Ghioca (arXiv:2302.13420, first submitted 2023-02-26) prove the degree-\(q-1\) tangent-filling construction for \(q\ge11\), characteristic greater than three, and characterize its singularity, but do not give these arithmetic Jacobian invariants. Kudo and Harashita (arXiv:2203.11801) give general algorithms for differentials and Cartier–Manin matrices of singular plane curves; applying the formula to this particular normalization, deriving its exact rank and Newton polygon, is additional work. The Tallini plane-filling curves discussed in other arithmetic-geometry literature are a distinct construction; their invariants do not immediately imply the claim here.

## Limitations
Only the explicit first prime-field member at \(q=11\) is computed. The calculation provides a finite-field exact-arithmetic certificate coupled to standard Cartier and nodal adjunction theorems, not an independent formal proof of those classical results. No claim is made about zeta-function numerator, full Frobenius characteristic polynomial, or other finite fields. Prior coverage from unindexed computational databases cannot be excluded, and independent mathematical audit has not been performed.

## References
- S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (2023), especially Theorem 1.3.
- M. Kudo and S. Harashita, *Computing the space of differential forms of a plane curve and its Cartier-Manin matrix*, arXiv:2203.11801 (2022), §6.
- K.-O. Stöhr and J. F. Voloch, *A formula for the Cartier operator on plane algebraic curves*, J. Reine Angew. Math. 377 (1987), 49–64.
