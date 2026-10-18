# Sharp quartic growth of binary one-gap pair-deck profiles

## Finding

For a binary word \(w=w_1\cdots w_n\), record its two letter multiplicities and the four ordered one-gap pair counts
\[
G_{ab}(w)=\#\{(i,j):1\le i<j\le n,\ j-i\ge2,\ w_i=a,\ w_j=b\},\qquad a,b\in\{0,1\}.
\]
Write \(Q(n)\) for the number of distinct profiles of binary words of length \(n\). For each integer \(n\ge100\), put \(m=\lfloor n/100\rfloor\). Then
\[
\boxed{(m+1)(9m+1)(4m-1)^2\ \le\ Q(n)\ \le\ 2n(n+1)(\lfloor n^2/4\rfloor+1).}
\]
Consequently \(Q(n)=\Theta(n^4)\). In the noiseless zero-error code whose decoder observes precisely this profile, the maximum codebook cardinality is \(Q(n)\), and its information capacity is \(\log_2 Q(n)=4\log_2 n+O(1)\) bits.

## Assumptions and scope

The alphabet is \(\{0,1\}\). Two chosen positions must have at least one unchosen position strictly between them; the pair is ordered from left to right. Both length-one counts are observed. Words need not be periodic, balanced, or factors of a fixed infinite sequence. All counts are exact integer multiplicities. The upper bound holds for every \(n\ge1\), and the displayed constructive lower bound holds for \(n\ge100\). No formula for the exact value of \(Q(n)\) is asserted.

## Proof

**Upper bound: four sufficient statistics.** Fix \(n\ge1\). For each word define \(K\) to be the number of ones, \(R\) its number of nonempty maximal constant runs, \(e\) its first letter, and \(T\) its *unrestricted* scattered \(01\)-pair count (no gap constraint). The four-tuple \((K,R,e,T)\) determines the gapped pair profile.

Indeed, the number \(r_0\) of zero runs and \(r_1\) of one runs follow from \(R\) and \(e\), because the runs alternate. The adjacent \(00\) and \(11\) counts are, respectively, \(n-K-r_0\) and \(K-r_1\); the adjacent \(01\) and \(10\) counts are the numbers of corresponding boundaries between consecutive runs, also determined by \(R,e\). Before subtracting adjacent pairs, the four unrestricted two-letter counts are
\[
U_{00}=\binom{n-K}{2},\quad U_{11}=\binom K2,\quad U_{01}=T,\quad U_{10}=K(n-K)-T.
\]
Thus every \(G_{ab}=U_{ab}-A_{ab}\) is determined by \((K,R,e,T)\), and length-one counts are \(n-K,K\). There are at most \(n+1\) possibilities for \(K\), at most \(n\) for \(R\), two for \(e\), and at most \(\lfloor n^2/4\rfloor+1\) for \(T\), since \(0\le T\le K(n-K)\). Multiplying gives the claimed upper bound. This is an injection from *distinct profiles* into the set of four-tuples: every tuple deterministically produces at most one profile, and any one profile may have several tuples without affecting the bound.

**Lower bound: four independent effective parameters.** Let \(n\ge100\) and \(m=\lfloor n/100\rfloor\), so \(m\ge1\) and \(n\ge100m\). Set \(b=8m\), \(c=8m+1\). For integers
\[
m\le s\le2m,\quad m\le h\le10m,\quad 1\le a\le4m-1,\quad 1\le d\le4m-1,
\]
define \(H_0=n-(24m+1+2s+h)\) and the binary word
\[
w(s,h,a,d)=0^{H_0+a}\,1^{8m}\,0^{4m-a}\,(10)^s\,1^d\,0^{8m+1}\,1^{h+4m-d}.
\]
Every displayed exponent is a positive integer: in particular \(H_0\ge62m-1\ge1\). The length is exactly \(n\). Its number of ones is \(K=12m+s+h\); its runs alternate between a zero run and a one run, starting at zero and ending at one, with exactly \(s+3\) runs of each type. Hence \(R=2s+6\).

The observed profile recovers \(K\). Moreover, because this word has \(s+3\) one runs, its adjacent \(11\) count equals \(K-(s+3)\). Consequently
\[
G_{11}=\binom K2-K+(s+3),
\]
so the profile recovers \(s\), and then \(h=K-12m-s\). Therefore no profile collision is possible between witnesses with distinct \((s,h)\).

At fixed \(s,h\), let \(T\) be the unrestricted scattered \(01\) count. Counting the ones in each successive block against preceding zeros gives
\[
\begin{aligned}
T={}&8m(H_0+a)+s(H_0+4m)+\frac{s(s-1)}2\\
&+d(H_0+4m+s)\\
&+(h+4m-d)(H_0+4m+s+8m+1).
\end{aligned}
\]
Thus, when \(s,h\) are fixed, \(T=T_0+8ma-(8m+1)d\), where \(T_0\) depends only on \(n,m,s,h\). Equality of \(T\) for two choices would imply
\[
8m(a-a')=(8m+1)(d-d').
\]
As \(8m\) and \(8m+1\) are coprime, \(8m+1\) divides \(a-a'\), and \(8m\) divides \(d-d'\). Both absolute differences are at most \(4m-2\), forcing \(a=a'\) and \(d=d'\). Finally, at fixed \(s,h\) the adjacent \(01\) count is \(s+3\), hence \(G_{01}=T-(s+3)\); distinct \(T\) values give distinct observed profiles.

All \((m+1)(9m+1)(4m-1)^2\) witness words therefore have pairwise distinct profiles, which proves the lower bound. Since \(m\) is proportional to \(n\), the bounds prove \(Q(n)=\Theta(n^4)\). A decoder may use one representative per observed profile and no larger zero-error code, establishing the coding corollary. \(\square\)

## Verification

The accompanying `verify.py` uses direct position-pair enumeration and, independently, a four-statistic reconstruction of every gapped profile for every binary word of lengths \(1\) through \(12\). It also checks distinctness of the full parameterized witness collection at lengths \(100,200,300,400,500\). Running `python3 verify.py` raises an assertion upon any disagreement. These finite checks are independent corroboration; the arbitrary-length statement follows from the preceding proof.

## Relationship to prior work

Golm, Nahvi, Gabrys and Milenkovic introduced gapped-deck reconstruction and investigated when *colliding words first exist* for varying deck order. Rigo, Stipulanti and Whiteland developed gapped-binomial equivalence and complexity for factors of specific infinite sequences, notably Thue–Morse and Sturmian words. Their binary characterization of pair-deck equivalence provides relevant structural context, but does not state this fourth-degree number of observation classes for *all* binary words of each length. Classical \(2\)-abelian equivalence records consecutive substring multiplicities rather than ordered pairs with an intervening position; its class counts are not the present profile counts. The distinction is essential: the sharp exponent here requires both the run-structure upper bound and the four-parameter coprime-block lower construction.

## Limitations

The result establishes the sharp polynomial exponent, not the leading asymptotic constant, eventual quasipolynomiality, an exact formula for \(Q(n)\), or the size distribution of ambiguity classes. The explicit lower-bound constants are not optimized. Any truly equivalent enumeration or stronger previously published theorem would affect the originality assessment; absence from the inspected material does not prove global novelty.

## References

1. J. Golm, M. Nahvi, R. Gabrys, O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671, first posted 29 January 2022. https://arxiv.org/abs/2201.12671 .
2. M. Rigo, M. Stipulanti, M. A. Whiteland, *Gapped Binomial Complexities in Sequences*, ISIT 2023. https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf .
3. J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, *\(k\)-Abelian Equivalence and Rationality*, 2017. https://www.utupub.fi/server/api/core/bitstreams/6c4a5f5d-c647-410d-9a5f-bf5b229bfde6/content .
