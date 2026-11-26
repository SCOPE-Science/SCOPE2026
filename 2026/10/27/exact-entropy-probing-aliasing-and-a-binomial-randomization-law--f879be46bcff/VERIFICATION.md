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

Normalizing the cycle Laplacian by 2n gives eigenvalues (1-cos(2 pi j/n))/n. Each residue indicator is supported at Fourier modes j divisible by L, with combined squared weight exactly L per surviving mode. Hence T_(m,L)=S_m+log L, and the deficit is the difference of the m- and mL-grid means of g(theta)=(1-cos theta)log(1-cos theta). The integrable identity log(1-cos theta)=-log 2+2 log|1-e^(i theta)| gives complex coefficients -1/|k| at k!=0 before multiplication by 1-cos theta. For |k|>=2 multiplication takes a second difference and gives 1/[|k|(k^2-1)]; the resulting series is absolutely convergent and equals continuous g, including at zero. Grid averaging thus selects exactly the frequency multiples stated. Terms removed are precisely multiples of mL. Positivity, monotonicity and the unattained envelope follow termwise. The geometric expansion's tail starting at m^(-5) is bounded by 2 zeta(5)m^(-5)/(1-m^(-2)), uniformly in L. At L=2 circulant symmetry gives a common antipodal entry -Delta_m/(2m), and the products of vertex signs on disjoint antipodal pairs are independent fair signs. This proves the exact binomial probabilities, variance, extrema and standard normal limit with the asserted normalization. A fresh finite diagonalization compared four m,L cases with bounded series truncation errors; independent pair-sign enumerations at m=3,4,5 checked the probabilities and moments. Those checks corroborate the formulas without replacing the proof.

## originality

PASS

The supported distinct content is the explicit entropy-cycle alias coefficient, its sharp envelope and expansion, and the corresponding scale in the exact stochastic law. The generic sign of the deterministic error, periodic coloring, class-supported stochastic probes, binomial shape for identical two-point classes, and central limit theorem are not original separately. Related indexed cycle probes target a different matrix function.

## value

PASS

The exact envelope and uniform cubic coefficient sharpen what general probing bounds give on a natural benchmark. For the same number of probes the sharp deterministic magnitude and the exact randomized scale permit a precise bias and error comparison, including the improvement by a factor of sqrt(m) in RMS for the specified antipodal setting. This is useful without extending the result to other graphs or stochastic probe allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
