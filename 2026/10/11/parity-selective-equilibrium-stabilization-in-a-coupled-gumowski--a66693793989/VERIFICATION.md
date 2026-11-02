---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Independently reconstructed the actual displayed odd-numerator map. F(0)=0, F(±1)=±1 and slopes c0=2−mu, c±=mu. At E_s the Fourier eigenmode λ=cos(2πk/N) has Jacobian [[d,B],[c_s d−1,c_s B]], d=(1−eps)c_s+eps λ, B=(1−eps)(1+a)>0; direct symbolic calculation gives det=B and trace=(1−eps)(2+a)c_s+eps λ. The quadratic Jury tests reduce to eps>a/(1+a), c_s<1, and (1−eps)(2+a)(1+c_s)+eps δ_N>0 with exact extremal λ_min=−1 for even N or −cos(π/N) for odd N. The c_s<−1 odd window has lower endpoint max{a/(1+a), A/(A+δ_N)}, positive width, and for fixed A>0 the width asymptotic π²/(2AN²). The smooth map has open locally exponentially attracting basins at strict Schur sinks. The independent SymPy check verified symbolic trace/det and both tight Jury endpoints, and exact 2N×2N spectra at N=3,4,5,6 with a=1/4,mu=−2,eps=9/10 (stable only N=3 there). Equality cases are correctly excluded; numerical finite checks are not used as the proof.

## originality

PASS

Best-of-knowledge exact specialization not found covered in a primary same mathematical model article: Fatoyinbo–Ghosh gives the ring recurrence and numerical collective phase diagnostics; Ambika–Ambika uses a distinct quadratic-numerator local map and unnormalized two-map coupling; general master-stability references establish methods, not the stated strict all-N ring criteria under these dynamics. Full original preprints inspected, Resultary queried three ways, and a high-relevance general theory source remained inaccessible at full-text level. Novelty qualification: routine Fourier/Jury tools, possible buried special case in generic network-spectral theory, and the Resultary self-match cannot establish priority.

## value

PASS

A canonical finite ring has three explicitly given homogeneous equilibria whose local stability is a natural, interpretable invariant directly relevant to a published phase-diagram study. This exact whole-parameter classification yields a genuine odd/even structural transition for c<−1, its sharp N^−2 vanishing coupling-window size, and rigorously open basins of two distinct sinks in both source-study parameter bands. It resolves a specific mathematically motivated local-stability question rather than a random slice or mere numerical confirmation. The contribution is modest and standard-tool based; it establishes no global basin volumes, periodic/chaotic attractors, synchronization prevalence, or nonlinear behavior on Schur boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
