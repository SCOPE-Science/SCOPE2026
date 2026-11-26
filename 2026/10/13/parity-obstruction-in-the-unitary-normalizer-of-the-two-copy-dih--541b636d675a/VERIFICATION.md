---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The vertex action is faithful. For n≥3 every automorphism takes r to r^a with a a unit, since all elements outside the rotation subgroup have order two and r has order n. The image of f must be outside that subgroup and every resulting pair (a,b) is an automorphism by the presentation. The kernel of conjugation on the represented subgroup is precisely its centralizer, so the quotient is the image of that map, not automatically the full abstract group. In the convention r:i↦i+1, f:i↦−i, the trace on V of r^j f is the number of solutions of 2i=j modulo n and the trace on W is twice that. For even n, odd b sends f from trace 4 to trace 0; at n=4 this already rules out the shift f↦rf. For every eligible b choose 2c=b and directly conjugate r and f by the permutation i↦ai+c on both copies, giving exactly the claimed automorphism. This proves sufficiency, the odd case, and the even order nφ(n)/2. It concerns the full unitary normalizer of the stated two copies of V, not either a literal vertices-plus-edges action or a restricted error group. The frozen artifacts/verify.py was inspected, not executed; the finite check is not needed for the proof.

## originality

PASS

The supported distinct contribution is a precise correction of Eq. (125) for the explicitly stated two-copy representation, not an originality claim about dihedral characters, affine permutations or the first isomorphism theorem. The closest primary source asserts the full abstract group and attempts to implement it; the available related catalog findings concern different objects. No inspected source states or supplies the parity-restricted full unitary normalizer for this code. This is a bounded conclusion, not a priority certification.

## value

PASS

The parity computation is elementary, but it corrects an explicit full-normalizer assertion in a concrete code, in the even dyadic family that motivates its physical encoding. It gives an obstruction valid against every unitary and constructs every surviving lift, so an implementation can distinguish unavailable reflection swaps from possible normalizer operations without altering or making claims about the separate syndrome and error-group constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
