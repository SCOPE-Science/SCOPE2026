# Prime-three collapse and exact spectra of three-chirp inverse pencils

## Finding
Let \(p\) be any odd prime and \(d\ge2\). For symmetric matrices \(U,V\in M_d(\mathbb F_p)\) such that \(U\), \(U+V\), and \(U+2V\) are invertible, set \(A_j=(U+jV)^{-1}\) and \(c_j=\chi_p(\det A_j)\in\{\pm1\}\), for \(j=0,1,2\). Here \(\chi_p\) is the Legendre character with \(\chi_p(0)=0\), and \(\zeta_p=\exp(2\pi i/p)\). Form the three-chirp filter
\[
h(x)=\sum_{j=0}^{2}c_j\zeta_p^{x^{\mathsf T}A_jx},\qquad x\in\mathbb F_p^d,
\]
and its unnormalized cyclic convolution operator \(T_h f(y)=\sum_{x\in\mathbb F_p^d}h(x)f(y-x)\) on the complex Hilbert space \(\ell^2(\mathbb F_p^d)\).

**Complete singular-value multiset.** Put \(t(\xi)=-\tfrac14\xi^{\mathsf T}V\xi\in\mathbb F_p\). For each residue \(t\), let \(N_V(t)=\#\{\xi:t(\xi)=t\}\). The singular values of \(T_h\), counted with multiplicity, are precisely
\[
p^{d/2}\left|1+2\cos(2\pi t/p)\right|\quad\text{with multiplicity }N_V(t),\qquad t\in\mathbb F_p.
\]
The formula below determines every multiplicity from the rank and discriminant of \(V\): choose a nonsingular restriction of \(V\) to a complement of its radical and write \(r=\operatorname{rank}V\), \(\Delta\) for its determinant modulo squares. If \(r=0\), \(N_V(0)=p^d\) and all other \(N_V(t)=0\). If \(r=2m+1\), then
\[
N_V(t)=p^{d-1}+p^{d-m-1}\chi_p\bigl((-1)^m\Delta(-4t)\bigr).
\]
If \(r=2m>0\), with \(\sigma=\chi_p((-1)^m\Delta)\), then
\[
N_V(t)=p^{d-1}+\sigma p^{d-m-1}\begin{cases}p-1,&t=0,\\-1,&t\ne0.\end{cases}
\]

**Arithmetic dichotomy and sharp bounds.** For every \(p\ge5\), the operator is invertible. If also \(\operatorname{rank}V\ge2\), define
\[
\mu_p=\min\left\{\left|1+2\cos\frac{2\pi\lfloor p/3\rfloor}{p}\right|,\left|1+2\cos\frac{2\pi\lceil p/3\rceil}{p}\right|\right\}.
\]
Its sharp spectral condition number is \(\kappa(T_h)=3/\mu_p\), independent of \(d,U,V\), and \(\kappa(T_h)=3\sqrt3\,p/(2\pi)+O(1)\) as odd primes tend to infinity. For \(p=3\), the operator has only two singular values, \(0\) and \(3^{d/2+1}\), with respective multiplicities \(3^d-N_V(0)\) and \(N_V(0)\). It satisfies the universal sharp lower bound
\[
\operatorname{rank}_{\mathbb C}T_h\ge3^{d-2},
\]
with equality precisely when \(V\) has rank two and its nondegenerate binary part is anisotropic, equivalently \(\chi_3(-\Delta)=-1\). Equality is attainable for every \(d\ge2\).

## Assumptions and scope
All arithmetic in matrices, quadratic forms and expressions such as \(\tfrac14\) is performed in \(\mathbb F_p\). The displayed real cosines use an integer representative of \(t\in\mathbb F_p\); this is independent of its representative. Convolution is **unnormalized**. Singular values are computed for the counting-measure \(\ell^2\) inner product. The matrix \(V\) need not be nonsingular or nonzero, but all three members of the inverse pencil must be nonsingular; no claim is made for singular pencil members. A determinant of the induced nonsingular form on the quotient by the radical is defined modulo squares, making the displayed Legendre signs independent of the chosen complement.

## Proof
**1. Exact Fourier diagonalization.** The characters \(x\mapsto\zeta_p^{\xi\cdot x}\) form an orthogonal Fourier basis, with convolution eigenvalue \(\widehat h(\xi)=\sum_x h(x)\zeta_p^{-\xi\cdot x}\). Set \(G_p=\sum_{u\in\mathbb F_p}\zeta_p^{u^2}\). Completing the square, then diagonalizing an invertible symmetric matrix by congruence, proves the standard quadratic Gauss identity
\[
\sum_{x\in\mathbb F_p^d}\zeta_p^{x^{\mathsf T}Ax-\xi\cdot x}
=\chi_p(\det A)G_p^d\zeta_p^{-\frac14\xi^{\mathsf T}A^{-1}\xi}.
\]
Here \(G_p^2=\chi_p(-1)p\), so \(|G_p|=\sqrt p\). Inserting \(A=A_j\), the two equal Legendre signs multiply to one. Because \(A_j^{-1}=U+jV\), one obtains **exactly**
\[
\widehat h(\xi)=G_p^d\zeta_p^{-\frac14\xi^{\mathsf T}U\xi}
\left(1+\zeta_p^{t(\xi)}+\zeta_p^{2t(\xi)}\right).
\tag{1}
\]
There is no unverified proportionality or hidden normalizing scalar. Since \(1+z+z^2=z(1+2\cos\theta)\) for \(z=e^{i\theta}\), the singular-value formula follows.

**2. Exact level-set counts.** Let \(r\) and \(\Delta\) be as stated. By splitting off \(\ker V\), the number of solutions of \(\xi^{\mathsf T}V\xi=a\) is \(p^{d-r}\) times the count for a nondegenerate form of dimension \(r\). For the latter, introduce the additive-character orthogonality indicator \(p^{-1}\sum_{s\in\mathbb F_p}\zeta_p^{s(Q(\xi)-a)}\). Each \(s\ne0\) contributes \(\chi_p(s)^r\chi_p(\Delta)G_p^r\). If \(r=2m\), the \(s\)-sum is \(p-1\) for \(a=0\) and \(-1\) otherwise, yielding the even-rank formula using \(G_p^{2m}=\chi_p(-1)^m p^m\). If \(r=2m+1\), the sum is \(\chi_p(-a)G_p\), yielding the odd-rank formula from \(G_p^{2m+2}=\chi_p(-1)^{m+1}p^{m+1}\). Use \(a=-4t\). The zero-rank case is immediate. This proves all spectral multiplicities without any finite-sample extrapolation.

**3. Invertibility and extremal conditioning.** A sum of three consecutive powers of a \(p\)-th root of unity vanishes if and only if that root has order exactly three. As \(p\) is prime, this occurs only when \(p=3\) and \(t\ne0\). Thus \(p\ge5\) gives invertibility, while \(p=3\) gives precisely the two values claimed. Every nondegenerate quadratic form of rank at least two over \(\mathbb F_p\) represents every element of \(\mathbb F_p\): for binary hyperbolic forms use a product form, for binary anisotropic forms use surjectivity of the norm map \(\mathbb F_{p^2}^{\times}\to\mathbb F_p^{\times}\), and for higher rank restrict to an invertible binary subform. Hence all \(t\) occur when \(r\ge2\). The maximum of \(|1+2\cos(2\pi t/p)|\) is three at \(t=0\); on integers from zero through \(\lfloor p/2\rfloor\), the real function decreases strictly through its unique zero near \(p/3\). Its smallest absolute sampled value is therefore attained at one of \(\lfloor p/3\rfloor\) or \(\lceil p/3\rceil\). This proves the sharp condition number. Taylor expansion at \(2\pi/3\), with the nearest integer distance from \(p/3\) equal to \(1/3\), yields \(\mu_p=2\pi/(\sqrt3\,p)+O(p^{-2})\) and the asymptotic formula.

**4. Sharp ternary rank collapse.** At \(p=3\), equation (1) is nonzero precisely on the zero cone \(\xi^{\mathsf T}V\xi=0\), with modulus \(3^{d/2+1}\). If \(r=0\), its size is \(3^d\); if \(r\) is odd, its size is \(3^{d-1}\); if \(r=2m>0\), its size is \(3^{d-1}+2\sigma 3^{d-m-1}\). Among these, the minimum is \(3^{d-2}\), possible only for \(r=2\) and \(\sigma=-1\), i.e. precisely for anisotropic binary \(V\). To realize it in every dimension, take
\[
U=I_d,\qquad V=\begin{pmatrix}1&1\\1&2\end{pmatrix}\oplus0_{d-2}\quad\text{over }\mathbb F_3.
\]
Its nonzero block has determinant one and is anisotropic; the determinants of \(U,U+V,U+2V\) are respectively \(1,2,2\), so all prescribed inverses exist. Consequently \(\operatorname{rank}T_h=3^{d-2}\). For \(d=2\), the particularly transparent example has \(h(x)=-1\) at all nine positions and rank one. This completes the proof.

## Verification
The accompanying standard-library-only `verify.py` checks equation (1) by exact cyclotomic integer arithmetic for every Fourier frequency in five nondegenerate pencil cases over primes \(3,5,7,11\), including the sharp ternary example in dimensions two and three. Polynomial coefficient arrays are reduced modulo the prime cyclotomic polynomial \(1+X+\cdots+X^{p-1}\); no floating-point zero test is used. The same checker independently tests all quadratic-level multiplicities for 52 diagonal forms over primes \(3,5,7,11\). Execute with `python3 verify.py`; the program prints `VERIFY_OK` only if all assertions succeed. These finite exact checks are corroboration, not a proof for unbounded \(p\), \(d\) or all admissible pencils. The preceding algebra supplies that proof.

## Relationship to prior work
Klappenecker and Rötteler (2003), Section 2 and Theorem 2, construct mutually unbiased quadratic-phase bases over odd finite fields using quadratic Gauss sums. Their object is a family of orthonormal bases and its cross-overlaps; it does not give the convolution spectrum of determinant-weighted sums of three inverse-pencil chirps. Casazza and Fickus (2006), Section 5, compute the Fourier transform of individual finite cyclic chirps and examine frame coherence; this is a direct method precursor but does not classify the spectrum of the present three-chirp matrix pencil or its ternary rank collapse. Srivastava and collaborators (2022), Sections 3–4, establish discrete quadratic-phase Fourier and generalized convolution identities, not the precise elementary-abelian convolution symbol, its quadratic-form level-set multiplicities, or its sharp prime-three rank bound. The new contribution is the inverse-pencil alignment, complete singular-value census, arithmetic phase transition and universal sharp extremizers, rather than a claim of new quadratic Gauss sums.

## Limitations
The filter is a deliberately structured **three-chirp pencil**, not an arbitrary sum of three chirps. Both the inverse-pencil hypothesis and determinant-character weights are essential to the exact phase alignment; arbitrary weights have other cancellation behavior. The fixed-prime condition-number formula is asserted as sharp for \(\operatorname{rank}V\ge2\); the complete multiset formula, not the simplified condition number, covers rank zero and one. For \(p=3\), the rank classification uses only the stated pencil domain and does not imply generic rank estimates for arbitrary filters. The novelty comparison rests on inspected sources and recorded searches; historical equivalence in broader chirp/filter-bank literature cannot be ruled out without independent examination. No external mathematical audit has been performed.

## References
1. A. Klappenecker and M. Rötteler, *Constructions of Mutually Unbiased Bases*, arXiv:quant-ph/0309120v1, first public 15 September 2003, Section 2, Theorem 2. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Constructions-of-Mutually-Unbiased-Bases.pdf
2. P. G. Casazza and M. Fickus, *Fourier Transforms of Finite Chirps*, EURASIP Journal on Applied Signal Processing 2006, Article 70204, doi:10.1155/ASP/2006/70204, Section 5. https://link.springer.com/content/pdf/10.1155/ASP/2006/70204.pdf
3. H. M. Srivastava, W. Z. Lone, F. A. Shah, and A. I. Zayed, *Discrete Quadratic-Phase Fourier Transform: Theory and Convolution Structures*, Entropy 24 (2022), 1340, doi:10.3390/e24101340, Sections 3–4. https://pmc.ncbi.nlm.nih.gov/articles/PMC9601639/
