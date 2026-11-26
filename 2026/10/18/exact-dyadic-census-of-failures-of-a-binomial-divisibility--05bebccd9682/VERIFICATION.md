---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed RESULT.md lines 33–86. Rotation stabilizers act freely on positions, so their order divides both 5n+1 and 2n, making the tested quotient integral or a half-integer (integral for even n). For odd n with h=v2(3n+1), the trailing h ones of 3n force precisely the first h−1 carry-outs at positions 1 through h−1; failure means all carry-outs from h on are zero. Recomputed the seven transitions and acceptance under the actual infinite zero suffix: G rejects immediately, while the other six enter D (or remain there). The seven polynomial numerator equations check with constant-term identity matrix; padding to L bits therefore gives z(1+z)/Q, with F_0=0. The primitive C,F,D,G block has characteristic polynomial lambda(lambda−1)(lambda²−1)−1; the other blocks have spectral radius at most 1. The unique dominant simple root gives the claimed positive residue constant and all-cutoff density-zero bound. In the pole argument it is the quotient that has a pole, i.e. Q has a zero. Independently computed math.comb(5*n,2*n) % (3*n+1) for 1 <= n < 4096 and got counts 0,1,2,3,4,6,9,14,21,32,48,73,110 for L=0..12 (branches/d9759b80-6deb-4115-82f1-9370b39e5584/direct_exact_L12.txt). This is only a bounded check; the proof supplies the all-level claims. Frozen VERIFICATION.md and verify.py inspected, not executed.

## originality

PASS

Pass the explicit joint-event dyadic census and Perron asymptotic, not the known denominator bound, carry interpretation or infinitude. The same-day valuation-fibre result has a genuinely shared denominator and transfer mechanism, but its marginal count does not give the index-dependent joint event.

## value

PASS

The exceptions to a previously studied divisibility problem are a natural family. Exact prefix counts quantify how sparse the infinite failures are, including the nontrivial exponent and density zero, neither of which follows from existence or the previously available valuation marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
