# Same-model review

## Correctness

PASS. The displayed source comparison is tested directly against the source equations and fails at an explicit admissible state with the source's own \(\mathcal R_0<1\) parameter set. The repair is exact: subtracting the normalized susceptible equations gives a closed one-sided differential inequality for
\[
q=\frac S\rho-\frac L{1-\rho}.
\]
Its positive part decays at least as \(e^{-\mu t}\). The exact algebraic decomposition of \(\alpha S+\beta L\) then yields eventual domination of the infected subsystem by a constant Hurwitz Metzler matrix below the same threshold. Convergence of \(R,S,L\) follows by variation of constants. Local stability is independently reconstructed from the Jacobian.

## Originality

PASS. The motivating paper explicitly contains the invalid pointwise comparison but not the composition contraction. Searches by source title, SLEIRS incidence terminology, weighted susceptibility, heterogeneous-risk models, and correction language found no source-specific theorem closing the gap.

## Value

PASS. The result preserves the useful published threshold while replacing a globally invalid comparison with a rigorous structural mechanism. It also quantifies the transient excess of effective susceptibility caused by arbitrary initial overrepresentation of the high-risk class.

## Closest literature and limitations

The primary source is Pan and Tang (2024), DOI 10.3934/math.20241032. Ibrahim et al. (2022), DOI 10.3390/vaccines11010003, is the closest inspected high-/low-risk COVID-19 model, but its risk-class flows differ. Katriel (2012), DOI 10.1007/s00285-011-0460-2, treats general heterogeneous susceptibility and does not cover this source-specific contraction.

The proof treats \(0<\rho<1\), \(\alpha>\beta\), and the strict threshold \(\mathcal R_0<1\). The critical case is not claimed.

Same-model review: passed. Independent audit: not yet performed.
