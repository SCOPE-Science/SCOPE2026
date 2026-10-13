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
# Verification

The proof is symbolic; there is no finite enumeration standing in for an infinite assertion.

1. **Polynomial part versus finite support.** If \(\iota(f)\in D\), then any nonzero value \(f(p)\) would repeat on infinitely many coordinates \((p,j)\), contradicting finite support. Hence \(f\) vanishes on all of the Zariski-dense set \(X\), so \(f=0\). Therefore \(R/D\cong k[x,y,z]\).
2. **Primes containing \(D\).** Quotient correspondence gives precisely \(D+\iota(\mathfrak p)\) for \(\mathfrak p\in\operatorname{Spec}k[x,y,z]\).
3. **Primes avoiding \(D\).** The coordinate idempotents are pairwise orthogonal. A prime avoiding \(D\) must omit one and only one \(\delta_\omega\). Then \(1-\delta_\omega\) belongs to the prime, which forces every function vanishing at \(\omega\) into it. Surjective evaluation shows the resulting kernel is maximal, so the prime is exactly \(M_\omega\).
4. **Minimality and dimension.** Coordinate primes are incomparable with the quotient component and have no smaller primes; \(D\) is the zero-prime pullback from the domain quotient. All nontrivial chains therefore lie in \(V(D)\cong\operatorname{Spec}k[x,y,z]\), giving dimension \(3\).
5. **Idempotents.** For \(e=\iota(f)+d\), infinitely many untouched coordinates in every fiber give \(f(p)^2=f(p)\) for every \(p\in X\). Density yields \(f(f-1)=0\) in the domain \(k[x,y,z]\), hence \(f=0\) or \(1\). Coordinatewise idempotence then gives exactly \(\chi_F\) or \(1-\chi_F\) with \(F\) finite.

The argument does not determine spectra for arbitrary function rings \(\Delta B+D\); it uses the polynomial quotient and Zariski density of this example. No independent audit has been performed.
