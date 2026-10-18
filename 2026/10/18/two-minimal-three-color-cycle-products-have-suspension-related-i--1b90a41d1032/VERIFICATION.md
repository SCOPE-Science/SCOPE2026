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

# Reproducible verification

Run `python3 check_morse.py` followed by `python3 check_chain.py` using Python 3 standard-library modules only. The captured outputs are `morse_output.txt` and `chain_output.txt`, respectively.

The discrete-Morse verifier regenerates both categorical product graphs, all independent sets, the complete matching, and every Hasse cover relation. Its topological sort checks acyclicity on all 5,281 and 18,721 nonempty faces. It computes the signed integral Morse differential using recursion on matched lower faces and asserts that both degree-adjacent Morse differentials vanish exactly. Critical degrees for the two examples are \((0,3,4,4,4)\) and \((0,4,5,5,5)\).

The second program independently generates all signed simplicial boundary entries and makes integral unit-coefficient eliminations, finishing with five generators per complex, in exactly those degrees and with zero differential. This algebraic computation independently verifies integral homology but does not alone prove homotopy. The Forman matching and attaching-map argument in `RESULT.md` proves homotopy.

The verifier explores the complete finite complexes, not a truncated skeleton. Neither program proves the general torsion-freeness question for arbitrary categorical products. The abstract suspension comparison is deduced from the two separate wedge classifications and is not claimed to be induced by a graph morphism. No independent external audit has been performed.
