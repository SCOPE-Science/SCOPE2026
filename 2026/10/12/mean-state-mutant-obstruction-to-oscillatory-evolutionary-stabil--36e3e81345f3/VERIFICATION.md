---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The general theorem follows from inserting \(m(t)=p\) into the strict comparison and evaluating the two period averages; no numerical certificate is needed. For Definition 1c, \(m_\eta=(1-\eta)r+\eta p\) is distinct, stays in the simplex, shares period mean \(p\), and tends uniformly to the resident, so the same exact equality contradicts strictness in every deleted neighborhood.

For replicator trajectories, the stationary-mean statement follows from the identity
\[
0=\frac1\tau\int_0^\tau\frac{d}{dt}\log r_i(t)\,dt
=(Ap)_i-\frac1\tau\int_0^\tau r(t)^{\mathsf T}Ar(t)\,dt
\]
on each occupied strategy, followed by summation with weights \(p_i\). This is an analytic, all-dimensional argument with no simulation assumption.

`verify.py` performs exact rational checks for the published four-strategy game matrix, a nonconstant strictly interior trigonometric simplex path with known period mean, the global constant mutant, several near-path same-mean mutants and rational invasion fractions. It also checks stationarity of the uniform strategy in the three-strategy zero-sum rock–paper–scissors replicator game. Execute with `python verify.py`; no dependencies beyond the Python standard library. The trigonometric test path is **not claimed to solve** the four-strategy replicator system, and its finite algebraic checks do not certify existence, stability, or the universal theorem by enumeration. The unrestricted proof is in `RESULT.md`.
