---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For odd m, the algebra map π*:C[R_{2m}]→C[R_m] splits via s(e_i)=(e_i+e_{i+m})/2. The kernel K spanned by κ_i=(−1)^i(e_i−e_{i+m}) satisfies s(A_m)K=K²=0, and κ_i s(e_j)=κ_(2j−i). Thus each element has unique s(b)+κ(w), its square is s(b²)+κ(wb), and it is idempotent exactly when b²=b and R_b(w)=w: each fiber is an affine Peirce +1 eigenspace. Fourier coordinates of any odd-base idempotent satisfy F_t=F_(−t) F_(2t); nonzero generated <2,−1> orbits form finite torus-isogeny solutions with nonsingular exponent matrix, giving Δ_d known root counts, isolated reduced base points, and F_tF_(−t)=1 on active orbits. In the even cover, odd-frequency pairs are linear and each active orbit supplies h_d/2 parameters; augmentation 1 adds the self-opposite Fourier parameter. Therefore all reduced complex components are affine spaces and the component dimension polynomial is (1+z)∏_{d|m,d>1}(1+Δ_d z^(h_d/2))^(φ(d)/h_d), with zero the only isolated component and maximum dimension (m+1)/2. Independent complete arithmetic enumeration of C[R_6] idempotents over F7 (7^6 tuples) found 176, with eight fibers and cardinalities {1:1,7:4,49:3}, matching P_6=1+4z+3z². Finite-field check is only corroboration of the complex algebraic proof.

## originality

PASS

Conditional quandle-covering idempotent theorems (Elhamdadi–Nunez–Singh–Swain 2022) require a base with only trivial idempotents, violated by the complex odd-dihedral base. Prior Fourier idempotence relations and odd-base root multiplicities are explicitly known ingredients. The claimed additional even-order split square-zero/Peirce fiber geometry and all-m component-dimension polynomial are qualified new findings. Generic square-zero-extension results might implicitly yield the lifting phenomenon and remain a priority risk.

## value

PASS

Even-order dihedral quandle algebras are a canonical nonassociative algebra family, with nontrivial idempotent varieties over C. A complete smooth component decomposition and exact dimension polynomial for every order twice an odd number is a natural geometric classification; it uses more than a small root count and identifies how odd-base Peirce eigenspaces govern lifting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
