# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reuses only the explicitly identified geometric and recurrence ingredients of Lerner's \(p=2\) construction and recomputes every exponent needed for general \(p\).

The key substitution is \(w=\sigma^{-(p-1)}\). On a cell of \(\sigma\)-mass \(m\) and area \(A\),
\[
w(C)=A^p/m^{p-1}.
\]
Combining this identity with Lerner's bounds
\[
m_{u,v}\ge\theta S_{u,v},\qquad
S_{r,s}/S_{u,v}\le(3/2)^{(r-u)+(s-v)},\qquad
|C_{u,v}|/|R_{r,s}|\le2^{-(r-u)-(s-v)}
\]
gives a geometric series with ratio
\[
\frac{(3/2)^{p-1}}{2^p}=\frac{3^{p-1}}{2^{2p-1}}<1
\]
for every \(p>1\). This verifies the full general-\(p\) \(A_p\) upper bound. The lower characteristic is computed exactly on \(R_{1,0}\).

For the norm lower bound, \(f=\sigma\mathbf1_Q\) has exactly unit \(L^p(w)\) norm. Each hyperbolic output cell contributes
\[
4^{-p}\theta^{-(p-1)}S_{r,s}^{-(p-1)}
\]
to the \(p\)-th power. Lerner's \(S_{r,s}<2\) estimate on \(rs\le D\), together with the divisor-sum count \(\gtrsim D\log D\), gives
\[
\|M_{\mathrm s}f\|_{L^p(w)}^p\gtrsim_p\theta^{-p}\log(1/\theta).
\]
The reflection lemma extends to \(A_p\) with factor \(9^p\), because the same pulled-back rectangle is used for the averages of \(w\) and its dual weight. Product extension then gives all \(d\ge2\).

Potential failure modes checked include \(p\downarrow1\), large \(p\), the cell \((0,0)\), normalization of the dual weight, and the conversion from the \(\theta\)-scale to the \(A_p\)-characteristic scale.

## Originality

**PASS, to the best of our knowledge.**

The following highly relevant sources were inspected:

- Lerner, arXiv:2609.14008v1. Its full accessible text states the direct Buckley analogue is open in general, proves failure at \(n=2,p=2\), and explicitly says the note concentrates on \(p=2\).
- Ombrosi--Rey, arXiv:2609.17246. Its accessible text gives improved upper exponents for every \(1<p<\infty\) and \(d\ge2\), while describing Lerner's lower obstruction specifically in the \(p=2\) case.
- Luque--Pérez--Rela, arXiv:1512.01112 / J. Geom. Anal. 27 (2017), which is the earlier strong-weight context cited for the Buckley-type question.

Searches used exact and synonymous combinations of: strong maximal operator/function, rectangular \(A_p\), Buckley exponent, endpoint power \(1/(p-1)\), logarithmic lower bound, counterexample, all \(p\), Lerner, and arXiv:2609.14008. No prior all-\(p\) statement matching
\[
A^{1/(p-1)}(\log A)^{1/p}
\]
was located. The current SCOPE archive was searched by source identifier, object name, and claim family with no matching record.

No relevant primary source identified by the search was inaccessible. The main residual risk is recency: Lerner's note and the Ombrosi--Rey follow-up are both new enough that a simultaneous observation may not yet be indexed.

The originality claim excludes Lerner's \(p=2\) case and all ingredients already present there. It is specifically the \(p\ne2\) extension, the explicit general-\(p\) logarithmic rate, and the immediate all-dimensional consequence.

## Value

**PASS.**

The direct Buckley-type endpoint estimate was a basic quantitative question for the strong maximal operator. Lerner's new \(p=2\) counterexample showed the phenomenon at one exponent. The present theorem shows that the obstruction is not special to Hilbert-space structure: it persists for every \(1<p<\infty\), with a transparent \(p\)-dependent logarithmic defect. This closes the endpoint pure-power question negatively across the full strong-type range while preserving the still-open problem of the optimal power infimum.

## Limitations

The theorem does not show \(\alpha_p>1/(p-1)\), does not establish optimality of the logarithmic exponent \(1/p\), and makes no \(p=1\) endpoint claim. It is a theorem about the strong maximal operator itself, not an automatic lower bound for other multiparameter operators.

No independent validation is asserted.
