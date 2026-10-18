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

# Reproducibility and scope

Run `python3 verify.py` with standard Python 3. The standalone script constructs Euler's totient values by trial factorization and by an independent integer sieve. It compares the complete map \(F(n)=\varphi(n)+3\) on \(1\) through \(25\), validates both cases of the arithmetic descent mechanism for \(26\le n<5000\), and follows all one million starting values to their periodic terminal components. It identifies exactly the cycles \((9)\), \((11,13,15)\), and \((23,25)\), with maximum finite-range preperiod \(46\).

The mathematical proof is in `RESULT.md`, Steps 1–5. The only infinite argument is elementary: the least-prime-factor bound gives \(m-\varphi(m)\ge\sqrt m\) for composites, and the prime case splits according to primality of \(p+2\), using divisibility by \(3\) if necessary. The computed tests are useful independent cross-checks but do not establish that every positive integer eventually descends. No external computation or independent mathematical audit has been performed.
