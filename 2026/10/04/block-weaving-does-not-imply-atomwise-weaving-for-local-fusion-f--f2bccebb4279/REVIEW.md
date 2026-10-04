# Same-model review

## Correctness
PASS. With one outer block \(I=\{{1\}}\), \(V_1=W_1=\mathbb R^2\), and unit weights, every fusion weaving is exactly \(\{{(\mathbb R^2,1)}\}\). The local systems \((e_1,e_2)\) and \((e_2,e_1)\) are orthonormal bases with bounds \(1\), but the atomic weave selecting \(f_{{11}}\) and \(g_{{12}}\) is \((e_1,e_1)\), which has zero energy on \(e_2\). Thus the source theorem's forward implication is false under its own hypotheses. The reverse implication follows from \(aE_\sigma\le Q_\sigma\le bE_\sigma\), giving fusion bounds \(L/b\) and \(U/a\).

## Originality
PASS. The primary 2024/2025 source materially inspected states the stronger atomwise equivalence and its forward proof only quantifies over outer subsets. Exact-title, theorem-number, correction, local-frame, and counterexample searches found no indexed correction. The materially inspected 2018 source gives the weaker and correct blockwise local-frame equivalence, so it does not cover the counterexample or the diagnosis that the stronger 2024/2025 implication fails.

## Value
PASS. The affected statement is presented as a characterization transferring robustness between fusion frames and ordinary local frame systems. The counterexample shows that block-level robustness cannot be promoted to arbitrary atom-level robustness, even with one block, unit weights, and orthonormal local frames. The one-way correction identifies exactly which direction remains safe to use.

## Closest literature and limitations
The closest prior result is Neyshaburi--Arefijamaal, Lemma 2.2 (arXiv:1802.03352), which characterizes fusion weaving through unions of complete local blocks for each outer partition. Bemrose et al. (doi:10.7153/oam-10-61) supplies the ordinary atomwise weaving definition. No indexed erratum or correction to Bhandari's Theorem 3.1 was located. An unindexed note or informal observation could still exist. The result does not address extra structural assumptions that might restore the false implication. A possible interpretive defense is that condition (2) was intended to mean only block-constant switching, but that would be a different notion from ordinary woven frames and would reduce the statement to the earlier blockwise characterization.

Same-model review: passed. Independent audit: not yet performed.
