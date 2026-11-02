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

PASS. Uniform iid continuous bond priorities on an open path produce the same greedy parking law as the discrete Page–Rényi process. Conditioning on the earliest accepted bond yields independent residual left and right path processes, hence a_n=Pr(left endpoint vacant)=(Σ_{j=0}^{n−2}a_j)/(n−1) and b_n=Pr(both endpoints vacant)=(Σ_{j=0}^{n−2}a_j a_{n−2−j})/(n−1), initialized a_0=0,a_1=1. The exponential generating manipulation yields a_n=Σ_{j=0}^{n−1}(−1)^j/j!; a beta-integral representation of joint remainder is strictly positive, giving cov(I_1,I_n)=b_n−a_n² with sign (−1)^n for n≥3, zero for n=2, and |cov|~2^{n−2}/(n−1)! with the stated exact coefficient. This is an analytical all-n sign and factorial asymptotic, not an extrapolation. Independent from-scratch enumeration of all (n−1)! priority orders for n=2..9 yielded cov n=3 −1/4, n=4 2/9, n=5 −9/64, n=6 59/900, n=7 −505/20736, etc., matching recurrences; a_n and signs checked through n=29. The supplied checker additionally verifies exact b_n formulas through n=79.

## originality

PASS

PASS best-of-knowledge for parity-alternating correlation of the TWO OPPOSITE BOUNDARY vacancies at every finite n, with exact factorial asymptotic; the random parking process, first-split recurrence, and one-point marginal are classical and not new. Gerin 2015 primary full text establishes infinite-line vacancy density, factorial DECAY BOUNDS for long-range correlation, and one short-range positive pair, but does not state the finite-endpoint all-parity sign or exact sharp asymptotic. Page 1959 original and the 1961 Downton note are highly plausible sources of general finite moment or multisite identities but their complete primary text was not read; this is an explicit priority risk. No decisive stronger prior implication was identified, so literature inaccessibility alone is not treated as failure.

## value

PASS

PASS. The two vacancies lie at maximum distance across the finite parking interval. Their correlation switches sign under every one-site increase and remains nonzero for all n≥3, yet dies at a precise factorial scale. This is a natural finite-volume boundary effect invisible to the standard bulk occupancy law and is more informative than a routine one-point recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
