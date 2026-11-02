# Exact ternary ordered-bigram multispectrum counts and the degree-six law

## Finding

Write \(\Sigma=\{0,1,2\}\). For an integer \(m\geq 1\), let \(T_m\) be the number of distinct nine-entry vectors
\[
\mathbf c(w)=(c_{ij}(w))_{i,j\in\Sigma},\qquad
c_{ij}(w)=|\{t:1\leq t\leq m,\ (w_t,w_{t+1})=(i,j)\}|,
\]
realized by words \(w\in\Sigma^{m+1}\). Thus \(\mathbf c(w)\) retains the full multiset, not merely the set, of overlapping ordered length-two factors.

The exact generating function, valid as a formal power series, is
\[
\boxed{\displaystyle
\sum_{m\geq1}T_m z^m=\frac{z\bigl(9-12z+5z^2+19z^3-4z^4-10z^5-14z^6+14z^7+6z^8-9z^9+3z^{10}\bigr)}{(1-z)^7(1+z)^2(1+z+z^2)}.}
\]
The first eleven values \(T_1,\ldots,T_{11}\) are \(9,24,65,156,342,683,1272,2226,3708,5919,9120\). Moreover \(T_m\) is a degree-six quasipolynomial with period dividing six for all \(m\geq1\), and
\[
\boxed{\displaystyle T_m=\frac7{8640}m^6+O(m^5).}
\]
For a lossless readout that reports only this ordered-bigram multiset, the maximum number of length-\(m+1\) input words perfectly distinguishable by a single read equals \(T_m\).

## Assumptions and scope

All factors are contiguous, overlapping, *ordered*, and counted with multiplicity. The alphabet is exactly three labeled symbols; a word may omit one or two symbols. The parameter \(m\) is the number of adjacent pairs, so the source word has length \(m+1\). At source length one there is one empty multiset (that exceptional length is excluded from the displayed series). The asymptotic holds as \(m\to\infty\). The code-size interpretation assumes noiseless observation of the entire nine-component vector, with no other side information.

## Proof

**1. Eulerian characterization.** Interpret a nonnegative integer matrix \((c_{ij})\) with total weight \(m\) as a directed multigraph on the labeled vertices \(\Sigma\), with \(c_{ij}\) copies of the arc \(i\to j\). A source word is exactly an Eulerian trail through all these arcs. Such a trail exists if and only if the vertices incident with positive-weight arcs induce one weakly connected component, and the degree differences \(d_i^+-d_i^-\) are either all zero or consist of one \(+1\), one \(-1\), and one zero. This is the standard directed Euler-trail criterion; it follows by adjoining an arc from end to start in the unbalanced case and applying the Euler-circuit construction. Thus the balanced and six ordered unbalanced classes are disjoint.

**2. Balanced matrices.** Put
\[
\delta_{01}=c_{01}-c_{10},\quad
\delta_{12}=c_{12}-c_{21},\quad
\delta_{20}=c_{20}-c_{02}.
\]
Degree balance is equivalent to \(\delta_{01}=\delta_{12}=\delta_{20}=t\) for some \(t\in\mathbb Z\). Each of the three unordered off-diagonal pairs contributes an independently selectable common number of opposite arcs, with generating function \((1-z^2)^{-1}\). Diagonal loops contribute \((1-z)^{-3}\). If \(t\ne0\), the positive arcs contain a directed triangle; hence connectivity is automatic and the extra cost is \(3|t|\), with total contribution \(2z^3/(1-z^3)\).

If \(t=0\), each off-diagonal pair is bidirected. The connected possibilities are exactly: a single occupied vertex carrying at least one loop; two occupied vertices joined by a positive opposite-arc pair (and arbitrary loops at these two vertices); or all three vertices joined by at least two of the three available opposite-arc pairs. Summing the respective series gives
\[
3\frac{z}{1-z}+3\frac{z^2}{(1-z)^2(1-z^2)}
+\frac{z^4(3-2z^2)}{(1-z)^3(1-z^2)^3}.
\]
Consequently the balanced profile enumerator is
\[
A(z)=3\frac{z}{1-z}+3\frac{z^2}{(1-z)^2(1-z^2)}
+\frac{z^4(3-2z^2)+2z^3/(1-z^3)}{(1-z)^3(1-z^2)^3}.
\]

**3. Unbalanced matrices.** Fix the ordered start vertex \(0\) and end vertex \(1\). The degree conditions become \(\delta_{01}=t+1\) and \(\delta_{12}=\delta_{20}=t\). For every integer \(t\), freely inserted opposite-arc pairs and loops contribute the denominator \((1-z)^3(1-z^2)^3\), and the forced unpaired-arc cost is \(|t+1|+2|t|\). Summing over \(t\ge0\) and \(t\le-1\) yields
\[
F(z)=\frac{z+z^2}{(1-z)^3(1-z^2)^3(1-z^3)}.
\]
This counts degree-correct matrices whether or not connected. If \(t\ge1\), the directed triangle is present; if \(t\le-1\), the forced arcs include a path from vertex \(0\) to vertex \(1\) through vertex \(2\). Both cases connect all occupied vertices. For \(t=0\), the mandatory \(0\to1\) arc joins vertices \(0,1\); vertex \(2\) is disconnected precisely when all four arcs incident with it and another vertex vanish but its self-loop count is positive. This forbidden family contributes
\[
B(z)=\frac{z^2}{(1-z)^3(1-z^2)}.
\]
Thus each fixed ordered endpoint pair contributes \(F(z)-B(z)\), and all six ordered endpoint pairs contribute \(6(F(z)-B(z))\) by relabeling. By the Eulerian characterization,
\[
\sum_{m\ge1}T_mz^m=A(z)+6(F(z)-B(z)).
\]
Taking a common denominator and canceling factors gives the boxed rational generating function.

**4. Growth and interpretation.** The only pole of order seven is at \(z=1\); the numerator after extracting the factor \(z\) evaluates to \(7\) there, and \((1+z)^2(1+z+z^2)\) equals \(12\). Its coefficient contribution is \((7/12)\binom{m+6}{6}\), with leading term \(7m^6/8640\). The remaining poles have orders at most two and occur at roots of unity of orders two and three, so the coefficient sequence is a degree-six quasipolynomial of period dividing six and the stated error term follows. Every realizable profile has at least one representative word and different profiles are distinguishable; conversely two words with one profile cannot be distinguished by that observation. Selecting one representative for each profile proves the exact zero-error code-size assertion.

## Verification

The standalone Python program `verify_ternary_profiles.py` computes the rational generating-function coefficients by exact integer recurrence, independently enumerates every ternary source word at lengths \(2\) through \(11\), and independently enumerates every nonnegative three-by-three arc-count matrix of degrees \(1\) through \(10\) to apply the directed Eulerian criterion. At every checked size the sets and coefficient counts agree exactly. It also checks the first eleven coefficients and the exceptional source length one. Run `python3 verify_ternary_profiles.py` in the directory containing this document. Its successful output begins `VERIFY_OK` and reports `literal_words=265716` and `sum_distinct_profiles=14404`. These finite tests corroborate the algebra but do not substitute for the all-length proof.

## Relationship to prior work

General reconstruction from substring spectra and the Eulerian graph correspondence are established tools. Marcovich and Yaakobi's *Reconstruction of Strings from their Substrings Spectrum* treats substring-spectrum reconstruction; Yehezkeally, Marcovich, and Yaakobi's *Multi-strand Reconstruction from Substrings* studies reconstruction constraints. Bernardini, Conte, Gabory and coauthors' *On Strings Having the Same Length-\(k\) Substrings* analyzes equality of substring **sets** and graph structure; equality of sets is not equality of multisets. The present statement enumerates every realizable **ternary multiset** of overlapping ordered bigrams at every length, and gives a complete rational enumerator. A known exact **binary** bigram-multispectrum enumeration has a different alphabet domain and does not imply the ternary formula.

## Limitations

The result does not enumerate preimage sizes of individual spectra, noisy or incomplete readout, nonoverlapping bigrams, higher-order substrings, or alphabets of size four and above. Literature-search nonappearance does not prove global novelty; an equivalent derivation may exist in enumerations of integer Eulerian flows, directed lattice walks, or multigraph degree sequences. The leading constant concerns labeled ternary symbols and full ordered-bigram multiplicities only. Independent mathematical validation has not yet been performed.

## References

1. A. Marcovich and E. Yaakobi, *Reconstruction of Strings from their Substrings Spectrum*, arXiv:1912.11108 (first public 2019-12-23), https://arxiv.org/abs/1912.11108.
2. Y. Yehezkeally, A. Marcovich, and E. Yaakobi, *Multi-strand Reconstruction from Substrings*, arXiv:2108.11725 (first public 2021-08-26), https://arxiv.org/abs/2108.11725.
3. G. Bernardini, A. Conte, G. Gabory, et al., *On Strings Having the Same Length-\(k\) Substrings*, 2022 conference contribution and expanded journal treatment, https://link.springer.com/article/10.1007/s00224-025-10240-z.
