# Scientific review: strict cycle–descent association for Ewens derangements

## Correctness — PASS
The explicit finite domain, \(\theta>0\), and the function's strict monotonicity are required. The adjacent-label conjugation involution proves the established class-conditional descent mean; marking one two-cycle gives the exact mixed-moment identity. A deletion/insertion decomposition gives a positive two-component mixture of derangement cycle-count laws. Induction establishes the stochastic sandwich, and the one-long-cycle event makes the increasing-function expectation gap strict. The unrestricted sign follows from marking two fixed points versus a two-cycle. Exact enumeration through size eight and tail checks through size 35 support but do not replace the proofs. Reproduction: `python3 verify.py` gives `PASS: 3295 exact checks`.

## Originality — PASS (qualified historical priority)
The class-conditional descent mean is a prior theorem of Fulman, reproduced in Campion Loth et al., Corollary 4.10. Da Silva–Jamshidpey–Tavaré give the Ewens derangement cycle law. The companion cycle-covariance result cited in RESULT.md gives the exact formula and positive sign for Cov(C₂,K), so the conditional mean settles f(k)=k. The marked-cycle method also gives the transformed covariance identity; that identity alone gives no sign for general f. The distinct claim is that the deletion mixture yields a stochastic sandwich, not just ordered means, and hence the strict sign for every strictly increasing f. The catalogue date does not settle priority between the two results. Exact enumerative coverage by broader generating functions remains a residual risk; no absolute priority is asserted.

## Value — PASS
Conditioning on no fixed points reverses the sign of the classical cycle-count/ordinary-descent covariance under the uniform law. The effect holds for every positive Ewens parameter and every strictly increasing cycle-count transform, not just for one numerical covariance. Its proof identifies the structural mechanism—forcing a two-cycle stochastically raises the cycle count—and covers all finite sizes with exact boundary cases. This is an interpretable dependence result for a natural probability family, not a routine finite recomputation.

## Limitations and closest literature
Most ingredients are established. The finding is a strict association at the level of mixed first moments, not stochastic dependence of the full pair. Material examined: Bóna (2006), the full 2008 Eriksen–Freij–Wästlund paper, da Silva–Jamshidpey–Tavaré (2020), Campion Loth et al. (2023). Gessel–Reutenauer (1993) has stronger joint enumerative coverage; it was identified through the 2023 literature discussion but its full original text was not accessible during this assessment. This limits historical-priority confidence without changing the mathematical proof.

Self-review: passed. Independent audit: not yet performed.
