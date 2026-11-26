---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

After dividing by the gcd (which also divides the hypotenuse), Euclid parametrization writes the odd leg as uv with coprime odd u,v and the even leg as (u+v)(u-v)/2. I checked the exhaustion: for a lone odd prime in uv one of u,v is 1; the odd parts of u−1 and u+1 are coprime, and the mod-8 valuations and even-exponent factorization give uv=3,9 or 5. If both 3 and 5 divide uv, the even leg is a power of two, so u−v=2; the joint allocation u=uv,v=1 would force uv=3, while the separate allocation requires powers of 3 and 5 of the form 2^t±1. Parity of t modulo 3 and factoring the even exponent (in 2^t or in 3^r) leave 3 and 5 only. The four primitive pairs therefore give exactly the four stated displacement directions. Selecting a=0,1 mod 5 is independent. On the padded torus every wrapped displacement in a coordinate needs a difference at least the original side length, so cannot join two occupied box vertices. For A≥2 the five template vertices remain distinct by their first coordinates; every translate has at most two selected vertices and each occupied vertex is counted five times. This proves the floored upper bound, and dividing both bounds by ABC gives the joint limit as all three side lengths grow. Independent bounded replay: python3 /workspace/branches/independent_replays.py, function pythagorean, found the four coprime pairs among 240 smooth numbers and checked that the template is an induced 5-cycle of independence number two. Neither finite replay nor the theorem determines arbitrary finite box optima.

## originality

PASS

The supported distinction is the sharp fixed-three-prime density and its finite bounds, not the prime-box problem or the general tiling/averaging method. No checked statement supplies this result; the closest two-prime Resultary record is same-day and has different mathematical scope, not established chronological priority.

## value

PASS

The first three primes give a natural fixed-support comparison to the growing-prime problem and the two-prime path case. A new odd cycle changes the extremal density from the path regime, and the same classification gives explicit effective rectangular bounds and a reusable list of forbidden primitive ratios. This is a resolved sharp asymptotic, not a numerical fit or a claim of all finite maximizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
