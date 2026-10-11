# Log-periodic second-order entropy law for geometric gap shifts

## Finding

Fix any integer \(b\ge2\). In the two-sided binary \(S\)-gap shift whose allowed distances between consecutive occurrences of 1 are \(1,b,b^2,\ldots\), the largest measure-theoretic entropy at a prescribed frequency \(t\) of 1s has a **genuinely oscillatory second-order sparse-frequency expansion**. The principal point is not the already known renewal representation, but the explicit periodic correction that survives after subtracting the logarithmic and iterated-logarithmic terms.

For \(0<t<1\), define
\[
E_b(t)=\sup\{h_\mu(\sigma):\mu\in\mathcal M_\sigma(X_b),\ \mu([1])=t\}.
\]
All logarithms without an indicated base are natural. There is a unique positive \(\lambda_b(t)\) for which
\[
\frac{\sum_{k=0}^\infty b^k\exp(-\lambda_b(t)b^k)}{\sum_{k=0}^\infty\exp(-\lambda_b(t)b^k)}=\frac1t.
\]
Set \(K=\lfloor\log_b(1/\lambda_b(t))\rfloor\), \(\rho=b^K\lambda_b(t)\in(1/b,1]\), and \(L=\log_b(1/t)\). Define absolutely convergent bilateral sums
\[
A_b(\rho)=\sum_{j\in\mathbb Z}\rho b^j e^{-\rho b^j},\qquad
\Psi_b(\rho)=\sum_{j=-\infty}^{-1}(e^{-\rho b^j}-1)+\sum_{j=0}^{\infty}e^{-\rho b^j},
\]
and the phase function
\[
\Xi_b(\rho)=\log_b\!\left(\frac{\rho}{A_b(\rho)}\right)+\Psi_b(\rho)+A_b(\rho).
\]
The precise sparse-frequency law is
\[
\boxed{\frac{E_b(t)}t=\log L+\frac{\log_b L+\Xi_b(\rho)}{L}+O_b\!\left(\frac{(\log L)^2}{L^2}\right)}
\qquad(t\downarrow0).
\]
The error is uniform for \(\rho\in[1/b,1]\). Moreover \(\Xi_b(b\rho)=\Xi_b(\rho)\), and the one-periodic function \(u\mapsto\Xi_b(b^u)\) is real-analytic and **not constant**. In particular, the cluster set at \(t=0\) of
\[
L\left(\frac{E_b(t)}t-\log L\right)-\log_b L
\]
is exactly the nondegenerate interval \([\min_{\rho\in[1/b,1]}\Xi_b(\rho),\max_{\rho\in[1/b,1]}\Xi_b(\rho)]\). Consequently \(E_b(t)\sim t\log\log_b(1/t)\), but the next term contains a genuine geometric-lattice effect.

## Assumptions and scope

The space \(X_b\subset\{0,1\}^{\mathbb Z}\) is the closure of all bi-infinite concatenations of blocks \(10^{b^k-1}\), with \(k\ge0\), and \(\sigma\) is the bilateral left shift. This convention admits the all-zero fixed point and one-sided infinite-zero tails in the closure. For invariant probabilities, those tails carry zero mass except possibly at the all-zero fixed point. The integer \(b\) is fixed while \(t\) tends to zero. The entropy normalization uses natural logarithms, while \(\log_b\) means base-\(b\) logarithm. \([1]\) means the cylinder where coordinate zero is 1.

The statement does **not** treat ordinary topological entropy as a new invariant: for general \(S\)-gap shifts the familiar topological entropy is given by a renewal equation. Nor is the renewal-Gibbs description itself claimed as novel. The new content is the uniform second-order asymptotic and proof that its periodic factor is genuinely nonconstant.

## Proof

**1. The constrained variational problem, including the zero atom.** Let \(D_k=b^k\), and for \(\lambda>0\) put
\[
Z(\lambda)=\sum_{k\ge0}e^{-\lambda D_k},\quad
p_k(\lambda)=\frac{e^{-\lambda D_k}}{Z(\lambda)},\quad
m(\lambda)=\sum_{k\ge0}D_k p_k(\lambda).
\]
These series are finite for every positive \(\lambda\). The derivative \(m'(\lambda)=-\operatorname{Var}_{p(\lambda)}(D_k)<0\), and \(m(\lambda)\) decreases continuously from infinity to one as \(\lambda\) increases from zero to infinity. Thus for each \(0<t<1\) exactly one positive parameter satisfies \(m(\lambda)=1/t\).

Take an arbitrary invariant probability \(\mu\) with \(\mu([1])=t>0\). Split off the invariant all-zero atom: \(\mu=a\delta_{0^\infty}+(1-a)\nu\), where \(\nu(\{0^\infty\})=0\). The invariant measure \(\nu\) is supported modulo null sets on paths with infinitely many 1s in both directions. Inducing \(\nu\) on \([1]\) yields an invariant measure on the countable full shift of return-length labels \(k\), with single-label marginal \(q=(q_k)\). Kac's formula gives
\[
\sum_kD_kq_k=\frac{1-a}{t}\le\frac1t.
\]
Abramov's entropy formula and the single-symbol entropy bound yield
\[
h_\mu(\sigma)=t\,h_{\mathrm{induced}}\le t H(q),\qquad H(q)=-\sum_kq_k\log q_k.
\]
The atom splitting here is essential: without it, the return-time mean need not be \(1/t\).

For the unique parameter \(\lambda\) above, relative-entropy nonnegativity implies
\[
H(q)\le\log Z(\lambda)+\lambda\sum_kD_kq_k
\le\log Z(\lambda)+\frac\lambda t.
\]
Both inequalities become equalities for independent return labels with law \(p_k(\lambda)\) and with \(a=0\), lifted to the unique stationary renewal probability. Conversely, because \(\lambda>0\), equality forces \(a=0\), \(q=p(\lambda)\), and independent return labels. Hence the maximizer is unique, and
\[
\boxed{\frac{E_b(t)}t=\log Z(\lambda)+\frac\lambda t.}
\]
The underlying renewal mechanism is standard; it is included here to fix exactly which constrained quantity is expanded and to handle all invariant measures.

**2. Uniform lattice expansions.** Write \(\lambda=\rho b^{-K}\) with \(\rho\in(1/b,1]\). Shifting the summation index by \(K\) gives
\[
Z(\lambda)=\sum_{j=-K}^\infty e^{-\rho b^j}
=K+\Psi_b(\rho)+O_b(b^{-K}).
\]
Likewise, with \(a(\lambda)=\lambda\sum_{k\ge0}D_ke^{-\lambda D_k}\),
\[
a(\lambda)=\sum_{j=-K}^\infty\rho b^je^{-\rho b^j}
=A_b(\rho)+O_b(b^{-K}).
\]
Both bounds are uniform in the phase because the omitted negative-index tails are bounded by geometric series. Positive-index tails converge superexponentially. In particular, \(A_b\) is bounded above and away from zero on \([1/b,1]\).

The mean condition gives \(t=\lambda Z(\lambda)/a(\lambda)\). Therefore, with \(L=\log_b(1/t)\),
\[
L=K-\log_bK-\log_b\rho+\log_b A_b(\rho)+O_b(K^{-1}),
\]
and hence
\[
K=L+\log_b L+\log_b\!\left(\frac\rho{A_b(\rho)}\right)
+O_b\!\left(\frac{\log L}{L}\right).
\]
Finally, \(\lambda/t=a(\lambda)/Z(\lambda)\), so
\[
\frac{E_b(t)}t=\log K+
\frac{\Psi_b(\rho)+A_b(\rho)}K+O_b(K^{-2}).
\]
Substitute the expansion of \(K\), expand \(\log K\) at \(L\), and use \(K=L+O_b(\log L)\). This proves the claimed uniform formula, with \(O_b((\log L)^2/L^2)\) error.

**3. A real nonconstant phase.** Directly from index shifts,
\[
A_b(b\rho)=A_b(\rho),\qquad\Psi_b(b\rho)=\Psi_b(\rho)-1.
\]
Consequently \(\Xi_b(b\rho)=\Xi_b(\rho)\). Uniformly convergent differentiated series make \(u\mapsto A_b(b^u)\) and \(u\mapsto\Xi_b(b^u)\) real-analytic and one-periodic. Let \(\mathscr A(u)=A_b(b^u)\). By changing variables in the sum over all integer shifts, its first Fourier coefficient is
\[
\int_0^1\mathscr A(u)e^{-2\pi i u}\,du
=\frac1{\log b}\,\Gamma\!\left(1-\frac{2\pi i}{\log b}\right)\ne0.
\]
The nonvanishing uses the standard Euler product for the gamma function (which has no zeros). Thus \(\mathscr A\) is nonconstant. Differentiating the phase relation and using \(d\Psi_b(b^u)/du=-(\log b)\mathscr A(u)\) gives the exact factorization
\[
\frac{d}{du}\Xi_b(b^u)
=\bigl(1-(\log b)\mathscr A(u)\bigr)
\left(1-\frac{\mathscr A'(u)}{(\log b)\mathscr A(u)}\right).
\]
If the phase were constant, analyticity and the nonconstancy of \(\mathscr A\) would force \(\mathscr A'=(\log b)\mathscr A\) everywhere; its positive solutions are exponential and cannot be periodic. This proves nonconstancy.

For each fixed phase \(\rho\in[1/b,1]\), the values \(\lambda=\rho b^{-K}\) as \(K\to\infty\) give a sequence \(t\downarrow0\) with that phase. Conversely, any sequence of phases has a convergent subsequence. Continuity of \(\Xi_b\) on the phase circle therefore proves the claimed exact cluster interval.

## Verification

A standalone dependency-free script, `checker.py`, uses finite exponential sums to test the normalization, periodicity of the phase expression, and decreasing finite-scale errors for bases \(2,3,5\) and several exponents \(K\). Its actual output is `DIAGNOSTICS_OK 19`, with 19 passed numerical assertions. These finite checks are not used as a proof of uniformity, nonconstancy, the variational characterization, or the infinite asymptotic. Each infinite assertion is addressed in the preceding proof.

To reproduce, extract `checker.py` from the package and run `python3 checker.py` using Python's standard library. The index-shift identities and analytic argument require no external data or numerical constants.

## Relationship to prior work

Haydarov, Kadyrov, Makhmudov and Mamayusupov (2026, arXiv:2606.17031v1) treat renewal-type potentials for arbitrary \(S\)-gap shifts and establish equilibrium uniqueness and effective estimates. Their inducing and zero-atom splitting framework is part of the existing mathematical background, not a new claim here. The ordinary pressure equation and exponential return weights can also be applied to a chemical-potential perturbation and thus motivate the exact constrained renewal formula.

Ramirez and Somers (arXiv:2501.08438v1, first submitted January 2025) explicitly single out gaps of powers of two as interesting lacunary examples; their theorem gives topological entropy for a broader class of gap shifts, without prescribing marker density or deriving a sparse-density two-term phase law. Climenhaga (2014) likewise gives the classical \(S\)-gap topological-entropy equation and ergodic induction route. Their results do not state the normalized second-order correction \(\Xi_b\) or its nontrivial phase range. Classical Mellin analysis of digital sums supplies relevant techniques, but the constrained-entropy combination and exact cluster interval are the statements examined here.

## Limitations

This theorem holds for **geometric integral return distances** and fixed base \(b\ge2\). It does not claim a corresponding expansion for arbitrary lacunary sets, nonrenewal constraints, nonlinear observables, or topological entropies of individual noncompact level sets. The phase amplitude can be very small (especially at base 2); numerical observations of small variation do not replace the gamma-function proof of nonconstancy. No independent audit or externally certified proof has been performed. Older or unindexed equivalent lattice-asymptotic calculations remain an originality risk.

## References

1. F. Haydarov, S. Kadyrov, M. Makhmudov and K. Mamayusupov, *Effective Intrinsic Ergodicity for renewal-type potentials on S-gap shifts*, arXiv:2606.17031v1 (first public June 15, 2026). https://arxiv.org/abs/2606.17031
2. C. Ramirez and A. Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438v1 (January 14, 2025). https://arxiv.org/html/2501.08438v1
3. V. Climenhaga, *Entropy of S-gap shifts*, September 8, 2014. https://vaughnclimenhaga.wordpress.com/2014/09/08/entropy-of-s-gap-shifts/
4. R. Rühr and O. Sarig, *Effective intrinsic ergodicity for countable state Markov shifts*, arXiv:2112.01186 (2021). https://arxiv.org/abs/2112.01186
