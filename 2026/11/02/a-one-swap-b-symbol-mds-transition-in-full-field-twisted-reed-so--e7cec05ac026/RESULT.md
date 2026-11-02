# A one-swap \(b\)-symbol MDS transition in full-field twisted Reed–Solomon codes

## Finding
Let \(p\ge5\) be prime, \(2\le k\le p-1\), and \(\eta\in\mathbb F_p^{\times}\). Consider the \(k\)-dimensional polynomial space
\[
\mathcal P_{k,\eta}=\left\{\sum_{j=0}^{k-2}a_jX^j+a_{k-1}(X^{k-1}+\eta X^k):a_j\in\mathbb F_p\right\}.
\]
For any cyclic ordering \(\sigma=(\sigma_0,\ldots,\sigma_{p-1})\) of the elements of \(\mathbb F_p\), define the length-\(p\) linear code \(C_\sigma=\{(f(\sigma_i))_{i=0}^{p-1}:f\in\mathcal P_{k,\eta}\}\). Indices of words and orderings are read modulo \(p\). Define the \(b\)-symbol weight to be the number of nonzero consecutive \(b\)-tuples, for \(1\le b\le p\). Set
\[
s=-\eta^{-1},\qquad
N_\sigma(s)=\#\left\{i\in\mathbb Z/p\mathbb Z:\sum_{j=0}^{k-1}\sigma_{i+j}=s\right\}.
\]
**Exact cyclic-order criterion.** The minimum \(b\)-symbol distances, simultaneously for all window lengths, are
\[
d_b(C_\sigma)=
\begin{cases}
p-k,&b=1,\\
p-k+b-\mathbf 1_{\{N_\sigma(s)>0\}},&2\le b\le k,\\
p,&k<b\le p.
\end{cases}
\]
Whenever \(N_\sigma(s)>0\), for every \(2\le b\le k\) the number of nonzero codewords attaining that minimum is exactly \((p-1)N_\sigma(s)\).

**Sharp one-swap transition.** In every affine arithmetic cyclic ordering \(\sigma_i=a+di\), \(d\ne0\), one has \(N_\sigma(s)=1\), so every \(b\)-distance with \(2\le b\le k\) misses the \(b\)-symbol Singleton bound by exactly one. In contrast, for \(2\le k\le p-2\), put
\[
t=\frac{k-1}{2}-\frac{1}{k\eta}\in\mathbb F_p,
\quad \tau=(t+1,t,t+2,t+3,\ldots,t+p-1).
\]
This ordering is obtained from the arithmetic order \((t,t+1,\ldots,t+p-1)\) by swapping its first two coordinates. It satisfies \(N_\tau(s)=0\), and the resulting code meets the Singleton bound for **every** \(2\le b\le p\):
\[
d_b(C_\tau)=\min\{p,p-k+b\}.
\]
The exception \(k=p-1\) is sharp: every cyclic ordering has \(N_\sigma(s)=1\), hence no coordinate permutation makes the code \(b\)-symbol MDS for \(2\le b\le p-1\). The Hamming minimum distance \(p-k\) is unchanged by every reordering.

For example, at \((p,k,\eta)=(5,2,1)\), the arithmetic order \((0,1,2,3,4)\) gives pair distance \(4\), whereas the single-swap order \((1,0,2,3,4)\) gives the optimal pair distance \(5\). Both codes have Hamming distance \(3\).

## Assumptions and scope
The alphabet is the prime field \(\mathbb F_p\), not an unspecified prime-power field. The evaluation set is all of \(\mathbb F_p\); each point appears once. The twist is exactly one term, with hook \(k-1\) and twist degree increment one. The consecutive windows wrap cyclically, and the code is linear. Only \(p\ge5\), \(2\le k<p\), and nonzero \(\eta\) are asserted; for \(k=p-1\), the obstruction rather than an MDS reordering applies. The Singleton comparison concerns the \(b\)-symbol metric, not ordinary Hamming MDS status.

## Proof
**1. Polynomial roots and dimension.** Every nonzero member of \(\mathcal P_{k,\eta}\) has degree at most \(k<p\). Evaluation at all \(p\) field elements is injective, so \(\dim C_\sigma=k\). A nonzero polynomial with exactly \(k\) distinct roots must have nonzero leading coefficient \(\eta a_{k-1}\) and coefficient ratio \(a_{k-1}/(\eta a_{k-1})=\eta^{-1}\) in degrees \(k-1\) and \(k\). Vieta's formula therefore forces its roots to sum to \(s=-\eta^{-1}\). Conversely, every \(k\)-subset \(T\subset\mathbb F_p\) with \(\sum_{x\in T}x=s\) yields the polynomial \(\prod_{x\in T}(X-x)\in\mathcal P_{k,\eta}\): its leading coefficient is one and its \(X^{k-1}\)-coefficient is \(-s=\eta^{-1}\). Every codeword with precisely these \(k\) zero positions is a nonzero scalar multiple of this polynomial. Translating any fixed \(k\)-subset by an element of \(\mathbb F_p\) shifts its sum by \(k\) times that element; since \(k<p\), some translate has sum \(s\). Thus the ordinary Hamming distance is exactly \(p-k\) for every ordering.

**2. Zero-window lemma.** If a nonzero word has \(z\le k<p\) zero positions, split them into maximal cyclic runs of consecutive zeros of lengths \(\ell_1,\ldots,\ell_r\). The number of all-zero length-\(b\) windows is exactly \(\sum_j\max\{0,\ell_j-b+1\}\). For \(2\le b\le k\), this number is at most \(k-b+1\), with equality if and only if there are exactly \(k\) zeros and they form a single cyclic run of length \(k\). Otherwise it is at most \(k-b\) (interpreted as zero when \(b=k\)). Therefore \(d_b\ge p-k+b-1\), with equality exactly when a polynomial has the zero set of a cyclic length-\(k\) interval. Part 1 identifies such intervals by their evaluation-point sum \(s\). If none exists, the sharper bound \(d_b\ge p-k+b\) holds. For \(2\le b\le k-1\), the reverse inequality follows constructively: evaluation of the polynomial space at any \(k-1\) selected points has rank \(k-1\), because the subspace of degree at most \(k-2\) already gives an invertible Vandermonde evaluation matrix. Thus a nonzero polynomial vanishes at \(k-1\) consecutive points, producing at least \(k-b\) all-zero length-\(b\) windows. For \(b=k\), the reverse inequality is the trivial \(d_k\le p\). For \(b>k\), a nonzero polynomial has fewer than \(b\) zeros, so every \(b\)-window is nonzero. The criterion and every displayed distance follow.

Whenever the smaller bound is attained, its root set is a consecutive length-\(k\) interval with sum \(s\). Distinct cyclic length-\(k\) intervals have distinct zero sets because \(1\le k<p\). By Part 1 each such set yields exactly \(p-1\) nonzero scalar-multiple codewords, proving the minimum-layer multiplicity.

**3. Arithmetic ordering.** For \(\sigma_i=a+di\) in \(\mathbb F_p\), the sum of the length-\(k\) interval beginning at \(i\) is \(ka+d(ki+k(k-1)/2)\). Its slope in \(i\) is \(dk\ne0\), so it takes each field value exactly once and \(N_\sigma(s)=1\).

**4. One-swap construction and sharp obstruction.** Let \(\alpha_i=t+i\), where \(t=(k-1)/2-(k\eta)^{-1}\). In this arithmetic order, the interval starting at \(i=1-k\) has sum \(kt-k(k-1)/2=s\), and by Part 3 this is the unique bad interval. Swap positions zero and one. Exactly two length-\(k\) interval sums change: the sum for the interval starting at \(1-k\) increases by one, and the sum for the interval starting at one decreases by one. The latter was initially \(s+k^2\); hence after the swap it is \(s+k^2-1\). For \(2\le k\le p-2\), primality gives \(k^2\not\equiv1\pmod p\), so neither changed interval has sum \(s\); the remaining intervals were not bad. Consequently \(N_\tau(s)=0\). Parts 1–2 then yield all Singleton-optimal \(b\)-symbol distances at once.

For \(k=p-1\), the sum of all elements of \(\mathbb F_p\) is zero, and each length-\(p-1\) cyclic interval is the complement of exactly one coordinate. As the omitted coordinate ranges over all elements, these interval sums range over all field elements exactly once. Thus \(N_\sigma(s)=1\) for every order and the obstruction follows.

## Verification
Run `python3 verify.py` from the directory containing the standalone verifier; it uses Python's standard library only. The verifier directly enumerates polynomial-code messages for 54 complete code instances totaling 354,480 nonzero codewords, across primes \(5,7,11,13\). It checks all \(b\)-symbol minima and all smaller-minimum multiplicities. It independently checks all 360 cyclic coordinate permutations for \(p=5\) in dimensions two through four, and 4,056 exact window-sum cases through prime 29. The recorded output is in `verification_output.txt`; it ends in `TWISTED_B_SYMBOL_VERIFY_OK`. This is corroboration only: the proof is all-prime and does not extrapolate from these finite tests.

## Relationship to prior work
Beelen, Puchinger and Rosenkilde developed twisted Reed–Solomon evaluation codes in the Hamming metric. Liu, Chen, Zheng and Chen (2026) determine generalized Hamming weights and subcode support distributions for one- and two-twist codes; their full-field family includes the present polynomial space, but their results aggregate *Hamming* support information and do not determine cyclic-window arrangements. Chee and collaborators established the symbol-pair Singleton bound and constructions, while Liu and Pan provide general \(b\)-symbol MDS rank criteria. Those results supply the established metric language and bounds. The claim here is the explicit **all-order cyclic-window sum criterion**, the sharp **one-adjacent-swap arithmetic construction**, and the unavoidable **codimension-one obstruction** for this family. It is not a claim of a new Hamming-code construction or of a new Singleton inequality.

## Limitations
The coordinate-reordering statement is special to full-prime-field evaluation and the highest-hook, degree-one twist. It does not classify all permutations yielding optimal windows, nor address arbitrary prime powers, shortened evaluation sets, or decoding complexity. Existing general \(b\)-MDS rank criteria could be specialized to recover parts of the statement; no absolute priority is asserted. Independent validation has not been performed.

## References
1. C. Liu, H. Chen, D. Zheng and Y. Chen, *Generalized Hamming Weights and Subcode Support Weight Distributions of Twisted Reed–Solomon Codes*, arXiv:2610.16283v1 (first submitted 2026-10-12), Sections 1–4. https://arxiv.org/abs/2610.16283
2. P. Beelen, S. Puchinger and J. Rosenkilde, *Twisted Reed–Solomon Codes*, arXiv:2107.06945, Sections II–IV. https://arxiv.org/abs/2107.06945
3. H. Liu and X. Pan, *Generalized \(b\)-symbol Weights of Linear Codes and \(b\)-symbol MDS Codes*, arXiv:2103.16299, Sections 3–4. https://arxiv.org/abs/2103.16299
4. Y. M. Chee, L. Ji, H. M. Kiah, C. Wang and J. Yin, *Maximum Distance Separable Codes for Symbol-Pair Read Channels*, arXiv:1211.1728, Sections 2–3. https://arxiv.org/abs/1211.1728
