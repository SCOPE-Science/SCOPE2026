---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For any r>1 a generic point of E_r has exactly four normal feet inside the evolute astroid and two outside, so M(r)=2+2 Area(E_r∩astroid)/(πr). The astroid semiaxes are A=(r²−1)/r and B=r²−1; it lies within E_r exactly through r²≤2, giving 2+3(r²−1)²/(4r²). Beyond, the first-quadrant crossing parameter v=(2r²−1)/(r⁴−1) solves the ellipse–astroid intersection equation, and the two elementary antiderivatives give J and M=2+8J/(πr). Normalized-disk astroid growth proves strict monotonicity. The thin first-quadrant cap has leading horizontal width (2√3/9) ε^(3/2) and height ε(1−z^(2/3)); integrating gives the stated negative 5/2 correction and C²/not-C³ transition. The long-aspect missing quarter cap has leading integral 44√2/15, yielding 4−M~352√2/(15πr³). Independently reconstructed all eight blob identities and their exact assigned Git tree; checked symbolic cap constants, high-aspect integral, and independent ellipse/evolute overlap numerical integrals at multiple aspect ratios. The finite tests corroborate but do not prove the all-parameter analytic deductions.

## originality

PASS

Best-of-knowledge PASS for the complete explicit area-averaged normal-count function of ellipse aspect ratio, its strict monotonicity, the 5/2-order nonanalytic onset at r=sqrt(2) and sharp large-r inverse-cubic deficit. The pointwise 2-versus-4 normal classification, evolute astroid, and ellipse/evolute crossing threshold are explicitly prior results, not novel here. Relevant general normal-count theory did not supply the inspected ellipse-specific full mean and sharp asymptotics. The earlier Hann 1993 and Hug 1995 texts could not be materially inspected, so coverage uncertainty is substantive and named, not dismissed as proof of novelty.

## value

PASS

The area-averaged number of normals is a canonical scale-invariant Santaló-type convex-geometric statistic. Even for ellipses, exact normalization against a four-cusped evolute changes at the nontrivial containment threshold r=sqrt(2). The all-r law, strict monotonicity, and sharp 5/2 and inverse-cubic boundary layers give exact structural and regularity information absent from the classical pointwise normal classification, and a useful benchmark for further convex-body comparisons. It is not just a known pointwise formula reparameterized; genuine integration and asymptotic analysis are required. No claim of general convex-body formula is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
