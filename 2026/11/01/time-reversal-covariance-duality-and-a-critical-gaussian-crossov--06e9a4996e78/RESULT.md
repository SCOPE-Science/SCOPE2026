# Time-reversal covariance duality and a critical Gaussian crossover in affine random maps

## Finding
For the stationary expanding/contracting affine interval process defined below, the *single-coordinate* annealed autocovariance has a closed algebraic generating function, is exactly invariant under interchanging the expansion and contraction probabilities, and has summable but critical power-law decay. The integrated autocovariance has an exact cusp at the zero-Lyapunov parameter. The critical covariance has distinct parity amplitudes and a Gaussian parameter-window crossover.

Put \(r=1/b\), \(q=1-p\), and, as formal power series about \(z=0\), set
\[
 h(z)=\frac{2}{1+\sqrt{1-4pqz^2}},\qquad a(z)=pz h(z).
\]
For all integers \(b\geq2\) and all \(p\in[0,1]\), the covariance \(C_n(b,p)\) of the coordinate at time zero and time \(n\) satisfies
\[
 \boxed{\sum_{n\geq0} C_n(b,p)z^n=
 \frac{1}{12}\frac{1-a(z)/r}{(1-r a(z))(1-z(p/r+q r))}.}
\]
This identity is an identity of Taylor series: any apparent singularities introduced by the displayed quotient are removable wherever the generating series remains regular. At all lags,
\[
 \boxed{C_n(b,p)=C_n(b,1-p).}
\]
All covariances are nonnegative, their series is summable, and
\[
 \boxed{\sum_{n\geq0}C_n(b,p)=
 \frac{1}{12(1-r)\big((1+r)\max\{p,1-p\}-r\big)}.}
\]
The integrated covariance has its strict global maximum and a nonsmooth cusp at \(p=1/2\), although each fixed-lag covariance is a polynomial in \(p\).

For \(\epsilon\in\{0,1\}\), define
\[
 K_{b,\epsilon}=\frac{1-r^2}{12}\sqrt{\frac{2}{\pi}}
 \left(\frac{1}{(1-r)^4}+\frac{(-1)^\epsilon}{(1+r)^4}\right)>0.
\]
As \(n\to\infty\) along integers satisfying \(n\equiv\epsilon\pmod2\),
\[
 \boxed{n^{3/2}C_n(b,1/2)\longrightarrow K_{b,\epsilon}.}
\]
More generally, for every fixed \(u\in\mathbb R\), with \(p_n=1/2+u/\sqrt n\) (and \(n\) sufficiently large that \(p_n\in[0,1]\)),
\[
 \boxed{n^{3/2}C_n(b,p_n)\longrightarrow e^{-2u^2}K_{b,\epsilon}}
\]
along the same parity subsequence.

## Assumptions and scope
Fix an integer \(b\geq2\). On \([0,1)\) independently select at each step either the expansion \(T_b(x)=\{bx\}\) with probability \(p\), or one of the \(b\) inverse branches \(I_{b,j}(x)=(x+j)/b\), \(j=0,\ldots,b-1\), each with probability \((1-p)/b\). Let \(X_0\) have normalized Lebesgue distribution, independently of all map choices, and let \(X_n\) be the resulting coordinate process. Lebesgue measure is stationary because the expansion preserves it and the uniform mixture of the inverse branches also preserves it. Define \(C_n(b,p)=\mathbb E[(X_0-1/2)(X_n-1/2)]\), including \(C_0=1/12\). The conclusion is an *annealed* two-time covariance for the bounded coordinate observable, not a quenched or two-particle covariance theorem. Endpoint choices \(p=0,1\) are included by direct definition and continuity, although the motivating work assumes interior probabilities.

The geometric Lyapunov exponent of the random branch derivative is \((2p-1)\log b\), so probability interchange reverses its sign. This quantity describes typical branchwise expansion, not a rate inferred from the coordinate covariance.

## Proof
**Fourier chain reduction.** Let \(e_m(x)=e^{2\pi i mx}\). The Koopman operator of expansion obeys \(Ue_m=e_{bm}\), whereas averaging the inverse branches gives its Hilbert adjoint \(U^*\): it sends \(e_m\) to \(e_{m/b}\) when \(b\) divides \(m\), and to zero otherwise. The annealed observable operator is therefore \(P_p=pU+qU^*\). Each frequency has a unique representation \(m=b^k \ell\), where \(k\geq0\) and \(\ell\) is nonzero and not divisible by \(b\). On each such orthogonal frequency chain, \(P_p\) acts as \(pS+qS^*\) on \(\ell^2(\mathbb N_0)\), with \(S e_k=e_{k+1}\) and \(S^* e_0=0\).

The Fourier coefficient of the centered coordinate \(f(x)=x-1/2\) at nonzero frequency \(m\) is \(-1/(2\pi i m)\). Hence on each chain its coefficient vector is a scalar multiple of \(v=(1,r,r^2,\ldots)\). Parseval and \(\|f\|_2^2=1/12\) yield exactly
\[
 C_n(b,p)=\frac{1-r^2}{12}\langle v,(pS+qS^*)^n v\rangle.
\]
The pairing is real because all chain coefficients and transition weights are real after removing their common complex scalar; the original observable has both positive and negative chains.

**Algebraic resolvent.** Write \(Q=pS+qS^*\) and \(t=p/r+qr\). Directly, \(Qv=t v-(p/r)e_0\). The resolvent column \(G(z)=(I-zQ)^{-1}e_0\) solves a nearest-neighbor recurrence with the boundary condition at index zero; solving it as formal series gives \(G_k(z)=h(z)a(z)^k\), since \(a=pz+qz a^2\) and \(h=1/(1-qza)\). In particular, \(\langle v,G(z)\rangle=h(z)/(1-ra(z))\). Applying the resolvent to \(v\) and substituting yields
\[
 \langle v,(I-zQ)^{-1}v\rangle
 =\frac{1}{1-tz}\left(\frac{1}{1-r^2}-\frac{pz}{r}\frac{h(z)}{1-ra(z)}\right).
\]
Multiplication by \((1-r^2)/12\), followed by \(a=pzh\), gives the claimed generating function. The endpoint cases follow from the same formal recurrences. Since \(Q^*=qS+pS^*\), the quadratic form is unchanged when \(p\) and \(q\) are swapped; this proves exact all-lag duality. All matrix entries of \(Q\) and coefficients of \(v\) are nonnegative, proving nonnegative covariances.

**The integrated cusp.** By monotone convergence of the nonnegative coefficients, the sum is the radial limit of the generating function at \(z=1\). For \(p\geq1/2\), the chosen nonnegative quadratic root obeys \(a(1)=1\). Evaluating the quotient and simplifying gives \(1/[12(1-r)((1+r)p-r)]\), finite even at \(p=1/2\). For \(p\leq1/2\), apply the already proved duality. The denominator strictly increases with \(|p-1/2|\), proving the cusp and strict maximum. Polynomiality at each finite lag follows by expanding \((pU+qU^*)^n\).

**Parity amplitudes and Gaussian crossover.** For \(i,j\geq0\), the reflection principle for paths on the half-line killed at \(-1\) gives
\[
 (Q^n)_{ij}=
 p^{(n+i-j)/2}q^{(n-i+j)/2}
 \left[\binom n{(n+i-j)/2}-\binom n{(n+i+j+2)/2}\right],
\]
with the entry set to zero when the parity is wrong; binomial coefficients outside \(\{0,\ldots,n\}\) are zero. The two terms have identical weights because the original paths to fixed endpoints have a fixed number of steps in each direction. When \(p=1/2\), the local central-binomial estimate for fixed admissible \(i,j\) is
\[
 (Q^n)_{ij}\sim 2\sqrt{\frac2\pi}\,(i+1)(j+1)n^{-3/2},
\]
for the parity \(n+i-j\) even. For \(p_n=1/2+u/\sqrt n\), the same binomial difference is multiplied by
\[
 (4p_n(1-p_n))^{n/2}
 \left(\frac{p_n}{1-p_n}\right)^{(i-j)/2}
 \longrightarrow e^{-2u^2}.
\]
The convergence can be summed against the weights \(r^{i+j}\). Indeed, \(\|Q\|\leq p+q=1\); truncating \(v\) at index \(L_n=c\log n\) with \(c\) sufficiently large makes its \(\ell^2\) tail contribute \(o(n^{-3/2})\). Uniform central-binomial expansion over the remaining \(i,j=O(\log n)\) gives the same limit. Finally the weighted parity sum is
\[
 \sum_{\substack{i,j\geq0\\ i-j\equiv n\pmod2}}r^{i+j}(i+1)(j+1)
 =\frac12\left((1-r)^{-4}+(-1)^n(1+r)^{-4}\right).
\]
Combining with the Fourier reduction proves the stated constants and the full fixed-\(u\) Gaussian parameter window, including both parity subsequences.

## Verification
The self-contained `checker.py` computes the covariance coefficients using two structurally independent exact-rational procedures. One propagates the Fourier half-line chain; the other composes the original piecewise-affine interval maps, splits preimages at every expanding-branch discontinuity, and integrates the coordinate product exactly over each resulting subinterval. It tests expansion bases \(b=2,3,4\), eleven rational probability cases including both endpoints, and finite lags through six; it also tests probability interchange, initial variance, and first-lag covariance. Executing the file produced `PASS; exact rational identities checked: 158`. These finite tests do **not** establish the infinite identities or asymptotics; those follow from the operator, reflection-principle, and uniform-local-limit arguments above.

To reproduce: save the accompanying standalone file `checker.py` in the same directory and run `python checker.py` with Python 3.9 or later; no third-party packages are needed.

## Relationship to prior work
Homburg and Kalle introduced the expanding/inverse-branch random interval model, proved stationarity of Lebesgue measure, and analyzed the two-point synchronization/intermittency transition in terms of the Lyapunov exponent. The present theorem specializes to matching expansion and contraction bases and studies a different observable: the full annealed *single-coordinate* two-time covariance, including its exact time-reversal symmetry and critical decay profile. Their original open-access manuscript and later full journal manuscript were compared for these specific statements; the inspected text does not supply this covariance generating function or the parity-resolved Gaussian window.

A related two-dimensional heterochaos baker-map calculation has the same critical half-line Fourier-chain mechanism and corresponding parity constants, so the parity asymptotic at equal probabilities is not asserted as a new mechanism. Its different system does not imply the all-probability covariance identity, probability-reversal symmetry, integrated cusp, or Gaussian parameter window for the present one-dimensional random interval maps. Yan and coauthors analyze correlations for the related Pelikan random map, which combines doubling with one *deterministic* inverse branch. Its stationary density and correlation structure are different; its autocovariance formulas do not imply those for a uniformly chosen inverse-branch map. Kalle and Zeegers develop correlation bounds for other critically intermittent random maps with superattracting branches, not the exact stationary model here. General gambler's-ruin reflection formulas account for a proof ingredient but do not themselves identify the interval-map covariance or its probability-duality cusp.

## Limitations
This result treats only matched integer expansion/contraction bases, a uniform distribution across all inverse branches, and the stationary Lebesgue coordinate observable. It makes no general-parameter \(M\ne N\) claim, no quenched or nonlinear-observable correlation claim, and no claim about two-particle correlations or invariant-measure uniqueness at the degenerate endpoints. Literature indexing cannot certify absolute publication priority; equivalent treatments of birth–death resolvents or random interval-map correlations not identified in the inspected sources remain a risk. Independent validation has not been performed.

## References
- A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1 (first public 2022-07-20), https://arxiv.org/html/2207.09987v1. Journal version: *Advances in Mathematics* 482 (2025), 110605, https://doi.org/10.1016/j.aim.2025.110605. Open manuscript: https://pure.uva.nl/ws/files/297456680/Iterated_function_systems_of_affine_expanding_and_contracting_maps_on_the_unit_interval.pdf.
- Yan et al., *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269, https://arxiv.org/abs/2308.09269.
- C. Kalle and B. Zeegers, *Decay of correlations for critically intermittent systems*, arXiv:2206.07601, https://arxiv.org/abs/2206.07601.
