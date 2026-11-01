---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every integer m>=3 and n>=2, each nonzero coefficient a_j induces the regular m-gon a_j conv(mu_m), and the Minkowski sum P has circumradius exactly R=max_{k in Z_m^n}|sum_j a_j omega^{k_j}| (vertices of convex hull of all phase sums). Cauchy planar perimeter additivity gives per(P)=2m sin(pi/m) sum_j|a_j|; the sum has at most mn edges. For a convex polygon with at most mn sides inscribed in a radius-R disk, per(P)<=2mn R sin(pi/(mn)), strict equality classification regular mn-gon. Equal amplitudes and coefficient phases 2pi(j-1)/(mn) modulo 2pi/m give exactly this polygon. Reverse equality rigidity forces mn distinct summand edge-direction classes and equal edge lengths, hence equal coefficient moduli and equally spaced phases up to permutation, one common phase, and independent mu_m factors. The proof handles all m,n in scope, vanishing coefficients (excluded at equality), support-one degeneracies, disk centers, and the n/m limits. Independent Git-tree object reconstruction yielded the supplied SHA-1; all seven original files inspected at source commit, including verbatim verify.py Git blob, which executed VERIFY_OK for 15 extremizer exhaustions and 960 random inequalities. Finite checks are corroborative only, not proofs of all-parameter statements.

## originality

PASS

Best-of-knowledge pass for the exact m>=3 finite-order coordinate-character Sidon constant and all equality configurations, not a claim of inventing the polygon perimeter lemma. The strongest overlapping published Resultary finding proves the same type of geometric rigidity for the order-two Rademacher system only (n>=5); its signed-zonogon statement does not contain or logically imply the m>=3 regular-m-gon numeric formula without an additional finite-root geometric argument. Seigner 1997 proves the limiting order-two constant pi/2 using integration and coefficient phases; Hare-Ramsey prove qualitative epsilon-Kronecker-to-Sidon implications; Bourgain-Lewko prove structural Rademacher-Sidon and tensor/psi_2 Sidon theorems. Cartwright-Howlett-McMullen 1981 characterize endpoint values 1 and sqrt(sum d_pi^2), not this natural intermediate constant or extremizers. Searches of aliases, equal-root vector sums and polygon constructions found no independently covering m>=3 result. The formula is an elementary application of known sharp polygon geometry, a significant proximity/priority risk, so originality is best-of-knowledge only.

## value

PASS

The Fourier-analytic Sidon constant is a natural quantitative invariant for the independent coordinate characters of finite exponent, and the problem asks for its exact dependence on both torsion order m and finite cardinality n. The final answer includes a sharp closed expression for every m>=3,n>=2 and a COMPLETE rigid equality family (equal amplitudes, phases interlacing into a regular mn-gon). The result quantifies the finite-phase loss and its fixed-order asymptotic (pi/m)/sin(pi/m) and continuous-phase limit 1; it is not a sample-specific table. A future researcher working with finite torsion character sets could use this precise normalization and equality class; the source has a clear object and invariant motivation before computation. This is a modest natural exact invariant, not a new polygon theorem or broad Sidon classification. The proof uses standard geometry, which limits its depth but does not negate the exact structural fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
