# Prime-order cyclic quotient Euler forms: a complete positivity classification

## Finding

For every odd prime \(p\), let \(\mu_p\) act on the complex affine plane with two nonzero weights \(a,b\in(\mathbb Z/p\mathbb Z)^\times\). The associated Euler form, extended as a real quadratic form on the full character-multiplicity space, is positive semidefinite **if and only if**
\[
\boxed{b/a\in\{-1,-2,-2^{-1}\}\pmod p.}
\]
Thus, up to a change of cyclic generator and exchange of coordinates, precisely the diagonal type \((1,-1)\) and the skew type \((1,-2)\) have nonnegative Euler forms. In each such case the radical is the one-dimensional line of constant multiplicities and the form is positive definite on its orthogonal complement. Every other pair of nonzero weights gives an indefinite form, with both positive and negative real directions.

More precisely, after normalizing the first weight to \(1\), let \(t=b/a\), let \(c=-t\in\mathbb F_p^\times\), and let \(r_k\in\{1,\ldots,p-1\}\) be the least positive representative of \(ck\pmod p\). The complete real inertia \((\nu_+,\nu_-,\nu_0)\) is
\[
\boxed{\nu_-=\#\{k\in\{1,\ldots,p-1\}:2|k-r_k|>p\},\qquad
\nu_+=p-1-\nu_-,\qquad \nu_0=1.}
\]
The two nonzero inertia numbers are even whenever they are positive. In particular, an indefinite form has at least two strictly negative and two strictly positive directions.

## Assumptions and scope

The ground field for the quotient stack is \(\mathbb C\). Let \(p\ge3\) be prime, let \(a,b\) be nonzero residues, and write \(u=(u_j)_{j\in\mathbb Z/p\mathbb Z}\in\mathbb R^p\). The quadratic form is the unique polynomial extension of the Euler correction formula for character multiplicities:
\[
Q_{p;a,b}(u)=\frac12\sum_{j\in\mathbb Z/p\mathbb Z}
\bigl[(u_j-u_{j+a})^2+(u_j-u_{j+b})^2-(u_j-u_{j+a+b})^2\bigr].
\]
The indexing is cyclic throughout. If \(a+b=0\), its difference term vanishes. The theorem concerns this canonical **formal real quadratic extension**. A real vector, or an arbitrary nonnegative integer vector, need not be the character decomposition of a nonempty equivariant Hilbert scheme; indefiniteness therefore asserts no automatic geometric realizability.

## Proof

**1. Euler form and normalization.** The displayed formula is the cyclic specialization of the character-difference expression for the Euler form in Bachhuber–Gholampour, Theorem 4.6, with the three nontrivial displacements \(a,b,a+b\), the final one carrying negative sign. The formula is polynomial in its coordinates, so it determines the specified quadratic form on all of \(\mathbb R^p\). Since \(a\) is invertible modulo \(p\), reindexing by its inverse replaces the weights by \((1,t)\) without changing the inertia.

**2. Exact Fourier spectrum.** Let \(H\) be the real symmetric matrix with \(Q_{p;1,t}(u)=u^{\mathsf T}Hu\). Its integer polar matrix \(2H\), with \(S\) the cyclic shift, is
\[
2H=2I-S-S^{-1}-S^t-S^{-t}+S^{1+t}+S^{-(1+t)}.
\]
The discrete Fourier vectors \(j\mapsto\exp(2\pi i kj/p)\) diagonalize \(H\), with eigenvalues
\[
\lambda_k=1-\cos(2\pi k/p)-\cos(2\pi tk/p)+\cos(2\pi(1+t)k/p),\qquad 0\le k<p.
\]
In particular, \(\lambda_0=0\). For \(1\le k<p\), write \(tk\equiv-r_k\pmod p\). The trigonometric identity \(1-\cos A-\cos B+\cos(A+B)=-4\sin(A/2)\sin(B/2)\cos((A+B)/2)\) gives
\[
\lambda_k=4\sin(\pi k/p)\sin(\pi r_k/p)\cos(\pi(k-r_k)/p).
\]
Both sine factors are strictly positive. As \(0<k,r_k<p\), the cosine is positive when \(2|k-r_k|<p\) and negative when \(2|k-r_k|>p\). Equality is impossible because \(p\) is odd. Hence every nonconstant Fourier eigenvalue is nonzero and the sign count gives exactly the stated inertia. Fourier conjugation pairs the signs at \(k\) and \(p-k\). Therefore the radical is precisely the constant line for every allowed weight pair.

**3. Arithmetic necessity of the three weight ratios.** Write \(c\in\{1,\ldots,p-1\}\). The form is positive semidefinite precisely if
\[
2|k-[ck]_p|<p\qquad(1\le k<p),
\]
where \([ck]_p\) is the representative in \(\{1,\ldots,p-1\}\). At \(k=1\), this requires \(c\le(p+1)/2\). Three values satisfy every inequality:

- If \(c=1\), then \([ck]_p=k\).
- If \(c=2\), then \([ck]_p=2k\) or \(2k-p\), according to the half containing \(k\), so \(|k-[ck]_p|\le(p-1)/2\).
- If \(c=(p+1)/2\), then \([ck]_p=k/2\) for even \(k\), and \([ck]_p=(k+p)/2\) for odd \(k\), yielding the same bound.

Conversely suppose \(3\le c\le(p-1)/2\). Set \(k=\lfloor(p-1)/c\rfloor\ge2\), so primality implies \(p=ck+r\) with \(1\le r\le c-1\), and \([ck]_p=ck=p-r\). We claim \((c-2)k>r\). For \(c\ge4\), its left side is at least \(2(c-2)\ge c>r\). For \(c=3\), the only possible failure would be \(k=r=2\), forcing \(p=8\), not prime. Thus
\[
2|k-[ck]_p|-p=2(c-1)k-(ck+r)=(c-2)k-r>0.
\]
The corresponding Fourier eigenvalue is strictly negative. This proves the complete positivity classification, since \(c=-t\) and \(c\in\{1,2,(p+1)/2\}\) translates to \(t\in\{-1,-2,-2^{-1}\}\).

**4. Strict positive directions outside the exceptional set.** For \(t\ne-1\), character orthogonality gives \(\sum_{k=0}^{p-1}\lambda_k=p>0\), since each of \(1,t,1+t\) is nonzero modulo \(p\). Thus at least one positive eigenvalue accompanies the negative one. For \(t=-1\) all nonzero eigenvalues are positive by the preceding argument. Equivalently, in the exceptional cases the formula reduces to a single connected-cycle energy \(\tfrac12\sum_j(u_j-u_{j+s})^2\) with nonzero step \(s\), up to a positive constant. This establishes all assertions.

## Verification

The accompanying `verify.py` is an executable standard-library checker. It builds the integer polar matrix directly from the three shifted squared differences, independently diagonalizes it by Fourier vectors, and checks the factorized signs against the unfactorized trigonometric eigenvalues. It exhausts all nonzero weight ratios for each odd prime below \(200\) using *exact integer residue comparisons*, and verifies explicit arithmetic witnesses against all nonexceptional multipliers. Its output was:

`VERIFY_OK primes=45 exact_negative_witnesses=2001 trigonometric_sign_cases=40016 exact_integer_polar_cases=34`

These are finite regression checks, not an exhaustive proof over all primes. The proof of necessity is the integer inequality argument above.

## Relationship to prior work

Bachhuber and Gholampour derive the Euler form and classify quotient-stack families by coincidences among character displacements. In particular their section 7 distinguishes diagonal \((1,-1)\), scalar \((1,1)\), and \((1,-2)\) actions. Their Theorem 4.6 and sections 6–7 supply the form and action terminology used here, but do not state the all-prime positive-semidefiniteness criterion or an exact sign-count formula.

General signed-graph Laplacian papers, such as Agbanusi–Bronski–Kielty, give techniques and positivity bounds for broad classes of signed graphs; those general results alone do not supply this sharp parameter classification. A scalar-action specialization and an integral Smith-form computation for more general cyclic actions also address related Euler matrices: the former concerns only one weight ratio, while the latter specifies integral cokernels rather than their real inertia. Neither statement by itself implies the present complete prime-weight positivity classification. No novelty is asserted for the originating Euler formula, its Fourier diagonalizability, or the known individual action families.

## Limitations

Only nonzero weights of an odd-prime cyclic group are classified. Composite orders, zero weights, noncyclic groups, actual Hilbert-scheme existence, and geometric realization of negative vectors are not addressed. General signed-Laplacian criteria or earlier work may contain an implicit equivalent argument; a literature search does not certify historical priority.

## References

1. S. J. Bachhuber and A. Gholampour, *G-Equivariant Hilbert Schemes and Quadratic Forms*, arXiv:2610.12736v1 (first public 2026-10-08), Theorem 4.6 and §§6–7. https://arxiv.org/pdf/2610.12736
2. I. Agbanusi, J. C. Bronski and D. Kielty, *A moment inequality and positivity for signed graph Laplacians*, arXiv:2005.09608 (2020). https://arxiv.org/abs/2005.09608
