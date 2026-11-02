---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Define K_{vs}=∏_{edges on tree path v↔s}t_e and b=Kπ. For a source s, the event that both monitors are reached requires the union of two source-to-monitor paths, giving exactly ρ_ab f_s, where f_s is the product of transmissions on the source-to-monitor-path attachment. Direct neighbor cancellation proves K^{-1}=Q with Q_vv=1+∑_{e∋v}t_e²/(1−t_e²), Q_uv=−t_e/(1−t_e²) on adjacent vertices, zero otherwise; this weighted tree product-distance inverse is prior work. Applying Q to f gives zero off P_ab and c_v=1−∑_{e∈P_ab,e∋v}t_e/(1+t_e) on the path, since branches cancel. Thus Pr(Ba∩Bb)=ρπ^Tf=ρb^TQf=ρ∑_{v∈P}c_v b_v. Interior vertices have two summands each <1/2, endpoints one, hence strict coefficient positivity for 0<t_e<1. The homogeneous and adjacent formulas follow exactly. Fresh independent checker enumerated all 2–5-vertex labelled trees with two heterogeneous rational transmission families and nonuniform source priors, verifying 2712 exact monitor pairs by all source×edge configurations.

## originality

PASS

The inverse of the weighted product-distance matrix of a tree is established by Bapat–Sivasubramanian (Theorem 2.2) and earlier Bapat–Lal–Pati homogeneous versions, so Q is not new. The specific event kernel for two ever-infected monitors and its exact path-supported inverse action yield reconstruction of all joint alarms solely from the on-path marginals and transmission parameters, regardless of the unknown source law. Sharkey et al. examine time-dependent pair epidemic equations under Markovian SIR dynamics, not this exact static bond-percolation one-source source-eliminating identity. Equivalent formulations from Gaussian Markov trees or network reliability remain a priority risk; none inspected directly implies the stochastic event identity.

## value

PASS

This is a natural, source-prior-independent inverse-problem identity: |V| observable one-monitor probabilities determine all |V| choose2 pairwise co-detection probabilities on a known weighted tree. Its positive coefficients and path locality give structural constraints useful to epidemic sensor inference, and exactly distinguish what fails for cycles or multiple sources. More than routine inversion: identifying the joint infection kernel and showing Qf supported exactly on the monitor path is the key nontrivial step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
