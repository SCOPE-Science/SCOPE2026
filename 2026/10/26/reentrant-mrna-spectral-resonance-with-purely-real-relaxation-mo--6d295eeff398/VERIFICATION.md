---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: For the explicitly normalized four-channel two-species birth--death circuit, the unique deterministic steady state is (m,p)=(1,1); linearization K=[[-10,−q],[1,−1]], stationary noise D=diag(20,2), and the eigenvalues (−11±√(81−4q))/2 are distinct negative for 0≤q<81/4. Independent exact symbolic matrix inversion gives mRNA PSD [20(1+ω²)+2q²]/[(10+q−ω²)²+121ω²] and protein PSD (220+2ω²)/the same denominator (two-sided Fourier convention). With x=ω², derivative of mRNA PSD has the sign P(q)/10−2(1+q²/10)x−x² where P(q)=2q³−91q²+220q−10. It strictly decreases in x, so P>0 iff a unique positive-frequency GLOBAL peak exists. The first two cubic roots are q1=0.046341956618..., q2=2.512597182950... and only these lie before 81/4; initial spectral derivatives at q=0,1,5 yield low/band/low and are stable under small rate perturbations. Protein derivative q²+240q−11010−220x−x² stays negative over this domain. Finite-system jump-process PSD not asserted: only stationary linear-noise OU approximation.

## originality

PASS

PASS (qualified): Gupta--Khammash (2022) already derives the same mathematical model protein/output resolvent and exact output positive-frequency condition; that low-pass corollary is fully credited. Aslyamov--Ptaszyński--Esposito (2025/2026) gives the general OU resolvent for gene regulation, and earlier stochastic-resonance work establishes noise peaks without complex deterministic poles. The inspected primary statements do not give the mRNA/controller reentrant two-cubic-boundary global phase diagram at fixed positive means, which remains the only claimed novelty. Priority risk from general spectral derivative criteria persists.

## value

PASS

PASS: Exact bounded feedback window with TWO distinct transitions in mRNA but not protein observable, while deterministic relaxation eigenvalues remain real, is a meaningful systems-theoretic phase diagram and distinguishes observable-dependent noise resonance from deterministic oscillations. It is not merely an arbitrary numerical frequency sweep; both thresholds and uniqueness follow from an explicit cubic sign classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
