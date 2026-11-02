# A two-scale sign reversal for cherry leaves and path length in Yule trees

## Finding

**Theorem (local-positive, global-negative depth dependence).** Grow a rooted binary tree by replacing one uniformly chosen leaf with a pair of child leaves at each step. At size \(n\), let \(C_n\) be the number of cherries (pairs of sibling leaves) and \(S_n\) the sum of all leaf depths, with root depth zero. Independently choose a uniformly random leaf of the final tree. Write \(D_n\) for its depth and \(I_n\) for the indicator that it belongs to a cherry.

For every integer \(n\geq3\), the **local** association has the exact positive value
\[
\operatorname{Cov}(I_n,D_n)=\frac29,
\qquad
\mathbb E[D_n\mid I_n=1]-\mathbb E[D_n\mid I_n=0]=1.
\]
Yet the **global** cherry-count/path-length association is
\[
\operatorname{Cov}(C_n,S_n)=-\frac{(n-3)(n+2)}{9(n-1)},
\qquad n\geq3,
\]
which is strictly negative for every \(n\geq4\), zero for \(n=3\), and asymptotic to \(-n/9\).

The mechanism is an exact cherry-weighted depth identity. Let \(Q_n\) be the sum of the depths of leaves belonging to cherries, with each such leaf counted once. Then
\[
\mathbb E[Q_n]=\frac23\mathbb E[S_n]+\frac{2n}{9},
\qquad n\geq3.
\]
These are identities under the leaf-splitting Yule–Harding–Kingman topology law, not assertions for uniformly selected labeled binary trees or for arbitrary time-weighted phylogenies.

## Assumptions and scope

Start at one root leaf. At each stage with \(k\) leaves, independently select one of the \(k\) current leaves with probability \(1/k\), delete it, and place two children at its position. Continue to exactly \(n\) leaves. Internal edge lengths are irrelevant; a leaf's depth counts the number of root-to-leaf edges. The model is the standard Yule leaf-splitting topology law, whether or not labels are subsequently assigned uniformly. A *cherry* is an internal node with two leaf children.

The final sampled leaf is uniform **conditional on the complete random tree**. Thus the local conditional means above concern this two-stage law; they do not mean sampling a uniformly random tree and then independently giving equal weight to each distinct cherry.

For \(n=2\), the only tree has \(C_2=1\), \(S_2=2\), and every leaf is a cherry leaf, so the global covariance is zero and the comparison conditioned on \(I_2=0\) is undefined. The nontrivial formulas begin at \(n=3\).

## Proof

Fix any tree with \(k\geq2\) leaves. For each leaf \(v\), let \(d(v)\) be its depth and \(b(v)\) indicate membership in a cherry. There are exactly \(2C\) cherry leaves, and the sum of \(b(v)d(v)\) over leaves is \(Q\). If a uniformly chosen leaf \(V\) splits, directly from the definitions,
\[
\begin{aligned}
S'&=S+d(V)+2,\\
C'&=C+1-b(V),\\
Q'&=Q+2(d(V)+1)-2b(V)d(V).
\end{aligned}
\]
For the last line, splitting a non-cherry leaf adds a new cherry with two new depths; splitting a cherry leaf removes the old cherry's two depth contributions and adds those of the new cherry. Taking conditional expectations gives
\[
\begin{aligned}
\mathbb E[C'\mid T]&=(1-2/k)C+1,\\
\mathbb E[S'\mid T]&=(1+1/k)S+2,\\
\mathbb E[Q'\mid T]&=(1-2/k)Q+(2/k)S+2.
\end{aligned}
\]
Multiplying the first two increment identities **before** averaging, and using the same cherry-depth sum, also gives
\[
\mathbb E[C'S'\mid T]
=(1-1/k)CS+(1+1/k)S+(2-4/k)C-Q/k+2.
\]
All four identities hold separately for every possible tree; no distributional approximation is involved.

Write \(c_k=\mathbb E[C_k]\), \(s_k=\mathbb E[S_k]\), \(q_k=\mathbb E[Q_k]\), and \(r_k=\mathbb E[C_kS_k]\). At size two, \((c_2,s_2,q_2,r_2)=(1,2,2,2)\), and after one split \((c_3,s_3,q_3,r_3)=(1,5,4,5)\). Averaging the conditional recurrences and inducting from size three yields
\[
 c_k=\frac{k}{3},\qquad
 s_k=2k(H_k-1),\qquad
 q_k=\frac23s_k+\frac{2k}{9},
 \qquad k\geq3,
\]
where \(H_k=\sum_{j=1}^{k}1/j\). For example, the first two formulas follow by direct substitution in their first-order recurrences, and the third follows by substituting them into
\[
q_{k+1}=(1-2/k)q_k+(2/k)s_k+2
\]
and verifying the displayed expression at \(k=3\).

To obtain the global covariance, put \(K_k=r_k-c_ks_k\). Subtracting the product of the recurrences for \(c_{k+1}\) and \(s_{k+1}\) from that for \(r_{k+1}\) gives exactly
\[
K_{k+1}=(1-1/k)K_k+\frac{2c_ks_k}{k^2}-\frac{q_k}{k}.
\]
Using the three established mean identities, the last two terms combine to \(-2/9\) for every \(k\geq3\). Therefore
\[
K_{k+1}=\frac{k-1}{k}K_k-\frac29,
\qquad K_3=0.
\]
The claimed closed form \(K_k=-(k-3)(k+2)/(9(k-1))\) satisfies this recursion and its initial condition. This proves the global formula and its strict sign and asymptotic value.

Finally, uniform conditional sampling of one leaf gives
\[
\mathbb E[I_n]=\frac{2c_n}{n}=\frac23,
\quad\mathbb E[D_n]=\frac{s_n}{n},
\quad\mathbb E[I_nD_n]=\frac{q_n}{n}.
\]
Hence \(\operatorname{Cov}(I_n,D_n)=2/9\). As \(\mathbb P(I_n=1)=2/3\) and \(\mathbb P(I_n=0)=1/3\), the two conditional depth means are respectively
\[
\mathbb E[D_n\mid I_n=1]=\frac{s_n}{n}+\frac13,
\qquad
\mathbb E[D_n\mid I_n=0]=\frac{s_n}{n}-\frac23.
\]
Their difference is exactly one, completing the theorem.

## Verification

The standalone `verify_yule.py` contains independent exact enumeration of the Yule leaf-splitting histories through nine leaves, checks the key conditional transition identities over all 873 histories through seven leaves, and tests the rational closed forms and recurrences through 1,001 leaves. Run with `python3 verify_yule.py`; it uses only the Python standard library.

In the packaged verification, the executable reported `PASS: 60677 exact assertions; 46233 growth histories; 873 independent transition cases.` These finite checks test the implementation and algebra but are **not** used as an infinite-size proof; the conditional identities and induction above establish the theorem for all specified sizes.

## Relationship to prior work

The Yule model and cherries are classical. McKenzie and Steel study the marginal distribution of cherry counts. Mir, Rosselló and Rotger derive and discuss classical Sackin expectations as part of a broader study of tree-balance indices. Wu and Choi analyze the joint distribution of **cherries and pitchforks**; this is not a joint statement about cherry membership, leaf depth, and the Sackin sum. Coronado and coauthors study leaf-depth variation and a covariance between **Sackin and total cophenetic indices**, not the two-scale cherry-depth contrast. Plazzotta and coauthors empirically compare shape statistics in outbreak-branching models whose conditioning and reproduction mechanisms differ from fixed-size Yule leaf splitting.

Thus the sign contrast and the particular finite-size mixed-moment identities are not consequences explicitly supplied by these inspected results. The entire historical literature has not been exhausted, and the claim of originality is conditional on the documented source comparisons. In particular, an equivalent identity could be implicit in older multivariate tree generating functions.

## Limitations

The results concern discrete **topological** depth, not elapsed evolutionary time or time-weighted branch length. They do not apply automatically under a uniform-on-topologies model, conditioning on observed molecular data, non-Yule speciation rates, extinction, or incomplete sampling. The sign reversal is between two different probability spaces—a random leaf in a random tree versus a random whole-tree statistic—not a within-tree deterministic comparison. This work does not give the complete joint law of cherry count and Sackin index or an exact asymptotic correlation without additional variance analysis.

## References

1. A. Mir, F. Rosselló and L. Rotger, *A new balance index for phylogenetic trees*, arXiv:1202.1223v1, first public version 2012-02-06; later *Mathematical Biosciences* 241 (2013), 125–136.
2. A. McKenzie and M. Steel, *Distributions of cherries for two models of trees*, *Mathematical Biosciences* 164 (2000), 81–92. Accessible manuscript: https://ir.canterbury.ac.nz/server/api/core/bitstreams/246ff6f4-967f-4550-9f98-c4b3d671fe84/content .
3. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, arXiv:1508.03139v1 (2015); later *Theoretical Population Biology* 108 (2016), 13–23.
4. T. M. Coronado, A. Mir, F. Rosselló and L. Rotger, *On Sackin's original proposal: the variance of the leaves' depths as a phylogenetic balance index*, *BMC Bioinformatics* 21 (2020), 154; doi:10.1186/s12859-020-3405-1.
5. G. Plazzotta, C. Kwan, M. Boyd and C. Colijn, *Effects of memory on the shapes of simple outbreak trees*, *Scientific Reports* 6 (2016), 21159; doi:10.1038/srep21159.
