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

Writing \(r=1-\theta\), \(a=d+\delta\), and \(m=d+\alpha+b\), the paper's reproduction number gives \(\Lambda\beta/m\le d(a+\gamma)/(a+r\gamma)\) when \(R_{vac}\le1\). Because \(r(a+\gamma)\le a+r\gamma\), \(\Lambda\beta r/m\le d\). Substitution into \(B/(βm)\) yields at most \(-\delta-r(\gamma+d)\); the only apparent equality corner \(r=\delta=0\) still gives the exact strict value \(-d\). Thus \(B<0\). Root signs then give none at/below threshold and exactly one above it, including the linear \(r=0\) case. A fresh exact-rational grid checked 972 parameter/boundary configurations against these implications.

## originality

PASS

The 2024 SVIR paper was reread at its equilibrium polynomial and Theorem 3.3. The paper explicitly advertises a unique endemic equilibrium above threshold and forward bifurcation in the abstract, yet its theorem also includes an algebraic branch with one or two endemic equilibria below threshold when coefficient \(B>0\). Direct substitution of its own reproduction number shows that this sign condition cannot occur in the subthreshold regime under the stated biological parameter domain. Fresh Resultary and publisher searches found no correction or prior source making this exact sign collapse.

## value

PASS

Whether an epidemic model admits a subthreshold endemic branch is a central qualitative question. Removing an impossible backward-bifurcation branch from a published equilibrium theorem, while proving the exact all-parameter alternative, is a substantive correction with direct interpretive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
