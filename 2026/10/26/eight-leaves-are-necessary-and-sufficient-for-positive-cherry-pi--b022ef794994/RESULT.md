# Eight leaves are necessary and sufficient for positive cherry–pitchfork covariance in Ford trees

## Finding
Let \(A_n\) and \(C_n\) be the respective numbers of rooted pitchforks (fringe subtrees with three leaves) and cherries (fringe subtrees with two leaves) in Ford's \(\alpha\)-growth tree with \(n\ge3\) leaves and \(0\le\alpha\le1\). Then:

1. For \(n=3\) or \(\alpha=1\), \(\operatorname{Cov}_\alpha(A_n,C_n)=0\).
2. For every \(4\le n\le7\) and every \(0\le\alpha<1\), \(\operatorname{Cov}_\alpha(A_n,C_n)<0\).
3. For each integer \(n\ge8\), there exists \(\delta_n>0\) such that \(\operatorname{Cov}_\alpha(A_n,C_n)>0\) whenever \(1-\delta_n<\alpha<1\). More precisely, for each fixed \(n\ge3\),
\[
\operatorname{Cov}_{1-\varepsilon}(A_n,C_n)
=\left(\frac{n-3}{2}-H_{n-3}\right)\varepsilon+O_n(\varepsilon^2),
\qquad \varepsilon\downarrow0,
\]
where \(H_0=0\) and \(H_k=\sum_{j=1}^k1/j\).

Thus the smallest number of leaves at which **some** Ford parameter admits positive cherry–pitchfork covariance is exactly eight. The result does not assert positivity for every \(n\ge8\) and every \(\alpha>1/2\).

## Assumptions and scope
The initial tree has two leaves and one cherry. To grow from \(n\) to \(n+1\) leaves, choose a pendant edge with weight \(1-\alpha\) and an internal edge with weight \(\alpha\), subdivide it, and attach a new pendant leaf; the total weight is \(n-\alpha\). The root's stem edge is counted as internal, as in Ford's original convention. At \(n=3\), both counts equal one. At \(\alpha=1\), the tree is the deterministic comb, so both counts equal one for all \(n\ge3\). This is a finite-size statement for rooted trees; no asymptotic interchange in \(n\) and \(\alpha\) is claimed.

## Proof
Write \(p=A_n\), \(q=C_n\), and \(z=n-\alpha\). Classification of selected edges by the two- and three-leaf fringe shapes gives the four possible changes \((\Delta A,\Delta C)\) with *unnormalized* weights
\[
\begin{array}{c|c}
(0,0)&2p+\alpha(n-p-q-1)\\
(-1,+1)&(1-\alpha)p\\
(+1,0)&(2-\alpha)(q-p)\\
(0,+1)&(1-\alpha)(n-p-2q).
\end{array}
\]
Their sum is \(n-\alpha\); these edge categories follow by counting pitchfork-pendant edges, essential-cherry edges, and the remaining edges (Kaur–Choi–Wu, Lemma 2.1). The table is also an independent finite-state transition rule used by `verify.py`.

Set \(m_n=\mathbb E[C_n]\), \(a_n=\mathbb E[A_n]\), \(s_n=\mathbb E[C_n^2]\), and \(b_n=\mathbb E[A_nC_n]\). Multiplying the four transition increments gives, with all four quantities initially equal to one at \(n=3\),
\[
\begin{aligned}
(n-\alpha)m_{n+1}&=(n-2+\alpha)m_n+n(1-\alpha),\\
(n-\alpha)a_{n+1}&=(n-3+\alpha)a_n+(2-\alpha)m_n,\\
(n-\alpha)s_{n+1}&=(n-4+3\alpha)s_n+2(n-1)(1-\alpha)m_n+n(1-\alpha),\\
(n-\alpha)b_{n+1}&=(n-5+3\alpha)b_n+(n-1)(1-\alpha)a_n+(2-\alpha)s_n.
\end{aligned}
\]
For fixed \(n\), all four moments are rational analytic functions of \(\varepsilon=1-\alpha\) near zero, because the denominators \(n-\alpha\) are nonzero there. Write
\[
m_n=1+u_n\varepsilon+O_n(\varepsilon^2),\quad
a_n=1+v_n\varepsilon+O_n(\varepsilon^2),\quad
s_n=1+3u_n\varepsilon+O_n(\varepsilon^2),\quad
b_n=1+w_n\varepsilon+O_n(\varepsilon^2).
\]
Differentiating the moment recurrences at \(\varepsilon=0\) yields, for \(n\ge3\),
\[
\begin{aligned}
u_{n+1}&=u_n+\frac{n-2}{n-1},\\
v_{n+1}&=\frac{(n-2)v_n+u_n-1}{n-1},\\
w_{n+1}&=\frac{(n-2)w_n+n-4+3u_n}{n-1},
\end{aligned}
\]
with \(u_3=v_3=w_3=0\). The covariance coefficient is \(r_n=w_n-u_n-v_n\); therefore
\[
r_{n+1}=\frac{(n-2)r_n+u_n-1}{n-1},\qquad
u_n=n-2-H_{n-2}.
\]
Solving this recurrence gives \(r_n=(n-3)/2-H_{n-3}\). Moreover \(r_7=-1/12\), \(r_8=13/60\), and for \(n\ge5\), \(r_{n+1}-r_n=1/2-1/(n-2)>0\). Thus \(r_n>0\) for every \(n\ge8\), proving part 3 by analyticity.

For the sharp lower bound, let \(x=\alpha\). Direct symbolic iteration of the same moment recurrences gives
\[
\operatorname{Cov}_x(A_4,C_4)=\frac{2(x-1)}{(x-3)^2},\qquad
\operatorname{Cov}_x(A_5,C_5)=\frac{2(x-1)(x+2)^2}{(x-4)^2(x-3)^2},
\]
\[
\operatorname{Cov}_x(A_6,C_6)=\frac{2(x-1)P_6(x)}{(x-5)^2(x-4)^2(x-3)^2},
\]
\[
\operatorname{Cov}_x(A_7,C_7)=\frac{-2(x-1)P_7(x)}{(x-6)^2(x-5)^2(x-4)^2(x-3)^2},
\]
where
\[
P_6(x)=11x^4-88x^3+391x^2-458x+240
\]
and
\[
P_7(x)=13x^6-320x^5+1409x^4-1834x^3-10164x^2+20376x-10080.
\]
To certify their strict signs on the entire continuous interval \(0\le x\le1\), set \(x=t/(1+t)\), \(t\ge0\). Expanding \((1+t)^4P_6(t/(1+t))\) in ascending powers of \(t\) gives coefficients \((240,502,457,280,96)\), all positive. Similarly \((1+t)^6[-P_7(t/(1+t))]\) has coefficients \((10080,40104,59484,40330,12517,2260,600)\), all positive. Hence \(P_6>0\) and \(P_7<0\) on \([0,1]\); all covariances for \(4\le n\le7\) are strictly negative when \(x<1\). Combining this with the near-comb result proves the claimed exact minimal size.

## Verification
The included `verify.py` independently propagates the exact four-transition probability distribution through thirteen leaves at seven rational parameter values and compares its raw moments with the algebraic recurrence. It symbolically checks the four small-size covariance factorizations and both nonnegative-coefficient certificates, and verifies the harmonic coefficient identity through \(n=149\) with exact arithmetic. Run `python verify.py` in an environment with SymPy installed. These finite tests complement the unrestricted analytical argument; they do not themselves establish its infinite parameter range.

## Relationship to prior work
Kaur, Choi and Wu (2021; published 2023) proved a complete finite-size joint-distribution recurrence and an asymptotic correlation sign change at \(\alpha=1/2\). Their recurrences and local edge classification are credited as the starting point, not claimed as new. The present statement isolates the **minimum finite sample size permitting positive covariance anywhere in the Ford family**, by deriving an exact near-comb linear-response law valid for every \(n\) and combining it with interval-wide polynomial sign certificates for smaller trees. The earlier asymptotic result neither supplies the minimum sample size nor the harmonic coefficient. Wu and Choi (2015/2016) treat the two endpoint models, not the interior-parameter near-comb response.

## Limitations
Positivity for a fixed \(n\ge8\) is proved only in a parameter neighborhood of one, and no uniqueness or monotonicity of a finite-size root in \(\alpha\) is asserted. The first-order expansion is **fixed-\(n\)**, not uniform as \(n\to\infty\). The result draws on previously published moment recurrences; the originality claim concerns their new global finite-threshold consequence. An unlocated earlier explicit analysis could supersede this consequence. Independent audit has not been performed.

## References
1. Gursharn Kaur, Kwok Pui Choi, Taoyang Wu, *Distributions of cherries and pitchforks for the Ford model*, arXiv:2110.02850, initial public posting 2021-10-06; Theoretical Population Biology (2023), especially Lemma 2.1, Theorems 4.1 and 4.6, Corollary 4.4.
2. Taoyang Wu and Kwok Pui Choi, *On joint subtree distributions under two evolutionary models*, arXiv:1508.03139, first posted 2015-08-13, later published (2016).
3. Kwok Pui Choi, Ariadne Thompson, Taoyang Wu, *On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees*, arXiv:2002.12643, first posted 2020-02-28.
