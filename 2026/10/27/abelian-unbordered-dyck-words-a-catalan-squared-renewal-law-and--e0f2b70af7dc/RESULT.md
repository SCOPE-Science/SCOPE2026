# Abelian-unbordered Dyck words: a Catalan-squared renewal law and limiting density

## Finding
A Dyck word is a binary word with equally many zeros and ones and nonnegative excess of zeros over ones in each prefix. Its **semilength** is half its ordinary length. Two equal-length words are *abelian equivalent* when they have the same number of zeros. A nonempty proper prefix that is abelian equivalent to the suffix of the same length is an *abelian border*.

Put \(C_n=\frac{1}{n+1}\binom{2n}{n}\), \(C(z)=\sum_{n\ge0}C_nz^n=\frac{1-\sqrt{1-4z}}{2z}\), and
\[
S(t)=\sum_{j\ge0}C_j^2t^j.
\]
Let \(U_n\) denote the number of Dyck words of semilength \(n\) having no nonempty proper abelian border, with \(U_0=1\) for the empty word. Then, as an identity of formal power series,
\[
\boxed{U(z)=\sum_{n\ge0}U_nz^n=\frac{C(z)}{S(z^2)}.}
\]
More precisely, set \(E_0=0\) and define \(E_j\) for \(j\ge1\) through
\[
E(t)=\sum_{j\ge1}E_jt^j=1-\frac1{S(t)}.
\]
For every \(n\ge1\) and \(1\le j\le\lfloor n/2\rfloor\), the number of semilength-\(n\) Dyck words whose **shortest** abelian border has ordinary length \(2j\) is exactly \(E_j C_{n-2j}\). No shortest abelian border of a Dyck word has odd length. The corresponding two-variable series, with \(y\) recording half the shortest border length, is
\[
\sum_{n\ge0}\sum_{j\ge1}E_j C_{n-2j} z^n y^j
=C(z)\left(1-\frac1{S(yz^2)}\right),
\]
where terms with negative Catalan indices are omitted. In particular,
\[
\lim_{n\to\infty}\frac{U_n}{C_n} = \frac1{S(1/16)}
=\frac{\pi}{16-4\pi}\approx 0.91494809158.
\]
The initial values are \(U_0,\ldots,U_{12}=1,1,1,4,9,34,94,354,1079,4076,13156,49896,167238\). The first values of \(E_j\), starting at \(j=1\), are \(1,3,18,141,1280,12778\).

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\), with zero interpreted as an up-step and one as a down-step. Words have indexed positions, not equivalence classes modulo cyclic rotation. Abelian borders are proper, nonempty, and contiguous at both ends; they are not scattered-subsequence borders and need not be literal word borders. Results hold for all semilengths \(n\ge0\), and for the shortest-border distribution when \(1\le j\le\lfloor n/2\rfloor\). \(C_0=1\), and the empty word is included by convention.

## Proof
**1. Height-return criterion.** For a Dyck word \(w\) of ordinary length \(2n\), let \(H_i\) be its height after \(i\) steps. Its first \(k\) symbols contain \((k+H_k)/2\) zeros, while its final \(k\) symbols contain \((k-H_{2n-k})/2\) zeros (the total number of zeros is \(n\)). Thus its prefix and suffix of length \(k\) are abelian equivalent exactly when
\[
H_k+H_{2n-k}=0.
\]
Every Dyck height is nonnegative, so this holds precisely when both heights are zero. Every return to zero occurs at an even index. Moreover, a border of length \(k\) implies one of complementary length \(2n-k\). Consequently, a shortest border, when present, has length \(2j\), with \(1\le j\le\lfloor n/2\rfloor\), and occurs exactly when \(H_{2j}=H_{2n-2j}=0\) with no earlier symmetric pair of returns.

**2. First paired-return convolution.** Consider an ordered pair \((A,B)\) of Dyck words, each of semilength \(j\). The pair admits a *paired return at size* \(i\), \(1\le i\le j\), if the prefix of \(A\) of semilength \(i\) and the suffix of \(B\) of semilength \(i\) are each Dyck words. Size \(j\) is always a paired return, so there is a unique smallest size. Let \(E_i\) count pairs of semilength \(i\) with no paired return of smaller positive size. Splitting \((A,B)\) at its smallest paired return size \(i\) gives uniquely
\[
A=A_0A_1,\qquad B=B_1B_0,
\]
where \((A_0,B_0)\) is an \(E_i\)-pair and \(A_1,B_1\) are arbitrary Dyck words of semilength \(j-i\). Conversely, such a concatenation has smallest paired return \(i\). Therefore
\[
C_j^2=\sum_{i=1}^j E_i C_{j-i}^2\qquad(j\ge1).
\]
Together with \(S(0)=1\), this is \(S(t)-1=E(t)S(t)\), giving \(E(t)=1-1/S(t)\).

**3. Decomposition of abelian-bordered Dyck words.** If \(w\) has shortest abelian border of length \(2j\), the two symmetric returns split it uniquely as \(w=AMB\), where \(A\) and \(B\) are each Dyck words of semilength \(j\), \(M\) is an arbitrary Dyck word of semilength \(n-2j\), and \((A,B)\) is an \(E_j\)-pair. Conversely, each such triple has shortest abelian border \(2j\). Hence its count is \(E_jC_{n-2j}\). Summing over \(j\) yields
\[
C(z)-U(z)=C(z)E(z^2),
\]
so \(U(z)=C(z)(1-E(z^2))=C(z)/S(z^2)\). Marking \(j\) by \(y\) gives the bivariate identity.

**4. Limiting proportion and exact constant.** By Stirling's formula \(C_j^2/16^j=O(j^{-3})\). Hence \(S(1/16)\) converges, is positive, and its derivative from the left is finite. The hypergeometric representation
\[
S(t)={}_3F_2\!\left(\begin{matrix}1/2,1/2,1\\2,2\end{matrix};16t\right)
\]
has its nearest possible finite singularity at \(t=1/16\), with local expansion consisting of a constant, a linear term, and an \(O((1-16t)^2\log(1-16t))\) remainder. The identity \(S(1/16)-1<1\) follows, for example, from \(C_j\le4^j/(j+1)\), giving a strictly convergent bound \(\sum_{j\ge1}(j+1)^{-2}<1\). Thus \(S(z^2)\ne0\) for \(|z|\le1/4\), with continuation near that disk's boundary. At \(z=1/4\), \(C(z)=2-2\sqrt{1-4z}+O(1-4z)\) and \(S(z^2)=S(1/16)+O(1-4z)\); at \(z=-1/4\) the denominator's first nonanalytic term is of order \((1+4z)^2\log(1+4z)\). Standard singularity transfer therefore gives \(U_n\sim C_n/S(1/16)\); the contribution from \(z=-1/4\) is lower order.

For the constant, direct cancellation using \(C_j=\binom{2j}{j}/(j+1)\) verifies, for every integer \(N\ge0\),
\[
\sum_{j=0}^{N}\frac{C_j^2}{16^j}=-4+\frac{(4N+5)\binom{2N+1}{N}^2}{16^N}.
\]
Stirling's formula makes the right-hand side tend to \(16/\pi-4\), proving \(S(1/16)=16/\pi-4\) and the asserted limit. This uses a known Catalan-square summation; no novelty is claimed for that summation alone.

## Verification
The bundled standard-library-only program `verify.py` enumerates all \(290511\) nonempty Dyck words of semilength at most \(12\). It compares literal Parikh-vector borders against paired zero-height returns, and compares each shortest-border count with \(E_jC_{n-2j}\). It independently enumerates \(19414\) ordered pairs of Dyck words (semilengths \(1\) through \(6\)) to verify the first-return pair counts. Algebraic recurrences are checked through semilength \(30\). Run with `python3 verify.py`. Its success marker is `DYCK_ABELIAN_BORDERS_PASS`. Finite checks are supporting tests, not proof for arbitrary semilength.

## Relationship to prior work
Blanchet-Sadri, Chen, and Hawes (2017) studied abelian borders in **unrestricted binary words** through Dyck-path encodings, including a formula for the number of unrestricted binary words having a shortest abelian border of prescribed length. Their encoding of a binary word by an auxiliary Dyck path does not restrict the original word itself to be a Dyck word. The present result instead enumerates abelian borders inside the Catalan family, with a different Catalan-squared renewal kernel. The 2014 study by Christodoulakis and collaborators and the 2022 survey of Fici and Puzynina establish the definition and the unrestricted setting. Habib, Shamil, and Rahman's 2021 work concerns attainable abelian border arrays of binary words rather than this restricted counting measure. An earlier exact formula for the absence of **literal** borders in Dyck words is a different invariant: literal equality entails abelian equivalence, but the converse fails.

## Limitations
This theorem concerns binary Dyck words only. It does not give the distribution of *all* abelian border lengths per word, only the shortest-border distribution and the no-border count. The limiting density is for uniformly sampled words from the complete Catalan family, not an arbitrary Dyck-generating process. An equivalent formula in unindexed literature remains possible; source and database searches cannot certify absolute originality. Independent mathematical review has not been performed.

## References
1. F. Blanchet-Sadri, K. Chen, K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, 2017, arXiv:1708.06461, https://arxiv.org/abs/1708.06461 .
2. G. Fici, S. Puzynina, *Abelian Combinatorics on Words: a Survey*, 2022, arXiv:2207.09937, https://arxiv.org/abs/2207.09937 .
3. M. Christodoulakis, M. Christou, M. Crochemore, C. S. Iliopoulos, *Abelian borders in binary words*, Discrete Applied Mathematics 171 (2014), 141–146, doi:10.1016/j.dam.2014.02.012 .
4. M. Habib, M. S. Shamil, M. S. Rahman, *Counting and Verifying Abelian Border Arrays of Binary Words*, 2021, arXiv:2111.00259, https://arxiv.org/abs/2111.00259 .
