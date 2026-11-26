---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the stated unitary transform, vanishing on the time support S is the kernel condition for its principal minor. Translation acts on this matrix by invertible diagonal factors and a scalar, so sets through the origin suffice. Independently exhausted those sets in bounded batches using the Schur complement of the origin entry and vectorized modular elimination at primitive seventh roots, in reversed field order. By the cyclotomic specialization homomorphism a nonzero residue rules out characteristic-zero singularity. The exact subset determinant recurrence in Z[T]/(T^7−1) returns zero for all 672 remaining six-sets; no smaller candidate remains. At size six the successive modular survivor counts in this run were 14208, 768, 672, 672. The 672 normalized zeros give 5488 sets by marked-point double counting. Every five-point principal block is invertible, forcing rank five and all coordinates nonzero on the nonzero kernel line. Linear similitudes preserve singularity by Galois conjugation; independent enumeration of all 2-by-2 matrices by A^T A=λI found 96 maps. Direct affine images of the three stated representatives produced disjoint classes of sizes 2352, 784, 2352 and exhausted all 5488 sets. Replay: python3 /workspace/branches/reproduce_fourier7.py <fresh-output-directory>; output in /workspace/branches/fourier7_reproduction.txt. This proves a finite standard-dot-product theorem, not an all-prime result.

## originality

PASS

The distinct contribution is the complete six-point support layer, including its exact count, coefficient lines and affine-similitude classification. Earlier verified results do not yield this classification. The separately indexed Nov. 8 result repeats the minimum at p=7 and extends six-point existence to a prime subclass, so the minimum in isolation should not be presented as exclusively established here. Its catalogue date is later than the frozen Oct. 19 record and does not itself settle priority; mathematical overlap is real but does not extend to the census and orbit theorem.

## value

PASS

The standard pairing on the first prime in the complementary residue class is a natural boundary instance of the support-disjointness problem. A complete minimal layer is more informative than another example: it determines precisely what minimum-size cancellation geometries and coefficient freedoms are available, and offers concrete orbit types to test structural conjectures beyond this finite plane.

The dated certificate retains the supplied scientific assessment, sources and limitations.
