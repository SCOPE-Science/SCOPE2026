---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

F^(h+1)=F^h exactly says the height is at most h with one fixed point per component. For a fixed layer vector the multinomial label choice times the product of parent choices counts every map once. In the Poisson path probabilities the parameter factors contribute r^(sum a_j) times exp(∑_{j<h}a_j t_(h−j−1)), which cancels the offspring Poisson exponential; conditioning on total n therefore gives exactly the labeled counting law. The strictly increasing saddle equation is the sum of the unconditioned layer means. For fixed h, a first failed relative-step bound can be charged against a Poisson parameter bounded below by a positive constant times μ_0; on the remaining paths the finitely many step errors multiply within the target tolerance. Rounding the first h means and fixing the last to make the sum n yields positive counts within O_h(1) of those means, and their path means are perturbed by at most O_h(log n). The lowest mean is much larger than (log n)², so Stirling gives each local factor asymptotic to (2πμ_j)^(-1/2). Their product gives the stated polynomial lower bound, absorbable into the root-scale tail exponent. The last product dominates the saddle equation; taking logarithms gives t_(h−1)~log n since logarithms of all other factors are lower order, and each descending recursion subtracts only log r, negligible relative to log t_i for i≥1. Inverting t_1=r exp(r) gives the Lambert scale. The cited μ_j are unconditioned means, not claimed exact conditional means. I inspected but did not execute the uploaded checker; the independently implemented complete finite checks for n=1..5 and h=3,4 matched all profile counts (python /workspace/review-evidence/independent_checks.py), and the asymptotic claim is justified by proof rather than enumeration.

## originality

PASS

The distinct content is the fixed-height labeled forest level law with a simultaneous exponential relative tail and the explicit hierarchy of scales. The standard bounded-height EGF and conditioned Boltzmann construction are not treated as independent novelty. No prior statement or direct specialization covering the concentration theorem was established in the searched sources.

## value

PASS

The simultaneous quantitative bound distinguishes all depth levels, including the root-scale rare deviations that a last-layer fraction law would miss. The Lambert and iterated-log factors identify actual scales of the natural uniform finite model. A finite conditioning argument makes the quantitative result usable without assuming an unproved local limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
