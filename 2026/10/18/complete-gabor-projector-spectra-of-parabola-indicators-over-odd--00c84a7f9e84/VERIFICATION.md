---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Weyl character orthogonality in the Hilbert–Schmidt basis, with norms squared D, gives the frame eigenvalues D times squared window ambiguity. The Gram has the same spectrum including zeros because the analysis operator is square. D=N² cancels the squared normalization 1/N²; the eigenvalue is the squared unnormalized intersection sum. The intersection equation is 2At=B+A². For A with p-adic valuation j<k there are p^(k-j) valid B, and the fiber t=t0+p^(k-j)s reduces the phase to the modulus p^j with coefficients C+2Et0 and p^(k-j)E. Translating s by p^(j-alpha) tests divisibility of the linear coefficient by p^alpha when alpha is the valuation of the nonzero quadratic coefficient. After division, the primitive squared magnitude is the reduced modulus, by the invertible sum-and-difference substitution and additive orthogonality. For a vanishing quadratic coefficient the nonzero counts are (p-1)p^(k-j-1) times p^(k-j) valid B times p^(k-max(2j-k,0)) E times p^(k-j) C, exactly L_j. At ell=nu_p(E)<k the genuinely quadratic contribution per eligible A, summing valid B, equals (p-1)p^(2k-2ell-1), the same as the zero-shift contribution. Including A=0, eligible A are exactly the multiples of p^(floor((k+ell)/2)+1), yielding Q_(k-ell). The A=0,B≠0 shifts contribute zeros only; only the trivial Weyl displacement attains p^(2k). Colliding exponents must add, and the low exponents come from L_j while Q_s fills k through 2k-1. Dividing by p^(4k), the low-j geometric sum tends to p²/(p²+p+1), with the remaining terms O(k p^(-3k/2)) for fixed p. Independently enumerated ordered point pairs and reduced squared phase sums exactly modulo the prime-power cyclotomic polynomial for (3,2), (5,2), (3,3); all multiplicities, including zeros and the collision, match (python3 /workspace/branches/independent_replay.py 2). This is finite corroboration, not the all-depth proof. The packaged verifier and frozen FFT output were read, not executed.

## originality

PASS

The ambiguity-to-Gram reduction and Gauss-sum evaluation are prior methods; a prior Resultary result already treats additive characters on this exact parabola. Neither that result nor the inspected full Gabor spectra for other objects supply the translated-fiber valuation census and the evaluated full Gram spectrum here. The added rank and conditioning are consequences of that census, not separate claims of new general phase-retrieval machinery.

## value

PASS

The parabola is a canonical sparse window; the prime-power setting adds nontrivial fibers as translation valuation increases. Determining every positive multiplicity and the entire kernel quantifies exactly how this changes recoverability and nonzero singular-value conditioning for linear operator tomography. The limiting identifiable fraction is strictly below one and is not supplied by diagonalization alone. A nonlinear pure-state phase-retrieval conclusion would not follow and is not needed for this value assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
