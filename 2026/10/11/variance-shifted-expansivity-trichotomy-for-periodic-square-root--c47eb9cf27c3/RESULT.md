# Variance-shifted expansivity trichotomy for periodic square-root weighted shifts

## Finding

A zero-mean periodic perturbation of size \(j^{-1/2}\) shifts the logarithmic drift of a unilateral weighted shift by precisely one-half of its period mean square. The sign of the corrected drift determines a **complete three-way orbit and expansivity classification**, although all spectra relevant to the motivating spectral comparison are identical throughout the family.

Fix any integer \(p\ge1\), a real \(0\le\alpha\le1\), and a real \(p\)-periodic sequence \((c_j)_{j\ge1}\) with \(\sum_{r=1}^{p}c_r=0\) and \(|c_r|\le1/2\). On the complex Hilbert space \(\ell^2(\mathbb N)\), with orthonormal basis \((e_j)\), set
\[
T e_j=w_j e_{j+1},\qquad w_j=1+\frac{\alpha}{j}+\frac{c_j}{\sqrt j},\quad
v=\frac1p\sum_{r=1}^{p}c_r^2,\qquad \delta=\alpha-\frac v2.
\]
For \(P_{k,n}=\prod_{j=k}^{k+n-1}w_j\), where \(P_{k,0}=1\), there is a finite parameter-dependent \(C\) such that for **every** \(k\ge1\), \(n\ge0\),
\[
\left|\log P_{k,n}-\delta\log\frac{k+n}{k}\right|\le \frac{C}{\sqrt k}.
\tag{1}
\]
For each fixed \(k\), \(P_{k,n}/((k+n)/k)^\delta\) converges to a number \(L_k\in(0,\infty)\), with \(|\log L_k|\le C/\sqrt k\).

The exact alternatives are: **(a)** if \(\delta>0\), then \(\|T^nx\|\to\infty\) for every \(x\ne0\); \(T\) is positively expansive and strongly asymptotically expansive; **(b)** if \(\delta<0\), then \(T^nx\to0\) for every \(x\), but \(T\) is not strongly asymptotically expansive; **(c)** if \(\delta=0\), then for each \(x\ne0\),
\[
\lim_{n\to\infty}\|T^nx\|=\left(\sum_{k\ge1}|x_k|^2L_k^2\right)^{1/2}\in(0,\infty),
\]
so \(T\) is not asymptotically expansive. In every case,
\[
\sigma(T)=\overline{\mathbb D},\quad
\sigma_{\mathrm p}(T)=\varnothing,\quad
\sigma_{\mathrm{ap}}(T)=\{z\in\mathbb C:|z|=1\}.
\tag{2}
\]
Therefore no member is hyperbolic or super asymptotically expansive. For \(c_j=(-1)^j\beta\), \(|\beta|\le1/2\), the phase boundary is the explicit parabola \(\alpha=\beta^2/2\).

## Assumptions and scope

The Hilbert space is complex, the shift is unilateral and acts on indices \(j\ge1\), \(p\) is any positive integer, and \(n\) includes zero. The point spectrum and approximate point spectrum are those of the bounded operator on this Hilbert space. Positive expansivity means that each nonzero vector has unbounded forward orbit. Asymptotic expansivity means every bounded forward orbit tends to zero; strong asymptotic expansivity requires that decay to be uniform on a fixed positive-radius set of vectors whose full forward orbits stay within that radius. Super asymptotic expansivity has the definition in Bag--Mandal--Das, Definition 3.3, and equals hyperbolicity by their result. All weights are strictly positive because \(w_j\ge1-1/(2\sqrt j)\ge1/2\); boundedness also holds.

## Proof

**Uniform product law.** Put \(u_j=\alpha/j+c_j/\sqrt j\). For all sufficiently large \(j\), Taylor's formula, uniformly for the bounded periodic coefficients, yields
\[
\log(1+u_j)=\frac{c_j}{\sqrt j}+\frac{\alpha-c_j^2/2}{j}+O_{\alpha,c}(j^{-3/2}).
\tag{3}
\]
By periodicity and zero mean, the partial sums of \(c_j\) are uniformly bounded. The partial sums of \(c_j^2-v\) are also uniformly bounded. Abel summation thus gives, uniformly in \(n\ge0\),
\[
\left|\sum_{j=k}^{k+n-1}\frac{c_j}{\sqrt j}\right|\le \frac{C_1}{\sqrt k},\quad
\left|\sum_{j=k}^{k+n-1}\frac{c_j^2-v}{j}\right|\le\frac{C_2}{k}.
\tag{4}
\]
The Taylor remainders sum to \(O_{\alpha,c}(k^{-1/2})\), while integral comparison gives \(\sum_{j=k}^{k+n-1}j^{-1}=\log((k+n)/k)+O(k^{-1})\). Combining (3)--(4) produces (1) for large \(k\). The finitely many smaller indices can be absorbed by enlarging \(C\), since all \(w_j>0\). Each series used in (3)--(4) has a convergent tail for fixed \(k\) (Dirichlet or absolute convergence), as does the harmonic-number/logarithm correction. Therefore the correction in (1) has a finite real limit, giving the stated \(L_k\) and its bounds. In particular,
\[
e^{-C/\sqrt k}\left(\frac{k+n}{k}\right)^\delta
\le P_{k,n}\le
e^{C/\sqrt k}\left(\frac{k+n}{k}\right)^\delta.
\tag{5}
\]

**Orbit classes.** The images \(T^ne_k=P_{k,n}e_{k+n}\) are mutually orthogonal as \(k\) varies, so for every \(x=(x_k)\in\ell^2\),
\[
\|T^nx\|^2=\sum_{k\ge1}|x_k|^2P_{k,n}^2.
\tag{6}
\]
If \(\delta>0\), any nonzero coordinate \(x_k\) contributes a term tending to infinity by (5); thus every nonzero orbit norm tends to infinity. There is then no nonzero bounded orbit, proving positive and strong asymptotic expansivity directly from the definitions. If \(\delta<0\), each \(P_{k,n}\to0\), while (5) gives the uniform bound \(P_{k,n}\le e^C\). Dominated convergence in (6) proves \(T^nx\to0\) for every \(x\), hence asymptotic expansivity. Yet strong asymptotic expansivity fails: fix an arbitrary radius \(r>0\). For every \(n\), choose \(k_n\) so large that \(P_{k_n,n}>1/2\), possible since \(w_j\to1\). Then \(x^{(n)}=r e_{k_n}/e^C\) satisfies \(\|T^m x^{(n)}\|\le r\) for all \(m\ge0\), but \(\|T^n x^{(n)}\|>r/(2e^C)\). Uniform decay fails for every radius. If \(\delta=0\), (5) uniformly bounds \(P_{k,n}\), and \(P_{k,n}\to L_k>0\). Dominated convergence in (6) proves the stated strictly positive finite limit for every nonzero \(x\). Rescaling any such vector into an arbitrary observation radius disproves asymptotic expansivity.

**Identical spectra.** Write \(S e_j=e_{j+1}\) for the unweighted unilateral shift. Since \(w_j\to1\), \(T-S\) is compact (a norm limit of finite-rank weighted shifts). The spectral radius is one: (5) gives \(\|T^n\|\le e^C\max\{1,(n+1)^\delta\}\), while for every fixed \(n\), \(P_{k,n}\to1\) as \(k\to\infty\), so \(\|T^n\|\ge1\). Thus \(\sigma(T)\subseteq\overline{\mathbb D}\). For \(|z|<1\), \(S-zI\) is Fredholm of index \(-1\) and \(T-zI\) has the same index under compact perturbation. The weighted shift \(T\) has no eigenvalues: for \(z\ne0\), the coordinate-one equation in \(Tx=zx\) forces \(x_1=0\) and induction forces all coordinates zero; for \(z=0\), injectivity follows from positive weights. Hence \(T-zI\) is an injective Fredholm operator of index \(-1\): it has proper closed range. Therefore every \(|z|<1\) is in the spectrum but not in the approximate point spectrum. For \(|z|=1\), normalized vectors supported on arbitrarily long blocks far out, with coordinates proportional to \(z^{-j}\), satisfy \(\|(S-zI)x\|\to0\), while \(\|(T-S)x\|\to0\) as the block moves to infinity. Thus every boundary point is approximate, proving (2). The full spectrum meets the unit circle, so no shift in this family is hyperbolic; by the cited equivalence, none is super asymptotically expansive.

## Verification

The included `check_weight_phase.py` implements the weights directly using positive `log1p` evaluations and checks finite log-product corrections against \(\delta\log((k+n)/k)\) in 28 independent period/parameter/start-index cases with lengths 100, 1,000 and 5,000. Cases include zero perturbation, two-point alternation on both sides and at the critical curve, and three- and four-point zero-mean periods. The test prints the residuals and passed when run with Python 3. Its finite checks support arithmetic and normalization only; (1)--(2) and the infinite dynamical classification are proved analytically above.

## Relationship to prior work

Bag, Mandal and Das introduce and distinguish asymptotic, strong asymptotic and super asymptotic expansivity. Their Example 4.2 treats one telescoping contracting shift, and Example 4.4 compares the unweighted shift with that example to show that point, approximate-point and full spectra alone do not characterize asymptotic expansivity. They do not state the periodic square-root perturbation law (1), its mean-square threshold, or the three-region classification. Bernardes Jr., Cirilo, Darji, Messaoudi and Pujals characterize positive expansivity of unilateral weighted shifts via unbounded products (Theorem E and Remark 32): the positive-expansive branch here agrees with this general criterion **once (1) is supplied**, so the broad product criterion and the spectrum-blindness observation are not claimed as new. Related weighted-shift literature treats uniform or average expansivity rather than the exact strong/asymptotic trichotomy with periodic \(j^{-1/2}\) modulation. The new content is the uniform quantitative product estimate and the resulting complete variance-controlled orbit phase diagram.

## Limitations

The result is for unilateral Hilbert-space shifts with a fixed finite period, bounded real zero-mean modulation and the specified critical \(j^{-1/2}\) size; it is not a criterion for arbitrary weight sequences or arbitrary Banach spaces. It does not classify scalar rescalings, mixtures of stable and unstable invariant subspaces, or the geometry of every spectral subset. The phase boundary depends on the empirical period mean square, not on a stochastic variance theorem. The full-history and literature comparisons do not prove global uniqueness, and an unindexed equivalent characterization in weighted-shift theory remains a residual originality risk. No external independent audit or validation has been performed.

## References

1. P. Bag, P. N. Mandal and P. K. Das, *Asymptotic Expansive and Hyperbolic Linear Operators*, arXiv:2610.01196v1 (first public 2026-10-01), especially Definitions 3.1--3.3, Examples 4.2 and 4.4, and Open Questions.
2. N. C. Bernardes Jr., P. R. Cirilo, U. B. Darji, A. Messaoudi and E. R. Pujals, *Expansivity and Shadowing in Linear Dynamics*, J. Math. Anal. Appl. 461 (2018), 796--816; arXiv:1612.02921, especially Theorem E and Remark 32. DOI: 10.1016/j.jmaa.2017.11.059.
3. *On notions of expansivity for operators on locally convex spaces*, RACSAM (2026), DOI: 10.1007/s13398-026-01840-6, relevant sections on average and uniformly expansive weighted shifts.
