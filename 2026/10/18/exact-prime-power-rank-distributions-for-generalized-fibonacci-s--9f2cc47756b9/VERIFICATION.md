---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For every odd p, k>=1, and each s modulo p^k, the first n>=1 with U_n(s)=0 exists and is counted. The Laurent identity for roots z,z^-1 with trace s yields U_ab(s)=U_a(s)U_b(V_a(s)). For nonzero discriminant mod p, Hensel roots lie in either a split unit or unramified norm-one cyclic group of order (p∓1)p^(k−1); the rank equals order(z²). Dividing the root counts by inversion gives phi(d) for d with nontrivial p-free part dividing m±=(p±1)p^(k−1)/2, with p-prime-part multiplicity correctly included. Singular traces s≡±2 mod p require ramified analysis: for p>=5 the exact formula ν_p(U_n(s))=ν_p(n) yields rank p^k for 2p^(k−1) residues; at p=3, U3(s)=s²−1 and V3 iteration give rank 3^max(1,k−ν3(s²−1)+1), yielding a tower with weights 2 at rank3 and 4*3^(a−2) for rank3^a, 2<=a<=k. These disjoint split/nonsplit/singular cases exhaust every trace, and the sums equal p^k. Independently recomputed exact first-zero histograms p=3 through k3; p=5,7 through k2; p=11 k1; all matched formulas. The valuation proof—not bounded enumeration—justifies all odd prime powers.

## originality

PASS

Best-of-knowledge comparison of exact theorem and implications, not title matching. The Chebyshev alias was checked explicitly. First-kind Chebyshev maps T_n and their iteration periods are a different object; equality of the eigenvalue parametrization does not identify their dynamical periods with the second-kind first-zero ranks. Underlying unit-group decomposition and root valuation facts are known tools, but Park prime-field ranks do not provide all p^k trace multiplicities and exceptional p3 tower. First-kind iterative fixed-point counts do not directly imply first-zero second-kind counts. A finite prime-power table would provide examples, not the uniform distribution. No equivalent complete p^k formula was found; the risk of an unindexed stronger Chebyshev root-count theorem is explicitly retained. The new p^k formula specializes to Park p1 order cases and uses the same groups, but Park/panraksa theorems do not logically determine singular trace counts across all lifts or exact odd-prime-power rank frequencies.

## value

PASS

The full first-zero rank distribution as the trace parameter s ranges across a prime-power ring is a natural invariant not supplied by first-kind Chebyshev orbit-period results. The p=3 singular tower shows genuinely delicate exceptional behavior; this precise classification answers the kind of prime-power extension Park raised and can be used for counting polynomial recurrence zero sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
