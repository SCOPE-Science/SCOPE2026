# Review

## Correctness

PASS. Let \(H_a=\{K\ge a\}\). Vovk's Proposition 1 gives \(\mathbf m(H_a)\ge\tau(a)/c_1\), while Theorem 2 gives \(\mathbf m(B_g(a))\le c_3S_g(a)\), where \(S_g(a)=\sum_{k\ge a}2^{-g(k)}\). Hence the conditional bad share is at most \(c_1c_3S_g(a)/\tau(a)\). The companion note proves \(\tau(a)/f(a)\to\infty\) for every computable decreasing \(f\to0\). With \(f=1/h\), this gives \(1/\tau(a)=o(h(a))\), proving the master conditional estimate. Each displayed specialization follows from the corresponding series bound in Corollaries 3--6.

The proof correctly preserves the quantifiers: the constant controlling the best-fit threshold depends on \(g\), while the normalization conclusion holds for every separately chosen computable divergent \(h\).

## Originality

PASS. The September source supplies the numerator bound and says informally that the “vast majority” of high-complexity objects are probabilistically random, but it does not formulate or bound the normalized conditional ratio. Its denominator comparison explicitly points to the August companion note, whose tail lemma supplies the additional asymptotic fact needed for normalization. Targeted published-finding and literature searches did not locate the master conditional theorem or the four conditional-rate consequences.

The result is not a new absolute concentration theorem; its originality is the quantified conditional normalization statement, especially the fact that the loss is smaller than every prescribed computable divergent factor.

## Value

PASS. The primary paper's motivating language is conditional—what proportion of sufficiently complex objects are probabilistically random—while its main inequalities are absolute universal masses. The accepted theorem closes that interpretive gap rigorously. It shows that conditioning on high complexity does not destroy the source's qualitative decay regimes and quantifies exactly how little can be lost to normalization. This gives a reusable form for comparing future bad-set estimates against the extraordinarily slow universal tail.

## Closest literature and limitations

Vovk (September 2026) gives Proposition 1, Theorem 2, and Corollaries 3--6. Vovk (August 2026) proves the universal-tail domination lemma. Standard algorithmic-information references supply the universal-semimeasure framework but do not state the combined conditional theorem.

The result is a structural corollary, not a sharper numerator estimate, and its little-\(o\) onset is noncomputable in general.

Same-model review: passed. Independent audit: not yet performed.
