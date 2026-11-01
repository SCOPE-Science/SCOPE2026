# Exact binary collision distances after erasing one minimal cyclic Fourier sample

## Finding
For every integer \(N\ge 2\), fix one DFT frequency \(k_d\in\mathbb Z_N\) of *additive-character order* \(d\) for every positive divisor \(d\mid N\); equivalently \(N/\gcd(N,k_d)=d\). Measure the complex, labelled Fourier coefficients
\[\widehat x(k)=\sum_{j=0}^{N-1}x(j)e^{-2\pi i jk/N}\]
for binary words \(x\in\{0,1\}^N\) at these \(\tau(N)\) frequencies. For each omitted frequency \(k_d\), the exact minimum Hamming distance of two different binary words whose remaining measurements agree is
\[\boxed{\Delta(N,d)=\frac Nd\,2^{\omega(d)},}\]
where \(\omega(d)\) counts the distinct prime divisors of \(d\), with \(\omega(1)=0\). The formula is independent of the chosen representative \(k_e\) in each order class. In particular, for a lost representative of unknown order the smallest possible collision distance is exactly
\[\boxed{\min_{d\mid N}\Delta(N,d)=2^{\omega(N)}.}\]
Both minima are attained by explicitly constructed pairs. This theorem determines a *Hamming-distance floor for ambiguous binary signals*; it does not quantify stability to errors in Fourier values.

## Assumptions and scope
All coordinates and frequencies are indexed by \(\mathbb Z/N\mathbb Z\). Fourier values are exact complex values, not magnitudes, and the measurement frequencies are individually labelled. The alphabet is exactly \(\{0,1\}\). The original mask contains exactly one frequency of every character order; exactly one of those frequencies is erased. There is no sparsity restriction on the individual words, only on their difference. The Hamming distance of \(x,y\) is the number of indices where \(x(j)\ne y(j)\).

## Proof
**1. Cyclotomic reduction.** Put \(h=x-y\). Then \(h\in\{-1,0,1\}^N\) and its support size equals the Hamming distance. Conversely every vector \(h\in\{-1,0,1\}^N\) can be written as a binary difference by setting \(x=\mathbf1_{\{h=1\}}\) and \(y=\mathbf1_{\{h=-1\}}\). For any rational vector \(h\), the polynomial \(H(X)=\sum_{j=0}^{N-1}h(j)X^j\) has rational coefficients. If it vanishes at a primitive \(e\)-th root, the cyclotomic polynomial \(\Phi_e\) divides \(H\), so it vanishes at every primitive \(e\)-th root. Therefore equality of all retained samples is equivalent to the Fourier support of \(h\) being contained in the complete shell of characters whose order is \(d\). Denote this rational subspace by \(V_{N,d}\).

**2. Prime-power shell.** For \(n=p^a\) and \(e=p^b\), \(0\le b\le a\), consider \(V_{p^a,p^b}\). If \(b=0\), this is the one-dimensional space of constant vectors, whose least nonzero support is \(p^a\). If \(b\ge1\), Fourier inversion shows that a vector belongs to this space exactly when it is periodic modulo \(p^b\) and the sum of its values over the \(p\) residue classes
\[r,\ r+p^{b-1},\ \ldots,\ r+(p-1)p^{b-1}\pmod{p^b}\]
is zero for each \(0\le r<p^{b-1}\). Indeed periodicity kills all characters of order exceeding \(p^b\), while the displayed sum-zero conditions kill every character of order at most \(p^{b-1}\). A nonzero such block has at least two occupied residue classes, each repeated \(p^{a-b}\) times, so the least nonzero support is \(2p^{a-b}\). Equality is attained by assigning \(+1\) at residue \(0\) and \(-1\) at residue \(p^{b-1}\) modulo \(p^b\), zero elsewhere, then repeating periodically.

**3. Chinese-remainder tensor product.** Write \(N=\prod_{i=1}^s p_i^{a_i}\) and \(d=\prod_{i=1}^s p_i^{b_i}\), with \(0\le b_i\le a_i\). The Chinese remainder permutation identifies \(\mathbb Z_N\) with \(\prod_i\mathbb Z_{p_i^{a_i}}\). Character order is the product of its local prime-power orders; hence
\[V_{N,d}\cong\bigotimes_{i=1}^s V_{p_i^{a_i},p_i^{b_i}}.\]
The minimum nonzero support of a tensor product of finite-dimensional subspaces is the product of their minimum nonzero supports: for two spaces, choose a nonzero row of a nonzero matrix in their tensor product; at least the minimum number of columns are nonzero, and each nonzero column has at least its factor's minimum number of occupied rows. Rank-one tensors of minimum-support factor vectors attain equality. Iteration gives
\[\min_{0\ne h\in V_{N,d}}|\operatorname{supp}h|=\prod_{b_i=0}p_i^{a_i}\prod_{b_i>0}2p_i^{a_i-b_i}=\frac Nd 2^{\omega(d)}.\]
The explicit local minimizers take only values \(-1,0,1\), so their tensor product does too. This converts the sharp support bound into a sharp binary-pair Hamming bound, without an integrality gap.

**4. Worst deleted order.** Every local factor in the above product is at least \(2\) (because \(p_i^{a_i}\ge2\) when \(b_i=0\), and \(2p_i^{a_i-b_i}\ge2\) otherwise). Choosing \(b_i=a_i\) for every \(i\) makes every local factor exactly \(2\), so the minimum over all deleted orders equals \(2^{\omega(N)}\). This concludes the proof.

## Verification
The included `check.py` performs exact integer-polynomial reductions modulo the cyclotomic polynomials \(\Phi_e\). It exhausts every ternary difference vector of lengths \(2\) through \(10\), hence all pairs of binary words in those dimensions up to redundant representations, and independently verifies the formula for every omitted character order. It also verifies the explicit product construction at lengths \(12,15,18,20,24,30,36,45,60,72\). Running `python check.py` with SymPy installed gives `PASS: 103 exact primitive-shell checks, including exhaustive ternary differences for N <= 10.` The proof applies to every integer length; no finite scan is treated as its proof.

## Relationship to prior work
Pei and Chang (2022) established minimal DFT sampling for binary signals and constructed ambiguity pairs whose difference Fourier transforms live in a single cyclotomic order shell. Those uniqueness results and explicit upper-bound witnesses are prior; they do **not** establish a sharp *lower bound on the support of every possible ambiguity difference* in the accessible descriptions. Levinson and Viviano (arXiv:2510.11949), Section 2.1 and Lemma 2.2, display a signed-vector construction with \(2^{\omega(N)}\) nonzero entries for a primitive shell and develop general integer/image recovery. Their construction supplies the upper-bound pattern used here but not the tensor-product minimum-distance theorem for every omitted divisor. Iosevich and Mayeli (arXiv:2311.04331), Sections 2 and 4, provide uncertainty-based binary recovery guarantees for different missing-frequency regimes; those inequalities do not determine the present sharp, arithmetic collision distance. The new assertion is the all-order *minimality and deletion-distance classification*, not the known cyclotomic orbit criterion or an existing ambiguity-pair construction.

## Limitations
The theorem is only about exact coincidence of the retained Fourier coefficients on binary words and their Hamming distance. It does not give a noise-tolerance radius in Fourier measurement space, a decoder, a full classification of minimizing collision pairs, or an extension to multiple erasures. Historical priority remains provisional because the full 2022 Pei--Chang paper was not accessible for a definitive comparison of its ambiguity-pair lemmas; its available abstract and later published expositions have been compared, and a broader coding-theoretic formula may imply this theorem. The exact support result for arbitrary rational vectors is proved here as an ingredient, not asserted to be a new general coding-theory theorem independently of the application.

## References
1. A. Iosevich and A. Mayeli, *Uncertainty Principles on Finite Abelian Groups, Restriction Theory, and Applications to Sparse Signal Recovery*, first posted 2023-11-07, arXiv:2311.04331, https://arxiv.org/abs/2311.04331.
2. S.-C. Pei and K.-W. Chang, *Binary Signal Perfect Recovery From Partial DFT Coefficients*, IEEE Transactions on Signal Processing 70 (first public 2022-07-13), 3848--3861, DOI:10.1109/TSP.2022.3190615.
3. H. W. Levinson and I. Viviano, *Recovery of Integer Images from Minimal DFT Samples: Uniqueness and Inversion Algorithms*, arXiv:2510.11949, https://arxiv.org/abs/2510.11949, Sections 2--3 and 6.
