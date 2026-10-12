# Review: All open-locating-dominating sets of crown graphs

## Correctness
PASS. The necessity is forced by same-side pairs: if two \(B\)-vertices \(b_i,b_j\) are both omitted, then \(a_i\) and \(a_j\) have identical OLD signatures, and symmetrically for \(A\). For sufficiency, at most one omission on each side leaves at least two selected vertices per side for \(n\ge3\), which guarantees nonempty signatures; same-side pairs are separated by one of the two indexed opposite-side vertices, while cross-side signatures live in disjoint bipartition classes. The enumerator follows by independent side choices. The packaged exhaustive checker agrees for every subset for \(3\le n\le8\).

## Originality
PASS. The 2010 foundational article and the 2014 general follow-up were inspected at statement level and by full-text family-name search; neither contains a crown or complete-bipartite-minus-matching theorem. The 2014 follow-up's extremal and \(C_4\)-free results do not imply the crown formula. Alias searches for identifying open codes and open-separating total-dominating codes found no crown-family statement. The 2015 chain-graph result is inapplicable because crown same-side neighborhoods are pairwise incomparable. A cubic identifying-open-code bound can concern only \(\operatorname{Cr}_4\), not the family classification or polynomial.

## Value
PASS. OLD is a standard hard identification parameter, while crown graphs are a canonical highly symmetric bipartite family. The sidewise one-omission rule classifies every OLD-set, not only one optimum, and immediately gives the exact cardinality enumerator \(z^{2n-2}(n+z)^2\), the optimum \(2n-2\), and the exact \(n^2\) minimizer count. This is a natural complete classification rather than an arbitrary finite computation.

## Closest literature and limitations
Seo–Slater (2010) supplies the foundational definition. Chellali–Jafari Rad–Seo–Slater (2014) gives extremal-value and \(C_4\)-free results plus general bounds. Kincaid–Oldham–Yu (arXiv:1403.7061) is an archive-era OLD-set source on infinite triangular grids. Henning–Yeo treats identifying open codes in cubic graphs, and Pandey treats complexity plus chain-graph algorithms. None of these inspected statements implies the crown all-set criterion.

The scalar boundary \(\operatorname{Cr}_3\cong C_6\) may be covered by cycle-specific work. The exhaustive checker is finite and only stress-tests the symbolic proof. The older 2010 paper was found with month/year public-date evidence but no exact day, so metadata uses the exact 2014-03-27 arXiv public date of an archive-era OLD-set source rather than inventing a day.

Self-review: passed. Independent audit: not yet performed.
