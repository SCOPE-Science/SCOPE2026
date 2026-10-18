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

The self-contained `verify.py` uses standard-library `fractions.Fraction` and exhaustive integer residue calculations. Reproduction command: `python3 verify.py`. Success prints `VERIFY_OK`.

The executable tests triangular-map uniform fibers for exponents one through twelve; compares the closed expression to a separately enumerated valuation disintegration for \(0\le h\le25\), all four odd residue classes modulo eight and both signs; tests congruence-square frequencies modulo \(8,16,32,64,128,256,512\) for 22 integer shifts; checks direct triangular pair residue counts against independently uniform inputs through modulus \(128\); and verifies exact rational sample values and the claimed sharp universal bounds for shifts from \(-2000\) through \(2000\).

The complete proof, including all infinite valuation tails, is in `RESULT.md`; finite tests are neither exhaustive over the 2-adic integers nor a substitute for proof. No external independent review has been conducted. The preprint motivating the equation was read at abstract level rather than in full text, and this remains a literature-coverage limitation.
