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
The proof was checked directly from its stated assumptions.

1. The recent input theorem was verified in arXiv:2609.12566v1: for every polynomial failure exponent, a uniformly random subsystem of cardinality \(\lceil R^{2/p}\rceil\) has bounded \(\Lambda(p)\) constant with a bound independent of \(R\).
2. The block-generation law is exactly a uniform permutation: the first uniformly selected unordered block, its uniform internal ordering, and an independent recursive uniform ordering of the complement multiply to probability \(1/R!\) for each prescribed residual ordering.
3. Every prefix through \(N/2\) meets at most \(1+2^{2/p}mN^{-2/p}\) blocks, and all relevant residual sizes are at least \(N/2\). Choosing a larger polynomial failure exponent makes one union bound control all these blocks simultaneously.
4. For an arbitrary \(r\)-element set, orthogonality gives the \(L^2\) bound and pointwise Cauchy--Schwarz gives the \(L^\infty\) bound; interpolation yields \(K_p\le r^{(1-2/p)/2}\). This controls every tail beyond the halfway prefix.
5. For Fourier characters, on \(|x|\le(12N)^{-1}\) every phase has real part at least \(\sqrt3/2\), giving the stated lower constant for every subset. A singleton coefficient gives the independent lower bound one.

No numerical experiment, truncated enumeration, or external certificate is used as proof. The constants are not numerically optimized, and no exact random-prefix tail law is claimed.
