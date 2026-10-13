# Second generalized Hamming weight of the new \([184,21,72]\) code
## Finding
Let \(C\) be the explicit binary quasi-cyclic code of length \(184\), dimension \(21\), and minimum distance \(72\) specified in the appendix of Seddas--Shashkov--Viazovska--Abbe, arXiv:2609.37056v1. Then
\[
d_2(C)=108.
\]
Moreover, exactly \(582{,}811\) two-dimensional subcodes \(D\le C\) satisfy \(|\operatorname{Supp}(D)|=108\). For every such \(D\), all three nonzero words of \(D\) have Hamming weight \(72\).

## Assumptions and scope
For a binary linear code \(C\), the second generalized Hamming weight is
\[
d_2(C)=\min_{\substack{D\le C\\ \dim D=2}} |\operatorname{Supp}(D)|,
\]
where \(\operatorname{Supp}(D)\) is the union of the coordinate supports of the words in \(D\).

The calculation concerns the specific published code, not every binary code with the same parameters. To reproduce the code, work in
\[
R=\mathbb F_2[x]/(x^{85}-1).
\]
The source specifies
\[
h=(x+1)(x^4+x^3+x^2+x+1)
(x^8+x^6+x^5+x^4+x^2+x+1)
(x^8+x^7+x^5+x^4+x^3+x^2+1),
\]
\(g=(x^{85}-1)/h\), and
\[
f_2=x^{13}+x^9+x^8+x^7+x^6+x^5+x^3+x+1.
\]
For \(\deg b<21\), the first \(170\) coordinates are the coefficients of \((bg,bgf_2)\) in \(R^2\). The final \(14\) coordinates are obtained from \(b\bmod(x^5-1)\) using the source's binary patterns
\[
11001,\ 01001,\ 00101,\ 11101,\ 11110,\ 00111,\ 11100,\ 01010,\ 10010,\ 10001,\ 11111,\ 01110,\ 10011,\ 00110.
\]
The accompanying verifier implements this description directly.

## Proof
Let \(D=\langle u,v\rangle\) be any two-dimensional binary subcode of \(C\). Its three nonzero words are \(u\), \(v\), and \(u+v\). At every coordinate belonging to \(\operatorname{Supp}(D)\), exactly two of these three words have a \(1\). Therefore
\[
2|\operatorname{Supp}(D)|
=\operatorname{wt}(u)+\operatorname{wt}(v)+\operatorname{wt}(u+v).
\]
Since the published code has minimum distance \(72\),
\[
|\operatorname{Supp}(D)|\ge \frac{3\cdot72}{2}=108.
\]

The exhaustive reconstruction described below finds minimum words corresponding to messages \(0x63\), \(0x318\), and \(0x37b\), with
\[
0x63\mathbin{\operatorname{xor}}0x318=0x37b.
\]
All three associated codewords have weight \(72\), and their union support has size \(108\). Hence \(d_2(C)\le108\), so the lower bound is sharp.

Equality \(|\operatorname{Supp}(D)|=108\) holds if and only if all three nonzero words of \(D\) have weight \(72\): the displayed support identity gives total weight \(216\), and each nonzero word has weight at least \(72\). Thus it remains only to count additive triples inside the minimum shell. Exhaustive enumeration gives \(1{,}748{,}433\) unordered pairs \(\{u,v\}\) of distinct weight-\(72\) words for which \(u+v\) also has weight \(72\). Each two-dimensional binary subcode has exactly three unordered pairs among its three nonzero words, so the exact number of minimizing subcodes is
\[
\frac{1{,}748{,}433}{3}=582{,}811.
\]

## Verification
The standalone verifier reconstructs the \(21\) generator rows from the polynomial and tail data above, checks their binary rank, enumerates all \(2^{21}\) messages, and independently recovers minimum distance \(72\) with exactly \(9{,}826\) minimum words. It then checks all
\[
\binom{9826}{2}=48{,}270{,}225
\]
unordered pairs of minimum words for closure under addition. The exact count is \(1{,}748{,}433\), and the explicit three-message witness has union support \(108\).

The finite computation is exhaustive for this finite code. The proof of the universal lower bound is symbolic and does not rely on sampling.

## Relationship to prior work
The source paper supplies the quasi-cyclic construction, proves the code has parameters \([184,21,72]\), and reports \(9{,}826\) minimum-weight words. Its manuscript does not state the second generalized Hamming weight or the additive-triple count above. The new statement is not implied by the ordinary minimum distance or by the number of minimum words alone: it uses the incidence of the minimum shell under vector addition.

Generalized Hamming weights are standard support invariants of linear codes; here the first higher weight attains the sharp binary support lower bound forced by \(d_1(C)=72\). The multiplicity \(582{,}811\) records how abundantly that extremal support size occurs.

## Limitations
The result is for this single explicitly specified code and does not classify the higher generalized Hamming weights \(d_r(C)\) for \(r\ge3\). It also does not assert that every \([184,21,72]\) code has the same value or multiplicity. An unindexed supplementary computation could independently contain the same invariant; no such statement was found in the inspected manuscript or targeted literature/index searches.

## References
1. M. Seddas, N. Shashkov, M. Viazovska, and E. Abbe, *Evolving Towards Better Codes: LLM-Guided Search for High-Distance Binary Linear Codes*, arXiv:2609.37056v1, 2026.
2. V. K. Wei, *Generalized Hamming Weights for Linear Codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
