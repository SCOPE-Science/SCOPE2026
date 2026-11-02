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

# Reproducibility and verification

Run `python3 verify_forbidden.py` with Python 3 and no third-party packages. Its exact-integer checks use (i) suffix-automaton dynamic programming for avoiding words, (ii) a separate coefficient recurrence of the weighted cluster formula, and (iii) direct brute-force generation of all host words for smaller cases.

- \(630\) single forbidden patterns: binary lengths one through eight, ternary lengths one through four; recurrence and suffix-state histograms agree through host lengths nineteen and fourteen, respectively.
- For every tested forbidden-pattern length and alphabet, equal first-jet signatures through \(2m-1\) yield identical tested full spectra.
- Sharp witnesses checked separately for each \(4\le m\le10\), with the first total marked-letter discrepancy exactly at \(2m-1\), of size one.
- An independent brute enumeration checks \(932\) individual pattern/host-length histograms.
- The two-pattern boundary verifies equality of \(N,M\) through length twelve and different weight polynomials already at length two.

Expected output is included in `verification_output.txt`. The symbolic proof in `RESULT.md`, not finite testing, establishes the universal quantifiers. Verification code and reports are self-contained. Self-review passed; independent mathematical audit has not been performed.
