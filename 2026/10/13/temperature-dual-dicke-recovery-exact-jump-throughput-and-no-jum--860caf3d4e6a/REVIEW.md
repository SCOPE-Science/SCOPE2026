# Review of temperature-dual Dicke recovery

## Correctness

**PASS.** The three syndrome domains are mutually orthogonal because the two Dicke weights differ by at least three. Each recovery operator has singular values bounded by one. The one-site Dicke projection identity gives exactly the accepted down/up jump coefficient, while a first-order diagonal filter equalizes the two no-jump logical amplitudes. A separate hypergeometric calculation proves the exact normalized no-jump coherence, including its strict inequality at intermediate bath population and its quadratic variance coefficient. Full Kraus-matrix compositions and rational coefficient checks from `verify.py` agree with the statements. Residual risk: the expansions require fixed block length and sufficiently weak damping; no all-size uniform error constant is established.

## Originality

**PASS, with bounded residual risk.** Dutta et al. (arXiv:2609.15924v1) already give the five-qubit Dicke encoding, probabilistic recovery idea, and first-order error removal, plus a general analytic PAQEC framework; these are credited, not claimed. Its main text, recovery sections, general theorem, and appendices were inspected. They do not state the all-size accepted-jump coefficient together with the exact Kraus-group-resolved normalized no-jump coherence factor. The 2026 zero-temperature code paper, 2018 constant-excitation bosonic code paper, and 2014 generalized-amplitude-damping code comparison address different scopes. The leading coefficient remains algebraically derivable from earlier channel identities; an undiscovered equivalent specialization is the main residual risk. Searches of published findings and primary literature found no implication-equivalent exact classification.

## Value

**PASS.** The new combined formula separates throughput and unavoidable thermal coherence loss for a natural extension of a recently studied noise-adapted code. It also locates the exact finite-strength threshold \(D<1\) for every intermediate bath population, and yields a transparent choice of Dicke weight: increasing the smaller excitation weight simultaneously improves the accepted jump coefficient and weakly decreases the no-jump dephasing coefficient (strictly at interior bath population), subject to the three-syndrome separation condition. These are physically motivated design invariants rather than isolated recomputations. The theorem does not claim full-channel optimal recovery or an implementation cost bound.

Self-review: passed. Independent audit: not yet performed.
