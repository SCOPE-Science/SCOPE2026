# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument was checked at the structural points most likely to fail.

1. The endpoint coefficient is exactly a Dirichlet convolution:
   \[
   n^{2e}\sigma_{\ell-2e-1,D,1}(n)
   =\sum_{ab=n}\chi_D(a)a^{\ell-1}b^{2e}.
   \]
   The inverse of \(a_\ell(d)=\chi_D(d)d^{\ell-1}\) is \(\mu(d)\chi_D(d)d^{\ell-1}\), including at primes dividing \(D\). Hence the proposed triangular column transform has determinant one and sends the endpoint matrix exactly to \((n^{2e})\).
2. The transformed error exponent in a divisor \(d\) is \(-k_e-2\), so the divisor sum is uniformly bounded. This is the key point preventing the Möbius transform from destroying the Fourier-coefficient estimate.
3. The ordinary Vandermonde is controlled through its inverse rather than through a crude cofactor or determinant bound. Lagrange interpolation gives \(\|W_r^{-1}\|_\infty\le r2^r(r!)^2\), whose logarithm is only \(O(r\log r)\).
4. For \(r=c\sqrt\ell\), all non-exponential factors are \(\exp(o(\ell))\), while Stirling's formula gives exponential rate \(\log(2\pi e|D|c^2)\) for the transformed error. The strict inequality \(c<(2\pi e|D|)^{-1/2}\) therefore makes the Neumann-series criterion valid eventually.
5. The normalization factors are nonzero in the admissible parity class, and \(k_e\ge4\) for all sufficiently large \(\ell\). The Petersson identity then places every bracket in the twisted-nonvanishing subspace, so linear independence gives the eigenform count.

Exact integer tests independently verified the Möbius/Vandermonde identity for the trivial character and for the quadratic character modulo 5, including the zero values of that character at multiples of 5.

## Originality

**PASS, to the best of our knowledge.** The September 2026 paper of Takloo-Bighash was read at the theorem, explicit Fourier-coefficient estimate, determinant proof, effectivity remark, and Petersson implication. It explicitly keeps \(D\) and \(r\) fixed while the weight grows. Its determinant argument uses fixed prime Fourier indices. No growing-\(r\) theorem or square-root lower bound is stated there.

Kayath--Lane--Neifeld--Ni--Xue was checked for its spanning construction and discussion section. It frames linear independence of the relevant Rankin--Cohen families as a route to lower bounds and records a conjectural linear-size family; it also records Luo's stronger \(D=1\) result. It does not provide the square-root growing family proved here. Ni--Xue proves fixed-size linear independence of twisted periods for sufficiently large weight, again with the number of periods fixed.

Searches were made for equivalent formulations involving growing Rankin--Cohen families, weight-aspect lower bounds for the dimension of the fixed-twist nonvanishing subspace, square-root numbers of eigenforms, and quantitative dependence of the recent fixed-\(r\) theorem. No prior statement matching the present theorem was located. This negative search evidence is not treated as exhaustive.

The most relevant incompletely inspected older source is W. Luo, *Nonvanishing of the central L-values with large weight*, Adv. Math. 285 (2015), DOI 10.1016/j.aim.2015.08.009. Its abstract and the later literature's description were inspected, but the full text was not. It gives an optimal large-weight result for the untwisted \(D=1\) case, so it already dominates the present theorem's **counting** corollary when \(D=1\). It does not thereby cover the explicit growing Rankin--Cohen independence theorem or the nontrivial fixed-\(D\) statement. Residual originality risk is therefore concentrated in unindexed concurrent work and in any older fixed-twist weight-aspect result not surfaced by the searches.

## Value

**PASS.** The improvement is qualitative as well as quantitative: the number of independent explicit brackets changes from an arbitrary fixed integer to a family of order \(\sqrt\ell\), with an explicit lower constant \((2\pi e|D|)^{-1/2}\). The proof introduces a useful exact arithmetic preconditioning step: Möbius inversion removes the divisor-sum endpoint and exposes an ordinary Vandermonde, making a growing-dimensional perturbation estimate possible. For nontrivial fixed \(D\), this yields a concrete quantitative lower bound on the number of level-one eigenforms with nonzero \(D\)-twisted central value. The result remains far below the conjectural linear scale, so its scope is substantive but clearly limited.
