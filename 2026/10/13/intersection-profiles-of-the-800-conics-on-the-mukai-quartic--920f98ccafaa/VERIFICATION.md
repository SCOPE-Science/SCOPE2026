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
# Verification

Run `python3 artifacts/verify.py` from the package root. The script uses only the Python standard library and exact integer arithmetic. It reconstructs the extended binary Golay code and verifies its complete weight enumerator, generates all three standard families of minimal Leech vectors, checks that the five source vectors have the required Gram matrix, and filters the source conic equations to exactly \(800\) Leech vectors.

It then uses the proved identity \(C_\ell\cdot C_m=2-\ell\cdot m\) to exhaust all \(319600\) unordered pairs. It checks the global counts \(72240,174720,72240,400\), the two local profile classes of sizes \(480\) and \(320\), all same-class and cross-class counts, and the fact that multiplicity \(4\) is a perfect matching with \(400\) edges. A successful replay prints one line beginning `VERIFY_OK`.

The checker does not reprove the global geometric realization theorem identifying the filtered Leech classes with irreducible conics on a smooth quartic; that is a premise from Degtyarev. It also does not recompute Naskręcki's projective automorphism group or its orbit sizes; those are cited premises used only after the two profile classes have been established. The originality assessment remains literature-bounded and does not convert search failure into a proof of novelty.
