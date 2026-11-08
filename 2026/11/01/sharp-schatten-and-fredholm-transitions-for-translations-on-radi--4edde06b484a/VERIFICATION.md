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

Monomial norms equal alpha^(-2n/m) Gamma((2n+2)/m)/Gamma(2/m), so differentiation is a backward weighted shift with w_n~(alpha m/2)^(1/m) n^(-(1-m)/m). For m<1 the shift is compact quasinilpotent; T_b=exp(bD). D^2H_b(D) has singular numbers O(n^(-2beta)); Ky Fan rank shifts k=floor(n^gamma), 1/2<gamma<1, yield s_n(T_b-I)~|b| c_m n^(-beta), including exact Schatten p cutoff, weak endpoint and singleton ordinary/essential spectra. For m=1, w_n=(alpha/2)sqrt(2n/(2n+1)), so D differs compactly from R times the backward shift. The Calkin circle, holomorphic factorization of exp(bz)-mu, and surjectivity of interior backward-shift factors establish the folded Fredholm curve, integer index and resonance kernel count (boundary roots are not eigenvectors). Complete matrix polynomial norm equality follows from the matrix von Neumann inequality plus the unitary Calkin image. This independently reconstructed analytic proof covers every n and m in the stated ranges; a finite check alone would not.

## originality

PASS

Best-of-knowledge comparison of exact conclusions and logical implications, not titles or equal parameter words. Weighted backward shift, translation semigroup exp(bD), and composition-operator formulations were compared. No inspected valid theorem computes the full current difference singular spectrum or the folded index. Mengestie 2017 Theorem 1.2(i) asserts an all-S_p statement contradicted by its own monomial weighted shift: its proof tests only diagonal matrix elements <De_n,e_n>=0 and reverses Schatten inclusion for p<1. The present direct singular-value computation is necessary and is not inferred from that erroneous statement. General boundedness and Toeplitz spectral mapping furnish premises; the sharp Ky Fan remainder argument and root-count spectral folding still require additional calculations. The most relevant newer 2026 arXiv full text was inaccessible, so broader hidden coverage remains a residual risk, not a proof of noncoverage. Residual source-access risks and credited antecedents are explicit.

## value

PASS

The family is a natural translation semigroup on the power radial Fock scale. After known boundedness and derivative compactness, the exact singular-value constant and all-p weak endpoint are genuine quantitative ideal invariants; at m=1 the winding of exponential preimages, jump in Fredholm index, and exact complete essential norm distinguish a sharp critical regime. These are not a routine restatement of boundedness or Hilbert-Schmidt membership.

The dated certificate retains the supplied scientific assessment, sources and limitations.
