# Root-split boundary localization of Yule cherry moments

## Finding
For every integer \(n\ge10\), let \(C_n\) count cherries in a rooted Yule–Harding–Kingman (YHK) binary tree on \(n\) leaves, and let \(K_n\) be the leaf count in a randomly oriented root daughter subtree. Thus \(K_n\) is uniform on \(\{1,\ldots,n-1\}\). Write \(s=\min\{k,n-k\}\) and define
\[
 a_n(k)=\begin{cases}-1/3&s=1,\\1/3&s=2,\\0&s\ge3,\end{cases}
\qquad
 b_n(k)=\frac1{45}\begin{cases}
 -10n+3&s=1,\\10n+1&s=2,\\-6&s=3,\\2&s=4,\\0&s\ge5.
 \end{cases}
\]
Then the **complete root-split regression profiles of the first two cherry moments** are
\[
 \mathbb E[C_n\mid K_n=k]=\frac n3+a_n(k),
 \qquad
 \mathbb E[C_n^2\mid K_n=k]=\frac{n^2}{9}+\frac{2n}{45}+b_n(k).
\]
The first profile differs from the unconditional mean only at the two outermost split sizes; the second differs only at the four outermost split sizes. Consequently, for every real function \(g\) on \(\{1,\ldots,n-1\}\),
\[
 \operatorname{Cov}(C_n,g(K_n))=
 \frac{g(2)+g(n-2)-g(1)-g(n-1)}{3(n-1)},
\]
\[
 \operatorname{Cov}(C_n^2,g(K_n))=
 \frac{(-10n+3)[g(1)+g(n-1)]+(10n+1)[g(2)+g(n-2)]-6[g(3)+g(n-3)]+2[g(4)+g(n-4)]}{45(n-1)}.
\]
In particular, the extreme-root event \(E_n=\{\min(K_n,n-K_n)\le2\}\), of probability \(4/(n-1)\), is invisible to the mean but not to the variance:
\[
 \mathbb E[C_n\mid E_n]=\mathbb E C_n=\frac n3,
 \qquad
 \operatorname{Var}(C_n\mid E_n)=\frac{2(n+1)}{45}
 =\operatorname{Var}(C_n)+\frac2{45}.
\]

## Assumptions and scope
The YHK law is the leaf-splitting model: begin with a rooted cherry and repeatedly choose uniformly one current leaf to bifurcate until \(n\) leaves exist; labeling the final leaves uniformly does not change these shape statistics. The two root branches are independently assigned an orientation at the start, making \(K_n\) the size of a named branch. A cherry is a pair of leaves sharing one immediate parent. A one-leaf daughter subtree contains no cherry by convention. All stated identities are exact for **every integer \(n\ge10\)**. They concern unweighted tree topology, not evolutionary branch lengths or the PDA tree model.

## Proof
**Root-split law and conditional factorization.** Starting with one leaf in each root daughter, when there are \(m\) leaves the left daughter gains the next leaf with probability equal to its current size divided by \(m\). This is the two-color Pólya urn initially containing one ball of each color; its final left size is uniform on \(\{1,\ldots,n-1\}\). Conditional on the two daughter sizes, all leaf splits within each daughter were uniform among the leaves currently in that daughter, and these internal choices are independent. Hence, given \(K_n=k\), the two daughter trees are independent YHK trees of respective sizes \(k\) and \(n-k\). No cherry straddles the root for \(n\ge3\), so
\[
 C_n\mid\{K_n=k\}\ \overset d=\ C_k'+C_{n-k}'',
\]
with independent variables on the right.

**Small-size corrections.** Let \(\mu_m=\mathbb E C_m\) and \(v_m=\operatorname{Var}(C_m)\). The established YHK moments are \(\mu_m=m/3\) for \(m\ge3\), and \(v_m=2m/45\) for \(m\ge5\). Directly from the leaf-splitting rule, \(\mu_1=0,\mu_2=1\), and \(v_1=v_2=v_3=0,v_4=2/9\). Define
\[
 \delta_m=\mu_m-m/3=\begin{cases}-1/3&m=1,\\1/3&m=2,\\0&m\ge3,\end{cases}
\]
\[
 \varepsilon_m=v_m-2m/45=\begin{cases}-2/45&m=1,\\-4/45&m=2,\\-6/45&m=3,\\2/45&m=4,\\0&m\ge5.\end{cases}
\]
The conditional independent sum gives
\[
 \mathbb E[C_n\mid K_n=k]=n/3+\delta_k+\delta_{n-k},\quad
 \operatorname{Var}(C_n\mid K_n=k)=2n/45+\varepsilon_k+\varepsilon_{n-k}.
\]
For \(n\ge10\), no split can have both daughter sizes below five. Therefore only one daughter can contribute a correction. With \(d=\delta_k+\delta_{n-k}\) and \(e=\varepsilon_k+\varepsilon_{n-k}\),
\[
 \mathbb E[C_n^2\mid K_n=k]-\left(n^2/9+2n/45\right)
 =2nd/3+d^2+e.
\]
For \(s=1,2,3,4\), substitution gives respectively \((-10n+3)/45\), \((10n+1)/45\), \(-6/45\), and \(2/45\), while all interior cases give zero. This proves both regression tables without relying on any finite-range enumeration.

**Covariance profiles.** The conditional-correction sums vanish because \(\sum_{k=1}^{n-1}a_n(k)=\sum_{k=1}^{n-1}b_n(k)=0\). Since \(K_n\) is uniform, \(\operatorname{Cov}(C_n^r,g(K_n))=(n-1)^{-1}\sum_k g(k)\,[\mathbb E(C_n^r\mid K_n=k)-\mathbb E C_n^r]\) for \(r=1,2\). Substitution gives the two displayed formulas.

**A mean-invisible extreme root.** The event \(E_n\) comprises exactly \(k=1,2,n-2,n-1\), each with equal conditional probability. The two mean corrections \(-1/3\) and \(+1/3\) cancel. The conditional variance is the mean of the four within-split variances plus the variance of their conditional means. The within-split average is \(2n/45-1/15\), and the between-split variance is \(1/9\). Their sum is \(2(n+1)/45\), proving the claimed positive variance increment.

## Verification
The accompanying standard-library-only `verify.py` uses exact rational arithmetic. It independently builds the Yule cherry probability distributions by the leaf-splitting transition \(\Pr(C_{m+1}=c\mid C_m=c)=2c/m\), convolves independently generated daughter distributions, and checks the two conditional-moment tables and the extreme-root event for all \(10\le n\le65\) and every valid split. A separate direct enumeration of all Yule leaf-splitting histories through eight leaves checks uniform root-split counts. The script reports **4,228 exact checks**. These computations check implementations and small cases; the proof above, not the finite checks, establishes the all-size statements.

## Relationship to prior work
McKenzie and Steel (1999, Technical Report No. 177; subsequently published in 2000) established the marginal Yule cherry mean and variance and the cherry generating-function recursion, which are used as inputs here. Harding's rooted-tree branching model provides the standard split framework. Wu and Choi (2015 preprint; 2016 journal) developed the joint cherry–pitchfork distribution under YHK and PDA, a different pair of statistics. The claimed contribution is the complete **conditional first- and second-moment dependence on root daughter size**, the finite four-layer localization, and the mean-invisible variance change. The two earlier inspected texts do not state or entail an already-given bivariate law between root split and cherries; their marginal results plus the standard branching construction make the present calculation possible but do not itself display the claimed dependence structure.

## Limitations
Historical priority is not guaranteed: a root-split/cherry mixed-moment identity may appear under another tree-index terminology. The result is exact only for the YHK model and integer \(n\ge10\); smaller cases require overlapping-boundary corrections. No higher conditional moments, full joint distribution, or independence of cherry count and root imbalance is claimed. In fact, the displayed covariance shows dependence at exceptional root splits. No independent external audit has been performed.

## References
1. A. McKenzie and M. Steel, *Distributions of cherries for two models of trees*, Biomathematics Research Centre Technical Report No. 177, University of Canterbury, May 6, 1999 (journal version: *Mathematical Biosciences* **164** (2000), 81–92). https://ir.canterbury.ac.nz/bitstreams/246ff6f4-967f-4550-9f98-c4b3d671fe84/download
2. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, preprint arXiv:1508.03139, first submitted August 13, 2015 (journal version: *Theoretical Population Biology* **108** (2016), 13–23). https://arxiv.org/abs/1508.03139 ; accepted text: https://ueaeprints.uea.ac.uk/id/eprint/55603/1/Pattern_stat_TPB_final.pdf
3. E. F. Harding, *The probabilities of rooted tree-shapes generated by random bifurcation*, *Advances in Applied Probability* **3** (1971), 44–77.
