---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Reconstructed from original RESULT.md Git blob 2231ded6...: writing n=p^a q^b, p<q, rad(n)^2|sigma(n) is exactly p^2|sigma(q^b) and q^2|sigma(p^a). Since sigma(p)=p+1<q^2 and sigma(p^2)=p^2+p+1<q^2, a>=3. For a+b<=5 the complete possible exponent pairs are (3,1),(3,2),(4,1). For (3,2), q cannot divide p+1; then q^2 divides p^2+1<q^2 for odd p, impossible; p=2 gives sigma(8)=15, without odd prime-square divisors. For (3,1), p^2|q+1 implies q>=p^2-1; for p>=3, (p^2-1)^2-sigma(p^3)=p(p^3-p^2-3p-1)>0, checked as positive-coefficient polynomial after p=t+3. p=2 cannot give q^2|15. For (4,1), q+1=kp^2. If k>=2, q^2>=(2p^2-1)^2>sigma(p^4), with the last difference 3p^4-p^3-5p^2-p positive after p=t+2. Thus k=1 and q=p^2-1, composite for odd p; p=2 gives q=3 and 9∤31. Finally sigma(96)=252, rad(96)^2=36, 252/36=7, Omega=6. No other exponent case is omitted.

## originality

PASS

The exact predicate and the witness 96 predate the submission: the 2012 source studies gamma(n)^2|sigma(n) in its final remarks, and OEIS A173615 tabulates the same predicate. The claimed new part is the uniform unbounded exclusion of all p^a q^b, p<q, with a+b<=5, not the predicate, the example 96, or the fixed {2,3} characterization. The two accessible relevant primary texts and OEIS entry were compared at the level of hypotheses and implications; none of the inspected statements establishes the all-prime-pair exponent cutoff. This is a best-of-knowledge assessment, not certification of priority.

## value

PASS

The precise first Omega layer is a motivated structural invariant of the two-prime-support component of the reverse core-square divisor-sum problem explicitly considered by Broughan et al. and tabulated in OEIS A173615. A magnitude-ordered table showing 96 first cannot preclude arbitrarily large p^a q^b of smaller total exponent. The theorem gives a uniform cross-support obstruction and proves the exact optimal total multiplicity 6. Its contribution is modest and elementary, but supplies a size-independent cutoff a future classification or search over all prime pairs can rely on; it is neither an arbitrary slice nor a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
