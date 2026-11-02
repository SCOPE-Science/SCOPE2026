# Sharp center-to-edge reversal of fixed-point marginals in finite Mallows permutations

## Finding

For an integer \(n\ge 2\), real \(q>0\), and a permutation \(\Pi\) sampled from the inversion-weighted Mallows distribution on \(S_n\), put
\[
p_{n,i}(q)=\Pr\{\Pi(i)=i\},\qquad 1\le i\le n.
\]
The fixed-point marginal profile is symmetric, \(p_{n,i}(q)=p_{n,n+1-i}(q)\). It satisfies the following **strict finite-sample center-to-edge law** for every integer \(1\le i<n/2\):
\[
\begin{array}{ll}
p_{n,i}(q)>p_{n,i+1}(q),&0<q<1,\\
p_{n,i}(q)=p_{n,i+1}(q)=1/n,&q=1,\\
p_{n,i}(q)<p_{n,i+1}(q),&q>1.
\end{array}
\]
When \(n\) is even, the two central positions have exactly equal marginals for every \(q\). Thus \(q=1\) is the sharp sign-reversal boundary for the entire positional profile.

An exact distributional explanation strengthens the comparison. For integers \(a,b\ge0\), define \([h]_q=1+q+\cdots+q^{h-1}\) for \(h\ge1\), \([0]_q!=1\), \([h]_q!=\prod_{r=1}^h[r]_q\), and the Gaussian binomial coefficient
\[
{h\brack j}_q=\frac{[h]_q!}{[j]_q![h-j]_q!}\qquad (0\le j\le h).
\]
Let \(J_{a,b}\) be the integer-valued random variable with distribution
\[
\Pr(J_{a,b}=j)
=\frac{q^{j^2}{a\brack j}_q{b\brack j}_q}{{a+b\brack a}_q},
\quad 0\le j\le \min(a,b).
\]
With \(a=i-1\) and \(b=n-i\), one has the **exact diagonal formula**
\[
\boxed{p_{n,i}(q)=\frac{\mathbb E\bigl[q^{2J_{a,b}}\bigr]}{[n]_q}.}
\]
Moreover, for any integers \(b\ge a+2\), balancing the two sides by one endpoint gives the strict monotone likelihood-ratio ordering
\[
J_{a,b}<_{\mathrm{lr}}J_{a+1,b-1}.
\]
The ordering means that the ratio of the two probability masses is strictly increasing on the smaller support, with an additional positive upper-support mass when applicable. It holds for every \(q>0\), including \(q=1\); the fixed-point reversal results from the monotonicity of \(j\mapsto q^{2j}\).

## Assumptions and scope

Use one-line permutation notation. The inversion count is
\[
\operatorname{inv}(\pi)=\#\{(u,v):1\le u<v\le n,\ \pi(u)>\pi(v)\}.
\]
The Mallows law is \(\Pr(\Pi=\pi)=q^{\operatorname{inv}(\pi)}/[n]_q!\) for \(q>0\), and every assertion is an exact finite-\(n\) statement. In particular, no limiting regime in \(n\), no assumption that \(q\) approaches one, and no stochastic independence of the fixed-point indicators is used. The normalization, formula, and inequalities include \(a=0\), \(b=0\), and \(q=1\) by their displayed definitions.

## Proof

**1. Deleting a forced fixed point.** Fix \(i\) and put \(a=i-1\), \(b=n-i\), \(m=a+b=n-1\). A permutation with \(\pi(i)=i\) is in bijection with \(\sigma\in S_m\) after deleting position \(i\), deleting value \(i\), and standardizing remaining positions and values. Let \(J\) be the number of values larger than \(i\) in the first \(a\) positions; equivalently, it is the number of values smaller than \(i\) in the last \(b\) positions. Each such value contributes exactly one inversion with the fixed value \(i\) on its side, so
\[
\operatorname{inv}(\pi)=\operatorname{inv}(\sigma)+2J.
\]
The projection of \(\sigma\) has Mallows inversion weight \(q^{\operatorname{inv}(\sigma)}\).

**2. Exact cut-crossing distribution.** Partition the standardized values into the \(a\) smaller and \(b\) larger labels, and record which \(a\) values occupy the left block. If exactly \(j\) larger labels lie to the left, exactly \(j\) smaller labels must lie to the right. The number of left-greater-than-right pairs contributed by this cross-type mismatch is \(j^2\). Inversions among the smaller labels across the cut have generating polynomial \({a\brack j}_q\), and the corresponding inversions among larger labels have generating polynomial \({b\brack j}_q\). Finally, arbitrary orderings internal to the two position blocks independently contribute factors \([a]_q!\) and \([b]_q!\). Thus the total inversion weight with this cut-crossing count is
\[
[a]_q![b]_q!\,q^{j^2}{a\brack j}_q{b\brack j}_q.
\]
Summing over \(j\) gives the standard Gaussian-binomial Vandermonde decomposition
\[
\sum_{j=0}^{\min(a,b)}q^{j^2}{a\brack j}_q{b\brack j}_q={a+b\brack a}_q.
\]
This identity also follows directly by summing all subsets of \(a\) values with their cross-inversion weights. Dividing by \([m]_q!\) gives precisely the law of \(J_{a,b}\). Since adding the forced fixed point multiplies its weight by \(q^{2J}\), while \([n]_q!=[n]_q[m]_q!\),
\[
p_{n,i}(q)=\frac{[m]_q!\,\mathbb E(q^{2J_{a,b}})}{[n]_q!}
=\frac{\mathbb E(q^{2J_{a,b}})}{[n]_q}.
\]
Equivalently, its unnormalized numerator is
\[
\sum_{\pi:\,\pi(i)=i}q^{\operatorname{inv}(\pi)}
=[a]_q![b]_q!\sum_{j=0}^{\min(a,b)}q^{j(j+2)}{a\brack j}_q{b\brack j}_q.
\]

**3. Strict likelihood-ratio balancing.** Suppose \(b\ge a+2\). On the old support \(j=0,\ldots,a\), the ratio of new to old unnormalized masses is
\[
\frac{{a+1\brack j}_q{b-1\brack j}_q}{{a\brack j}_q{b\brack j}_q}
=\frac{[a+1]_q}{[b]_q}\frac{[b-j]_q}{[a+1-j]_q}.
\]
Set \(d=b-a-1\ge1\), \(t=a+1-j\ge1\). Its variable factor becomes
\[
\frac{[t+d]_q}{[t]_q}=1+\frac{q^t[d]_q}{[t]_q}.
\]
For every \(t\ge1\), \([t+1]_q=1+q[t]_q\), hence
\[
\frac{q^{t+1}}{[t+1]_q}<\frac{q^t}{[t]_q}.
\]
Therefore the ratio of new to old masses strictly increases as \(j\) increases. The new law also has positive mass at \(j=a+1\), since \(b-1\ge a+1\). The normalization factors do not alter the ordering. In particular \(J_{a+1,b-1}\) strictly stochastically dominates \(J_{a,b}\), and its expectation of every strictly increasing function is strictly larger.

For adjacent positions \(i\) and \(i+1\) on the left half, \(a=i-1\), \(b=n-i\) satisfy \(b\ge a+2\). If \(q>1\), the function \(j\mapsto q^{2j}\) is strictly increasing, whereas for \(0<q<1\) it is strictly decreasing; the diagonal formula yields the respective strict comparisons. For \(q=1\) it is constant, so \(p_{n,i}(1)=1/n\). Simultaneous reversal of both positions and values, \(\pi\mapsto r\circ\pi\circ r\) for \(r(s)=n+1-s\), preserves inversion number and maps fixed point \(i\) to fixed point \(n+1-i\). This gives symmetry and the even-center equality. The proof covers every asserted parameter value.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only Python's standard library and exact integer or rational arithmetic. Its independently enumerated checks match the closed polynomial numerator for all permutations through \(n=8\), verify the positional symmetry and signs at seven positive rational values of \(q\) through \(n=18\), verify the binary-cut Gaussian hypergeometric distribution through nine remaining labels, and test all adjacent likelihood-ratio minors over a separate parameter grid. Execution returned `PASS 8885 exact assertions`. These finite tests are reproducibility checks; the preceding argument, rather than the finite grid, establishes the theorem for every integer \(n\ge2\) and every real \(q>0\).

For orientation, at \(n=5\) and \(q=1/2\) the ordered marginals are \((16/31,52/155,47/155,52/155,16/31)\); at \(q=2\) they are \((1/31,19/155,47/155,19/155,1/31)\).

## Relationship to prior work

Diaconis, Evans, and Graham (2013 public technical report) study fixed points and unseparated pairs of *uniform* permutations. Bhatnagar and Peled (2013 preprint) develop Mallows inversion weights and displacement bounds, but those bounds do not compare fixed-point marginals at neighboring positions. Mukherjee (2015 preprint) studies fixed-point and cycle-count limits through permuton densities; its asymptotic statements do not supply the exact finite-position inequalities. He, Müller, and Verstraaten (2022 preprint) give Mallows cycle-count limits and reversal symmetries but not the present strict positional comparison. Standard Gaussian-binomial and \(q\)-Vandermonde identities underlie the proof and are not claimed as new. The assessed contribution is the exact cut-crossing representation combined with strict cross-position likelihood-ratio balancing and the resulting sharp finite-\(n\) sign reversal. A comprehensive historical-priority determination for all older \(q\)-enumeration or one-point-marginal results remains open.

## Limitations

The conclusion concerns the individual diagonal marginals \(\Pr(\Pi(i)=i)\); it does not assert joint independence, ordering of entire fixed-point sets, or a corresponding law for other permutation distances. No asymptotic approximation or monotonicity in \(q\) is claimed. The likelihood-ratio ordering is for the auxiliary cut-crossing statistic, not a likelihood-ratio comparison between Bernoulli fixed-point indicators. Mathematical novelty is assessed against the inspected literature, not independently certified against every possible historical source.

## References

1. P. Diaconis, S. N. Evans, and R. Graham, *Unseparated pairs and fixed points in random permutations*, University of California, Berkeley, Statistics Technical Report 822, first public date August 1, 2013. https://statistics.berkeley.edu/tech-reports/822
2. N. Bhatnagar and R. Peled, *Lengths of Monotone Subsequences in a Mallows Permutation*, preprint posted June 16, 2013, arXiv:1306.3674. https://arxiv.org/abs/1306.3674
3. S. Mukherjee, *Fixed points and cycle structure of random permutations*, preprint posted September 15, 2015, arXiv:1509.04552. https://arxiv.org/abs/1509.04552
4. J. He, T. Müller, and T. Verstraaten, *Cycles in Mallows random permutations*, preprint posted January 27, 2022, arXiv:2201.11610. https://arxiv.org/abs/2201.11610
