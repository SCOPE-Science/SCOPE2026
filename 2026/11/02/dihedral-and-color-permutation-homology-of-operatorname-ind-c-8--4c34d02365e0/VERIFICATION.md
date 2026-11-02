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

# Exact computational verification

The supporting `verify_c8k3.py` is fully self-contained and requires Python 3.10 or newer. Command: `python3 verify_c8k3.py`.

Expected terminal marker: `C8_K3_INTEGRAL_MORSE_AND_96_ACTIONS_OK`.

The script enumerates **all** 18,721 nonempty faces, 9,353 distinct elementary Morse matches, and the 15 remaining critical cells. It proves acyclicity of the complete oriented Hasse diagram by processing every node, not sampling. It builds the integral six-by-eight Morse boundary and checks a primitive null row and a determinant-one five-by-five minor, sufficient for the exact Smith factors. It constructs a 66-term closed integral four-cycle and verifies its primitive pairing with an integral cocycle; checks that cocycle against all original five-boundaries; computes induced action on the generator and all 96 group elements; and independently tests each corresponding signed Lefschetz trace against the complete degree-five character formula.

The homotopy-type inference uses the fact that attaching maps from four-spheres into a wedge of four-spheres are classified by the integral degree vector; the machine checks the underlying integer matrix and full Morse acyclicity. No infinite-family assertion, integral classification of the representation, or integral quotient-homology claim is verified here. No independent audit has been performed.
