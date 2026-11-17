---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

On the Hardy monomial basis, T_r e_{n+d}=((n+d)!/n!)r^n(e_n+c e_{n+m}); phase removal reduces epsilon^d T_r, epsilon=-log r, to (I+a S^m)D_epsilon, a=|c|>0, diagonal b_epsilon(n)=exp(-epsilon n)prod_{j=1}^d epsilon(n+j). The exact shift-form identity ||(I+aS^m)h||²=(1+a)²||h||²-a||(I-S^m)h||² yields variational norm deficit. Its unique interior maximum at epsilon n≈d has B_epsilon²=A_d²[1+(d+1)epsilon+O(epsilon²)]; shifted lattice rounding requires an explicit -C epsilon² error in lower localization bound. Rescale y=sqrt(epsilon)(n-d/epsilon), separate m residue classes and interpolate near-minimizers. Tightness and local discrete H¹ compactness give a harmonic-oscillator functional with kinetic am² and potential (1+a)²/d; its exact minimum A_d² m(1+a)sqrt(a/d) follows by completing the square. Squared norm and square root then yield first correction (d+1)/2 -m sqrt(a)/[2(1+a)sqrt d]. Independently reproduced SciPy band-matrix top eigenvalues for d=1,m=4,a=1 (coefficient→0), d=1,m=2,a=1 (→0.5), and d=2,m=2,a=1 (→1.14645), with errors decreasing as epsilon→0. Finite samples do not prove the infinite-dimensional lower bound; the interpolation/oscillator argument does.

## originality

PASS

PASS best-of-knowledge: Results indexed for Hardy composition–differentiation include Sun–Liu exact monomial-weight singular values and Fatehi unweighted or general norm bounds. Neither inspected available statement gives the first interior spectral-edge correction for *two taps* 1+c z^m, where shifted columns overlap and a discrete oscillator appears. Resultary search found no exact m sqrt a/[2(1+a)sqrt d] coefficient, apart from this assigned finding. General Kac–Murdock–Szegő bulk distributions do not by themselves imply the top edge first correction. Inaccessible plausible full Sun–Liu manuscript after both arXiv and OA attempts and failed authorized Oxford VPN access is a documented residual risk, not automatic originality failure.

## value

PASS

A sharp first-order norm expansion for a natural finite-band Hardy composition–differentiation family reveals tap-separation dependence invisible to the leading norm and an exact sign change at d=a=1,m=4; it requires a motivated discrete-to-continuum oscillator calculation, not a routine diagonal monomial case. This edge information may guide spectral perturbation and other finite-band composition operators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
