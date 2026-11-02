# Fixed-opinion memory strictly enhances voter correlations on every finite ring

## Finding
For every integer \(N\ge 3\), every copying/reset rate pair \((1,r)\) with \(r>0\), and all distinct sites at cyclic distance \(n\in\{1,\ldots,N-1\}\), independently restoring each spin to its *original* fair opinion produces a strictly larger stationary annealed spin correlation than independently drawing a *new* fair spin at each reset, with the same rate. The difference is explicitly positive for every parameter. At the diffusive finite-size scale \(r=\lambda/N^2\), the two protocols have the same leading continuum correlation profile but an exactly positive correction of order \(N^{-1}\) at macroscopic separation and order \(N^{-2}\) for the nearest-neighbor domain-wall statistic.

Set \(a=\operatorname{arcosh}(1+r)\), \(h=N/2\), and \(z_n=h-\min\{n,N-n\}\). Write \(C_n^{\mathrm M}\) for original-opinion resetting and \(C_n^{\mathrm F}\) for fresh independent resetting. Then
\[
C_n^{\mathrm F}=\frac{\cosh(a z_n)}{\cosh(a h)},\qquad
C_n^{\mathrm M}-C_n^{\mathrm F}=
\frac{r^2\cosh(a z_n)}{\sinh^2(a)\sinh(a h)}
\left[h\tanh(a h)-z_n\tanh(a z_n)\right]>0.
\]
Both correlations are \(1\) at zero separation.

For fixed \(\lambda>0\), suppose \(r_N=\lambda/N^2\) and \(n_N/N\to x\in(0,1)\). Define \(k=\sqrt{2\lambda}\), \(s=k/2\), and
\[
g_\lambda(x)=\frac{\cosh(k(1/2-x))}{k\sinh s}.
\]
Then
\[
\lim_{N\to\infty} C_{n_N}^{\mathrm M}=
\lim_{N\to\infty} C_{n_N}^{\mathrm F}=
\frac{\cosh(k(1/2-x))}{\cosh s}
\]
and
\[
\lim_{N\to\infty} N(C_{n_N}^{\mathrm M}-C_{n_N}^{\mathrm F})=
\frac{\lambda^2g_\lambda(x)}{k}
\left[\tfrac12\tanh s-(\tfrac12-x)\tanh(k(\tfrac12-x))\right]>0.
\]
For stationary domain-wall densities \(\rho_N^{\mathrm M}=(1-C_1^{\mathrm M})/2\) and \(\rho_N^{\mathrm F}=(1-C_1^{\mathrm F})/2\), the common leading limit is
\[
\lim_{N\to\infty}N\rho_N^{\mathrm M}=
\lim_{N\to\infty}N\rho_N^{\mathrm F}=s\tanh s,
\]
but memory lowers the domain-wall density by the strictly positive exact second-order amount
\[
\boxed{\lim_{N\to\infty}N^2(\rho_N^{\mathrm F}-\rho_N^{\mathrm M})
=\frac\lambda4\left(1+\frac{2s}{\sinh(2s)}\right)>0.}
\]

## Assumptions and scope
On the cycle \(\mathbb Z/N\mathbb Z\), each \(S_i\in\{-1,1\}\) copies one of its two neighbors chosen uniformly at rate \(1\). Independently, at rate \(r\), the memory process restores \(S_i\) to the initially sampled opinion \(\xi_i\), which is independently equally likely to be \(-1\) or \(+1\) for each site and remains fixed for all time; in the fresh process the same event instead samples a new independent fair sign. The initial fair opinions are annealed, meaning averaged over together with the stationary dynamics. The stationary limits exist for finite \(N\) and \(r>0\); the moment equations below determine their correlations uniquely. For \(N\ge3\), the two neighbors are distinct. All assertions concern stationary *annealed* correlations; no claim is made about each individual frozen initial environment.

## Proof
Let \(T\) shift cyclic indices and let \(L_r=(1+r)I-(T+T^{-1})/2\) on functions on the ring. It is strictly positive definite for \(r>0\); its inverse is the strictly positive translation-invariant kernel
\[
G_n=\frac1N\sum_{j=0}^{N-1}
\frac{\cos(2\pi jn/N)}{r+1-\cos(2\pi j/N)}
=\frac{\cosh(a z_n)}{\sinh(a)\sinh(a h)}.
\]
The final equality follows by solving the discrete second-order recurrence away from zero, imposing periodicity and its unit source. The formula remains correct for odd \(N\) (half-integer \(h\)).

For the memory process let \(H_n=\mathbb E[S_i\xi_{i+n}]\). Differentiating this observable under the Markov generator and averaging over the independent fair original spins gives \(L_rH=r\delta_0\), hence \(H_n=rG_n\). For \(n\ne0\), the generator applied to \(S_iS_{i+n}\) yields \(L_r C_n^{\mathrm M}=rH_n=r^2G_n\); at \(n=0\), normalization instead demands \(C_0^{\mathrm M}=1\). Define the positive convolution resolvent
\[
F_n=(G*G)_n=\sum_{k\in\mathbb Z/N\mathbb Z}G_kG_{n-k}=-\partial_rG_n.
\]
The unique solution of the inhomogeneous difference equation with the normalization is
\[
C_n^{\mathrm M}=r^2F_n+
(1-r^2F_0)\frac{G_n}{G_0}.
\]
For fresh resets the resetting source at distinct sites vanishes because a newly chosen fair sign is independent of the remaining spins. The same normalized recurrence gives \(C_n^{\mathrm F}=G_n/G_0\). Consequently
\[
C_n^{\mathrm M}-C_n^{\mathrm F}
=r^2\left(F_n-\frac{G_n}{G_0}F_0\right)
=-r^2G_n\partial_r\log\frac{G_n}{G_0}.
\]
Since \(G_n/G_0=\cosh(a z_n)/\cosh(a h)\) and \(\partial_ra=1/\sinh a\), this is exactly the displayed difference. It is strictly positive for \(0<n<N\), because \(t\mapsto t\tanh(at)\) increases strictly on \([0,\infty)\) and \(0\le z_n<h\). This establishes the finite-volume comparison at every rate, without an approximation.

For the limits, uniformly for fixed \(\lambda>0\), \(a=\sqrt{2\lambda}/N+O(N^{-3})\), \(\sinh a=\sqrt{2\lambda}/N+O(N^{-3})\), and \(z_{n_N}/N\to1/2-x\). Substitution in the exact hyperbolic expressions gives the common continuum profile and macroscopic positive correction. For \(n=1\), the crucial bracket is
\[
h\tanh(ah)-(h-1)\tanh(a(h-1))
\longrightarrow\tanh s+s\operatorname{sech}^2s.
\]
With \(G_1\sim N\coth(s)/k\) and \(\sinh a\sim k/N\), this yields
\[
\lim N^2(C_1^{\mathrm M}-C_1^{\mathrm F})
=\frac\lambda2\left(1+\frac{2s}{\sinh(2s)}\right).
\]
Finally \(C_1^{\mathrm F}=\cosh(ah-a)/\cosh(ah)\) implies \(\lim N(1-C_1^{\mathrm F})/2=s\tanh s\), and the memory correction is only order \(N^{-2}\). Dividing its coefficient by two proves the domain-wall difference.

## Verification
The attached standalone `voter_ring_verifier.py` uses only standard Python. It independently solves the *full finite-state stationary Markov generator* with exact rational arithmetic for both protocols at sizes \(N=3,4\) and two rational rates, checking the resolvent formulas. It further tests all nonzero separations for six cycle sizes and four resetting rates and tests convergence of the three scaling quantities at four fixed positive scaling parameters. Its completed execution reported 16 exact-rational checks, 200 strict-sign checks and 36 scaling checks. Those finite tests support, but are not replacements for, the generator derivation and infinite-limit proof above. To reproduce, use `python3 voter_ring_verifier.py` in a Python 3 environment with no third-party packages.

## Relationship to prior work
Grange's voter-model resetting study (2022) established the original-opinion resetting mechanism, its infinite-lattice correlation equations, and the stationary domain-wall density. Pymar and Rivera's noisy-voter work (2021) analyzed fresh randomization on finite graphs and its cycle-scale transition; the fresh-reset ring resolvent and diffusive noise scale are therefore not claimed as new. This result instead compares *these two distinct stationary processes at identical rate and ring size* through a globally strict correlation inequality, and extracts the first memory-sensitive correction to their shared leading finite-size domain-wall limit. Familiar coalescing-walk and discrete resolvent methods are explicitly acknowledged. Closely related broader literature might imply the comparison; no exhaustive priority assertion is made.

## Limitations
The result assumes nearest-neighbor symmetric copying, homogeneous independent Poisson reset clocks, independent initially fair frozen opinions, and a finite cycle. It does not assert strict correlation order for arbitrary graphs, biased initial opinions, individual quenched environments, asynchronous common/global resets, or other resetting distributions. It gives population stationary correlations rather than statistical inference guarantees. Its subleading limit is at fixed \(\lambda>0\), not a uniform two-parameter asymptotic in all limits.

## References
1. P. Grange, *Voter model under stochastic resetting*, first public preprint 18 July 2022, https://arxiv.org/abs/2207.08590 .
2. R. Pymar and N. Rivera, *On the stationary distribution of the noisy voter model* (also catalogued as *Asymptotic behaviour of the noisy voter model density process*), first public preprint 2 December 2021, https://arxiv.org/abs/2112.01478 .
3. P. Nowak et al., *Discontinuous phase transitions in the multi-state noisy q-voter model: quenched vs annealed disorder*, https://arxiv.org/abs/2012.11725 . Different model of frozen voter types, included for terminology comparison only.
