---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Under the cyclic encoding R=F2[z,z^-1]/(z^n-1), the exact update block is [[z+z^-1,1],[1,z^3+z^-3]] and determinant z^-4 Phi_5(z)^2. For n coprime to five determinant is a unit. Otherwise Phi_5 occurs to multiplicity e=2^nu2(n). At this factor the characteristic polynomial has two simple roots 0 and 1, which lift to complementary rank-one local summands; on the zero summand the eigenvalue is unit*Phi_5². Multiplication by Phi_5^(2t) has kernel degree 4min(2t,e); this gives the rank, primary Jordan blocks and eventual-periodic counts, not an extrapolation. Independent GF2 bit-vector matrices constructed from labelled graph edges checked all t=0..7 for every 7<=n<=50 (352 exact rank checks) plus all 44 fixed dimensions, agreeing with det(B+I)=z^-4(z+1)^4Phi_5. The general proof uses CRT/local factorization; the bounded checks do not prove it.

## originality

PASS

Best-of-knowledge originality of the exact final combined claim, after reviewing primary statements and Resultary hits; credited known partial antecedents. Gera–Stănică gives the same graph adjacency blocks but over the real/complex spectral setting; the characteristic-two Jordan nilpotent part and exact periodic-state entrances are not determined by ordinary real eigenvalue multiplicities. Zaidenberg treats linear prime-characteristic convolution on lattices and provides a general harmonic framework, but no inspected result specifies the GP(n,3) squared fifth-cyclotomic factor, exact valuation-two nilpotent chain or entry-time population. Gera–Stănică Theorem 2.4 gives real eigenvalue quadratic equations for GP(n,k), not the modular Jordan filtration. Real adjacency spectra and the general convolution setup allow the 2x2 reduction but do not alone imply the characteristic-2 Phi_5² valuation or dyadic index ceiling(e/2). Those local computations are the differentiating mathematical steps.

## value

PASS

For the classical GP(n,3) graph family, the exact GF2 periodization and rank-loss clock has sharp dependence on the 2-adic valuation of n and the 5-divisibility obstruction. This is a nontrivial natural family-wide classification of transient populations, not merely a numerical rank list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
