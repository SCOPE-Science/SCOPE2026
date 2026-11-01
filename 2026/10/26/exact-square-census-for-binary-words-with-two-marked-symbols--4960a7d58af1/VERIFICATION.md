---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For w=0^a1 0^b1 0^c, every ordinary square has either zero ones (0^(2j), j<=floor(M/2)) or both ones and equals (0^u1 0^v)^2 with u+v=b, u<=a, v<=c. This proves D=floor(M/2)+[1+min(a,b,c,a+c-b)]_+. Inclusion-exclusion for runs with at least 2j zeros gives the first generating-function summand; the bijection b=u+v,a=u+r,c=v+s yields 1/((1-z)^2(1-z²)^2). Leading pole gives mean 7m/18+O(1); integer slack of M+2(T-1)<=m establishes sharp max, min and explicit even/odd maximizer families. New direct literal square-set enumeration for 1140 gap triples through m=17 reproduces D and full aggregate/extreme counts; not a substitute for the all-m proof.

## originality

PASS

Qualified PASS for complete pointwise ordinary-square count, rational full-length first moment, sharp minimum and exact max-equality census. Previously published minority-symbol upper bound is explicitly credited, and 2026 two-marker Abelian-square theorem is not equivalent.

## value

PASS

Exact binary square factor counting with a fixed minority of two ones is a natural first nontrivial case motivated by known minority-k square bounds. The complete all-length ordinary square census, sharp lower extreme and explicit count of all upper extremizers give useful invariants not contained in the global inequality, and distinguish literal from Abelian squares.

The dated certificate retains the supplied scientific assessment, sources and limitations.
