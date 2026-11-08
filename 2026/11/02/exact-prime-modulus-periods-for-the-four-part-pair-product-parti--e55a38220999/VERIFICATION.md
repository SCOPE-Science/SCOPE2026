---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Checked unique four-part gap parametrization, weighted quadratic E and geometric-moment generating-function algebra; independent direct enumeration agreed with coefficients for 52 terms n=4..55. The numerator P has residues 864,32,6,-12 modulo Phi1,Phi2,Phi3,Phi4, all units mod p>=5, so rational GF is reduced in F_p(q). Any eventual period T must have H dividing 1-q^T. Primitive orders 3,4 give 12|T; multiplicity 6 at q=1 forces p^{v_p(T)}>=6, hence 300 at p=5 and 12p for p>=7. Frobenius proves H|1-q^T at those T. Since deg(q^4P)+T-deg(H)=T-6<T, initial coefficients are periodic starting at n=0. Independent recurrence and exact modular comparisons checked primes 5,7,11 for >2 full periods. Thus finite checks supplement the all-prime divisibility proof.

## originality

PASS

Ballantine–Beck–Merca 2025 open-access full article explicitly displays numerical period table (300,84,132 etc) as conjectural, proves congruences modulo 2,3,4, and does not prove exact minimum for all primes >=5. Nijenhuis–Wilf and Kwong give general techniques for *unweighted* restricted partition counts; their theorem statements cannot be substituted for this weighted quadratic statistic without establishing its reduced denominator. Best-of-knowledge O PASS for new proof and uniform prime classification, not for the already conjectured table values.

## value

PASS

Solves the explicit prime-period conjecture for a natural weighted four-part partition count, determines the full infinite-prime family and distinguishes pure and eventual periodicity; exceptional p=5 has a structural explanation via pole order six.

The dated certificate retains the supplied scientific assessment, sources and limitations.
