# Geometric fixed-rank singular staircase for finite-tree Cesàro averaging

## Finding
Let \(b\ge2\) be an integer and let \(\mathcal T_{b,N}\) be the complete rooted \(b\)-ary tree of height \(N\ge0\), with one vertex at depth zero. On complex counting-measure \(\ell^2(\mathcal T_{b,N})\), define the **ancestor Cesàro operator**
\[
 (C_{b,N}f)(v)=\frac1{|v|+1}\sum_{u\preceq v}f(u).
\]
Write \(s_1(C_{b,N})\ge s_2(C_{b,N})\ge\cdots\) for singular values, including multiplicity. For every **fixed** integer \(j\ge1\), as \(N\to\infty\) with \(b\) fixed,
\[
 \boxed{\lim_{N\to\infty}(N+1)b^{-N/2}s_j(C_{b,N})
 =\frac{b}{b-1}\,b^{-\lceil\log_b j\rceil/2}.}
\]
The limiting positive values are \(b/(b-1)\), followed by \((b/(b-1))b^{-1/2}\) with multiplicity \(b-1\), followed by \((b/(b-1))b^{-1}\) with multiplicity \(b(b-1)\), and so on. In particular,
\[
\|C_{b,N}\|=\frac{b}{b-1}\frac{b^{N/2}}{N+1}(1+o(1)),\qquad
\lim_{N\to\infty}\frac{s_2(C_{b,N})}{s_1(C_{b,N})}=b^{-1/2}.
\]
For every finite \(N\), the largest singular value is simple and its right singular vector is strictly positive and constant on each level. The full finite-height singular multiset is described exactly by the matrix blocks below.

## Assumptions and scope
The order \(u\preceq v\) means that \(u\) lies on the unique path from the root to \(v\), including both endpoints; \(|v|\) denotes depth. Each vertex carries counting measure, *not* level-normalized probability measure. The branching number \(b\) is a fixed integer at least two while height \(N\) grows; \(j\) must be fixed before taking the limit. The theorem makes no claim about ranks growing with \(N\). Matrix singular values refer to the ordinary complex Hilbert norm; real matrices have identical singular values.

## Proof
**1. Radial block.** Let \(e_\ell\) be the unit vector uniformly distributed on level \(\ell\): \(e_\ell(v)=b^{-\ell/2}\) when \(|v|=\ell\), zero otherwise. The radial subspace is invariant. On \(e_0,\ldots,e_N\) the operator has the lower-triangular matrix
\[
 A_N(j,\ell)=\frac{b^{(j-\ell)/2}}{j+1}\,\mathbf1_{\{\ell\le j\}},
 \qquad 0\le j,\ell\le N.
\]
This follows by summing the single level-\(\ell\) ancestor of each vertex of level \(j\) and multiplying by the square root \(b^{j/2}\) of that level's size.

**2. Every transverse block.** For each vertex \(w\) at depth \(k-1\), \(1\le k\le N\), choose an orthonormal basis of the \((b-1)\)-dimensional child-contrast space \(\{c\in\mathbb C^b:\sum_{i=1}^b c_i=0\}\). For a contrast vector \(c\) and each \(\ell\ge k\), put the value \(b^{-(\ell-k)/2}c_i\) at descendants of the \(i\)-th child of \(w\) on level \(\ell\), and zero elsewhere. The resulting vectors at different levels are orthonormal. Contrasts at distinct vertices are mutually orthogonal, even for nested vertices, because all child-contrast sums vanish. Together with the radial vectors, they form an orthonormal basis: their dimensions sum to
\[
 (N+1)+\sum_{k=1}^N(b-1)b^{k-1}(N-k+1)
 =\sum_{\ell=0}^N b^\ell.
\]
Each fixed-contrast span is invariant under ancestor averaging. On its levels \(k,\ldots,N\), its matrix is the trailing principal block \(A_N^{(k)}=A_N[k{:}N,k{:}N]\). Thus the complete multiset of singular values consists of those of \(A_N\), plus those of \(A_N^{(k)}\), each repeated \((b-1)b^{k-1}\) times for every \(1\le k\le N\). This is an **exact finite-dimensional unitary decomposition**, not an asymptotic approximation.

**3. Strict finite-height leading eigenvalue.** For \(N\ge1\), every entry of \(A_N^*A_N\) is strictly positive: its last row contribution is strictly positive. Perron--Frobenius theory therefore makes the top right singular vector of \(A_N\) strictly positive and its top singular value simple. Every proper trailing block is a compression to proper input and output coordinate subsets. Equality of its norm to \(\|A_N\|\) would extend an attaining vector by zero to a top right singular vector of \(A_N\), contradicting strict positivity. Hence the entire operator's leading singular value is simple and radial. The case \(N=0\) is a one-dimensional identity.

**4. Sharp limit for each block.** Set \(a_N=(N+1)b^{-N/2}\). Reverse the output level index using \(h=N-j\), but keep the input index \(\ell\). Extend \(a_NA_N^{(k)}\) by zero to an operator on \(\ell^2(\mathbb N_0)\). Its entries are
\[
 K_{N,k}(h,\ell)=\mathbf1_{\{\ell\ge k,\ h+\ell\le N\}}
 \frac{N+1}{N-h+1}\,b^{-(h+\ell)/2}.
\]
For \(h+\ell\le N\), the factor \((N+1)/(N-h+1)\) is at most \(h+1\). Therefore
\[
 |K_{N,k}(h,\ell)|\le (h+1)b^{-(h+\ell)/2},
\]
whose square is summable over \(h,\ell\ge0\) for every \(b>1\). Pointwise, for fixed \(h,\ell\), the entries converge to \(u_h v^{(k)}_\ell\), where \(u_h=b^{-h/2}\) and \(v^{(k)}_\ell=b^{-\ell/2}\mathbf1_{\{\ell\ge k\}}\). Dominated convergence in the double sum proves **Hilbert--Schmidt convergence** to the rank-one operator \(u\otimes v^{(k)}\). Its only nonzero singular value is
\[
 \|u\|_2\|v^{(k)}\|_2
 =\left(\frac b{b-1}\right)b^{-k/2}.
\]
Thus, for each fixed \(k\), the leading singular value of \(a_NA_N^{(k)}\) tends to this number, while every other singular value tends to zero.

**5. Ordering across infinitely many contrasts.** Proper trailing blocks satisfy \(\|A_N^{(k+1)}\|\le\|A_N^{(k)}\|\), as they are compressions. Fix \(m\). For the finitely many blocks with \(0\le k\le m\), Step 4 gives one limiting nonzero singular value per block with the multiplicity from Step 2, and all their other singular values vanish. Every block with \(k\ge m+1\) has top singular value bounded by \(\|a_NA_N^{(m+1)}\|\), which tends to \((b/(b-1))b^{-(m+1)/2}\), strictly smaller than the limiting \(k=m\) value. Hence the ordered, normalized first \(b^m\) singular values converge, with successive multiplicities \(1,(b-1),b(b-1),\ldots,(b-1)b^{m-1}\). Since \(m\) is arbitrary, this proves the displayed formula for every fixed rank \(j\) and the norm and gap consequences. \(\square\)

## Verification
Run `python checker.py` with NumPy installed. The standalone program independently constructs the original vertex-indexed matrix and compares its entire finite singular-value multiset against the block decomposition for binary, ternary and quaternary trees. It additionally tests the scaled first and second singular values of block matrices at heights \(40,80,120\). This program passed **133 finite assertions**. The infinite-rank-in-height theorem is justified by Step 4's Hilbert--Schmidt convergence and Step 5's uniform tail separation, not by numerical extrapolation. The code does not supply a rigorous finite-\(N\) error bound for the displayed \(o(1)\).

## Relationship to prior work
Evans, Harris and Lang analyzed approximation numbers for Hardy integral operators on metric trees, including asymptotic estimates under their geometric hypotheses. Lifshits and Linde analyzed weighted summation operators on discrete trees, focusing on entropy numbers from \(\ell^1\) to \(\ell^q\); the adjoint of the present operator fits their general weighted-summation framework with input weight one and output weight \(1/(|v|+1)\). Vasil'eva studied norm estimates for weighted ancestor sums, including \(\ell^p\)-to-\(\ell^q\) estimates for \(p<q\), but the inspected statements do not give the present *sharp fixed-rank Hilbert singular values*. A geometrically damped ancestor kernel has different exact singular values: a diagonal similarity or nonunitary weighting does not preserve the singular spectrum. The decisive new assertion here is the explicit geometric limiting staircase and its branch-multiplicity law, not the basic definition of tree summation.

## Limitations
Only complete regular finite trees and the ordinary counting Hilbert norm are covered. No uniform claim for ranks \(j\) growing with height, nonregular trees, or other \(\ell^p\) norms is proved. The asserted originality is based on the inspected material and qualified literature searches; an equivalent result hidden in inaccessible weighted-summation/width literature cannot be ruled out. Numerical checks are finite consistency tests, not a substitute for the proof. Independent historical-priority and mathematical audits have not been performed.

## References
1. W. D. Evans, D. J. Harris and J. Lang, *The approximation numbers of Hardy-type operators on trees*, arXiv:math/0003215 (first posted March 30, 2000), https://arxiv.org/html/math/0003215v1.
2. M. Lifshits and W. Linde, *Compactness Properties of Weighted Summation Operators on Trees*, arXiv:1006.3867 (first posted June 19, 2010), https://arxiv.org/abs/1006.3867.
3. A. A. Vasil'eva, *Estimates for norms of two-weighted summation operators on a tree under some conditions on weights*, arXiv:1311.0375 (first posted November 2, 2013), https://arxiv.org/abs/1311.0375.
4. A. A. Vasil'eva, *Estimates for norms of two-weighted summation operators on trees for \(1<p<q<\infty\)*, arXiv:1509.06974 (first posted September 18, 2015), https://arxiv.org/abs/1509.06974.
5. A. A. Vasil'eva, *Estimates for \(n\)-widths of two-weighted summation operators on trees*, *Mathematical Notes* 99 (2016), 243--252, https://doi.org/10.1134/S0001434616010260 (abstract available; the complete text was not inspected).
