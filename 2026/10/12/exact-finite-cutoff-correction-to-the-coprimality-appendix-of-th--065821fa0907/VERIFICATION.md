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

The exact identities were checked in two independent ways inside `verify_coprime_probabilities.py`: Möbius formulas and direct brute-force counting. They agree for every \(2\le a\le30\) and \(1\le N\le60\). The script also checks the exact counterexamples \((a,N)=(6,10)\), \((3,4)\), and \((5,6)\), and compares several large finite cutoffs with the proved fixed-\(a\) limiting density.

The analytic proof, not the finite computation, establishes the infinite limit. Its critical steps are the exact Möbius expansions, periodicity of coprime residue classes, the bound \(C_a(\lfloor N/d\rfloor)\le N/d\), dominated convergence against \(d^{-2}\), and absolute convergence of the Euler product. No claim is made about uniformity in simultaneous growth of \(a\) and \(N\), or about the exact physical detector distribution.
