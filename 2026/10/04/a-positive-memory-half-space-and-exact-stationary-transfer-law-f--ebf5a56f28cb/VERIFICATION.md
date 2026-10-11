---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For any bounded complete trajectory, variation of constants backwards in \(\dot v=y^2-v\) gives \(v(t)=\int_{-\infty}^{t}e^{-(t-s)}y(s)^2\,ds\ge0\). If it vanished, then \(y=0\) on a backward half-line; bounded backward solutions of \(\dot z=-dz\) with \(d>0\) force \(z=0\) there, and then \(\dot y=k\ne0\), a contradiction. Thus every compact invariant set lies a positive distance inside \(v>0\). The generator identities for \(u,v,v^2/2,y^2/2,z^2/2\) give \(\langle y\rangle=0\), \(\langle v\rangle=\langle y^2\rangle\), \(\langle v^2\rangle=\langle vy^2\rangle\), and \(d\langle z^2\rangle=c\langle y^2\tanh v\rangle\). Strict positivity and \(0<\tanh v<v\) on the compact support give the strict transfer chain.

## originality

PASS

The introducing 2023 paper was inspected in full-text HTML around the model, equilibrium discussion, hidden-attractor computations, bifurcations, coexistence/offset boosting and DSP realization. It contains the exact memory equation but no bounded-complete-trajectory half-space theorem or invariant-measure transfer law. Fresh Resultary search found the audited result itself and otherwise different memristor systems or stationary laws, with no stronger theorem covering this source-specific chain.

## value

PASS

The result converts a numerically explored hidden-attractor model into an exact geometric constraint and a strict stationary transfer law valid for every compact recurrent regime. The positive-memory half-space is also a useful simulation/validation invariant, so the theorem has structural value beyond a routine moment calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
