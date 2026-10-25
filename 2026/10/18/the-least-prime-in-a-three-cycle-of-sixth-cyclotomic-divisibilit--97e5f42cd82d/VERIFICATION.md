---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS. Rotate any three-cycle to its unique smallest vertex p<=349. Every outgoing q is a prime divisor of F(p)=p^2-p+1 and every subsequent r a prime divisor of F(q), so two-stage complete factorization exhausts the infinite condition without upper bounds on q,r. Independent SymPy enumeration recovered exactly 70 candidate p->q->r paths and exactly one closing cycle (349,121453,9710803); primality/divisibilities and H(pqr)=F(p)F(q)F(r)/(pqr)=410433300314317 verified exactly. No stronger claim for p>349.

## originality

PASS

PASS best of knowledge. Earlier De Koninck–Letendre gives the reciprocal-gcd multiplicative identity and introduces prime-factor cycles, while the OEIS small values and Resultary Phi_3 prime-pair classification do not imply this Phi_6 three-vertex least-prime cutoff. The closely related global least-product result is a different optimization: knowing a minimum product does not exclude a smaller cycle vertex at much larger product. Full primary text of the newly posted preprint was unavailable and remains a genuine priority risk.

## value

PASS

PASS. The 3-cycle is the smallest nontrivial feedback pattern after the excluded 2-cycle, arising directly in the natural reciprocal-gcd integrality construction. Its sharp least starting prime and explicit first witness answer a motivated arithmetic minimality question; it is not arbitrary finite sampling or a general infinitude claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
