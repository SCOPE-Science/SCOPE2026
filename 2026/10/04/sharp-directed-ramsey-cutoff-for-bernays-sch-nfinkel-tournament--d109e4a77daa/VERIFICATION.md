---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Preserving all chosen existential witnesses, there are at most 2^k orientation profiles for remaining vertices. A model of size greater than k+(R_dir(ell)-1)2^k therefore contains a transitive ell-vertex tournament of one profile. Every assignment to at most ell universally quantified variables in a larger cloned transitive block has an equality- and arc-preserving injection into that block, preserving the quantifier-free matrix and yielding all orders n>=k+ell. Sharpness uses an R_dir(ell)-1-vertex transitive-ell-free tournament copied to every one of 2^k profiles, with a universal prohibition of ell distinct nonwitness profile-mates inducing a transitive tournament. This condition is quantifier-free after ell universals and finite conjunction/disjunction. Cases k=0 and ell=2 are included. Independent enumeration of 64 labeled four-vertex tournaments shows a transitive triple, and a three-cycle supplies R_dir(3)>=4. These finite checks only calibrate ell=3.

## originality

PASS

The directed version requires transitive order preserving tuple transfer and is not an implication of the sharp undirected-graph BSR cutoff; directed Ramsey numbers are different from graph Ramsey numbers. The Pikhurko–Verbitsky survey and the directed Ramsey primary source provide separate ingredients but no located theorem for the exact fixed-prefix tournament finite-spectrum endpoint or its attainable construction. A short folklore adaptation is plausible and remains a residual risk.

## value

PASS

The exact best possible finite-spectrum ceiling across a natural first-order fragment restricted to tournaments is a meaningful logical classification: it determines all sufficiently large model sizes and gives a matching sentence for every k,ell. It is more than recording a small directed Ramsey value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
