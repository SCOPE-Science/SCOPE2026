# A quantized sharp Poincaré law for two-cluster ultrametrics

## Finding
Let \(X=A\sqcup B\) consist of two clusters of cardinalities \(m,n\ge2\), with mutual distance \(s\in(0,1]\) between distinct points in either cluster and distance \(1\) between clusters. Give every point mass \(1/(m+n)\), and write \(N=m+n\), \(H=\max(m,n)\), \(L=\min(m,n)\). The exact squared operator norm of the centering map from real Lipschitz functions modulo constants to ordinary Euclidean \(\ell_2(X)\) is
\[
\boxed{V_{m,n}(s):=\max_{\operatorname{Lip}(f)\le1}\sum_{x\in X}|f(x)-\overline f|^2=\max_{0\le k\le H}\left[L+ks^2-\frac{(L+ks)^2}{N}\right].}
\]
The integer \(k\) ranges over \(\{0,1,\dots,H\}\). Equivalently, with \(\theta(s)=N/2-L/s\),
\[
\boxed{V_{m,n}(s)=\frac{Ns^2}{4}+L(1-s)-\frac{s^2}{N}\operatorname{dist}\bigl(\theta(s),\mathbb Z_{\ge0}\bigr)^2.}
\]
The expression on the right is exact, including all integer-rounding effects.

For \(0<s<1\), every maximizer, up to translation, sign, and within-cluster permutations, takes the value \(1\) on all points of a smaller cluster and, on a larger cluster, takes the value \(s\) at exactly \(k\) points and \(0\) at its other \(H-k\) points, where \(k\) is a closest nonnegative integer to \(\theta(s)\). If the cluster sizes agree, either may be designated smaller. At \(s=1\), every maximizing function, up to translation and sign, is a balanced two-level \(0/1\) partition of the \(N\) points and \(V_{m,n}(1)=\lfloor N^2/4\rfloor/N\).

The sharp centered Poincaré inequality is
\[
\boxed{\frac1N\sum_{x\in X}|f(x)-\overline f|^2\le\frac{V_{m,n}(s)}{N}\operatorname{Lip}(f)^2.}
\]
It is attained by all the described maximizers. The constant remains \(HL/N\) when \(H\le L+1\), and also for \(H\ge L+2\) when \(s\le 2L/(N-1)\). When \(H\ge L+2\), strict improvement over this baseline occurs exactly for \(s>2L/(N-1)\). Every further phase change occurs at
\[
\boxed{s_j=\frac{2L}{N-(2j+1)}\quad\text{for integers }j\ge0\text{ satisfying }2j+1<H-L.}
\]
At each of these distinct values \(V_{m,n}\) is continuous but its right derivative minus its left derivative equals the same positive number \(2L/N\). Thus the sharp constant has a finite sequence of *equal-sized slope jumps*, with the active cardinality increasing by one at each jump.

## Assumptions and scope
All scalars and observables are real. The metric is an ultrametric because the largest distance in any triple is attained at least twice; for \(s=1\) it is equilateral. The Lipschitz seminorm is \(\operatorname{Lip}(f)=\max_{x\ne y}|f(x)-f(y)|/d(x,y)\), and \(\overline f=N^{-1}\sum_x f(x)\). Functions are considered modulo additive constants. The displayed sum uses counting measure; dividing by \(N\) gives probability variance, not a different sharp shape of extremizer. A common nonzero Lipschitz multiplier scales both sides quadratically.

## Proof
**1. Reduction to vertices.** Fix any one value of \(f\) to remove constant shifts. The set \(\{f:\operatorname{Lip}(f)\le1\}\) is a compact convex polytope. Its centered sum of squares is strictly convex on the quotient by constants: for distinct quotient vectors \(f,g\), the quadratic value at their midpoint is strictly below the mean of their values. Therefore every global maximizer is a vertex. A feasible function is a vertex exactly when the undirected graph of its *tight pairs*, namely pairs satisfying \(|f(x)-f(y)|=d(x,y)\), is connected. Indeed a connected tight graph determines all values from one basepoint; if it is disconnected, its components admit arbitrarily small independent shifts while preserving all strict inequalities across components, contradicting extremality.

**2. Shape of a vertex for \(0<s<1\).** A connected tight graph must contain a cross-cluster tight pair. All cross-cluster tight pairs have the same orientation: if \(f(b)-f(a)=1\) and \(f(a')-f(b')=1\) for \(a,a'\in A\), \(b,b'\in B\), then \(2\le|f(a)-f(a')|+|f(b)-f(b')|\le2s<2\), a contradiction. After a sign change and translation, let a tight pair satisfy \(f(a_0)=0\), \(f(b_0)=1\). From the Lipschitz constraints, every value on \(A\) lies in \([0,s]\), and every value on \(B\) lies in \([1-s,1]\). A value strictly inside either interval can form no tight pair, within or across clusters, and would be isolated in the tight graph. Hence every vertex has only the values \(0,s\) on \(A\) and \(1-s,1\) on \(B\).

**3. Only the larger cluster may split in an optimum.** Suppose \(a\) points of \(A\) carry \(s\) and \(b\) points of \(B\) carry \(1-s\). If \(a,b>0\), change one \(s\)-value in \(A\) to \(0\) and one \((1-s)\)-value in \(B\) to \(1\). All distances remain Lipschitz-admissible; the total sum is unchanged, while the sum of squares increases strictly by \(2s(1-s)>0\). Therefore a maximizer has \(a=0\) or \(b=0\). Assume \(m\ge n\), so \(H=m\), \(L=n\). If only the smaller cluster is split with \(b\ge1\), direct calculation relative to the all-constant-cluster variance gives
\[
\sum|f-\overline f|^2-\frac{HL}{N}=\frac{bs}{N}\bigl[s(N-b)-2H\bigr]<0,
\]
because \(N-b\le N-1\), \(s\le1\), and \(N-1-2H=L-H-1<0\). The same argument holds on interchanging the two clusters. Thus all maximizers for \(0<s<1\) have the larger cluster as their only possible nonconstant cluster.

**4. Exact maximizing integer.** Take all \(L\) points of the smaller cluster at \(1\), \(H-k\) larger-cluster points at \(0\), and \(k\) of them at \(s\). These choices are feasible for every integer \(0\le k\le H\), and their sum and sum of squares are \(L+ks\) and \(L+ks^2\). Therefore their centered variance is exactly
\[
F_k(s)=L+ks^2-\frac{(L+ks)^2}{N}.
\]
The preceding steps show that no other feasible function can exceed the maximum of these \(H+1\) candidates. Completing the square gives
\[
F_k(s)=\frac{Ns^2}{4}+L(1-s)-\frac{s^2}{N}\bigl(k-\theta(s)\bigr)^2.
\]
As \(\theta(s)<H\) for \(0<s\le1\), a nearest nonnegative integer lies in \(\{0,\dots,H\}\), yielding the rounded formula and the asserted extremizer classification for \(s<1\).

**5. Sharp transitions.** Adjacent branches satisfy
\[
F_{k+1}(s)-F_k(s)=\frac{s}{N}\bigl[(N-2k-1)s-2L\bigr].
\]
Thus the winning integer starts at \(k=0\) and increments exactly where \(\theta(s)\) crosses a half-integer, at the displayed \(s_j\) precisely when \(s_j<1\). At such a crossing, subtracting the derivatives gives
\[
F_{k+1}'(s_j)-F_k'(s_j)=\frac{2L}{N}>0.
\]
This proves the baseline, strict-imbalance criterion, transition list, and identical slope jumps. When \(s=1\), all distinct pair distances equal one, and the vertices of the Lipschitz ball are exactly two-level \(0/1\) functions. The centered variance is maximized by the two levels having sizes as equal as possible, yielding \(\lfloor N^2/4\rfloor/N\), consistent with the formula. This also proves the endpoint optimizer statement.

## Verification
The standard-library part of the standalone script `verify_two_cluster_variance.py` evaluates all four-level candidate families exactly with rational arithmetic for 600 cluster-size/scale combinations, validates the completed-square formula and the baseline transition, and checks 122 exact branch crossings and derivative jumps. Its optional SciPy component enumerates the actual vertices of the *full* centered Lipschitz polytope for 27 small metric instances; this enumeration is independent of the four-level classification. Run `python3 verify_two_cluster_variance.py` using Python 3, NumPy and SciPy. Expected final line: `ALL_TWO_CLUSTER_LIPSCHITZ_VARIANCE_TESTS_OK`. These tests corroborate the proof, not replace the universal argument.

## Relationship to prior work
Barthe and O'Connell's *Matchings and the variance of Lipschitz functions* studies exact maximal observable variance for Gaussian and Euclidean-ball distributions, not finite two-level ultrametrics [1]. Cúth and Doucha establish general Banach-space structure of Lipschitz-free spaces over ultrametric spaces, but not this exact centered Lipschitz-to-Euclidean norm or its cardinality-transition law [2]. Nakajima and Shioya study observable variance and its rigidity under geometric isoperimetric hypotheses; their inspected results do not specialize to this finite uniformly weighted ultrametric classification [3]. A published exact four-point ultrametric Banach–Mazur calculation and a published clustered free-space projection-constant calculation concern different optimized operators and do not imply the variance formula [4,5]. The sharp variance-to-range profile law for prescribed atom probabilities [6] does not impose the independent within-cluster Lipschitz restrictions or optimize the resulting constrained variance, so it supplies a global range bound rather than the present sharp operator norm. The relation between centered real Lipschitz observables, their sharp variance and a discrete hierarchy of extremizer cardinalities is the asserted contribution. No claim of exhaustive global priority follows from these comparisons.

## Limitations
The classification assumes two nonempty equal-radius equilateral clusters of at least two points each, uniform atomic masses, and real Lipschitz observables. It does not address unequal within-cluster radii, nonuniform masses, more hierarchical levels, or \(L^p\) deviations with \(p\ne2\). The observed phase ladder is exact for this family and is not asserted for arbitrary finite ultrametrics. Unindexed equivalent results may exist. The stated finite checks corroborate the formulas but do not replace the universal analytic argument.

## References
[1] F. Barthe and N. O'Connell, *Matchings and the variance of Lipschitz functions*, ESAIM Probability and Statistics 13 (2009), 400–408, first verifiable online publication 2009-09-22, DOI:10.1051/ps:2008018.

[2] M. Cúth and M. Doucha, *Lipschitz-free spaces over ultrametric spaces*, arXiv:1411.2434v1 (2014-11-10), https://arxiv.org/abs/1411.2434.

[3] H. Nakajima and T. Shioya, *Isoperimetric rigidity and distributions of 1-Lipschitz functions*, arXiv:1801.01302v1 (2018-01-04), https://arxiv.org/abs/1801.01302.

[4] *Exact Hilbert distortion of a balanced four-point ultrametric*, published mathematical research record, 2026-10-11, identifier 471d4a0126f4.

[5] *Sharp optimal projection constants for clustered finite metric free spaces*, published mathematical research record, 2026-10-11, identifier bd13acd51aa3.

[6] *Exact fixed-profile range of variance relative to squared range*, published mathematical research record, 2026-10-04, identifier cdf5b2d6b4a3.
