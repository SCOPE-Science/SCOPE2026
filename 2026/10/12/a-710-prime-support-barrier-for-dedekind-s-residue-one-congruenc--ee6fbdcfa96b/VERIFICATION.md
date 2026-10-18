---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Prime-power factors p^a, a>=2 make p divide psi(n), violating residue one; an even squarefree composite also contradicts parity. For any remaining odd squarefree composite n, (psi(n)-1)/n is an odd integer >=3, hence psi(n)/n>3. The pairwise obstruction q=-1 mod r forces support primes into one of fifteen explicitly compatible intersections S of B={3,5,7,11,13}. The t smallest eligible primes dominate the Euler factors of any t-element support. Exact integer products of the first 709 eligible primes for all fifteen S are <3; independently reproduced the prime sieve and rational comparisons, including maximum S={11,13}, ratio approximately 2.99970965505, q_709=6661 and the 710th q=6673. This establishes all n without size cutoff; a scan through n<=100000 is not the unbounded proof.

## originality

PASS

The exact OEIS residue-one conjecture is public, and the squarefree reduction equates this equation to the sigma(n) residue-one equation, but the inspected database entries give no quantified 710-prime-support bound. The closest Resultary support-sieve records handle distinct arithmetic predicates. The Alzer–Kwong source studies multiplicative analytic inequalities; only its abstract, not its complete PDF, was read this run. Best-of-knowledge distinctive quantified local-residue plus abundancy exclusion survives.

## value

PASS

A 710-prime-support necessary condition addresses an explicit natural open congruence primality criterion, not an arbitrary finite cutoff. The fifteen-branch rational certificate plus an unbounded domination argument yields information no finite n-range search could establish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
