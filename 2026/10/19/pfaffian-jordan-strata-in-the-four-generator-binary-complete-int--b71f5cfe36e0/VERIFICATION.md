---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The general theorem follows from the explicit proof of the square-zero property, reduction of nonzero linear components by algebra automorphisms, the alternating-matrix rank calculation, and elementary finite-field form counts.

The standalone verifier `verify_rank_spectrum.py` was executed against this exact package source. It exhaustively enumerated all \(32768\) elements of the binary radical, returning rank multiplicities \(1,1,30,1120,896,30720\) for ranks \(0,1,2,4,6,8\). It also exhausted \(4096\) degree-two elements over \(\mathbb F_4\), giving ranks \(0,4,6\) with multiplicities \(1,1071,3024\), and checked \(300\) independently seeded full-radical samples over \(\mathbb F_4\). Printed success marker: `ALL_RANK_SPECTRUM_TESTS_PASSED`.

The finite-field verification does not certify an infinite-field assertion; that assertion is deduced algebraically. Numerical counts depend on the field being a power of two, and the polynomial addresses the radical rather than the whole ring. No independent mathematical audit has been performed.
