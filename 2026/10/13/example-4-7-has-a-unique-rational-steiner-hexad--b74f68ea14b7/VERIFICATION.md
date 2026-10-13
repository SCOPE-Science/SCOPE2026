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
The attached `verify.py` is an exact exhaustive certificate for the finite-group step in the claim.

It verifies the following facts without floating-point arithmetic:

- the quadratic model has exactly \(28\) odd theta characteristics;
- the \(63\) nonzero vectors of \(\mathbb F_2^6\) yield \(63\) distinct twelve-element Steiner hexads;
- the stabilizer of the distinguished nonzero class has order \(23040\) and acts faithfully on the twelve members of its hexad;
- the displayed generators of 12T31 generate a group of order \(48\) and have exactly one invariant partition into six pairs;
- the corresponding lifts generate a group of order \(48\) on the \(28\) odd theta characteristics, with orbit sizes \(12,16\);
- the induced action on the \(63\) nonzero two-torsion classes has orbit sizes \(1,6,16,16,24\);
- the distinguished class is the only common nonzero fixed vector.

A successful replay prints:
`VERIFY_OK Uv=23040 H=48 bitangent_orbits=12+16 torsion_orbits=1+6+16+16+24 rational_2torsion=2 unique_steiner=true`

The certificate does not independently establish the source's geometric identification of the Example 4.7 bitangent Galois action with 12T31 or its conjugacy statement for the two sign choices; those are literature inputs. It verifies the new finite implication from that input to the claimed rational two-torsion subgroup and orbit profile.
