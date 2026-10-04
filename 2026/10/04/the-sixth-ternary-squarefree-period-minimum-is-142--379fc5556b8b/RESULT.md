# The sixth ternary squarefree-period minimum is \(142\)
## Finding
Let \(g(p)\) be the minimum length of a ternary squarefree word having exactly \(p\) nontrivial periods. Then
\[
g(5)=142.
\]
Equivalently, if the trivial full-length period is included as in OEIS A332866, the next term is
\[
a(6)=142.
\]

One witness is
`0102101201020120212010210120102012102010210120102012021201021012010212021020102101201020120212010210120102012102010210120102012021201021012010`.
Its proper border lengths are exactly
\[
1,\ 3,\ 11,\ 30,\ 67,
\]
so its nontrivial periods are exactly
\[
75,\ 112,\ 131,\ 139,\ 141.
\]

## Assumptions and scope
A positive integer \(q\le |w|\) is a period of a word \(w\) when \(w_i=w_{i+q}\) whenever both positions exist. The full length \(|w|\) is the trivial period. A proper border is a nonempty proper prefix that is also a suffix; a border of length \(b\) corresponds to period \(|w|-b\).

A word is squarefree when it contains no factor \(xx\) with \(x\) nonempty. The alphabet is ternary. Relabeling the three symbols preserves both squarefreeness and all border and period lengths, so exhaustive enumeration may fix the first symbol to \(0\).

## Proof
Two elementary facts make the finite search small and complete.

First, if a squarefree word \(w\) of length \(n\) has a proper border of length \(b\), then
\[
b<\frac n2.
\]
Otherwise the associated period \(n-b\) is at most \(n/2\), and the first \(2(n-b)\) symbols form a square.

Second, let \(u\) be the longest proper border of \(w\). Every shorter border of \(w\) is also a border of \(u\). Indeed, \(u\) occurs both as the prefix and suffix of \(w\), so equality of a shorter prefix and suffix transfers to the corresponding prefix and suffix of the two copies of \(u\).

Consequently, every squarefree word with at least \(r\ge1\) proper borders has the form
\[
w=u\,v\,u,
\]
where \(u\) is squarefree, \(|u|<|w|/2\), and \(u\) has at least \(r-1\) proper borders. This gives an exhaustive recursion.

The bundled verifier performs that recursion over the ternary alphabet. It normalizes the first symbol to \(0\), enumerates every squarefree middle word compatible with both copies of \(u\), and deduplicates words arising from more than one chosen border. It finds the successive minimum lengths for at least \(r\) proper borders,
\[
1,\ 3,\ 7,\ 23,\ 59,\ 142
\]
for \(r=0,1,2,3,4,5\), respectively. The first five values reproduce the published exhaustive table. At length \(142\) there are four minimizers after fixing the first symbol to \(0\), including the displayed witness. That witness has exactly five proper borders, so the “at least five” lower-bound computation and the exact-five witness together prove \(g(5)=142\).

## Verification
Run `python3 verify.py` in the package directory. The verifier reconstructs the entire recursive enumeration from first principles. It checks squarefreeness incrementally, regenerates the published minima \(1,3,7,23,59\), proves that no word of length below \(142\) reaches five proper borders, and confirms the witness at length \(142\).

The key completeness invariant is structural rather than heuristic: the longest-border lemma forces every candidate into the recursively enumerated form \(u\,v\,u\). No stabilization assumption or sampling is used.

## Relationship to prior work
Gabrić, Rampersad, and Shallit define \(g(p)\) as the shortest ternary squarefree word with \(p\) nontrivial periods. Their exhaustive table gives
\[
g(0),g(1),g(2),g(3),g(4)=1,3,7,23,59,
\]
and their Theorem 23 supplies a general, explicitly non-optimal upper bound. Their following remark states that improving the bounds for \(g(p)\) would be interesting and points to OEIS A332866.

The current OEIS entry A332866 still lists only
\[
1,3,7,23,59
\]
and marks the sequence as needing more terms. Thus \(142\) is the first value immediately beyond the published exact table and the current database table.

A later paper on the number of possible period sets studies unrestricted period-set enumeration and asymptotics; its stated scope does not impose squarefreeness and does not determine this extremal ternary value.

## Limitations
The result determines only the next exact value \(g(5)\). It does not give a closed formula or asymptotic estimate for \(g(p)\) as \(p\) grows. The four normalized length-\(142\) minimizers are certified by the verifier, but no structural classification of minimizers for all \(p\) is claimed.

An unindexed computation or thesis could contain the same sixth value under different terminology; targeted database and literature searches did not locate one.

## References
1. D. Gabrić, N. Rampersad, and J. Shallit, “An inequality for the number of periods in a word,” arXiv:2005.11718, first public version 2020-05-24; International Journal of Foundations of Computer Science 32 (2021), 597–614, DOI 10.1142/S0129054121410094.
2. OEIS A332866, “Length of shortest ternary squarefree word having n periods,” current entry inspected in 2026.
3. E. Rivals, M. Sweering, and P. Wang, “Convergence of the Number of Period Sets in Strings,” ICALP 2023, DOI 10.4230/LIPIcs.ICALP.2023.100.
