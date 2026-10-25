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

# Exact checks and scope

Install SymPy using `requirements.txt`, then run `python verify.py` from the same directory. The program checks the nine finite Walsh-kernel rational identities displayed in the proof, the sign of the critical four-dimensional diagonal at \(h=3/2\), Descartes-compatible coefficients, two exact rational isolating intervals and two positive roots, and all entries in several direct rational matrix inversions. It separately checks the sign of the universal diagonal witness for a finite sample of higher dimensions.

Replay result: `VERIFY_OK 9 symbolic kernel identities, 2 root isolations, 14 dimension checks, 124 direct rational matrix entries`.

The program is not an exhaustive infinite-dimensional certificate. The argument for every dimension \(d\ge4\) is the sign-and-binomial inequality in RESULT.md. The complete timestep classification is proved only for \(d\le4\). Source inspection and bibliographic comparisons do not constitute independent mathematical validation.
