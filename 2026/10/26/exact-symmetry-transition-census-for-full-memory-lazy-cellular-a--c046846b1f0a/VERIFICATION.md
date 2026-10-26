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

# Reproducibility and verification

The standalone `verify.py` is a standard-library Python 3 program. Run `python verify.py` from the directory containing this document and the script. It enumerates every coloring and every full-memory lazy writing-symbol choice for cyclic groups of orders 2, 3, 4, 5, 6, 8; products of cyclic groups \(C_2^2\), \(C_2^3\), \(C_2\times C_3\), \(C_2\times C_4\), and \(C_3^2\), with binary and selected ternary alphabets.

It computes stabilizers of original and updated configurations directly from each translation, and independently checks: (i) the total \(H\)-invariant coloring count; (ii) the exact \(H\)-to-\(K\) count for each strict pair; and (iii) the diagonal count for each \(H\). On the checked 17 group/alphabet combinations, it reports `ALL PASS` and 349 counting identities.

The exhaustive tests cover only groups with at most nine sites. They do not prove the theorem for arbitrary finite groups, nor establish historical novelty. The universal proof uses finite-group Fourier orthogonality, subgroup Möbius inversion and explicit aperiodic-coloring constructions; its hypotheses, cases and boundary conditions are in `RESULT.md`.
