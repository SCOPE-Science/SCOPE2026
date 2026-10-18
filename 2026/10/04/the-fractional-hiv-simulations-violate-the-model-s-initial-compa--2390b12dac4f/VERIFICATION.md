---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For any absolutely continuous X and continuous polynomial F, bounded CF kernel gives ||CFD X(t)||→0 as t↓0; thus continuous solution of CFD X=F(X) requires F(X0)=0. Checked original Ahmad et al parameter Table1 and Figures1–3 X0=(100,0,1), and independently computed rational vector (.109,.027,-2). Therefore no AC fractional solution for stated initial data, not a claim for gamma=1. Read source equations (3.4), (4.3), (4.4)–(4.6): (3.4) subtracts Xi(0) inconsistent with Definition 2.2 as printed; (4.3) uses an exponential weighted history unlike unweighted integral in that definition; (4.6) replaces its increment by unweighted newest interval. Splitting weighted integral proves exactly Q(t+h)-Q(t)=(e^-kh-1)Q(t)+∫new exp(-k(t+h-s))Xi(s)ds, with omitted term = -kh Q(t)+O(h²) and counterexample Xi=1. Results concern printed scheme, not arbitrary fractional HIV models.

## originality

PASS

General nonsingular-kernel initial-compatibility restriction is pre-existing Diethelm–Garrappa–Giusti–Stynes 2020 theorem and is explicitly NOT claimed new. The specific exact published HIV-model initial residual and independent error in its equation-to-algorithm history are not supplied by that general theorem and no prior correction to this paper was located.

## value

PASS

The two concrete errors invalidate the inference that plotted fractional paths are trajectories of the stated HIV model; a source-specific exact correction to simulation logic and history-dependent discretization is important for faithful analysis even without broader theorem. Distinguishes γ=1 and possible alternative regularized models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
