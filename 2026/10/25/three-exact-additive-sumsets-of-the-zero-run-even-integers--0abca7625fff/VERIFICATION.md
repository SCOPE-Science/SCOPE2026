---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

A={0} plus positive binary words having only even-length maximal zero runs, with the zero convention stated distinctly from A086747. The disjoint digit decomposition A=4A ⊔(8A+1)⊔(4A+3) is exact. Simultaneous strong induction covers every residue class, with explicit base n=2 and n=5, proving A+A=A+2A=N0. The modulo-four exclusion 2 and constructive reverse inclusions then give A+4A=N0\{n≡2 mod4}. Allowed binary words are tiled by 1 and 00; their dyadic counts F_{k+2} show density zero. Independent direct binary recognition for 20,001 values and direct sumset witnesses through 4000 passed. The finite tests do not replace mutual induction.

## originality

PASS

Baum–Sweet zero-run digit condition and Fibonacci growth are old, as are substitution sumset methods (Dekking 2021/2022). The three universal exact additive-basis/dilate identities are additional claims not stated by inspected Dekking theorem examples or OEIS entries. Possible implicit derivation from a wider automatic-set theorem is qualified.

## value

PASS

Establishes sparse zero-density automatic integer set as an exact additive basis of sharp order two and classifies two natural dilated sumsets. This connects digit-language combinatorics to exact additive representation; not merely an OEIS count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
