# Exact minimum string-attractor profile of the powers-of-two characteristic word

## Finding

Let \(c=c_0c_1c_2\cdots\) be the binary word given by \(c_i=1\) precisely when \(i+1\) is a power of two, with indexing from zero. For each positive integer \(n\), let \(\gamma(n)\) denote the minimum cardinality of a **string attractor** for the prefix \(c_0\cdots c_{n-1}\): a set of positions such that every distinct nonempty contiguous factor has at least one occurrence crossing a chosen position.

**Theorem (exact profile).** For all positive integers \(n\),
\[
\gamma(n)=\begin{cases}
1,&1\le n\le2,\\
2,&3\le n\le5,\\
3+j,&6\cdot4^j\le n<24\cdot4^j\quad(j\in\mathbb Z_{\ge0}).
\end{cases}
\]
Thus the only jumps, after the initial jump at length three, occur precisely at lengths \(6,24,96,384,\ldots\). In particular, the known explicit attractor-size upper bounds for this word are simultaneously optimal at every prefix length, not merely asymptotically sharp.

## Assumptions and scope

Indices, intervals and chosen attractor positions are zero-based. A factor is contiguous, not a scattered subsequence; its different occurrences may overlap. The prefix is linear, not circular. All alphabet symbols are the literal binary symbols. The claim concerns **minimum cardinality**, not the number or uniqueness of minimum attractors.

For \(i\ge0\), write \(t_i=2^i-1\). The ones are exactly at \(t_i\); the consecutive gaps have lengths \(t_{i+1}-t_i=2^i\) and contain \(2^i-1\) zeros. When \(m\ge2\) and \(2^m\le n<2^{m+1}\), write \(n=2^m+h\), where \(0\le h<2^m\), and write \(W_m=c_0\cdots c_{2^m-1}\). The prefix of length \(n\) is \(W_m0^h\).

## Proof

### 1. Two explicit attractors

If \(0\le h<2^{m-1}\), take
\[
S_{m,h}^{\mathrm{low}}=
\{t_i:1\le i\le m-2,\ i\ \mathrm{odd}\}
\cup\{t_{m-1},t_m-1\}.
\]
This set has \(\lceil m/2\rceil+1\) elements. For each distinct factor, select an occurrence as follows.

* A factor consisting exclusively of zeros has length at most \(2^{m-1}-1\) and occurs in the last complete zero gap, crossing \(t_m-1\).
* A factor with exactly one one has the form \(0^a10^b\). If an occurrence is centered at any one before \(t_m\), its available left and right zero runs are dominated by those of the one at \(t_{m-1}\), so it can be centered there and crosses the selected \(t_{m-1}\). If it is centered at \(t_m\) and \(a\ge1\), its occurrence crosses \(t_m-1\). In the remaining case \(a=0\), its trailing-zero count satisfies \(b\le h<2^{m-1}\), so it also occurs centered at \(t_{m-1}\).
* A factor containing at least two ones contains a consecutive pair \(t_i,t_{i+1}\). Every such pair of ones, for \(0\le i<m\), meets one of the selected odd-indexed ones or the extra selected \(t_{m-1}\).

Thus \(S_{m,h}^{\mathrm{low}}\) is a string attractor.

If \(2^{m-1}\le h<2^m\), take
\[
S_{m,h}^{\mathrm{high}}=
\{t_i:1\le i\le m-1,\ i\ \mathrm{odd}\}
\cup\{t_m-1,t_m+1\}.
\]
This has \(\lfloor m/2\rfloor+2\) elements. Every zero-only factor occurs in the appended final zero run and crosses \(t_m+1\). All factors containing exactly one one can be centered at \(t_m\), because its left zero run and the appended right zero run dominate both runs of every earlier one. If the factor is longer than one letter, it crosses either \(t_m-1\) or \(t_m+1\); the length-one factor \(1\) crosses any selected odd-indexed one. Finally, every consecutive pair of ones is met by an odd-indexed selected one, except possibly the last pair, whose gap contains \(t_m-1\). This proves the second upper bound.

### 2. Projection lemma for a trailing zero run

For every \(m\ge2\) and \(0\le h<2^m\),
\[
\gamma(W_m0^h)\ge\gamma(W_m).
\]
Indeed, start with any attractor \(S\) of \(W_m0^h\). Replace **each** selected position in the appended zero block by the single position \(t_{m-1}+1=2^{m-1}\), retaining all selected positions inside \(W_m\). We show that the resulting set is an attractor for \(W_m\), with no greater cardinality.

Consider a nonempty factor \(f\) of \(W_m\) that was covered solely by an occurrence meeting a chosen position in the appended block. Such an occurrence must extend past the last one \(t_m\). If \(f\) contained at least two ones, its last two ones in this occurrence would be \(t_{m-1}\) and \(t_m\), separated by the uniquely largest consecutive-one gap \(2^{m-1}\). Every occurrence of \(f\) inside \(W_m\) would then have to use this same pair, but could not extend beyond \(t_m\), a contradiction. Hence \(f\) has at most one one.

If \(f=0^\ell\), its occurrence inside \(W_m\) implies \(\ell\le2^{m-1}-1\). It occurs in the complete last zero gap starting at \(t_{m-1}+1\), crossing the replacement position. Otherwise \(f=0^a10^b\), with \(b\ge1\) because its chosen occurrence reaches the appended block. The occurrence inside \(W_m\) must be centered at some earlier one and hence has \(a\le2^{m-2}-1\) and \(b\le2^{m-1}-1\). The same factor consequently occurs centered at \(t_{m-1}\), crossing \(t_{m-1}+1\). This proves the projection lemma.

### 3. Disjoint factor certificates at dyadic lengths

If several distinct factors have all their occurrences confined to pairwise disjoint position intervals, any attractor must choose at least one position from each interval. The factors below give matching lower bounds, and the distinct consecutive-one gaps ensure the uniqueness claims.

For each \(i\ge0\), the factor \(U_i=1\,0^{2^i-1}\,1\) occurs **exactly once** in any prefix containing both \(t_i\) and \(t_{i+1}\), namely on \([t_i,t_{i+1}]\).

For even \(m=2k\ge4\), in \(W_m\) choose the \(k\) factors \(U_i\) with \(i=0,2,\ldots,m-2\). Their occurrence intervals are disjoint. Add the factor \(V_m=0^{2^{m-1}-2}1\), which occurs uniquely at \(t_m\) on \([t_{m-1}+2,t_m]\). Its required interval is disjoint from all the former intervals. Hence \(\gamma(W_m)\ge k+1\).

For odd \(m=2k+1\ge3\), choose the \(k\) factors \(U_i\) with \(i=0,2,\ldots,m-3\). Add \(F_m=0^{2^{m-2}-1}10\), uniquely centered at \(t_{m-1}\) **within \(W_m\)**, with interval \([t_{m-2}+1,t_{m-1}+1]\); and add \(V_m\), uniquely centered at \(t_m\), with interval \([t_{m-1}+2,t_m]\). All \(k+2\) occurrence intervals are disjoint. Thus \(\gamma(W_m)\ge k+2\). The projection lemma transfers both dyadic lower bounds to every \(W_m0^h\).

For \(m=2\), \(W_2=1101\); its factors \(11\) and \(01\) occur only at disjoint intervals \([0,1]\) and \([2,3]\). Therefore \(\gamma(W_2)\ge2\), also inherited by trailing-zero extensions.

### 4. The additional lower bound in the second half of an even dyadic block

Let \(m=2k\ge4\) and \(h\ge2^{m-1}\). There are \(k+2\) independently required, disjoint regions:

1. The unique occurrences of \(U_0,U_2,\ldots,U_{m-4}\), giving \(k-1\) regions ending no later than \(t_{m-3}\).
2. The unique occurrence of \(1\,0^{2^{m-2}-1}\,10\) on \([t_{m-2},t_{m-1}+1]\).
3. The unique occurrence of \(V_m=0^{2^{m-1}-2}1\) on \([t_{m-1}+2,t_m]\).
4. Every occurrence of \(0^{2^{m-1}}\) lies completely in the appended final zero run \([t_m+1,n-1]\), since all earlier zero runs are shorter.

The four groups force \((k-1)+1+1+1=k+2\) distinct attracting positions. For \(m=2\) and \(h\ge2\), the same three-region argument uses the factors \(11\), \(01\), and \(00\), whose occurrences are confined respectively to \([0,1]\), \([2,3]\), and the appended suffix \([4,n-1]\). Therefore the high-block upper bound is sharp for every even \(m\ge2\).

### 5. Evaluation and initial cases

For even \(m=2k\), the first half of the block \(2^m\le n<2^{m+1}\) has optimal value \(k+1\), and the second half has optimal value \(k+2\). For odd \(m=2k+1\), both halves have optimal value \(k+2\). These values produce the jumps at \(6\cdot4^j\), for all \(j\ge0\). Directly, the first two prefixes have minimum size one, the length-three prefix has size two, and the preceding proof covers all lengths at least four. The theorem follows. \(\square\)

## Verification

The standalone file `verify.py` uses only the Python standard library. Running `python3 verify.py` checks actual complete factor coverage by the displayed explicit attractors for every length from one through 184 and at further dyadic threshold examples, verifies the prescribed disjoint lower-bound occurrence regions at those lengths (using the dyadic projection boundary for odd depths), and independently exhausts all chosen-position subsets for lengths one through fourteen. It prints `VERIFY_OK` on success. These finite checks are reproducibility tests; the argument above proves the universal statement.

## Relationship to prior work

Schaeffer and Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, Section 6, Theorem 8, explicitly provide attractors of sizes \(j+2\) and \(j+3\) in the two respective powers-of-four ranges **for this exact word**; their text immediately following Theorem 8 explicitly states that only an upper bound is obtained and that a matching lower bound needs other techniques. The present finding is the **matching lower-bound theorem and hence exact minimum cardinality at all lengths**, not a new claim to those pre-existing upper bounds. Restivo, Romana and Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376, develops attractor profiles and general classifications but does not give this exact sparse-word profile in the inspected material. Mantaci and colleagues, *String Attractors and Combinatorics on Words*, arXiv:1907.04660, studies other finite word families; its results do not imply this formula. The simple-Parry word studies arXiv:2302.13647 and arXiv:2511.00650 concern different morphic families.

## Limitations

The statement applies only to the binary characteristic word of positive powers of two, with zero-based indexing and linear prefixes. It does not classify every minimum attractor, treat all automatic words, or determine optimal constructions under other notions of attraction. The scientific proof and finite verifier do not certify publication priority; an unindexed equivalent or unpublished related result remains possible.

## References

1. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (first publicly available December 12, 2020), especially §6 and Theorem 8. https://arxiv.org/pdf/2012.06840
2. A. Restivo, G. Romana and M. Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376 (June 1, 2022). https://arxiv.org/pdf/2206.00376
3. S. Mantaci, A. Restivo, G. Romana, G. Rosone and M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (July 10, 2019). https://arxiv.org/pdf/1907.04660
4. F. Gheeraert, G. Romana and M. Stipulanti, *String attractors of some simple-Parry automatic sequences*, arXiv:2302.13647 (February 27, 2023). https://arxiv.org/pdf/2302.13647
5. L. Dvořáková and V. Moravcová, *Attractors of sequences coding β-integers*, arXiv:2511.00650 (November 2025). https://arxiv.org/pdf/2511.00650
