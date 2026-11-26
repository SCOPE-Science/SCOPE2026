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

A simplicial automorphism preserves the forbidden triples, and the unique third point of the line through distinct nonzero a,b is a+b. Fixing 0 extends the permutation to an additive automorphism; conversely every invertible binary linear map preserves caps. The independent reproduction python3 /workspace/branches/b1e54b28-ad19-4de5-8599-85dacbc0266c/independent_check.py (full_output.txt in the same directory) gave exact augmented simplicial boundary ranks over Q (1,14,91,329,616,315,105,15), hence only reduced H₄ of rank 77. This does not rely on the frozen Morse matching. For an invariant nonempty face of k vertices in r vertex orbits, its chain sign is (−1)^(k−r), which becomes (−1)^(r−1) under alternating trace; the empty face subtracts 1. Thus the alternating fixed-face sum is the H₄ character. Enumeration of all 20160 binary matrices independently gives the stated (order, trace, count) distribution. The distinct class sizes within each nonsplit order under the classical GL₄(2)≅A₈ identification pin down the trace per class; for orders 7 and 15 each split pair has a single trace. The independent Specht character calculation matches every entry, with both self-inner-product numerators 20160 and cross numerator 0, giving absolute irreducibility and the decomposition over Q by characteristic-zero semisimplicity. In the barycentric subdivision a stabilized simplex is fixed pointwise, and rational quotient cellular chains are coinvariants of the subdivided complex; averaging is exact and identifies coinvariants with invariants. The weighted character sum is zero, so this gives precisely rational acyclicity, not contractibility or any assertion about integral quotient homology. Frozen verification scripts and recorded outputs were inspected, not executed.

## originality

PASS

The rational dimension and concentration follow already from the earlier same-complex nonequivariant homotopy type and are not credited as new. The checked early cap literature and the dated earlier catalogue statement do not compute the homology action. A later indexed result computes materially the same full GL₄(2) character and quotient acyclicity, but not the 7+70 identification; its later listing is not evidence of earlier coverage or a basis for asserting historical priority. The distinct result on the inspected evidence is the full equivariant invariant, identified with two natural restricted Specht constituents.

## value

PASS

For a standard small binary projective geometry with known nonequivariant topology, the full collineation-module structure is a natural missing invariant. The split into two irreducibles of different degrees describes which symmetries survive in homology, and it decides rational homology of the natural orbit space. The record is not credited merely for reproducing the Betti number or the abstract group identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
