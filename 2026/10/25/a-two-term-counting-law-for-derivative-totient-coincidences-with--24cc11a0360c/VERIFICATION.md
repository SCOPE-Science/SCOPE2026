---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For fixed odd prime p, the equality D(p^a q^b)=phi(p^a q^b) reduces exactly to aq+bp=(p-1)(q-1). The exponents require t=p-1-a in 1..p-2, q in one reduced residue class tq=-1 mod p and b=(tq-(p-1))/p. These classes are disjoint, and p=2 has none. Logarithmic size equals (t/p)*q log q -(p-1)/p*log q+constant; its cutoff differs by O_p(1) from Q=(p/t)L/W((p/t)L), L=log X. Fixed-modulus prime number theorem in progressions supplies Li(Q)/(p-1) with errors smaller than the prescribed inverse log powers. Expand W(cL)=ell+log c-log ell+O_p(log ell/ell) and Li(Q) to obtain pL/[(p-1)ell^2] times [H_p+((2 log ell+1)H_p-2J_p)/ell+O_p((log ell)^2/ell^2)], where ell=log L. Independent brute arithmetic verified 180 distinct small-prime Diophantine pairs and unique exponent criterion. No finite enumeration is used to infer PNT or the asymptotic.

## originality

PASS

The integer arithmetic derivative and exact two-prime Diophantine existence are established prior work, including Robert Israel’s August 21 2014 OEIS A166374 comment. The claimed new content is the fixed-p counting asymptotic with a full explicit two-term harmonic constant. The construction is a classical application of PNT in fixed progressions and Lambert W inversion, but the existing cited sequence/comment and primary basic derivative text do not already state that distribution. Resultary fixed-multiplier D(n)=kn and cototient-gap studies have different equations and cannot directly imply it. Some specialized arithmetic-derivative counting sources may have equivalent formulas that were not indexed.

## value

PASS

The fixed-prime layer of a classical arithmetic-derivative/totient coincidence is a naturally defined infinite Diophantine set. Its precise quantitative density with explicit secondary logloglog term and harmonic constants is new information beyond an old existence/parametrization argument, though the analytic ingredients are standard. It is a complete answer within an exact two-prime support slice, rather than arbitrary numerical instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
