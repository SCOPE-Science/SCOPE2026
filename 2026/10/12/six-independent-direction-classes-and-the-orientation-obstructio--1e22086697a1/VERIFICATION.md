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
# Verification of the direction-characteristic-class calculation

The six incidence equations \(\langle n_{ij},v_i-v_j\rangle=0\) define the zero locus of a section of \(\bigoplus\lambda_{ij}^{\vee}\). Their differential is surjective on the open quadrangle locus by the two-case proof of Lemma 3.1 in the initiating article: if vertices are distinct, the corresponding projective-slope derivative is nonzero; if a pair coincides, its vertex-coordinate gradient has a nonzero block unavailable to any other coincident-pair gradient because triple coincidences are excluded. This independently identifies the exact normal bundle used in the determinant calculation.

For every unordered pair \(ij\), fix positions \(v_i=v_j=(0,0)\), \(v_k=(1,0)\), and \(v_l=(0,1)\). The three fixed lines joining the three distinct positions form a nondegenerate triangle; the remaining free line passes through the double vertex and can rotate through all projective angles. Along its rotation the respective tautological normal line is the Möbius bundle, while the other five normal lines are trivial. The resulting six-by-six mod-two evaluation matrix is exactly the identity, independent of any numerical approximation. Its row sums give orientation evaluation one along every collision loop.

Connectedness of the orientation-preserving similarity group implies it preserves the orientation on the ambient product and on its own adjoint representation. This verifies that the upstairs determinant identity descends to the quotient rather than assuming injectivity of pullback in degree one.

No independent audit or external validation has been performed. The argument does not compute the full cohomology of the quotient or assert the same formula for the reflection-containing similarity group.
