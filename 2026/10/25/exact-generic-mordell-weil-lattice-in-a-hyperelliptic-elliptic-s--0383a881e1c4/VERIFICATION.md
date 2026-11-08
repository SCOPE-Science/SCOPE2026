---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Rational source E0:y^2=x^3+(t^2+1)x+1 has squarefree discriminant 4t^6+12t^4+12t^2+31, six I1 fibers and, from u=1/t with a4=u^2+u^4, a6=u^6, a split I0* at infinity. Rational surface rho=10 and D4 correction give MW rank 4, zero torsion and D4* lattice by Oguiso-Shioda row 9. At each unramified-discriminant hyperelliptic cover, χ=1 and all twelve fibers are I1. P0=(0,1), Pi=(ri,si t), ri^3+ri+1=0, si^2=ri, satisfy equation. In local infinity chart t=v^-2, X=v^2x,Y=v^3y, each Pi has Y=si v, P0 has Y=v^3: distinct slopes at unique smooth point force pairwise local intersection multiplicity 1; affine x differ and all sections avoid O. Shioda height formula gives Gram 2I4. Heights halve on E0; determinant of Z4 is 1, D4* det 1/4, hence index 2. Eliminate free c0 in w²=t^(2g+1)+sum c_j t^j to obtain F(B)=C(t)(c1,...,c_(2g),w), a pure transcendental extension; any morphism P1->elliptic curve is constant, so rational points do not increase. Degree-two base change doubles the source height pairing. Boundaries: g>=2, distinct branch points excluding zero and 6 discriminant roots; generic field only, not equality on all fixed complex specializations. Exact sympy reproduction confirmed gcd(D,Dprime)=1, discriminant(ri cubic)=-31, symbolic c0 elimination, base lattice determinants, and reconstructed both Git tree SHA1 hashes. The saved verifier is a limited arithmetic checker, not a proof of global theorems.

## originality

PASS

Best-of-knowledge originality attaches to the specific uniform explicit four-section system and its index/height interpretation for the newly introduced high-genus covers, not to the already-classified rational-source D4* lattice or the standard no-new-points fact for pure transcendence. The full generic-field group follows quickly from classical table plus actual coefficient elimination and is NOT claimed as a fundamentally new classification theorem; its elementary covered ingredients sharply limit novelty. No direct prior statement of the combined explicit section system was found in material actually read. This remains a narrow PASS with substantial residual risk of implicit prior coverage.

## value

PASS

The invariant is the complete generic arithmetic MW lattice and explicit height-orthogonal section subsystem of Li-Liu’s recently motivated elliptic surfaces with χ=1 and arbitrarily high-genus (-1)-curves. Knowing the precise four independent sections, index-two embedding, and separation of generic arithmetic rank from possible specialization jumps can serve geometric studies of negative curves and arithmetic base-change phenomena. This is a motivated exact invariant on a natural new family, not an arbitrary numerical slice, although the generic group reduces to a classical rational-source table and the new mathematical content is modest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
