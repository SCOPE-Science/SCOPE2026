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

The standalone pure-Python verifier `verify_bh_picard.py` was executed for \(q=2,3,5\). It enumerated all \(6,24,120\) projective fractional-linear maps and the respective \(1,3,10\) conjugate node-pairs, finding one orbit in every case. The unordered-pair stabilizers had orders \(6,8,12\), and in each stabilizer exactly half of the elements exchanged branches. The signed characters had zero average; for \(q=5\), their squared character norm was \(2\). The complete signed-character values by element order were respectively \(10,-2,1,0,0,1\) for orders \(1,2,3,4,5,6\), with class-size totals \(1,25,20,30,24,20\); these agree with the stated sum of Specht characters.

These checks corroborate the geometric group-action description and detect a nontrivial sign character. The unrestricted theorem is proved by the general nonsplit-torus normalizer argument and integral coinvariants, not extrapolation from finite field samples. The Specht constituents are established by the abstract \(\mathfrak S_5\) identification and Pieri rule, not inferred solely from the character-norm test. No third-party scientific validation is asserted.
