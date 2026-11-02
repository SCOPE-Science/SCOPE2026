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

# Reproduction checks

Run `python3 verify.py` from the directory containing the program. This exhaustive finite checker independently enumerates matrix entries over prime fields, performs explicit matrix multiplication, and tests nilpotency using powers, not symbolic trace shortcuts. It checks the claimed rational probabilities for the finite cycles and separately exhausts the rank-conditioned lemma for three small-dimensional cases.

Selected exact checks: the binary triple of square order-two matrices yields \(2368/4096=37/64\), the binary length-three rectangular cycle \((1,2,3)\) yields \(1376/2048=43/64\), and the ternary two-factor test yields \(1377/6561=17/81\). The successful program terminates with `VERIFY_OK`.

These checks cover only stated finite instances. General validity follows from the linear-algebra proof in `RESULT.md` using the classical Fine–Herstein nilpotent-operator enumeration. No independent mathematical audit or external proof certification has been undertaken.
