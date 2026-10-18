---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For one prime p^a, equality forces a=2. At >=2 distinct primes, if all a_p<=2 then sum p^{a_p}< (sum p)^2, so some exponent >=3. Omega<=5 leaves precisely (3,1,1), (3,2), (3,1), (4,1) (after ordering p<q) with the larger prime exponent <=2, since q^3>(p+q)^2. Each is eliminated by the displayed modular factorizations: t(t-1)=0 mod p in the three-prime case, q=p(p-1)/2 in (3,2), and p^{a-2}=(kp-1)^2+k for (a,1). The explicit 144=2^4 3^2 has B=25=(2+3)^2 and Omega=6. Direct independent enumeration n<=100000 agrees; proof handles all n.

## originality

PASS

Best-of-knowledge PASS. Primary De Koninck--Luca paper presents this exact equation and proves asymptotic density bounds but not the first five Omega layers; the new complete finite multiplicity exclusion is not a consequence of those counts.

## value

PASS

A sharp natural structural cutoff in a studied Diophantine family: it distinguishes trivial prime-square solutions from the first genuinely mixed-support solution, and gives a complete classification for all Omega<=5 without size bounds. Useful as an exact baseline for future parametrization and searches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
