# A sharp three-regime tail law for two-column volume sampling

## Finding

Let \(X=(x_1,x_2,x_3,x_4,x_5)\in\mathbb R^{1\times5}\) have nonzero real entries. Sample an unordered pair \(S\subset\{1,2,3,4,5\}\), \(|S|=2\), by exact volume sampling:
\[
\Pr_X(S=\{i,j\})=\frac{x_i^2+x_j^2}{4\sum_{r=1}^{5}x_r^2}.
\]
Define its squared Frobenius representation amplification by
\[
T_X(S)=\|X_S^{\dagger}X\|_F^2=\frac{\sum_{r=1}^{5}x_r^2}{x_i^2+x_j^2}.
\]
For every real \(t>0\), the **sharp universal tail envelope**, with the event defined inclusively, is
\[
\boxed{\sup_{X\,:\,x_i\ne0}\Pr_X\{T_X\ge t\}=\begin{cases}
1,&0<t\le5/2,\\
3/t-1/2,&5/2<t\le3,\\
3/(2t),&t\ge3.
\end{cases}}
\]
The bounds are attained for every threshold, by explicit positive squared-column masses. In particular, the extremal risk changes shape at \(t=3\) and drops discontinuously from \(1\) at \(t=5/2\) to a right-hand limit of \(7/10\). The exact mean \(\mathbb E T_X=5/2\) is constant across all nonzero \(X\) in this class, so the tail envelope adds information not contained in the known expectation identity.

## Assumptions and scope

Only rank-one, five-column real matrices are considered. All five columns are nonzero. Sample exactly two distinct indices without replacement, with probabilities proportional to \(\det(X_S X_S^{\mathsf T})\). The Moore--Penrose inverse and Frobenius norm have their standard definitions. The probability and supremum are with respect to this one random subset, with \(X\) otherwise fixed. The theorem is not a tail bound for arbitrary row dimension, sample size, or sequential/replacement sampling.

Introduce normalized squared masses \(p_i=x_i^2/\sum_r x_r^2>0\), with \(\sum_i p_i=1\). Every positive mass vector arises from nonzero columns, for example \(x_i=\sqrt{p_i}\). Then
\[
\Pr\{S=\{i,j\}\}=\frac{p_i+p_j}{4},\qquad T_X(\{i,j\})=\frac{1}{p_i+p_j}.
\]
Write \(\theta=1/t\); a pair is *light* when \(p_i+p_j\le\theta\). If \(E_\theta\) is the collection of light pairs, its total weight is \(W_\theta=\sum_{\{i,j\}\in E_\theta}(p_i+p_j)\), and the sought probability is \(W_\theta/4\).

## Proof

**Step 1: exact reduction and mean.** For a nonzero row \(X_S\in\mathbb R^{1\times2}\), its Moore--Penrose inverse is \(X_S^{\mathsf T}/\|X_S\|_2^2\), giving the formula above. The volume-sampling normalizer is \(\sum_{i<j}(p_i+p_j)=4\); hence
\[
\mathbb E_X T_X=\frac14\sum_{i<j}(p_i+p_j)\frac{1}{p_i+p_j}=\frac{10}{4}=\frac52.
\]

**Step 2: at most seven light pairs when \(\theta<2/5\).** Reorder the masses so that \(p_1\le p_2\le p_3\le p_4\le p_5\). The two largest pair sums are \(p_4+p_5\) and \(p_3+p_5\), with harmless ties. If at least eight of the ten pairs were light, every edge other than at most those two largest pairs would be light. In particular, the five edges \(\{1,5\},\{5,2\},\{2,4\},\{4,3\},\{3,1\}\) would be light. These edges form a five-cycle and their weights sum to \(2\sum_i p_i=2\). Five light inequalities would give \(2\le5\theta<2\), impossible. Thus there are at most seven light pairs.

**Step 3: classify seven light pairs.** Suppose exactly seven pairs are light and \(\theta<2/5\). The three heavy pairs, which have weights strictly greater than \(\theta\), must be the three largest pair sums. Hence they are \(\{4,5\}\), \(\{3,5\}\), and one of \(\{2,5\}\) or \(\{3,4\}\), accounting for ties. The first alternative is impossible: if the heavy pairs are \(\{2,5\},\{3,5\},\{4,5\}\), then \(\{1,5\}\) and \(\{3,4\}\) are light. As \(p_2\le p_3\le p_4\),
\[
1=(p_1+p_5)+(p_3+p_4)+p_2\le\theta+\theta+\theta/2=5\theta/2<1,
\]
a contradiction. Thus the heavy pairs are exactly the triangle \(\{3,4\},\{3,5\},\{4,5\}\). Set \(s=p_1+p_2\). The other seven edges are light, and their aggregate mass is
\[
W_\theta=4s+2(1-s)=2+2s.
\]
In particular, the six light cross-pairs with one endpoint in \(\{1,2\}\) and the other in \(\{3,4,5\}\) give
\[
6\theta\ge3s+2(1-s)=2+s,
\]
so \(W_\theta\le12\theta-2\). If at most six pairs are light, trivially \(W_\theta\le6\theta\). For \(0<\theta<2/5\), therefore,
\[
\frac{W_\theta}{4}\le\frac14\max\{6\theta,12\theta-2\}=\begin{cases}
3\theta/2,&0<\theta\le1/3,\\
3\theta-1/2,&1/3\le\theta<2/5.
\end{cases}
\]

**Step 4: all upper bounds are attained.** For \(0<\theta\le1/3\), choose
\[
(p_1,\ldots,p_5)=(\theta/2,\theta/2,\theta/2,\theta/2,1-2\theta).
\]
Exactly the six pairs in the first four positions are light; their sum is \(6\theta\). For \(1/3<\theta<2/5\), choose
\[
(p_1,\ldots,p_5)=(3\theta-1,3\theta-1,1-2\theta,1-2\theta,1-2\theta).
\]
Exactly the six cross-pairs and the one small--small pair are light, with total mass \(12\theta-2\). Every specified mass is strictly positive on its stated interval. For \(\theta\ge2/5\), uniform masses \(p_i=1/5\) make all ten pairs light, attaining probability one. Substituting \(\theta=1/t\) gives the claimed three-regime law. The two formulas meet at \(t=3\); at \(t=5/2\), inclusion of equality gives probability one, while the right-hand limit is \(7/10\). This proves the theorem.

## Verification

The standalone standard-library file `verify.py` checks exact rational identities and sharp mass vectors at eleven thresholds, together with 127,600 exhaustive comparisons over strictly positive integer-composition grids of total mass \(8\), \(12\), \(18\), or \(24\), and 100 nonuniform exact expectation identities. Run `python verify.py` with Python 3. The exhaustive finite tests are corroboration of the proof, **not** a proof for arbitrary real masses; Steps 2--4 establish the infinite statement. All numerical values in the displayed theorem are derived as exact rational expressions.

## Relationship to prior work

Kozyrev and Osinsky's October 6, 2026 paper studies \(\|X_S^\dagger X\|_F\), exact volume sampling and algorithms with the optimal universal expectation guarantee. Its equation for the expected squared amplification specializes to \(5/2\) here. The present result instead optimizes a *tail probability over all rank-one five-column inputs* for every threshold, and supplies two extremal squared-mass configurations separated by a sharp phase transition. The paper's expectation equality alone does not imply the piecewise tail or its sharpness. Earlier volume-sampling research develops unbiased pseudoinverse estimates and regression loss guarantees; those results concern different functionals or statistical comparisons. Search and text inspection do not constitute exhaustive historical-priority certification.

## Limitations

This is an exact small-instance theorem, not a concentration theorem in increasing dimension. It does not bound errors from approximate sampling, numerical roundoff, non-volume designs or non-rank-one matrices. Other weighted-threshold-graph formulations might yield an equivalent older inequality; historical priority remains a residual risk. The proof itself is finite combinatorics and linear algebra; independent external validation has not been performed.

## References

- I. Kozyrev and A. Osinsky, *Subset selection for matrices by volume sampling*, arXiv:2610.08576v1, first posted October 6, 2026. https://arxiv.org/html/2610.08576v1
- M. Dereziński and M. K. Warmuth, *Unbiased estimates for linear regression via volume sampling*, arXiv:1705.06908, first posted May 19, 2017. https://arxiv.org/abs/1705.06908
- M. Dereziński, M. K. Warmuth, and D. Hsu, *Leveraged volume sampling for linear regression*, NeurIPS 2018. https://proceedings.neurips.cc/paper_files/paper/2018/file/2ba8698b79439589fdd2b0f7218d8b07-Paper.pdf
