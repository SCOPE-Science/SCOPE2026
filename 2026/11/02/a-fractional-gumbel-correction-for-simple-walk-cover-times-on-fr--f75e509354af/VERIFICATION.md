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

# Verification of the mathematical result

The standalone `checker.py` uses exact rational arithmetic in the two independent representations of excursion coverage: inclusion-exclusion over marked leaf subsets and the Markov recurrence indexed by the numbers of untouched pairs and singly incomplete pairs. It checks all integer sizes \(1\le n\le6\) and counts \(0\le m\le15\), a total of 96 exact CDF comparisons. Six independent exact mean comparisons follow.

For \(1\le n\le3\), the checker independently constructs and solves the visited-subset Markov-chain equations for the original discrete-step walk and verifies the identity \(\mathbb ET_n=3\mathbb EM_n-2\). It also performs 32 large-size numerical asymptotic comparisons in four centered locations. A complete execution reports `PASS 137 exact identities / asymptotic numerical comparisons`.

The general theorem is established analytically, not by finite enumeration. Its critical nonfinite steps are Poisson splitting, concentration for Poisson arrival counts, a uniform maximal inequality for geometric excursion lengths, and an integrable bound for the expectation-correction integral. The checker does not independently certify these infinite arguments. No independent audit has been performed.
