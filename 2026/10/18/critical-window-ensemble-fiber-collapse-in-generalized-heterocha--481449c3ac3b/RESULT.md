# Critical-window ensemble fiber collapse in generalized heterochaos baker maps

## Finding
Fix an integer \(M\ge2\), a parameter \(0<a<1/M\), and the generalized two-dimensional heterochaos baker map \(f_a\) defined in [1,2]. For Lebesgue-almost every base coordinate \(u\in[0,1]\), let \(I_n(u)\) be the vertical image of the complete initial fiber \(\{u\}\times[0,1]\) after \(n\) iterations. Its length is \(L_n(u)=|I_n(u)|\). Put \(p=Ma\), \(q=1-p\), and \(s=1/M\). Then \(L_n=M^{-K_n}\), where \(K_0=0\) and the law of \(K_{n+1}\), conditional on \(K_n=j\), is \(j+1\) with probability \(p\) and \(\max(0,j-1)\) with probability \(q\).

This identification yields an exact finite-time law and a sharp drift crossover. For every \(n\ge0\) and integer \(j\ge0\), let \(S_n\) be a simple walk with upward probability \(p\), let \(\pi_{n,p}(k)=\Pr_p(S_n=k)\) (zero unless \(|k|\le n\) and the parity agrees), and let \(\zeta=q/p\). Then
\[
\Pr(K_n=j)=\pi_{n,p}(j)+\zeta\pi_{n,p}(j+1)
 +(\zeta-1)\zeta^{-j-1}\Pr_q(S_n\ge j+2).
\]
Here \(\Pr_q\) denotes the walk with upward probability \(q\). Therefore the expected fiber width is given exactly by summing this finite distribution against \(M^{-j}\).

For each fixed real \(\eta\), use the triangular parameter sequence \(a_n=(1/2+\eta/\sqrt n)/M\), defined for all sufficiently large \(n\). Writing \(\mathbb E_{a_n}\) for the base-Lebesgue expectation under the corresponding map,
\[
\boxed{\lim_{n\to\infty}\sqrt n\,\mathbb E_{a_n}[L_n]
 =\frac{2\varphi(2\eta)-4\eta\Phi(-2\eta)}{1-1/M},}
\]
where \(\varphi\) and \(\Phi\) are the standard Gaussian density and distribution function. At the exact neutral-center parameter \(a=1/(2M)\), this is \(\sqrt{2/\pi}/(1-1/M)\). At the same triangular parameters,
\[
\frac{-\log L_n}{\sqrt n\log M}\ \Longrightarrow\
 \max_{0\le t\le1}(B_t+2\eta t),
\]
where \(B\) is standard Brownian motion. The limiting distribution function at \(x\ge0\) is
\[
\Phi(x-2\eta)-e^{4\eta x}\Phi(-x-2\eta).
\]
For a fixed parameter \(a\), the expected width tends to \((q-p)/(q-p/M)>0\) when \(p<q\); it tends to zero when \(p>q\). At \(p=q\), the expected width tends to zero at the above sharp order, but along almost every fixed base fiber \(\limsup_n L_n=1\) and \(\liminf_nL_n=0\): ensemble contraction does not imply pathwise convergence. For \(p>q\), \(L_n\to0\) almost surely.

## Assumptions and scope
For each \(1\le k\le M\), on the narrow base interval \([(k-1)a,ka)\), the base map is \(\tau_a(u)=(u-(k-1)a)/a\) and the vertical map is \(v\mapsto (v+k-1)/M\). On the wide base interval \([Ma,1]\), the base map is \(\tau_a(u)=(u-Ma)/(1-Ma)\), while the vertical coordinate in \([(k-1)/M,k/M)\) is mapped to \(Mv-k+1\) (the usual final-interval endpoint convention applies). All width assertions ignore the Lebesgue-null set of base endpoints and their preimages. A fiber image is viewed as a vertical interval, with negligible boundary conventions. No invariant probability distribution on the space of fibers is assumed. For fixed \(\eta\), all parameter-dependent statements are valid for \(n\) large enough that \(0<p_n<1\).

## Proof
**Exact geometric reduction.** Starting with the full vertical interval \([0,1]\), every image is a complete \(M\)-adic interval. A narrow-base step maps a depth-\(j\) interval to a depth-\(j+1\) interval, dividing its length by \(M\). A wide-base step takes an \(M\)-adic interval of positive depth to its parent, multiplying its length by \(M\); when the current interval is \([0,1]\), the union of the \(M\) wide-base pieces maps to \([0,1]\). Since \(\tau_a\) is full-branch and preserves Lebesgue measure, base labels are independent with narrow probability \(p=Ma\) and wide probability \(q=1-Ma\). This proves the claimed reflected birth-death recursion and \(L_n=M^{-K_n}\).

**Reflection formula.** Let \(X_i\in\{-1,1\}\) be the independent base labels, \(S_n=\sum_{i=1}^nX_i\). The reflected recursion gives \(K_n=S_n-\min_{0\le k\le n}S_k\). Reversing the iid increments gives the distributional equality \(K_n\stackrel{d}{=}\max_{0\le k\le n}S_k\). For \(z\ge1\), reflect the path after its first visit to \(z\): a path ending at \(k<z\) that reached \(z\) is paired with a path ending at \(2z-k\), with the original-to-reflected probability ratio \((q/p)^{z-k}\). Thus
\[
\Pr(K_n<z)=\Pr_p(S_n<z)-\sum_{\ell>z}(q/p)^{\ell-z}\Pr_p(S_n=\ell).
\]
Set \(z=j+1\) and subtract the same formula at \(z=j\). The identity \((q/p)^{\ell}\Pr_p(S_n=\ell)=\Pr_q(S_n=\ell)\) converts the remaining weighted tail into the finite-time distribution stated above, valid with no parity restrictions beyond those in \(\pi_{n,p}\). At \(p=q=1/2\), it simplifies to the binomial formula
\[
\Pr(K_n=j)=2^{-n}{n\choose\lfloor(n-j)/2\rfloor},\quad 0\le j\le n.
\]

**Critical window and exact coefficient.** Set \(p_n=1/2+\eta/\sqrt n\), \(q_n=1-p_n\), \(\zeta_n=q_n/p_n\). For each fixed integer \(j\ge0\), the lattice local central limit theorem gives
\[
\sqrt n\{\pi_{n,p_n}(j)+\zeta_n\pi_{n,p_n}(j+1)\}\to2\varphi(2\eta).
\]
Also \(\sqrt n(\zeta_n-1)\to-4\eta\), \(\zeta_n^{-j-1}\to1\), and, using the ordinary central limit theorem under the swapped probability \(q_n\), \(\Pr_{q_n}(S_n\ge j+2)\to\Phi(-2\eta)\). Consequently
\[
\sqrt n\Pr(K_n=j)\to h(\eta):=2\varphi(2\eta)-4\eta\Phi(-2\eta).
\]
This boundary constant is strictly positive because it equals the density at zero of the maximum of a drifted Brownian motion. To sum over \(j\), choose \(J_n=\lceil 3\log n/\log M\rceil\). The local binomial bound \(\sup_k\pi_{n,p_n}(k)=O_\eta(n^{-1/2})\), the exact finite-time formula, and \(\zeta_n^{-j-1}=O_\eta(1)\) uniformly for \(0\le j\le J_n\), give \(\sqrt n\Pr(K_n=j)\le C_\eta\) on this range. The contribution of \(j>J_n\) to \(\sqrt n\mathbb E[M^{-K_n}]\) is at most \(\sqrt nM^{-J_n}\to0\). Dominated summation against \(M^{-j}\) now yields \(h(\eta)\sum_{j\ge0}M^{-j}=h(\eta)/(1-1/M)\).

**Distributional crossover.** Donsker's invariance principle for the triangular Bernoulli arrays gives \(S_{\lfloor nt\rfloor}/\sqrt n\Rightarrow B_t+2\eta t\) in continuous-path scaling. The maximum is a continuous functional on continuous limits, so the equality in law with \(K_n\) gives the stated convergence. The explicit CDF follows from the Brownian reflection principle with drift.

**Fixed-parameter boundaries.** If \(p<q\), the reflected chain is irreducible positive recurrent, with stationary masses \((1-p/q)(p/q)^j\); multiplying by \(M^{-j}\) and summing yields \((q-p)/(q-p/M)\). If \(p>q\), \(S_n/n\to p-q>0\) and its all-time minimum is finite almost surely, so \(K_n\to\infty\) and \(L_n\to0\) almost surely. If \(p=q\), the symmetric walk is recurrent and unbounded, so its reflection hits zero and arbitrarily large levels infinitely often almost surely. The same recurrence argument applies to \(p<q\). Therefore \(\limsup L_n=1\), \(\liminf L_n=0\) in the neutral and expanding-center regimes. The critical mean follows from the critical-window formula at \(\eta=0\).

## Verification
The standalone `CHECK.py` uses exact rational arithmetic for each reflected-walk distribution through 14 iterations at five distinct rational biases, and independently compares the exact reflection formula with the recurrence. It checks geometric \(M\)-adic fiber evolution at \(M=2,3,5\), plus standard-library numerical local-limit and critical-mean constants for several drifts and values of \(M\). Execute `python CHECK.py` from the same directory; expected markers end in `_PASS`. These tests support arithmetic reproducibility but are not substitutes for the above infinite-parameter and asymptotic arguments.

## Relationship to prior work
Saiki, Takahasi, Yamamoto and Yorke [1] define the generalized heterochaos baker maps and classify expanding, contracting, and neutral central Lyapunov regimes, leaving quantitative fiber-width scaling outside their mixing statements. Takahasi [2] establishes strong and exponential mixing and bounds inducing return-time tails; those return times are different random variables from the image width of a whole vertical fiber. Takahasi and Tsujii [3] prove sharp \(n^{-3/2}\) correlation decay at the neutral point using an **absorbed** random-walk representation for a transfer operator. Here the fiber depth is a **reflected** walk with a holding boundary; the observable is an initial-fiber image width, not a correlation or transfer-operator norm. Standard random-walk reflection, Gaussian limits, and Brownian maximum formulas are credited as classical ingredients. The map-specific exact fiber law and the explicit near-critical mean-width crossover are the contributions assessed here; they are not claims to discover the classical random-walk results.

## Limitations
The result concerns two-dimensional maps and full initial vertical fibers; it does not imply analogous laws for arbitrary subintervals, individual point separations, correlation decay, or three-dimensional stable fibers. Near-critical convergence is pointwise in fixed \(\eta\), not uniformly in a growing drift range. The random-walk ingredients themselves are classical. No independent validation or exhaustive publication-priority certification has been performed; unidentified equivalent formulations remain possible.

## References
[1] Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836v1 (public 2024-01-01), particularly Sections 1.1 and 2.5–2.6; manuscript v2 inspected.

[2] H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119v1 (public 2023-07-16), particularly Sections 2.5–2.8.

[3] H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618v1 (public 2024-08-29), particularly Sections 1.2, 2.4, 3 and 4.
