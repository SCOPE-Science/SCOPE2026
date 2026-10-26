# Sharp orbit-kernel aliasing and critical sparsity in weighted Bergman spaces

## Finding
Fix \(\alpha>-1\), put \(\beta=\alpha+2>1\), and let \(A^2_\alpha\) be the weighted Bergman Hilbert space on the unit disk, with probability-normalized area weight \((\alpha+1)(1-|z|^2)^\alpha/\pi\). For positive integers \(N,m\) and \(0<r<1\), project the unit monomial \(e_N(z)=\sqrt{c_N}z^N\), where \(c_j=(\beta)_j/j!\), onto the span \(V_{m,r}\) of the \(m\) reproducing kernels at \(r\exp(2\pi i h/m)\), \(0\le h<m\). Let \(M_{N,m}\) be the supremum of the squared projection norm as \(r\) varies.

**Exact finite-degree law.** With \(s=r^2\) and \(\ell\) the residue of \(N\) modulo \(m\),
\[
\|\Pi_{V_{m,r}}e_N\|^2=\frac{c_Ns^N}{\displaystyle\sum_{j\ge0,\ j\equiv N\ ({\rm mod}\ m)}c_js^j}.
\]
For \(m\le N\), this fraction has exactly one maximizer \(s\in(0,1)\); for \(m>N\), its supremum is \(1\), approached as \(r\downarrow0\) but not attained at a positive radius.

**Sharp sparsity laws.** For sequences of positive integers \(m=m_N\), with \(\beta\) fixed:

1. If \(m/N\to0\), then
\[
\frac{N}{m}M_{N,m}\longrightarrow\frac{\beta^\beta e^{-\beta}}{\Gamma(\beta)},\qquad -N\log s_{N,m}\longrightarrow\beta,
\]
where \(s_{N,m}\) is the unique maximizing squared radius.

2. If \(m/N\to c\in(0,1)\), then \(M_{N,m}\to\mathcal M_\beta(c)\in(0,1)\). Explicitly,
\[
\mathcal M_\beta(c)=\max_{t>0}\frac{e^{-t}}{\displaystyle\sum_{k\in\mathbb Z:\,1+kc>0}(1+kc)^{\beta-1}e^{-t(1+kc)}}.
\]
The maximizer \(t_{\beta,c}\) is unique, and \(-N\log s_{N,m}\to t_{\beta,c}\).

3. If \(m/N\to1\) with \(m\le N\), writing \(\ell=N-m\) and \(a_N=c_\ell/c_N\), then \(a_N\to0\) and the exact leading deficit is
\[
1-M_{N,m}\sim \frac{2\sqrt{c_\ell c_{N+m}}}{c_N}\sim2^{(\beta+1)/2}\sqrt{\frac{c_\ell}{c_N}}.
\]
In particular, \(M_{N,m}\to1\). If eventually \(m>N\), the exact supremum already equals \(1\).

All assertions concern the specified **equal-radius regular-polygon kernel dictionary**, not the unconstrained best \(m\)-kernel approximation over arbitrary node locations.

## Assumptions and scope
The normalized reproducing kernel is \(K_w(z)=(1-z\overline w)^{-\beta}\), and the monomials satisfy \(\|z^j\|^2=1/c_j\). The weight exponent obeys \(\alpha>-1\) (equivalently \(\beta>1\)); this hypothesis is used for the critical \(m/N\to1\) law. Distinct equally spaced nodes with common radius strictly between zero and one are required. No restriction on the number of kernels relative to the monomial degree is imposed.

## Proof
**1. Fourier-sector identity.** The kernel expansion is \(K_w(z)=\sum_{j\ge0}c_j\overline w^{\,j}z^j\). Applying the discrete Fourier transform in the polygon index separates the span of the \(m\) kernels into mutually orthogonal vectors supported on the residue classes \(j\pmod m\). The vector in the residue class of \(N\) is a nonzero multiple of
\[
\Psi_{\ell,m,r}(z)=\sum_{j\ge0,\ j\equiv\ell\ ({\rm mod}\ m)}c_jr^jz^j.
\]
Its squared norm is the denominator in the displayed finite-degree law, and \(|\langle e_N,\Psi_{\ell,m,r}\rangle|^2=c_Nr^{2N}\). All other discrete-Fourier sectors are orthogonal to \(e_N\), proving the projection formula.

**2. Exact uniqueness.** Set \(s=e^{-t/N}\), \(t>0\), and define \(p_j(t)\) proportional to \(c_j e^{-tj/N}\) among indices congruent to \(N\) modulo \(m\). The logarithm of the projection fraction satisfies
\[
\frac{d}{dt}\log Q_{N,m}(t)=\mathbb E_t(j/N)-1,\qquad
\frac{d^2}{dt^2}\log Q_{N,m}(t)=-\operatorname{Var}_t(j/N)<0.
\]
For \(m\le N\), the limiting expectation is \(\ell/N<1\) as \(t\to\infty\), while it tends to infinity as \(t\downarrow0\); therefore there is exactly one critical point, a strict global maximum. For \(m>N\), the smallest index in the residue class is \(N\), so the derivative is strictly negative and the fraction tends to \(1\) as \(t\to\infty\).

**3. Sublinear regime.** The standard gamma-ratio asymptotic gives \(c_j\sim j^{\beta-1}/\Gamma(\beta)\). If \(m/N\to0\), then for every fixed \(t>0\), uniformly on compact positive \(t\)-intervals, ordinary residue-class Riemann sums give
\[
\sum_{j\equiv N\ ({\rm mod}\ m)}c_je^{-tj/N}\sim\frac{N^\beta}{m t^\beta},\quad
\frac{\sum_{j\equiv N} (j/N)c_je^{-tj/N}}{\sum_{j\equiv N}c_je^{-tj/N}}\longrightarrow\frac\beta t.
\]
Indeed the mesh is \(m/N\to0\), the shifted grid has spacing \(m/N\), and \(x^{\beta-1}e^{-tx}\) and \(x^\beta e^{-tx}\) are integrable and continuous at zero; finite and exponential-tail truncation make the convergence uniform. Together with \(c_N\sim N^{\beta-1}/\Gamma(\beta)\), this proves the pointwise limit of \((N/m)Q_{N,m}(t)\). The strictly decreasing log-derivative changes sign between any fixed \(t<\beta\) and \(t>\beta\), so the *global* maximizing \(t\) converges to \(\beta\). Substitution proves the sharp coefficient.

**4. Macroscopic regime.** When \(m/N\to c\in(0,1)\), write every admissible index as \(j=N+km\). After division by \(N^{\beta-1}/\Gamma(\beta)\), its term converges to \((1+kc)^{\beta-1}e^{-t(1+kc)}\) if \(1+kc>0\), and to zero if the limiting index is zero. There are finitely many negative \(k\), and an exponentially summable positive tail. The same dominated-convergence argument applies with an additional factor \(j/N\), locally uniformly in \(t>0\). Thus both the fraction and its log-derivative converge to those of the displayed limiting series. This series contains a positive term at \(1-c<1\) and positive terms above \(1\). Its log-derivative is strictly decreasing, positive near zero, and negative for sufficiently large \(t\); the limiting maximizer is therefore unique and interior. The finite maximizing points converge by derivative bracketing. The limiting maximum is strictly between zero and one.

**5. Critical near-degree regime.** Suppose \(m/N\to1\) and \(m\le N\). Eventually \(m>N/2\), and the only residue-class index below \(N\) is \(\ell=N-m\). Define \(a=c_\ell/c_N\), \(b=c_{N+m}/c_N\), and \(h=m/N\). Dividing the denominator by its \(j=N\) term gives exactly
\[
Q_{N,m}(t)^{-1}=1+a e^{ht}+b e^{-ht}+R_N(t),
\]
where \(R_N(t)\) is the sum of terms with \(j=N+km\), \(k\ge2\). The gamma-ratio bounds yield \(a\to0\), \(b\to2^{\beta-1}\), and \(c_{N+km}/c_N\le C_\beta(1+k)^{\beta-1}\), uniformly for all such \(N,k\). By arithmetic-geometric mean, \(a e^{ht}+b e^{-ht}\ge2\sqrt{ab}\). At the positive choice \(t=\log(b/a)/(2h)\), both terms equal \(\sqrt{ab}\), and
\[
0\le R_N(t)\le C_\beta\sum_{k\ge2}(1+k)^{\beta-1}(a/b)^{k/2}=O_\beta(a).
\]
Consequently \(\inf_{t>0}(Q_{N,m}(t)^{-1}-1)=2\sqrt{ab}+O_\beta(a)\). Since \(a=o(\sqrt a)\), the relative deficit assertion follows upon inverting. This also proves the stated limiting saturation. The case \(m>N\) was already settled exactly in Step 2.

## Verification
The accompanying standalone Python checker independently computes projections both by complex Gram-matrix inversion and by the residue sum, tests numerical log-concavity and unique maximization, and checks the sublinear and critical asymptotic formulas for several noninteger weights. It passed 630 finite assertions. These tests are not a substitute for the infinite-sequence arguments in the proof; their numerical tail cutoffs are documented in the checker.

## Relationship to prior work
Best kernel approximation in standard weighted Bergman spaces is a well-established problem; Qu, Qian, Li and Zhu prove existence of unconstrained finite-kernel optimizers, while Qu, Qian and Deng prove a general reproducing-kernel existence criterion. Those existence theorems do not, from the inspected portions and publicly accessible statements, furnish the exact residue formula or the quantitative regular-polygon sparsity transition. Seip's earlier Bergman sampling work explains the general connection with Fourier localization but concerns different sampling and concentration statements. The orbit-kernel Gram-determinant work located in mathematical-result searches concerns Hardy/Szegő kernels and determinant optimization, not monomial projection onto weighted Bergman orbit dictionaries.

## Limitations
This is an exact result for a canonical symmetric dictionary, not an assertion of optimality among arbitrary configurations of \(m\) points. The limiting macroscopic constant is specified by a rapidly convergent series and its unique maximizer, rather than a claimed elementary closed form. Its derivation uses \(\beta>1\); Hardy-space endpoint behavior is not treated. Full-text access to one relevant 2021/2022 kernel-approximation paper was incomplete, so equivalence hidden in that or unindexed literature cannot be categorically excluded. Independent scientific validation and priority assessment have not been performed.

## References
- W. Qu, T. Qian, H. Li, and K. Zhu, *Best kernel approximation in Bergman spaces*, Applied Mathematics and Computation **416** (2022), 126749. First online November 10, 2021. DOI: 10.1016/j.amc.2021.126749.
- W. Qu, T. Qian, and G.-T. Deng, *A sufficient condition for n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2006.03290 (June 5, 2020).
- K. Seip, *Reproducing Formulas and Double Orthogonality in Bargmann and Bergman Spaces*, SIAM J. Math. Anal. **22** (1991), 856–876. DOI: 10.1137/0522054.
