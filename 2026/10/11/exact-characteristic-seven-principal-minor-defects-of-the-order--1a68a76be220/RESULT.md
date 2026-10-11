# Exact characteristic-seven principal-minor defects of the order-fifteen Fourier matrix

## Finding
Let \(K\) be an algebraic closure of \(\mathbb F_7\), let \(\omega\in K\) be **any** primitive fifteenth root of unity, and let \(F=(\omega^{ij})_{0\le i,j<15}\). Put
\[
B=\{0,2,3,6,7,9\}\subset\mathbb Z/15\mathbb Z.
\]
For each nonempty \(S\subseteq\mathbb Z/15\mathbb Z\), the principal matrix \(F[S,S]\) is singular **if and only if**
\[
S=B+t\quad\text{or}\quad S=(\mathbb Z/15\mathbb Z)\setminus(B+t)
\quad\text{for some }t\in\mathbb Z/15\mathbb Z.
\]
There are exactly thirty such sets: fifteen of cardinality six and their fifteen complements of cardinality nine. Every singular principal matrix has **nullity exactly one**. Consequently, all other \(32737\) nonempty principal matrices are nonsingular. This is a theorem in **characteristic seven**, not an assertion of singularity over \(\mathbb C\).

## Assumptions and scope
The Fourier matrix is unnormalized. The base field may be any extension of \(\mathbb F_7\) containing a primitive fifteenth root, and the singularity classification is independent of which of the eight primitive roots is chosen. Indices and translations are modulo fifteen; the empty minor is excluded from the enumerated total. All ranks are computed over the stated field, and scalar extension does not change them.

## Proof
**Algebraic model.** Over \(\mathbb F_7\), the fifteenth cyclotomic polynomial factors as
\[
\Phi_{15}(X)=X^8-X^7+X^5-X^4+X^3-X+1
=g_0(X)g_1(X),
\]
where
\[
g_0=X^4+2X^3+4X^2+X+2,\qquad
 g_1=X^4+4X^3+2X^2+X+4.
\]
Each polynomial is monic irreducible of degree four. The two quotient fields \(K_j=\mathbb F_7[X]/(g_j)\) contain the two Frobenius orbits of primitive fifteenth roots; the image of \(X\) has order exactly fifteen. Thus one evaluation in each quotient, followed by Frobenius conjugacy, exhausts every primitive root.

**Explicit exceptional seed.** The permutation formula for a determinant, followed by reduction modulo \(\Phi_{15}\) in \(\mathbb Z[X]\), gives the exact characteristic-zero identity
\[
\det(\zeta^{ij})_{i,j\in B}
=35\bigl(3\zeta^7+\zeta^6+2\zeta^4-\zeta^3-\zeta^2+4\zeta-1\bigr),
\qquad\zeta=e^{2\pi i/15}.
\]
The degree-seven parenthesis is nonzero in \(\mathbb Q(\zeta)\), since the minimal polynomial of \(\zeta\) has degree eight. Nevertheless the entire determinant becomes zero upon reduction in characteristic seven, for either factor of \(\Phi_{15}\). The accompanying independent integer-arithmetic script evaluates all \(6!\) permutation terms and confirms every coefficient of this exact identity.

**Translations and complements.** Replacing every index \(i\) by \(i+t\) multiplies each matrix entry by \(\omega^{t i}\omega^{t j+t^2}\); this is conjugation by invertible diagonal row and column factors. Therefore all fifteen translates \(B+t\) give singular principal matrices. Moreover \(F\) is invertible in characteristic seven: \(F^{-1}=15^{-1}(\omega^{-ij})\), since fifteen is nonzero in the field. Jacobi's complementary-minor identity implies that a principal minor is zero if and only if its complementary principal minor is zero. This yields all fifteen complements as singular matrices.

**Exhaustiveness and exact nullity.** The complete finite verification enumerates every nonempty bitmask from \(1\) through \(2^{15}-1\) for **each** quotient \(K_0,K_1\). An element is represented by four base-seven coefficients, multiplication is exact polynomial multiplication followed by monic-quartic reduction, and all \(2400\) nonzero elements have checked multiplicative inverses. Gaussian elimination computes the exact rank of each principal matrix. Both field calculations return precisely the same thirty singular masks: the fifteen translates of \(B\) and their complements, and each has rank one less than its size. The remaining \(32737\) masks have full rank. The complete, independently runnable C++17 certificate is `verify_f15_char7.cpp`; it checks the field axioms needed, primitive-root orders, every rank, both orbit outputs, the predicted orbit classification, and nullity. There is no sampling or reliance on numerical tolerances.

## Verification
Run `python3 verify_seed_polynomial.py` for the integer cyclotomic determinant identity. Compile `verify_f15_char7.cpp` using `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_f15_char7.cpp -o verify_f15_char7` and execute `./verify_f15_char7`. The second program must report `nonzero_principal=32737 singular_six=15 singular_nine=15 nullity_one=30` independently for each `root_orbit=0,1`, followed by `VERIFY_OK`. The number of nonempty masks tested per orbit is exactly \(32767\), so every candidate principal minor is checked. No data files, specialized packages, or random seeds are needed.

## Relationship to prior work
Chebotarëv's prime-order Fourier minor theorem and the square-free principal-minor conjecture concern complex Fourier matrices. Caragea–Lee–Malikiosis–Pfander (arXiv:2505.24326, Theorems 1.3 and 1.4) proved principal nonsingularity for orders \(2p,3p,5p,6p,7p\) and gave a finite-characteristic **sufficient condition** for lifting to additional square-free orders. They did not classify the characteristic-seven principal minors of the composite order-fifteen base matrix. In particular, their lifting condition for order \(105=7\cdot15\) is not satisfied: the present result precisely describes the exceptional locus instead of interpreting failure of the sufficient condition as complex singularity. Gu–Zhou–Wang (arXiv:2608.17746) certified the different base matrices of orders ten and eleven in characteristics seven and thirteen to obtain complex orders seventy and 143. Zhou (arXiv:2608.06335) discusses the complex square-free conjecture and disjoint time/Fourier supports; the finite-field classification here is a different statement.

## Limitations
The result is an exact classification for order fifteen in characteristic seven only. It gives no counterexample to complex principal nonsingularity for order fifteen or 105, no negative theorem about all possible lifting or proof methods, and no result for other characteristics or matrix orders. Exact arithmetic eliminates numerical error, but the finite computation still requires the supplied certificate to be inspected or reproduced. Prior literature with unindexed equivalent characteristic-seven computations remains possible. Independent audit has not been performed.

## References
1. W. Zhou, *On number of cyclic n-roots and disjointness of Fourier supports*, arXiv:2608.06335v1 (first public: 2026-08-06), especially Section 2.3 and Conjecture 2.
2. A. Caragea, D. G. Lee, R. Malikiosis, G. E. Pfander, *Principal minors of Fourier matrices of square-free order*, arXiv:2505.24326v3 (2025), Theorems 1.3–1.4, Corollary 5.2.
3. W. Zhou, *Principal non-singularity of Fourier matrices on \(\mathbb Z_p\times\mathbb Z_q\) and \(\mathbb Z_2^k\times\mathbb Z_q\)*, arXiv:2505.01189 (2025).
4. J. Gu, L. Zhou, Y. Wang, *Principal nonsingularity of the Fourier matrices of orders 70 and 143*, arXiv:2608.17746 (2026).
