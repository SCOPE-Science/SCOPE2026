---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

The attached `verify.py` is self-contained (Python standard library) and may be executed with `python3 verify.py` from the extracted package directory. It prints eleven sample integral Gram matrices' ranks and determinants in a compact form and ends in `EXACT_SAMPLE_CHECKS_OK` if all tests pass. These include an \(A_1\)-type quotient example, smooth two-eigenvalue example, multiple gaps, the empty regular-part case, and regular versus singular cases with identical distinct Jordan sizes.

For each sample, the program constructs contracted adjacent-difference vectors and (for a regular pencil) the line-at-infinity class in the unimodular blow-up basis. It tests pairwise orthogonality of the proposed integral cohomology generators, computes their complete integer Gram matrices, evaluates exact determinants using Bareiss elimination, and checks the gcd of maximal minors of the contracted-curve matrix equals one whenever the tested dimension is at most eight. The gcd-one check means that those finite contracted lattices are saturated.

**Logical boundary:** finite sample tests do not establish the theorem for every Kronecker type. The general saturation argument is based on the integer incidence structure of disjoint paths, with one coefficient-one class added in the regular case; the Leray sequence and degree-one top-cohomology map then imply the claimed integral ring. The proof's input describing precisely which curves are contracted is the published [1, Propositions 3.7 and 4.5, Theorem 4.6]; this is separately identified so that a reader can verify it in the source. No external verification or independent audit has been performed.
