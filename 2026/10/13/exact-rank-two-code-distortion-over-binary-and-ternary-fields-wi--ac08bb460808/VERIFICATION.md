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

The projective action is faithful by the three-point test; the order of PGL2 is the full permutation order at q=2,3. Swapping an inversion sends both ratios inside the original interval [b_k/a_j,b_l/a_i] for i<j and k<l; adjacent swaps terminate, including when weights tie. For i<j both r_j/r_i and its reciprocal are at most n, and equality in the chain of bounds requires exactly the stated repeated weight and 1,n endpoints. The kernel-column construction gives weights equal to nonzero length minus the kernel multiplicity, has rank two with at least two distinct represented kernels, and gives both sharp examples for every n≥3 with the specified zero padding. For n=2 the only rank-two code is the whole space. At q=4 the translations, nonzero dilations and inversion act evenly and generate a group of order 60; the odd transposition is the only weight-preserving matching. Every feasible matching has product of ratios 1 and is not constant, so it has an upward ratio at least 10/9 and a downward one at most 9/10. The identity attains both. The algorithm examines a constant number of messages and candidate projective maps and hence is linear in block length over either fixed field.

## originality

PASS

The credited binary example already gives the n lower-bound witness, and the projective group action is classical. The supported contribution is the exact linear optimization for all pairs in rank two over both small fields, with the uniform bound, equality criterion, and quantified obstruction at q=4. Two later indexed records give significant overlap, but neither date establishes priority or provenance; they are not evidence of earlier coverage of this record.

## value

PASS

The theorem gives an exact optimal field-linear map in a natural first nontrivial dimension of an established code distortion problem and identifies when the sharp all-pair upper bound is attained. It also exhibits explicitly where weight spectra stop being sufficient, quantitatively rather than by a bare non-equivalence example. The already known binary witness is not counted as the main value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
