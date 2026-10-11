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
# Verification

`verify.py` contains the complete 24-facet presentation and uses only Python's standard library.

It checks the face vector \((9,36,24)\), verifies that every edge has degree two and that the one-skeleton is complete, row-reduces the mod-two triangle-boundary space to rank \(23\), and obtains \(\dim H_1=5\).

It then enumerates every unoriented simple cycle of length \(3,4,5,6\): respectively \(84,378,1512,5040\) cycles. Reduction modulo the exact boundary space gives all \(31\) nonzero homology classes and verifies every minimum length and shortest-representative multiplicity.

All \(9!\) vertex permutations are tested against the facet set. Exactly \(18\) are automorphisms, and their action gives the seven stated class orbits.

Finally, increasingly oriented facets are summed integrally. The verifier checks that their boundary has coefficients \(-2,0,2\), divides it by two, verifies the result is an integral one-cycle, and checks that its mod-two class is the unique length-six class with \(66\) shortest representatives and a singleton automorphism orbit.

Exact successful output:

`VERIFY_OK f=9,36,24 H1_F2_dim=5 nonzero_classes=31 min_lengths=3:24,4:3,5:3,6:1 triangular_multiplicities=1:3,2:9,3:9,4:3 length4_multiplicity=6x3 length5_multiplicity=18x3 length6_multiplicity=66x1 missing3=60 essential3=60 aut=18 class_orbits=1:6:66|3:3:1|3:3:4|3:4:6|3:5:18|9:3:2|9:3:3 bockstein_length=6 bockstein_minimizers=66 bockstein_fixed=yes`

The checker proves the finite combinatorial statements. Identification of the nonzero order-two cycle as the unique integral torsion generator also uses the published integral homology group \(\mathbb Z^4\oplus\mathbb Z/2\).
