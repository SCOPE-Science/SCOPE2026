# Same-model review

## Correctness
PASS. The boundary-format degree formula is classical and was checked in the supporting full text. Legendre's formula gives
\[
\nu_p(D)
=
\nu_p(N+1)
+
\frac{\sum_j s_p(k_j)-s_p(N)}{p-1}.
\]
The digit-sum excess is zero exactly for carry-free base-\(p\) addition. In base two, positive carry-free summands correspond bijectively to nonempty blocks in a set partition of the one-bit support of \(N\), giving exactly
\[
S(s_2(N),r)
\]
unordered formats when \(N\) is even, and none when \(N\) is odd. The package checker independently verifies the degree, valuation, carry criterion, and enumeration on a broad finite range; finite tests are not used as the infinite proof.

## Originality
PASS. The inspected algebraic-geometry source places boundary hyperdeterminants inside Segre coisotropic geometry, and the supporting boundary-format paper states the factorial degree formula. Neither inspected source states the prime-adic carry criterion or the Stirling enumeration. Direct searches using odd degree, parity, valuation, binary carries, multinomial degree, and Stirling-number formulations found no covering statement. The closest local prior result concerns hypercubical formats and a different degree sequence.

Residual risk: the valuation identity is a short Legendre/Kummer consequence of the classical degree formula, and an unindexed source could have recorded it. The family-wide parity enumeration is the stronger part of the claim.

## Value
PASS. The result classifies prime avoidance for every boundary-format hyperdeterminant degree and turns parity into an exact enumeration of tensor formats. Boundary format is geometrically distinguished by Segre duality and determinant-like representations, so the arithmetic classification concerns a canonical projective family rather than an arbitrary numerical slice.

Same-model review: passed. Independent audit: not yet performed.
