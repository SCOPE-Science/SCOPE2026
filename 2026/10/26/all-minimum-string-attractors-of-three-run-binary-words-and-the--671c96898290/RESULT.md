# All minimum string attractors of three-run binary words and the mean–typical gap

## Finding

For every three-run binary word \(w=0^a1^b0^c\), where \(a,b,c\) are arbitrary positive integers, the minimum string-attractor size is exactly \(2\), and **all** minimum position sets are as follows (positions are indexed from \(1\)).

* If \(b=1\), select the unique central \(1\) at position \(a+1\) and **any** position in a longest run of zeros. When \(a=c\), either zero run is permitted.
* If \(b\ge2\), the only candidates are \(\{a,a+b\}\), which occurs exactly when \(a\ge c\), and \(\{a+1,a+b+1\}\), which occurs exactly when \(c\ge a\).

Thus, letting \(K(a,b,c)\) denote the number of smallest attractors,
\[
K(a,b,c)=\begin{cases}
\max(a,c)+a\mathbf1_{a=c},&b=1,\\
1+\mathbf1_{a=c},&b\ge2.
\end{cases}
\]
The full length enumerator of minimum attractors, counting distinct binary words beginning with zero, is
\[
F(z)=\sum_{a,b,c\ge1}K(a,b,c)z^{a+b+c}
=\frac{2z^3(1+2z+2z^2)}{(1-z)^3(1+z)^2}.
\]

Writing \(n\ge3\), exactly
\[
U_n=\binom{n-1}{2}-(n-2)-\left\lfloor\frac{n-2}{2}\right\rfloor
\]
of the \(\binom{n-1}{2}\) three-run binary words beginning with zero have a **unique** minimum attractor. Therefore the unique-minimum proportion tends to \(1\), but the **mean** number of minimum attractors tends to \(5/2\):
\[
\lim_{n\to\infty}\frac{U_n}{\binom{n-1}{2}}=1,
\qquad
\lim_{n\to\infty}\frac{[z^n]F(z)}{\binom{n-1}{2}}=\frac52.
\]
The same two limits hold if both initial binary symbols are allowed, by complementation.

## Assumptions and scope

A *factor* is a nonempty **contiguous** substring. An attractor for a finite word is a subset \(\Gamma\) of its positions such that every distinct nonempty factor has at least one occurrence whose index interval intersects \(\Gamma\). Distinct occurrences of the same factor may be used to satisfy the intersection condition. A *minimum* attractor has the smallest cardinality. Parameters \(a,b,c\) are positive integers, \(w\) is not cyclic, and different subsets of positions count separately. The aggregate enumerator counts three-run words starting with \(0\); reversal and alphabet-complement images need not be identified.

## Proof

**Minimum size.** Both letters occur in \(w\). A factor consisting of a single \(0\) and a factor consisting of a single \(1\) demand at least two distinct positions in any attractor. Existence of a two-position attractor follows from the cases below.

**Case \(b=1\).** The unique occurrence of the symbol \(1\) sits at \(a+1\), so any two-position attractor must contain that position to hit the one-letter factor \(1\). Every factor containing \(1\) therefore has an occurrence meeting this position. The longest all-zero factor is \(0^{\max(a,c)}\), whose occurrences lie precisely in the zero runs attaining the maximum, and a second position must lie in one of those runs. Conversely any selected position in such a longest run intersects an occurrence of every all-zero factor \(0^j\) with \(1\le j\le\max(a,c)\): choose an interval of length \(j\) within that run through the selected position. This proves the complete characterization and count for \(b=1\).

**Case \(b\ge2\).** Every two-position attractor consists of one zero position and one one position, because each singleton letter must be covered. The factor \(01\) has a unique occurrence on the first run boundary, at positions \(a,a+1\), and \(10\) has a unique occurrence on the second boundary, at positions \(a+b,a+b+1\). If the selected zero is in the initial zero run, then to cover \(10\) the one-position must be \(a+b\). Since \(b\ge2\), this one-position does not cover \(01\), so the zero-position must be \(a\). To cover \(0^{\max(a,c)}\), we then need \(a\ge c\). Conversely, when \(a\ge c\), \(\{a,a+b\}\) is an attractor: all-zero factors occur through \(a\), all-one factors occur through \(a+b\), factors of type \(0^i1^j\) cross \(a\), factors of type \(1^j0^k\) cross \(a+b\), and factors of type \(0^i1^b0^k\) cross both. These are every possible type of factor of a three-run word.

If the selected zero lies in the final zero run, covering \(01\) forces the selected one-position to be \(a+1\); covering \(10\) then forces the zero to be \(a+b+1\). The longest all-zero factor requires \(c\ge a\). Conversely, when \(c\ge a\), the pair \(\{a+1,a+b+1\}\) intersects occurrences of every factor by the same complete factor-type classification with the boundary roles exchanged. There are no remaining cases, which proves the full pair list.

**Generating function.** For \(b\ge2\), there are two possible boundary candidates, with total weight \(1+\mathbf1_{a=c}\); summing over parameters gives
\[
F_{\ge2}(z)=\frac{z^4}{(1-z)^3}+\frac{z^4}{(1-z)(1-z^2)}.
\]
For \(b=1\), the two longest-run directions contribute symmetrically. Splitting the equal-run case exactly once gives
\[
F_{=1}(z)=2z\!\sum_{a>c\ge1} a z^{a+c}
+2z\!\sum_{a\ge1}a z^{2a}
=\frac{2z^3}{(1-z)^3}-\frac{2z^4}{(1-z)(1-z^2)^2}.
\]
Indeed the second equality follows by summing geometric series and their derivatives. Adding these two rational expressions and simplifying yields the stated \(F(z)\). The number of length-\(n\) positive compositions into three parts is \(\binom{n-1}{2}\). Nonunique minimum attractors occur exactly when \(b=1\) (there are \(n-2\) such compositions) or when \(b\ge2\) and \(a=c\) (there are \(\lfloor(n-2)/2\rfloor\)), proving the formula for \(U_n\). Finally, the principal part of \(F(z)\) at \(z=1\) is \(\tfrac52(1-z)^{-3}\); its other pole is at \(z=-1\), of smaller order, so \([z^n]F(z)=\tfrac54 n^2+O(n)\). Division by \(\binom{n-1}{2}=\tfrac12 n^2+O(n)\) gives the mean limit.

## Verification

Run `python3 verify.py` from the directory containing this file. The independent implementation enumerates factors and their occurrence-position masks directly, then tests all position pairs. It checks every \((a,b,c)\in\{1,\ldots,14\}^3\) against the explicit pair formula and rejects singleton attractors. It also independently computes every enumerator coefficient for lengths \(3\) through \(40\) and counts unique minimizers. A successful run prints `VERIFY_OK exhaustive_triplets=2744 maximum_single_run=14 enumerator_coefficients=38 unique_counts=38`. Finite tests confirm implementation consistency but do not replace the all-parameter proof above.

## Relationship to prior work

The string-attractor concept and its general optimization and combinatorial theory precede this result. Mantaci, Restivo, Romana, Rosone and Sciortino (2019/2021) study string-attractor bounds and special families, including the two-run power case, but their inspected results do not give all optimum position-pairs of arbitrary positive three-run words or the aggregate enumerator. Banbara and collaborators (2026) determine numbers of smallest attractors for special morphic families, motivating minimum-attractor multiplicity as an invariant; the inspected results do not supply the present parameter-wide classification or the mean–typical separation. A general algorithm for per-word attractor verification does not, by itself, state an all-parameter formula. Earlier fixed-length binary censuses and results for four alternating runs classify different word domains; the fourth run is required and these do not directly imply the three-run count.

## Limitations

The classification covers exactly three contiguous runs over a binary alphabet and an ordinary noncyclic factor-attractor definition, not arbitrary runs, larger alphabets or the distribution over all binary words. The mean is over the uniform finite set of three-run words at each length, rather than over all binary strings or over a stochastic letter source. Other unindexed literature may contain an equivalent special case. Independent scientific validation has not been performed.

## References

- Mantaci, Restivo, Romana, Rosone and Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660, first public version 10 July 2019; later published in *Theoretical Computer Science* (2021).
- Kempa, Policriti, Prezza and Rotenberg, *String Attractors: Verification and Optimization*, arXiv:1803.01695, ESA 2018.
- Banbara et al., *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.33.
