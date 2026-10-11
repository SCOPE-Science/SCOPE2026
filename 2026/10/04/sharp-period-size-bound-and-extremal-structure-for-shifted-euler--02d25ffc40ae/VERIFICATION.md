---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The cototient identity \(c(x_i)=x_i-x_{i+1}+k\) telescopes to \(\sum_i c(x_i)=Tk\). Every cycle term is at least two, hence contributes at least one; a maximal term cannot be prime, and for composite \(M\) with least prime divisor \(p\le\sqrt M\), \(c(M)\ge M/p\ge\sqrt M\). Therefore \(\sqrt M\le Tk-(T-1)\). Equality forces all other cototients to be one and both composite inequalities to be equalities, hence \(M=q^2\) and every other term prime. Prime terms advance by exactly \(k-1\), and the return from \(q^2\) is equivalent to \(q=T(k-1)+1\). The inspected verifier independently checks the telescoping identity, bound, equality recognition and explicit periods 2, 3 and 4.

## originality

PASS

Leonetti--Luca's full open Cambridge article explicitly says that sharpness/nontrivial size information remains unanswered and proposes cycles made of primes in arithmetic progression except the last term. It does not state the period-sensitive square bound or prove that its suggested pattern is the unique equality case. The later Danh et al. paper concerns the separate two-step recurrence. Resultary returned no stronger published record.

## value

PASS

The result directly answers a sharpness direction explicitly highlighted by the source, gives a scale-free period-sensitive bound, and rigidly identifies every equality case. The period-size tradeoff is a natural dynamical invariant of this arithmetic map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
