# The positive second-order gap in hyperbolic Bergman spectral filling

## Finding

For each complex dimension \(d\in\{1,2,\ldots\}\), Bergman weight \(\alpha>-1\), and cost power \(p>0\), the radial spectral sum of hyperbolic distance powers exceeds the corresponding exact volume-filling lower bound by a strictly positive and asymptotically *sharp* second-order term.

With \(b=\alpha+1\), \(A=\Gamma(b+d)/(d!\,\Gamma(b))\), \(r(z)=\operatorname{arctanh}|z|\), and \(\lambda_j\) the nondecreasing eigenvalues of the Toeplitz form with symbol \(r^p\), define
\[
S_N=\sum_{j=1}^N\lambda_j,\qquad
I_N=\int_0^N\left[\operatorname{arsinh}\left((s/A)^{1/(2d)}\right)\right]^pds.
\]
Then for all fixed parameters as above,
\[
\boxed{\lim_{N\to\infty}\frac{S_N-I_N}{N(\log N)^{p-1}}
=\frac{p}{(2d)^p}\left[\log\frac{\Gamma(b+d)}{\Gamma(b)}-d\psi(b)\right]>0.}
\]
Here \(\psi=\Gamma'/\Gamma\) is the digamma function. The assertion is an asymptotic equality: it gives the exact coefficient, not merely a lower bound. It remains valid for the fractional range \(0<p<1\).

## Assumptions and scope

Equip the unit ball \(\mathbb B^d\subset\mathbb C^d\) with the probability measure
\[
d\mu_\alpha(z)=\frac{\Gamma(\alpha+d+1)}{\pi^d\Gamma(\alpha+1)}(1-|z|^2)^\alpha\,dV(z).
\]
Let \(\mathcal A^2_\alpha\) be its closed holomorphic subspace. The densely defined nonnegative Toeplitz form is \(q(f)=\int_{\mathbb B^d}r(z)^p|f(z)|^2d\mu_\alpha(z)\). Its closed realization is diagonal on normalized monomials and has compact resolvent; \(\lambda_j\) are its eigenvalues with *complex* multiplicities. This is the same hyperbolic normalization, symbol, and filling lower bound as Proposition 5.2 of Alvarez–Camper–Mitkovski. The integer \(N\to\infty\); \(d,\alpha,p\) stay fixed. No statement concerning a joint semiclassical \(\alpha\to\infty\) limit is made.

## Proof

**1. Exact diagonalization.** A normalized monomial of total degree \(k\ge0\) has radial squared-modulus distribution
\[
T_k=|z|^2\sim\mathrm{Beta}(k+d,b),\qquad b=\alpha+1,
\]
and the corresponding eigenvalue, with multiplicity \(m_k=\binom{k+d-1}{d-1}\), is
\[
\mu_k(p)=\frac{1}{B(k+d,b)}\int_0^1
[\operatorname{arctanh}\sqrt t]^p t^{k+d-1}(1-t)^{b-1}\,dt.
\]
All these integrals are finite because \(b>0\), and finite polynomial combinations form a dense form core. For \(k'>k\), the likelihood ratio of the two beta densities is a strictly increasing function of \(t\); therefore \(\mu_{k'}(p)>\mu_k(p)\). This fixes the eigenvalue ordering exactly, including the shell multiplicities.

**2. The beta boundary layer and its logarithmic moment.** Put \(a=k+d\) and \(W_a=a(1-T_k)\). Its density on \((0,a)\) is
\[
\frac{a^{-b}}{B(a,b)}w^{b-1}\left(1-\frac wa\right)^{a-1}.
\]
For every \(a\ge2\), this is bounded by \(C_bw^{b-1}e^{-w/2}\); the factor \(a^{-b}/B(a,b)\) is uniformly bounded because it converges to \(1/\Gamma(b)\). Dominated convergence therefore gives \(W_a\Rightarrow G_b\), with \(G_b\) gamma-distributed with shape \(b\) and rate \(1\), together with convergence of all fixed logarithmic moments and uniform bounds \(\sup_{a\ge2}\mathbb E|\log W_a|^q<\infty\) for each \(q>0\). In particular,
\[
\mathbb E\log W_a=\log a+\psi(b)-\psi(a+b)=\psi(b)+O_b(a^{-1}).
\]
The exact logarithmic identity
\[
\operatorname{arctanh}\sqrt{T_k}=\tfrac12\log a+Y_a,\qquad
Y_a=\log(1+\sqrt{T_k})-\tfrac12\log W_a
\]
implies \(\sup_a\mathbb E|Y_a|^q<\infty\). Since
\(0\le\log2-\log(1+\sqrt t)\le1-t\) on \([0,1]\) and \(\mathbb E(1-T_k)=b/(a+b)\),
\[
\mathbb E Y_a=c_b+O_b(a^{-1}),\qquad c_b=\log2-\tfrac12\psi(b).
\]
For every fixed \(p>0\), Taylor expansion on \(\{|Y_a|\le\tfrac14\log a\}\) has remainder \(O_p((\log a)^{p-2}Y_a^2)\). Its complement is controlled by uniformly bounded logarithmic moments of sufficiently high order, even when \(0<p<1\), and contributes \(O((\log a)^{p-2})\). Thus
\[
\mu_k(p)=\left(\tfrac12\log(k+d)\right)^p
+p c_b\left(\tfrac12\log(k+d)\right)^{p-1}
+O_{d,b,p}\bigl((\log k)^{p-2}\bigr),\quad k\to\infty.
\]
Consequently \(\mu_k(p)\to\infty\) and the diagonal form has compact resolvent. The finite number of small \(k\) play no role in the asymptotic.

**3. Summation over degree shells.** Define \(M_K=\sum_{k=0}^Km_k=\binom{K+d}{d}\). The weighted degree distribution satisfies
\[
\frac1{M_K}\sum_{k=0}^Km_k\log(k+d)
=\log K-\frac1d+o(1),\qquad
\frac1{M_K}\sum_{k=0}^Km_k
\left|\log\frac{k+d}{K}\right|^2=O_d(1).
\]
For example, these follow by summation/Riemann sums from the density \(d t^{d-1}dt\) on \((0,1]\), whose expected \(\log t\) is \(-1/d\). The very small degrees \(k<K^{1/2}\) have total multiplicity \(O_d(K^{d/2})\), so their contribution is negligible even at the second logarithmic order; the moment bound justifies Taylor expansion on the other degrees. With \(L_K=\tfrac12\log K\), this yields
\[
\sum_{k=0}^Km_k\mu_k(p)
=M_K\left[L_K^p+p\left(c_b-\frac1{2d}\right)L_K^{p-1}
+o(L_K^{p-1})\right].
\]
For arbitrary integer \(N\), at most one terminal shell is partially filled. Its size is \(O_d(K^{d-1})\) and its eigenvalue \(O((\log K)^p)\); this error is \(o(N(\log N)^{p-1})\). Inverting \(M_K=K^d/d!+O_d(K^{d-1})\) gives \(\log K=(\log N+\log(d!))/d+o(1)\). Hence
\[
S_N=\frac{N(\log N)^p}{(2d)^p}
+\frac{pN(\log N)^{p-1}}{(2d)^{p-1}}
\left[\log2-\frac{\psi(b)}2+\frac{\log(d!)-1}{2d}\right]
+o(N(\log N)^{p-1}).\tag{1}
\]

**4. Subtract the exact filling integral.** Proposition 5.2 gives the exact volume radius in \(I_N\). For \(s\to\infty\),
\[
\operatorname{arsinh}((s/A)^{1/(2d)})
=\frac{\log s}{2d}+\log2-\frac{\log A}{2d}+O_{d,A}(s^{-1/d}).
\]
Taylor expansion and a single integration by parts show
\[
I_N=\frac{N(\log N)^p}{(2d)^p}
+\frac{pN(\log N)^{p-1}}{(2d)^{p-1}}
\left[\log2-\frac{\log A+1}{2d}\right]
+o(N(\log N)^{p-1}).\tag{2}
\]
The region of bounded \(s\) contributes only \(O(1)\), so this also holds for \(0<p<1\). Subtract (2) from (1) and use \(d!A=\Gamma(b+d)/\Gamma(b)\) to obtain the stated limit.

**5. Strict positivity.** A gamma random variable \(G_b\) is nonconstant with \(\mathbb E G_b=b\) and \(\mathbb E\log G_b=\psi(b)\). Strict Jensen gives \(\psi(b)<\log b\). Since \(\Gamma(b+d)/\Gamma(b)=\prod_{j=0}^{d-1}(b+j)\ge b^d\), the bracket is strictly positive for every \(b>0\), \(d\ge1\). This completes all quantifiers and boundaries.

## Verification

The spectral integral is the beta expectation in Step 1, not an inferred numerical formula. The logarithmic expansion is backed by all-order uniform moment domination in Step 2; small-degree and terminal-shell errors are estimated explicitly. The integral expansion is checked independently in Step 4, and the constant is strictly positive by Step 5. In addition, the standalone `numeric_check.py` reproduces two finite-\(N\) Gauss–Jacobi spot checks: for \((d,\alpha,p,N)=(2,0,1,2016)\) the scaled gap is \(0.4657778\) versus asymptotic constant \(0.4618946\), and for \((2,1.5,2,2016)\) it is \(0.1232278\) versus \(0.0953426\). Those approximate numbers provide only consistency checks and are not certificates of asymptotic limits.

## Relationship to prior work

Alvarez–Camper–Mitkovski, arXiv:2610.02484v1, Proposition 5.2, gives the *exact* volume-filling integral lower bound \(I_N\) and the leading equality \(S_N\sim N(\log N)^p/(2d)^p\); their proof does not compute its next-order gap. Their Corollary 3.6 supplies a general comparison by fixed kernel moments, which is too coarse to recover the present exact coefficient, notably in the fractional range. Classical weighted-ball radial Toeplitz diagonalization appears in Grudsky–Karapetyants–Vasilevski (2003) and García–Vasilevski (2015). Such diagonalization is used as an ingredient, not claimed as new: the content here is the sharp *positive second-order defect* after combining the logarithmic beta boundary layer, dimension multiplicities, and the explicit filling integral. Available inspections did not identify an earlier theorem implying that same normalized defect; an unindexed equivalent expansion remains a literature risk.

## Limitations

All parameters are fixed as \(N\to\infty\). There is no uniform error estimate as \(p\to0\), \(\alpha\to-1\), \(\alpha\to\infty\), or \(d\to\infty\), nor a generalization to nonradial costs or nonball domains. The displayed little-\(o\) terms do not give finite-\(N\) rigorous error bars. The numerical examples do not replace the analytic proof. No independent external validation has been conducted.

## References

1. T. Alvarez, T. Camper, and M. Mitkovski, *Orthogonality, Spectral Filling, and Uncertainty*, arXiv:2610.02484v1 (2026), Sections 3 and 5.2, especially Proposition 5.2. https://arxiv.org/html/2610.02484v1
2. S. Grudsky, A. Karapetyants, and N. Vasilevski, *Toeplitz operators on the unit ball in \(\mathbb C^n\) with radial symbols*, Journal of Operator Theory 49 (2003), 325–346. https://jot.theta.ro/jot/archive/2003-049-002/2003-049-002-007.pdf
3. A. García and N. Vasilevski, *Toeplitz Operators on the Weighted Bergman Space over the Two-Dimensional Unit Ball*, Journal of Function Spaces (2015), article 306168. https://doi.org/10.1155/2015/306168
4. W. Bauer, C. Herrera Yañez, and N. Vasilevski, *Eigenvalue Characterization of Radial Operators on Weighted Bergman Spaces Over the Unit Ball*, Integral Equations and Operator Theory 78 (2014), 271–300, doi:10.1007/s00020-013-2101-1 (abstract inspected; full text not assessed for the claimed asymptotic).
