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

# Computational verification

Run `python3 verify_linearforests.py` from the directory containing this file. Only the Python 3 standard library is required.

The program performs an exact, finite comparison between: (i) coefficients of the component-labeled exponential generating function, computed through rational polynomial multiplication; and (ii) direct enumeration of every subset of edges of the complete bipartite input graph, checking its degree sequence and acyclicity by union-find. It also compares the predicted maximum-induced-forest size and the number in each admissible component class.

The replay covered the nine boards with \(2\le m\le n\le5\) and \(m\le4\), totaling exactly 1,152,848 tested edge subsets. The printed result starts `VERIFY_OK` and reports the boardwise maximum sizes and numbers of maximum forests. The \(R_{2,4}\) check gives 30 maximizers, the \(R_{3,5}\) check gives 540, and the \(R_{4,5}\) check gives 1,440.

This verifier is not an exhaustive computation across all graph orders. The unrestricted claim is proved combinatorially in RESULT.md; no external or independent audit is asserted.
