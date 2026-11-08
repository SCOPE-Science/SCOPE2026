---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For every odd prime power q and nonconstant affine step uT+v, u≠0, invertible coordinates (a,b)↔(x=D0/u²,y=D1/u²) yield the third discriminant z=2y−x+2. Irreducible monic quadratics correspond to all three discriminants being nonzero nonsquares. Expanded quadratic-character weight W=(1−χ(x))(1−χ(y))(1−χ(z)), proved the pairwise terms vanish, computed triple sum q and removed weighted zero-line union 3q−3, giving 8N=(q−1)(q−3). All boundaries, including q=3 zero, follow. Independent direct square-set enumeration for all nonzero-slope h over F_3,F_5,F_7,F_11,F_13 and independently implemented GF_9 matched 0,1,3,10,15,6 per shift. Finite tests corroborate, not replace, the character-sum proof.

## originality

PASS

Best-of-knowledge originality from statement-level comparison of actual primary sources and published mathematical-record search; no inspected accessible stronger theorem states or directly implies the same complete claim. Source-access and historical alias risks retained; nonhits do not establish priority. Bary–Soroker Theorem1.1 q²/8+O(q^{3/2}) does not imply N=(q²−4q+3)/8

## value

PASS

The precise finite-field count, coefficient-independence and q=3-to-5 existence cutoff give the first natural three-prime translation layer for monic quadratics, refining a known asymptotic tuple theorem. The lower-order correction and sharp small-field restriction are useful exact arithmetic facts, not simply a restatement of the leading asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
