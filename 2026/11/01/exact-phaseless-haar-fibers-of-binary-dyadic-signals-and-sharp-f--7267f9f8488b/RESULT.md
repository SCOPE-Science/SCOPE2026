# Exact phaseless Haar fibers of binary dyadic signals and sharp fixed-weight ambiguity

## Finding

Let \(N=2^m\), with integer \(m\ge1\), and let \(x\in\{0,1\}^N\). For each dyadic interval \(I\subseteq\{0,\ldots,N-1\}\) of length at least two, write \(I_L,I_R\) for its left and right halves, and define the (unnormalized) Haar detail
\[
h_I(x)=\sum_{j\in I_L}x_j-\sum_{j\in I_R}x_j,
\qquad s_I(x)=\sum_{j\in I}x_j.
\]
The phaseless Haar data consist of the **signed** root total \(s_{[N]}(x)\) and **all individually labelled** detail magnitudes \(\{|h_I(x)|:|I|\ge2\}\). Let \(\mathcal F(x)\) be the set of all binary vectors with exactly these measurements, and let
\[
b(x)=\#\{I:|I|\ge2,\quad s_I(x)=|I|/2,\quad h_I(x)\ne0\}.
\]
Then, without exceptions,
\[
\boxed{|\mathcal F(x)|=2^{b(x)}.}
\]
In particular, the only uniquely recoverable binary signals are the two constants. Every other observation has a fiber whose cardinality is a power of two, at least two.

More sharply, for **every** Hamming weight \(0\le k\le N\),
\[
\boxed{\max_{x\in\{0,1\}^N:\,s_{[N]}(x)=k}|\mathcal F(x)|=2^{\min(k,N-k)}.}
\]
For \(k\le N/2\), equality is achieved by placing the \(k\) ones in \(k\) different adjacent dyadic pairs; the case \(k>N/2\) follows by complementation. The unconditional maximum is \(2^{N/2}\), and the **unique measurement fiber** of that cardinality consists of precisely the \(2^{N/2}\) vectors with exactly one one in every adjacent pair.

The conclusions remain true for any prescribed alphabet \(\{\alpha,\beta\}\subset\mathbb R\) of two distinct numbers: the affine map \(x_j\mapsto\alpha+(\beta-\alpha)x_j\) rescales details and affinely transforms the measured root sum.

## Assumptions and scope

The transform is the standard **nonperiodic finite dyadic Haar orthogonal basis**, without redundant translates or extra measurements. Each Haar detail is indexed by its particular dyadic interval; losing labels changes the problem. Dividing \(h_I\) by \(\sqrt{|I|}\) converts to the orthonormal convention and does not affect magnitude equivalence. The root average is measured with sign, not merely in absolute value. The alphabet is known in advance. All assertions hold for each finite integer \(m\ge1\), not only asymptotically.

## Proof

**1. Local binary Parseval constraint.** For any dyadic interval \(I\) of length \(n\), Haar orthogonality restricted to the interval gives
\[
\sum_{j\in I}x_j^2=\frac{s_I(x)^2}{n}+
\sum_{\substack{J\subseteq I\\|J|\ge2}}\frac{h_J(x)^2}{|J|}.
\tag{1}
\]
Since the entries are zero or one, the left side equals \(s_I(x)\). Therefore the detail magnitudes strictly **inside** \(I\) determine
\[
V_I=s_I(x)-\frac{s_I(x)^2}{n}.
\tag{2}
\]
Any competing binary vector with the same internal detail magnitudes must consequently have its interval sum in the two-element set \(\{s_I(x),n-s_I(x)\}\), possibly with coincident elements.

**2. Exact count at a fixed subtree sum.** Write \(F_I(t)\) for the number of binary configurations on \(I\) with prescribed internal detail magnitudes and interval total \(t\), and set \(a=s_{I_L}(x)\), \(c=s_{I_R}(x)\), \(d=|a-c|\). Suppose the parent total is fixed to its observed value \(s=a+c\), and let \(n=|I|\), \(q=n/2\). The parent contrast magnitude permits child-sum orientations \((a,c)\), and, when \(d>0\), \((c,a)\). An exchanged orientation can satisfy (2) on the left only if \(c=a\) or \(c=q-a\). In the distinct case \(d>0\), this forces \(a+c=q\). The same condition is sufficient: the binary complement on each child exchanges sums \((a,c)\) with \((q-a,q-c)=(c,a)\), preserves every descendant detail magnitude, and bijects the corresponding child fibers. Thus there are exactly two disjoint, equally large root orientations **if and only if** \(s=n/2\) and \(d>0\); otherwise there is exactly one.

Under either orientation, choices in the two children are independent, so
\[
F_I(s_I(x))=2^{\mathbf1_{\{s_I(x)=n/2,\ h_I(x)\ne0\}}}
F_{I_L}(a)F_{I_R}(c).
\tag{3}
\]
The base case is a single leaf, for which a fixed sum determines its binary value. Induction in (3) proves the exact formula \(|\mathcal F(x)|=2^{b(x)}\). Every nonconstant binary vector has a smallest nonconstant dyadic interval. Its two children are constant and of opposite values, giving \(s_I=|I|/2\) and \(h_I\ne0\), so \(b(x)\ge1\). Conversely both constants have no balanced splits.

**3. Sharp weight bound.** We claim by induction for each dyadic interval \(I\) that
\[
b_I(x)\le \min\{s_I(x), |I|-s_I(x)\},
\tag{4}
\]
where \(b_I\) counts eligible nodes contained in \(I\). For length one this is immediate. If the root is not an eligible balanced split, the child bounds add to at most both \(s_I\) and \(|I|-s_I\). If it is eligible, with \(n=2q\) and child sums \(a\ne c\) satisfying \(a+c=q\), the child bounds give
\[
b_I\le 1+\min(a,q-a)+\min(c,q-c)
=1+2\min(a,c)\le a+c=q.
\]
The last inequality uses distinct nonnegative integer values \(a,c\). This proves (4) and the stated maximum-fiber upper bound. With \(k\le N/2\), place the ones in \(k\) different length-two dyadic intervals. Each gives an eligible split, so \(b(x)\ge k\); (4) forces equality. Complementing proves the \(k>N/2\) case.

**4. Rigidity of the absolute maximum.** If \(N=2\), attaining \(b=N/2\) means the unique adjacent pair is mixed. For \(N\ge4\), attainment of \(b=N/2\) forces total \(N/2\). If its root contrast were nonzero, the two child sums would be distinct integers adding to \(N/2\), and the preceding bound would be **strict** (at most \(N/2-1\)); hence the root contrast is zero and both children have totals \(N/4\). Saturation of the bound then forces each child separately to saturate. Inducting down the tree yields exactly one one in each bottom pair. Conversely, all such vectors have \(N/2\) eligible bottom pairs, and all their coarser details vanish. They therefore share the same measurement vector, and there are exactly \(2^{N/2}\) of them, proving uniqueness of the maximal measurement fiber.

## Verification

The standalone checker `checks/haar_phase_fibers.py` enumerates **every** binary signal of lengths \(2,4,8,16\), groups signals by the complete labelled phaseless Haar data, and independently computes the balanced-split exponent. For all \(65{,}536\) signals of length \(16\), the exact identity \(|\mathcal F(x)|=2^{b(x)}\), each fixed-weight sharp bound, the two singleton fibers, and the unique maximal fiber hold. The number of length-sixteen measurement fibers is \(3{,}256\); their size histogram at sizes \(1,2,4,8,16,32,64,128,256\) is respectively \(2,85,453,862,921,650,238,44,1\). Exact rational arithmetic also verifies local Parseval identities on all binary inputs of lengths \(2,4,8\). Run with `python3 checks/haar_phase_fibers.py` from the artifact root. The all-length theorem follows from the proof, not enumeration.

## Relationship to prior work

Wavelet phase retrieval and sign retrieval are established research questions. Alaifari, Bartolucci and Wellershoff (2023) prove injectivity up to sign for a **redundant multiwavelet** system on real continuous signals with Poisson/Hilbert-derived analyzing wavelets. Alaifari, Daubechies, Grohs and Thakur (2016) obtain continuous-signal recovery for suitably oversampled Meyer wavelets and other frames. Those results use different measurement families and do not determine fibers of a **nonredundant finite Haar basis restricted to binary inputs**. The present theorem quantifies, rather than merely exhibits, failure of injectivity and finds the exact fixed-weight extremal ambiguity. Classical Haar orthogonality and Parseval are standard and are not new ingredients.

## Limitations

The theorem requires a complete **labelled** set of Haar magnitudes together with the signed total and known binary or two-level alphabet. It does not imply the same counts for arbitrary real-valued signals, different wavelets, noisy data, omitted coefficients, absolute-only total, or unknown permutation of coefficient labels. An equivalent older statement from binary hierarchical data reconstruction has not been ruled out universally; independent literature and mathematical audit remain necessary.

## References

1. R. Alaifari, F. Bartolucci, M. Wellershoff, *Unique wavelet sign retrieval from samples without bandlimiting*, first posted 16 February 2023, arXiv:2302.08129, https://arxiv.org/abs/2302.08129.
2. R. Alaifari, I. Daubechies, P. Grohs, G. Thakur, *Reconstructing real-valued functions from unsigned coefficients with respect to wavelet and other frames*, first posted 27 January 2016, arXiv:1601.07579, https://arxiv.org/abs/1601.07579.
3. R. Alaifari, F. Bartolucci, M. Wellershoff, *Phase retrieval of bandlimited functions for the wavelet transform*, first posted 10 September 2020, arXiv:2009.05029, https://arxiv.org/abs/2009.05029.
4. I. Daubechies, *Ten Lectures on Wavelets*, SIAM, 1992; standard background for Haar orthogonality.
