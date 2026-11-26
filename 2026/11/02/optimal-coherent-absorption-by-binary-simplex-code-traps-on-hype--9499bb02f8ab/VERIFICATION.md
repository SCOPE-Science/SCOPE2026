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

Walsh characters diagonalize adjacency by weight. On an affine trap set each restricts to a nonzero phase times a parameter character indexed by the syndrome consisting of the XOR of its selected columns. The restricted rank is therefore the number of distinct syndromes, independent of translation. Complement preserves rank. At weights 0,N the rank is one. If r1≤N−1, the symmetric deficits at 1,N−1 alone give B≤N²−3. If r1=N all columns are distinct (zero need not be excluded), so no two sum to zero, r2≤N, and the combined low- and high-shell deficits give the same bound. For simplex, the shell Gram diagonal is c=binom(N,w) and the common off-diagonal is b_w=[z^w](1−z)(1−z²)^(L−1), L=(N+1)/2. By the displayed decreasing successive ratios within each parity, c/|b_w| on the interior is at least the endpoint ratio N(N−2)/3>N, including the two interior weights at N=7. Both Gram eigenvalues are positive there. The endpoint ranks follow from actual size-one and size-two syndrome sets and complement. The dark subspace is a direct sum of shell kernels (a vector in the sum need not itself be a single eigenvector); it is reducing, Gamma vanishes there, and a real-energy eigenvector anywhere would have zero Gamma expectation and hence lie in a shell kernel. The complementary finite-dimensional semigroup therefore decays even without diagonalizability. The captured fraction for arbitrary density matrix is its bright projection weight, so for the maximally mixed state it is B/2^N. `python3 /workspace/review-evidence/reproduce.py 5` derives physical Walsh rank lower bounds matching the analytic upper bounds at N=7, tests exact syndrome enumerators for m=3 through 7, and exhausts the 2696 spanning column multisets at m=3, obtaining 176 attainers. These finite checks do not replace the proof for all m.

## originality

PASS

The distinct claim supported here is the sharp optimum across ALL affine dimension-m placements with the specified trap budget, attained by simplex. The simplex shell profile is the support of a classical Hamming-code coset weight enumeration; it is a coding-theory consequence after translating the observable, not an independent priority claim about those ranks or enumerators. Dark spaces and algebraic walk frameworks also predate this theorem. Neither the exact enumerator for one code nor the inspected prior studies of other support families provide the universal upper bound.

## value

PASS

The result optimizes an operationally defined total capture probability under a natural affine-placement constraint, not merely evaluates a standard code table. The forced low-weight deficits explain why even the best affinity-constrained layout fails to saturate the naive rank bound, and an explicit physical layout reaches the sharper bound for all m. No interpretation as fastest decay or optimum among unconstrained trap sets is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
