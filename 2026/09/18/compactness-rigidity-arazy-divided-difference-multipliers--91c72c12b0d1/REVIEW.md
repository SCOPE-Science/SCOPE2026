# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The necessity argument was checked against all endpoint conventions
\(0<p,q\le\infty\). Matrix units \(e_{ik}\) have unit norm in every
\(\mathcal S^q\), and differences sharing the same row have one singular value,
so the noncompactness and essential-norm arguments do not depend on local
convexity.

For sufficiency, the condition \(f(H_\lambda)=0\) forces all divided differences
between distinct spectral values to vanish. Every nonzero eigenspace of
\(H_\lambda\) is finite dimensional because \(\lambda\in\ell^r\), while the
possibly infinite zero eigenspace contributes nothing because the derivative
bound implies \(f'(0)=0\). The resulting multiplier is a weighted spectral
pinching.

The two exponent regimes were checked separately. If
\(p<s=\max\{q,1\}\) (with \(s=\infty\) for \(q=\infty\)), the sharp boundedness
condition gives the exact Hölder relation needed to put the diagonal weight in
\(\mathcal S^t\). If \(p\ge s\), the weights tend to zero and finite spectral
truncations converge in multiplier norm. The argument also covers
\(q\le1\), \(p<1\), and the \(\infty\) endpoints.

## Originality

Verdict: PASS, to the best of our knowledge.

The primary recent source, Huang--Sukochev arXiv:2609.17144v1, was inspected at
the theorem and definition level. Its Theorem 1.1 gives the sharp universal
boundedness region for the divided-difference multiplier. The inspected full
text does not state the compactness equivalence proved here; searching the full
text for compactness located only background/reference uses rather than a
compactness theorem for this family.

Related literature considered under compact Schur multipliers,
divided-difference multipliers, unequal Schatten exponents, Schur--Hadamard
compactness, and double-operator-integral terminology includes Hladnik's
characterization of compact Schur multipliers on \(B(H)\), Stout's
essential-numerical-range theorem, Andersson's factorization of compact Schur
multipliers, the Sukochev--Tomskova theory of \((E,F)\)-multipliers, and the
Aleksandrov--Peller theory for quasi-Banach Schatten multipliers. Their located
statements concern different multiplier spaces or boundedness/complete
boundedness and do not state the fixed divided-difference criterion across the
full unequal-exponent quasi-Schatten range.

The complete texts of Hladnik (2000) and Andersson (2005) were not inspected;
only bibliographic records and abstracts were available. They are the main
residual originality risk because they contain general compact-Schur-multiplier
factorization criteria that could imply special endpoint cases. Stout's
available abstract likewise addresses compact Schur multiplication after a
choice of basis and “smaller Schatten classes,” so an unrecognized equivalent
formulation is a secondary risk. No located source gave the theorem as stated
here or the spectral equivalence \(S_{\Psi_{f,\lambda}}\) compact iff
\(f(H_\lambda)=0\) under the 2026 sharp exponent region.

## Value

The theorem separates boundedness from compactness for the newly completed
Arazy classification. The entire exponent polyregion governs boundedness, but
compactness is controlled by the much more rigid spectral condition
\(f(H_\lambda)=0\). The fixed-row obstruction gives a reusable mechanism and a
quantitative essential-norm lower bound. The converse identifies the compact
case with a weighted finite-spectral pinching and explains exactly how the
sharp exponent condition supplies the required Schatten summability.

This is more informative than a single counterexample: for the natural
prototype \(f(t)=t|t|^\alpha/(\alpha+1)\), every nonzero admissible compact
diagonal \(H_\lambda\) produces a bounded but noncompact multiplier throughout
the full sharp region.

## Limitations

No statement is made for arbitrary exceptional bounded multipliers outside the
universal exponent region. Ordinary compactness, not complete compactness, is
classified. The result is discrete and does not assert an atomless semifinite
analogue. Residual prior-art risk remains in the older general compact Schur
multiplier literature described above.
