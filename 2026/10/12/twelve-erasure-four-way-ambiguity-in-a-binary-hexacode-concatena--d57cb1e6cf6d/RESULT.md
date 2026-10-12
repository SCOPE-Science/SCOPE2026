# Twelve-erasure four-way ambiguity in a binary hexacode concatenation

## Finding
Let \(C\) be the binary \([18,6,8]\) code defined below, with six natural three-coordinate repair blocks. For an erased-coordinate set \(E\subseteq\{1,\ldots,18\}\), let \(C[E]=\{c\in C:\operatorname{supp}(c)\subseteq E\}\). Given a received word consistent with some codeword, the number of codeword completions equals \(|C[E]|\). For every erased set with \(|E|=12\), the exact numbers of sets with respectively \(1\), \(2\), and \(4\) completions are
\[
\boxed{9576,\quad8748,\quad240.}
\]
There are no twelve-erasure patterns with more than four completions. All \(240\) four-completion patterns are distinct supports of binary two-dimensional subcodes. When the six repair blocks are inspected, the nonempty block-intersection sizes, sorted in descending order, have the exact distribution
\[
(3,3,3,3):15,\qquad(3,3,2,2,2):180,\qquad(2,2,2,2,2,2):45.
\]
In particular \(d_2(C)=12\), and every binary three-dimensional subcode has support size at least \(14\). The complete rank-multiplicity and block-profile formulas, rather than the code construction, its parameters, or its ordinary weight distribution, are the finding.

## Assumptions and scope
Use \(\mathbb F_4=\{0,1,\omega,\omega^2\}\), where \(\omega^2+\omega+1=0\). Put
\[
M=\begin{pmatrix}1&\omega&\omega\\\omega&1&\omega\\\omega&\omega&1\end{pmatrix},\qquad
H=[I_3\mid M],\qquad C_4=\ker_{\mathbb F_4}H
     =\{(My,y):y\in\mathbb F_4^3\}.
\]
Replace each quaternary symbol with the binary even-weight triple \(\psi(0)=000\), \(\psi(1)=110\), \(\psi(\omega)=101\), \(\psi(\omega^2)=011\). Let \(C=\psi(C_4)\), with the six consecutive triple blocks retained as part of the code definition. The statement concerns exact subsets of the \(18\) coordinates, without identification under automorphisms; received words are assumed to be consistent with at least one codeword. All ranks below are binary unless explicitly marked \(\mathbb F_4\).

## Proof
**1. Outer structure and minimum words.** Every three columns of \(H\) are linearly independent: this follows directly by checking its \(\binom63=20\) minors (all are nonzero in \(\mathbb F_4\)). Thus \(C_4\) is \([6,3,4]_4\) MDS. Every fixed four-element coordinate set \(A\subseteq\{1,\ldots,6\}\) supports a unique one-dimensional quaternary subcode of \(C_4\); its three nonzero words have support exactly \(A\). Hence there are \(15\cdot3=45\) quaternary words of weight four. For any five-element coordinate set, the supported subcode has dimension two, so its \(15\) nonzero words consist of the five weight-four support classes times three: there are no weight-five words. The remaining \(63-45=18\) have weight six. Every nonzero inner triple has binary weight two, giving
\[
W_C(z)=1+45z^8+18z^{12}.
\]
The columns also satisfy \(M\overline M^{\,T}=I_3\), with bar the Frobenius square. Since \(M=M^T\), the quaternary kernel code is Hermitian self-orthogonal: for all \(u,v\in C_4\),
\[
\sum_{i=1}^6 u_i\overline{v_i}=0.
\]
This can be verified by multiplying the displayed matrices, without invoking any classification theorem.

**2. The smallest binary two-space supports.** For a binary two-dimensional subspace \(P=\langle a,b\rangle\) its three nonzero words are \(a,b,a+b\), and each coordinate in its support occurs in exactly two of those three. Thus
\[
2|\operatorname{supp} P|=\operatorname{wt}(a)+\operatorname{wt}(b)+\operatorname{wt}(a+b)\ge24.
\]
Equality is equivalent to all three nonzero words having weight eight. A pair of nonzero, distinct, quaternary weight-four words with supports \(A,B\) spans such a binary plane precisely when their sum is also weight four. As \(|A|=|B|=4\) in a universe of six blocks, intersections have size \(2\), \(3\), or \(4\).

If \(A=B\), the two words are distinct nonzero multiples in the unique \(\mathbb F_4\)-line with support \(A\); the binary plane consists of all its nonzero words. There are \(\binom64=15\) such planes, and each of its four active blocks contributes all three binary coordinates. Profile: \((3,3,3,3)\).

If \(|A\cap B|=3\), Hermitian orthogonality and \(v_i^2=v_i^{-1}\) for \(v_i\ne0\) yield \(\sum_{i\in A\cap B}u_i/v_i=0\). Three nonzero elements of \(\mathbb F_4\) sum to zero exactly when they are the three distinct elements \(1,\omega,\omega^2\), so there is exactly one common coordinate at which \(u_i=v_i\), and their sum has quaternary weight four. Each of the \(\binom65\binom52=60\) unordered support pairs has \(3\cdot3=9\) unordered choices of a nonzero word from each of the two support lines. Every resulting binary plane is counted three times, one for each pair of its nonzero words. Thus there are \(60\cdot9/3=180\) planes. The two common blocks where symbols differ each contribute three binary coordinates to the plane support; the one shared block where symbols agree and two blocks outside the intersection each contribute two. Profile: \((3,3,2,2,2)\).

If \(|A\cap B|=2\), Hermitian orthogonality forces the two nonzero ratios \(u_i/v_i\) to coincide. Precisely three of the nine choices of nonzero words on each unordered pair of four-support lines make this common ratio equal to one; both shared positions then cancel, and the sum has quaternary weight four. There are \(\binom62\binom42/2=45\) unordered four-support pairs with intersection two. Dividing again by the three word pairs per binary plane gives \(45\cdot3/3=45\) planes. Both cancelled overlap positions and all four exclusive positions contribute two binary coordinates each. Profile: \((2,2,2,2,2,2)\).

All \(240\) planes above have union support exactly twelve. No other plane does, because the equality condition in the binary support identity is necessary.

**3. Distinct masks and exhaustive counts.** Every binary three-dimensional subcode \(D\subseteq C\) satisfies
\[
4|\operatorname{supp}D|=\sum_{0\ne c\in D}\operatorname{wt}(c)\ge7\cdot8=56,
\]
so \(|\operatorname{supp}D|\ge14\). Two different twelve-support planes cannot have the same support, since together they span a three-space supported on that same twelve-set. Hence the \(240\) planes yield \(240\) distinct masks with ambiguity dimension two, and no mask of size twelve can have larger ambiguity.

For all twelve-coordinate masks, count incidences with nonzero codewords whose support fits inside. Each of \(45\) weight-eight words is contained in \(\binom{10}{4}=210\) masks, and each of the \(18\) weight-twelve words in one. Thus the incidence total is \(45\cdot210+18=9468\). Each ambiguity-dimension-one mask contributes one incidence; each dimension-two mask contributes three. Therefore the count of dimension-one masks is \(9468-3\cdot240=8748\). Finally, \(\binom{18}{12}=18564\) gives \(18564-8748-240=9576\) masks of dimension zero. This completes the proof for all erased sets of the prescribed size.

## Verification
The standalone `verify.py` works with Python 3 standard-library modules only. Running `python3 verify.py` must print `VERIFY_OK`. It builds \(\mathbb F_4\), checks every three-column minor, verifies the Hermitian identity, reconstructs the \(64\) codewords, and enumerates the \(651\) binary two-spaces and their support profiles. Separately, for **all** \(18564\) twelve-erasure masks it computes the rank of the six-column un-erased binary generator restriction, checks the resulting completion dimension against direct codeword inclusion, and confirms the exact histogram \((9576,8748,240)\). The mathematical proof above establishes the structural classification; finite enumeration is an independent finite verification, not an argument about unstated larger codes.

## Relationship to prior work
Jin and Fu construct this locality-two concatenation and give the \([18,6,8]\) parameters and ordinary weight enumerator in Example 6.5 of their 2026 work. The quaternary hexacode, its Hermitian structure, and the binary code itself are classical, not new. Bouyukliev and collaborators' 2006 classification includes two \([18,6,8]\) self-orthogonal binary codes, with one having the same ordinary weight enumerator; Kurz, Landjev and Rousseva (2026) consider generalized weights of optimal codes, including this parameter regime. Those facts are compatible with the present theorem but do not themselves specify the number of four-completion masks or their three repair-block profiles. This result is restricted to the explicitly defined six-block concatenation and makes no claim that \(d_2(C)=12\) alone is novel.

## Limitations
The code is finite and the claim is exact for twelve erasures; no asymptotic coding bound, unique identification of an equivalence class from its weight enumerator, or decoding algorithm is claimed. The structural block profile refers to the specified concatenation partition, not every coordinate permutation. Literature coverage cannot exclude an earlier unindexed computation of the same erasure-rank distribution or an implicit specialization of a stronger matroid support-enumerator theorem. Independent verification beyond the included checks has not been performed.

## References
1. H. Jin and F.-W. Fu, *Constructions of locally repairable codes via concatenated codes*, arXiv:2605.04618 (first public version, 6 May 2026), §3 and Example 6.5. https://arxiv.org/abs/2605.04618
2. I. Bouyukliev, S. Bouyuklieva, T. A. Gulliver and P. R. J. Östergård, *Classification of Optimal Binary Self-Orthogonal Codes*, Journal of Combinatorial Mathematics and Combinatorial Computing **59** (2006), 33–87. https://combinatorialpress.com/article/jcmcc/Volume%20059/vol-059-paper%203.pdf
3. S. Kurz, I. Landjev and A. Rousseva, *Optimal codes and arcs for the generalized Hamming weights*, arXiv:2601.00250 (2026). https://arxiv.org/abs/2601.00250
