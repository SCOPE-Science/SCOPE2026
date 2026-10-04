# Exact covariance defect in the multigrade EAIE
## Finding
For the efficient assessment for interrelated effects (EAIE) in Liao (2025), let \(F\) be a finite set of factors, let \(n=|F|\), and let factor \(m\) have positive maximum grade \(d_m\). Write
\[
\Delta_{m,k}H=H(k e_m)-H((k-1)e_m),
\]
where \(e_m\) is the grade-one vector for factor \(m\). The published EAIE is
\[
\Psi_{m,k}(H)=\Delta_{m,k}H+\frac1n\left(H(d)-\sum_{j\in F}\Delta_{j,d_j}H\right).
\]
Under the paper's covariant transformation
\[
H(\mu)=U(\mu)+\sum_{{j:\mu_j>0}}\sum_{{q=1}}^{{\mu_j}}\zeta_{{j,q}},
\]
the exact transformation law is
\[
\Psi_{{m,k}}(H)-\Psi_{{m,k}}(U)
=\zeta_{{m,k}}+\frac1n\sum_{{j\in F}}\sum_{{q=1}}^{{d_j-1}}\zeta_{{j,q}}.
\]
Hence the published covariant-transformation requirement \(\Psi_{{m,k}}(H)=\Psi_{{m,k}}(U)+\zeta_{{m,k}}\) holds for a particular shift if and only if
\[
\sum_{{j\in F}}\sum_{{q=1}}^{{d_j-1}}\zeta_{{j,q}}=0.
\]
It holds for every allowed shift if and only if \(d_j=1\) for every factor. Therefore on every genuine multigrade domain, meaning at least one \(d_j\ge2\), Lemma 3.4 is false as written, and the characterization in Theorem 3.9 cannot hold as stated because its proposed characterized rule fails one of the required axioms.

## Assumptions and scope
A multichoice situation has grade space \(D_F=\prod_{{m\in F}}\{{0,1,\ldots,d_m\}}\), characteristic mapping \(H:D_F\to\mathbb R\) with \(H(0)=0\), and positive-grade rule coordinates \((m,k)\) with \(1\le k\le d_m\). The statement uses exactly Definition 2.1 and the definition of covariant transformation (COTR) in the cited paper. No monotonicity, superadditivity, convexity, or probabilistic assumption is needed.

The consequence for Theorem 3.9 is only logical: a rule that fails COTR on the stated domain cannot be the rule characterized by a conjunction that includes COTR. This finding does not assess the paper's completeness axiom, its bilateral-reduction calculations, or its dynamic convergence theorem except where those statements explicitly depend on the failed COTR characterization.

## Proof
For every positive grade \(k\), the additive transformation gives
\[
\Delta_{{m,k}}H
=\Delta_{{m,k}}U+\zeta_{{m,k}}.
\]
At the grand grade vector \(d\), however, every grade shift accumulated along every factor is present:
\[
H(d)-U(d)=\sum_{{j\in F}}\sum_{{q=1}}^{{d_j}}\zeta_{{j,q}}.
\]
The EAIE balancing term subtracts only the highest-grade step of each factor. Therefore
\[
\begin{{aligned}}
&\frac1n\left(H(d)-\sum_j\Delta_{{j,d_j}}H\right)
-\frac1n\left(U(d)-\sum_j\Delta_{{j,d_j}}U\right)\\
&=\frac1n\left(\sum_j\sum_{{q=1}}^{{d_j}}\zeta_{{j,q}}-\sum_j\zeta_{{j,d_j}}\right)\\
&=\frac1n\sum_j\sum_{{q=1}}^{{d_j-1}}\zeta_{{j,q}}.
\end{{aligned}}
\]
Adding the transformed step effect proves the displayed covariance-defect identity.

For a fixed shift, COTR is therefore equivalent to vanishing of the common defect term. If every \(d_j=1\), the inner sums are empty and the defect is identically zero. Conversely, if some \(d_r\ge2\), choose \(\zeta_{{r,1}}=1\) and every other \(\zeta_{{j,q}}=0\). The common defect is then \(1/n
e0\), so universal COTR fails. This proves the if-and-only-if classification.

For an explicit two-factor witness, take \(d=(2,1)\), \(U=0\), \(\zeta_{{1,1}}=1\), and every other shift equal to zero. Then \(H(1,0)=H(2,0)=H(1,1)=H(2,1)=1\), while \(H(0,1)=0\). The step effects are \(1,0,0\), the grand value is \(1\), and the EAIE balancing term is \(1/2\). Thus the three positive-grade EAIE coordinates shift by \((3/2,1/2,1/2)\), whereas COTR requires \((1,0,0)\).

The published proof of Lemma 3.4 correctly obtains the step shift \(\zeta_{{m,k}}\), but in its next displayed calculation it replaces the grand-value shift by only \(\sum_j\zeta_{{j,d_j}}\). The definition of the transformation instead gives the full sum over all grades, and the omitted lower-grade terms are exactly the defect above.

## Verification
The standalone `verify.py` uses exact rational arithmetic. It reconstructs the two-factor counterexample, verifies the published EAIE formula coordinate by coordinate, checks the defect identity on several multigrade vectors at the level of formal coefficient dictionaries, and verifies that the defect vanishes in the binary-grade case. Running

```text
python verify.py
```

prints `VERIFY_OK` if all checks pass. No floating-point comparison is used.

## Relationship to prior work
Liao (2025) defines the EAIE in Definition 2.1, defines COTR in Section 3, states in Lemma 3.4 that the EAIE satisfies COTR, and uses that lemma in the characterization stated as Theorem 3.9. The publisher's worked industrial example also uses the same EAIE balance term.

A close predecessor is Chen, Huang, and Liao (2021), which defines the multi-choice level-individual index (MLII). Its balance term subtracts the sum of individual-level distinctions over all activity grades, not merely the highest-grade distinction of each factor. Under an additive grade shift, the grand-value shift and that full sum cancel. Thus the predecessor does not imply the defect above; the defect is tied to the different balance term printed in the 2025 EAIE.

Exact-title, DOI, lemma-name, covariance, correction, corrigendum, and semantic searches did not locate a public correction of the 2025 COTR statement. Those searches are evidence of comparison, not a proof that no correction exists.

## Limitations
The result is a correction to the formula and axiomatic characterization as publicly available, not a claim that every conclusion in the article is false. In particular, the binary-grade specialization has no covariance defect, and a particular multigrade shift can still satisfy COTR when its lower-grade shifts sum to zero. A repaired multigrade rule would require a changed balancing term, a restricted covariance axiom, or another modification; no uniqueness claim for such repairs is made here.

The exact first public date used for the source is the publisher's dated record, 30 June 2025. A ResearchGate metadata page currently labels the article by month as January 2025 but does not supply an exact earlier public day; no exact earlier dated copy was verified.

## References
1. Y.-H. Liao, “Integrating axiomatic and dynamic mechanisms under industrial management situations: game-theoretical analysis,” *AIMS Mathematics* 10(6), 14975–14995 (2025). DOI: 10.3934/math.2025671. See Definition 2.1, the COTR definition, Lemma 3.4, Theorem 3.9, and Eqs. (5.2)–(5.3).
2. K. H.-C. Chen, J.-C. Huang, and Y.-H. Liao, “Sustainable Combination Mechanism for Catalysts: A Game-Theoretical Approach,” *Catalysts* 11, 345 (2021). DOI: 10.3390/catal11030345. See Definition 1 for the MLII balance term.
