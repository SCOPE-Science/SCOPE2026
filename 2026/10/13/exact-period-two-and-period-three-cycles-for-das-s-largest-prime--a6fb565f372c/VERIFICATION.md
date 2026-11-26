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

A composite always goes to a smaller prime, and a prime increases by k>0. In a two-cycle there is one prime p, and return requires P(p+k)=p. This gives p|k; conversely p+k=p(1+k/p) is composite and has largest prime p precisely when 1+k/p has no prime factor larger than p. The largest-prime-factor notation on this cofactor has its usual meaning for prime as well as composite inputs. Distinct p give distinct cycles. In a three-cycle there must be exactly one composite (two composites cannot be adjacent cyclically, and all-prime steps strictly increase). Rotate to p, p+k, p+2k, ending at the return to p. Then p|2k, and odd p would divide the strictly larger prime p+k, so p=2. The return requires 2(k+1) to be a power of two; the intervening integer 2^a+1 must be prime. These conditions suffice, and the three points are distinct, including k=1. A nontrivial odd factor of a would give a proper sum-of-odd-powers divisor of 2^a+1. Thus a is a power of two; no assertion about which Fermat numbers beyond known examples are prime is needed. Independently sieving largest prime factors up to 6500, composing the map twice and three times for 1<=k<=500 and 2<=n<=5000, and keeping only the smallest point of each exact cycle gave zero mismatches, 495 two-cycles in total, and three-cycle parameters 1,3,15,255. This bounded check corroborates, but does not replace, the proof.

## originality

PASS

The supported distinct claim is the complete two- and three-cycle classification, not the definition, general periodicity, isolated examples, or the classical factorization of Fermat numbers. The strongest exact indexed overlap is in a later-dated record; no evidence found makes it prior coverage. The checked earlier statements provide only ingredients and examples.

## value

PASS

The short exact periods are natural invariants of Das's map. The result turns isolated period-three examples into a restriction to Fermat-prime parameters with one orbit at each admissible parameter, and gives an exact count for period two. The complete converse and the exclusion of all other parameters supply useful information even though the proof is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
