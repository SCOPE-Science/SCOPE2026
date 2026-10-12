# A universal square-root covariance transition for two component sizes in weighted Cayley forests

## Finding

For a labeled vertex set \([n]=\{1,\ldots,n\}\), let a *rooted forest* mean a spanning acyclic undirected graph with one distinguished vertex (root) in every connected component. For a fixed parameter \(t>0\), give each rooted forest \(F\) probability proportional to \(t^{K(F)}\), where \(K(F)\) is its number of components. Let \(Z_k\) denote the number of components with exactly \(k\) vertices.

**Theorem (two-size covariance phase diagram).** For every integer \(n\geq3\), every pair of distinct integers \(1\leq k<\ell\leq n\), and every \(t>0\), the covariance \(\operatorname{Cov}_t(Z_k,Z_\ell)\) is strictly negative if \(k+\ell>n\). If \(k+\ell\leq n\), put \(m=n-k-\ell\) and
\[
R_{n;k,\ell}(t)
=\frac{(n-k)!(n-\ell)!}{n!\,m!}
\frac{(n+t)^{n-1}(m+t)^{m-1}}{(n-k+t)^{n-k-1}(n-\ell+t)^{n-\ell-1}}.
\]
The expression is valid also for \(m=0\), with \((m+t)^{m-1}=t^{-1}\). Then
\[
\operatorname{Cov}_t(Z_k,Z_\ell)
=\mathbb E_t Z_k\,\mathbb E_t Z_\ell\,[R_{n;k,\ell}(t)-1].
\]
For each feasible pair \(k+\ell\leq n\), the function \(t\mapsto R_{n;k,\ell}(t)\) decreases *strictly* from a value exceeding one (possibly infinite) to a limit strictly below one. Thus there is exactly one \(t_{n;k,\ell}>0\) with zero covariance; the covariance is positive for \(0<t<t_{n;k,\ell}\) and negative for \(t>t_{n;k,\ell}\).

Furthermore, for every fixed pair of distinct positive integers \(k<\ell\), as \(n\to\infty\),
\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{t_{n;k,\ell}}{\sqrt n}=\sqrt{\frac32}.}
\]
The limiting transition constant is independent of both specified component sizes. For the smallest feasible instance \((n,k,\ell)=(3,1,2)\), the exact transition is \(t_{3;1,2}=3/\sqrt2\).

## Assumptions and scope

All forests are rooted in every component, with exactly one root per component; the root choices are part of the random outcome. Edges on the complete graph have unit weight; the only tunable weight is the positive component fugacity \(t\). The labels are fixed, and no independent-edge random graph or unrooted uniform-forest law is asserted. No statement of independence of distinct component-size counts is made. The asymptotic limit fixes \(k\) and \(\ell\) before sending \(n\) to infinity; it does not cover growing component sizes.

## Proof

**1. Partition function and mixed moments.** Put \(\Phi_j(t)=\sum_F t^{K(F)}\) over rooted forests on \(j\) labeled vertices, with \(\Phi_0(t)=1\). Attach a new vertex to every root with an edge of weight \(t\). This bijects rooted forests on \([j]\) with trees on \(\{0,1,\ldots,j\}\) whose edges incident with the new vertex carry weight \(t\), other edges weight one. The weighted Matrix-Tree theorem gives a principal Laplacian minor \((j+t)I_j-J_j\), with eigenvalues \(t\) (once) and \(j+t\) (\(j-1\) times). Therefore, including \(j=0\) by the continuous algebraic convention,
\[
\Phi_j(t)=t(j+t)^{j-1} \quad (j\geq0,t>0),
\qquad \Phi_0(t)=1.
\]
A prescribed size-\(k\) vertex subset can carry \(k^{k-1}\) rooted labeled trees (Cayley), and the remaining labels carry any rooted forest. Thus for \(1\leq k\leq n\),
\[
\mathbb E_tZ_k={n\choose k}k^{k-1}t\frac{\Phi_{n-k}(t)}{\Phi_n(t)}>0.
\]
If \(k\ne\ell\) and \(k+\ell\leq n\), order the two distinguished disjoint component vertex sets and count their rooted trees independently:
\[
\mathbb E_t[Z_kZ_\ell]
={n\choose k}{n-k\choose\ell}k^{k-1}\ell^{\ell-1}t^2
\frac{\Phi_{n-k-\ell}(t)}{\Phi_n(t)}.
\]
If \(k+\ell>n\), this product is identically zero. Dividing the displayed mixed expectation by the product of the two means yields exactly \(R_{n;k,\ell}(t)\); its prefactor \((n-k)!(n-\ell)!/(n!m!)\) is strictly between zero and one.

**2. Monotonicity and endpoint signs.** For \(m=n-k-\ell\geq0\), direct differentiation gives
\[
\frac{\mathrm d}{\mathrm dt}\log R_{n;k,\ell}(t)
=-(t+1)\left[\frac1{t+n}+\frac1{t+m}
-\frac1{t+n-k}-\frac1{t+n-\ell}\right]<0.
\]
Indeed \(m<n-k,n-\ell<n\), the two inner arguments have the same sum as the two outer arguments, and \(x\mapsto (t+x)^{-1}\) is strictly convex. As \(t\to\infty\), \(R\) tends to the strict-subunit combinatorial prefactor.

At \(t\downarrow0\), if \(m=0\), its factor \(t^{-1}\) forces \(R\to\infty\). If \(m\geq1\), define \(a_j=j^{j-1}/j!\) for integers \(j\geq1\). Then
\[
\lim_{t\downarrow0}R_{n;k,\ell}(t)=\frac{a_n a_m}{a_{n-k}a_{n-\ell}}>1.
\]
To see the strict inequality, note that \(a_{j+1}/a_j=(1+1/j)^{j-1}\) increases strictly for integers \(j\geq1\), so \((a_j)\) is strictly log-convex from index one. The outer pair \((m,n)\) is strictly more spread than \((n-k,n-\ell)\), with equal total index sum. Strict log-convexity gives the asserted inequality. By continuity and strict monotonicity, a unique crossing exists with precisely the claimed covariance signs. For \(n=3,k=1,\ell=2\), the equation \(R=1\) reduces to \((t+3)^2=3t(t+2)\), giving \(t=3/\sqrt2\).

**3. Universal square-root transition.** Fix \(k<\ell\) and let \(t=c\sqrt n\) for a constant \(c>0\). For real \(x>0\) define
\[
H_t(x)=(x-1)\log(x+t)-\log\Gamma(x+1).
\]
The log-ratio equals the crossed second difference
\[
\log R_{n;k,\ell}(t)
=H_t(n)+H_t(n-k-\ell)-H_t(n-k)-H_t(n-\ell)
=\int_0^k\!\int_0^\ell H_t''(n-u-v)\,\mathrm dv\,\mathrm du.
\]
The identity also holds when \(m=0\), although the present asymptotic uses \(n>k+\ell\). Differentiation and the standard trigamma expansion \(\psi_1(x+1)=x^{-1}-(2x^2)^{-1}+O(x^{-3})\) give
\[
H_t''(x)=\frac{x+2t+1}{(x+t)^2}-\psi_1(x+1)
=\frac{x-t^2}{x(x+t)^2}+\frac1{2x^2}+O(x^{-3}).
\]
Uniformly for \(x\in[n-k-\ell,n]\) at \(t=c\sqrt n\),
\[
n^2 H_{c\sqrt n}''(x)\longrightarrow \frac32-c^2,
\quad\text{hence}\quad
\frac{n^2}{k\ell}\log R_{n;k,\ell}(c\sqrt n)
\longrightarrow \frac32-c^2.
\]
For any \(0<c_-<\sqrt{3/2}<c_+\), the ratios at \(c_-\sqrt n\) and \(c_+\sqrt n\) lie respectively above and below one for sufficiently large \(n\). The already established unique crossing lies between these parameters. Letting the brackets approach \(\sqrt{3/2}\) proves the limit.

## Verification

The standalone `verify.py` enumerates Prüfer codes for every labeled tree on \(n+1\) vertices, deletes the hub vertex, and measures component sizes directly, rather than generating forests via the analytic moment formulas. At each \(n=2,3,4,5,6\) and \(t\in\{1/2,1,2\}\), it independently aggregates exact rational weighted means and distinct-pair joint moments. It then compares all of them with the displayed formulas, along with each partition function. The recorded run passed 15 weighted cases and 180 exact-rational identity checks over 54,741 weighted tree cases. Use `python3 verify.py` from the directory containing this file; it requires only the Python standard library.

Finite checks are not used to establish strict monotonicity for all sizes or the universal asymptotic constant; the analytic arguments above do so.

## Relationship to prior work

The underlying component-weighted rooted-forest measure is standard: Pitman's 1996 report treats Cayley-type rooted-forest enumeration and coalescence; Avena and Gaudillière (first public preprint 2013, equations (1.6)–(1.10) and Section 6) formulate rooted-forest fugacity measures and root-set laws on general weighted graphs. D'Achille, Enriquez, and Melotti (first preprint 2024, particularly Theorem 1.1 and Lemma 3.2) study massive spanning forests on complete graphs, including single-root component geometry. Their weight projected to unrooted forests is exactly the present law, and none of these basic constructions, tree counts, or one-component formulas is asserted to be new.

The contribution asserted here is the *two-distinct-size* mixed moment comparison, its unique fugacity-induced covariance sign reversal for every feasible pair, and the universal \(\sqrt{3/2}\) crossover scale for all fixed distinct sizes. Root-set determinantal properties do not supply these size-count covariances; a local law for one distinguished component does not determine correlations between two different component counts. General partition-function machinery may make the finite moment evaluation derivable, so priority for the explicitly evaluated transition requires further independent historical scrutiny.

## Limitations

The covariance theorem concerns rooted forests on complete graphs, not uniform unrooted forests, independent-edge Erdős–Rényi forests, or arbitrary weighted underlying graphs. The critical point is defined implicitly and need not have a closed elementary form except for special parameters. The asymptotic is fixed-size only; no claim is made for \(k\) or \(\ell\) growing with \(n\). The result does not describe higher cumulants, multivariate Gaussian limits, or independent auditing. Classical forest-counting and recent general partition-function results may contain implicit derivations of the finite identity; this historical-priority uncertainty does not change the correctness of the stated elementary proof.

## References

1. J. Pitman, “Coalescent random forests,” Berkeley Statistics Technical Report 457, publicly dated 1996-09-01; https://statistics.berkeley.edu/tech-reports/457 (report abstract and archival metadata).
2. L. Avena and A. Gaudillière, “Random spanning forests, Markov matrix spectra and well distributed points,” arXiv:1310.1723v1, first public 2013-10-07; https://arxiv.org/html/1310.1723v4 (full text, Definitions 1.1 and Section 6).
3. M. D'Achille, N. Enriquez, P. Melotti, “Local limit of massive spanning forests on the complete graph,” arXiv:2403.11740v1, first public 2024-03-18; https://arxiv.org/html/2403.11740v1 (full text, component distribution and local limit).
