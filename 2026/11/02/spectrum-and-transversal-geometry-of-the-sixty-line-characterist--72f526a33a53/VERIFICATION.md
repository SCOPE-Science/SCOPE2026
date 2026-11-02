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

# Verification of the finite geometric certificate

The `verify.py` program is a standalone, ordinary exact-arithmetic Python checker. Run it with `python verify.py` after installing the version-compatible package in `requirements.txt`. Its captured execution is in `verify_output.txt`. The final line in the actual output is `VERIFY_OK`.

The checker reconstructs \(\mathbb F_{16}=\mathbb F_2[a]/(a^4+a+1)\) and verifies the exact parameter and representative line. It enumerates the complete \(S_5\)-orbit and normalizes Plücker coordinates. Each pairwise intersection is decided by all five maximal minors of the \(5\times4\) matrix of line generators. It constructs the integer adjacency matrix, checks its row sums, computes the integer characteristic polynomial exactly via SymPy, and counts all unordered pairs by adjacency and number of common neighbors. It then computes the full \(S_5\)-action on the maximally transversal pairs and the fourth-power Frobenius map; these exhaustive checks establish the three pair-orbit sizes and identify the unique conjugate-pair orbit.

An additional independent census enumerates every reduced-row-echelon representative of a projective line in \(\mathbb P^3(\mathbb F_4)\) and \(\mathbb P^3(\mathbb F_{16})\). Each candidate line is tested against the degree-four surface polynomial at five distinct projective points, an exhaustive zero-polynomial test on that line. It finds zero of \(357\) and sixty of \(70161\) ambient lines, respectively.

The named characteristic-two quartic's geometric smoothness and rank-\(20\) construction rely on Rams–Schütt; the cited characteristic-two at-most-sixty theorem of Degtyarev supplies geometric completeness. The certificate verifies the claimed *finite* invariants and makes no deduction about arbitrary fields from a finite census. Literature originality remains a historical, non-computational judgment; this verification is not an independent scientific audit.
