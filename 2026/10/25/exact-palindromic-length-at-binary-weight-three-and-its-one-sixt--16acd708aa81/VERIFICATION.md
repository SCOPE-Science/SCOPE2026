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

The source \`check.py\` executes a direct minimum-palindromic-factorization dynamic program, treating the empty word separately from nonempty palindrome factors. It compares the resulting minimum against the complete arithmetic four-gap classification for all \(14641\) parameter quadruples in \(\{0,\dots,10\}^4\).

A separate enumeration generates length-\(n\) three-one words directly from choices of three positions for every \(3\leq n\leq28\), computing palindromic lengths without reference to the gap formula, and compares four-piece counts to coefficients of the proved rational generating function. The first nonzero count is \(E_8=2\) with witnesses \(00110100\) and \(00101100\). All checks passed.

Reproduce using \`python3 check.py\` with Python 3 standard library only. No finite enumeration is used as an infinite proof. The source-file proof establishes the four-tier formula and exact generating function for every admissible quadruple. No independent audit or external formal certification has been performed.
