# A sharp \(01\)-subsequence enumerator for near-shortest binary universal words

## Finding
For every integer \(k\ge1\), let \(\mathcal U_k\) consist of binary words with exactly \(k+1\) zeros and \(k\) ones that contain every binary word of length \(k\) as a scattered subsequence. Write \(|w|_{01}\) for the number of ordered index pairs \(i<j\) with \(w_i=0\) and \(w_j=1\). Then
\[
\boxed{\sum_{w\in\mathcal U_k}z^{|w|_{01}}=
 z^{\binom{k}{2}}(1+z)^{k-1}(1+z+\cdots+z^{k+1}).}
\]
In particular, the exact number at \(01\)-count \(\binom{k}{2}+h\) is
\[
 N_{k,h}=\sum_{i=\max(0,h-k-1)}^{\min(k-1,h)}\binom{k-1}{i}
 \qquad(0\le h\le2k),
\]
with the empty sum interpreted as zero. Every integer in this range is attained; the distribution is symmetric and unimodal, with maximum \(2^{k-1}\) at exactly \(h=k-1,k,k+1\). The number of words in this near-minimal fixed-composition universal class is \(\boxed{(k+2)2^{k-1}}\).

## Assumptions and scope
The alphabet is ordered \(0<1\). A scattered subsequence retains order but may skip positions. A word is \(k\)-universal if all \(2^k\) length-\(k\) binary patterns occur as scattered subsequences. The theorem concerns all integers \(k\ge1\), exact composition \((k+1,k)\), word length \(2k+1\), and exact \(01\)-subsequence counts, not contiguous bigrams. The shortest possible binary \(k\)-universal length is \(2k\), so this is the first redundant-symbol layer in the fixed-composition setting.

## Proof
**Unique structural decomposition.** The greedy arch factorization of a binary word cuts off, repeatedly, the shortest nonempty prefix containing both symbols; its number of complete arches equals the subsequence-universality index. Indeed, each complete arch can independently provide either requested letter. Conversely, when fewer than \(k\) complete arches exist, requesting at each step the letter missing from the current unfinished arch produces a length-\(k\) absent subsequence. This is the standard binary arch criterion. Every complete arch has length at least two and consumes at least one one. Thus any member of \(\mathcal U_k\), with length \(2k+1\) and exactly \(k\) ones, has exactly \(k\) complete arches, each containing exactly one one, and has either a terminal suffix of length one or no terminal suffix.

If a one-letter suffix exists, it must be zero, and all complete arches have length two. Every two-letter complete arch is \(01\) or \(10\), so the unique form is \(b_1\cdots b_k0\), with each \(b_i\in\{01,10\}\). If there is no suffix, precisely one arch has length three, the others length two. A length-three greedy complete arch with only one one must be \(001\): \(010\) would have completed after \(01\), and \(100\) after \(10\). Therefore, the unique form is \(b_1\cdots b_{j-1}\,001\,b_{j+1}\cdots b_k\), with \(1\le j\le k\) and \(b_i\in\{01,10\}\). Conversely, every word in either disjoint family has \(k\) greedy complete arches and is \(k\)-universal. Hence these are exactly the words in \(\mathcal U_k\).

**Weight enumerator.** Between two different complete arches, the earlier arch contributes one zero and the later arch one one, giving exactly \(\binom{k}{2}\) scattered \(01\) pairs for \(k\) ordinary two-letter arches. The internal contribution of \(01\) is one for block \(01\) and zero for block \(10\). The terminal zero contributes no further \(01\) pairs. Therefore all \(2^k\) words in the terminal-zero family contribute
\[
 z^{\binom{k}{2}}(1+z)^k.
\]
In the second family, the unique \(001\) block is in position \(j\). Compared with the baseline of one zero and one one per block, its extra zero contributes one additional \(01\) pair with its own one and another one with the one in each of the \(k-j\) later blocks. Furthermore, a normal block \(01\) contributes one internal pair, whereas \(001\) contributes two. Thus the special block contributes exactly \(2+(k-j)\) additional pairs, while the other \(k-1\) blocks contribute independently zero or one internal pair. The enumerator of the second family is therefore
\[
 z^{\binom{k}{2}}(1+z)^{k-1}\sum_{j=1}^k z^{k-j+2}
 =z^{\binom{k}{2}}(1+z)^{k-1}(z^2+\cdots+z^{k+1}).
\]
Adding the two disjoint families and factoring \((1+z)^{k-1}\) proves the claimed identity.

**Consequences.** The coefficient formula is the convolution of the \(k\)-term binomial row with a run of \(k+2\) ones. It has positive coefficients at every exponent from zero to \(2k\), symmetry from polynomial reciprocity, and successive coefficient differences that first are nonnegative and then nonpositive. The coefficient at \(h=k-1,k,k+1\) includes all binomial terms and is \(2^{k-1}\); outside this three-point plateau at least one positive binomial term is omitted. Evaluating the polynomial at \(z=1\) gives \((k+2)2^{k-1}\). All statements include \(k=1\).

## Verification
The standalone `verify_near_minimal_universal.py` enumerates every fixed-composition word for \(k=1,\ldots,9\), independently measures its scattered \(01\)-count, checks greedy-arch universality, and compares the full coefficient vector with the displayed product polynomial. For \(k=1,\ldots,5\), it independently tests containment of *every* length-\(k\) pattern rather than relying only on arch factorization. It reports `VERIFY_OK`. These finite calculations are checks, not the proof of the all-\(k\) claim. No computational assumption enters the proof.

## Relationship to prior work
The binary arch characterization and the structure of shortest universal words are standard; see Fazekas, Huang, and Mercaş, arXiv:2610.06717, Lemma 2.1 and Corollary 2.2. Their paper gives arithmetic existence and all-representative conditions for fixed binary Parikh matrices but does not state this exact near-shortest **composition-and-\(01\)-pair-refined** universal-word polynomial. Richomme, arXiv:2510.07159, supplies the correspondence between fixed \(01\)-counts and partitions; that correspondence alone does not enumerate universal representatives. Published unrefined length-by-universality enumerators do not determine the joint \(01\)-count distribution. The formula's univariate specialization at \(z=1\) is not claimed as a new unrefined enumeration.

## Limitations
The result treats exactly one excess zero and no excess one above the minimum per-symbol counts, with arbitrary universality order \(k\). Other compositions, larger excess, and general alphabets are not classified here. The formula is an ordinary \(01\)-pair enumerator and should not be confused with a \(q\)-deformed subsequence-count statistic. Priority against unindexed equivalent formulas remains uncertain; no independent review has been performed.

## References
1. S. Z. Fazekas, X. Huang, and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first public 2026-10-05), §§2–4, especially Lemma 2.1, Corollary 2.2, Theorem 3.3 and Theorem 4.5. https://arxiv.org/abs/2610.06717
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (first public 2025-10-08), §4.2. https://arxiv.org/abs/2510.07159
