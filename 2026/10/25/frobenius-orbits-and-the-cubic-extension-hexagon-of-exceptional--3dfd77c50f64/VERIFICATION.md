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

# Verification notes

Execute `python3 verify_exceptional_curves.py` with Python's standard library. The executable checks the irreducibility of the source's degree-nine base polynomial over \(\mathbb F_5\) using the polynomial gcd criterion, the root norm and fiber intersection constraints for all \(240\) root representatives, all cyclic-permutation orbits, all six fixed roots after three Frobenius steps, and all fifteen pairwise exceptional intersection numbers of those six curves.

Observed exact outputs: `irreducible: z^9+z^6+z-1 mod 5 (Rabin criterion)`, `orbit histogram: {3: 2, 9: 26}`, `F_{5^3}-defined curves: 6`, `six-curve pairwise intersection histogram: {0: 6, 2: 6, 3: 3}`, `disjointness graph is connected cycle: C6`, `all tests PASS`.

The proof also uses the geometric facts from Cheltsov et al., Theorem 1.5 and Lemma 4.1, and the integral fiber-lattice identification justified in RESULT.md. Finite checks alone do not prove that an arbitrary geometric Picard class descends to a curve or that the relative Jacobian preserves the intersection lattice; those steps are handled in the accompanying proof. No independent audit has been performed.
