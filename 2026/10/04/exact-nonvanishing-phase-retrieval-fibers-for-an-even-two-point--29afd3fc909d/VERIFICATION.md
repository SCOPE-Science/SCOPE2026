---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every time slice, the squared STFT magnitude has exactly the character coefficients at \(0,\pm a\). Since \(L\ge4\), the \(a\) and \(-a\) characters are distinct, so the measurements recover both \(s_x=|f_x|^2+|f_{x+a}|^2\) and \(c_x=f_x\overline{f_{x+a}}\). If \(\tilde f\) has the same data, the ratios \(q_x=\tilde f_x/f_x\) obey \(q_x\overline{q_{x+a}}=1\), forcing a common phase and alternating reciprocal moduli around each even step cycle. Equality of the recovered sums factors as \((r^2-1)(r^2|f_x|^2-|f_{x+a}|^2)=0\); the nontrivial branch therefore forces constant magnitudes on each parity class and gives exactly the level swap. The converse preserves every recovered coefficient. The exact-rational verifier checks all eligible steps through \(N=120\), but the complete classification follows from these algebraic equations.

## originality

PASS

Bojarovska--Flinth give general Gabor phase-retrieval criteria, and Bartusel's full open article treats windows with ambiguity zeros and records almost-all nonvanishing uniqueness plus short-window support criteria. Those results do not classify every full-support signal for the degenerate equal two-point window. Resultary's exact hit is the audited finding itself; related cyclic-STFT findings solve different support or odd-order cases.

## value

PASS

The theorem determines the entire nonvanishing fiber of a natural degenerate short STFT window, including the exceptional set missed by generic almost-all uniqueness. Exact exceptional-fiber geometry is a motivated phase-retrieval classification rather than a routine numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
