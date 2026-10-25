# Exact component–singleton covariance in site-percolated recursive trees

## Finding

Let \(T_n\) be a uniformly random recursive tree on \(\{1,\ldots,n\}\), \(n\ge 1\), constructed by attaching each new vertex independently to a uniformly random earlier vertex. Independently retain every vertex with probability \(p\in(0,1)\). Denote by \(K_n\) the number of connected components of the induced forest on retained vertices and by \(I_n\) the number of its singleton components (components containing one retained vertex). Write \(q=1-p\) and define
\[
\begin{aligned}
h_n&=\prod_{j=1}^{n-1}\left(1-\frac{p}{j}\right),\\
s_n&=\sum_{j=1}^{n-1}\frac1{j-p},\qquad
 t_n=\sum_{j=1}^{n-1}\frac1{(j-p)^2},\\
b&=\frac{2p^2}{1+p},\qquad b'=\frac{2p(p+2)}{(1+p)^2},\\
c&=\frac{p(1-p)(2p^4+5p^3+3p^2-p+1)}{(1+p)^3}.
\end{aligned}
\]
Empty products and sums equal one and zero, respectively. For **every** \(n\ge1\) and \(p\in(0,1)\), the following exact identity holds:
\[
\boxed{
\operatorname{Cov}(K_n,I_n)=cn-2p^2q+h_n\left[pq(1+2p)-c+p^2q\left((b-b')s_n+\frac b2(s_n^2-t_n)\right)\right].
}
\]
Consequently, for every fixed \(p\in(0,1)\),
\[
\boxed{
\operatorname{Cov}(K_n,I_n)
=cn-2p^2(1-p)+O_p\bigl(n^{-p}(\log n)^2\bigr)
}
\]
with \(c>0\). In particular the covariance is eventually strictly positive and has a positive linear growth rate. At \(p=1/2\), that rate is exactly \(4/27\). No finite-size all-\(n\) sign theorem or joint central limit theorem is claimed.

## Assumptions and scope

All random tree attachment choices are mutually independent and independent of the identically distributed Bernoulli retention indicators. The model is *independent site percolation* on the uniformly random recursive tree, not a process conditioned to retain an exact number of vertices. The empty induced forest has zero components and zero singleton components. The number of vertices \(n\) is any integer at least one; the parameter \(p\) is fixed strictly between zero and one for the asymptotic formula.

## Proof

**1. Growth transitions.** Let \(M_n\) be the number of retained vertices. On adding vertex \(n+1\), a uniformly selected existing parent is attached, and the new vertex is independently retained with probability \(p\). Conditional on \((M_n,K_n,I_n)\), the increment has the following distribution:
\[
\begin{array}{c|c}
(\Delta M,\Delta K,\Delta I)&\text{conditional probability}\\\hline
(0,0,0)&q\\
(1,1,1)&p(1-M_n/n)\\
(1,0,-1)&pI_n/n\\
(1,0,0)&p(M_n-I_n)/n.
\end{array}
\]
The cases correspond to a closed new vertex, a newly retained singleton, a retained vertex attaching to an old singleton, and a retained vertex attaching to a larger retained component. This transition table follows directly from the parent-choice construction and contains all possible cases.

**2. Elementary first moments and cross-moments.** The retained induced graph is a forest, so its component count is its retained vertex count minus its number of retained edges. Each of the \(n-1\) tree edges has both endpoints retained with probability \(p^2\). Consequently
\[
\mathbb E M_n=np,\qquad
\mathbb E K_n=np-(n-1)p^2.
\]
For each edge with endpoints \(u,v\), the covariance of \(M_n\) with its retention indicator is \(2p^2q\). Summing over edges gives
\[
\operatorname{Cov}(M_n,K_n)=pq[n-2p(n-1)]. \tag{1}
\]
Let \(i_n=\mathbb E I_n\). From the transition table,
\[
i_1=p,\qquad i_{n+1}=\left(1-\frac pn\right)i_n+pq.
\]
Putting \(a=pq/(1+p)\) and \(b=2p^2/(1+p)\), direct substitution yields
\[
i_n=an+bh_n. \tag{2}
\]
Because the tree distribution is independent of \(p\), differentiating the product Bernoulli measure gives the score identity
\[
\operatorname{Cov}(M_n,I_n)=pq\,\frac{d i_n}{dp}. \tag{3}
\]
This identity holds for every \(p\in(0,1)\); it follows by differentiating the finite expectation of \(I_n\) over all independent site-retention configurations.

**3. Exact covariance recurrence.** Set \(C_n=\operatorname{Cov}(K_n,I_n)\). Multiplying the increments in the transition table shows that \(\Delta K\,\Delta I=\Delta K\) in every case. Expanding the covariance and subtracting the product of conditional means therefore gives
\[
\begin{aligned}
C_{n+1}&=\left(1-\frac pn\right)C_n+pq(1-pq)\\
&\quad-\frac pn\left[\operatorname{Cov}(M_n,K_n)+\operatorname{Cov}(M_n,I_n)\right]
+\frac{p^2q}{n}i_n.
\end{aligned}\tag{4}
\]
Insert (1)–(3), noting \(h_n'= -h_n s_n\), and differentiate \(b\) to obtain \(b'=2p(p+2)/(1+p)^2\). Simplification yields
\[
C_{n+1}=\left(1-\frac pn\right)C_n+(1+p)c-\frac{2p^3q}{n}+
\frac{p^2q h_n}{n}\left[b-b'+bs_n\right], \tag{5}
\]
where the displayed rational polynomial for \(c\) is equivalently defined by
\[
(1+p)c=pq(1-2p+3p^2)+p^2q\left(a-\frac{da}{dp}\right).
\]
The last identity is verified by expanding rational functions of \(p\), with no limiting argument.

**4. Solve the recurrence.** Define \(R_n=C_n-cn+2p^2q\). Since \(h_{n+1}=(1-p/n)h_n\), (5) becomes
\[
\frac{R_{n+1}}{h_{n+1}}-\frac{R_n}{h_n}
=\frac{p^2q}{n-p}\left[b-b'+bs_n\right]. \tag{6}
\]
At \(n=1\), both \(K_1\) and \(I_1\) equal a Bernoulli variable, whence \(C_1=pq\) and \(R_1=pq(1+2p)-c\). Summing (6) from one to \(n-1\) and using
\[
\sum_{k=1}^{n-1}\frac1{k-p}=s_n,\qquad
\sum_{k=1}^{n-1}\frac{s_k}{k-p}=\frac{s_n^2-t_n}{2}
\]
gives the boxed exact covariance formula.

**5. Growth rate and its sign.** For fixed \(p\in(0,1)\),
\[
h_n=\frac{\Gamma(n-p)}{\Gamma(1-p)\Gamma(n)}=O_p(n^{-p}),\qquad
s_n=\log n+O_p(1),\quad t_n=O_p(1).
\]
Thus the correction term in the exact formula is \(O_p(n^{-p}(\log n)^2)\). Finally
\[
2p^4+5p^3+3p^2-p+1=(1-p)+p^2(3+5p+2p^2)>0
\]
for \(0<p<1\), proving \(c>0\) and the asymptotic statement.

## Verification

The accompanying `verify.py` independently enumerates every recursive-tree parent assignment and all site-retention subsets for \(1\le n\le7\) at \(p\in\{1/4,1/2,3/4\}\), compares the resulting exact rational covariance with the boxed formula, and separately checks the recurrence and first-moment expressions through larger finite sizes. The analytical proof above, rather than finite enumeration, establishes the theorem for all \(n\ge1\). Run using a standard Python 3 interpreter; no external packages are required.

## Relationship to prior work

Gu and Yuan [1] rigorously study the site-percolation cluster-size profile and largest components of random recursive trees. Their Equation (1.5) gives the full Markov transition mechanism for the cluster-size counts, and their Theorem 1 gives a first-order law of large numbers. In particular, the transition principle used in Step 1 is already available in [1], and is **not** claimed as new. The result here is the explicit all-size *mixed covariance* between the total retained component count and the singleton component count, including its positive, nontrivial linear coefficient and its decaying correction. Neither Theorems 1–2 nor the proof sections of the inspected full text of [1] state this covariance identity; the broad transition mechanism does determine it indirectly and is acknowledged as prior coverage of the underlying process.

Kalay and Ben-Naim [2] investigate fragmentation of recursive trees, principally cluster-size distributions and scaling under removal of a prescribed number of vertices. Their full paper was checked for the same mixed-covariance statement; it does not present this result and its fixed-removal sampling model differs from the independent-retention model here. Janson [3] studies fluctuations of *total* component counts during graph uncovering, including recursive-tree examples; his results do not specify the present singleton–total covariance. The independent-retention hypothesis and explicit finite-\(n\) formula distinguish the present theorem from these prior results.

## Limitations

The result does not address covariance with other fixed cluster sizes, stochastic dependence orders, a central limit theorem, or site percolation conditioned on an exact retention count. It establishes eventual positivity of the covariance, not a proved sign classification at every finite \(n\). Historical priority has been checked against the named primary sources and searched research records, but no literature search proves that an independently discovered identity does not exist. Independent mathematical validation has not been performed.

## References

[1] C. Gu and L. Yuan, *Size distribution of clusters in site-percolation on random recursive tree*, arXiv:2408.12515 (first publicly posted 22 August 2024), especially Equation (1.5), Theorems 1–2, and Sections 2–4. https://arxiv.org/pdf/2408.12515

[2] Z. Kalay and E. Ben-Naim, *Fragmentation of Random Trees*, arXiv:1409.7106 (2014); *Journal of Physics A* **48** (2015), 045001. https://arxiv.org/pdf/1409.7106

[3] S. Janson, *Uncovering a graph*, *Probability Theory and Related Fields* (2025), https://doi.org/10.1007/s00440-025-01401-9, particularly the component-count fluctuation results and random-recursive-tree example.
