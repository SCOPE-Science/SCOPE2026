# Complete size spectrum of reverse-complement-closed length-three non-overlapping codes

## Finding

Let \(\Sigma\) be a labeled alphabet of cardinality \(2h\), where \(h\geq1\), equipped with a fixed-point-free involution \(c:\Sigma\to\Sigma\). Write \(\rho(u,v,w)=(c(w),c(v),c(u))\). Let \(H_h(x)\) count every set \(C\subseteq\Sigma^3\) satisfying \(\rho(C)=C\) and the non-overlap condition, with weight \(x^{|C|}\); the empty code is included. The exact cardinality enumerator is

\[
H_h(x)=\sum_{a=0}^{h}(-1)^{h-a}\binom ha2^a
(1+x^2)^{a^2(h-a)}\left(2(1+x^2)^a-1\right)^{\binom a2}.
\]

As a consistency check with previously published extremal results, for \(h\geq2\) the largest code has exactly

\[
M_h=h^2(h-1)
\]

words, and there are precisely \(2^{h+\binom h2}\) distinct labeled maximum codes. Every maximum code arises uniquely by choosing one symbol from each complementary pair, orienting every edge of the resulting complete graph as a tournament, and taking all words specified in the proof. For \(h=1\), only the empty code exists, so \(H_1(x)=1\) and \(M_1=0\).

Examples are \(H_2(x)=1+12x^2+8x^4\) and

\[
H_3(x)=1+60x^2+726x^4+3072x^6+6276x^8+7344x^{10}
+5256x^{12}+2304x^{14}+576x^{16}+64x^{18}.
\]

## Assumptions and scope

A code is an ordinary set, not a multiset, of length-three words over \(\Sigma\). The non-overlap condition is that for **every ordered pair** \((u,v)\in C\times C\), including \(u=v\), neither the length-one nor length-two suffix of \(u\) is the corresponding prefix of \(v\). The complementary involution has no fixed letters. Codewords and codes are labeled; no quotient by alphabet permutations or word reversal is taken. The variable \(x\) is formal, so the polynomial identity is over \(\mathbb Z[x]\).

## Proof

**1. Endpoint sets.** Fix a non-overlapping \(\rho\)-closed code \(C\). Let \(A\) be the set of letters used in its first coordinate. Closure implies that its last-coordinate set is exactly \(B=c(A)\). Length-one non-overlap forces \(A\cap B=\varnothing\), so \(A\) uses at most one member of each complementary pair. Put \(a=|A|\leq h\), \(D=\Sigma\setminus(A\cup B)\), and \(|D|=2(h-a)\).

**2. A graph controlling all length-two overlaps.** Every codeword with middle coordinate in \(D\) is \((u,d,c(z))\), where \(u,z\in A\) and \(d\in D\). It belongs to a two-word \(\rho\)-orbit, and none of these orbits creates a length-two overlap with any other allowed orbit: their prefixes have second coordinate in \(D\), while their suffixes start in \(D\). There are exactly \(a^2(h-a)\) such independent orbits.

Every remaining orbit has one word with middle coordinate in \(A\) and one with middle coordinate in \(B\). Write it as

\[
(u,v,c(z)),\quad (z,c(v),c(u)),\qquad u,v,z\in A.
\]

Associate the directed arc \(v\to z\) to the orbit. Its length-two suffix of the first word is \((v,c(z))\); its length-two prefix of the second word is \((z,c(v))\). All other types of prefixes and suffixes lie in distinct Cartesian products of \(A,B,D\). Consequently, an overlap occurs among these orbits **if and only if** an arc \(v\to z\) is a loop (\(v=z\)) or both orientations \(v\to z\) and \(z\to v\) occur. For any nonloop directed arc, the first letter \(u\) may independently range over an arbitrary subset of \(A\), with no further conflicts.

**3. Enumerating with an allowed first-coordinate set.** For a fixed partial complementary transversal \(A\), allow the first-coordinate set of a code to be any subset of \(A\). Then the \(a^2(h-a)\) independent \(D\)-middle orbits contribute \((1+x^2)^{a^2(h-a)}\). For each of the \(\binom a2\) unordered pairs of vertices, select neither orientation or select exactly one orientation and a nonempty subset of the \(a\) possible first letters. This contributes

\[
1+2\big((1+x^2)^a-1\big)=2(1+x^2)^a-1.
\]

Thus the polynomial for codes with first-coordinate set *contained* in a fixed \(A\) is

\[
G_a(x)=(1+x^2)^{a^2(h-a)}\big(2(1+x^2)^a-1\big)^{\binom a2}.
\]

Let \(E_b(x)\) count codes with their first-coordinate set *equal* to a fixed allowable set of \(b\) letters. Involutive alphabet relabeling shows this depends only on \(b\), and containment gives \(G_a=\sum_{b=0}^a\binom ab E_b\). Binomial inversion yields \(E_b=\sum_{a=0}^b(-1)^{b-a}\binom ba G_a\). There are \(2^b\binom hb\) choices of the actual first-coordinate set of size \(b\). Summing and interchanging the finite sums, using \(\binom hb\binom ba=\binom ha\binom{h-a}{b-a}\) and the binomial theorem, gives

\[
\begin{aligned}
H_h(x)&=\sum_{b=0}^{h}2^b\binom hb E_b(x)\\
&=\sum_{a=0}^{h}G_a(x)\binom ha2^a
\sum_{j=0}^{h-a}\binom{h-a}{j}(-2)^j\\
&=\sum_{a=0}^{h}(-1)^{h-a}\binom ha2^a G_a(x).
\end{aligned}
\]

This proves the enumerator, without assuming all letters are used.

**4. Sharp maximum and all equality cases.** For a code with actual first-letter set of size \(a\), Step 2 gives the sharp conditional bound

\[
|C|\le 2a^2(h-a)+2a\binom a2=a^2(2h-a-1)=:f_h(a).
\]

For \(h\ge2\), the function \(f_h(a)\) increases strictly at integer arguments from \(a=0\) to \(a=h\). Indeed its derivative on \((0,h)\) is \(a(4h-2-3a)>0\) for \(h\ge2\), with possible equality only at the endpoint \(a=h=2\). Hence the maximum is \(f_h(h)=h^2(h-1)\). Equality requires \(a=h\), so \(D=\varnothing\), and requires each unordered pair of \(A\) to use exactly one direction with *all* \(h\) possible first letters. Thus each equality code is determined by a complementary transversal \(A\) and a tournament on \(A\). The construction is valid by Step 2, and the first-letter set and directed arcs are recoverable from the code. There are \(2^h\) transversals and \(2^{\binom h2}\) tournaments. For \(h=1\) there are no possible nonloop arcs and no unused middle symbols once a first symbol is chosen, so only the empty code exists.

## Verification

Run `python3 verify.py` and `python3 crosscheck.py` in the directory containing the supplied standalone scripts. Both use only the Python standard library. The first expands the enumerator at \(1\le h\le9\), checks the top coefficient and constructs maximum codes at those values. The second exhaustively enumerates all reverse-complement word-pair cliques at alphabet sizes \(2\), \(4\) and \(6\) by direct prefix/suffix comparisons, independently of the formula. Their expected success messages are `VERIFY_OK` and `CROSSCHECK_OK`. The independent exhaustive histograms for alphabet sizes four and six, respectively, are \((1,12,8)\) and \((1,60,726,3072,6276,7344,5256,2304,576,64)\), where entry \(j\) counts codes with \(2j\) words. The proof, not the finite checks, establishes all alphabet sizes.

## Relationship to prior work

**Previously known extremal results are not claimed as new.** Blackburn's 2013 preprint (Section 4, Theorem 7) solves the *unrestricted* maximum-size problem for length-three non-overlapping codes. More directly, Fimmel, Michel and Strüngmann's 2017 treatment of strong comma-free genetic codes gives the exact reverse-complement-constrained four-letter extremal counts, including eight maximum four-word codes. Most decisively, Fimmel, Michel, and coauthors' 2023 paper, *Diletter and triletter comma-free codes over finite alphabets*, **Proposition 5.9**, already proves, for **every even alphabet**, precisely the largest size \(h^2(h-1)\), the number \(2^{h+\binom h2}\) of maximum codes, and the partition/orientation description underlying those extremizers. The maximum formula and tournament characterization above are included only as derivable boundary checks, not originality claims. The 2023 paper's Theorem 5.3 gives a structural description of inclusion-wise non-expandable (unrestricted) codes, and its Proposition 5.9 specializes this to self-complementary non-expandable codes, but does not state or count the entire **nonmaximal** self-complementary codebook spectrum.

**The new claim here is specifically the complete polynomial \(H_h(x)\) for all even alphabets, including every nonmaximal code size, the empty code, and all possible endpoint supports.** It cannot be inferred numerically from knowing only the maximum or its number of extremizers: for example, at \(h=3\), the coefficients of \(x^2,x^4,\ldots,x^{16}\) constitute nine further exact counts not specified in Proposition 5.9. The proof uses allowed-support counting and binomial inversion to account for multiply extendable subcodes. Stanovnik, Moškon and Mraz (2024) also address unrestricted non-overlapping extremal codes; this does not give the symmetric all-size enumerator. Existing general code classifications may furnish an alternative derivation, but the consulted texts do not state this polynomial or its coefficients; unindexed computations are a priority risk.

## Limitations

The statement is for words of length exactly three and a fixed-point-free complement on an even-sized labeled alphabet; it does not establish formulas at other word lengths, fixed-point-bearing involutions, or additional distance/biochemical restrictions. The enumerator includes every codebook, including nonmaximal codes and the empty code. Computational tests through \(h=9\) or the exhaustive tests at \(h\le3\) are finite, not an independent proof of the universal identity. The maximal size, number of maximizers, and four-letter special case were established in earlier work and are not new. Historical priority for the full all-size enumerator is not independently certified; a non-obvious implication of published structural classifications or an unindexed enumeration remains a risk.

## References

1. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first public version 5 March 2013, especially Section 4, Theorem 7. https://arxiv.org/abs/1303.1026
2. Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, IEEE Transactions on Information Theory 59 (2013), 4668–4674. https://doi.org/10.1109/TIT.2013.2252952
3. E. Fimmel, C. J. Michel and L. Strüngmann, *Strong Comma-Free Codes in Genetic Information*, Bulletin of Mathematical Biology (2017), DOI:10.1007/s11538-017-0307-0. https://dpt-info.di.unistra.fr/~c.michel/Michel_Article75.pdf
4. E. Fimmel et al., *Diletter and triletter comma-free codes over finite alphabets*, Australasian Journal of Combinatorics 86 (2023), 233–270, especially Proposition 5.9. https://ajc.maths.uq.edu.au/pdf/86/ajc_v86_p233.pdf
5. L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024), 1299–1326. https://doi.org/10.1007/s10623-023-01344-z
