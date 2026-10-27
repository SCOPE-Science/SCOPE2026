# Review of the joint linear-prime law for binary continuants

## Correctness — PASS

The recurrence for continuants at the evaluation points \(0\) and \(1\) yields nine nonzero product states. The explicitly listed first five state-count vectors satisfy \(v_4=v_3+2v_1+4v_0\). Multiplication by the fixed transition matrix transfers this identity to every degree, so the fourth-order recurrence and generating function hold without experimental extrapolation. A three-state marginal transfer establishes the marginal count. Inclusion–exclusion determines all four joint cells. Algebraic substitution yields the covariance identities; no probabilistic independence is assumed in their proof. Independent full-polynomial enumeration for all words through degree 14 and exact recurrence checks through degree 99 returned `VERIFY_OK`. The proof is finite-dimensional algebra valid for all degrees. Risk: arithmetic transcription of the displayed matrices and closed forms; the accompanying checker constructs all transitions directly and independently checks low-degree polynomials.

## Originality — PASS, subject to independent priority review

The September/October 2026 literature on orthogonal multiplicity supplies the foundational word–denominator correspondence and studies non-linear residue invariants and an unweighted positive-multiplicity count. It does not give the four-cell distribution by divisibility by \(T\) and \(T+1\), nor the sharp sign-changing finite-degree covariance. The 1998 study of odd orthogonal multiplicities treats a different classification; a 2020 survey of perfect linear complexity treats infinite-sequence equivalences. Published mathematical-record searches found no identical or stronger result that implies the exact two-linear-factor distribution. The 1999 work on prescribed sets of partial quotients is a plausible broader antecedent; its complete full text could not be compared through available lawful access routes. An indexed or unindexed stronger transfer theorem could subsume the calculation. This residual risk is not represented as proof of global uniqueness.

## Mathematical value — PASS

The measure \(\Pr(f)=m(f)/2^d\) is intrinsic to the exact word enumeration used in the 2026 orthogonal-multiplicity problem. Its special linear-prime factors contribute the two exceptional local places in that problem's proposed Euler product. The present exact joint calculation determines the local law unconditionally: each avoidance probability tends to \(2/3\), their joint probability tends to \(4/9\), and the finite-degree dependence oscillates at a sharp \(2^{-d/2}\) scale. This is not the obvious uniform-monic-polynomial law, whose corresponding joint probability is \(1/4\). It supplies an exact local input and a quantitative independence check, rather than a renamed general counting identity. Limitations: only the two degree-one factors are classified; no positive-orthogonal-multiplicity density asymptotic or independence for all prime factors follows.

## Closest sources and comparison limits

- D. Niedbala Giraudin (2026), arXiv:2610.02352v1, Sections 1–4 and references: word parametrization, unweighted counts, residue reciprocity and local non-linear results, not this degree-one joint distribution.
- A. G. B. Lauder (1998), *Polynomials with odd orthogonal multiplicity*, Sections 2–4 inspected from author-hosted full text: odd-multiplicity classification, not this weighted two-linear-factor law.
- J.-P. Allouche, G.-N. Han, H. Niederreiter (2020), arXiv:2008.12160v1, Sections 1–5: PLCP/apwenian equivalents and constructions, not this weighted joint count.
- A. G. B. Lauder (1999), *Continued fractions of Laurent series with partial quotients from a given set*: bibliographic description available, but inaccessible complete text leaves a precise priority risk.

Self-review: passed. Independent audit: not yet performed.
