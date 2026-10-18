# Exact two-deck spectra and fiber multiplicities with distinct marker letters

## Finding
Let \(A,B\ge1\) and \(r\ge1\) be integers. Among all words with \(A\) occurrences of \(a\), \(B\) occurrences of \(b\), and exactly one occurrence of each of \(r\) other, individually distinguishable symbols \(c_1,\ldots,c_r\), the exact number of distinct length-two scattered-subsequence decks is
\[
D_2(A,B;r)=r!\binom{A+r}{r}\binom{B+r}{r}\left(1+\frac{AB}{r+1}\right).\tag{1}
\]
Moreover, **every nonempty deck fiber can be enumerated exactly** as follows. The deck identifies a unique order of the marker symbols and nonnegative binary gap compositions \(\mathbf a=(a_0,\ldots,a_r)\), \(\mathbf b=(b_0,\ldots,b_r)\) summing respectively to \(A\) and \(B\). Put
\[
H=\sum_{0\le s<t\le r}a_sb_t,\qquad S=\sum_{s=0}^{r}a_sb_s.
\]
For this marker order and these compositions, the feasible values of the deck coordinate \(K=\#_{ab}\) are **exactly all integers** in \([H,H+S]\). The number of words with that particular deck is
\[
[z^{K-H}]\prod_{s=0}^r {a_s+b_s\brack a_s}_{z},\tag{2}
\]
where the Gaussian binomial \({p+q\brack p}_{z}\) is the generating polynomial of binary words with \(p\) letters \(a\) and \(q\) letters \(b\), weighted by their number of scattered \(ab\) subsequences. Every feasible deck has a nonempty fiber, so (1) is also the exact maximum number of words distinguishable by a two-deck observation in this composition class.

## Assumptions and scope
A *scattered subsequence* is obtained by selecting positions in increasing order, not necessarily consecutively. The *length-two deck* \(\mathcal D_2(w)\) is the vector of counts \(\#_{xy}(w)\) for all ordered alphabet pairs \((x,y)\), where \(\#_{xy}(w)\) counts index pairs \(i<j\) with \(w_i=x\) and \(w_j=y\). Symbols \(c_1,\ldots,c_r\) are different labeled symbols, each occurring exactly once, rather than indistinguishable copies of one marker. Every word in the stated composition class has length \(A+B+r\). Counts include same-letter pairs, and word identity is by literal symbol sequence. The result is for decks of **scattered length-two subsequences**, not adjacent-pair multispectra or substring counts.

## Proof
**Marker reconstruction.** Fix any word in the composition class. For two distinct markers \(c_i,c_j\), exactly one of \(\#_{c_ic_j}\) and \(\#_{c_jc_i}\) is one, and the other is zero. Thus the deck recovers the full strict order in which all markers appear. Write this order as \(m_1,\ldots,m_r\), and decompose the word uniquely as
\[
w=u_0m_1u_1m_2\cdots m_ru_r,
\]
where every \(u_s\) is a binary word. Let \(a_s=\#_a(u_s)\) and \(b_s=\#_b(u_s)\). For each \(m_j\), the deck coordinate \(\#_{am_j}\) is precisely \(a_0+\cdots+a_{j-1}\), and \(\#_{bm_j}=b_0+\cdots+b_{j-1}\). Taking successive differences and using total counts \(A,B\) reconstructs the entire gap-composition vectors. Conversely, an arbitrary marker permutation and two nonnegative compositions of \(A\) and \(B\) into \(r+1\) parts are realized by at least one word.

**The sole remaining independent coordinate.** Once marker order and gap compositions are known, all two-deck entries containing a marker are fixed. Same-letter entries are \(\binom A2\), \(\binom B2\), and zero for marker self-pairs. Between \(a\) and \(b\), the invariant \(\#_{ab}+\#_{ba}=AB\) leaves exactly one variable \(K=\#_{ab}\). The contributions from different gaps are fixed:
\[
\sum_{s<t}\#_a(u_s)\#_b(u_t)=H.
\]
Consequently \(K=H+\sum_s\#_{ab}(u_s)\).

**No gaps in the possible values.** For a binary word with \(p\) occurrences of \(a\) and \(q\) of \(b\), \(\#_{ab}\) ranges over every integer from zero to \(pq\): the word \(b^qa^p\) has zero, \(a^pb^q\) has \(pq\), and each swap of an adjacent occurrence \(ba\) to \(ab\) increases the count by exactly one. Sorting by these swaps therefore realizes every intermediate integer. This also holds for \(p=0\) or \(q=0\), where the sole attainable value is zero. The Minkowski sum of the integer intervals \([0,a_sb_s]\) is the entire interval \([0,S]\). Thus the only possible values are precisely \(K=H,H+1,\ldots,H+S\), and each corresponds to a distinct full two-deck. The coefficient of \(z^j\) in \({p+q\brack p}_{z}\) counts the binary gap words with \(j\) scattered \(ab\) pairs, so independence of the disjoint gap choices proves the convolution coefficient formula (2). In particular there are exactly \(S+1\) deck values for each marker order and gap-composition pair.

**Counting all decks.** Write \(C_A=\binom{A+r}{r}\) and \(C_B=\binom{B+r}{r}\) for the numbers of weak compositions. The set of \(A\)-compositions is invariant under permuting gap positions, so each coordinate has mean \(A/(r+1)\); equivalently \(\sum_{\mathbf a}a_s=A C_A/(r+1)\), and analogously \(\sum_{\mathbf b}b_s=B C_B/(r+1)\). Summing \(S+1\) over all pairs of gap compositions gives
\[
\begin{aligned}
\sum_{\mathbf a,\mathbf b}(S+1)
 &=C_AC_B+\sum_{s=0}^{r}\left(\sum_{\mathbf a}a_s\right)\left(\sum_{\mathbf b}b_s\right)\\
 &=C_AC_B\left(1+\frac{AB}{r+1}\right).
\end{aligned}
\]
There are \(r!\) distinguishable orders for the singleton markers; their deck classes are disjoint because marker-marker pair entries recover the order. Multiplying by \(r!\) proves (1). For each class one may choose one representative, while two words with the same deck are observationally indistinguishable; hence the exact zero-error code-size interpretation follows. This completes the proof for all \(A,B,r\) in the stated range.

## Verification
An independent exhaustive checker constructs all fixed-content multiset permutations, computes their full length-two decks directly from index pairs, groups fibers by deck, and compares (1) and every fiber multiplicity against the Gaussian-gap formula. All 36 tested triples with \(1\le A,B\le3\) and \(0\le r\le3\) passed, representing 23,526 source words. The cases with \(r=0\) are additional checks of the binary base case, not part of the stated \(r\ge1\) theorem. In particular \(D_2(2,2;1)=27\) and \(D_2(3,3;2)=800\). Reproduce using `python3 checker.py`; recorded output is in `checker-output.txt`. The general claim follows from the proof, not from this finite experiment.

## Relationship to prior work
Lejeune, Rigo, and Rosenfeld study general \(k\)-binomial equivalence classes, give a general algorithm for two-binomial classes, and establish standard binary inversion-count properties. The present formula uses those elementary binary properties but provides an explicit closed all-parameter exact spectrum and all deck-fiber multiplicities in a labeled-marker composition family, not a general class-enumeration algorithm. Chrisnata et al. investigate bounds and enumeration for distinct decks, primarily binary examples. Nilforoushan and Parvaresh study general \(q\)-ary \(k\)-deck degrees of freedom and the polynomial-order count for \(k=2\); their abstract does not state this exact labeled-marker formula. Thus the present result is a fixed-composition, finite exact refinement rather than a claim to resolve unrestricted \(q\)-ary deck enumeration. Related adjacent-pair multispectra concern contiguous pairs and are a different observation.

## Limitations
Each marker must occur exactly once; the result does not assert a formula for repeated marker types, unrestricted compositions, or longer decks. This is a direct combinatorial derivation rather than an independent external certification. A directly relevant 2026 preprint was accessible through its bibliographic record and abstract, but the full text could not be examined; a special case hidden there, or in unindexed prior work, remains a residual originality risk. The checker only verifies the stated finite parameter range. The observed general Gaussian coefficient identity is independently justified in the proof.

## References
1. A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106, first submitted September 19, 2026, https://arxiv.org/abs/2609.23106.
2. M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (2020), https://arxiv.org/abs/2001.11732; available full text https://www.lirmm.fr/~mrosenfeld/LejeuneRigoRosenfeld.pdf.
3. J. Chrisnata, H. M. Kiah, S. Karingula, A. Vardy, E. Yaakobi and N. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications, DOI:10.3934/amc.2021032.
