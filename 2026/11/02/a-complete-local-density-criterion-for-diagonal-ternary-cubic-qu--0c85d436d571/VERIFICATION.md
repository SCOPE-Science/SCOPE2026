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
# Verification and reproducibility

The theorem has an algebraic infinite proof in `RESULT.md`. The local input is Hasse's bound for smooth plane cubics and the standard one-coordinate Hensel lemma. The classification of the nine nonzero cubic cosets is a complete calculation in \((\mathbb Z/3\mathbb Z)^2\).

Run `python3 verify.py` from the directory containing the files. It exhausts the nonsplit coefficient pairs modulo all primes \(p\le127\) satisfying \(p\equiv1\pmod3\), and all 27 configurations of three unit coset classes with distinct valuation residues. It also checks the \(p=7\) mixed-valuation witness. Finite modular observations are consistency checks, not a proof for arbitrary primes. No external computational dependencies are required. The checker was executed and printed:

`VERIFY_OK primes_1mod3=14 noncube_unit_pairs=47232 coset_patterns=27 p7_witness=1,2,7`

The result is reviewed during self-review only; there has been no independent validation or external mathematical certification.
