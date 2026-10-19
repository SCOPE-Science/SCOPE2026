# Four-valued shortest-absent-subsequence law for period-doubling prefixes

## Finding

Let \(p=p_0p_1\cdots\) be the binary fixed point beginning in \(0\) of \(\sigma(0)=01\), \(\sigma(1)=00\), and let \(W_n=p_0\cdots p_{n-1}\) for each integer \(n\ge1\). A shortest absent subsequence (SAS) is a shortest binary word that cannot be read in order (not necessarily contiguously) from \(W_n\). Put
\[
r_n=|W_n|_1=\sum_{j=1}^n [\nu_2(j)\equiv1\pmod2].
\]
Here \(\nu_2(j)\) is the exponent of \(2\) dividing the positive integer \(j\), and brackets denote an indicator.

**Theorem.** Every SAS of \(W_n\) has length \(r_n+1\) and is of the form \(1^a0^{r_n+1-a}\). At \(n=2\), the complete set is \(\{00,10,11\}\). At all other \(n\ge1\), define \(\ell_n\) by
\[
\ell_n=\begin{cases}
-1,&n\text{ odd, or }4\mid n\text{ and }\nu_2(n)\text{ even},\\
1,&4\mid n\text{ and }\nu_2(n)\text{ odd},\\
2,&n\equiv2\pmod4,\ n>2,\ \nu_2(n-2)\text{ odd},\\
0,&n\equiv2\pmod4,\ n>2,\ \nu_2(n-2)\text{ even}.
\end{cases}
\]
Then, with the second set empty when \(\ell_n=-1\),
\[
\mathrm{SAS}(W_n)=\{1^{r_n+1}\}\cup
\{1^{r_n-j}0^{j+1}:0\le j\le\ell_n\}.
\]
Thus, for every \(n\ge1\), \(1\le |\mathrm{SAS}(W_n)|\le4\). The four count classes have exact natural densities
\[
\lim_{N\to\infty}\frac{\#\{1\le n\le N:|\mathrm{SAS}(W_n)|=k\}}N
=\begin{cases}2/3,&k=1,\\1/6,&k=2,\\1/12,&k=3,\\1/12,&k=4.\end{cases}
\]

## Assumptions and scope

The alphabet is the fixed, labeled binary alphabet \(\{0,1\}\), including the one-letter prefix \(W_1=0\). Subsequence positions strictly increase; a subsequence need not be contiguous. All statements concern prefixes beginning at index zero of this particular fixed point, not arbitrary factors, alternate codings, or other substitutions. The displayed densities count positive prefix lengths, not randomly chosen words. For \(n=2\) the valuation \(\nu_2(n-2)\) is undefined; its separate case is essential.

## Proof

**Step 1: valuation representation and arches.** The substitution gives \(p_{2i}=0\) and \(p_{2i+1}=1-p_i\). Since \(\nu_2(2i+1)=0\) and \(\nu_2(2i+2)=1+\nu_2(i+1)\), induction proves
\[p_i\equiv\nu_2(i+1)\pmod2.\]
In particular, every \(1\) occurs at an odd index and is immediately preceded by a \(0\). Therefore \(W_n\) contains the word \((01)^{r_n}\) as a scattered subsequence, using each \(1\) with the zero immediately before it. Every binary word of length \(r_n\) is a subsequence of \((01)^{r_n}\), by taking one required symbol from each pair, whereas \(1^{r_n+1}\) is absent from \(W_n\). The shortest absent length is therefore exactly \(r_n+1\), including \(r_n=0\).

**Step 2: reduce all possible shortest absences to monotone words.** Any binary word of length \(r_n+1\) which is not of the form \(1^a0^{r_n+1-a}\) contains the adjacent pattern \(01\). Merge one such adjacent pair into a single block, leaving the other letters singleton blocks. This partitions the word into exactly \(r_n\) blocks, each of which embeds in \(01\). The whole word consequently embeds in \((01)^{r_n}\) and hence \(W_n\). Thus only the displayed monotone patterns can be absent.

**Step 3: a general suffix criterion.** Write the zeros preceding the successive ones and those following the last one as
\[
W_n=0^{g_1}1\,0^{g_2}1\cdots0^{g_{r_n}}1\,0^b,
\]
where every \(g_i\ge1\) and \(b\ge0\); when \(r_n=0\), the word is \(0^b\). The pattern \(1^a0^{r_n+1-a}\) embeds if and only if at least \(r_n+1-a\) zeros remain after choosing the first \(a\) ones (when \(a=0\), all zeros are available). Choosing the earliest ones maximizes the remaining zeros. Since each remaining one has at least one preceding zero, for \(0\le a\le r_n\) absence is equivalent to \(b=0\) and \(g_{a+1}=\cdots=g_{r_n}=1\); the sequence of equalities is vacuous if \(a=r_n\). The pattern \(1^{r_n+1}\) is always absent. Thus if \(W_n\) ends in \(0\), the only SAS is \(1^{r_n+1}\). If it ends in \(1\), the extra SAS are precisely those with \(a=r_n-j\), \(0\le j\le\ell\), where \(\ell\) is the number of consecutive terminal blocks \(0^11\), counting the initial block if reached.

**Step 4: determine the terminal-run parameter arithmetically.** Since \(p_{n-1}\equiv\nu_2(n)\pmod2\), every odd \(n\) ends in \(0\), and a multiple of four ends in \(1\) exactly when \(\nu_2(n)\) is odd. Suppose first \(4\mid n\) and \(\nu_2(n)\) is odd. Necessarily \(n\ge8\). The preceding index \(n-3\equiv1\pmod4\) is a \(1\), but \(p_{n-5}=0\) since \(\nu_2(n-4)=2\); therefore exactly one terminal zero gap has length one, so \(\ell=1\).

Now let \(n\equiv2\pmod4\) and \(n>2\). The last symbol is always \(1\). The symbol at \(n-3\) is a \(1\) exactly when \(\nu_2(n-2)\) is odd. Otherwise the preceding \(1\) occurs at \(n-5\), and \(\ell=0\). In the first case \(p_{n-5}=1\), giving two successive terminal gaps of length one. There cannot be a third because \(\nu_2(n-6)=2\) whenever \(\nu_2(n-2)\) is odd: \((n-2)/4\) is then even whereas \((n-6)/4\) is odd. Hence \(p_{n-7}=0\) and \(\ell=2\). Directly \(W_2=01\), whose absent length-two subsequences are \(00,10,11\). This proves the full set classification and the universal bound of four.

**Step 5: densities.** The positive integers with exact \(2\)-adic valuation \(h\) have density \(2^{-h-1}\). The one-SAS class contains all odd lengths (density \(1/2\)) and lengths with even positive valuation at least two (density \(\sum_{j\ge1}2^{-2j-1}=1/6\)), totaling \(2/3\). The three-SAS class outside the single exceptional length \(2\) consists of valuation \(3,5,7,\ldots\), of density \(\sum_{j\ge1}2^{-2j-2}=1/12\). Among lengths \(n\equiv2\pmod4\) (density \(1/4\)), \(\nu_2(n-2)\) is odd on a conditional proportion \(1/3\); these have four SAS, density \(1/12\). The remaining lengths of that residue class have two SAS, density \(1/6\). Finite exceptions do not affect natural densities.

## Verification

The independent standard-library checker `verify.py` reconstructs the substitution fixed point and independently evaluates the valuation formula; it compares the classification against suffix-based subsequence tests on multiple finite prefixes, and exhaustively enumerates all subsequences for lengths through \(18\) as applicable. Run `python3 verify.py`. It reports `PASS` upon success. The finite checks are supplemental; Steps 1–5 are a proof for all positive lengths.

## Relationship to prior work

Kosche, Koß, Manea, and Siemer introduce and characterize shortest absent scattered subsequences and the universality-index/arch framework in a 2021 preprint (updated and published later). Their full accessible paper gives generic algorithms and extremal constructions, not the explicit period-doubling all-prefix four-valued law, its exact absent words, or its density constants. Existing work on period-doubling string attractors addresses **contiguous factors hitting selected positions**, not absence of order-preserving scattered subsequences. Results on maximal numbers of SAS over all binary words provide universal upper bounds but do not imply this automatic-prefix classification. No literature search proves novelty exhaustively; equivalent results under other terminology remain a risk.

## Limitations

The theorem concerns the specified fixed point and its prefixes, not all factors or generalized period-doubling substitutions. The asymptotic statements are natural densities of prefix lengths and do not give probabilities under a random-word model. Mathematical proof and finite replay are same-author/one-model checks; no independent audit has been performed. Novelty comparisons are limited to the inspected and located literature.

## References

1. Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, initially submitted 2021-08-31; full open-access version in *Fundamenta Informaticae* 189 (2023), DOI:10.46298/fi.9221, https://fi.episciences.org/12396/pdf.
2. Narad Rampersad and Manon Stipulanti, *The Formal Inverse of the Period-Doubling Sequence*, arXiv:1807.11899 (2018), for independent context on the classical sequence.
