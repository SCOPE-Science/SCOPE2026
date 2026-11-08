---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Chebyshev P_j recurrence and exact outgoing tail self-energy sigma_h(e)=(e-i sqrt(4h²-e²))/(2h²) yield local secular determinant without division by a vanishing compact-state factor. Values and derivatives at e=-1 for N=3m+1 give F_e=2(m+1)sigma_h(-1)≠0 and e=-1-epsilon/(m+1)+B epsilon², B=m/[2(m+1)²]-(2m+1)²/[2(m+1)³ sigma_h(-1)]. For h>1/2, inverse sigma=(-1+i sqrt(4h²-1))/2 gives negative imaginary coefficient. At h=1/2, physical/outgoing square-root edge and e+1≈-epsilon/(m+1) yield t^(5/2) for epsilon=-t<0; epsilon>0 below continuum gives real physical pole. Fresh independent SymPy secular expansion m=1..3 confirmed derivative identities; inspected source high-precision pole diagnostics. Perturbation asymptotics are fixed m,h, not uniform in m or h.

## originality

PASS

Weimann 2013 already constructs compact surface Fano BICs at periodic attachments, and Longhi/Molina/Flach establish related BIC and detangling mechanisms; their existence is not claimed new. This review concerns exact dependence of leakage on attachment and continuum background and a one-sided 5/2 threshold crossover. Accessible primary abstracts do not imply these coefficients; inaccessible full text and general threshold scattering asymptotics remain priority risks.

## value

PASS

Near-band-edge leakage of a compact embedded state is a natural quantitative stability invariant in discrete-waveguide resonance theory. The explicit distance-dependent linewidth and singular 5/2 law with opposite-sided bound-state transition distinguish distinct physical regimes and can guide perturbation scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
