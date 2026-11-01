---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

At a translated Chern-critical Gaussian entire-function peak the independent jets satisfy a1=0, with s=|a0|² and t=|a2|²; the positive Jacobian for maxima is (s-2t)+, whose expectation 1/3 normalizes Palm density 3(s-2t)exp(-s-t) on s>2t. The -1/2 real log-Hessian is I plus the traceless matrix determined by c=sqrt(2)a2/a0; positivity is |c|<1, giving K=(1+|c|)/(1-|c|). Changing variable U=2t/s yields density 3(1-U)/(1+U/2)^3 and survival ((1-U)/(1+U/2))². Exact transformation gives P(K>r)=64r²/(3r²+2r+3)², hence finite E K but infinite E K². Under height s>=h, s/h->1 and t|s tends in total variation to unit Exp, so sqrt(h)c tends to two independent N(0,1) components. Congruence by diag(e^b,e^-b) yields high-peak eigenvalue splitting: b_h sqrt(h)->eta gives twice shifted planar Gaussian radius, with the stated Rician density; fixed nonzero b gives N(0,4) fluctuations about e^(4|b|). Independently integrated the U density and verified exact curvature-tail algebra at r=1,1.1,2,5,10,100; random/simulated checks alone cannot prove distributional convergence.

## originality

PASS

Abreu 2022 open-access primary article computes counts/heights of white-noise spectrogram maxima and Kac–Rice jets; its Sections 3–4 were inspected, providing the essential precursor but not the continuous condition-number mark or height-and-squeeze joint scaling. Haimi–Koliander–Romero 2022 concerns signed zero/critical-point index counts, not Hessian eigenvalue ratios; Haimi–Odelius–Romero 2025 concerns spatial two-point repulsion. Existing finite cyclic two-tap spectrogram Hessian results in Resultary are not the Gaussian entire-function Palm problem. The curvature-mark calculation and Rician crossover require further nontrivial analysis beyond Abreu height marginal. Priority risk remains from unindexed general marked random-field Kac–Rice shape laws.

## value

PASS

Peak eccentricity is a natural geometric mark of a spectrogram maximum. Its exact power-law curvature-tail index and failure of the second moment have direct significance for noise peak shape, and the critical h^-1/2 squeeze scaling separates random circularity splitting from deterministic anisotropy. The Rician transition is not a trivial re-labeling of the known peak-count or peak-height marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
