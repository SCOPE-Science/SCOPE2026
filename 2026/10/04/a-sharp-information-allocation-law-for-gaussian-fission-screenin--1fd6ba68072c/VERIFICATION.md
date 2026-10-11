---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The split has covariance zero and is jointly Gaussian, hence its selection and inference components are independent with the displayed variances. With \(\tau=\tan\theta\), the log discovery probability is \(g(\mu\cos\theta)+g(\mu\sin\theta-z)\), where \(g=\log\Phi\) has strictly negative second derivative because the inverse Mills ratio is strictly decreasing. Both inner sine/cosine terms have negative second derivative, so the objective is strictly concave. Endpoint derivative signs give one critical point; evaluating at \(\theta=\pi/4\) places it strictly to the inference-heavy side. The first-order equation gives the weak-signal limit uniformly. Independent numerical replay reproduced \(\tau_*(1,0.05)=2.322477560969451\) and the weak-signal limit \(2.585227122870808\), while the analytic proof supplies the quantifiers.

## originality

PASS

The modern primary paper gives exactly the independent Gaussian \((U,V)\) decomposition, explains that the randomization variance allocates information between selection and inference, and explicitly says its information-averaging representation offers a possible way of selecting that variance. The inspected full text does not state the audited scalar sign-screen/independent-confirmation objective, its unique inverse-Mills optimizer, the strict \(\tau_*>1\) theorem, or the weak-signal closed form. Cox’s 1975 abstract is materially close because it studies split proportions in a normal-means significance problem, but the full article was not lawfully available in this run; under the owner rule that inaccessible plausible literature alone does not fail originality, it is retained as a specific residual risk rather than treated as proof of coverage.

## value

PASS

Information allocation is an explicit open design issue in the modern fission source. The audited theorem supplies a unique exact optimizer, proves a qualitative inference-heavy direction for every positive signal and conventional one-sided level, and yields a closed weak-signal benchmark while preserving the boundary-null probability. That is a motivated quantitative design law rather than an arbitrary numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
