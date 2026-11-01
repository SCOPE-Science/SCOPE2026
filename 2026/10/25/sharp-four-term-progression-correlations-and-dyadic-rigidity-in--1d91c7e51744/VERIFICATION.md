---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The one-sided Rudin–Shapiro sign recursion r(2n)=r(n), r(2n+1)=(-1)^n r(n), and the four equally spaced factors give exact dyadic invariance C(2h)=C(h). The actual package verify.py defines a 30-state carry/sign transducer with three addition carries and four previous bits. I independently reimplemented its state graph: exactly 30 reachable states, exact zero-digit three-step dual stationary functional T0* f3=2f3, bounded terminal dual |f3|<=8, and exact C(1)=-1/2. All 16 odd five-bit prefixes have norm partition >16 iff prefixes 1,31, =16 iff 15,17; those boundary prefixes contract on either next spacing bit. The only two exceptional eventual constant-bit branches obey independently recomputed explicit affine vector recurrences and norm identities, including stable signs for every integer parameter t>=7; their departure contracts to strictly below 1/2 even under mandatory zero padding. Therefore no finite cutoff is substituted for the all-h bound, and the equality set is exactly powers of two. Direct independent exact terminal correlations for 150 additional odd gaps (3..299) corroborate this unrestricted proof. C is defined only for four arithmetic-progression sites and Cesàro average on the balanced Rudin–Shapiro subshift.

## originality

PASS

Mazáč (2022) gives the complete all-order correlation recurrence and examples including C(1)=-1/2 and dyadic propagations; his Theorem 6.6 and Propositions 6.4–6.10 concern higher correlations at other unequal-gap geometries, some tending to 1. The visible four-point general recursion has potential to compute any particular gap, but the inspected theorem does not establish a sharp maximum on the diagonal triple (h,2h,3h) nor exclude all other h. Ravy (2013) studies four-point coherent diffraction/homometry; Konieczny treats averaged Gowers uniformity rather than a pointwise extremal h. Resultary semantic search returned finite Fourier fourth moments, Shapiro doubling constants and generic four-frequency supports, not the Rudin–Shapiro diagonal-parameter extremum. The extra two-branch global transducer extremal induction is a substantive implication missing from the prior statements. This is a best-of-knowledge PASS, not a declaration of universal historical originality.

## value

PASS

Equal-spacing four-point correlations are a natural nontrivial higher-order statistic of an automatic system with vanishing pair correlations; the exact supremum and complete dyadic equality classification across all gaps is a genuine arithmetic rigidity theorem, not a table or substitution. No claim for arbitrary four-site shapes; those can have larger correlation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
