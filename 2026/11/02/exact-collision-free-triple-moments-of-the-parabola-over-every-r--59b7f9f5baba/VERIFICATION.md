---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS. Over F_p, p>=5, centered variables a=3x-s,b=3y-s give Q=a^2+ab+b^2=3(3w-s^2)/2. Classical split/nonsplit quadratic-form counts and exclusion of the three collision lines give c_p(s,w). For p=3 only six permutations of (0,1,2) contribute at (0,2); p=2 gives zero. The two-row moment Jacobian [1,1,1;2x,2y,2z] has rank 2 mod p for unit-distinct triples, yielding exactly p lifts per prime-power step; CRT multiplies counts. Positivity in p=5,7,11 and all p>=13 establishes stated support proportions and full-support iff every p|m is >=13 and =1 mod3. Independently enumerated each ordered triple and every target for moduli 3,5,7,9,11,13,15,25,49; all per-target counts agree with the formula.

## originality

PASS

Best-knowledge PASS for full pair-of-moments fiber and local-to-composite support criterion. Classic conic solution counts are acknowledged ingredients. Hou–Sun 2002 Theorem 1.1 gives single-coordinate restricted sums with general avoidance, and Mockenhaupt–Tao 2004 provide paraboloid restriction/convolution estimates, neither the simultaneous two-moment collision-free ring fibers.

## value

PASS

PASS. A natural complete fiber and support classification for a structured additive triple convolution; small-prime obstructions and the exact coverage threshold for p≡1 mod3 are precise features of mathematical utility. The all-modulus statement is not a recomputation of an already-known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
