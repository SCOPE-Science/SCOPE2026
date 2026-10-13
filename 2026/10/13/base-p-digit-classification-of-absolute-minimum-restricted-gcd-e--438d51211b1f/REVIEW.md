# Self-review

## Correctness
PASS. At the absolute smallest admissible row \(N=2m\), there is only one selected lower index, so \(G(2m;m)=\binom{2m}{m}\). Kummer's theorem identifies its \(p\)-adic valuation with carries in \(m+m\). Since the published sharp maximum is \(r_p(m)\), the row is extremal exactly when every one of the \(r_p(m)\) possible digit positions emits a carry. This gives the stated digit inequalities, and the counting and binary consequences follow exactly. The bundled checker independently verifies the digit criterion and counts over a broad deterministic grid.

## Originality
PASS with residual bibliographic risk. The direct 2026 source defines the least-extremal-row invariant and solves the distinct family \(m=p^a+1\); it records \(T_2(3)=6\) as an isolated prior instance, but not a general characterization of the absolute-minimum branch. McTague and Wu treat the same multiple-index GCD under different theorem hypotheses. Exact-formula, central-binomial, carry-language, and base-digit searches located no equivalent complete classification or exact count. One supporting paper's full text was unavailable through the inspected HTML endpoint, so absolute historical priority is not asserted.

## Value
PASS. Determining when a newly defined least-extremal invariant attains the smallest admissible row is a natural boundary question. The result gives a complete all-prime structural answer, an exact enumeration for every odd-prime digit length, and a rigid binary family; it is not a routine finite recomputation.

## Closest literature and limitations
The closest sources are arXiv:2610.01328v1, arXiv:1510.06696v5, and arXiv:2606.20940v2. The theorem classifies only the branch \(T_p(m)=2m\); it does not determine \(T_p(m)\) when a digit inequality fails. The known isolated case \(T_2(3)=6\) is explicitly acknowledged as prior art.

Self-review: passed. Independent audit: not yet performed.
