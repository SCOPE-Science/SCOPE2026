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
# Reproduction of exact finite checks

Use Python 3 with the standard library and run `python3 verify.py` in this directory. The script reconstructs all elementary Rule 73 pair-state transitions directly from the eight truth-table entries; checks each of the sixteen subset transitions and all sixteen reachable masks; verifies the four singleton-readability suffixes (hence state distinguishability); and verifies the transition identities proving an infinite family of minimal forbidden words.

The script independently checks 255 instances of that infinite family, computes the full fifteen-state live transition matrix and its characteristic polynomial by exact integer Faddeev–LeVerrier recurrence, proves the claimed rational numerator through a polynomial vector identity, compares finite words with direct application of the local rule through length 12, and verifies strictly positive entries in the ninth power of the live transition matrix.

The finite checks certify the explicit formulas and tables that occur in the paper. The step from those identities to the infinite language and entropy uses the displayed mathematical arguments: deterministic path recognition for arbitrary lengths, the symbolic loop for all gap parameters, a polynomial-matrix inverse identity, and Perron–Frobenius theory. No finite search is presented as a substitute for those deductions. Numerical Perron approximations are supplementary, not an exact proof of the algebraic identity.
