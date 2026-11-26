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

Substitution of a Gaussian times its mass gives V′=2D−2V², m′=−2V(m−z_B), and per-capita mass growth r−V−(m−z_B)²−κM. Positive variance converges exponentially to √D and the mean converges to the periodic tracking solution with damping y=2√D. The harmonic lag multiplier has squared modulus ω²/(y²+ω²); the two frequencies are orthogonal over the common period and the mortality term is excluded by definition. This yields exactly f_B(y)=Λ_B−r as stated. I independently replayed the exact derivative identity, Q signs, all eight derivative signs at both B endpoints, and both polynomial endpoint comparison certificates with /workspace/record5_rate_certificate.py. The three Descartes sign variations of Q and its three disjoint sign brackets prove exactly three positive zeros of h′. Four sign brackets for f′ persist throughout [26,27] by affine dependence on B. Hence h=B has exactly four positive roots and all are simple: Rolle already puts the three h′ zeros strictly between the four roots, leaving none at a root. The maximum branches therefore vary smoothly and lie in disjoint advertised intervals. The exact B=26 and B=27 comparison polynomials are strictly positive on their required intervals, giving opposite branch-height orderings. The height difference has strictly positive envelope derivative because the high-branch argument is larger. Thus there is exactly one crossing, and the global maximizer switches discontinuously there; f_B(2)−f_B(0)=7/5+B/226>0 and f_B tends to −infinity, so no omitted endpoint can optimize. Numerical bisection independently reproduces B*=26.8881859300076 and D values 1.2664896175302, 175.4861044673641, and is not used in the proof.

## originality

PASS

The exact rate is an application of prior Gaussian tracking and harmonic superposition, not the novelty. The supported distinct contribution is a proved global two-positive-optimizer crossing in one explicit periodic quadratic model, with exactly four simple stationary points throughout the interval, opposite branch ordering at the two ends, and a unique switching intensity. The closest periodic-mutation papers give positive or intermediate optima or comparisons between rates, not this global classification.

## value

PASS

The two forcing frequencies separate slow tracking from faster tracking and suffice to refute a single, continuously varying optimal mutation rate even in a scalar quadratic-Gaussian model. The exact number of branches and unique crossing make this a useful explicit witness, not a numerical observation or a claim based on two hand-picked rates. The roughly 139-fold diffusion contrast at equality illustrates the separated optimizer scales, without implying biological coexistence or generality beyond the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
