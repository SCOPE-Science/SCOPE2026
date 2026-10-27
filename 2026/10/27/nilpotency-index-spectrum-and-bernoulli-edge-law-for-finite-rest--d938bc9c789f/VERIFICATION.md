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

# Reproducibility and scope

Run `python verify.py` with a standard Python 3 installation. The program constructs the finite-field addition and multiplication tables implicitly; in particular, it uses the irreducible polynomial \(u^2+u+1\) for \(\mathbb F_4\). It enumerates all restricted-range matrices for seven small parameter choices, multiplies matrices to determine nilpotency indices without presupposing the proof's index formula, and then checks the observed multiplicities against the partition/orbit enumeration.

The verified parameter triples \((q,k,c)\) are \((2,1,1)\), \((2,2,1)\), \((2,2,3)\), \((2,3,2)\), \((3,2,2)\), \((4,2,1)\) and \((5,1,2)\). Exactly \(44,642\) matrices are examined (including nonnilpotent matrices), and the final output is `VERIFY_OK 7 field/truncation cases; 44642 direct matrices`.

For example, the exact index multiplicities at \((q,k,c)=(2,3,2)\) are \(1,399,1680,2016\) at indices \(1,2,3,4\); at \((3,2,2)\) they are \(1,152,576\) at indices \(1,2,3\); at \((4,2,1)\) they are \(1,75,180\). These are direct enumerations, not symbolic substitutions of the theorem.

The general finite-field identity, exact near-maximum formula and total-variation limits require the mathematical proof in `RESULT.md`. Finite enumeration alone cannot establish them. No independent audit has been performed.
