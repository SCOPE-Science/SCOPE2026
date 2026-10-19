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

# Reproduction and proof evidence
The theorem's infinite assertions are established by the elementary circular-start incidence reduction and the complete cyclic arc equality characterization in `RESULT.md`. The finite checker is independent corroboration, not an infinite proof.

Run `python3 periodic_balance_checker.py` using Python 3.10 or later; it uses only standard-library modules. Compare stdout to `periodic_balance_checker_output.txt`.

The checker tests all 974 primitive binary periods with lengths two through nine, every binary two-run word of those lengths, and all 3222 primitive ternary periods with lengths two through seven. It enumerates nonempty patterns of lengths at most one period. For a primitive period, any pattern longer than a full period has at most one starting residue: two occurrences at different residues would force two equal length-period factors and contradict primitivity. Such patterns cannot raise the optimum above one. A separate direct substring algorithm checks every ternary test and the two-run binary equality cases with factor lengths up to twice the period plus one, without invoking the cyclic arc count formula.

The program's assertions verify both \(B(w)\le\lfloor p/2\rfloor\) and the precise equivalence between attaining the bound and the largest-minus-second-largest cyclic run criterion. The recorded output must match the actual program output; no independent audit or certification is claimed.
