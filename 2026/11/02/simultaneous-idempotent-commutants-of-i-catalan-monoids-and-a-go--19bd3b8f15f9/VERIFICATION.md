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

PASS: For an extensive injective partial map, f^2=f iff f is a partial identity. Commutation of f with e_B is equivalent to B being invariant across every strict arrow i->f(i); the increasing partial-injection graph is disjoint directed paths, with n-r(f) components and c_E(f)=2^(n-r(f)). Rank-r strict injections enumerate by ballot/reflection as Narayana 1/m binom(m,r)binom(m,r+1), and fixed-point gap insertion gives S=1+zS(1-u+uS), F=S/(1-zS). Hence all k-fold idempotent tuple counts equal 2^(kn)F_n(2^-k). Analytic positive root z=(1-u)/(2-u) enters the physical sheet iff u<(3-sqrt5)/2, and meets the branch singularity at equality; standard transfer produces three stated asymptotic regimes. Independent n<=5 direct element enumeration+commutation and F4 checks passed; this does not alone prove the asymptotic.

## originality

PASS

The k=1 pair-count sequence and asymptotic coincide exactly with known OEIS A225887 and cannot be claimed original. Narayana enumerators, Catalan cardinality, and weighted path machinery are classical. The idempotent relative-centralizer *spectrum* and joint k>=2 counts/phase transition were not identified as stated or immediately implied in inspected same-monoid or OEIS literature. Best-of-knowledge with explicit alternate weighted-path risk.

## value

PASS

PASS: The count c_E(f) is a canonical algebraic centralization invariant of a natural finite Catalan monoid. Its entire spectrum and the probability that an element centralizes k independently chosen idempotents are exact natural questions, not arbitrary numerical slices. The golden-ratio analytic transition sharply separates k=1 from all k>=2 and is not determined by the known k=1 sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
