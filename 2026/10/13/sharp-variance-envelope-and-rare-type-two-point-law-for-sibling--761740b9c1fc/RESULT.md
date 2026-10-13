# Sharp variance envelope and rare-type two-point law for sibling coupon deficits

## Finding

Fix an integer \(N\ge 2\). For a probability vector \(p\) in the **open** \(N\)-simplex, let \(U_j^N\) be the number of coupon types missing from the album of sibling \(j\) when the first collector finishes, as defined below. The following sharp asymptotic optimization holds:

\[
\lim_{j\to\infty}\sup_{p_i>0,\,\sum_{i=1}^N p_i=1}
\operatorname{Var}_p(U_j^N)=\frac{(N-1)^2}4.
\]

For every fixed \(c>0\), the positive triangular-array probabilities

\[
p_N^{(j)}=\frac cj,\qquad
p_i^{(j)}=\frac{1-c/j}{N-1}\quad(1\le i<N,\ j>c)
\]

produce the exact two-point weak limit

\[
U_j^N\  \Longrightarrow
\begin{cases}
1,&\text{with probability }e^{-c(N-1)},\\
N,&\text{with probability }1-e^{-c(N-1)}.
\end{cases}
\]

In particular the limiting variance is \((N-1)^2e^{-c(N-1)}(1-e^{-c(N-1)})\), and \(c=\log(2)/(N-1)\) realizes half of the limiting mass at each extreme. In contrast, the uniform vector has variance tending to zero as the sibling index increases. The sharp variance envelope is therefore asymptotically opposite to the established uniform maximization of the **mean** deficit.

An exact finite illustration is \(N=j=3\): with probabilities \((1/3,1/3,1/3)\), the variance is \(707/1296\); with \((4/9,4/9,1/9)\), it is \(416326091/590490000\). Their positive difference is \(5887451/36905625\).

## Assumptions and scope

Let \((Z_t)_{t\ge1}\) be independent random variables taking values in \(\{1,\dots,N\}\), with \(\mathbb P(Z_t=i)=p_i>0\) and \(\sum_i p_i=1\). Define

\[
T_N=\min\{t\ge1:\text{every coupon type appears among }Z_1,\ldots,Z_t\},
\]

and write \(C_i(T_N)=\sum_{t=1}^{T_N}\mathbf1_{\{Z_t=i\}}\). For every integer \(j\ge2\), define \(U_j^N=\sum_{i=1}^N\mathbf1_{\{C_i(T_N)<j\}}\). These definitions coincide with the sequential duplicate-passing sibling model of Doumas and Spektor [1]. The fixed positive integer \(N\) does not grow; the variable \(j\) does. The optimizing probabilities may depend on \(j\). All limits are over integers \(j\to\infty\); no limiting assertion concerns a fixed \(j\) with \(N\to\infty\).

## Proof

**1. Universal sharp upper bound.** Exactly one type occurs for its first time on the last draw \(T_N\), hence that type has count one at completion. Therefore \(1\le U_j^N\le N\) almost surely for every \(j\ge2\). For any random \(W\in[1,N]\), nonnegativity of \((W-1)(N-W)\) gives

\[
\operatorname{Var}(W)\le (\mathbb EW-1)(N-\mathbb EW)
\le\frac{(N-1)^2}4.
\]

The bound applies to the supremum over every positive vector and every sibling index.

**2. Rare-type waiting time.** Fix \(c>0\) and set \(p_N=c/j\), \(p_i=(1-c/j)/(N-1)\) for the remaining types, with \(j>c\). Let \(G_j=\min\{t\ge1:Z_t=N\}\). Then \(G_j\) is geometric with success probability \(c/j\), and for every \(x\ge0\),

\[
\mathbb P(G_j/j>x)=(1-c/j)^{\lfloor jx\rfloor}
\longrightarrow e^{-cx}.
\]

Thus \(G_j/j\Rightarrow E_c\), where \(E_c\) is exponential of rate \(c\). In particular \(\mathbb EG_j=j/c\).

**3. Simultaneous occupancy concentrations.** Let \(B_{i,j}=\sum_{t=1}^{G_j-1}\mathbf1_{\{Z_t=i\}}\) for \(i<N\). Conditional on \(G_j\), these counts have the multinomial distribution with \(G_j-1\) trials and equally likely categories \(1,\ldots,N-1\). In particular, writing \(q=1/(N-1)\),

\[
\mathbb E\left[\left(\frac{B_{i,j}-q(G_j-1)}j\right)^2\right]
=\frac{q(1-q)\mathbb E(G_j-1)}{j^2}
\le\frac{1}{cj},
\]

where the \(N=2\) case has zero conditional variance. A union bound over the fixed \(N-1\) categories and the convergence of \(G_j/j\) prove joint convergence

\[
\left(\frac{B_{1,j}}j,\ldots,\frac{B_{N-1,j}}j\right)
\Rightarrow\left(\frac{E_c}{N-1},\ldots,\frac{E_c}{N-1}\right).
\]

Since \(E_c>0\) almost surely, \(\mathbb P(\min_{i<N}B_{i,j}=0)\to0\): for example compare \(\min B_{i,j}/j\) with an arbitrarily small positive constant, then let that constant decrease to zero. If every common type has appeared before the first rare type, the collection finishes **at** \(G_j\), so

\[
\mathbb P(T_N=G_j)\longrightarrow1.
\]

**4. Deficit limit.** On \(T_N=G_j\), rare type \(N\) has count exactly one and is missing from the \(j\)-th album. The other \(N-1\) counts are \(B_{i,j}\). Their limiting normalized value is the same continuous random variable \(E_c/(N-1)\), which has no atom at one. The continuous mapping theorem for the indicators of the strict inequalities gives

\[
U_j^N\Rightarrow 1+(N-1)\mathbf1_{\{E_c<N-1\}}.
\]

As \(\mathbb P(E_c>N-1)=e^{-c(N-1)}\), this has exactly the two probabilities stated in the finding. Because \(U_j^N\) stays in the fixed finite set \(\{1,\ldots,N\}\), convergence in distribution implies convergence of its first two moments. Its variance therefore converges to \((N-1)^2e^{-c(N-1)}(1-e^{-c(N-1)})\).

**5. Exact extremum.** For \(c=\log(2)/(N-1)\), the parameter \(e^{-c(N-1)}\) equals \(1/2\); the limiting variance equals \((N-1)^2/4\). The universal bound from Step 1 sandwiches the optimizing supremum and proves its exact limit. No finite-\(j\) global maximizer is asserted.

**6. Contrast with fixed uniform probabilities.** On a single infinite iid sequence with uniform type probabilities, \(T_N<\infty\) almost surely, and every count \(C_i(T_N)\) is finite. Consequently \(U_j^N=N\) for every sufficiently large \(j\), almost surely. Bounded convergence proves \(\operatorname{Var}_{\mathrm{uniform}}(U_j^N)\to0\). The same conclusion holds for any *fixed* strictly positive vector; the rare-type construction succeeds only because its probabilities change with \(j\).

**7. Exact finite comparison.** Cap individual occupancy counts at \(j\), and stop once all are positive. For every nonabsorbing capped count vector \(s\), the distribution of the final deficit satisfies

\[
F(s)=\frac{\sum_{i:s_i<j}p_i F(s+e_i)}{\sum_{i:s_i<j}p_i}.
\]

Here each \(F(s)\) denotes a probability-mass vector indexed by possible deficits, and an absorbing \(s\) has a point mass at \(\#\{i:s_i<j\}\). This formula eliminates self-loops arising when an already-capped type is drawn. Backward finite recursion with exact rational probabilities gives the two distributions and variances above; see `checker.py`.

## Verification

The analytical argument independently establishes all infinite statements. The accompanying standard-library Python program `checker.py` recomputes finite stopped-occupancy laws using `fractions.Fraction`, including all terminal probabilities, means, variances, their strictly positive difference, and a separate two-type case. Execute with `python checker.py`. The exact finite outputs are \(707/1296\), \(416326091/590490000\), and their difference \(5887451/36905625\); no floating-point approximation is used in any asserted inequality.

## Relationship to prior work

Doumas and Spektor [1] prove uniform maximization of \(\mathbb E U_j^N\), for each finite \(N,j\). Their seven-page primary article, including its result statements, variance-comparison remark, and reference list, does **not** assert an extremum for the variance of the sibling deficit. The variance problem described in its Remark 2 and treated by Long [5] instead concerns the collection **completion time**, a different random variable. Long [2] studies expectation extremality and a limit in which the **number of coupon types** tends to infinity while sibling indices remain fixed; that is not the present fixed-\(N\), growing-\(j\) regime. Long's [3] full probability-generating-function and binomial-moment inequalities establish stronger *moment-order* comparisons at each fixed \(N,j\), but variance subtracts the square of the mean and is not determined by that order. Our exact finite variance reversal is compatible with those inequalities. The older introduction of the model [4] principally analyzes asymptotics of mean deficits with growing \(N\). The newly proved optimization is a sharp variance statement about a different scaling regime; no novelty is claimed for the underlying coupon model, the expectation extremality, or elementary range-variance and geometric-limit tools.

## Limitations

The theorem gives the limiting supremum as sibling index \(j\) grows for each fixed \(N\), not the exact finite-\(j\) maximizers or their rates. The maximizing sequence is in the open probability simplex for all sufficiently large \(j\), but no global finite-\(j\) attainment is claimed. The result does not address simultaneous growth of \(N\) and \(j\). A full-text priority comparison with [2] and [3] remains limited by accessibility; their publicly available detailed abstracts and summaries describe a different asymptotic regime and transform order, respectively, but cannot exclude an unindexed variance corollary. Independent external scientific validation has not been performed.

## References

[1] A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, arXiv:2606.21591v1, first publicly posted 19 June 2026. Full primary text: https://pdfs.assets.alphaxiv.org/2606.21591v1.pdf .

[2] C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635v1 (28 June 2026), https://arxiv.org/abs/2606.29635 .

[3] C. D. Long, *Radial Transform Extremality for the Siblings of the Coupon Collector*, arXiv:2606.31391v1 (30 June 2026), https://arxiv.org/abs/2606.31391 .

[4] A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, arXiv:1412.4346v1 (2014), https://arxiv.org/abs/1412.4346 .

[5] C. D. Long, *Terminal Defects, Growing Multiplicity, and Variance Extremality in the Double Dixie Cup Problem*, arXiv:2604.25108 (2026), https://arxiv.org/abs/2604.25108 .
