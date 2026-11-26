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

At a stationary observation, the rescaled backward Poisson gaps have exponential law of rate α, giving independent Beta(1,α) stick breaks and independent uniform directions. The Dirichlet-mean transform gives b_n=[t^n]exp(Σ a_j t^j), with a_n=α(1/2)_n/[2n(d/2)_n]. For the normalized summable sequence q_n=a_n/Σa_j, the two endpoint pieces of its self-convolution each contribute q_n asymptotically, while the middle is bounded by C q_n Σ_{k>K}q_k using comparability of q_{n−k} and q_n for k≤n/2. The same decomposition for fixed convolution orders gives q_n^{*j}∼j q_n, and the global self-convolution bound gives q_n^{*j}≤B^(j−1)q_n. The factorial series then rigorously yields b_n∼exp(Σa_j)a_n. Isotropy divides out the same coordinate-sphere moment as in a_n, leaving E R^(2n)∼C Γ(α+1)(2n)^−α. Monotone interpolation and a Laplace–Stieltjes Tauberian theorem for −log R give the deficit mass C ε^α. The constant is exp(−α E log(1−U_1)), not the expectation of an exponential; symmetry and the Beta(1/2,(d−1)/2) law give the stated digamma difference. Strictly decreasing trigamma proves the dimension ordering. The stationary thermal Gaussian has component variance D/μ, yielding exactly the stipulated σ after rescaling. On bounded deficit t and bounded Gaussian vectors, the norm expansion has a uniform O(σ²) error; the projected Gaussian has bounded density, so the probability kernel tends locally uniformly to the normal upper tail. The normalized deficit mass below t=η is O(η^α), and the contribution from large Gaussian vectors is bounded by a truncated Gaussian α-moment using δ≤σ(∥Z∥+|u|), plus an exponentially small term. This proves compact-u uniformity and the normalized profile H_α(u)=E[(Z−u)_+^α]. Its u=0 value is the stated half-normal moment. The packaged moment/simulation script was inspected, not executed; its printed comparisons would not prove the limit. No joint divergent-u or large-d scaling is checked or claimed.

## originality

PASS

The exact coordinate transform, Gaussian convolution and low-dimensional radial distributions are prior results, and the d=2 athermal edge coefficient is explicitly implied by the known beta law. The distinct supported finding is the fixed-d all-dimensional sharp radial shell coefficient and its normalized weak-noise boundary profile; neither was found as an evaluated statement in the inspected original passages and indexed comparisons. The unresolved general endpoint comparison is recorded below.

## value

PASS

The chance of leaving the athermal turning sphere is a motivated observable, not a statistic selected for ease of calculation. The all-dimensional coefficient and the normalized profile distinguish the chance of exceeding the original sphere from the chance at thresholds a few thermal standard deviations away, specifying the power and prefactor for comparison across dimensions and noise levels. The result adds a sharp asymptotic benchmark beyond the known existence of Gaussian smoothing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
