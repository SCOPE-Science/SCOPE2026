---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For all strictly positive rates and R0>1, the exact positive equilibrium yields q*=R0 and B=bγE=t e4/D with t=(R0−1)/R0 in (0,1). The characteristic polynomial calculated from J is λ4+e1 λ3+(e2+B)λ2+(e3+Bc)λ+BD. Expanding Δ3 gives base Hurwitz determinant e1e2e3−e3²−e1²e4>0, plus e1²(1−t)e4>0, B[c(e1e2−2e3)+e1e3]>0, and B²c(e1−c)>0; e1e2−3e3=∑_{i<j}αiαj(αi+αj)>0 and e1−c=α1+μL>0. All ηi positive, proving Hurwitz stability by the quartic Liénard–Chipart criterion. The proof excludes Hopf crossings of this equilibrium but not other global dynamics.

## originality

PASS

The motivating 2026 article proves only a conditional Hurwitz criterion (Theorem 9); its global coexistence theorem (Theorem 13) also assumes local stability and six additional negativity bounds. Exact elimination of Delta3 for every positive rate vector and every R0>1 is not supplied there. Examined analogues use different discrete-time or two-state PDE operators. No identified published result implies this universal assertion; best-of-knowledge with classical-stage-model priority risk.

## value

PASS

The determinant condition in the motivating published four-stage mite model is not a mere arbitrary algebra exercise: it separates proven local coexistence stability from an entire unclassified positive-parameter region. Showing it is automatic gives a complete sharp qualitative local threshold picture and rules out Hopf loss of the positive equilibrium anywhere for R0>1, avoiding casewise quartic tests. The result is model-specific and elementary in technique, but closes a real model-level analytical gap; this is an independently useful stability conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
