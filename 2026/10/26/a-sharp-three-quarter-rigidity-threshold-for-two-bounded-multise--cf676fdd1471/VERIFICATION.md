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

The local binary pair (1{x≥1},1{x≥2}) reproduces min parity, including the diagonal. Total isotropy of the full span in a nondegenerate 2n-space gives dimension at most n. A surjective coordinate projection excludes a full coset, namely the fiber of (0,1), exactly a quarter of the span. If every coordinate projection has rank at most one, the nonzero projected lines must contain an actual embedding generator, so only (1,0) and (1,1) lines occur. The (1,0) bits form a self-orthogonal binary image, of dimension at most floor(|I|/2); its kernel has dimension at most the number of (1,1) coordinates. An actual digit 1 requires |I|≥2 (self-orthogonality excludes a nonzero image for |I|=1), giving codimension at least one relative to n. The construction with the first two digits identical and the other digits even is compatible and reaches the asserted bound including n=2. The independent direct-minimum clique search `python3 /workspace/independent_checks.py 5` returned 3, 6, 12, 24 for n=2 through 5; only the span argument gives the infinite claim.

## originality

PASS

The inspected multiset theorem already gives the 2^n maximum and the unique all-even extremizer. The supported distinct claim is the sharp occupancy loss under the presence of any multiplicity 1. Neither that unrestricted theorem nor an indexed equivalent supplying the subextremal loss was found in the evidence compared.

## value

PASS

The estimate gives a sharp, dimension-independent gap below the known maximum and a structural witness for the loss: one forbidden local projection state or a full dimension loss. The gap is genuinely stronger than qualitative uniqueness and the construction attains it at all sizes. Neither larger multiplicity bounds nor classification of all gap extremizers is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
