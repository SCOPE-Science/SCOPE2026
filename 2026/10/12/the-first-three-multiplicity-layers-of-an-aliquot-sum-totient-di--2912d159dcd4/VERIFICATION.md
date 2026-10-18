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

The exhaustive multiplicity-shape partition p,p²,pq,p³,p²q,pqr covers Omega=1,2,3. For pq, positivity yields (p-2)(q-2)<=4, leaving 2*3 and 2*5 after the odd candidate 3*5 fails. For p²q, p=2 reduces q-1|10 and gives q=3,11; p=3 is bounded and excluded directly; p>=5 is excluded by q(p²-2p-1)<=2p²+1 and congruence mod p. All-odd squarefree pqr fail because sigma(n)-n is odd while phi(n) is even; if n=2qr then (q-1)(r-1)|4q+4r+2 bounds q in {3,5,7}, whose direct divisibility tests fail. Explicit sigma and phi quotient checks give 2,6,10,12,44 and sigma(90)-90=144=6 phi(90). A separate SPF-based exact calculation enumerating every n<=160000 with Omega<=3 found exactly these five. That finite test is corroborative only; factorization-shape proof is unbounded.

## originality

PASS

OEIS A066679 is exactly the full congruence sequence and already lists every claimed small integer, including subsequent 90,184,440,..., and a parametric large-term family. That listing alone does not prove every unlisted >44 solution has Omega>=4. Iannucci 2017, full 11-page primary text, addresses the strictly narrower quotient-one equation sigma(n)=n+phi(n), with necessary conditions including n odd square for hypothetical n>2; its hypotheses do not cover quotients 2,3,4,6 here. Resultary searches found no matching universal Omega<=3 theorem. The increment beyond known exact terms is only the unbounded multiplicity classification, not discovery of integer values or the sequence.

## value

PASS

Prime-factor multiplicity Omega is an intrinsic measure of arithmetic complexity and the first three layers form a complete natural structural slice of the established congruence sequence. A universal boundary at Omega=4 with sharp witness 90 is potentially useful when excluding low-complexity solutions and is stronger than the previously published bounded list; not an arbitrary numerical interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
