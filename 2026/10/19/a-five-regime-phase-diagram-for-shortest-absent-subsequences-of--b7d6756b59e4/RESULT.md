# A five-regime phase diagram for shortest absent subsequences of periodic binary run words

## Finding
For arbitrary positive integers \(a,b,k\), consider the *linear* binary word \(W_{a,b,k}=(0^a1^b)^k\), where exponents mean repetition. A scattered subsequence keeps the letter order but may skip positions. Denote the distinct shortest words absent as scattered subsequences by \(\operatorname{SAS}(W)\). Write \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\).

The shortest absent length equals \(k+1\) when \(\min(a,b)=1\), and \(2k\) otherwise. Its exact multiplicity is
\[
|\operatorname{SAS}(W_{a,b,k})|=
\begin{cases}
k+2,&a=b=1,\\
2,&\min(a,b)=1<\max(a,b),\\
F_{2k},&a=b=2,\\
2^{k-1},&\min(a,b)=2<\max(a,b),\\
1,&\min(a,b)\ge3.
\end{cases}
\]

All missing words are explicitly classified. If \(a=b=1\), they are \(1^j0^{k+1-j}\), for \(0\le j\le k+1\). If \(a=1<b\), they are \(0^{k+1}\) and \(10^k\); if \(b=1<a\), they are \(1^{k+1}\) and \(1^k0\). If \(a,b\ge2\), they are exactly the binary words of length \(2k\) starting with one in which each maximal zero-run has *odd* length for \(a=2\), and length one for \(a\ge3\), while each maximal one-run has *odd* length for \(b=2\), and length one for \(b\ge3\).

## Assumptions and scope
The alphabet is the fixed binary alphabet \(\{0,1\}\). Subsequence always means scattered (not contiguous). The input is the linear word written, not its circular rotation class; a shortest absent subsequence is absent and has minimal length, not merely inclusion-minimal. All parameters are positive integers; no asymptotic qualification or unproved extension is required.

## Proof
**Greedy run-embedding lemma.** Decompose a nonempty candidate \(v\) uniquely into maximal constant runs \(x_1^{r_1}\cdots x_t^{r_t}\), and set \(c_i=a\) when \(x_i=0\), \(c_i=b\) when \(x_i=1\). Let \(\delta=1\) if \(v\) begins with one and \(\delta=0\) otherwise. Index the alternating constant-symbol host runs \(0^a,1^b,\ldots\) starting at one. Greedily embedding \(v\) into the infinite periodic word ends at host-run index
\[
J(v)=\delta+t+2\sum_{i=1}^t\left(\left\lceil\frac{r_i}{c_i}\right\rceil-1\right).
\]
Indeed, the first candidate run starts at host index \(1+\delta\); using one additional host run of the same symbol advances by two host-run indices; switching candidate symbol advances by one. Greediness yields the earliest possible last position. The exact finite-word criterion is therefore \(v\) present in \(W_{a,b,k}\) if and only if \(J(v)\le2k\).

Rewrite, with \(L=|v|\),
\[
J(v)=\delta+L+\sum_{i=1}^t E_{c_i}(r_i),\qquad
E_c(r)=2\bigl(\lceil r/c\rceil-1\bigr)-(r-1).
\]
If \(c\ge2\), then \(E_c(r)\le0\). For \(c=2\), equality holds exactly when \(r\) is odd; for \(c\ge3\), equality holds exactly when \(r=1\). In particular, when \(a,b\ge2\), every candidate with \(L\le2k-1\) is present, since \(J\le1+L\le2k\). The length-\(2k\) candidate \((10)^k\) is absent. At that length, \(J>2k\) is possible exactly when \(\delta=1\) and every run contribution is zero. This proves both the exact length and the explicit classification for \(a,b\ge2\).

Every word in this latter classification starts with one, has even total length, and has exclusively odd-length runs; hence it also ends in zero and its runs occur in an even number of alternating symbol-pairs. Writing \(R_c(z)=z/(1-z^2)\) for \(c=2\) and \(R_c(z)=z\) for \(c\ge3\), the generating function by total length is
\[
\frac{R_a(z)R_b(z)}{1-R_a(z)R_b(z)}.
\]
When both lengths equal two, this is \(z^2/(1-3z^2+z^4)\), whose coefficient at \(z^{2k}\) is \(F_{2k}\), by the even-Fibonacci recurrence and base coefficient one. When precisely one length is two, the function is \(z^2/(1-2z^2)\), with coefficient \(2^{k-1}\); when both are at least three, it is \(z^2/(1-z^2)\), with coefficient one.

If at least one of \(a,b\) is one, any binary word of length at most \(k\) embeds by taking one requested symbol from each successive \(0^a1^b\) block. A constant word of the symbol whose run has length one, of length \(k+1\), is absent, establishing the shortest absent length \(k+1\).

For \(a=1<b\), let \(v\) have length \(L=k+1\) and \(z\) zeros, arranged in \(t_0\) zero-runs. If \(z=0\), then the all-one candidate embeds (each of the \(k\) one-blocks holds at least two ones). If \(0<z\le k-1\), its zero-run contribution is \(z-t_0\), and its one-run contributions are nonpositive. Thus \(J\le\delta+k+1+z-t_0\le2k\), because \(\delta\le1\), \(t_0\ge1\), and \(z\le k-1\). If \(z=k+1\), \(v=0^{k+1}\) is absent. If \(z=k\), the unique one occurs before all zeros, after all zeros, or inside a zero-run. The first case \(10^k\) is absent (\(J=2k+1\)); the other placements embed (they have \(J\le2k\)), proving that precisely the two specified candidates are absent. Complementation plus reversal transforms \((0^a1)^k\) into \((01^a)^k\), transferring this result to \(b=1<a\).

Finally, for \(a=b=1\), every host run has length one, so \(J(v)=\delta+L+h(v)\), with \(h(v)\) the number of adjacent equal-letter pairs. At \(L=k+1\), a word starting with zero is absent exactly when all \(k\) adjacent pairs agree, namely \(0^{k+1}\). A word starting with one is absent exactly when at least \(k-1\) of its \(k\) adjacent pairs agree, i.e. it changes letter at most once, from one to zero. These are exactly \(1^j0^{k+1-j}\) for \(1\le j\le k+1\). Together with the all-zero case this gives \(k+2\) missing words. This finishes all cases.

## Verification
The accompanying standalone `verify.py` constructs all candidate binary words at the claimed shortest length and all words at the preceding length for each \(1\le a,b,k\le6\). It directly greedy-tests subsequence membership, separately evaluates the host-run embedding index, matches the *entire absent-word set* against the structural classification, and matches all five formulas; 216 parameter triples and 139,272 candidate words were checked. It independently compares integer Fibonacci values and the mixed-power formula through \(k=69\). Run `python3 verify.py` with Python 3; no third-party packages are needed. Finite enumeration is corroboration, not the infinite proof, which is given above.

## Relationship to prior work
Okhotin (2010) studies automaton state complexity of *scattered substring languages*, providing older background for subsequences, but does not address shortest missing words of these specific linear periodic strings. Kosche et al. (2021 preprint; 2023 journal) established foundational characterizations and algorithms for shortest absent subsequences. Their general approach can decide individual instances; the inspected paper does not state the evaluated complete \((a,b,k)\) phase diagram, its five count regimes, or this exact run-by-run classification. The published Fibonacci extremal result linked below maximizes shortest-absent-subsequence counts over *all* binary words at a fixed length; it does not give the exact count on the restricted periodic family or follow from our count by parameter substitution. No absolute uniqueness claim is made from search failure.

## Limitations
The result concerns scattered subsequences of binary linear run-block powers, not absent contiguous substrings or arbitrary periodic bases with more than two runs. Earlier equivalence under a different terminology or a derived special-case enumeration may exist. The 2010 source supplies the archive-period literature anchor; the more directly relevant absent-subsequence definitions were introduced in later literature. No independent validation is claimed.

## References
1. Alexander Okhotin, *On the State Complexity of Scattered Substrings and Superstrings*, Fundamenta Informaticae 99 (2010), 325–338, DOI 10.3233/FI-2010-252; published online April 1, 2010.
2. Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1 (August 31, 2021); published in Fundamenta Informaticae 189 (2023), 199–240.
3. *Fibonacci extremals for shortest absent subsequences of binary words*, published October 4, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28.
