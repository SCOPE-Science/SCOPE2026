---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With cyclic subscripts the minor on rows i+j,j and columns j,0 gives x_i x_j = x_0 x_{i+j} for i,j nonzero; if a subscript is zero the relation is tautological. Conversely all minors equate products with the same subscript sum. In degree d>0 the resulting n normal forms x_0^(d−1)x_s have independent images t^d z^s in Z[t,z]/(z^n−1), so span and are independent integrally. In particular x_i^n=x_0^n covers Proj by D_+(x_0); degree-zero localization is exactly Z[z]/(z^n−1), which is finite free of rank n and gives the given morphism. Over an algebraically closed positive-characteristic field, factorization through (z^m−1)^(p^a) and Chinese remaindering give exactly the proposed Artin factors and no other associated support. This includes a=0 and m=1. Over a field x_0 is regular, and the Artinian reduction is k⊕W where W has dimension n−1 in degree one and square zero. The minimal resolution reduces along x_0, and the Koszul complex on W has in homological degree i>0 homology only in internal degree i+1: its scalar-to-linear differential is injective as each nonempty wedge expands into a disjoint nonzero set of monomials. The resulting rank is (n−1) binom(n−1,i)−binom(n−1,i+1)=i binom(n,i+1). This gives the characteristic-independent Betti numbers and the stated Hilbert series. The supplied script and verification note were inspected statically, not replayed; the integral calculation supplies the general check.

## originality

PASS

The supported contribution is the integral determinantal identification and hence the exact wild fibers. The target is the classical diagonalizable group D(Z/n), whose local fibers are immediate once that target is recognized, but the assertion that the all-minor projective scheme realizes it integrally is the distinctive comparison. The inspected pluri-circulant Fourier diagonalization identifies the split non-wild case and confirms contextual Betti numbers there. Its hypotheses exclude the new fiber regime. Neither that reduction nor Cohen–Macaulayness or constant Betti numbers can identify the wild completed local rings. No matching integral identification was established in the accessible material; this pass does not credit a new homological formula or establish priority.

## value

PASS

For the natural rank-one circulant section, invertible Fourier diagonalization loses its force exactly in wild characteristic. The result gives the actual integral family and precise nilpotent thickness at each wild point, distinguishing geometric support from scheme length and supplying a model usable under base change. These facts are not supplied by dimension or Hilbert data alone. The standard calculations about the target and the Betti numbers are context, not the reason for acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
