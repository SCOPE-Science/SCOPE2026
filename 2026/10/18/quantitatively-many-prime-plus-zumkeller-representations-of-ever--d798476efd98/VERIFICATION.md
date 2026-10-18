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

# Verification evidence and limits

The symbolic proof is the source of the universal and quantitative statement. Checks include the signed-binary equal-sum certificate for 46 odd prime seeds, independent exact divisor-subset-sum computations for nine small coprime products, and direct primality/modular congruence checks over 14,525 odd trial inputs (14,005 successful witnesses, 520 without a central-window witness at this small range). All finite certificate checks passed; **absence of a small witness is not evidence of impossibility** and does not violate the eventual theorem. Reproduce with `python3 verify.py`.

Critical infinite steps: (i) prime number theorem for the bound on the smallest odd prime missing from the factors of the input; (ii) uniform Siegel–Walfisz for prime counts in coprime residue classes modulo at most a fixed power of a logarithm. Those established infinite analytic results are not certified by finite testing; their ineffectivity is inherited by the final threshold. No independent external mathematical audit was performed.
