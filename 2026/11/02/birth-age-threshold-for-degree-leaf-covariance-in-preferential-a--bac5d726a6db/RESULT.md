# Birth-age threshold for degree–leaf covariance in preferential-attachment trees

## Finding
Consider the degree-proportional preferential-attachment tree initialized by the edge \(\{1,2\}\). For integers \(n\ge j\ge3\), denote the degree of birth-rank vertex \(j\) in the \(n\)-vertex tree by \(D_{n,j}\) and the total number of degree-one vertices by \(L_n\). Define, for \(t\ge2\),
\[
h_t=\prod_{s=2}^{t-1}\left(1-\frac{1}{2(s-1)}\right),\qquad h_2=1,
\]
and for \(n\ge j\ge3\),
\[
a_{n,j}=\prod_{s=j}^{n-1}\left(1+\frac{1}{2(s-1)}\right),\qquad
b_{n,j}=\prod_{s=j}^{n-1}\left(1-\frac{1}{2(s-1)}\right).
\]
Empty products equal one. The exact finite-sample covariance is
\[
\boxed{\operatorname{Cov}(D_{n,j},L_n)=
\frac{a_{n,j}+3b_{n,j}-4+4(h_j-a_{n,j}h_n)}{3}.}
\tag{1}
\]
For every fixed integer \(j\ge3\), there is a finite first positive index \(\kappa_j>j\) such that the covariance is strictly negative for \(j<n<\kappa_j\), apart from at most one possible zero, and is strictly positive for all \(n\ge\kappa_j\). As \(j\to\infty\),
\[
\boxed{\frac{\kappa_j}{j}\longrightarrow9.}
\tag{2}
\]
More precisely, whenever \(j\to\infty\) and \(n/j\to\rho>1\),
\[
\operatorname{Cov}(D_{n,j},L_n)\longrightarrow
\frac{(\sqrt\rho-1)(\sqrt\rho-3)}{3\sqrt\rho}.
\tag{3}
\]
Thus at a fixed macroscopic birth fraction \(j/n\to\alpha\in(0,1)\), the covariance is eventually positive for \(\alpha<1/9\) and negative for \(\alpha>1/9\). No assertion of a sign at \(\alpha=1/9\) is needed.

## Assumptions and scope
Start with the deterministic undirected edge joining vertices 1 and 2. If \(t\ge2\) vertices are present, vertex \(t+1\) attaches by one edge to an existing vertex \(v\) with conditional probability \(\deg_t(v)/(2(t-1))\). No self-loops, multiple edges, fitness weights, or attractiveness offsets are allowed. A leaf is any vertex of undirected degree one. The claimed birth-rank range begins at \(j=3\) to avoid initial-seed conventions. Expectations and covariances refer to the full random tree under this precisely stated law.

## Proof
Write \(p_t=1/[2(t-1)]\), let \(I_{t,j}\) indicate that vertex \(j\) remains a leaf at time \(t\), and put \(\mu_t=\mathbb E L_t\), \(d_t=\mathbb E D_{t,j}\), \(q_t=\mathbb E I_{t,j}\). At a growth step let \(J_t\) indicate attachment to vertex \(j\), and let \(U_t\) indicate attachment to some leaf. Conditionally on the entire current tree,
\[
\mathbb E[J_t\mid T_t]=p_tD_{t,j},\quad
\mathbb E[U_t\mid T_t]=p_tL_t,\quad
\mathbb E[J_tU_t\mid T_t]=p_tI_{t,j}.
\]
The increments obey \(D_{t+1,j}=D_{t,j}+J_t\) and \(L_{t+1}=L_t+1-U_t\), whence
\[
\mathbb E[D_{t+1,j}L_{t+1}\mid T_t]
=D_{t,j}L_t+(1+p_t)D_{t,j}-p_tI_{t,j}.
\]
Because \(\mu_{t+1}=(1-p_t)\mu_t+1\), \(d_{t+1}=(1+p_t)d_t\) and \(q_{t+1}=(1-p_t)q_t\), subtraction of mean products gives the exact identity
\[
C_{t+1}-C_t=p_t^2d_t\mu_t-p_tq_t,
\qquad C_t=\operatorname{Cov}(D_{t,j},L_t).
\tag{4}
\]
At birth \(D_{j,j}=I_{j,j}=1\) deterministically, so \(C_j=0\), \(d_j=q_j=1\). Starting with \(L_2=2\), the leaf-mean recursion solves to
\[
\mu_t=\frac{2(t-1)}3+\frac{4h_t}3.
\tag{5}
\]
Likewise \(d_t=a_{t,j}\), \(q_t=b_{t,j}=h_t/h_j\). The identities
\[
d_{t+1}-d_t=p_td_t,\quad q_{t+1}-q_t=-p_tq_t,\quad
d_{t+1}h_{t+1}=(1-p_t^2)d_th_t
\]
turn (4) and (5) into a telescoping sum:
\[
C_{t+1}-C_t=\tfrac13(d_{t+1}-d_t)
+(q_{t+1}-q_t)+\tfrac43(d_th_t-d_{t+1}h_{t+1}).
\]
Summing from \(t=j\) to \(n-1\) proves (1) exactly, including the empty-product boundary \(n=j\).

For the sign assertion, direct telescoping of the product gives
\[
\frac{d_t}{q_t}=\frac{t-3/2}{j-3/2}.
\]
Define \(B_t=(t-3/2)\mu_t/[2(t-1)]\). Then (4) has the sign of \(B_t-(j-3/2)\). For each \(t\ge3\), the elementary leaf bound \(\mu_t\le t-1\) and recurrence (5) give
\[
B_{t+1}-B_t=\frac{2t-1}{4t}-\frac{(2t-3)\mu_t}{8t(t-1)}
\ge\frac{2t+1}{8t}>0.
\tag{6}
\]
Also \(B_j/(j-3/2)=\mu_j/[2(j-1)]\le1/2\); hence the first covariance increment is strictly negative. Since \(\mu_t\ge2(t-1)/3\), one has \(B_t\to\infty\). Thus the increments change at most once, from negative to positive, and eventually stay positive. Moreover \(d_n\) grows as a positive multiple of \(\sqrt n\) with fixed \(j\), whereas \(q_n,h_n\to0\); (1) shows \(C_n\to+\infty\). Therefore the cumulative covariance crosses from strictly negative to strictly positive just once (with at most one zero at the transition), establishing existence and uniqueness of \(\kappa_j\).

Finally, standard product estimates obtained by expanding logarithms, or by gamma-ratio asymptotics, give, uniformly when \(n/j\to\rho\in(1,\infty)\),
\[
a_{n,j}\to\sqrt\rho,\qquad b_{n,j}\to\rho^{-1/2}.
\]
The remaining correction in (1) tends to zero: since \(a_{n,j}h_n=h_j\prod_{s=j}^{n-1}(1-p_s^2)\),
\[
0\le h_j-a_{n,j}h_n\le h_j\sum_{s=j}^{n-1}p_s^2
\le\frac{h_j}{4(j-2)}\to0.
\]
Consequently (1) yields (3), whose sign is determined by \(\sqrt\rho-3\) for \(\rho>1\). At every fixed \(\rho<9\), covariance is eventually negative; at every fixed \(\rho>9\) it is eventually positive. Combined with the single-crossing property, this proves (2).

## Verification
Run the included dependency-free program `python verify.py`. It enumerates all weighted parent-attachment outcomes through eight vertices, independently calculates exact rational cross moments, checks the closed form against the separate mixed-moment recurrence, and tests finite birth-rank sign transitions. Its successful completion prints `VERIFICATION_OK`. Computational checks are finite checks; the all-size and asymptotic assertions follow from the preceding proof, not from enumeration or floating-point fitting.

## Relationship to prior work
The degree-proportional growth mechanism is classical (Barabási and Albert, 1999). Ben-Naim and Krapivsky (2009) studied degree stratification by distance from the root, rather than birth-age degree covariance with total leaf count. Hartle and Krapivsky (2026) developed joint ordinary-degree/leaf-neighbor-degree distributions and global degree-class/leaf-count fluctuation results, including the exact leaf-mean formula equivalent to (5), but their age-agnostic formulas do not give the age-indexed mixed covariance (1) or its \(1/9\) boundary. The root-degree/leaf-count identity for uniform-attachment recursive trees concerns a different attachment mechanism. The full sample-size covariance profile and its single-crossing law are not consequences of the inspected reported marginal statistics alone.

## Limitations
The result is restricted to the unit-edge, degree-proportional one-parent tree with the stated seed. The distinction between a sampled vertex's own degree and its number of leaf neighbors is essential. It does not establish corresponding thresholds for multi-edge attachment, affine preferential attachment, age-dependent fitness or other seed conventions. The bound \(\alpha=1/9\) concerns a growing birth rank, not a fixed named vertex; equality at the threshold is not classified by the leading limit. The literature comparison is evidence of noncoverage among inspected sources, not a guarantee of historical priority.

## References
Barabási, A.-L., and Albert, R., “Emergence of scaling in random networks,” *Science* **286** (1999), 509–512, doi:10.1126/science.286.5439.509 (published 1999-10-15).

Ben-Naim, E., and Krapivsky, P. L., “Stratification in the Preferential Attachment Network,” arXiv:0905.1920 (first public preprint 2009-05-12); *Journal of Physics A* **42** (2009), 475001.

Hartle, H., and Krapivsky, P. L., “Leaves of preferential attachment trees,” arXiv:2602.01021 (first public preprint 2026-02-01).

Móri, T. F., “The Maximum Degree of the Barabási–Albert Random Tree,” *Combinatorics, Probability and Computing* **14** (2005), 339–348, doi:10.1017/S0963548304006133.
