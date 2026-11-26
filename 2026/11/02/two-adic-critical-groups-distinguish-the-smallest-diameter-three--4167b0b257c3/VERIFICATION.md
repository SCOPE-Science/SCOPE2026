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

The base graphs have A^2=4I+2J, degree six and adjacency eigenvalues 6,2,-2 of multiplicities 1,6,9, respectively. Products with K4 give Laplacian eigenvalues 0,4,8,12 of multiplicities 1,9,27,27; the reduced determinant is 2^147*3^27 by the matrix-tree theorem. Independent exact replay python3 -B /workspace/reproduce_frozen.py 4 regenerates both adjacency relations, checks intersection numbers from every basepoint (9,6,3;1,2,3), the full characteristic polynomials, both integer reduced determinants, and all local factors of the cofactor deleting the first vertex. The independent algorithm splits off an entire unit rank block, clears it, then divides the complementary block by p and repeats. This extracts the multiplicity of each p-adic valuation; all factors are recovered with no truncated final block. For exponents 0–6 the two-primary lists are (28,3,4,2,6,14,6) and (28,1,8,0,6,14,6); for 3 they are (36,27) at 0,1. The determinants rule out further primes, and the 28 unit factors give rank 28 mod two. The sum of min(e,2) is 67 and 69, respectively, so the two groups are distinct. This proves the finite computations, not a formula for other Doob graphs.

## originality

PASS

The retained contribution is the two-primary determination on D(1,1) and the exact four-torsion separation from H(3,4). The common intersection array, spectrum, prime-field ranks, and the base-pair counterexample are known. The Hamming factors alone are covered by specialization and small-block Smith reduction of Jacobson–Niedermaier–Reiner's Theorem 13; they are not counted as new. The arbitrary-product method in their Proposition 9 leaves the noncomplete Shrikhande factor to be analyzed. No compared statement supplies the missing Doob factors or the order-four torsion distinction at this product level.

## value

PASS

These are a canonical first diameter-three Doob–Hamming comparison, not an arbitrary 64-vertex sample. Their order-four torsion gives a specific integral separation where the common spanning-tree count and parity rank cannot. The exact two-primary Doob factors supply reusable benchmark data, with the sequence of lower invariants agreeing before the difference at order four. The Hamming factors serve as the known benchmark, not a separate scientific gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
