---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For p,q>=2 with p<q, 0<=c<1 and 0<=d<sqrt(ab), minimizing worst-direction conditional squared-error contraction is maximizing λ_min(G^{1/2}diag π G^{1/2}). Concavity and S_p×S_q averaging reduce an optimum to constant within each cluster. The spectrum then consists of p-1 eigenvalues s t/p, q-1 eigenvalues s(1-t)/q and the smaller eigenvalue of H(t), the 2x2 coupled-mode block. The exact determinant certificate det(H(t)-L0 I)=-κ(t-t0)^2 with κ=ab-d², L0=κ/(a+b+2d), t0=(b+d)/(a+b+2d) proves coupled optimum. Comparing it to the declining q-cluster contrast and the sign of qac-qd²-sd proves the uniform/mixed/coupled phases with thresholds d=c and d*=[sqrt(s²+4q²ac)-s]/(2q). PSD averaging equality together with full-support critical eigencoordinates rules out every asymmetric optimum. Independent full Gram eigensolver/scalar optimization checked d=1/4,1/3,2/5 at p=2,q=5,c=3/10, including the middle phase, and symbolic certificate code was inspected. Proof covers all allowed real parameters, finite checks do not.

## originality

PASS

The sharp one-step Kaczmarz contraction as an E-optimal probability-sampling SDP is known from Dai–Soltanalian–Pelckmans and Gower–Richtárik; norm-weighted sampling dates to Strohmer–Vershynin. The audited contribution is the explicit two-nontrivial-cluster three-regime optimizer with a distinct middle threshold and uniqueness among unrestricted asymmetric distributions, not the generic SDP.

## value

PASS

For a natural two-population correlated row family, the calculation gives a closed exact probability allocation and two structural phase transitions, useful as analytic benchmarks for E-optimal Kaczmarz experimental design; uniqueness eliminates ambiguity among asymmetric stationary sampling schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
