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

The theorem itself is checked by a source-to-proof dependency chain rather than by finite computation:

1. Barbina--Casanovas prove quantifier elimination for \(T^*_{\mathrm{Sq}}\).
2. Their Fraïssé limit \(M_F\) is locally finite, and Proposition 4.4 proves it is prime by isolating every tuple type realized there.
3. Corollary 5.5 states \(\operatorname{acl}(A)=\langle A\rangle\).
4. Theorem 3.3 constructs \(2^{\aleph_0}\) distinct three-variable types from countably infinite three-generated Steiner quasigroups.

The bundled `verify_steiner_isolated_types.py` independently checks the elementary finite closure facts used in the arity corollary. It exhaustively enumerates all \(19,683\) binary operations on three labeled points, verifies uniqueness of the three-element Steiner quasigroup, checks every one- and two-generator closure, and checks the seven-point Fano example including a three-generator closure of size seven.

A successful replay prints:

`VERIFY_OK 165 exact assertions`

The executable check does not prove quantifier elimination, primeness, local finiteness of the generic, or the continuum family; those are cited source theorems. It does not assess literature priority.
