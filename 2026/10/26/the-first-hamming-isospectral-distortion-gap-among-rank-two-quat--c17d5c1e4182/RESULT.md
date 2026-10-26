# The first Hamming-isospectral distortion gap among rank-two quaternary codes

## Finding

Use **linear equivalence** to mean equivalence under coordinate permutations and nonzero coordinate scalings over the stated field, **without field automorphisms**. Let \(\mathcal D(C,C')\) be the minimum multiplicative Hamming-weight distortion of an invertible linear map from one linear code to the other, as in Bennett--Fox--Morrell [1].

**Theorem (sharp alphabet and length threshold, with exact distortion).** For \(q=2\) or \(3\), any two \(q\)-ary linear codes of dimension two and the same length having identical ordinary Hamming weight enumerators are linearly equivalent. For \(q=4\), every pair of dimension-two, equal-length, Hamming-isospectral codes of length at most nine is linearly equivalent, but such inequivalent pairs exist at length ten. In fact, the weight enumerator

\[
1+3(z^{10}+z^9+z^8+z^7+z^6)
\]

has exactly two linear-equivalence classes of quaternary \([10,2]\) codes, and their mutual distortion is exactly \(100/81\).

More generally, for every integer \(t\ge 0\), there are two linearly inequivalent quaternary \([5t+10,2,4t+6]\) codes \(C_t,C'_t\) with the same ordinary Hamming weight enumerator, whose distortion is

\[
\boxed{\mathcal D(C_t,C'_t)=\left(\frac{4t+10}{4t+9}\right)^2.}
\]

Thus these inequivalent, Hamming-isospectral pairs have distortion strictly above one but arbitrarily close to one as \(t\to\infty\).

## Assumptions and scope

Work over \(\mathbb F_4=\{0,1,\omega,\omega^2\}\) with \(\omega^2=\omega+1\). Write the five points of \(\mathbb P^1(\mathbb F_4)\), in order, as \((\infty,0,1,\omega,\omega^2)\), represented by the nonzero column vectors

\[
v_0=(0,1)^\mathsf T,\quad v_1=(1,0)^\mathsf T,\quad v_2=(1,1)^\mathsf T,\quad
v_3=(1,\omega)^\mathsf T,\quad v_4=(1,\omega^2)^\mathsf T.
\]

For \(t\ge0\), let \(G_t\) be a two-row generator matrix with \(t+j\) copies of \(v_j\), for \(j=0,\ldots,4\), and let \(G'_t\) have the same columns except that the multiplicities at \(v_0,v_1\) are interchanged. Their row spaces are \(C_t,C'_t\). Both matrices have rank two, and their length is \(5t+10\). The notation \([n,k,d]_q\) specifies length, dimension and minimum Hamming distance.

For an invertible \(\mathbb F_q\)-linear map \(T:C\to C'\), define

\[
\mathcal D_T(C,C')=
\frac{\max_{x\in C\setminus\{0\}}\operatorname{wt}(Tx)/\operatorname{wt}(x)}
{\min_{x\in C\setminus\{0\}}\operatorname{wt}(Tx)/\operatorname{wt}(x)},
\qquad \mathcal D(C,C')=\min_T\mathcal D_T(C,C').
\]

All codes in the theorem are linear over their indicated fields; only \(\mathbb F_q\)-linear maps enter \(\mathcal D\). In particular, a nontrivial field automorphism is not an allowed linear equivalence.

## Proof

**1. The projective-weight dictionary.** Given a two-row generator matrix over \(\mathbb F_q\), let \(h\) be its number of zero columns, \(N=n-h\), and let \(m(P)\) count its nonzero columns in each direction \(P\in\mathbb P^1(\mathbb F_q)\). Each nonzero row-message direction annihilates precisely one projective column direction. Its corresponding codeword has weight \(w(P)=N-m(P)\), after using the annihilator bijection to label directions. Every projective message direction comprises exactly \(q-1\) nonzero codewords, so the ordinary weight enumerator recovers the multiset of the \(q+1\) weights. Moreover \(\sum_P w(P)=qN\); thus the enumerator also recovers \(N,h\) and the unordered multiplicity multiset \(\{m(P)\}\). Row-basis changes induce \(\operatorname{PGL}_2(q)\) on the projective line, while coordinate permutation and scaling merely reorder columns within the projective types. Therefore two codes are monomially equivalent exactly when their column-multiplicity functions match under \(\operatorname{PGL}_2(q)\), with equal zero-column counts.

**2. The sharp field-size boundary.** The faithful projective group has order \(q(q^2-1)\). For \(q=2,3\), this equals \((q+1)!\), so \(\operatorname{PGL}_2(2)=S_3\) and \(\operatorname{PGL}_2(3)=S_4\) as permutation groups. Hence equal enumerators allow a projective permutation matching every multiplicity and imply linear equivalence.

For \(q=4\), projective translations \(z\mapsto z+a\), dilations \(z\mapsto bz\), and inversion \(z\mapsto1/z\) generate the projective fractional-linear group. All three kinds of generator are even permutations of the five points: a nonzero translation is a product of two transpositions, a nonidentity dilation is a three-cycle, and inversion is a product of two transpositions. Since the group has order \(4(4^2-1)=60\), its action is exactly \(A_5\). Two assignments of the same five multiplicities are therefore inequivalent precisely when the multiplicities are all distinct and the matching permutation is odd: with a repeated value an odd matching can be made even by swapping two equal entries. Five distinct nonnegative multiplicities require at least \(0+1+2+3+4=10\) nonzero columns. This proves equivalence through length nine, and at length ten with five distinct multiplicities the unique unordered profile is \(\{0,1,2,3,4\}\). Its arrangements form exactly two \(A_5\)-orbits, proving the minimality and exact two-class statement.

**3. Matching family and exact Hamming spectra.** In \(G_t\), the five column multiplicities are \((t,t+1,t+2,t+3,t+4)\); in \(G'_t\) the first two are swapped. The corresponding five projective message weights in either code, as an unordered multiset, are \(w_j=4t+10-j\) for \(j=0,\ldots,4\). Every projective message line contains three nonzero words. Consequently both weight enumerators equal

\[
1+3\sum_{j=0}^4 z^{4t+10-j},
\]

and both codes have minimum distance \(4t+6\). Their ordered multiplicities differ by a single transposition, so no even projective transformation matches them: the codes are not linearly equivalent.

**4. Optimal distortion.** Label the five source message directions so their positive weights satisfy \(w_0>w_1>\cdots>w_4\). Under any invertible \(\mathbb F_4\)-linear map the direction permutation is even; the target weights are obtained from the source labels by one odd transposition. Hence the five weight ratios for any allowed map take the form \(r_j=w_{\rho(j)}/w_j\), where \(\rho\) is an odd permutation; conversely every such odd permutation is realized. Since \(\rho\) is not the identity, there is an index moved toward a larger weight and another moved toward a smaller weight. With consecutive integers \(w_j=4t+10-j\), the smallest possible ratio of two distinct weights that is greater than one is \(w_0/w_1=(4t+10)/(4t+9)\), and the largest possible ratio below one is its reciprocal. Therefore

\[
\max_j r_j\ge \frac{4t+10}{4t+9},\qquad
\min_j r_j\le \frac{4t+9}{4t+10},
\]

so every allowable map has distortion at least \(((4t+10)/(4t+9))^2\). The identity matching between the two prescribed generator bases induces exactly the transposition of the first two weights: its ratios are \(w_1/w_0,w_0/w_1,1,1,1\), achieving this lower bound. This proves the exact formula and its limit. At \(t=0\), it gives \(100/81\), as asserted.

## Verification

The standalone `verify.py` independently implements \(\mathbb F_4\) arithmetic, constructs both generator matrices directly, and enumerates all \(180\) invertible two-by-two \(\mathbb F_4\) matrices and the induced \(60\) projective permutations. It computes Hamming weights from actual codeword coordinates, rather than solely from the projective multiplicity formula. For \(t=0,1,2,3,7,20\), it checks equal weight enumerators and finds the exact minimum distortions \(100/81,196/169,324/289,484/441,1444/1369,8100/7921\). It also verifies the full symmetric projective actions for \(q=2,3\), the parity property for \(q=4\), and the nonexistence of five distinct nonnegative multiplicities summing to less than ten. The accompanying output ends `VERIFY_OK`.

The finite checks are not the proof for unbounded \(t\) or arbitrary codes; those cases follow from the four analytic steps above.

## Relationship to prior work

Bennett, Fox and Morrell [1] introduce the precise code-distortion metric, give general complexity and approximation results, and characterize distortion one via equivalence after unary scaling. The present result concerns a different, sharper question: how ordinary Hamming spectra can fail to determine linear equivalence and how closely the two inequivalent rank-two quaternary codes approach distortion one, with an exact all-length family. Their general exact-search algorithm does not provide this structural threshold or the closed formula.

Bouyukliev, Bouyuklieva and Kurz [2] use projective point multisets to classify linear codes. Importantly, their stated equivalence convention **also allows field automorphisms**. Here that changes the question: the nontrivial Frobenius automorphism of \(\mathbb F_4\) induces an odd permutation of the five projective points, so the displayed pairs become equivalent if semilinear transformations are admitted. The positive distortion gap is for the strictly \(\mathbb F_4\)-linear metric in [1].

## Limitations

This is a dimension-two theorem and an explicit infinite quaternary family; it does not classify code distortion in higher dimension or give a uniform nonunit distortion gap for arbitrary inequivalent codes. The isospectral exceptional pairs are semilinearly equivalent, despite not being monomially equivalent over \(\mathbb F_4\). Equivalence under Frobenius is not covered by the metric used here. An equivalent older projective-line classification may exist, while the precise distortion values and sharp length threshold were not identified in the inspected sources. No independent mathematical audit has been performed.

## References

1. H. Bennett, M. Fox and B. Morrell, *The Code Distortion Problem*, arXiv:2607.26261 (first publicly posted 2026-07-28); APPROX/RANDOM 2026, LIPIcs 392, article 24, DOI: 10.4230/LIPIcs.APPROX/RANDOM.2026.24. Public full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol392-approx-random2026/LIPIcs.APPROX-RANDOM.2026.24/LIPIcs.APPROX-RANDOM.2026.24.pdf.
2. I. Bouyukliev, S. Bouyuklieva and S. Kurz, *Computer classification of linear codes*, 2020; public full text: https://epub.uni-bayreuth.de/id/eprint/4618/1/LinCodeAugmentation_arxiv.pdf.
3. MSC2020, classification 94B05: Linear codes (general theory), https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=94B05.
