# Exact essential norm for slowly oscillating generalized Hilbert matrices on \(\ell^p\)

## Finding

Fix \(1<p<\infty\), \(-1/p<\gamma<1-1/p\), and a bounded complex sequence \(g=(g_k)_{k\ge1}\). Write \(w_k=|g_k|\), and suppose that \(w\) is *multiplicatively slowly oscillating* in the following precise sense:
\[
\forall R>1:\quad\lim_{N\to\infty}\sup_{\substack{m,n\ge N\\R^{-1}\le m/n\le R}}|w_m-w_n|=0.
\]
For \(x\in\ell^p(\mathbb N)\), define the generalized Hilbert matrix operator
\[
(H_{g,\gamma}x)_k=g_k\sum_{n=1}^{\infty}\frac{(k/n)^\gamma x_n}{k+n},\qquad k\ge1.
\]
Its exact essential norm, i.e. its distance to compact linear operators on \(\ell^p(\mathbb N)\), is
\[
\boxed{\|H_{g,\gamma}\|_{\mathrm{ess}}=\frac{\pi}{\sin(\pi(1/p+\gamma))}\,\limsup_{k\to\infty}|g_k|.}
\]
In particular, \(H_{g,\gamma}\) is compact if and only if \(g_k\to0\) in modulus. This does not require convergence of its block means. For example, the positive sequence
\[
g_k=1+\sin(\log\log(k+e)),\qquad k\ge1,
\]
has \(\liminf g_k=0\), \(\limsup g_k=2\), and \(\|H_{g,\gamma}\|_{\mathrm{ess}}=2\pi/\sin(\pi(1/p+\gamma))\).

## Assumptions and scope

All spaces are over the complex scalars, \(\mathbb N=\{1,2,\dots\}\), and \(1<p<\infty\). The parameter interval \(-1/p<\gamma<1-1/p\) is open. The sequence \(g\) need not have a limit; even its phases may oscillate arbitrarily because only \(|g_k|\) appears in output norms. Boundedness of \(g\) is an explicit hypothesis. The slow-oscillation condition is uniform for each fixed multiplicative window, with no uniformity claimed as \(R\to\infty\). Set \(a=\gamma+1/p\in(0,1)\) and
\[
C_{p,\gamma}=\int_0^\infty\frac{t^{-a}}{1+t}\,dt
=\int_0^\infty\frac{t^{a-1}}{1+t}\,dt
=\frac{\pi}{\sin(\pi a)}.
\]

## Proof

**1. A sharp universal upper bound.** Let \(H_\gamma=H_{1,\gamma}\), with strictly positive kernel \(h_{kn}=(k/n)^\gamma/(k+n)\). Choose Schur weights \(u_n=n^{-1/p}\) and \(v_n=u_n^{p-1}=n^{-1/p'}\). Because \(0<a<1\), each positive function \(t^{-a}/(k+t)\) and \(t^{a-1}/(n+t)\) is decreasing in \(t>0\). Comparison of sums with integrals gives, for every positive integer \(k,n\),
\[
(H_\gamma u)_k=k^\gamma\sum_{n\ge1}\frac{n^{-a}}{k+n}
\le k^\gamma\int_0^\infty\frac{t^{-a}}{k+t}\,dt
=C_{p,\gamma}u_k
\]
and
\[
(H_\gamma^*v)_n=n^{-\gamma}\sum_{k\ge1}\frac{k^{a-1}}{n+k}
\le n^{-\gamma}\int_0^\infty\frac{t^{a-1}}{n+t}\,dt
=C_{p,\gamma}v_n.
\]
For finitely supported \(x\), Hölder yields
\[
|(H_\gamma x)_k|^p\le (H_\gamma u)_k^{p-1}
\sum_n h_{kn}|x_n|^p/u_n^{p-1}.
\]
Multiplying out the bounds above, summing over \(k\), and using the adjoint inequality proves \(\|H_\gamma x\|_p\le C_{p,\gamma}\|x\|_p\), hence the same inequality for all \(x\) by density. As \(H_{g,\gamma}=M_gH_\gamma\), it is bounded. If \(P_N\) is the coordinate projection onto the first \(N\) output entries, \(P_NH_{g,\gamma}\) has finite rank, while
\[
\|H_{g,\gamma}-P_NH_{g,\gamma}\|
\le C_{p,\gamma}\sup_{k>N}|g_k|.
\]
Consequently \(\|H_{g,\gamma}\|_{\mathrm{ess}}\le C_{p,\gamma}L\), where \(L=\limsup_{k\to\infty}w_k\).

**2. Logarithmic test vectors.** Fix real numbers \(0<A<T\), and for positive integers \(N\) set
\[
x_n^{(N,T)}=n^{-1/p}\mathbf{1}_{\{Ne^{-T}\le n\le Ne^T\}}.
\]
Then \(\|x^{(N,T)}\|_p^p=\sum_{Ne^{-T}\le n\le Ne^T}n^{-1}\to2T\). Introduce the positive integrable function
\[
\kappa_a(t)=\frac{e^{(1-a)t}}{1+e^t},\qquad C_A=\int_{-A}^{A}\kappa_a(t)\,dt.
\]
For every output index \(k\), direct algebra gives the exact identity
\[
k^{1/p}(H_\gamma x^{(N,T)})_k
=\sum_{Ne^{-T}\le n\le Ne^T}\frac1n\,
\kappa_a\bigl(\log(n/k)\bigr).
\]
When \(N\to\infty\), these are Riemann sums for \(\int_{-T}^{T}\kappa_a(y-\log(k/N))\,dy\); convergence is uniform for \(Ne^{-T+A}\le k\le Ne^{T-A}\), because all scaled variables range over fixed compact subsets of \((0,\infty)\) and the integrands there are smooth. For every such \(k\), the integration interval contains \([-A,A]\), so
\[
(H_\gamma x^{(N,T)})_k\ge k^{-1/p}(C_A-o_{N\to\infty}(1)),
\]
where the error is uniform on the specified output interval.

**3. Compact-operator obstruction.** Choose integers \(N_j\to\infty\) with \(w_{N_j}\to L\). By multiplicative slow oscillation, for the *fixed* window \([e^{-T+A},e^{T-A}]\) one has \(w_k\ge L-o_{j\to\infty}(1)\) uniformly when \(N_je^{-T+A}\le k\le N_je^{T-A}\). Since also \(\sum_{N_je^{-T+A}\le k\le N_je^{T-A}}k^{-1}\to2(T-A)\), the preceding bound implies
\[
\liminf_{j\to\infty}\frac{\|H_{g,\gamma}x^{(N_j,T)}\|_p}
{\|x^{(N_j,T)}\|_p}
\ge L C_A\left(\frac{T-A}{T}\right)^{1/p}.
\]
The normalized vectors are weakly null: they are uniformly bounded and their supports escape every finite initial coordinate set; reflexivity of \(\ell^p\) gives the result directly by duality with \(\ell^{p'}\). Thus every compact operator sends them to norm-null sequences. For an arbitrary compact \(K\), its subtraction cannot reduce the liminf above, whence \(\|H_{g,\gamma}\|_{\mathrm{ess}}\ge L C_A((T-A)/T)^{1/p}\). With \(A\) fixed let \(T\to\infty\), and then let \(A\to\infty\). Since \(C_A\nearrow C_{p,\gamma}\), the lower bound is \(L C_{p,\gamma}\). Together with Step 1 this proves the boxed identity.

**4. Nonconvergent exact example.** For \(g_k=1+\sin(\log\log(k+e))\), the logarithmic argument varies by \(o(1)\) uniformly when both indices tend to infinity with bounded ratio; therefore \(|g_k|=g_k\) is multiplicatively slowly oscillating. The increasing unbounded argument has successive increments tending to zero, so the sine values approach both extrema along integer subsequences. In particular \(\limsup g_k=2\) and \(\liminf g_k=0\). For the partition \(d_j=j^2\), the average \(G_j\) of \(|g_k|^p\) on \([j^2,(j+1)^2)\) differs from \(g_{j^2}^p\) by \(o(1)\). Its limsup is \(2^p\) and liminf is zero, so \(G_j\) has no limit even though the exact essential norm is determined here.

## Verification

The proof uses only positive-kernel Schur estimates, the Euler beta integral, uniform Riemann-sum convergence on fixed multiplicative windows, and a weakly null lower-bound sequence. As a normalization check, at \(p=2\), \(\gamma=0\), the constant is \(\pi\), the classical Hilbert matrix norm. Both signs of \(\gamma\) are handled because \(a\in(0,1)\) makes each of the two comparison functions decreasing. The formula is unaffected by phase changes in \(g\). No finite-dimensional numerical computation is used to infer an infinite-dimensional conclusion.

## Relationship to prior work

David Norrbo, *The essential norm, block sizes, and some Generalized Hilbert operators on \(\ell^p\)*, arXiv:2609.13403v1 (first public 11 September 2026), Theorem 2, computes this constant when the short relative-width block means of \(|g|^p\) **converge**; Proposition 1 gives the unweighted sharp Hilbert matrix constant. Its main theorem statements do not give the boxed equality for oscillatory, nonconvergent means. The example above specifically violates that convergence hypothesis. Norrbo also obtains comparability using exponentially growing blocks, which is weaker than this exact slowly oscillating formula. The operator on \(\ell^p\) here is not the same as generalized Hilbert integral operators generated by measures on \([0,1]\) considered by Athanasiou, nor the Hilbert operators on analytic Hardy/Bergman spaces treated by Lindström, Miihkinen, and Norrbo. The proof is self-contained and credits the classical Schur and beta-integral ingredients.

## Limitations

The proof does not compute the essential norm for arbitrary bounded weights lacking multiplicative slow oscillation. No claim is made about nonlinear maps, other exponent endpoints, or spectral invariants. The closest preprint's theorem statements and early proof sections have been inspected; later proof pages were not materially examined, leaving a literature-overlap risk that another formulation there or in general Mellin limit-operator theory already implies this special case. No assertion is made that unindexed work lacks an equivalent formulation.

## References

1. D. Norrbo, *The essential norm, block sizes, and some Generalized Hilbert operators on \(\ell^p\)*, arXiv:2609.13403v1 (11 September 2026), especially Theorem 2 and Proposition 1. https://arxiv.org/abs/2609.13403
2. N. Athanasiou, *On the boundedness and norm of certain generalized Hilbert operators in \(\ell^p\)*, *Bulletin of the London Mathematical Society* 55 (2023), 2598–2610, doi:10.1112/blms.12882. https://doi.org/10.1112/blms.12882
3. M. Lindström, S. Miihkinen, D. Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, *Advances in Mathematics* 408 (2022), 108598, doi:10.1016/j.aim.2022.108598. https://arxiv.org/abs/2201.09591
