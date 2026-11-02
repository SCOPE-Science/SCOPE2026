# The complete binary six-dimensional nilpotency-index census for evolution algebras

## Finding

For the field \(K=\mathbb F_2\), let \(E_M\) be the six-dimensional evolution algebra with ordered natural basis \(e_1,\ldots,e_6\), products \(e_i e_j=0\) for \(i\ne j\), and \(e_i^2=\sum_{j=i+1}^6 m_{ij}e_j\), where each \(m_{ij}\in\mathbb F_2\). There are exactly \(2^{15}=32768\) labelled strictly upper-triangular structure matrices \(M\).

Define its nilpotency index \(\nu(E_M)\) as the least integer \(k\ge2\) such that \(E_M^k=0\), with \(E_M^1=E_M\) and \(E_M^k=\sum_{i=1}^{k-1}E_M^iE_M^{k-i}\). The complete number of such matrices at each index is:

| \(\nu(E_M)\) | Number of matrices |
|---:|---:|
| 2 | 1 |
| 3 | 1329 |
| 4 | 574 |
| 5 | 9760 |
| 6 | 352 |
| 7 | 1584 |
| 8 | 96 |
| 9 | 11648 |
| 10 | 64 |
| 11 | 192 |
| 13 | 512 |
| 17 | 5632 |
| 33 | 1024 |

Every other index has count zero; the displayed numbers sum to \(32768\). Consequently, the exact nilpotency-index spectrum of **all six-dimensional nilpotent evolution algebras over \(\mathbb F_2\)** (not only the displayed labelled presentations) is
\[
\{2,3,4,5,6,7,8,9,10,11,13,17,33\}.
\]
All indices in this set also occur over any characteristic-two extension field, by scalar extension of the displayed binary witnesses. No absence theorem for the additional indices over larger fields is asserted.

## Assumptions and scope

The field is exactly \(\mathbb F_2\) for the exhaustive distribution. Counts refer to **matrices in a fixed ordered natural basis**, not isomorphism classes and not all choices of natural basis counted without repetition. In the nilpotent evolution-algebra class, the upper-triangular natural-basis criterion from Casas--Ladra--Omirov--Rozikov ensures every six-dimensional nilpotent evolution algebra over \(\mathbb F_2\) admits one of these presentations, making the zero/nonzero spectrum an isomorphism-invariant conclusion. All arithmetic is exact in \(\mathbb F_2\).

The projective conjecture motivating the finite census, formulated for **infinite fields** in the 2026 evolution-algebra survey, is not claimed to be settled here. Our exact assertion is the finite binary case, with an explicit distribution rather than only attainable indices.

## Proof

**1. Exhaustive parameter domain.** A strictly upper-triangular six-by-six binary matrix has exactly \(\binom62=15\) free entries. Number them in row-major order \((1,2),(1,3),\ldots,(1,6),(2,3),\ldots,(5,6)\). The nonnegative integers \(m<2^{15}\), interpreted as bit masks in this order, enumerate each such matrix once and only once.

**2. Exact multiplication.** Encode \(\sum_j x_je_j\) as the bit set \(x\in\{0,\ldots,63\}\). If \(r_i\) is the bit-encoded square \(e_i^2\), then for any \(x,y\) their product is exactly
\[
xy=\bigoplus_{i:\,x_i=y_i=1}r_i,
\]
where \(\oplus\) means coordinatewise addition in \(\mathbb F_2\). Thus every multiplication required by the recursive definition can be executed using finite bit operations with no approximation.

**3. Subspace recurrence.** Start with \(E^1\) spanned by all six coordinate basis vectors. For each successive integer \(k\) take, for all \(1\le i<k\), every product of a basis vector of \(E^i\) with a basis vector of \(E^{k-i}\), then row-reduce these products over \(\mathbb F_2\). Bilinearity shows that their span is **exactly** \(E^k\); induction on \(k\) proves exactness at every step. Commutativity permits the first computation to use only \(i\le k-i\).

**4. Finite stopping bound.** The classical nilpotency-index theorem for \(n\)-dimensional nilpotent evolution algebras bounds the index by \(2^{n-1}+1\), which is \(33\) here. Hence testing \(k=2,\ldots,33\) yields the first zero power for every triangular matrix, without mistaking a timeout for impossibility.

**5. Certified complete census.** The accompanying dependency-free script `nilindex_six_binary.py` contains two separately implemented algorithms: one obtains subspace bases by highest-bit elimination and products by bit intersections; another forms complete span closures under XOR and computes products by coordinatewise tests. They agree for **each** of the \(32768\) masks, and both return exactly the histogram displayed above. The script asserts the sum, the full table, and that maximal index \(33\) occurs if and only if all five immediate superdiagonal coefficients are nonzero. It also prints the SHA-256 digest of the ordered \(32768\)-byte index vector:

`31661b0672ffe4caf7417840c56b7d5b9b69a20f91d7b51ff2674843fae737f6`

The lowest-mask witnesses for the thirteen respective indices are recorded in the next section. This is an **exhaustive finite proof** of the table because the inspected space contains exactly all possible binary triangular structure matrices and each case is evaluated with the exact defining power recurrence. It is not an extrapolation from samples.

**6. From presentations to all binary nilpotent evolution algebras.** The upper-triangular natural-basis theorem for finite-dimensional nilpotent evolution algebras supplies a triangular natural basis for each binary nilpotent algebra. Thus none can exhibit an index absent from this exhaustive list; conversely the explicitly enumerated matrices furnish witnesses for every listed index. Scalar extension preserves the computed nonzero/zero span dimensions, so each witnessed index also occurs over any extension of \(\mathbb F_2\).

## Verification

Run `python3 nilindex_six_binary.py` with Python 3.9 or later; the script uses only the standard library. It checks all \(32768\) masks through two separately written exact recurrences, verifies the full thirteen-row table and the classical maximal-index criterion, and exits with `VERIFY_OK` on success.

For a witness of index \(k\), write the following mask in the bit ordering from Proof step 1: \(k=2\): `0`; \(3\): `1`; \(4\): `579`; \(5\): `33`; \(6\): `5217`; \(7\): `4675`; \(8\): `22565`; \(9\): `545`; \(10\): `26145`; \(11\): `21601`; \(13\): `21059`; \(17\): `4641`; \(33\): `21025`. These witness masks are regenerated by the verifier and are not assumed as inputs to the count.

## Relationship to prior work

Kaygorodov, Martín González, and Viruel [1], Conjecture 9, predict the spectrum of nilpotency indices of evolution algebras over **infinite** fields. For dimension six their proposed set is identical to the displayed list. Their evidence includes random computations at dimension six, not an exhaustive \(\mathbb F_2\) distribution. The present census is an exact finite-field specialization which matches the predicted set and, beyond that, gives all labelled triangular multiplicities.

Casas, Ladra, Omirov, and Rozikov [2] provide the nilpotent triangular criterion and the maximal-index \(2^{n-1}+1\) condition. Those results already imply the existence of index \(33\) and the elementary count \(2^{10}=1024\) for that index in this labelled binary model. They do **not** imply the remaining multiplicities or complete index spectrum without additional work. This census uses those classical results, rather than claiming them anew.

## Limitations

This is a complete **finite** census, not a general proof of Conjecture 9 for infinite fields. The distribution is for fixed ordered triangular presentations over \(\mathbb F_2\), not for algebra isomorphism classes, and need not be invariant under changing the distribution on presentations. Full historical priority remains subject to specialized finite-field enumeration literature. The embedded checker supplies a finite, reproducible certificate but not an argument beyond the enumerated domain.

## References

[1] I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems* (first public version October 15, 2026), arXiv:2610.22248, especially Conjecture 9. https://arxiv.org/abs/2610.22248

[2] J. M. Casas, M. Ladra, B. A. Omirov, U. A. Rozikov, *On nilpotent index and dibaricity of evolution algebras*, Linear Algebra Appl. 439 (2013), 90--105; first public arXiv version August 8, 2012, arXiv:1208.1709. https://arxiv.org/abs/1208.1709
