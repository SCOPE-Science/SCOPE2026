# Review

## Correctness

PASS. Let \(\mathcal E=\{f_0,\ldots,f_{k-1}\}\) be \(\mathcal J\)-eventually different. The finite intersection of the pairwise inequality sets lies in \(\mathcal J^*\), so on a co-\(\mathcal J\) set the \(k\) values are distinct and \(F(n)\ge k\).

If \(\mathcal E\) is FSP, the source's Lemma 4.23 supplies an ultrafilter \(\mathcal U\supseteq\mathcal J^*\) making \(\mathcal E\) \(\mathcal U^*\)-maximal. If \(\mathcal U\) avoided \(\{n:F(n)=k\}\), then on a \(\mathcal U\)-large set one would have more than \(k\) available values and could choose a function pointwise outside all \(f_i\), contradicting maximality. Conversely, if the exact \(k\)-fiber is \(\mathcal J\)-positive, choose an ultrafilter containing it. On the simultaneous pairwise-distinct set the \(k\) functions exhaust all \(k\) coordinate values, and ultrafilter primeness forces one equality set to be large for every test function. This gives \(\mathcal U^*\)-maximality and hence FSP.

The existence criterion follows from the exact condition for a \(k\)-member \(\mathcal J\)-eventually-different family, namely \(\{n:F(n)\ge k\}\in\mathcal J^*\), proved in both directions in the package.

## Originality

PASS. The recent primary source explicitly characterizes finite Van Douwen families by the stronger condition \(\{n:F(n)=k\}\in\mathcal J^*\), and separately proves the general equivalence between FSP and maximality for one ultrafilter extending \(\mathcal J^*\). Full-text searches in that source for finite FSP statements and exact size-\(k\) criteria did not locate the retained theorem.

The new statement is not a special case of the published finite Van Douwen classification: it gives a different exact boundary, \(\mathcal J\)-positivity rather than membership in \(\mathcal J^*\), and produces an explicit finite FSP/Van-Douwen separation. Targeted published-finding and literature searches under the main aliases did not locate this criterion.

## Value

PASS. Finite-section productivity is one of the paper's principal new notions, while its explicit finite classification is given only for Van Douwen maximality. The retained theorem completes the adjacent finite case and reveals the exact structural gap between the two notions. The alternating-fiber example shows that this is a genuine hierarchy boundary, not merely a reformulation.

## Closest literature and limitations

The closest source is He--Luo--Zhang (2026): Proposition 3.3 gives the finite Van Douwen criterion; Lemma 4.23 gives the FSP/ultrafilter equivalence; Theorem 5.2 gives the Stone-space hierarchy. The theorem here adds the finite-cardinality analysis needed to convert the existential ultrafilter condition into an exact fiber condition.

Schembecker (2026) studies a different finite-product productivity hierarchy for ordinary MED families. Its abstract and the comparison in the primary source were inspected; no whole-document absence claim is made here, leaving a small terminology-level residual risk.

The theorem does not address infinite FSP families or descriptive complexity.

Self-review: passed. Independent audit: not yet performed.
