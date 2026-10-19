# Rigid ruler-word Abelian-border arrays and an unbounded alphabet hierarchy

## Finding

Let \(\nu_2(i)\) be the exponent of the largest power of \(2\) dividing the positive integer \(i\). For every integer \(n\geq1\), define the ruler word \(r^{(n)}=r_1\cdots r_n\) by \(r_i=\nu_2(i)\). Let \(\pi_w(i)\) be the longest proper Abelian-border length of the length-\(i\) prefix of a word \(w\). Then

\[
\pi_{r^{(n)}}(i)=i-2^{\nu_2(i)}\qquad(1\leq i\leq n).
\]

**Rigidity theorem.** Every word \(w\), over any alphabet, with this entire length-\(n\) Abelian-border array is obtained from \(r^{(n)}\) by a one-to-one relabeling of its occurring symbols. In particular, the array can be realized on an alphabet of size \(q\) if and only if

\[
q\geq1+\lfloor\log_2 n\rfloor.
\]

Consequently, if \(M(n)\) denotes the maximum, over all realizable length-\(n\) Abelian-border arrays (allowing arbitrary finite alphabets), of the least alphabet size needed to realize the array, then

\[
M(n)\geq1+\lfloor\log_2 n\rfloor.
\]

Thus no fixed alphabet realizes every valid Abelian-border array of every length. The rigid array is unique up to letter renaming, despite the known non-injectivity of Abelian-border arrays on unrestricted larger alphabets.

## Assumptions and scope

A word is a sequence of letters; the alphabet can be arbitrary but the word length \(n\) is finite. Two equally long words are *Abelian equivalent* if every letter occurs equally often. For a word \(w=w_1\cdots w_n\), a **proper Abelian border of length** \(j\) is an equality of the Parikh vectors of \(w_1\cdots w_j\) and \(w_{n-j+1}\cdots w_n\), where \(1\leq j<n\). The longest length is \(0\) when no such \(j\) exists. The array \(\pi_w\) records these lengths at each prefix of \(w\). A **letter renaming** is an injective map on the distinct letters actually occurring in the word, extended positionwise. No assumption of a fixed alphabet order is made.

For illustration, the first sixteen ruler symbols are \(0102010301020104\), and the corresponding array is

\[
(0,0,2,0,4,4,6,0,8,8,10,8,12,12,14,0).
\]

## Proof

**1. Complementarity of border lengths.** For any length-\(i\) word \(v\), equality of the Parikh vectors of its length-\(j\) prefix and suffix is equivalent, by subtracting each from the full Parikh vector, to equality for its length-\((i-j)\) prefix and suffix. Hence, if a positive border exists, the shortest positive border has length \(i-\pi_v(i)\). This elementary fact is also Proposition 3.2 of Habib–Shamil–Rahman [1]; it is used here, not claimed as new.

**2. Explicit ruler array.** Fix \(i\geq1\) and put \(d=2^{\nu_2(i)}\). If \(i=d\), then \(i\) is a power of two and the final letter \(\nu_2(i)\) has not appeared at any earlier position. Every nonempty proper suffix includes that letter, while every proper prefix omits it. Therefore no proper Abelian border exists, and \(\pi(i)=0=i-d\).

If \(i>d\), then \(i-d\) is a positive multiple of \(d\). For every \(1\leq j<d\), the elementary valuation identity

\[
\nu_2(i-d+j)=\nu_2(j)
\]

holds, because \(d\) divides \(i-d\) while \(\nu_2(j)<\nu_2(d)\). At the final position, \(\nu_2(i)=\nu_2(d)\). Thus the suffix of length \(d\) is *identically equal* to the prefix of length \(d\), and so \(d\) is an Abelian-border length. No shorter positive length \(t<d\) can be an Abelian border: the suffix of length \(t\) contains the terminal symbol \(\nu_2(i)\), which does not occur in the prefix of length \(t<d\). Thus \(d\) is the shortest positive Abelian border, and Step 1 yields \(\pi(i)=i-d\).

**3. Reconstruction and rigidity.** Suppose \(w_1\cdots w_n\) has the displayed array. We induct on \(i\), maintaining distinct letters \(a_0,a_1,\dots\) such that \(w_j=a_{\nu_2(j)}\) for every \(j\leq i\). At \(i=1\), set \(a_0=w_1\).

First let \(i=2^k\), where \(k\geq1\). Inductively the preceding positions contain exactly the distinct letters \(a_0,\ldots,a_{k-1}\). If the new letter were some \(a_s\) with \(0\leq s<k\), set \(t=2^s\). For each \(1\leq j<t\), valuations give \(\nu_2(i-t+j)=\nu_2(j)\); the last letter was assumed to be \(a_s=a_{\nu_2(t)}\). Therefore the first and last blocks of length \(t\) would be identical. This would give a positive Abelian border, contrary to the prescribed \(\pi_w(i)=0\). Hence \(w_i\) is a genuinely new letter; name it \(a_k\).

Next suppose \(i\) is not a power of two and put \(d=2^{\nu_2(i)}<i\). The prescribed longest border \(i-d\) and Step 1 imply that \(d\) is an Abelian-border length. Thus

\[
\Psi(w_{i-d+1}\cdots w_{i-1})+\mathbf e_{w_i}
=\Psi(w_1\cdots w_d),
\]

where \(\Psi\) is the Parikh vector and \(\mathbf e_a\) is the unit coordinate at letter \(a\). Every letter on either side except \(w_i\) is already specified by the induction. The valuation identities of Step 2 show that \(w_{i-d+1}\cdots w_{i-1}=w_1\cdots w_{d-1}\), so cancellation forces \(\mathbf e_{w_i}=\mathbf e_{a_{\nu_2(i)}}\). Therefore \(w_i=a_{\nu_2(i)}\), proving the induction and rigidity for all \(n\).

**4. Alphabet threshold.** The largest \(\nu_2(i)\) for \(1\leq i\leq n\) is \(\lfloor\log_2n\rfloor\), and each smaller value occurs. The ruler prefix uses exactly \(1+\lfloor\log_2n\rfloor\) distinct letters. Rigidity forces the same number in every realization. This proves the threshold and the lower bound on \(M(n)\). In particular, applying the bound as \(n\to\infty\) proves the absence of a universal fixed alphabet.

## Verification

The accompanying standalone `verify.py` computes longest proper Abelian-border arrays by direct multiset comparison, without using the valuation formula, at lengths \(1,2,3,4,5,6,7,8,16,32,64,128,256,512\). It additionally enumerates canonical first-occurrence relabelings and checks that the entire prescribed array admits exactly one representative at every length from \(1\) through \(16\). Execution command: `python3 verify.py`. Successful execution prints `RULER_ABELIAN_BORDER_CHECKS_PASS`. These finite checks exercise the definitions and boundary cases; the unrestricted assertion follows from the induction, not the tests.

## Relationship to prior work

Habib, Shamil, and Rahman [1] introduced the relevant inverse problem and proved that a binary Abelian-border array determines its word up to complementation. Their Section 4 discusses the non-injective larger-alphabet problem, including examples of distinct non-renaming-equivalent words sharing an array. Their shortest/longest border duality is used directly here. The present theorem instead isolates a rigid all-length family **across arbitrary alphabets**, yielding a quantitative alphabet-size obstruction.

Goč, Rampersad, Rigo, and Salimov [2] study abelian (un)bordered words and their enumeration, including larger alphabets, but not uniqueness of complete longest-border arrays. Berera and coauthors [3] study the ruler word in square-free-word constructions, not its Abelian-border array. Duval, Lecroq, and Lefebvre [4] consider **ordinary exact** border arrays over bounded alphabets; equality of words is not interchangeable with Abelian equivalence. The construction and proof here address the latter, weaker observation. The Abelian-combinatorics survey [5] treats border-length duality and related questions but does not state the present array reconstruction result in its inspected Abelian-border discussion.

## Limitations

The theorem characterizes only the displayed special family of arrays; it does not determine \(M(n)\) exactly, count all valid arrays on any prescribed larger alphabet, or solve the general larger-alphabet verification problem. The logarithmic bound is a proved lower bound, not an asserted asymptotic equality. Similar ruler/Zimin constructions occur in ordinary border theory; an independently published equivalent formulation not located by the cited searches cannot be excluded. Reproducibility checks at finite lengths are not an infinite proof.

## References

[1] M. Habib, M. S. Shamil, M. S. Rahman, *Counting and Verifying Abelian Border Arrays of Binary Words*, arXiv:2111.00259v1, first posted 2021-10-30. https://arxiv.org/pdf/2111.00259

[2] D. Goč, N. Rampersad, M. Rigo, P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science (2014). https://scispace.com/pdf/on-the-number-of-abelian-bordered-words-with-an-example-of-43gdbru0k3.pdf

[3] S. Berera et al., *The Lexicographically Least Square-Free Word with a Given Prefix*, Electronic Journal of Combinatorics 30(3), P3.11 (2023). https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i3p11/pdf/

[4] J.-P. Duval, T. Lecroq, A. Lefebvre, *Border Array on Bounded Alphabet*, Journal of Automata, Languages and Combinatorics 10(1), 51–60 (2005), original conference version 2002..

[5] G. Fici et al., *Abelian Combinatorics on Words: A Survey*, arXiv:2207.09937, 2022. https://arxiv.org/html/2207.09937v2
