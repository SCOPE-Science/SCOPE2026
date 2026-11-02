# Two age thresholds for degree–leaf dependence in random recursive trees

## Finding

In a uniform random recursive tree on vertices \(1,\ldots,n\), let \(L_n\) be its number of leaves, and let \(D_{v,n}\) count children of the vertex born at time \(v\). For every \(n\ge3\), every \(1\le v<j\le n\) with \(j\ge3\), and the attachment indicator \(A_{v,j}=\mathbf1\{P_j=v\}\), the **exact arrival-time cross-covariance** is
\[
\operatorname{Cov}(A_{v,j},L_n)=\frac{j-2v}{2(n-1)(j-2)}.
\tag{1}
\]
Thus, for each nonroot parent, an attachment before \(j=2v\) is negatively correlated with the final leaf count; one after \(j=2v\) is positively correlated, and the attachment at \(j=2v\), when present, is exactly uncorrelated. The root \(v=1\) is exceptional: all its nondeterministic attachments contribute positively and equally.

Summing over arrivals yields, for \(2\le v\le n\),
\[
\boxed{\operatorname{Cov}(D_{v,n},L_n)
 =\frac{n-v}{2(n-1)}
 -\frac{v-1}{n-1}\bigl(H_{n-2}-H_{v-2}\bigr)},
\tag{2}
\]
where \(H_m=\sum_{k=1}^m k^{-1}\), \(H_0=0\). In addition, \(\operatorname{Cov}(D_{1,n},L_n)=(n-2)/(2(n-1))\).

The second threshold is at the **age of the parent**. When \(3\le n\le6\), the covariance in (2) is strictly negative for all \(2\le v<n\). For \(n\ge7\), it has exactly one transition from positive to negative as \(v\) increases through \(2,\ldots,n-1\), allowing a zero at the threshold; \(D_{n,n}=0\) is deterministic. More quantitatively, if \(v_n/n\to\alpha\in(0,1)\), then
\[
\operatorname{Cov}(D_{v_n,n},L_n)\longrightarrow
 \Phi(\alpha):=\frac{1-\alpha}{2}+\alpha\log\alpha.
\tag{3}
\]
The function \(\Phi\) has a unique zero in \((0,1)\),
\[
\alpha_*=0.2846681370408\ldots.
\tag{4}
\]
In the large-tree limit, vertices born before approximately \(28.47\%\) of the growth process have positively correlated outdegree and total leaf count; those born later, but at a fixed fraction short of the final time, have negatively correlated outdegree and total leaf count. For every fixed label \(v\), the covariance tends to \(1/2\).

## Assumptions and scope

The standard uniform random recursive tree is constructed with root label \(1\) and independent parent choices
\[
P_j\sim\operatorname{Unif}\{1,\ldots,j-1\},\qquad j=2,\ldots,n.
\]
The outdegree \(D_{v,n}=\sum_{j=v+1}^n\mathbf1\{P_j=v\}\) counts children. The leaf count is
\[
L_n=\sum_{i=2}^nY_i,\quad
Y_i=\mathbf1\{P_k\ne i\text{ for every }k=i+1,\ldots,n\}.
\]
The root is not counted as a leaf for \(n\ge2\). Equations (1)–(2) hold for every admissible finite integer, not merely asymptotically. At \(j=2\) the attachment to the root is certain and has zero covariance; it is excluded from (1), whose denominator would vanish there.

## Proof

**1. Leaf probabilities and a pairwise cross-covariance.** Independence of the parent choices and telescoping give
\[
\mathbb EY_i=\prod_{k=i+1}^n\left(1-\frac1{k-1}\right)=\frac{i-1}{n-1}.
\tag{5}
\]
If \(i\ge j\), then \(A_{v,j}\) and \(Y_i\) depend on disjoint parent-choice times, so their covariance vanishes. For \(2\le i<j\) and \(i\ne v\), forcing \(P_j=v\) prevents \(P_j=i\), which would otherwise destroy leaf \(i\); hence
\[
\operatorname{Cov}(A_{v,j},Y_i)
=\frac{i-1}{(n-1)(j-1)(j-2)}.
\tag{6}
\]
For \(i=v\ge2\), the two indicators cannot both equal one, so
\[
\operatorname{Cov}(A_{v,j},Y_v)
=-\frac{v-1}{(n-1)(j-1)}.
\tag{7}
\]
The root has no indicator \(Y_1\). These calculations require no exchangeability between different birth labels.

**2. Exact local law.** Summing (6) over \(2\le i<j\), omitting \(i=v\) when \(v\ge2\), and adding (7), we find
\[
\begin{aligned}
\operatorname{Cov}(A_{v,j},L_n)
&=\frac{1}{2(n-1)}-\frac{v-1}{(n-1)(j-2)}\\
&=\frac{j-2v}{2(n-1)(j-2)}.
\end{aligned}
\]
This is (1), including \(v=1\) where the subtracted term vanishes. Its sign is that of \(j-2v\), proving the first threshold, with strict inequalities whenever the indicated attachment probability lies strictly between zero and one.

**3. Degree–leaf covariance and finite age threshold.** For \(v\ge2\), summing the local law over \(j=v+1,\ldots,n\) gives
\[
\begin{aligned}
\operatorname{Cov}(D_{v,n},L_n)
&=\frac{1}{2(n-1)}\sum_{j=v+1}^n
\left(1-\frac{2(v-1)}{j-2}\right)\\
&=\frac{n-v}{2(n-1)}-\frac{v-1}{n-1}\sum_{k=v-1}^{n-2}\frac1k,
\end{aligned}
\]
which is (2). For \(v=1\), the forced first attachment \(P_2=1\) contributes zero; the remaining \(n-2\) contributions are \(1/[2(n-1)]\).

Put \(F_n(v)=(n-1)\operatorname{Cov}(D_{v,n},L_n)\) for \(2\le v\le n\). Formula (2) yields
\[
F_n(v+1)-F_n(v)=\frac12-\sum_{k=v}^{n-2}\frac1k,
\qquad 2\le v<n.
\tag{8}
\]
These increments are strictly increasing in \(v\), so \(F_n\) is strictly discretely convex. Moreover,
\[
F_n(2)=\frac{n-2}{2}-H_{n-2},\quad
F_n(n-1)=-\frac12,\quad F_n(n)=0.
\tag{9}
\]
The first value is negative for \(n\le6\) and positive for \(n\ge7\), as follows from monotone increments \(1/2-1/(n-1)\) as \(n\) grows and the adjacent evaluations at \(n=6,7\). Since a convex sequence lies below the chord joining its endpoints, all \(2\le v\le n-1\) have negative covariance for \(n\le6\). For \(n\ge7\), the positive first value and negative penultimate value, together with the increasing increments and negative endpoint, force a unique positive-to-negative crossing, possibly with a zero at a single label. (Once its increment turns positive, all later increments increase; before then the sequence decreases.)

**4. Asymptotic age cutoff.** For \(v_n/n\to\alpha\in(0,1)\), harmonic sums satisfy
\[
H_{n-2}-H_{v_n-2}=\log(n/v_n)+o(1).
\]
Substitution into (2) gives (3). The derivative and second derivative are
\[
\Phi'(\alpha)=\frac12+\log\alpha,
\qquad \Phi''(\alpha)=\frac1\alpha>0.
\]
The function starts at \(\Phi(0+)=1/2\), falls below zero (for example \(\Phi(1/2)<0\)), and approaches \(\Phi(1)=0\) from below. It therefore has exactly one interior zero, numerically (4). For fixed \(v\ge2\), the negative term in (2) is \(O_v((\log n)/n)\), hence the claimed limit \(1/2\); the root limit follows directly.

Finally, \(\sum_{v=1}^nD_{v,n}=n-1\) deterministically. Hence
\[
\sum_{v=1}^n\operatorname{Cov}(D_{v,n},L_n)=0,
\tag{10}
\]
providing a consistency identity: positive correlations of early vertex degrees must be compensated by negative correlations later.

## Verification

Run the standalone Python 3 script `verify.py` without external dependencies. It enumerates every recursive tree on \(n=3,\ldots,9\) vertices, reconstructs every child count and leaf indicator, and compares the exact joint statistics against (1)–(2) using rational arithmetic. It also checks the finite sign classification for \(3\le n\le200\) and numerical convergence of (3). The checker passed 374 grouped exact and numerical assertions. The derivation above, rather than the finite enumeration, establishes the universal result.

## Relationship to prior work

Janson's study of random recursive tree degree distributions gives asymptotic covariances among **numbers of vertices of prescribed outdegree** (global degree counts), and not the mixed covariance of the outdegree of a **fixed birth-label vertex** with the total number of leaves. Bryc, Minda, and Sethuraman supply the Markov-chain theory of the **global leaf count**, including large deviations, but do not condition on the parent identity at a specified birth time. The previously published *Equal-share covariance of root degree and leaves in a random recursive tree* proves the \(v=1\) special case, where the root cannot be a leaf and every nontrivial arrival contributes equally. Equations (1)–(4) add the nonroot self-leaf loss, two exact sign transitions, and the interior macroscopic birth-time cutoff. They are not consequences of the root-only identity without a new computation.

## Limitations

These formulas are specific to independent uniform parent choices and do not cover preferential attachment or plane-oriented recursive trees. They are second-order mixed-moment identities; they do not establish association of all increasing transformations or a joint distribution of degree and leaf count. The 1991 work by Mahmoud and Smythe on the leaves of subtrees rooted at given labels is a plausible neighboring source but was not fully inspectable here; an implicit equivalent mixed moment in older work remains an originality risk. Full text of Janson's 2004 publication was also not accessible; its published abstract establishes global degree-count scope but cannot rule out unadvertised individual mixed moments. No independent audit has been performed.

## References

1. S. Janson, “Asymptotic degree distribution in random recursive trees,” *Random Structures & Algorithms* 26 (2005), 69–83; first publicly available November 16, 2004; DOI: https://doi.org/10.1002/rsa.20046.
2. W. Bryc, D. Minda, and S. Sethuraman, “Large deviations for the leaves in some random trees,” arXiv:0809.4741, first submitted September 27, 2008, https://arxiv.org/abs/0809.4741.
3. “Equal-share covariance of root degree and leaves in a random recursive tree,” publicly available research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f.
4. H. M. Mahmoud and R. T. Smythe, “On the distribution of leaves in rooted subtrees of recursive trees,” *Annals of Applied Probability* 1 (1991), 406–418, DOI: https://doi.org/10.1214/aoap/1177005874.
