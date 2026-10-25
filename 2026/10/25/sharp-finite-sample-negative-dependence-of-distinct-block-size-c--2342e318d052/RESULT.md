# Sharp finite-sample negative dependence of distinct block-size counts in noncrossing partitions

## Finding

Let \(\pi\) be uniformly distributed over all noncrossing partitions of \([n]\). Let \(B_j\) count blocks of size \(j\). For every integer \(n\ge2\) and all distinct \(a,b\in\{1,\ldots,n\}\),

\[
\operatorname{Cov}(B_a,B_b)<0.
\]

A sharp quantitative bound holds for \(n\ge3\):

\[
\frac{\mathbb E[B_aB_b]}{\mathbb E B_a\,\mathbb E B_b}
\le \frac{(n-1)(2n-1)}{(n+1)(2n-3)}<1.
\]

The first inequality is an equality for distinct sizes exactly when \(\{a,b\}=\{1,2\}\). Equivalently,

\[
-\operatorname{Cov}(B_a,B_b)\ge
\frac{2(n-2)}{(n+1)(2n-3)}\,\mathbb E B_a\,\mathbb E B_b,
\]

with the same equality characterization. The sharp bound applies uniformly over *all* distinct block sizes, including sizes that grow with \(n\), and strengthens previously established fixed-size asymptotic negative covariance.

## Assumptions and scope

For \(n\ge2\), a partition of \([n]=\{1,\ldots,n\}\) is noncrossing when it has no four indices \(i<j<k<l\) such that \(i,k\) lie in one block and \(j,l\) in a different block. The law is uniform over the \(C_n=\binom{2n}{n}/(n+1)\) noncrossing partitions. For every \(1\le j\le n\), \(B_j(\pi)\) counts its size-\(j\) blocks. The theorem concerns distinct \(a\ne b\); it makes no negative-variance claim when \(a=b\).

For integers \(1\le j\le n\), write

\[
A_j=\binom{2n-j-1}{n-j}>0.
\]

For distinct \(a,b\), define the number of ordered pairs of *distinguished, differently sized* blocks across all noncrossing partitions:

\[
M_{a,b}=\begin{cases}
 n\binom{2n-a-b-2}{n-a-b},&a+b\le n,\\
 0,&a+b>n.
\end{cases}
\]

## Proof

**1. Exact mixed moments.** The first-moment block count \(A_j\) is classical; see Bergerson and coauthors (2011), Theorem 1. An independent generating-function calculation supplies both moment formulas. Let \(F(z;u,v)\) enumerate noncrossing partitions, where \(u\) and \(v\) mark the numbers of blocks of distinct sizes \(a\) and \(b\). Root-block decomposition gives

\[
F(z;u,v)=\frac{1}{1-zF(z;u,v)}+(u-1)(zF)^a+(v-1)(zF)^b.
\]

With \(G=zF\) and \(\Phi(w)=1/(1-w)+(u-1)w^a+(v-1)w^b\), we have \(G=z\Phi(G)\). Lagrange inversion yields

\[
[z^n]F(z;u,v)=\frac1{n+1}[w^n]\Phi(w)^{n+1}.
\]

Differentiation once at \(u=v=1\) yields \(A_a\) and \(A_b\); differentiation once with respect to each variable yields, for \(a+b\le n\),

\[
\sum_{\pi}B_a(\pi)B_b(\pi)
=n[w^{n-a-b}](1-w)^{-(n-1)}
=n\binom{2n-a-b-2}{n-a-b}=M_{a,b}.
\]

When \(a+b>n\), no partition can contain both types of blocks, so the mixed count is zero. Consequently

\[
\mathbb E B_j=A_j/C_n,\qquad
\mathbb E B_aB_b=M_{a,b}/C_n.
\]

**2. A uniform bound through exact neighboring-size ratios.** For the following algebraic comparison only, extend the formula for \(M_{a,b}\) to \(a=b\) using the same binomial expression; at equal indices it counts ordered *distinct* blocks and hence the factorial moment, not \(\mathbb E[B_a^2]\). When \(a+b\le n\), set

\[
R_n(a,b)=\frac{C_n M_{a,b}}{A_aA_b}.
\]

This is positive. If \(a+b+1\le n\), elementary cancellation of factorials gives

\[
\frac{R_n(a+1,b)}{R_n(a,b)}
=\frac{(n-a-b)(2n-a-1)}{(2n-a-b-2)(n-a)}.
\]

All denominators are positive in the stated range. The numerator minus the denominator of the last displayed fraction is precisely

\[
n-b(n-1)-a\le0,
\]

for all integers \(n\ge3\) and \(a,b\ge1\). Equality occurs precisely at \(a=b=1\). Interchanging \(a\) and \(b\) gives the same result for the other coordinate. Hence every ratio \(R_n(a,b)\) on the triangular region \(a,b\ge1\), \(a+b\le n\) is at most \(R_n(1,1)\), and a distinct-size pair attains this upper bound exactly at \(\{a,b\}=\{1,2\}\). Direct factorial cancellation gives

\[
R_n(1,1)=\frac{(n-1)(2n-1)}{(n+1)(2n-3)}.
\]

For \(n\ge3\), the denominator exceeds the numerator by \(2(n-2)>0\). Thus \(R_n(a,b)<1\), proving strict negative covariance and the sharp upper bound when \(a+b\le n\).

**3. Disjoint-size boundary.** If \(a+b>n\), then \(M_{a,b}=0\), while \(A_a,A_b>0\); hence \(\operatorname{Cov}(B_a,B_b)=-A_aA_b/C_n^2<0\) and the ratio is zero. The only distinct-size pair at \(n=2\) is \(\{a,b\}=\{1,2\}\), which belongs to this case. This covers all boundary conditions. Subtracting the bound from one gives the stated sharp covariance deficit.

## Verification

Run the standalone `verify.py` with Python 3; it requires only the standard library. It checks the exact mixed-count formula and negative covariance by independent complete enumeration of Dyck paths through semilength ten (the maximal down-run lengths correspond to block sizes). It also checks the ratio inequalities and sharp equality cases algebraically over finite test ranges. The command output is `VERIFY_OK 50619 exact assertions; 23712 Dyck paths`. The unrestricted result is established by the preceding symbolic proof, not by the finite tests.

## Relationship to prior work

Bergerson, Miller, Pliml, Reiner, Shearer, Stanton and Switala (2011, Theorem 1) already give the exact enumeration of noncrossing partitions with one distinguished block, also refined by total block count. These first moments and refinements are **prior results**, not claimed as new here. Kargin (arXiv:1907.00632v1, 2019, Theorem 2.4) establishes the negative leading-order covariance of counts of two distinct fixed block sizes as \(n\to\infty\). The contribution assessed here is an all-finite-sizes, all-pairs **strict** sign theorem with a sharp common multiplicative bound, including growing block sizes and the equality cases. The proof uses a two-variable marking argument and monotonicity of a normalized mixed-moment ratio, not just the fixed-size asymptotic.

## Limitations

This establishes pairwise covariance signs and a sharp moment ratio, **not** full negative association of the entire random vector of block counts, nor stochastic domination under arbitrary joint conditioning. The all-size inequality is strict for distinct indices, but covariance magnitudes depend on the sizes and may be small for rare large blocks. The exact mixed counts are algebraic consequences of standard noncrossing-partition generating functions; the bounded-ratio interpretation might be implicit in older sources. Historical priority beyond the inspected literature is not independently established.

## References

1. V. Kargin, *Limit theorems for statistics of non-crossing partitions*, arXiv:1907.00632v1 (first posted 2019-07-01), Theorem 2.4 and its generating-function proof. https://arxiv.org/abs/1907.00632
2. M. Bergerson, A. Miller, A. Pliml, V. Reiner, P. Shearer, D. Stanton and N. Switala, *Note on 1-Crossing Partitions*, Ars Combinatoria 99 (2011), 83–87, Theorem 1. https://combinatorialpress.com/article/ars/Volume%2099/volume-99-paper-9.pdf
3. O. Arizmendi, *Statistics of blocks in k-divisible non-crossing partitions*, arXiv:1201.6576 (2012), block-count refinements. https://arxiv.org/abs/1201.6576
