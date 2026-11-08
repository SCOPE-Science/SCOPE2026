---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For E:y²=x³−1 and T=(0,i), direct chord-addition algebra yields x(P)x(P+T)x(P−T)=4, independent of chosen shift. Divisor of x(P+Q) is [T−Q]+[−T−Q]−2[−Q]. On each three-element H-orbit of points, valuation columns form the 3×3 matrix with diagonal −2 and off-diagonal 1; any two columns have unit 2×2 determinant 3 modulo m, while all three sum to zero and constant product is a true mth power over C. Disjoint H-cosets have disjoint divisor support. Thus exactly t independent Kummer relations, generic compositum group (Z/m)^{r−t} and generic tensor product splits into m^t fields. At each of 3c distinct branch points at least one valuation is coprime to m (m odd prime to 3), giving inertia m; Riemann–Hurwitz over elliptic base gives genus 1+(3c/2)m^{r−t−1}(m−1) per normalization component. Independently checked identity modulo Weierstrass polynomial and all modular relation kernels for m=5,7,11,13, including explicit cases (occupancies [1,1],[2],[3],[3,1]). The field-theoretic proof, not these finite checks, establishes every allowed m and shift pattern.

## originality

PASS

Best-of-knowledge originality after inspecting the assigned theorem, searching the relevant published Resultary findings and primary literature, and comparing equivalence, broader results, exact tables and logical implications. Separated-branch genus does not logically imply the number or genus of components after collision; standard Kummer and Riemann–Hurwitz tools plus the special torsion identity calculate it. Stewart full-text coverage was not fully independently resolved. Any full general connectedness theorem for these shifted Kummer classes might subsume the proposed statement; no verified stronger result was located. The inaccessible Stewart full text is named explicitly as an important residual risk rather than dismissed. Priority is not certified; the named residual source-access and prior-coverage risks remain.

## value

PASS

Translating covers of a fixed elliptic curve is a natural construction in curve moduli. Classifying all excluded 3-torsion collision strata pinpoints exactly when the fiber product disconnects and how genus changes while recording the same generic degree; this is a complete structural boundary of the original separated-cover regime, not an arbitrary special numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
