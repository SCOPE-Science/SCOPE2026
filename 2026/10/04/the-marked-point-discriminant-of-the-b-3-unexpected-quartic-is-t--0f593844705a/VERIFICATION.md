---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

On the \(c=1\) chart, direct expansion at \(B=[a:b:1]\) has no terms below degree three and gives \(T_3=-(bu-av)^3+bu^3-av^3\) and \(T_4=uv(u-v)(u+v)\). A fresh symbolic discriminant calculation gives \(-27a^2b^2(a-b-1)(a-b+1)(a+b-1)(a+b+1)\); cyclic charts therefore give the seven projective lines \(abc(a+b+c)(a+b-c)(a-b+c)(-a+b+c)=0\). Independent projective intersection enumeration gives exactly six triple and three double intersections, precisely the nine fixed \(B_3\) points. Specializing the published quartic at each of those nine points factors it into four distinct concurrent linear factors, proving multiplicity four there; away from the discriminant the binary cubic has three distinct tangent directions, and the displayed component factorizations give the stated triple-line versus double-plus-simple stratification.

## originality

PASS

The 2020 primary paper prints the exact \(B_3\) quartic family, the nine fixed points, the dual cubic, and the equality of tangent cones under BMSS duality. Targeted full-text searches in that source found no discriminant or non-Fano statement. The 2025 matrixwise-reloaded paper prominently uses the same seven-line weak combinatorics of the nine points to prove existence, but its inspected material does not identify that arrangement as the repeated-tangent-direction locus or give the singularity stratification. Current Resultary search returns the assigned discriminant theorem as the exact hit and no stronger same-object degeneration theorem.

## value

PASS

The parameter locus where the defining unexpected triple point changes analytic type is a natural geometric invariant of the canonical \(B_3\) family. Identifying it with the non-Fano arrangement and classifying its smooth-component and intersection strata explains exactly where ordinary triple points fail and where the quartic degenerates to four concurrent lines; this is more informative than a standalone symbolic discriminant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
