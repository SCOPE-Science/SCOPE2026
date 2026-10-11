# Independent mathematical audit

## correctness

PASS

The row Gram matrix has diagonal |B| and off-diagonal entry P_B(zeta^d). For d with valuation v, zeta^d is primitive of order p^(k-v), so its rational minimal polynomial Phi_{p^(k-v)} divides the integer mask precisely when that off-diagonal vanishes. Distinct required cyclotomic factors are pairwise coprime; their product divides P_B, and evaluating at one shows p^{|R(A)|} divides |B|. Conversely the proposed digit set has mask product over the required Phi_{p^s}; uniqueness of base-p digit expansions makes all coefficients 0 or 1 and keeps the exponents inside Z/(p^k). It therefore gives the matching tight frame. The singleton case has an empty scale set and minimum one. The frozen verifier exhausts Z/4, Z/8 and Z/9 and checks larger constructions, but the proof is general.

## originality

PASS

Frederick--Mayeli give the finite frame-spectral matrix framework but do not state a prime-power minimum-cardinality classification by p-adic difference scales. Lam--Leung and the full Malikiosis treatment supply vanishing-root and cyclotomic-mask structure for spectral/tiling problems, but those inspected results do not determine the minimum size of an oversampled tight frame for arbitrary A. The exact p^{|R(A)|} theorem and canonical free-digit optimizer were not found beyond the audited Resultary record.

## value

PASS

Minimum oversampling for a tight exponential frame is a natural finite-harmonic invariant. The theorem gives a complete closed form for every subset of every cyclic prime-power group and an explicit optimizer controlled only by the intrinsic p-adic difference scales, which is reusable structure rather than a finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
