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

# Verification record

Both programs were executed with the Python standard library. Reproduction commands, from a directory containing these files:

```sh
python verify_steiner.py
python verify_invariant.py
```

Actual output of `verify_steiner.py`:

```text
DESIGNS PASS: 15 points, 35 blocks, 105 pairs exactly once each
PASCH PASS: 420/420 noncollinear triples in projective design; 0/420 in Bose design
ANCHORS 0 PASS: all choices tested on both designs
ANCHORS 1 PASS: all choices tested on both designs
ANCHORS 2 PASS: all choices tested on both designs
COLLINEAR THREE PASS: no separation through six rounds
RANK PASS: refinement profiles agree at rounds 0,1,2; first differ at round 3
CERTIFICATE PASS
```

Actual output of `verify_invariant.py`:

```text
FOUR-BLOCK PASCH PASS: projective=105, Bose=0
UNIFORM EQUITABLE PASS: 1 collinear mark(s), all choices in both systems
UNIFORM EQUITABLE PASS: 2 collinear mark(s), all choices in both systems
UNIFORM EQUITABLE PASS: 3 collinear mark(s), all choices in both systems
INDEPENDENT CERTIFICATE PASS
```

The second checker independently enumerates all \(\binom{35}{4}=52360\) four-block subsets in each fifteen-point system. The first checker evaluates all 455 point triples in each design; the programs use different definitions of Pasch occurrence. Both independently verify that all 105 unordered point pairs occur exactly once.

**Logical checks.** The proof reconstructs one equitable cell system for all nontrivial Steiner \(2\)-designs with collinear landmarks. The rank-four sentence is expressed using only two recycled variable symbols. The quantified limitation is that the lower rank bound was established for the projective/Bose pair with three noncollinear marks and not for arbitrary designs. Program signatures check up to six refinement rounds, and do not themselves establish all-order equivalence; the equitable-partition argument does.

**Source and priority limits.** The full primary arXiv papers on \(C^2\) identification and colour refinement were materially inspected for the general background. Relevant anti-Pasch construction material was available only as a publisher abstract and bibliographic record in this verification; its complete paper was not inspected. The present certificate is a self-review, not independent mathematical verification.
