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

The primary tetrahedron calculation decomposes the graph into three rotation sectors and gives exact secular factors. For \(k\notin2\pi\mathbb N\), the common factor \(A(k)=(k^2+3)\cos^2(k/2)-1\) is zero exactly when \(\tan^2(k/2)=k^2+2\), and the sector-specific factor is zero exactly when \(k\tan(k/2)=\pm\sqrt3\). The two alternatives cannot coincide: squaring would force \(k^2=1\), inconsistent with the first equation. Monotonicity on each tangent half-period gives one \(A\)-root in each half and exactly one signed simple root in the appropriate half. Every \(A\)-root is simple in each of all three orthogonal sectors, hence multiplicity three; a signed root occurs in one sector, hence multiplicity one. At \(k=2n\pi\), direct reduced boundary systems have kernel dimensions \(2,1,1\), giving multiplicity four. The local cotangent/tangent expansions give the stated momentum and energy offsets. The inspected verifier independently reproduces root brackets, sector kernel dimensions and asymptotic scaling but is not the proof of the all-period result.

## originality

PASS

Exner and Lipovský's full primary section gives the sector secular equations and Theorem 3.2 only as a large-\(k\) enclosure near integer multiples of \(\pi\). The audited theorem resolves the equations globally, including exactly one root on every half-period, the multiplicities \(3,1,4\), total multiplicity twelve per full momentum period, and the sharper energy shifts. The 2026 spectral-statistics paper concerns statistical phenomena and periodic-orbit combinatorics rather than this equilateral tetrahedron classification. Current Resultary searches under the exact tetrahedron/preferred-orientation/tangent equations found no stronger published same-object theorem.

## value

PASS

The exact spectrum and multiplicities of a canonical equilateral Platonic quantum graph are natural invariants, and the source itself stops at asymptotic localization. The complete half-period census and exceptional multiplicities turn that asymptotic picture into a reusable spectral reference, with sharp satellite energy offsets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
