# Scientific review: sharp all-degree binomial-polynomial semigroup asymptotics

## Correctness — PASS
For fixed degree \(d\ge2\), a direct Vandermonde bound on index cost and a fixed-depth greedy binomial expansion give the exact power-saving profile \(\mu_d(n)=(d!n)^{1/d}+O_d((n+1)^{(d-1)/d^2})\). The coprimality condition gives an exact Apéry residue envelope, with the minimization over additional multiples of \(a\) pinned between two \(b\)-independent bounds. Standard Frobenius and genus Apéry identities imply the two stated expansions uniformly in \(b\). The proof covers all \(a\ge2\) and fixed \(d\ge2\); the asymptotic constants depend only on \(d\). The independent finite algorithm comparisons validate the residue setup on \(928\) sample cases but are not substituted for symbolic proof.

## Originality — PASS within checked literature
Hashuga–Herbine–Jensen (arXiv:2009.01981, §§3 and 8) analyze the same degree-two generator family; their Corollaries 8.3 and 8.5 give \(\Theta(a^{3/2}+ab)\), not the sharp constants and power-saving precision here, and do not treat all higher degrees. Liu–Xin–Ye–Yin (arXiv:2306.03459) give repunit-recurrence Apéry results with nonmatching hypotheses. Hwang–Song (arXiv:2412.17882) treat finite pure fixed-upper binomial coefficient generators, not the mixed polynomial family. Actual published-finding corpus queries for sharp constants, degree-d variants and coin-cost equivalences did not return an implication-matching record. An abstract-only broad graphical semigroup paper and unindexed earlier work remain residual coverage risks; no unconditional priority or independent novelty certification is claimed.

## Mathematical value — PASS
Both Frobenius number and genus are central numerical-semigroup invariants; replacing qualitative order estimates by exact normalized limits and uniform error control determines real new arithmetic information. The theorem also extends the motivating degree-two phenomenon to every fixed integer degree \(d\ge3\), with a structural weighted-binomial lemma useful for further analysis of polynomial-generated semigroups. The precise leading coefficients are mathematically motivated by the natural gap statistics of the family.

## Limitations
The error exponents need not be optimal; no exact finite-parameter Frobenius formula, growing-degree uniformity, or independent mathematical audit is asserted. Previously inaccessible or unindexed stronger theorems remain a publication-priority risk.

Self-review: passed. Independent audit: not yet performed.
