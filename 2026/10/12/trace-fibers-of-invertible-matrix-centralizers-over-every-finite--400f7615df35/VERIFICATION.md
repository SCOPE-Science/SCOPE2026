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

For cyclic primary summands the Hom dimension is deg(f) times the shorter length; distinct primaries have zero Hom. In each primary component order summands by length and reduce the action on V/fV. Maps from a shorter length into a longer length have image in fV, so the induced matrix is block triangular with the stated same-length diagonal residues. These coordinates are a surjective algebra map onto the product of matrix algebras. Invertibility is equivalent to invertibility of all these residues: a surjection modulo fV is a surjection on V by iterating the nilpotent f-action. Thus each invertible residue tuple has q^r lifts without needing an unproved assertion about the kernel. Trace counts each diagonal residue s times in the f-adic layers, with field trace back to F_q; off-diagonal blocks have trace zero. In the GL_m additive trace sum, subspace-lattice inversion of ker=0 leaves only the whole-space kernel: on each proper-kernel constraint space the trace functional is onto, as seen by scaling a rank-one operator of trace one. This gives (-1)^m Q^(m(m−1)/2). For p not dividing s, surjectivity of the separable finite-field trace (also when p divides deg f) makes every nonzero base-field frequency nontrivial in that factor; p-divisible s contributes the entire factor order. Orthogonality gives both trace fibers and the all-inactive concentration at zero. Independent python3 /workspace/reproductions/5.py checks eight exact examples by testing all ambient matrices and using permutation determinants, including equal and mixed lengths, distinct primaries, a squared irreducible, and an irreducible over F4. These are finite cross-checks, not an all-types enumeration.

## originality

PASS

The distinct claim is the exact ordinary-trace fiber formula for units of arbitrary finite-field matrix centralizers. The quotient dimensions, composition-length multiplicities and full-GL Gauss sums are known inputs, and the scalar-A case is prior work. The arbitrary-type formula is a short synthesis, not a new centralizer structure theorem or new scalar-A Gauss sum.

## value

PASS

Refining the classical full-GL trace census by a commuting constraint is natural for counting invertible commuting pairs with a prescribed trace. The closed formula covers all types without enumerating individual matrices, exposes the boundary where trace is identically zero, and gives the signed zero-versus-nonzero bias when types and lengths are mixed. This is an exact invariant of a natural family rather than a lone finite calculation; no joint determinant-and-trace formula is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
