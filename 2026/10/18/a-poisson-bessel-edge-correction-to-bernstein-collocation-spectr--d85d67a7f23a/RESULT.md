# A Poisson–Bessel edge correction to Bernstein collocation spectral energy

## Finding
For every integer \(n\geq1\), let the real equispaced Bernstein collocation matrix \(B_n\) have entries
\[
(B_n)_{jk}=\binom nk\left(\frac jn\right)^k\left(1-\frac jn\right)^{n-k},\qquad 0\leq j,k\leq n,
\]
with the usual endpoint convention that the Bernstein basis has value \(1\) in its unique nonzero position at each endpoint. Write its squared Hilbert–Schmidt energy as
\[
E_n=\operatorname{tr}(B_nB_n^{\mathsf T})=\sum_{j=0}^n\sum_{k=0}^n(B_n)_{jk}^{2}.
\]
Then, as \(n\to\infty\),
\[
\boxed{E_n=\frac{\sqrt{\pi n}}2+\mathcal C_{\mathrm B}+O(n^{-1/7}),}
\]
where the finite, absolutely convergent boundary constant is
\[
\boxed{\mathcal C_{\mathrm B}=2+\frac{\zeta(1/2)}{\sqrt\pi}
+2\sum_{j=1}^{\infty}\left[e^{-2j}I_0(2j)-\frac1{\sqrt{4\pi j}}\right].}
\]
Here \(I_0\) is the modified Bessel function defined by
\[
I_0(z)=\sum_{r=0}^{\infty}\frac{(z/2)^{2r}}{(r!)^2},
\]
and \(\zeta\) denotes the analytic continuation of the Riemann zeta function. Numerically \(\mathcal C_{\mathrm B}\approx1.2903\). The error constant is universal, independent of the integer \(n\).

## Assumptions and scope
The assertion concerns the specific \((n+1)\times(n+1)\) matrix built from the degree-\(n\) Bernstein polynomial basis evaluated at the complete uniform mesh (including both endpoints). It is a real matrix acting between Euclidean coefficient spaces with their unweighted counting-measure norms. Neither individual singular values nor any other node distribution is asserted to satisfy this expansion. The auxiliary estimates below apply for all real \(x\in[0,1]\), with the stated restriction on the positive variance scale. The displayed asymptotic is an infinite sequence statement, and the finite tests below are not part of its proof.

## Proof
**1. Exact collision integral.** Put
\[
r_n(x)=\sum_{k=0}^{n}\binom nk^2x^{2k}(1-x)^{2(n-k)}.
\]
By Parseval applied to \(((1-x)+xe^{it})^n\),
\[
r_n(x)=\frac1\pi\int_0^\pi\bigl(1-4x(1-x)\sin^2(t/2)\bigr)^n\,dt.
\tag{1}
\]
Consequently \(E_n=\sum_{j=0}^{n}r_n(j/n)\), and the endpoint contribution is exactly \(r_n(0)+r_n(1)=2\).

**2. Uniform Gaussian approximation away from the two mesh endpoints.** Set \(u=nx(1-x)\). There exists an absolute constant \(C\) for which
\[
\left|r_n(x)-\frac1{\sqrt{4\pi u}}\right|\leq C u^{-3/2},\qquad u\geq\tfrac12.
\tag{2}
\]
For verification, in (1) set \(q=4x(1-x)\sin^2(t/2)\), so that \(nq=4u\sin^2(t/2)\). Since \(x(1-x)\leq1/4\), one has \(n\geq4u\). On \(q\leq1/2\), the elementary logarithmic inequality
\[
0\leq e^{-nq}-(1-q)^n\leq nq^2e^{-nq}
\]
holds. Using \(\sin(t/2)\leq t/2\), \(\sin(t/2)\geq t/\pi\) on \([0,\pi]\), and \(n\geq4u\), the integral of this difference is at most
\[
\frac{u}{4\pi}\int_0^\pi t^4 e^{-4ut^2/\pi^2}\,dt=O(u^{-3/2}).
\]
On \(q>1/2\), the difference is bounded by \(e^{-n/2}\leq e^{-2u}=O(u^{-3/2})\). Moreover, on \([0,\pi]\),
\[
0\leq t^2-4\sin^2(t/2)\leq t^4/12.
\]
The mean-value bound for the exponential gives
\[
\int_0^\pi\left|e^{-4u\sin^2(t/2)}-e^{-ut^2}\right|dt
\leq\frac u{12}\int_0^\pi t^4 e^{-4ut^2/\pi^2}\,dt=O(u^{-3/2}).
\]
Finally, the tail \(\int_\pi^\infty e^{-ut^2}dt=O(u^{-3/2})\) for \(u\geq1/2\), and \(\pi^{-1}\int_0^\infty e^{-ut^2}dt=(4\pi u)^{-1/2}\). This proves (2), without assuming a pointwise central limit theorem near the boundaries.

**3. Endpoint Poisson limit and a summable domination.** For each positive integer \(j\), define
\[
g_j=\frac1{\sqrt{4\pi j}},\qquad q_j=e^{-2j}I_0(2j).
\]
The Poisson generating function/Parseval identity gives
\[
q_j=\sum_{k=0}^{\infty}\left(e^{-j}\frac{j^k}{k!}\right)^2
=\frac1\pi\int_0^\pi e^{-4j\sin^2(t/2)}dt.
\]
The Gaussian comparison in step 2 (applied directly to the last exponential integral) implies \(|q_j-g_j|\leq Cj^{-3/2}\). Hence \(\sum_j(q_j-g_j)\) converges absolutely.

For \(1\leq j\leq n-1\), let \(u_{n,j}=j(1-j/n)\) and \(g_{n,j}=(4\pi u_{n,j})^{-1/2}\). Then \(u_{n,j}\geq\frac12\min\{j,n-j\}\), and (2) yields
\[
|r_n(j/n)-g_{n,j}|\leq C\min\{j,n-j\}^{-3/2}.
\tag{3}
\]
For \(j\leq n/2\), coupling the \(n\) Bernoulli\((j/n)\) variables with independent Poisson\((j/n)\) variables gives
\[
d_{\mathrm{TV}}(\operatorname{Bin}(n,j/n),\operatorname{Poi}(j))\leq \frac{j^2}{n}.
\]
A collision functional \(\sum p_k^2\) changes by at most four times total variation. It follows that
\[
|r_n(j/n)-q_j|\leq 4j^2/n,
\qquad |g_{n,j}-g_j|\leq C\sqrt j/n.
\tag{4}
\]
For \(K\leq n/2\), symmetry in \(j\leftrightarrow n-j\), (3), (4), and \(\sum_{j>K}j^{-3/2}=O(K^{-1/2})\) together imply
\[
\sum_{j=1}^{n-1}\bigl(r_n(j/n)-g_{n,j}\bigr)
=2\sum_{j=1}^{\infty}(q_j-g_j)
+O\left(K^{-1/2}+K^3/n+K^{3/2}/n\right).
\tag{5}
\]
The potential middle index when \(n\) is even is included in the summable tail. Choose \(K=\lfloor n^{2/7}\rfloor\) for sufficiently large \(n\). Equation (5) then has error \(O(n^{-1/7})\).

**4. The singular bulk Riemann sum.** Set \(f(x)=[x(1-x)]^{-1/2}\) and
\[
h(x)=f(x)-x^{-1/2}-(1-x)^{-1/2}.
\]
The function \(h\) extends continuously to the closed interval, and its derivative is integrable there because its endpoint singularities are only of order \(x^{-1/2}\) and \((1-x)^{-1/2}\). Hence the corresponding Riemann sum differs from its integral by \(O(1)\). Since \(\int_0^1 f(x)dx=\pi\) and \(\int_0^1 x^{-1/2}dx=2\), while
\[
\sum_{j=1}^{n-1}j^{-1/2}=2\sqrt n+\zeta(1/2)+O(n^{-1/2}),
\]
we obtain
\[
\sum_{j=1}^{n-1}g_{n,j}
=\frac1{2\sqrt{\pi n}}\sum_{j=1}^{n-1}f(j/n)
=\frac{\sqrt{\pi n}}2+\frac{\zeta(1/2)}{\sqrt\pi}+O(n^{-1/2}).
\tag{6}
\]
Combining the two endpoints, (5), and (6) proves the displayed formula, with the slower of the two errors equal to \(O(n^{-1/7})\). The proof also shows that the constant is an explicit sum of the endpoint mass, the singular-mesh zeta correction, and the two Poisson collision boundary layers. \(\square\)

## Verification
Run `python3 bernstein_collocation_check.py` with the Python standard library; the checker computes small matrices exactly as rational numbers, independently compares double-precision row energy, checks five Poisson collision integrals against their defining series, and displays convergence of \(E_n-\sqrt{\pi n}/2\). Its 12 rational/numeric comparisons and the numerical limit provide diagnostic checks; the analytical derivation (1)–(6), not finite tests, proves the asymptotic. The computed correction approaches about \(1.2903\). Reproducibility requires only the embedded script. All constants hidden by \(O(\cdot)\) are absolute and no explicit best constant is claimed.

## Relationship to prior work
Marco and Martínez treat stable computation and factorization of Bernstein–Vandermonde matrices, including their singular values, but do not state the specific equispaced-mesh Frobenius energy correction [1,2]. Raşa identifies the pointwise binomial coincidence function, its special-function representations and estimates [3,4], and later establishes pointwise log-convexity [5]. Măduţa, Otrocol and Raşa provide recurrences and pointwise inequalities for the same coincidence function [6]. Those identities furnish the natural starting point but neither compute the complete sum at \(x=j/n\) nor give the two-term boundary-corrected asymptotic and power-rate estimate proved here. Priority relative to unindexed sources is not certified.

## Limitations
Only equispaced collocation in the unweighted Euclidean coefficient norm is treated. The rate \(n^{-1/7}\) is not asserted sharp. The coefficient \(\mathcal C_{\mathrm B}\) is defined exactly by an absolutely convergent series; its decimal approximation is illustrative, not an interval certificate. The finding does not provide the spectral measure, condition number, individual singular values, or analogous formulas for nonuniform nodes. Bibliographic equivalences under other matrix terminology remain possible.

## References
[1] A. Marco and J.-J. Martínez, *Accurate numerical linear algebra with Bernstein–Vandermonde matrices*, arXiv:0812.3115v1 (2008), https://arxiv.org/abs/0812.3115 .

[2] A. Marco and J.-J. Martínez, *Accurate computations with totally positive Bernstein–Vandermonde matrices*, Electronic Journal of Linear Algebra (2013), https://journals.uwyo.edu/index.php/ela/article/download/1251/1251/1251 .

[3] I. Raşa, *Special functions associated with positive linear operators*, arXiv:1409.1015v1 (2014), https://arxiv.org/abs/1409.1015 .

[4] I. Raşa, *Rényi entropy and Tsallis entropy associated with positive linear operators*, arXiv:1412.4971v1 (2014), https://arxiv.org/pdf/1412.4971 .

[5] I. Raşa, *The index of coincidence for the binomial distribution is log-convex*, arXiv:1706.05178v1 (2017), https://arxiv.org/pdf/1706.05178 .

[6] A. Măduţa, D. Otrocol and I. Raşa, *Inequalities for indices of coincidence and entropies*, arXiv:1910.13491v1 (2019), https://arxiv.org/pdf/1910.13491 .
