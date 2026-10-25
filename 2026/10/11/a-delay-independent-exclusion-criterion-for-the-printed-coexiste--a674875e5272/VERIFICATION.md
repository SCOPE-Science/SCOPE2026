---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

At a positive equilibrium the delay disappears. The infected-prey balance forces X_S>d2/beta; G is strictly increasing, and the predator balance then yields X_I>(G(d2/beta)-d3)/(xi*delta*(1-m)) when G(d2/beta)>d3. The susceptible balance yields r-d1>(b+beta)X_I. With the exact printed Section 7.2 parameters, G(1)=89/375, xi*delta*(1-m)=609/5000, and X_I>80/261. This conflicts with the susceptible budget by -1156/6525. The reported point has infected-prey residual -624357/1000000, hence nonzero derivative -44329347/2000000000. The proof is symbolic for all tau>=0; rational calculations specialize the stated parameter values. Independent exact Fraction arithmetic also checks the reported-point infected-prey residual, without using finite testing as an infinite proof.

## originality

PASS

The 2021 Wu–Meng paper supplies equilibrium equations (2.10) and claims a positive coexistence equilibrium and Hopf threshold for Section 7.2; its text does not derive the displayed delay-independent exclusion or identify its parameter contradiction. The 2019 Saha–Samanta model assumes a strong Allee effect and has different dynamics. Published discussions of equilibrium inconsistencies in other predator–prey systems do not mathematically imply this exact Wu–Meng nonexistence criterion. This is a best-of-knowledge assessment with the inaccessible predecessor full text and possibly unindexed correction identified as residual risks.

## value

PASS

A parameter-uniform structural coexistence exclusion has a substantive target: it falsifies the existence of any positive equilibrium at the principal published Section 7.2 scenario, invalidating stability and Hopf analyses centered at the reported point for the printed equations. It is stronger than a one-point residual and useful as a necessary viability screening inequality for the specified eco-epidemic model. No general claim about different equations, parameter sets or corrected simulation code is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
