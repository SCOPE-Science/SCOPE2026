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

For k_+,k_-,r>0 and the stationary two-sided PSD G(w)=a(c+w^2)/(w^4+2d w^2+c^2)+r/(4r^2+w^2), independently verified the exact rational identity G(sqrt(x))-G(0)=x(C_r+B_r x-A_r x^2)/[4r c(x+4r^2)(x^2+2d x+c^2)] symbolically with SymPy, with a=k_++k_-, b=k_+-k_-, d=a^2-b^2>0, c=a^2+b^2, E=3b^2-a^2, A_r=4ar+c, B_r=4ar(E-4r^2)-2cd, C_r=16ar^3 E-c^3. The difference is negative when E<=0. For E>0, the vertex of the concave quadratic lies in [0,E/2), and derivative at fixed x<E is 4a(x+12r^2)(E-x)>0; thus its maximum H(r) crosses zero uniquely. The critical-bias h derivative was independently derived and checked positive for 1/3<z<1; its unique root zc=0.9101817562569 gives the continuous/degenerate/jump split. Four independent representative rate comparisons reproduce r*=r0 for theta<=theta_c and r*<r0 with positive-frequency tie for theta>theta_c. The local normal forms x*(p delta-q x), x*(p delta-A x^2) and an isolated positive x* double root justify respective maximizing-frequency exponents 1/2, 1/4, 0-jump and efficiency exponents 2, 3/2, 1. These are analytical signs/expansions, not extrapolations from the source VERIFY.py logs.

## originality

PASS

The same eight-state process and its rational PSD are acknowledged as prior in Jia 2026. The audited claim is the global maximizer classification, exact rate criterion and directionality bifurcation rather than the spectrum itself. The available Jia abstract discusses efficiency bounds, while detailed equation (33)/(34) comparison is supplied in the audited source; this run could not access Jia full arXiv manuscript despite paper-specific public attempts and a lawful institutional retrieval (vpn_disconnected). Dechant establishes broad PSD/dissipation bounds, not the sharp global optimization of this particular rational spectrum. Actual Resultary searches found only other Markov/oscillator transitions. The O PASS is best of knowledge and materially qualified: no whole-document noncoverage assertion is made about unread Jia pages; inaccessible plausible source alone does not force a scientific rejection.

## value

PASS

The zero-frequency second derivative of a spectrum is a local condition and can misclassify whether an experimentally observed nonzero-frequency peak is globally dominant. The exact onset r*, bias boundary theta_c and three different local exponents completely classify a natural eight-state stochastic biochemical network. The high-bias jump supplies a mathematically motivated counterexample to taking local curvature as a sharp criterion; this is useful independent of novelty of the known input spectral formula. No thermodynamic phase transition of the stationary measure is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
