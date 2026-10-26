# Cut-robust universality of binary circular words: a Lucas enumeration

## Finding

For a finite binary word \(w=w_0\cdots w_{n-1}\) of length \(n\ge1\), let \(\iota(w)\) be the largest \(k\ge0\) for which every binary string of length \(k\) occurs as a scattered subsequence of \(w\). Let \(\rho_j(w)=w_j\cdots w_{n-1}w_0\cdots w_{j-1}\), \(\zeta(w)=\max_j\iota(\rho_j(w))\), and \(\eta(w)=\min_j\iota(\rho_j(w))\). Call \(w\) *cut-robust* when \(\eta(w)=\zeta(w)\), so its subsequence-universality index is independent of the origin chosen on the circular word.

Define the cyclic transition indicator \(t_i=1\) when \(w_i\ne w_{i+1\bmod n}\), and \(t_i=0\) otherwise. If \(t\) contains a zero, let \(\ell_1,\ldots,\ell_s\) be the lengths of its maximal cyclic runs of ones. If \(t\) has no zeros, necessarily \(n\) is even and \(w\) is alternating.

**Structural classification.** A word is cut-robust if and only if either its transition indicator is all ones, or every maximal cyclic run of ones has even length. More precisely, in the non-all-ones case exactly
\[
\sum_{j:\,\ell_j\text{ odd}}\frac{\ell_j+1}{2}
\]
choices of the cut edge yield \(\iota(\rho(w))=\zeta(w)-1\); all other cuts yield \(\zeta(w)\). In the all-ones case no cut loses an arch.

**Complete index-refined enumeration.** Let \(R_{n,k}\) be the number of indexed binary words of length \(n\ge1\) which are cut-robust and satisfy \(\zeta(w)=k\). Words are **not** identified modulo rotation. Then for every \(0\le k\le\lfloor n/2\rfloor\),
\[
\boxed{R_{n,k}=\frac{2n}{n-k}\binom{n-k}{k}-2\mathbf1_{\{n=2k,\ k\ge1\}}.}
\]
For all other \(k\), the count is zero. Consequently,
\[
\boxed{\sum_{n\ge1}\sum_{k\ge0}R_{n,k}z^nu^k
=\frac{2z(1+2uz)}{1-z-uz^2}-\frac{2uz^2}{1-uz^2}.}
\]
Writing \(L_0=2\), \(L_1=1\), and \(L_n=L_{n-1}+L_{n-2}\) for the Lucas sequence, the total number of cut-robust binary words is
\[
\boxed{R_n=2\bigl(L_n-\mathbf1_{\{2\mid n\}}\bigr).}
\]
For uniformly selected binary words, the cut-robust proportion is asymptotic to \(2(\varphi/2)^n\), where \(\varphi=(1+\sqrt5)/2\). In particular, the proportion decays exponentially.

## Assumptions and scope

The ambient alphabet is the fixed binary set \(\{0,1\}\); hence constant words have universality index zero. Every length \(n\ge1\) is included, including the degenerate circular lengths one and two. A *cut edge* is any indexed cyclic adjacency, including the wrap-around adjacency. Cutting immediately after an index produces a linear rotation of the same cyclic word. Different indexed words and cut indices are counted separately, even if two rotations coincide as strings. The formula is not asserted for larger alphabets, nor for consecutive factors instead of scattered subsequences.

## Proof

**1. Binary arch/matching correspondence.** For a finite binary word \(v\), the greedy arch factorization repeatedly takes the shortest remaining prefix containing both letters. A standard property of this factorization is that its number of arches equals \(\iota(v)\): any word of length \(k\) can select its required letters, one per arch, whereas greediness witnesses the failure of \((k+1)\)-universality after \(k\) complete arches. Each binary arch contains an adjacent unequal pair. Different arches occupy disjoint intervals; choosing one unequal pair inside each gives pairwise vertex-disjoint edges. Conversely, \(k\) disjoint unequal adjacent pairs can be selected in increasing order, one letter per pair for any prescribed length-\(k\) binary subsequence; equivalently, each pair is a two-letter full-support block. Thus \(\iota(v)\) equals the matching number of the subgraph of the path on positions of \(v\) containing exactly the edges joining unequal adjacent letters. No assertion of this kind is made for larger alphabets.

**2. Analyze all circular cuts.** Form the cycle graph on the \(n\) indexed positions with exactly the cyclic edges \(t_i=1\). For \(n=2\) interpret the two cyclic adjacencies as separate indexed edges. Its maximum matching has an unused cut edge, so the greatest matching number after deletion of one cyclic edge equals the matching number of the full graph. If there is at least one zero in \(t\), its edge components are paths of lengths \(\ell_1,\ldots,\ell_s\) (measured in edges), with matching number
\[
\zeta(w)=\sum_{j=1}^{s}\left\lceil\frac{\ell_j}{2}\right\rceil.
\]
Removing a zero edge changes nothing. Within a run of \(\ell\) unequal edges, enumerate its edges \(1,\ldots,\ell\). Removing edge \(j\) leaves two path components with \(j-1\) and \(\ell-j\) edges, hence changes that component's matching number from \(\lceil\ell/2\rceil\) to
\[
\left\lceil\frac{j-1}{2}\right\rceil+\left\lceil\frac{\ell-j}{2}\right\rceil.
\]
For even \(\ell\), this is unchanged at every \(j\). For odd \(\ell\), it drops by one exactly at odd-numbered \(j\), of which there are \((\ell+1)/2\). This proves the cut-loss formula and the even-run characterization. If every cyclic adjacency is unequal, binary alternation requires even \(n\), and the resulting path after any cut has \(n-1\) unequal edges, with matching number \(n/2\); no cut loses an arch. If all adjacencies are equal, the index is zero at every cut.

**3. Encode robust words by a weighted circular tiling.** The cyclic transition indicators satisfy \(\bigoplus_{i=0}^{n-1}t_i=0\). Conversely, an arbitrary binary circular transition indicator of even parity determines exactly two original indexed words, according to the choice of their first letter. An indicator containing a zero and having only even-length runs of ones has a unique circular tiling in which each zero is a monomer and each consecutive pair of ones is a dimer. An all-ones indicator of even length has exactly two such tilings. Every dimer contributes one unit to \(\zeta(w)\), including in the all-ones case.

Let
\[
A(u)=\begin{pmatrix}1&1\\u&0\end{pmatrix}.
\]
The standard two-state circular monomer/dimer transfer calculation gives the weight polynomial of these indexed circular tilings as \(\operatorname{tr}(A(u)^n)\), the coefficient of \(u^k\) marking \(k\) dimers. Correcting the twofold tiling of the all-ones indicator, and then choosing the original word's first letter, yields the exact identity
\[
\sum_kR_{n,k}u^k=2\operatorname{tr}(A(u)^n)-2\mathbf1_{\{2\mid n\}}u^{n/2}\qquad(n\ge1).
\]
This also holds at \(n=1,2\) directly.

**4. Evaluate the transfer matrix.** The matrix characteristic polynomial is \(\lambda^2-\lambda-u\). Hence, for \(n\ge1\),
\[
\sum_{n\ge1}\operatorname{tr}(A(u)^n)z^n
=-z\frac{d}{dz}\log\det(I-zA(u))
=\frac{z(1+2uz)}{1-z-uz^2}.
\]
Equivalently,
\[
\operatorname{tr}(A(u)^n)
=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n}{n-k}\binom{n-k}{k}u^k.
\]
Subtracting the alternating-tiling correction gives the coefficient formula and the bivariate generating function. At \(u=1\), the trace obeys the Lucas recurrence with initial values \(2,1\), giving \(R_n\). Finally, \(L_n=\varphi^n+((1-\sqrt5)/2)^n\); division by the \(2^n\) possible indexed binary words proves the stated asymptotic proportion.

## Verification

The included `verify.py` independently computes every cyclic rotation's binary universality index by greedy arches for all indexed binary words of lengths \(1\) through \(18\), totaling \(524286\) words. It checks each cut-loss count, the complete structural criterion, the \(R_{n,k}\) binomial identity, the Lucas totals, and an independently propagated two-state weighted transfer recurrence. For lengths \(1\) through \(9\), it additionally constructs the actual sets of scattered subsequences and checks all rotation indices without relying on arch/matching theory. The run completed with `VERIFY_OK`. The theorem for unbounded \(n\) is proved above; finite testing alone is not its proof.

To replay using standard Python 3, run `python verify.py` in a directory containing this file and `verify.py`. The script requires no third-party modules.

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea and Nowotka introduced subsequence and circular subsequence universality and proved the one-arch bound relating a word to its best circular rotation (2020, Lemma 20). Fleischmann, Germann and Nowotka developed the arch-remainder theory for circular universality (2021). Schnoebelen and Veron gave an arch-jumping treatment, including the bound between universality indices of two conjugates (2023, Lemma 3.4), and algorithms for circular universality. Their cited bounds and algorithms do not state the all-cuts binary transition-run criterion or the complete index-refined Lucas enumeration here. The counting coefficients themselves are classical Lucas/matching-polynomial quantities; originality is claimed only for their identification with cut-robust subsequence universality and the exact bad-cut interpretation, not for Lucas numbers or matching polynomials.

## Limitations

The result is specifically for the binary alphabet and arbitrary *linear cut positions* of a fixed circular word. The complete-index distribution of arbitrary binary circular words and general arch-factorization inequalities are related established results, not claimed anew. The asymptotic statement concerns uniformly selected indexed words, not uniformly selected necklaces. The primary literature comparison is limited to inspected public works and available result records; a previously unlocated equivalent statement remains possible. No independent audit of these proofs or computations has been performed.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, first public March 10, 2020, especially Section 4 and Lemma 20. https://arxiv.org/abs/2003.04629
2. P. Fleischmann, S. B. Germann and D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, arXiv:2104.09063v1, first public April 19, 2021, Sections 3–4. https://arxiv.org/abs/2104.09063
3. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1, first public April 24, 2023, Sections 3–4 and Lemma 3.4. https://arxiv.org/abs/2304.11932
4. OEIS Foundation, *A000032: Lucas numbers*, including the classical cycle-matching interpretation. https://oeis.org/A000032
