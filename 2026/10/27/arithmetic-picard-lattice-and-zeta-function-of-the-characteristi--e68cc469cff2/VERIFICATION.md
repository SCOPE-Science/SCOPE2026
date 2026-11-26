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

The exact F₂ equation is Dolgachev–Kondō's sextic; the geometric 42 classes generate integrally and have incidence Gram matrix M=[−2I,P;Pᵗ,−2I]. Its integral kernel consists of the relations by nondegeneracy of the geometric intersection form. Over Q the kernel is parametrized equivariantly by (Pb/2,b) with sum b=0, since PᵗP=4I+J. Squaring on the F₄ labels has seven fixed points and seven fixed lines; the trace on the relation space is 7−1=6, so the lattice trace is 14−6=8 and the multiplicities are 15 and 7. Independent exact replay: python /tmp/opencode/frozen_audit_k3_independent.py. It rebuilds incidence from projective dot products in F₄, with O the 42-by-28 orbit-sum matrix. The nonzero Smith factors of M are 1^20,2^2; those of OᵗMO are 1^8,2^6,4, which are the factors of the orbit-sum lattice since the relation kernel splits over Z and the invariant rational pairing is nondegenerate. Let L be the geometric lattice, H its fixed lattice, S the orbit-sum span. Traces of arbitrary generating lifts lie in S, hence 2H⊂S. In the projection A of M to 22 independent rows, the Hermite covolumes of A and [2A,AO] are 2048 and 262144. Thus [L:2L+S]=128 and S/2S maps injectively into L/2L (its image has dimension 15). If x∈H, then 2x∈S∩2L=2S, proving H=S. The Smith order gives absolute discriminant 256; hyperbolic signature (1,14) gives positive sign. Pic⁰ is trivial and Br(F₂)=0, so the geometric invariants are the arithmetic lattice. The independent computation does not execute the frozen verifier and checks lattice assertions, not the geometry or novelty. Cycle classes span H² and contribute eigenvalues ±2 with the stated multiplicities. Independently, in any standard affine chart the singularities have the two base coordinates in F₄ and tangent equation c²=uv after translation. The exceptional conic is split, so resolving adds q per rational node. The radicial double cover is bijective on finite-field points; adding q for seven or 21 nodes gives exactly the asserted counts and zeta, including 21 and 105.

## originality

PASS

The geometric K3, integral generators and squaring permutation are known, and the zeta function is a short consequence of the node geometry. The supported distinction is the integral arithmetic fixed-lattice calculation for this descent, especially its isomorphism type of the discriminant group and index-one orbit-sum generation. No inspected primary result or indexed finding was equivalent to this core; this is not a priority guarantee.

## value

PASS

For a natural characteristic-two K3 descent, an arithmetic Picard basis need not be recoverable integrally from geometric orbits merely by counting invariants over Q. The index-one result makes those readily defined divisors sufficient, and the discriminant and Smith factors quantify the exact integral intersection lattice for future divisor or lattice calculations. This is a motivated arithmetic invariant of the specified surface, not just a recalculation of the geometric discriminant or a finite-field point census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
