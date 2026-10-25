---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The final claim assumes r_n=n^{alpha+o(1)}, m_n=n^{beta+o(1)}, alpha,beta>0, fixed p in (0,1) and independence of entries INSIDE each matrix, without cross-index independence. For k=floor((1-epsilon)log r/lambda), every k-attribute subset has Bin(r,p^k) support, mean at least r^epsilon. Conditional independence of outside columns gives closure-failure <=exp(-r^epsilon/8)+m exp(-lambda r^epsilon/2); union over m^k=exp(O(log^2 n)) makes failures summable. The lower bound log binom(m,k)~(1-epsilon)log r log m/lambda follows. A concept with extent >=A=ceil((1+epsilon)log m/lambda) and intent >=B=ceil((1+epsilon)log r/lambda) induces a distinct all-one rectangle. Its first-moment sum is <=rm exp(A log r+B log m-lambda AB), with high-high exponent <=(1-epsilon^2)log r log m/lambda+O(log n); Markov plus Borel-Cantelli and smaller-side deterministic counts prove the upper a.s. and expectation bounds. The argument needs no independence across n. Independently computed all incidence matrices at p=1/2 for 2x2,3x3,4x4, obtaining expectations 39/16,1977/512,386463/65536; these are checks, not a substitute for the universal argument.

## originality

PASS

The almost-sure SHARP exponent and simultaneous closure of ALL logarithmically subcritical intents are not supplied by the inspected expected-value literature. Known exact means and lower bounds are acknowledged; an unindexed random maximal-biclique theorem remains possible.

## value

PASS

This establishes the typical logarithmic output-size scale in a standard random formal-context model and a simultaneous-intent structural theorem. The sharp exponent in polynomially rectangular regimes distinguishes typical from merely expected complexity. Both variables and the exact invariant are natural.

The dated certificate retains the supplied scientific assessment, sources and limitations.
