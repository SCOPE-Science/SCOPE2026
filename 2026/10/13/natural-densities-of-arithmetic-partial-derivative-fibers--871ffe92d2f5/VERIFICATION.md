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

# Verification protocol and limitations

The executable program `verify.py` uses only Python's standard library, exact integers, and `fractions.Fraction` for all local divisor computations, finite inclusion--exclusion sums, and density interval endpoints. To reproduce, run `python3 verify.py` in this directory. `verification_output.txt` contains the observed successful output.

For \(p=2,3,5,7,11\), the script computes rational intervals \([S_{p,A},S_{p,A}+p^{-A}]\) for the image density, with \(A=48,32,22,18,15\), respectively; the displayed decimal bounds are only human-readable representations of these exact rational inequalities. It checks that the low-valuation divisor families are singletons, the exceptional first missing valuation is empty, and the analytic logarithmic comparison lies within the claimed tail bound.

Independently, for \(p=2,3,5\) and every \(1\le x\le60000\), the script enumerates all \(y\le p x\) meeting \(D_p(y)=x\), via one global scan to \(p\cdot60000\), and checks image membership against the divisor criterion. The preimage bound follows from \(D_p(y)=y\nu_p(y)/p\ge y/p\) whenever the output is positive. For \(0\le a\le29\) and \(1\le m\le300\) coprime to \(p\), it separately solves the valuation equations for each admissible \(k\) and confirms the number of antiderivatives. It also checks all local residue multiplicity distributions for \(a\le29\).

The full unrestricted density theorem follows from the symbolic inverse bijection, CRT periodicity, the valuation-tail density bound, inclusion--exclusion, and the logarithmic series; the code checks finite instances only. Strict positivity for all \(j\ge1\) additionally invokes the published Emmons--Xiao existence theorem. No independent audit or external certification is represented here.
