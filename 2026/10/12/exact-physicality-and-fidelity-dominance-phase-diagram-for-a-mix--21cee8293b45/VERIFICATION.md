---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

rho_N=g|psi_r><psi_r|+(1−g)I4/4 has eigenvalues (1+3g)/4, (1−g)/4 triple. For g=(1+r²)/(3−r²)+epsilon, 0≤r<1, epsilon>0, positivity exactly epsilon≤2(1−r²)/(3−r²). Published fidelities differ by (4p−1)/9+epsilon(3−r²)/(6(1+r²)), giving threshold p*=1/4−3epsilon(3−r²)/(8(1+r²)). Strict all-p dominance iff p*<0 subject to physicality; crossing solves r²<1/2, at r²=1/2 both epsilon bounds equal 2/5 and p=0 ties. Independently checked exact rational/symbolic inversion of physicality and threshold. Does not independently reconstruct the original channel protocol, only the published density family and fidelity inputs.

## originality

PASS

The 2010 source already imposes 0≤g≤1 yet later asserts the entangled parametrization works for every epsilon<2/3 irrespective of r. The accepted claim is a mathematically motivated correction of the invalid parameter-wide operational conclusion, joined to an exact fidelity dominance threshold and r²=1/2 intersection. It does not claim eigenvalues, source fidelity formulas or routine inequality manipulation as novel independent techniques.

## value

PASS

The source advocates epsilon-only teleportation usefulness for a channel state which can actually have negative eigenvalues, and the correction excludes nonphysical settings and gives the exact domain for comparing two operational fidelities. Though the math is elementary, the concrete mistake affects physical interpretation and the sharp r=1/sqrt2 intersection is independently useful. No general teleportation theorem claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
