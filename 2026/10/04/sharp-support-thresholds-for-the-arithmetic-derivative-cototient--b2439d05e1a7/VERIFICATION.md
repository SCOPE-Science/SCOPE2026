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

The radical identity \(G(n)/n=G(\operatorname{rad}n)/\operatorname{rad}n+\sum_{p\mid n}(e_p-1)/p\) follows directly from the factorized arithmetic derivative and Euler product. For prime powers it gives \(G(p^e)=(e-1)p^{e-1}\), with minimum two only at \(4\). For two-prime support \(p^a q^b\), direct expansion gives \(G=p^{a-1}q^{b-1}[(a-1)q+(b-1)p+1]\), so the nonsquarefree minimum is eight only at \(12\). For a squarefree triple \(pqr\), \(G=p+q+r-1\ge9\) with equality only at \(30\); adding further squarefree primes strictly increases \(G\), while repeated exponents add a strictly positive radical term. These support bounds make the listed fibers through nine exhaustive. An independent enumeration through \(20000\) reproduced all stated minima and fibers; the proof is unrestricted.

## originality

PASS

OEIS A344178 is exactly \(G(n)=D(n)-(n-\varphi(n))\). Its current entry proves nonnegativity and records the complete fibers \(G=0\) and \(G=1\), while its data visibly contains the early values but does not prove that no later integer enters fibers two through nine. The audited support inequalities supply that missing global exclusion and therefore turn the observed initial table into a complete spectrum through nine. Resultary returned only the assigned same-object theorem, and the inspected arithmetic-derivative literature does not discuss this cototient difference.

## value

PASS

The function is a canonical recorded combination of the arithmetic derivative and cototient. Support-stratified sharp minima are natural inverse-value invariants, and the theorem gives the first complete nontrivial fiber spectrum rather than merely recomputing a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
