# Same-model review

## Correctness
PASS. The fibre optimization is solved exactly:
\[
\sup_{\|u\|_1=a}\min\{\|z+u\|_1,\|z-u\|_1\}
=
1+\max\{0,a-2\alpha\}.
\]
Two explicit witnesses attain the branches and a complete sign-and-crossing split supplies the upper bounds. The outer \(\ell_p\) norm then reduces every one-coordinate point to a one-variable optimization with endpoint values \(2^{1/p}\) and \(2\|z\|_\infty\). For arbitrary unit vectors, an outer coordinate of arbitrarily small norm yields the uniform lower bound; a balanced fibre point attains it.

## Originality
PASS. The 2018 primary paper was inspected at its local-octahedrality definition, symmetric-chord equivalence, and absolute-sum discussion; it contains qualitative permanence and summand results rather than this numerical profile. Searches covered the exact fibre, candidate formula, pointwise and global forms, and raw chord aliases. The nearest exact quantitative result treats Hilbert fibres and has the incompatible value \(\sqrt2\) for \(p>2\). The current and immediate-prior own ledgers contain no local-octahedrality result.

## Value
PASS. Formula (2) exposes two competing geometric mechanisms in a canonical vector-valued sequence space and supplies an attained exact global index. Its strict separation from the Hilbert-valued case for every \(p>2\) shows that the quantitative local-octahedrality index genuinely detects fibre geometry.

## Closest literature and limitations
Hardtke's 2018 work develops qualitative local octahedrality for absolute sums. The closest exact quantitative comparison is the Hilbert-fibre formula \(s(\ell_p(\Gamma;H))=2^{1/\min\{p,2\}}\). The present pointwise formula is restricted to one-coordinate base points in \(\ell_p(\Gamma;\ell_1^2)\), although the global infimum is exact on the entire unit sphere.

Same-model review: passed. Independent audit: not yet performed.
