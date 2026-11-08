---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For finite Blaschke B, D=I-T_B*T_B=P_h(1-|B|²)|H+H_B*H_B is positive; the monomial projection formula gives squared Hankel tail q²/((j+1)(j+q+1)) for j>=q and bounded first q-1 terms, implying H_{z^q} is Hilbert-Schmidt with norm²<=2q. Exponentially decaying Taylor coefficients of finite B make H_B Hilbert-Schmidt and correction trace class. Radial domination 1-|B|²<=C(1-|z|²) yields s_N(A)=O(1/N). The angular mean of the boundary derivative |B'| is deg B=m, giving for both ±j harmonic modes diagonal m/(j+1)+O(j^-2). Ky Fan lower bound and positive upper compression with M=ceil(N log N) squeeze S_N(A)/log N to 2m. Positive trace-class correction preserves coefficient and non-trace-class result. Independently computed for B=z^m: analytic defect eigenvalues m/(j+m+1), antianalytic tail m/(j+1), validating two contributions (not proving arbitrary finite B). Finite checks are not used for infinite proof.

## originality

PASS

Comparisons distinguish evaluated final mathematical statements from source theorems. Best-of-knowledge novelty assessment; inaccessible primary literature is treated as residual risk, not proof of novelty.

## value

PASS

The positive harmonic Bergman Toeplitz isometric defect is a canonical operator invariant. Its exact degree-only weak trace/Dixmier coefficient and sharp Schatten boundary distinguish two harmonic frequency tails and extend beyond point-spectrum studies of the Toeplitz compression itself; useful benchmark for spectral asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
