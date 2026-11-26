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

An independent global calculation avoids relying on the claimed CRT spectrum: set D=gcd(u,N), including D=N for u=0, and write the ambiguity as a normalized quadratic character sum with coefficients 3au and 3au²-v, up to a unit phase. In the squared modulus take two summation variables whose difference is h. The sum over the remaining variable vanishes unless N divides 6au h, i.e. h is a multiple of N/D. On these h, all phase terms other than -vh vanish modulo N. Orthogonality on this subgroup yields |A(u,v)|²=D/N if D divides v, zero otherwise. The conjugation characters of the distinct Weyl modes are orthogonal over the N² measured shifts, giving a normal eigenvalue N|A|² for W/sqrt(N) and no cross terms. Thus D occurs (N/D)phi(N/D) times, counting the delays of gcd D and admissible v independently. Factoring this count recovers the claimed local multiplicities, ranks, nullspace and both printed examples. At prime N only nonidentity diagonal Weyls are missing; a proper prime divisor p gives a composite null mode at (p,1). Along the specified primorial sequence, divergence of the sum of 1/p and convergence of the sum of 1/p² give the rank-fraction limit. The u=1 modes have eigenvalue one and recover every cyclic adjacent product. Nonzero-coordinate ratios alternate between c and 1/conj(c), so odd length forces unit modulus and equal ratios. For flat signals, the ±1 Weyl diagonals give at least 2/N² times the cyclic sum of squared differences of the unit ratios; cycle Poincaré with gap 4 sin²(pi/N) bounds this below by (8/N) sin²(pi/N)(1-|mean ratio|²). This implies the claimed constant using squared phase distance 2(1-|mean ratio|). Equal data on the coordinate vectors confirms that no unrestricted retrieval is asserted.

## originality

PASS

The general projector diagonalization, the prime Alltop spectrum, a sufficient local vanishing condition, CRT tensorization and graph spectral estimates are not new ingredients. The supported distinct part is the exact composite classification, including the converse and nonzero magnitude at all valuations, paired with full-support uniqueness and explicit restricted stability despite this nullspace. The closest catalogue record duplicates the local prime-power portion up to normalization, but is dated later and does not supply the remaining claims.

## value

PASS

The informative conclusion is that a natural, fully sampled Gabor intensity family can lose almost all linear lifting rank along an explicit sequence yet retain nonlinear full-support injectivity and quantitative flat-signal conditioning at each dimension. The exact arithmetic kernel says which modes are missing and why complete adjacent products nevertheless survive. This is structurally useful even though the spectral computation uses classical tools and unrestricted phase retrieval fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
