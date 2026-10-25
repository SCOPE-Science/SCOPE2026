# Exact circular subsequence-universality spectrum of binary words

## Finding
Fix the ambient alphabet \(\Sigma=\{0,1\}\). For every nonempty word \(w\in\Sigma^n\), its *circular scattered-subsequence universality index* \(\zeta(w)\) is the largest integer \(k\) such that at least one cyclic rotation of \(w\) contains every binary length-\(k\) word as a scattered subsequence. Unary source words have index zero because the ambient alphabet remains binary.

For every \(n\ge1\), define the complete distribution polynomial
\[
P_n(u)=\sum_{w\in\Sigma^n}u^{\zeta(w)}.
\]
Then, with \(\lambda_\pm(u)=(1\pm\sqrt{1+8u})/2\),
\[
\boxed{P_n(u)=\lambda_+(u)^n+\lambda_-(u)^n+1-2\mathbf1_{2\mid n}u^{n/2}.}
\]
Although square roots appear in the display, their sum is a polynomial in \(u\). Equivalently, the bivariate ordinary generating function is
\[
\boxed{\sum_{n\ge1}P_n(u)z^n=\frac{z+4uz^2}{1-z-2uz^2}+\frac{z}{1-z}-\frac{2uz^2}{1-uz^2}.}
\]
Consequently, the exact number of length-\(n\) binary words having \(\zeta(w)=k\) is
\[
\boxed{N_{n,k}=\begin{cases}
2,&k=0,\\
2^k\dfrac{n}{n-k}\binom{n-k}{k}-2\mathbf1_{n=2k},&1\le k\le\lfloor n/2\rfloor,\\
0,&k>\lfloor n/2\rfloor.
\end{cases}}
\]
Thus the number of words achieving the information-theoretic maximum \(\lfloor n/2\rfloor\) is explicit, including the even-length alternating exception.

For a uniformly random binary word \(W_n\), write \(Z_n=\zeta(W_n)\) and \(\epsilon_n=(-1)^n\). Its exact mean and variance are
\[
\boxed{\mathbb E Z_n=\frac n3+\frac{n(\epsilon_n-3)}{6\,2^n},}
\]
\[
\boxed{\operatorname{Var}(Z_n)=\frac{2n}{27}+\frac{n((9n-8)\epsilon_n+9n)}{108\,2^n}-\frac{n^2(\epsilon_n-3)^2}{36\,4^n}.}
\]
In particular, \(\mathbb E Z_n=n/3+O(n2^{-n})\) and \(\operatorname{Var}(Z_n)=2n/27+O(n^2 2^{-n})\).

## Assumptions and scope
The ambient alphabet is fixed to \(\{0,1\}\) even when a word uses only one symbol. Each of the \(2^n\) position-indexed, linear binary words is counted separately; words related by rotation are not identified in \(P_n\). A scattered subsequence is obtained by deleting arbitrary letters while retaining order. A cyclic rotation makes one cut in the original circle and reads exactly \(n\) positions once. All statements hold for every integer \(n\ge1\), including the length-one and length-two boundary cases.

For a cyclic word \(w\), form the cyclic graph \(G_w\) on its \(n\) positions, with an edge between successive positions precisely when the two letters differ. The length-two case is understood as a two-vertex multicycle with two labeled boundary edges. Then the structural identity is
\[
\boxed{\zeta(w)=\nu(G_w),}
\]
where \(\nu\) is the maximum cardinality of a matching. A length-one word gives an edgeless graph.

## Proof
**1. Binary arches equal adjacent unequal pairs.** A binary linear word \(v\) has universality index equal to the number of greedy arches in its left-to-right arch factorization (standard universality criterion). An arch is the shortest rich prefix of the current remaining suffix; over a binary alphabet it has the form \(a^r\bar a\), with \(r\ge1\). Its last two positions form an adjacent unequal pair. Distinct arches give disjoint pairs. Thus \(\iota(v)\), the linear index, is at most the maximum matching size of its path of unequal adjacent pairs. Conversely, any \(k\) vertex-disjoint unequal adjacent pairs arranged left-to-right form \(k\) consecutive two-symbol rich blocks after deletion of unused letters. Every length-\(k\) binary word embeds by choosing one required letter from each block, so \(\iota(v)\ge k\). Hence the path matching number equals \(\iota(v)\).

For circular \(w\), each rotation deletes one cyclic boundary edge from consideration. Every matching of \(G_w\) omits some boundary edge: when \(n\ge2\), a matching uses at most \(\lfloor n/2\rfloor<n\) of the \(n\) labeled boundaries, and for \(n=1\) there is no edge. Cutting along an unused boundary retains the entire matching, while the path matching in any rotation is certainly a cyclic matching. Therefore \(\zeta(w)=\nu(G_w)\), with the stated boundary conventions.

**2. Transitions and the weighted cyclic state matrix.** Number cyclic edges \(1,\ldots,n\). Let \(e_i=1\) if the two adjacent bits differ across edge \(i\), and \(e_i=0\) otherwise. Since toggling around the circle returns to the initial bit, \(\sum_i e_i\) is even. Conversely every cyclic transition vector with even sum reconstructs exactly two binary words, related by bit complementation. For a transition vector containing at least one zero, a maximal cyclic run of \(\ell\ge1\) consecutive ones gives a path component with \(\ell\) edges, whose maximum matching has \(\lceil\ell/2\rceil\) edges. Isolated vertices contribute zero. If all entries are one, the word is alternating, \(n\) is even, and the matching number is \(n/2\).

Use three states for cyclic transition sequences: state \(0\) means the last transition was zero, and states \(1\) and \(2\) mean a positive run of ones has respectively odd or even length. A transition equal to one carries a marker \(v\); the first, third, fifth, etc. ones in each run additionally carry the marker \(u\). A transition equal to zero resets the state to \(0\). The weighted transition matrix (row = prior state, column = next state) is
\[
M(v,u)=\begin{pmatrix}1&vu&0\\1&0&v\\1&vu&0\end{pmatrix}.
\]
For any cyclic transition vector containing a zero, there is exactly one consistent cyclic state path, and its weight is \(v^{\sum_i e_i}u^{\nu(G_w)}\). The exceptional all-one vector exists only at even length. It has two cyclic state paths, whereas the desired transition-vector count has one, so one copy must be subtracted. Parity projection \(v=1,-1\), followed by the two-to-one reconstruction of source words, gives
\[
P_n(u)=\operatorname{tr}(M(1,u)^n)+\operatorname{tr}(M(-1,u)^n)-2\mathbf1_{2\mid n}u^{n/2}.
\]
Here the correction is exactly two, not one, because the parity-projected and letter-reconstructed counts are combined. The characteristic polynomials are \(x(x^2-x-2u)\) for \(M(1,u)\) and \(x^2(x-1)\) for \(M(-1,u)\). Their traces for all positive powers give the asserted eigenvalue formula. Summing geometric series yields the displayed rational generating function.

**3. Exact coefficients.** Put \(T_0(u)=2\), \(T_1(u)=1\), and \(T_n(u)=T_{n-1}(u)+2uT_{n-2}(u)\). The characteristic roots show that \(T_n(u)=\lambda_+(u)^n+\lambda_-(u)^n\). It is also the weighted matching polynomial of the labeled \(n\)-cycle (using the conventional two parallel edges for \(n=2\)), with weight \(2u\) per chosen edge. For \(1\le k\le\lfloor n/2\rfloor\), choosing \(k\) nonadjacent cyclic edges has
\[
\frac{n}{k}\binom{n-k-1}{k-1}=\frac{n}{n-k}\binom{n-k}{k}
\]
solutions: mark a selected edge, distribute the \(n-k\) unselected edges into \(k\) positive cyclic gaps, then divide by the \(k\) choices of marked edge. Multiplying by \((2u)^k\) and applying the alternating correction gives precisely \(N_{n,k}\). The constant term is \(1+1=2\); those are the two unary words. The cycle count includes the length-two multicycle as a limiting labeled-edge case.

**4. Moments.** Differentiate the rational generating function in \(u\), set \(u=1\), and use \(P_n(1)=2^n\). Coefficient extraction gives
\[
\sum_w\zeta(w)=\frac{n2^n}{3}+\frac{n(-1)^n}{6}-\frac n2.
\]
A second derivative yields the factorial second-moment sum
\[
\sum_w\zeta(w)(\zeta(w)-1)=2^n\left(\frac{n^2}{9}-\frac{7n}{27}\right)+\frac{(-1)^n n(21n-26)}{108}+\frac{n(2-n)}4.
\]
Dividing both sums by \(2^n\), using \(\mathbb E Z_n^2=\mathbb E[Z_n(Z_n-1)]+\mathbb E Z_n\), and subtracting the squared mean gives the two moment formulas without any limiting argument. Their error bounds follow because the corrections are polynomial in \(n\) times \(2^{-n}\) or \(4^{-n}\).

## Verification
The standalone standard-library program `verify.py` exhaustively enumerates all \(131070\) nonempty binary words of lengths \(1\) through \(16\), computes the circular index by scanning every rotation, and compares every histogram cell to the closed coefficient formula. It independently tests all subsequences directly at every rotation through length \(10\) (\(18434\) rotation checks), and compares the circular index against a separate matching subset enumeration on all \(2046\) words through length \(10\). Exact rational arithmetic checks the mean and variance at every length through \(16\), and a separate polynomial recurrence checks the characteristic-root formula through length \(80\). To reproduce: `python3 verify.py`. A successful run prints `VERIFY_OK` followed by these check counts. These finite checks corroborate, but do not replace, the all-length proof.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka introduced scattered-subsequence circular universality and proved that the circular and linear indexes differ by at most one; their 2020 treatment includes the binary arch criterion and results concerning powers. Fleischmann, Germann and Nowotka (2021) characterized the growth of universality under repetitions, while Schnoebelen and Veron (2023) developed arch-jumping and circular-index algorithms. Those are the source of the circular object and its computational motivation; they are not claimed here as new. Adamson (2023) developed counting and ranking algorithms for ordinary (noncircular) universal words. The published finding *Closed-form law for binary subsequence universality* gives an explicit distribution for the ordinary index \(\iota\), not the circular index \(\zeta\).

The contribution here is the graph-matching model for the **circular** binary index, the exact full fixed-length distribution with its even-length alternating correction, and the exact moment identities. The prior computation algorithms can evaluate the index of each individual word, and brute enumeration could in principle compute any one finite histogram; neither yields the displayed all-length formulas or their structural justification directly.

## Limitations
This is an enumeration of position-indexed binary words, not binary necklaces or bracelets. The proof relies on the two-letter arch property and does not generalize unchanged to larger alphabets. The matching interpretation uses cyclic positions, including the separate labeled edges in the two-position case. No central limit theorem, concentration bound, or unique enumeration claim over all possible historical literature is asserted. An unindexed equivalent cyclic enumeration would supersede originality; targeted literature comparison has not identified one. Independent verification outside the present mathematical argument has not been performed.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, first public 2020-03-10. https://arxiv.org/abs/2003.04629
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality -- The Power of the Remainder*, arXiv:2104.09063v1, first public 2021-04-19. https://arxiv.org/abs/2104.09063
3. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, first public 2023-04-10. https://arxiv.org/html/2304.04583v1
4. P. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1, first public 2023-04-24. https://arxiv.org/abs/2304.11932
5. *Closed-form law for binary subsequence universality*, publicly available result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37
