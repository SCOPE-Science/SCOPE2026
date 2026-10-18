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
# Reproducibility and verification

The theorem is deductive. Reconstruct it from the explicit frame in `RESULT.md` and check the following quantified invariants:

1. For every oracle \(X\), every index \(e\), and every stage \(t\), first halting at stage \(t\) is a finite computation relative to \(X\); at most one \(t\) meets it.
2. Every row includes exactly the \(k\) base worlds. Only an \(s_e\)-row can have extras; if its program halts, the row has exactly \(\ell-k\) extras. Thus each row has degree either \(k\) or \(\ell\), including when \(k=0\).
3. Under the given atomic assignment, the only successors falsifying \(p\) are the possible extras. Thus at every \(s_e\), \(\neg\Box p\) is equivalent to relative halting.
4. For the upper direction, \(X'\) decides the finitely many \(\Sigma^0_1(X)\) successor-existence questions at each world; recursive evaluation of the formula syntax therefore terminates and computes the full valuation.
5. If the allowed degree is exactly \(k\), the number of successors is known, so all search and recursion are already computable in \(X\), formalizable in \(\mathrm{RCA}_0\).
6. Every model of \(\mathrm{VEL}(S)\) supplies a set coding the graph of the valuation. Extracting the \(s_e\)-section yields \(X'\) by recursive comprehension; for all \(X\), this is \(\mathrm{ACA}_0\).

A computer enumeration of finitely many worlds cannot certify the infinite reversal, so no experimental result is claimed. Independent audit has not been performed. Mathematical priority risk: an older generic degree-padding theorem may subsume the classification.
