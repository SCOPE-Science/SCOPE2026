# A sharp rim-price transition and critical window for resistance-optimized wheels

## Finding

A wheel has a cycle of \(n\ge3\) rim vertices and a single hub adjacent to every rim vertex. All spoke conductances have unit price; all rim conductances have common relative price \(t>0\). Among all nonnegative edge conductances satisfying a total price budget of one, the unique configuration minimizing the sum of unordered pairwise effective resistances is invariant under every rotation of the rim. Write its spoke conductance as \(a_n^*(t)\) and rim conductance as \(b_n^*(t)\).

The entire rim is omitted exactly when
\[
\boxed{t\ge t_n^{\mathrm{crit}}=\frac{2(n+1)}n.}
\]
In this regime, \(a_n^*(t)=1/n\), \(b_n^*(t)=0\), and the optimal Kirchhoff index is \(n^3\). Below the threshold every rim and spoke has positive optimal conductance, characterized uniquely by the scalar equation below. Thus for any fixed \(t>2\), sufficiently large wheels are optimized by a star, while at \(t=2\) every finite wheel retains a positive but vanishing rim.

At a fixed positive price the optimal value obeys the exact limit
\[
\boxed{\lim_{n\to\infty}\frac{K_n^*(t)}{n^3}=\begin{cases}
\frac12\sqrt{t(4-t)},&0<t<2,\\
1,&t\ge2.
\end{cases}}
\]
For \(0<t<2\), the limiting budget fractions spent on spokes and rim, respectively, are \(2/(4-t)\) and \((2-t)/(4-t)\). In particular, as an already positive rim price decreases towards zero, the two budget shares tend to one half each; the two limits \(n\to\infty\) and \(t\downarrow0\) are taken in that order.

The finite-size transition has a sharp critical window. For any fixed real \(s\), put \(t_n=2+s/n>0\) for sufficiently large \(n\), and \((z)_+=\max\{z,0\}\). Then
\[
\boxed{\lim_{n\to\infty}n^2b_n^*(t_n)=\frac{(2-s)_+}{4},\qquad
\lim_{n\to\infty}\frac{n^3-K_n^*(t_n)}{n}=\frac{(2-s)_+^2}{8}.}
\]
This determines both the scale of the emerging rim and its order-\(n\) improvement in the sum of effective resistances within the price window.

## Assumptions and scope

The graph has vertices \(0,\ldots,n-1,h\), where \(h\) is the hub. Its spoke edges are \(\{h,i\}\), and its rim edges are \(\{i,i+1\pmod n\}\), with \(n\ge3\). Every edge conductance is nonnegative; at least a connected spanning subgraph must remain. The feasible budget is
\[
\sum_{i=0}^{n-1}a_i+t\sum_{i=0}^{n-1}b_i=1,\qquad t>0.
\]
For a connected graph, \(R_{vw}\) is electrical effective resistance between vertices \(v,w\); define \(K=\sum_{v<w}R_{vw}\). Disconnected allocations are assigned \(K=+\infty\). The price \(t\) is constant across rim edges, but may depend on \(n\) in the critical-window statement. No integer or discretized restrictions are imposed on conductances.

Put
\[
\mu_k=2-2\cos(2\pi k/n),\qquad k=1,\ldots,n-1,
\]
and introduce \(u=nb\), so that for rotationally symmetric allocations
\[
a=\frac{1-tu}{n},\qquad b=\frac un,\qquad 0\le u<1/t.
\]
Define
\[
F_n(u;t)=\frac{1}{(n+1)(1-tu)}+
\sum_{k=1}^{n-1}\frac{1}{1+u(\mu_k-t)}.
\]
The exact optimum is \(K_n^*(t)=n(n+1)\min_{0\le u<1/t}F_n(u;t)\). If \(t<2(n+1)/n\), the unique minimizing value \(u=u_n(t)>0\) is the unique root in that interval of
\[
\frac{t}{(n+1)(1-tu)^2}+
\sum_{k=1}^{n-1}\frac{t-\mu_k}{[1+u(\mu_k-t)]^2}=0.
\]
If \(t\ge2(n+1)/n\), the minimizing value is \(u_n(t)=0\). The minimizer in the *full, nonsymmetric* feasible conductance space is unique in all cases.

## Proof

**1. Strict convexity, existence, and symmetry.** Let \(N=n+1\). For any connected conductance vector, restrict the weighted Laplacian \(L\) to the common subspace \(\mathbf1^\perp\), obtaining a positive-definite matrix \(H\). Kirchhoff's spectral identity is \(K=N\operatorname{tr}(H^{-1})\). For any nonzero feasible direction in the complete edge-conductance coordinate space, the corresponding symmetric perturbation \(E\) of \(H\) is nonzero: a simple graph's Laplacian off-diagonals recover its individual edge conductances. Differentiation along the direction gives
\[
\frac{d^2}{dz^2}\operatorname{tr}(H+zE)^{-1}\bigg|_{z=0}
=2\operatorname{tr}(H^{-1}EH^{-1}EH^{-1})>0.
\]
The strict inequality follows by writing the expression as the trace of a positive-definite weight times the square of the nonzero symmetric matrix \(H^{-1/2}EH^{-1/2}\). Hence \(K\) is strictly convex throughout the connected feasible domain. This domain is convex, and \(K\to+\infty\) along any conductance sequence tending to a disconnected network, because its smallest positive Laplacian eigenvalue tends to zero. The feasible simplex is compact and contains the connected star, so a unique minimum exists. Rim rotations preserve both budget and objective; uniqueness forces the minimum to have identical spokes and identical rim edges.

**2. Exact finite spectrum.** For uniform spokes \(a>0\) and uniform rims \(b\ge0\), the Laplacian eigenvalues are
\[
0,\qquad (n+1)a,\qquad a+b\mu_k\quad(1\le k<n).
\]
This follows by splitting the rim into its constant mode, coupled to the hub, and its \(n-1\) zero-sum discrete Fourier modes. Consequently,
\[
K=(n+1)\left[\frac{1}{(n+1)a}+
\sum_{k=1}^{n-1}\frac{1}{a+b\mu_k}\right]
=n(n+1)F_n(u;t).
\]
The Fourier-mode denominators are strictly positive on \(0\le u<1/t\). Every term is convex in \(u\), and the first is strictly convex. Thus \(F_n\) is strictly convex. Moreover \(F_n(u;t)\to+\infty\) as \(u\uparrow1/t\), so it has exactly one minimizer.

The elementary cycle eigenvalue identity \(\sum_{k=1}^{n-1}\mu_k=2n\) yields
\[
F_n'(0;t)=\frac{t}{n+1}+\sum_{k=1}^{n-1}(t-\mu_k)
=\frac{n^2}{n+1}t-2n.
\]
The constrained convex minimum occurs at zero if and only if this derivative is nonnegative, proving the sharp threshold. Otherwise the derivative begins negative and tends to positive infinity at the right endpoint, giving precisely the stated unique interior root. If the rim is omitted, each spoke is \(1/n\); summing \(n\) hub-to-rim resistances of size \(n\) and \(\binom n2\) rim-to-rim resistances of size \(2n\) gives \(K_n^*(t)=n^3\).

**3. Large wheels at a fixed price.** On every compact subinterval of \([0,1/t)\), uniform Riemann-sum convergence gives
\[
\frac{F_n(u;t)}n\longrightarrow
\int_0^{2\pi}\frac{d\theta}{2\pi[1-tu+2u(1-\cos\theta)]}
=\frac{1}{\sqrt{(1-tu)(1+(4-t)u)}}=:J_t(u).
\]
No minimizing sequence can approach \(u=1/t\): the normalized sums there diverge. Indeed, truncate the nonnegative integrand at any height \(M\), use bounded Riemann-sum convergence as the parameters approach that endpoint, and then let \(M\to\infty\); the limit integrand is proportional to \((1-\cos\theta)^{-1}\), which has infinite integral. Thus every cluster point of the finite minimizers minimizes \(J_t\).

Minimizing \(J_t\) is equivalent to maximizing
\[
P_t(u)=(1-tu)(1+(4-t)u)
=1+(4-2t)u-t(4-t)u^2,
\qquad 0\le u\le1/t.
\]
For \(0<t<2\), this is strictly concave with the unique maximizer
\[
u_\infty(t)=\frac{2-t}{t(4-t)},
\qquad 1-tu_\infty(t)=\frac2{4-t},
\qquad P_t(u_\infty)=\frac4{t(4-t)}.
\]
For \(2\le t\le4\), \(P_t\) is nonincreasing on the feasible interval; for \(t>4\), it is convex with endpoint values \(1\) and \(0\), so its unique maximizer is again \(u=0\). Uniform convergence and uniqueness force \(u_n(t)\to u_\infty(t)\), with zero for \(t\ge2\). As \(K_n^*(t)=n(n+1)F_n(u_n(t);t)\), this gives the asserted normalized optimum and budget shares. For fixed \(t>2\), the exact finite threshold also shows that \(u_n(t)=0\) whenever \(n\ge2/(t-2)\).

**4. Critical-window scaling.** Let \(t_n=2+s/n\). A second cycle identity, \(\sum_{k=1}^{n-1}\mu_k^2=6n\) for \(n\ge3\), follows by taking the trace of the square of the cycle Laplacian. Thus
\[
F_n'(0;t_n)=\frac{n(s-2)}{n+1},\qquad
F_n''(0;t)=2\left[\frac{n^2}{n+1}t^2-4nt+6n\right].
\]
Uniformly for each fixed \(C>0\) and \(0\le u\le C/n\), one has \(F_n''(u;t_n)/n\to4\), because \(0\le\mu_k\le4\) and the denominators converge uniformly to one. Consequently, for each fixed \(z\ge0\),
\[
F_n'(z/n;t_n)\longrightarrow s-2+4z.
\]
Strict convexity then implies \(nu_n(t_n)\to(2-s)_+/4\); when \(s\ge2\), the finite threshold makes the rim exactly zero. Taylor's formula uniformly on the \(O(1/n)\) interval gives
\[
F_n(0;t_n)-F_n(u_n(t_n);t_n)
=\frac{(2-s)_+^2}{8n}+o(1/n).
\]
Finally \(b_n^*(t_n)=u_n(t_n)/n\), while \(K_n^*(t_n)=n(n+1)F_n(u_n(t_n);t_n)\) and \(n(n+1)F_n(0;t_n)=n^3\). These identities prove both limits in the critical-window statement.

## Verification

The standalone `verification.py` uses exact rational arithmetic and no nonstandard Python packages. Running `python3 verification.py` checks 196 separate finite instances for \(3\le n\le9\), seven rational prices, and three feasible rim allocations per price (plus the independent derivative checks). It compares the full \((n+1)\)-vertex Kirchhoff-index inverse with the rotationally reduced matrix formula, verifies the exact star value and directional derivative, and checks the two cycle spectral moments. These finite checks corroborate the algebra but do not prove the infinite-\(n\) asymptotics or the universal convexity theorem; those follow from the analytical arguments above.

## Relationship to prior work

Ghosh, Boyd, and Saberi established convex minimization of total effective resistance and, in their longer 2008 treatment, a symmetric wheel reduction with *equal* unit prices for spokes and rim, including the wheel spectrum and a one-dimensional stationary equation. The present theorem credits and reuses that spectral reduction. Its added claim is the exact all-size rim-price exclusion threshold, full price-dependent optimizer characterization, limiting allocation/value phase law, and quantitative finite-size critical window. Their 2006 conference version sets out the general problem and numerical methods but does not present these priced-wheel conclusions.

Li, Yang, and Zhang studied the Kirchhoff index for weighted wheels; Bapat and Gupta obtained resistance-distance formulas for wheels and fans, including a weighted-spoke setting. These results address invariant evaluation rather than the same stated budgeted price-dependent minimization. The Li–Yang–Zhang primary full text was not accessible for complete comparison, so earlier equivalent specialized statements cannot be ruled out absolutely. No implication of novelty follows merely from unsuccessful bibliographic searches.

## Limitations

The prices must be common within each of the two edge classes; with distinct prices around the rim, the symmetry reduction does not apply. The theorem minimizes the *sum* of all pairwise resistances, not their maximum, and treats continuous real-valued conductance allocation rather than discrete edge-installation decisions. The limiting budget fractions require \(t>0\) to be fixed before \(n\to\infty\). The critical-window limits are asymptotic and do not provide exact closed forms for interior finite-size roots. The bibliographic overlap risk from a partly inaccessible weighted-wheel article remains open.

## References

1. A. Ghosh, S. Boyd, A. Saberi, "Minimizing Effective Resistance of a Graph," *SIAM Review* 50(1) (2008), 37–66, DOI: 10.1137/050645452. Freely available author's copy: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf . Section 5.2 and equation (38) give the equal-cost wheel reduction.
2. A. Ghosh, S. Boyd, A. Saberi, "Minimizing Effective Resistance of a Graph," *Proceedings of the 17th International Symposium on the Mathematical Theory of Networks and Systems* (July 2006); author's copy: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf .
3. C. Li, Y. Yang, H. Zhang, "Kirchhoff index of weighted wheel graphs \(W_n(a,b)\)," *Journal of Lanzhou University* 44(3) (2008); bibliographic record: https://www.researchgate.net/publication/268625211_Kirchhoff_index_of_weighted_wheel_graphs_W_n_ab . Complete primary text was not available for the present comparison.
4. R. B. Bapat, S. Gupta, "Resistance distance in wheels and fans," *Indian Journal of Pure and Applied Mathematics* 41(1) (2010), 1–13, DOI: 10.1007/s13226-010-0004-2 .
