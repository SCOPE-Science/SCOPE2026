# Nine missing subsequences of Cantor words and alternating-gap words

## Finding

For every even integer \(M\ge 4\), every binary word in the alternating-gap family below is \(M\)-subsequence-universal, but fails at length \(M+1\) in exactly nine ways. The exact set of missing subsequences of length \(M+1\) is
\[
\mathcal A_M=\{\alpha 1^{M-3}\beta:\alpha\in\{00,01,11\},\ \beta\in\{00,10,11\}\}.
\]
In particular, the finite binary Cantor iterate \(C_k\) has subsequence-universality index \(2^k\) and exactly the nine absent subsequences \(\mathcal A_{2^k}\) at length \(2^k+1\), for every \(k\ge2\). This statement concerns *scattered* subsequences, not contiguous factors.

## Assumptions and scope

A word \(u=u_1\cdots u_t\) is a scattered subsequence of \(w=w_1\cdots w_s\) if there are strictly increasing indices \(1\le i_1<\cdots<i_t\le s\) such that \(w_{i_j}=u_j\) for every \(j\). A word is \(t\)-subsequence-universal over \(\{0,1\}\) when all \(2^t\) binary words of length \(t\) occur as scattered subsequences. Its universality index is the largest such \(t\).

Fix an **even** integer \(M\ge4\) and integers \(g_1,\ldots,g_{M-1}\) with \(g_{2j-1}=1\) and \(g_{2j}\ge3\) wherever those indices occur. Set
\[
w=1\,0^{g_1}1\,0^{g_2}1\cdots 0^{g_{M-1}}1.
\]
Thus \(w\) has exactly \(M\) occurrences of \(1\), starts and ends with \(1\), and its first and final zero-gaps both have length one. No upper bound on the even-index zero gaps is required.

The Cantor words are \(C_0=1\) and \(C_{k+1}=\mu(C_k)\), where \(\mu(1)=101\) and \(\mu(0)=000\). For \(k\ge2\) they are instances of the above family with \(M=2^k\).

## Proof

**1. The short canonical word embeds in all members of the family.** Set
\[
W_M=(101000)^{M/2-1}101.
\]
Its \(M-1\) zero gaps alternate \(1,3,1,3,\ldots,1\). Because the odd-index gaps in \(w\) equal one and the even-index gaps are at least three, \(W_M\) is a scattered subsequence of \(w\): retain every \(1\), every zero in each odd gap, and three zeros from each even gap. Consequently, every subsequence of \(W_M\) is a subsequence of \(w\).

**2. Canonical universality.** The base word is \(W_4=101000101\), which partitions as \(10\mid10\mid001\mid01\), four consecutive blocks each containing both symbols. Hence \(W_4\) is \(4\)-universal. The block \(B=101000\) has the two universal blocks \(10\mid1000\), and so is \(2\)-universal. Since \(W_{M+2}=BW_M\), induction shows that every \(W_M\) is \(M\)-universal. Thus every \(w\) in the family is \(M\)-universal. Since \(w\) contains only \(M\) ones, \(1^{M+1}\) is absent, and the universality index is exactly \(M\).

**3. Exact length-\(M+1\) absence set for the canonical words.** Define \(\mathcal A_M\) as in the finding. In the base case \(M=4\), the nine missing length-five words of \(W_4\) are exactly
\[
00100,\ 00110,\ 00111,\ 01100,\ 01110,\ 01111,\ 11100,\ 11110,\ 11111.
\]
The twenty-three remaining length-five words, together with an explicit increasing-position witness in \(W_4\) for each, are listed in the following finite certificate. Position indices are one-based.

| Word | Positions | Word | Positions |
|---|---|---|---|
| `00000` | 2,4,5,6,8 | `00001` | 2,4,5,6,7 |
| `00010` | 2,4,5,7,8 | `00011` | 2,4,5,7,9 |
| `00101` | 2,4,7,8,9 | `01000` | 2,3,4,5,6 |
| `01001` | 2,3,4,5,7 | `01010` | 2,3,4,7,8 |
| `01011` | 2,3,4,7,9 | `01101` | 2,3,7,8,9 |
| `10000` | 1,2,4,5,6 | `10001` | 1,2,4,5,7 |
| `10010` | 1,2,4,7,8 | `10011` | 1,2,4,7,9 |
| `10100` | 1,2,3,4,5 | `10101` | 1,2,3,4,7 |
| `10110` | 1,2,3,7,8 | `10111` | 1,2,3,7,9 |
| `11000` | 1,3,4,5,6 | `11001` | 1,3,4,5,7 |
| `11010` | 1,3,4,7,8 | `11011` | 1,3,4,7,9 |
| `11101` | 1,3,7,8,9 |  |  |

For the induction, write \(W_{M+2}=BW_M\) with \(B=101000\). For an arbitrary binary target \(u\) of length \(M+3\), match its symbols **greedily** in \(B\) from left to right (always use the earliest possible position). Because \(B\) is \(2\)-universal, at least two symbols match in \(B\). If at least three symbols match, the remaining target suffix has length at most \(M\) and therefore occurs in \(W_M\). If exactly two match, then the first three symbols of \(u\) have one of the forms \(001,011,111\): this follows by checking the eight possible three-bit prefixes against \(B\). Thus \(u=\alpha x\) with \(\alpha\in\{00,01,11\}\), and \(x\) begins with \(1\) and has length \(M+1\). By the greedy exchange property, a target is a subsequence of \(BW_M\) if and only if the unmatched suffix after the greedy match inside \(B\) is a subsequence of \(W_M\). By induction, the only length-\(M+1\) missing words in \(W_M\) that start with \(1\) are \(1^{M-1}\beta\), with \(\beta\in\{00,10,11\}\). Hence the length-\(M+3\) missing words of \(BW_M\) are exactly \(\alpha1^{M-1}\beta\), establishing \(\mathcal A_{M+2}\).

**4. All nine remain absent even if the long zero gaps grow.** Let \(u=\alpha 1^{M-3}\beta\in\mathcal A_M\), and put \(z=\#_0(\alpha)+\#_0(\beta)\), the total number of zeros in the two boundary blocks. If \(u\) were a subsequence of \(w\), its \(M+1-z\) ones would omit exactly \(z-1\) of the \(M\) ones of \(w\). But the prefix block \(\alpha\) forces omission of at least \(\#_0(\alpha)\) initial ones: `00` needs two gaps before its next required one because the first gap is a single zero; `01` needs one omitted initial one; `11` needs none. Symmetrically, the suffix block \(\beta\) forces omission of at least \(\#_0(\beta)\) terminal ones (`00`, `10`, `11` require two, one, zero omitted terminal ones). These initial and terminal omissions are disjoint in any putative embedding, so at least \(z\) ones must be omitted, a contradiction. Therefore all nine words in \(\mathcal A_M\) are absent from \(w\). Step 1 and step 3 show that no further length-\(M+1\) words can be absent.

**5. Cantor-word specialization.** In \(C_k\), the positions of ones (counting from the beginning) have gaps of zeros \(g_j=3^{\nu_2(j)}\) for \(1\le j<2^k\), where \(\nu_2(j)\) denotes the exponent of two dividing \(j\). This follows inductively from \(C_{k+1}=C_k0^{3^k}C_k\): the two copies give previous gaps while their separating zero block gives the unique middle gap \(3^k\). All odd-index gaps are one and all even-index gaps are at least three. Thus for \(k\ge2\), \(C_k\) belongs to the family with \(M=2^k\), completing the proof.

## Verification

The self-contained script `checker.py` enumerates every length-\(M\) and length-\(M+1\) binary target and tests each against canonical words \(W_M\) for \(M\in\{4,6,8,10,12,14\}\), against Cantor iterates \(C_k\) for \(k\in\{2,3,4\}\), and against 27 variable-gap instances with \(M=6\). It checks exactly nine missing critical-length words and complete universality at the preceding length. It prints `PASS` on success. The mathematical induction and the twenty-three explicit base witnesses, not the finite experiments, prove the unrestricted assertions.

## Relationship to prior work

The Cantor sequence and its substitution structure are classical; Wen and Wu (2014) analyze its Hankel determinants and ternary support, while the 2016 paper *On the permutation complexity of the Cantor-like sequences* studies contiguous-factor and permutation complexities. Neither contains this stated scattered-subsequence classification. Kosche, Koß, Manea and Siemer (2021/2023) develop general theory and algorithms for absent and shortest absent subsequences; the present theorem specializes to a concrete sparse morphic word and extends to an infinite alternating-gap class with an explicit nine-word boundary classification. General characterization algorithms and arbitrary-word extremal bounds do not by themselves state the particular all-rank conclusion. Priority beyond inspected sources has not been established.

## Limitations

The family requires exactly \(M\) ones, an even \(M\ge4\), unit odd-index zero gaps, and even-index zero gaps at least three; the claim does not extend automatically to other gap patterns, other alphabets, arbitrary-length factors of the infinite Cantor word, or higher missing lengths. The explicit set is for the **first** nonuniversal length only. Earlier works may imply special cases through additional computations.

## References

1. Zhi-xiong Wen and Wen Wu, *Hankel determinants of the Cantor sequence*, arXiv:1407.3578, first submitted 2014-07-14, https://arxiv.org/abs/1407.3578.
2. *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science **616** (2016), 100–110, DOI:10.1016/j.tcs.2015.12.022, https://doi.org/10.1016/j.tcs.2015.12.022.
3. Maria Kosche, Tore Koß, Florin Manea, and Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (2021; later revisions 2023), https://arxiv.org/abs/2108.13968.
