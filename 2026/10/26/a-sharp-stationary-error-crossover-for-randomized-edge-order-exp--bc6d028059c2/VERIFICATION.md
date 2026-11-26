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

For r=1−q, column i in any sweep assigns mass at least q to i and rq to i+1 by the paths with zero or exactly one move. On a triangle any two such column supports overlap with mass at least rq, giving a uniform l1 contraction ≤1−rq on zero-sum vectors. This yields existence, uniqueness and convergence of the invariant probability law by contraction of the induced Markov operator on simplex laws in Wasserstein distance. Cyclic symmetry gives mean u and covariance VΠ/2: a symmetric circulant matrix with zero row sums is determined by its trace. The new permutation is independent of the state, so the stationary trace identity is V=aV+b with zero mixed terms. Independently evaluating the two representatives of the cyclic order classes gives b=r⁴(2+r+r²)/9 and 1−a=rD/3. The deterministic equilibria have weights (1,q,q) and (1,q,1), up to rotation. Direct symbolic substitution (`python3 /workspace/independent_checks.py 1`) reproduces both difference factorizations and q*=0.446703077326570687…, h*=0.805861161624800910…. D=q³(q²−3q+4)+q(6−q)+2>0; F′=4q+8+q²(1−q)(3−5q)>0 on (0,1), and F has opposite endpoint signs. The worst-order error difference is strictly negative because 2q⁴−6q³+7q²+2q+1>0 there. Endpoint substitution yields the limits and, with r∼h, the two small-step leading terms. This is a statement about a law of probability vectors and their mean-square error, not CTMC sample paths or almost-sure convergence to u.

## originality

PASS

The closest distinct catalogue result genuinely covers both deterministic biases via a stronger cyclic-ascent formula, and also explains an unbiased mean under cyclic rotations of one order. The distinct finding retained here is the exact invariant second moment for iid uniform draws over both order classes and its sharp comparison to the best fixed order at equal sweep cost. Neither those matched results nor the inspected literature gives that moment or crossover. The deterministic formulas and use of random ordering in themselves are not credited as distinct contributions.

## value

PASS

At identical work per step on a natural minimal directed Markov cycle, unbiasedness in mean is not sufficient for a smaller stationary squared error: the randomized method improves the small-step order but loses to a fixed order for sufficiently large steps. The exact crossover and fluctuation law's second moment provide a substantive benchmark for long-time splitting design. No generalization to larger graphs, unequal rates or other errors is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
