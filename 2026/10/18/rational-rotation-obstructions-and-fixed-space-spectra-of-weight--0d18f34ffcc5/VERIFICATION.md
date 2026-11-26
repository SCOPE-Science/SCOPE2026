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

In a nonzero ideal, multiplication of a vector by a basis vector corresponding to a nonzero coordinate gives a nonzero multiple of the successor basis element; squaring propagates around the cycle. For an automorphism, independence of the squares makes the supports of its basis images pairwise disjoint, so its matrix is monomial and the successor rule forces rotation by s. The coefficient recurrence doubles the exponent of c_0 at each step and inserts the unique numerator factor t on crossing index n−1−s (for s>0); closure gives c_0^N=t^(1−2^s). On the cycle containing 0 the weights multiply to c_0^H_s t^J_s, since the indices are the multiples of g_s, and both n and s are divisible by g_s. The L=n/g_s power of the map is diagonal, with successive entries related by squaring, and the entries have odd order dividing N. Accordingly all cycle products are 1 or none are, and the fixed dimension is g_s or zero even if the field characteristic divides L. The product-one equation implies closure by raising to 2^g_s−1. Counting roots in the field's cyclic multiplicative group yields exactly A_s and B_s, including s=0 (B_0=1) and q=2. The order formula follows by counting shifts modulo the order of the twist class under doubling; the tuple-orbit formula is Burnside. An independent enumeration over F_43, checking all first coefficients per shift and reducing explicit matrices phi−I over that field, found 21 matrices for each of 0,2,4 and nullity counts {0:62,6:1}. Conjugation by a shift-2 lift raises the diagonal parameter to 2^4=16 modulo 21, proving noncommutativity. The orbit number is 1+(43^6−1)/63=100339097. The proof is characteristic-independent for rational points, not a scheme calculation. The frozen verifier was inspected as source; its reported 843 cases are not relied on as an independently rerun test.

## originality

PASS

Pass for the rational fixed-space multiplicity polynomial and arithmetic separation between admissible shifts and shifts with fixed vectors. Monomiality, the graph exact sequence, and monomial isomorphism are prior. The group order and the specific order-63 example overlap with later-dated catalog records; the supported distinct contribution is the general fixed-space census, not priority for those ancillary facts or for abstract fixed-point-free groups.

## value

PASS

The classification accounts for all rational automorphisms, including the gap between existence of a rational rotation and existence of a lift preserving a nonzero vector, not detected by the group order or an algebraic-closure classification. The full fixed-space census simultaneously yields tuple-orbit counts and a freeness criterion, and the order-63 example shows that the distinction is nonvacuous for a nonabelian action on a simple algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
