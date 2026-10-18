---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For nonzero finite-rank H_{bar psi} with psi∈BMOA_0, compactness and weak nullness of normalized Hardy kernels at |a|→1 imply any SRKT norm equality is attained at some interior k_a. Classical Kronecker finite rank forces rational psi analytic with no closed-disk poles and hence bounded; the normalized disk involution phi_a transports k_a to the origin. Set g=psi∘phi_a-psi(a). Nehari distance dist(bar psi,H∞) is invariant under boundary composition phi_a and constants; the Poisson harmonic-measure/Bonsall kernel variance gives ||g||_2²=P(|psi|²)(a)-|psi(a)|²=||H_{bar psi}k_a||². Thus the transformed g has minimal Hankel norm equal to ||g||_2. Brevig–Seip Theorem 1, inspected in the original primary PDF, states minimal implies maximal norm, and simultaneous L² and L∞ equality forces constant boundary modulus; rational inner g=C I must be a finite Blaschke. Undo phi_a and g(0)=0 yields psi=C(B-B(0)). Conversely Bonsall for finite B gives ||H_{bar psi}k_a||²=|C|²(1-|B(a)|²), norm |C| and zeros exactly norming kernels; ker H_{bar B}=BH² gives rank deg(B), while sup_boundary|B-B(0)|=1+|B(0)|. The phase factor on H_{bar psi}=conj(C)H_{bar B}, not C, is an immaterial typographical scalar issue in the package proof: ranks and norms are unchanged. Analytic rationality, finite Blaschke and boundary arguments establish all degrees; finite matrix spot checks are not a proof.

## originality

PASS

Best-of-knowledge PASS: the primary September 27 Dyakonov paper, now inspected in full on official arXiv HTML, explicitly poses the general SRKT equality classification and asks for bounded cases with ||psi||_G<||psi||∞. A prior published SCOPE result covers only polynomials (monomials). The new classification for every finite-rank rational Hankel and norming kernels has a genuine Möbius-normalization bridge not stated in these sources; minimal/maximal theorem and Kronecker are correctly acknowledged as existing inputs.

## value

PASS

Finite-rank Hardy Hankel operators are a natural complete rational class, and the current primary paper explicitly requests the strong reproducing-kernel equality characterization and bounded strict examples. The exact shifted finite-Blaschke classification for arbitrary degree, norming-kernel zero set, rank formula and strict uniform-norm dichotomy solve a meaningful well-posed part of that request; this is not a routine polynomial substitution, because Möbius normalization bridges norming kernels at arbitrary disk points to a known but different minimal-norm theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
