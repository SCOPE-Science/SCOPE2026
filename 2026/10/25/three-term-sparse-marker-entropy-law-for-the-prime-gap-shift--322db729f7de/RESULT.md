# Three-term sparse-marker entropy law for the prime-gap shift

## Finding

Let \(\mathbb P=\{2,3,5,7,\ldots\}\), and let \(X_{\mathbb P}\) be the two-sided binary shift whose consecutive occurrences of 1 are separated by **a prime number of zeros**. Thus its allowed successive marker-return distances are \(\{p+1:p\in\mathbb P\}\). Denote by \(\sigma\) the left shift, by \([1]\) the cylinder with a 1 at coordinate zero, and by \(h_\mu(\sigma)\) entropy with natural logarithms. At marker frequency \(0<t<1/3\), put
\[
\mathcal E(t)=\sup\bigl\{h_\mu(\sigma):\mu\in\mathcal M_\sigma(X_{\mathbb P}),\ \mu([1])=t\bigr\}.
\]
Writing \(Q=\log(1/t)\) and denoting Euler's constant by \(\gamma\), one has the quantified asymptotic
\[
\boxed{\frac{\mathcal E(t)}t=Q-\log Q+1+\frac{\gamma}{Q}+\frac{\gamma^2/2+\pi^2/6-1/2}{Q^2}+O(Q^{-3})}\qquad(t\downarrow0).
\]
In particular, restricting allowed gaps to primes incurs a first-order entropy penalty of \(t\log\log(1/t)\) against unrestricted Bernoulli marker locations, followed by explicit Euler-constant and zeta-value corrections. Here *prime gap* refers to a gap whose number of zeros is prime, **not** to the differences between consecutive primes.

For every \(0<t<1/3\), the variational supremum is uniquely attained by the stationary renewal process whose successive marker-return distances \(p+1\) are independent with probability proportional to \(\exp(-s(t)(p+1))\). The existence and renewal expression are classical background; the assessed quantitative contribution is the explicit three-correction asymptotic specialized to prime-permitted gaps.

## Assumptions and scope

The space \(X_{\mathbb P}\subset\{0,1\}^{\mathbb Z}\) is the closure of bi-infinite concatenations of words \(10^p\), \(p\) prime. The closure contains the all-zero fixed point, and configurations with one-sided infinite zero tails. Shift-invariant probability measures give zero mass to the nonperiodic one-tail or isolated-marker configurations. The restriction \(0<t<1/3\) is sharp for nondegenerate positive-temperature renewal weights because the shortest return distance is 3. The asymptotic is for \(t\to0\), with the prime set fixed. No finite prime cutoff is taken in the theorem.

## Proof

**1. Exact constrained renewal variational identity.** For \(s>0\) write
\[
Z(s)=\sum_{p\in\mathbb P}e^{-s(p+1)},\quad
M(s)=\sum_{p\in\mathbb P}(p+1)e^{-s(p+1)},\quad
m(s)=M(s)/Z(s).
\]
Both sums converge absolutely. Their derivative obeys \(m'(s)=-\operatorname{Var}_{q_s}(p+1)<0\), where \(q_s(p)=e^{-s(p+1)}/Z(s)\). As \(s\downarrow0\), the mean \(m(s)\to\infty\); as \(s\to\infty\), it tends to 3. Hence for each \(0<t<1/3\) there is a unique \(s=s(t)\) with \(m(s)=1/t\).

Let \(\mu\) be any invariant measure with \(\mu([1])=t>0\). Decompose its all-zero atom as \(\mu=a\delta_{0^{\mathbb Z}}+(1-a)\nu\). The remaining positive-frequency part induces on \([1]\) a stationary process of prime-return labels with marginal \(q\). By Kac's return-time formula, \(\sum_p(p+1)q_p=(1-a)/t\). By Abramov's entropy formula, and the entropy-rate bound by one-symbol entropy,
\[
h_\mu(\sigma)\le t H(q),\quad H(q)=-\sum_pq_p\log q_p.
\]
The relative entropy \(D(q\Vert q_s)\ge0\) yields
\[
H(q)\le\log Z(s)+s\sum_p(p+1)q_p\le\log Z(s)+s/t.
\]
The iid-return law \(q_s\), lifted to a stationary renewal measure, gives equality in each inequality. Equality forces \(a=0\), marginal \(q=q_s\), and independent return labels. Therefore the maximizer is unique and
\[
\boxed{\mathcal E(t)/t=\log Z(s)+s/t.}
\]
No asymptotic novelty is asserted for this standard renewal representation itself.

**2. Laplace sums over primes.** We use the classical effective prime number theorem
\[
\pi(x)=\operatorname{Li}(x)+O\bigl(xe^{-c\sqrt{\log x}}\bigr),\qquad x\ge3,
\]
for some \(c>0\), and its Laplace–Stieltjes consequence. Set \(L=\log(1/s)\) and \(\kappa=\gamma^2+\pi^2/6\). By splitting the Stieltjes integrals at \(x=s^{-1/2}\), integrating by parts for the PNT error, and substituting \(u=sx\) for the main density \(1/\log x\), one obtains, uniformly as \(s\downarrow0\),
\[
Z(s)=\frac{1}{s}\left(\frac1L+\frac{\gamma}{L^2}+\frac{\kappa}{L^3}+O(L^{-4})\right),
\]
\[
M(s)=\frac{1}{s^2}\left(\frac1L+\frac{\gamma-1}{L^2}+\frac{\kappa-2\gamma}{L^3}+O(L^{-4})\right).
\]
Indeed, on \(u\in[s^{1/2},s^{-1/2}]\), expand \((L+\log u)^{-1}\) in powers of \(L^{-1}\), controlling the integral remainder by the integrability of \(e^{-u}(1+u)|\log u|^3\); the two excluded tails are superpolynomially small in \(1/L\). The effective-PNT error is \(O(s^{-1}e^{-c'\sqrt L})\) for the first sum, and \(O(s^{-2}e^{-c'\sqrt L})\) for the weighted sum, after reducing \(c'>0\) if necessary. Shifting \(p\) to \(p+1\) changes only exponentially smaller terms on the \(L^{-j}\) scales.

The coefficients are exact gamma-density logarithmic moments:
\[
\int_0^\infty e^{-u}\log u\,du=-\gamma,\quad
\int_0^\infty e^{-u}(\log u)^2\,du=\kappa,
\]
\[
\int_0^\infty ue^{-u}\log u\,du=1-\gamma,\quad
\int_0^\infty ue^{-u}(\log u)^2\,du=\kappa-2\gamma.
\]
They follow from the first two derivatives of the gamma function at 1 and 2; standard absolutely convergent differentiation suffices.

**3. Invert the marker-frequency relation.** Dividing the two Laplace expansions gives
\[
\frac{s}{t}=s\,m(s)=1-\frac1L-\frac\gamma{L^2}+O(L^{-3}).
\]
Because \(1/t=m(s)\), put \(Q=\log(1/t)\) to obtain
\[
Q=L+\log(s/t)=L-\frac1L-\frac{\gamma+1/2}{L^2}+O(L^{-3}),
\]
and consequently
\[
L=Q+\frac1Q+\frac{\gamma+1/2}{Q^2}+O(Q^{-3}).
\]
Meanwhile,
\[
\log Z(s)=L-\log L+\frac\gamma L+\frac{\gamma^2/2+\pi^2/6}{L^2}+O(L^{-3}).
\]
Insert these expansions into the exact identity \(\mathcal E(t)/t=\log Z(s)+s/t\). The \(Q^{-1}\) contributions from \(L\) and \(s/t\) cancel, while at order \(Q^{-2}\) their net contribution is \(-1/2\). This gives precisely the claimed formula and its \(O(Q^{-3})\) remainder.

## Verification

The critical nonstandard conclusion—the explicit \(Q^{-2}\) coefficient—is independently recoverable by substituting the displayed expansions into the exact renewal identity and collecting powers through \(Q^{-2}\). For example, \(\log L=\log Q+Q^{-2}+O(Q^{-3})\), \(1/L=1/Q+O(Q^{-3})\), and \(s/t=1-Q^{-1}-\gamma Q^{-2}+O(Q^{-3})\); the claimed coefficient follows algebraically without a numerical fit. The included standalone `verify.py` uses a finite prime sieve to cross-check the *exact finite-sum* Gibbs identity and tabulate the small-\(s\) trend; it is a diagnostic, not a proof of the PNT or the infinite asymptotic.

Run `python3 verify.py` using Python's standard library. The proof of the infinite result depends on the explicitly stated effective PNT and analytic remainder estimates, not on a finite prime enumeration or on a claimed external certification.

## Relationship to prior work

Baker and Ghenciu (arXiv:1411.7167v1, first submitted 2014-11-26) study standard \(S\)-gap shifts and their global topological entropy and dynamical properties. Ramirez and Somers (arXiv:2501.08438v1) explicitly identify the prime-permitted zero-gap set as an interesting nonsyndetic instance and extend the classical entropy-root formula, but their addressed invariant is global topological entropy, not entropy constrained by an asymptotically small marker density. Haydarov, Kadyrov, Makhmudov, and Mamayusupov (arXiv:2606.17031v1) provide general renewal-potential thermodynamic theory, which subsumes the underlying Gibbs/inducing mechanism but does not in the inspected material yield this prime-specific asymptotic with the displayed coefficients.

The separately published *Log-periodic second-order entropy law for geometric gap shifts* considers exponentially lacunary allowed return distances and derives a different leading constrained-entropy law, \(t\log\log_b(1/t)\), with a log-periodic correction. Its renewal framework is relevant prior method, but those results do not imply the density-one-logarithm prime-counting expansion here: geometric and prime return sets have different counting functions and different Laplace asymptotics. Neither the classical renewal framework nor the published geometric-gap calculation is claimed as newly established here.

## Limitations

This result treats exactly the set of **prime-valued numbers of zeros between markers** and the one-dimensional indicator frequency. It does not concern actual differences between consecutive primes, arbitrary arithmetic gap sets, equilibrium mixing rates, or a spatial finite-type approximation. The power-series coefficients use the classical effective PNT as a premise; no unconditional explicit numerical error bound or effective density threshold is asserted. Although the closest inspected sources do not contain the specific expansion, an earlier equivalent Tauberian or arithmetic-renewal computation in less searchable literature remains a priority risk. Independent scientific validation has not been performed.

## References

1. S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167v1 (2014-11-26), https://arxiv.org/abs/1411.7167 .
2. C. Ramirez and A. Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438v1 (2025-01-14), https://arxiv.org/abs/2501.08438 .
3. F. Haydarov, S. Kadyrov, M. Makhmudov and K. Mamayusupov, *Effective Intrinsic Ergodicity for renewal-type potentials on S-gap shifts*, arXiv:2606.17031v1 (2026-06-15), https://arxiv.org/abs/2606.17031 .
4. *Log-periodic second-order entropy law for geometric gap shifts*, published mathematical research record (2026-10-11), record identifier 166969f68799.
5. J. Hadamard and C. J. de la Vallée Poussin, the prime number theorem and classical zero-free-region quantitative error; \(\pi(x)=\operatorname{Li}(x)+O(xe^{-c\sqrt{\log x}})\) is used in the proof.
