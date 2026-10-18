# Balanced slow sites minimize diffusion in a biased periodic hopping chain

## Finding
For every integer \(n\ge4\), \(2\le m\le n-2\), and fixed positive rates \(p>q>0\) with \(p+q=1\), consider a nearest-neighbor continuous-time walk \(X_t\) on \(\mathbb Z\). At a site \(i\), its jump rates to \(i+1\) and \(i-1\) are respectively \(p/r_i\) and \(q/r_i\). The holding resistances are periodic and binary: \(r_i=r_0+\varepsilon b_i\), where \(r_0,\varepsilon>0\), \(b_i\in\{0,1\}\), \(b_{i+n}=b_i\), and exactly \(m\) entries in each period equal one.

Set \(R=nr_0+m\varepsilon\), \(\delta=p-q\), \(t=q/p\), and for \(1\le d<n\), \(F(d)=t^d+t^{n-d}\). If \(B\subseteq\{0,\ldots,n-1\}\) is the set of \(m\) slower sites, and \(d_{ab}\) is either cyclic separation between distinct \(a,b\in B\), then the long-time displacement variance rate \(C(B)=\lim_{T\to\infty}\operatorname{Var}(X_T)/T\) is
\[
C(B)=\frac nR+\frac{n^2\varepsilon^2}{R^3}\left\{\frac\delta{1-t^n}\left[m(1+t^n)+2\sum_{\{a,b\}\subset B} F(d_{ab})\right]-\frac{m^2}{n}\right\}.
\]
The unique global maximizers, up to cyclic rotation, have all \(m\) slow sites consecutive. The unique global minimizers, up to rotation, are the balanced mechanical patterns
\[
b_i=\left\lfloor\frac{(i+1)m}{n}\right\rfloor-\left\lfloor\frac{im}{n}\right\rfloor,\qquad 0\le i<n.
\]
The minimum is strictly below the maximum. Yet the limiting drift and stationary entropy-production rate are independent of the placement:
\[
v=\frac{n(p-q)}R,\qquad \sigma=\frac{n(p-q)}R\log\frac pq.
\]
Thus spatial arrangement changes dispersion even though drift, total holding inventory, and entropy dissipation are fixed.

## Assumptions and scope
The lattice is infinite, with rates periodic modulo \(n\). Occupation at a phase \(i\pmod n\) has the unique stationary law \(\pi_i=r_i/R\), and the variance limit exists for any initial phase; stationarity is used in the proof, while initial transients do not change the limit. The quantity \(C\) is the variance per unit time, twice the conventional effective diffusion coefficient \(D\). A slow site means larger \(r_i\), hence smaller total jump rate; the bias ratio \(p/q\) is identical at all sites. The assumptions \(p>q>0\) exclude degeneracies where strict rearrangement fails; reversing orientation treats \(q>p\).

## Proof
**Stationary flux and current.** Since \(\pi_i/r_i=1/R\), each clockwise edge carries stationary forward traffic \(p/R\) and backward traffic \(q/R\). Consequently every edge has net current \(\delta/R\). Summing the signed displacements of jumps around one period yields \(v=n\delta/R\). Summing current times the forward/backward traffic log ratio over the \(n\) bonds gives \(\sigma=n\delta\log(p/q)/R\).

**Exact corrector.** Write \(Q\) for the phase generator, \((Qh)_i=[p(h_{i+1}-h_i)+q(h_{i-1}-h_i)]/r_i\). Solve the finite irreducible Poisson equation \(Qh=v-\delta/r_i\), unique modulo a constant. Define \(u_i=1+h_{i+1}-h_i\). The equation becomes
\[
p u_i-q u_{i-1}=v r_i,\qquad \sum_{i=0}^{n-1}u_i=n.
\]
The corrected displacement \(X_T+h_{X_T\bmod n}-vT\) is a square-integrable martingale with clockwise increment \(u_i\) and counterclockwise increment \(-u_{i-1}\). Its predictable quadratic variation has stationary rate
\[
C=\frac1R\sum_i(pu_i^2+qu_{i-1}^2)=\frac1R\sum_i u_i^2.
\]
Since the correction is bounded, its contribution to the asymptotic variance vanishes. Existence and independence of the initial phase follow from finite-state ergodicity and the martingale central-limit variance calculation.

**Cyclic Green kernel.** Put \(w_i=b_i-m/n\) and \(z_i=u_i-1\). Then \(\sum_i z_i=0\) and
\[
(pI-qS^{-1})z=\frac{n\delta\varepsilon}{R}w,
\]
where \(S^{-1}\) shifts one coordinate backward. If \(K=[(pI-qS^{-1})^\top(pI-qS^{-1})]^{-1}\), direct multiplication (or a finite geometric series) gives its cyclic entries
\[
K_d=\frac{t^d+t^{n-d}}{\delta(1-t^n)},\quad 0\le d<n.
\]
(The formula includes \(d=0\).) Every row of \(K\) sums to \(\delta^{-2}\). Hence
\[
C=\frac nR+\frac{n^2\delta^2\varepsilon^2}{R^3}\left(\sum_{a,b\in B}K_{a-b}-\frac{m^2}{n\delta^2}\right).
\]
Separating the \(m\) diagonal and \(m(m-1)\) ordered off-diagonal terms gives the displayed variance formula.

**Global ordering.** List the slow sites cyclically and let their successive positive integer gaps be \(g_1,\ldots,g_m\), summing to \(n\). For each \(1\le k<m\), let \(d_i^{(k)}=g_i+\cdots+g_{i+k-1}\), with indices modulo \(m\). Then \(\sum_i d_i^{(k)}=kn\) and
\[
2\sum_{\{a,b\}\subset B}F(d_{ab})=\sum_{k=1}^{m-1}\sum_{i=1}^m F(d_i^{(k)}).
\]
Because \(0<t<1\), the function \(F(x)=t^x+t^{n-x}\) is strictly convex on \([0,n]\). Its sum over \(m\) integers of fixed total is least precisely when those integers differ by at most one. Thus the last displayed energy has a universal lower bound obtained by requiring, for every \(k\), all \(d_i^{(k)}\) to equal \(\lfloor kn/m\rfloor\) or \(\lceil kn/m\rceil\). The displayed mechanical pattern attains these requirements simultaneously: its ordered slow-site positions are \(x_j=\lfloor jn/m+\alpha\rfloor\), and all differences of positions \(k\) steps apart are the two required integers.

Conversely, an energy minimizer must attain the strict-convexity lower bound for every \(k\). Hence its slow-site positions satisfy \(x_j-x_i\in\{\lfloor (j-i)n/m\rfloor,\lceil (j-i)n/m\rceil\}\). The deviations \(x_i-in/m\) then have range strictly less than one. Choosing an intercept in the common intersection of intervals \([x_i-in/m,1+x_i-in/m)\) represents the positions as \(x_i=\lfloor in/m+\alpha\rfloor\). The rational mechanical configurations obtained by changing \(\alpha\) are cyclic rotations of each other (equivalently, the finite rational balanced-word conjugacy lemma, which follows by moving the intercept through the ordered residue classes of \(in/m\) modulo one). This proves the unique minimum up to rotation.

For the maximum, extend the energy to the real simplex \(g_i\ge1\), \(\sum_i g_i=n\). Each \(d_i^{(k)}\) is linear in the gap vector; the entire energy is strictly convex there, since the \(k=1\) contribution already contains \(\sum_iF(g_i)\). A strictly convex function has no nonvertex maximizer on a nontrivial segment. The simplex vertices have one gap \(n-m+1\) and all remaining gaps one, namely a consecutive block of \(m\) slow sites. All vertices are rotations of the same pattern. Strict convexity and the existence of another pattern when \(2\le m\le n-2\) give a strict maximum-to-minimum gap.

## Verification
The accompanying standalone \(\texttt{verify.py}\) uses exact rational arithmetic and independently solves the finite phase Poisson equation. It checked 336 generator/Poisson comparisons, all configurations in 56 nondegenerate size/particle-count/bias families for the asserted exact extrema, and 56 tests of unbiased and one-way ordering invariance. Execute \(\texttt{python3 verify.py}\) using only the Python standard library. These finite tests supplement rather than substitute for the analytic all-size proof.

For illustration, with \(n=6\), \(m=2\), \(r_0=\varepsilon=1\), \(p=3/4\), and \(q=1/4\), the opposite slow-site pair has \(C=81/104\), while consecutive slow sites have \(C=1161/1456\); both have drift \(3/8\) and entropy-production rate \((3/8)\log3\).

## Relationship to prior work
Derrida (1983) derived general exact drift/diffusion expressions for periodic one-dimensional hopping, and Koza (1999) developed a general characteristic-polynomial method for arbitrary periodic systems. Zhang (2009) studied limits of periodic hopping formulas. Guérin and Dean (2015) developed general non-equilibrium periodic dispersion formulas. These prior works supply broad transport results, so neither general computability of diffusion nor the bias/current formulas are claimed new. The present specialized conclusion is the exact positive cyclic pair-energy representation and the **unique, global binary-site-inventory extremizers** for every finite period under shared site-clock bias. The discrete convexity and balanced-word ingredients are classical; novelty is assessed only for their explicit coupling to this biased transport arrangement problem. No inspected source stated or directly resolved the fixed-inventory optimization; an unlocated equivalent rearrangement argument remains possible.

## Limitations
This is a single-particle periodic site-clock model. It does not cover unbiased strict extrema, spatially varying bias, edge-clock traps, many-particle exclusion, arbitrary multisets of more than two site rates, or time-dependent disorder. For \(p=q\) or one-way motion \(q=0\), placement cannot affect \(C\); these boundary observations do not extend the strict theorem. The evaluated formula alone is an instance of classical general transport theory; the claimed distinction is the global optimization, and its originality remains subject to independent literature verification.

## References
1. B. Derrida, *Velocity and diffusion constant of a periodic one-dimensional hopping model*, Journal of Statistical Physics **31** (1983), 433–450. DOI: 10.1007/BF01019492.
2. Z. Koza, *General technique of calculating drift velocity and diffusion coefficient in arbitrary periodic systems*, J. Phys. A **32** (1999), 7637–7651. arXiv:cond-mat/9909204.
3. Y. Zhang, *Limit properties of periodic one-dimensional hopping model*, arXiv:0906.3343 (2009).
4. T. Guérin and D. S. Dean, *Kubo formulas for dispersion in heterogeneous periodic non-equilibrium systems*, arXiv:1509.02733 (2015).
