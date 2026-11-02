# Complete Lyndon-factor and occurrence spectra of finite Zimin words

## Finding

Let \(a_1<a_2<\cdots<a_n\) be distinct symbols in that order, and define \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\) for every integer \(n\geq1\). A *Lyndon word* is a nonempty word strictly lexicographically smaller than every nonempty proper suffix. A *Lyndon factor* means a contiguous factor that is a Lyndon word; different occurrences of the same factor count once in the distinct-factor spectrum.

**Theorem (complete factor and endpoint classification).** For every integer \(n\geq1\), all the distinct Lyndon factors of \(Z_n\) are precisely
\[
\mathcal L(Z_n)=\{Z_{i-1}a_j:1\leq i\leq j\leq n\}.
\]
More sharply, number the positions of \(Z_n\) from \(1\) through \(2^n-1\). At position \(p\), put \(j=1+\nu_2(p)\), where \(\nu_2(p)\) is the exponent of \(2\) dividing \(p\). The complete list of Lyndon factors **ending at that particular position** is
\[
Z_0a_j,\ Z_1a_j,\ \ldots,\ Z_{j-1}a_j.
\]
Their lengths are exactly \(1,2,4,\ldots,2^{j-1}\), and there are exactly \(j\) of them.

Therefore the number of distinct Lyndon factors is \(n(n+1)/2\). For every \(1\leq i\leq n\), exactly \(n-i+1\) distinct ones have length \(2^{i-1}\), and the total number of *occurrences* of Lyndon factors of that length is \(2^{n-i+1}-1\). There are no Lyndon factors of other lengths. The total number of Lyndon-factor occurrences, over all lengths and positions, is
\[
2^{n+1}-n-2.
\]
As a further consequence, the Chen–Fox–Lyndon factorization of \(Z_n\) is the nonincreasing product
\[
(Z_{n-1}a_n)(Z_{n-2}a_{n-1})\cdots(Z_1a_2)(Z_0a_1).
\]

## Assumptions and scope

The alphabet is rank-dependent, finite, and *strictly ordered* \(a_1<a_2<\cdots<a_n\). Lexicographic comparison uses the ordinary convention that a proper prefix is smaller than the whole word. Factors are literal contiguous substrings; the symbols are not variables being substituted by arbitrary words. The theorem includes \(n=1\), uses one-based endpoints, and counts all occurrences with multiplicity only in the occurrence formulas. It makes no claim for reordered alphabets, arbitrary images of Zimin patterns, or subsequences.

## Proof

**Step 1 (ruler representation and desubstitution).** Induction in the defining recursion gives the letter at position \(p\) of \(Z_n\) as \(a_{1+\nu_2(p)}\) for \(1\leq p<2^n\). In particular, all odd positions carry \(a_1\); all even positions carry symbols strictly larger than \(a_1\). Define the lower-rank word \(V_{n-1}\) over \(a_2,\ldots,a_n\) as the corresponding copy of \(Z_{n-1}\) with every symbol index increased by one. Define the two-letter uniform coding \(\phi(a_j)=a_1a_j\) on those symbols. The ruler formula gives the exact identity
\[
Z_n=\phi(V_{n-1})a_1.
\]
In particular, every factor of \(Z_n\) that starts at an odd position and ends at an even position is \(\phi(u)\) for a nonempty contiguous factor \(u\) of \(V_{n-1}\), and conversely.

**Step 2 (rigidity of Lyndon factors).** A Lyndon factor of length greater than one cannot begin at an even position: its next symbol is \(a_1\), so its proper suffix beginning there is lexicographically smaller. It also cannot end at an odd position: its last symbol is \(a_1\), so its one-symbol proper suffix \(a_1\) is smaller than the whole factor, which begins at \(a_1\). Hence all nonsingleton Lyndon factors are exactly the aligned factors \(\phi(u)\) from Step 1 that satisfy the Lyndon property.

For any nonempty word \(u\) on \(a_2,\ldots,a_n\), \(\phi(u)\) is Lyndon if and only if \(u\) is Lyndon. Indeed, a proper suffix of \(\phi(u)\) starting in an even position begins with a letter greater than \(a_1\), so is automatically larger than \(\phi(u)\). A suffix starting at an odd position is \(\phi(v)\) for a proper nonempty suffix \(v\) of \(u\). Since the constant-length injective coding \(\phi\) preserves and reflects lexicographic comparisons (including the proper-prefix case), \(\phi(u)<\phi(v)\) holds exactly when \(u<v\). Thus
\[
\mathcal L(Z_n)=\{a_1,\ldots,a_n\}\ \cup\ \phi(\mathcal L(V_{n-1})),
\]
where the union is disjoint by length.

**Step 3 (solve the recursion).** For rank one, the only Lyndon factor is \(a_1=Z_0a_1\). Under an increase of all letter indices by one, the induction hypothesis describes the Lyndon factors of \(V_{n-1}\) as \(Z_{i-2}^{+}a_j\) with \(2\leq i\leq j\leq n\), where \(Z_{i-2}^{+}\) means \(Z_{i-2}\) with all indices increased by one. The ruler identity applied at rank \(i-1\) says \(\phi(Z_{i-2}^{+})a_1=Z_{i-1}\), so
\[
\phi(Z_{i-2}^{+}a_j)=Z_{i-1}a_j.
\]
Together with the singleton factors \(Z_0a_j=a_j\), this establishes the complete distinct-factor formula without omitted lengths. For each \(i\), the possible \(j\)'s are exactly \(i,i+1,\ldots,n\), and different pairs \((i,j)\) give different words because their lengths or final letters differ.

**Step 4 (one-based endpoint classification).** A symbol \(a_j\) occurs exactly at positions \(p\) with \(\nu_2(p)=j-1\), and there are \(2^{n-j}\) of these positions. At each such position, the immediately preceding \(2^{j-1}-1\) symbols form \(Z_{j-1}\): every occurrence of \(a_j\) is the center of a literal copy of \(Z_j\) in the recursive construction. Each \(Z_{j-1}\) ends with \(Z_{i-1}\) for \(i\leq j\). Thus every \(Z_{i-1}a_j\) (\(i\leq j\)) ends at *every* occurrence of \(a_j\). Conversely, Step 3 shows that a Lyndon factor ending at \(a_j\) must have one of precisely these forms. This proves the endpoint statement and its exact length list.

**Step 5 (enumeration).** Distinct factors at length \(2^{i-1}\) number \(n-i+1\). Summing over the rank yields \(\sum_{i=1}^n(n-i+1)=n(n+1)/2\). Counting factor occurrences of fixed length by their endpoint letters gives
\[
\sum_{j=i}^n 2^{n-j}=2^{n-i+1}-1.
\]
Summing by endpoint rank gives
\[
\sum_{j=1}^n j2^{n-j}=2^{n+1}-n-2,
\]
as claimed.

**Step 6 (ordinary Lyndon factorization).** Write \(H_j=Z_{j-1}a_j\). The definition gives \(Z_n=H_nZ_{n-1}=H_nH_{n-1}\cdots H_1\). Each \(H_j\) is Lyndon by Step 3, and \(H_{j-1}\) is a proper prefix of \(H_j\), so \(H_n>H_{n-1}>\cdots>H_1\) lexicographically. The uniqueness part of the Chen–Fox–Lyndon theorem identifies this as the canonical nonincreasing factorization.

## Verification

The accompanying standalone program `checker.py` constructs \(Z_n\) independently from its recursion, enumerates *every* contiguous factor ending at *every* position, and decides Lyndon status by direct comparison with every proper suffix. It compares the exact observed ending-factor sets against the formula, checks the distinct-factor and occurrence counts separately for every predicted length, and checks both the rank and total-count identities. Ranks \(1\) through \(9\) passed; the largest checked word has length \(511\). For ranks \(1\) through \(6\) it additionally checks the predicted Lyndon factors by a separate cyclic-rotation characterization. The full infinite-rank theorem is established by Steps 1–6, not by finite checks.

Run from the extracted package directory using `python checker.py`; it requires only the Python standard library.

## Relationship to prior work

Zimin words are classical unavoidable patterns. Głowinski and Rytter (2013, arXiv:1307.1560, Section 2) give an interleaving description of their factors and algorithms for compressed ranked pattern matching, not an explicit Lyndon-factor spectrum. Rytter and Shur (2014, arXiv:1409.8235, Sections 1–2) analyze Zimin-pattern embeddings and types, not Lyndon suffixes. Goc, Saari, and Shallit (2012, arXiv:1207.5124, Section 3) establish general \(k\)-regularity of Lyndon complexity for fixed-alphabet automatic sequences and give an explicit Thue–Morse length spectrum; that result does not provide the current rank-dependent Zimin classification. Badkobeh and Crochemore (2020 preprint, arXiv:2011.12742, Section 5) explicitly discuss **half Zimin words as Lyndon words**. Their observation covers the particular factors \(H_i=Z_{i-1}a_i\), which are therefore not individually asserted to be new. The present classification adds all factors \(Z_{i-1}a_j\) with \(i<j\), proves there are no others, and yields exact endpoint, length, and multiplicity spectra. Glen, Simpson, and Smyth (2017, arXiv:1701.00928) determine universal maximum and expected counts of Lyndon factors and give results for Christoffel words; the inspected scope does not give the full Zimin spectrum. A covering statement was not found in the inspected materials; historical priority is not independently certified.

## Limitations

The alphabet must have the designated increasing order, and the result is about literal finite Zimin words rather than homomorphic instances of Zimin patterns. The checker covers only finite ranks \(1\) to \(9\); it supplies no independent proof for all ranks. The observation that half Zimin words are Lyndon is already in the literature. It is possible that the full classification or an equivalent corollary appears elsewhere under ruler-sequence or Lyndon-suffix terminology; no claim of exhaustive historical priority is made. No independent mathematical audit has been performed.

## References

1. D. Goc, K. Saari, and J. Shallit, *Primitive Words and Lyndon Words in Automatic and Linearly Recurrent Sequences*, arXiv:1207.5124 (first posted 2012-07-21), especially Section 3. https://arxiv.org/abs/1207.5124
2. R. Głowinski and W. Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, arXiv:1307.1560 (first posted 2013-07-05), especially Sections 1–2. https://arxiv.org/abs/1307.1560
3. W. Rytter and A. M. Shur, *On Searching Zimin Patterns*, arXiv:1409.8235 (first posted 2014-09-29), especially Sections 1–2; explicitly classified under 68R15. https://arxiv.org/abs/1409.8235
4. G. Badkobeh and M. Crochemore, *Left Lyndon tree construction*, arXiv:2011.12742 (first posted 2020-11-25), Section 5, discussion of half Zimin words. https://arxiv.org/abs/2011.12742
5. J.-P. Duval, *Factorizing words over an ordered alphabet*, Journal of Algorithms 4 (1983), 363–381, for the classical nonincreasing Lyndon factorization.
6. A. Glen, J. Simpson, and W. F. Smyth, *Counting Lyndon factors*, arXiv:1701.00928 (first posted 2017-01-04), especially the abstract and introduction. https://arxiv.org/abs/1701.00928
