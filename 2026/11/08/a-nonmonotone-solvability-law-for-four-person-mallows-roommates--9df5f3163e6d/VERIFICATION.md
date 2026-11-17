---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The four-person strict complete matching problem has exactly three perfect matchings. The assigned verifier enumerates all 6^4=1296 reduced preference profiles and finds 48 unsolvable in two disjoint 24-profile relabeling orbits. Independent audit implemented an entirely separate direct enumeration over all 24^4=331,776 quadruples of complete Mallows four-name rankings, deleting each agent’s own name and directly checking all four candidate blocking pairs per matching. The total unsolvable numerator coefficients at powers 0..24 are [0,0,3,22,82,208,404,642,870,1038,1129,1162,1168,1162,1129,1038,870,642,404,208,82,22,3,0,0], sum 12288. Exact SymPy cancellation reproduces the submitted rational function over Z_4(q)^4; derivative factorization 2q(1−q)H(q)/positive denominator checked algebraically. H is reciprocal degree12 with two positive-root sign variations, H(0)>0,H(1)<0 and exact H(379/1000)>0>H(380/1000), so it has precisely one interior zero and global maximum; endpoint q=1 gives 1/27 and small q onset 3q². This is an exhaustive finite proof of the four-person model, not partial sampling.

## originality

PASS

PASS best-of-knowledge: published four-person stable-roommates orbit census already reports two unsolvable 24-sized relabeling classes and 48 bad profiles, and the impartial-culture 1/27 endpoint is standard; neither gives the rational full-order Mallows q-law nor unique interior maximum. The exact synthetic culture is specified by Boehmer–Heeger–Szufa, but their 200-agent sample experiments do not derive this four-person probability. Uniform large-n asymptotics by Chin–Michelen and Young–Studebaker concern q=1, not q∈[0,1].

## value

PASS

PASS: nonmonotonic unsolvability under increased randomness is an interpretable and sharp counterexample to monotone-noise intuition at the smallest size with possible stable-roommates failure. The exact peak q≈0.379464 and two-inversion threshold identify a natural phase/parameter phenomenon, not merely the known 48-profile census reweighted with no mathematical message.

The dated certificate retains the supplied scientific assessment, sources and limitations.
