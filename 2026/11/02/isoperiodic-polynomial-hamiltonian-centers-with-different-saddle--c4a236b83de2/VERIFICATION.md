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

For 0<r<r_c=(aq)^(-1/(q-p)), radial derivative r^(p-1)[1+aq r^(q-p) cos(kθ)] is positive and each E in (0,E_c) has one smooth inner radial root r_E(θ), with E_c=(q-p)r_c^p/(pq). Area is half integral of r_E(θ)²; integer multiplication θ↦kθ preserves normalized Haar circle measure, so areas match exactly and Hamiltonian coarea gives T=dA/dE in actual physical time. Critical points require sin(kθ)=0 and cos(kθ)=-1, r=r_c, so precisely k nondegenerate saddles outside the center. Local saddle expansion has radial quadratic coefficient -(q-p)r_c^(p-2)/2, angular +k²r_c^p/(2q), hence each passage time has coefficient [sqrt(q/(q-p)) r_c^(2-p)]/k times log(1/(E_c-E)); summing k passages gives independent total coefficient. Equal rotational sectors and bounded away-from-saddle residence imply equal k-atomic weak limit. Numerical inner-oval quadratures matched areas/periods across k=1,3,5 at four energies; asymptotic numerical ratios converge slowly due additive O(1), not a finite proof of the leading coefficient.

## originality

PASS

Gasull 2020 Problem 12 concerns how many critical periods occur for two homogeneous Hamiltonian terms; Zhuang–Liu 2023 asserts resolution of that critical-count question. Those do not by themselves equate full physical-time period functions across distinct k nor determine the number of limiting time-measure atoms. General angular rearrangement/isochrony theorems may subsume the construction, and the 2023 full article was inaccessible; this is documented priority uncertainty.

## value

PASS

The exact same area and physical period for globally nonconjugate polynomial Hamiltonian centers with 1,3,5 (or k) distinct separatrix saddles is a natural inverse-dynamics counterexample. The different limiting invariant time measures and k-independent saddle log coefficient explain precisely which orbit-topology information a period function loses. The phenomenon is structural across infinitely many admissible degrees, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
