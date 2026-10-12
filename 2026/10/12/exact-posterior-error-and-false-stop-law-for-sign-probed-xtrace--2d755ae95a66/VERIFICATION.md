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
The paper's naïve XTrace and XNysTrace estimators are reconstructed on \(A=\lambda I_2\) with independent Rademacher sign probes and Moore–Penrose rank-aware projector definitions.

`verify.py` exhaustively enumerates every ordered sign-probe family for \(3\le k\le8\) using exact rational arithmetic, independently calculates each leave-one-out span and basic trace estimate, and checks the three-point joint law, MSE and posterior proxy moments, correlations, and the exact adaptive stopping error events. Separate algebraic tests check the Nyström reconstruction identity on rank-one and rank-two rational sketches.

The enumeration is only a finite transcription guard. The main text proves the distribution and derived formulas for all integers \(k\ge3\). Continuous probes, spherical normalization, fast full-rank code, and global multistage stopping guarantees are outside the result.
