---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the stated single-focal process, sampling d distinct neighbors gives E[J(J-1)]=d(d-1)i(i-1)/[(N-1)(N-2)] for a negative focal at i positive agents, and the corresponding expression with N-i for a positive focal. Including the focal probabilities gives the stated down/up ratio (N+c-i)/(c+i). Both directions are possible at each interior state, so endpoints absorb almost surely. The harmonic equation gives successive differences proportional to the Gamma product; its denominators are exchanged by j↦N-1-j. As d increases c decreases, and the first-half nontrivial factors have strictly negative derivative in c; symmetry, the c→infinity neutral limit, and c=0 check the strict one-agent ordering and both endpoints. For fixed d, put c=aN-b exactly. Stirling's formula with the two offsets -b and 1-b yields h(x) times e^(NS(x)) uniformly on x=j/N in [0,1], with relative O(1/N) because all Gamma arguments have positive linear slopes. The saddle at 1/2 has curvature -2/(a+1/2); odd terms in the local Gaussian expansion cancel to this order on the centered integer grid and its tails away from the saddle are exponentially negligible. Thus the sum has leading factor h(1/2)*sqrt(pi*N*(a+1/2)); its reciprocal is the claimed C_d times N^(-1/2). Each fixed numerator weight tends to d^j with O(1/N) relative error. The integral of artanh(z/(1+2a)) proves rate monotonicity, the stated endpoint values and the strict inequality versus the Gaussian exponent. Fixed-width k/N integration of the extrapolated Gaussian has the claimed exponential rate, with a nonzero prefactor; no central-window failure follows. Read frozen RESULT.md, VERIFICATION.md and verify.py without executing the uploaded code. Independently accumulated log weight ratios, normalized via log-sum-exp, and tested k=3 at d=2,3,6 and N=501,2001,8001. N times the log error relative to the stated asymptotic stayed near 0.045, -1.03, -4.31 respectively, consistent with, but not proving, the error bound. No growing-degree or growing-minority asymptotic was tested or is affirmed.

## originality

PASS

The model and exact rates are prior; the finite Gamma law is a straightforward standard hitting-probability implication and the one-step kernel has an exact q-voter alias. Do not give credit for a new model, a new birth–death method, or the rate function in isolation across related sampling models. The supported contribution is the sharp fixed-d, fixed-k asymptotic with its particular without-replacement prefactor, and the quantified exponential mismatch with the Gaussian boundary extrapolation; the strict finite ordering supplements this. The materially overlapping later indexed result uses different finite sampling and a different prefactor; none of the inspected sources already implies the audited comparison and prefactor in this exact regime without a model-specific calculation.

## value

PASS

The original model has a natural, practically distinct extreme initial condition (a few minority agents); the standard Gaussian extrapolation is exponentially wrong there for every finite d>=2. The sharp asymptotic quantifies that failure and shows why sampling conventions that agree on the macroscopic barrier can disagree even at leading prefactor. This is a motivated boundary result, not just the textbook harmonic equation or a special-function rewrite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
