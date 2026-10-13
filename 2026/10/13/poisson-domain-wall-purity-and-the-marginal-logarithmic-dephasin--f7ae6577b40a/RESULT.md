# Poisson-domain-wall purity and the marginal logarithmic dephasing window

## Finding

A long-range pair-dephasing channel applied to a symmetric open-chain matrix-product state has an exactly computable, nontrivial global-purity limit when its domain-wall fugacity is inversely proportional to chain length. The limit is governed by an independent Poisson number of domain walls and an explicit crossing-pair product. It distinguishes long-range exponents at the summability boundary \(\alpha=2\), and a vanishing noise strength of order \(1/\log n\) produces an exact interpolation at that boundary.

For every integer \(n\ge2\), let \(D(x)=\#\{j\in\{1,\ldots,n-1\}:x_j\ne x_{j+1}\}\), for binary words \(x\in\{0,1\}^n\), and define the normalized state
\[
|\psi_{n,g}\rangle=\frac{1}{\sqrt{2(1+g)^{n-1}}}\sum_{x\in\{0,1\}^n}g^{D(x)/2}|x\rangle,\qquad g\ge0,
\]
where the value at \(g=0\) is the limiting GHZ state. For \(0\le p\le1\), and \(\alpha\in[0,1)\cup(1,\infty)\), apply the commuting quantum channel
\[
\mathcal E_{n,\alpha,p}=\prod_{1\le i<j\le n}\bigl[(1-a_{j-i})\operatorname{id}+a_{j-i}\operatorname{Ad}_{Z_iZ_j}\bigr],\qquad
 a_r=\begin{cases}p/(n^{1-\alpha}r^\alpha),&0\le\alpha<1,\\p/r^\alpha,&\alpha>1.\end{cases}
\]
Here \(\operatorname{Ad}_V(\rho)=V\rho V^\dagger\), and all channel probabilities lie in \([0,1]\). Let \(\rho_{n,g,\alpha,p}=\mathcal E_{n,\alpha,p}(|\psi_{n,g}\rangle\langle\psi_{n,g}|)\) and \(P_n(g,\alpha,p)=\operatorname{Tr}(\rho_{n,g,\alpha,p}^{2})\).

**Exact finite-size identity.** For \(h=2g/(1+g)^2\), let \(U\) be a binary word with uniformly fair first bit and independent successive bit flips, each of probability \(h\). Define \(C_r(U)=\#\{i\in\{1,\ldots,n-r\}:U_i\ne U_{i+r}\}\). Then
\[
P_n(g,\alpha,p)=\mathbb E_U\prod_{r=1}^{n-1}|1-2a_r|^{2C_r(U)}.\tag{1}
\]
The identity holds at all parameters specified above, including \(g=0\) and channel probabilities equal to \(1/2\).

**Dilute-domain-wall limit.** Fix \(\lambda\ge0\), put \(g_n=\lambda/n\), and fix \(p\in(0,1]\). Then
\[
\lim_{n\to\infty}P_n(g_n,\alpha,p)=\exp\!\left[-2\lambda\bigl(1-q_\alpha(p)\bigr)\right],
\qquad
q_\alpha(p)=\begin{cases}
0,&0\le\alpha<1\text{ or }1<\alpha\le2,\\
\displaystyle\prod_{r=1}^{\infty}|1-2p/r^\alpha|^{2r},&\alpha>2.
\end{cases}\tag{2}
\]
The infinite product converges for every \(\alpha>2\); it can be zero (notably at \(p=1/2\)). For \(p=0\), purity is exactly one for all chain lengths and all defined \(\alpha\).

**Marginal logarithmic window.** Fix \(\lambda,c\ge0\), choose \(\alpha=2\), and for all sufficiently large \(n\) put \(p_n=c/\log n\). Then
\[
\lim_{n\to\infty}P_n(g_n,2,p_n)
=\exp\!\left[-2\lambda\left(1-e^{-4c}\right)\right].\tag{3}
\]
This identifies a complete nontrivial crossover when the noise strength tends to zero at the inverse-logarithmic scale.

**Finite-size benchmarks.** For the nearest-neighbor-only version of the channel, denoted by \(\alpha=\infty\),
\[
P_n(g,\infty,p)=\left(1-\frac{8p(1-p)g}{(1+g)^2}\right)^{n-1}.\tag{4}
\]
For every \(\alpha>1\) and \(p=1/2\),
\[
P_n(g,\alpha,1/2)=\left(\frac{1+g^2}{(1+g)^2}\right)^{n-1}.\tag{5}
\]

## Assumptions and scope

The chain is open, with labeled sites \(1,\ldots,n\), and the input is the positive-amplitude branch \(g\ge0\) of the explicitly normalized family above. Its matrix-product representation is the one introduced in the first reference, with the symmetric boundary conditions of its Eq. (7). Pair channels act once per pair and commute because their Pauli conjugations are diagonal. The power-law convention excludes the undefined source exponent \(\alpha=1\); no assertion at that exponent is made. In Eq. (2), \(\lambda,p,\alpha\) are fixed as \(n\to\infty\); in Eq. (3), \(p=p_n\) is allowed to depend on \(n\). All limits are along integer chain lengths \(n\to\infty\), and none asserts convergence uniformly in those parameters.

## Proof

**Step 1: normalize and identify independent walls.** A binary word is specified by its first bit and its \(n-1\) wall indicators. There are \(2\binom{n-1}{k}\) words with exactly \(k\) walls. Consequently the squared coefficients of \(|\psi_{n,g}\rangle\) are
\[
\Pr(X=x)=\frac{g^{D(x)}}{2(1+g)^{n-1}},
\]
and \(X_1\) is fair while its wall indicators are independent Bernoulli variables with probability \(\theta=g/(1+g)\). These statements extend by continuity to \(g=0\).

**Step 2: obtain the exact pair-crossing formula.** Let \(X,Y\) be independent words sampled from the just-identified distribution, and put \(U=X\oplus Y\), bitwise. Acting on a density-matrix entry \(|x\rangle\langle y|\), the channel of a pair \(i<j\) multiplies it by \(1-2a_{j-i}\) precisely when \((x_i\oplus y_i)\ne(x_j\oplus y_j)\), and otherwise leaves it unchanged. Taking the Hilbert–Schmidt square gives
\[
P_n=\mathbb E_{X,Y}\prod_{i<j}\left|1-2a_{j-i}\right|^{2\mathbf1_{\{U_i\ne U_j\}}}.
\]
The wall on a bond of \(U\) is the exclusive-or of two independent Bernoulli-\(\theta\) walls. These exclusive-ors are independent across bonds and have probability \(h=2\theta(1-\theta)=2g/(1+g)^2\). The initial bit of \(U\) is uniform. Grouping the pairs by separation proves Eq. (1).

**Step 3: Poissonize the number of walls.** At \(g_n=\lambda/n\), one has \(h_n=2\lambda/n+O_\lambda(n^{-2})\). Hence \(K_n=D(U)\sim\mathrm{Binomial}(n-1,h_n)\) converges in distribution to a Poisson variable \(K\) of mean \(2\lambda\). Conditional on \(K_n=k\), the wall locations are uniformly distributed over the \(k\)-element subsets of the \(n-1\) bonds. For fixed \(k\), with probability approaching one their mutual separations and distances to both endpoints exceed \(\delta n\), provided \(\delta>0\) is chosen sufficiently small; more precisely, their rescaled locations converge jointly to the order statistics of \(k\) independent uniform points in \((0,1)\), which are distinct and interior almost surely.

**Step 4: control crossings.** A pair of sites with different \(U\) bits must span at least one wall. If \(U\) has \(k\) walls, this gives the deterministic bound \(0\le C_r(U)\le kr\), since a single wall can be straddled by at most \(r\) pairs separated by \(r\). When every wall is more than \(r\) bonds from both endpoints and from all other walls, each such pair spans only one wall, hence \(C_r(U)=kr\). On the fixed-\(k\) separated-wall events of Step 3, this equality holds for all \(1\le r\le\delta n\).

**Step 5: summable tails when \(\alpha>2\).** Fix \(p\in(0,1]\). Unless \(p=1/2\), all the numbers \(|1-2p/r^\alpha|\) are strictly positive. For sufficiently large \(r\), the magnitude of their logarithm is bounded by a constant times \(p/r^\alpha\); the crossing bound thus gives a uniform tail bound of order \(k\sum_{r>R}r^{1-\alpha}\), tending to zero as \(R\to\infty\). For every fixed \(R\) the separated-wall property gives \(C_r=kr\), so the finite product tends to \(q_\alpha(p)^k\). If \(p=1/2\), the factor at \(r=1\) vanishes whenever \(k>0\), giving the same conclusion with \(q_\alpha(1/2)=0\). This proves conditional convergence of the pair-crossing product to \(q_\alpha(p)^k\).

**Step 6: nonsummable tails when \(\alpha\le2\).** For \(1<\alpha\le2\), choose \(R\) sufficiently large that \(0<2p/r^\alpha<1\) for \(r\ge R\). For every fixed \(k\ge1\) on separated-wall configurations, the logarithm of the product is bounded above by
\[
-4pk\sum_{r=R}^{\lfloor\delta n\rfloor}r^{1-\alpha},
\]
which tends to minus infinity for \(\alpha\le2\). For \(0\le\alpha<1\), take \(\delta>0\) small enough and \(r\) in the macroscopic interval \([\delta n/2,\delta n]\), where again \(C_r=kr\). There are order \(n\) such separations and each \(a_r\) is bounded below by a positive constant divided by \(n\). Thus the log product is bounded above by a negative constant times \(n\), and also tends to minus infinity. If \(k=0\), the product equals one in every regime. Together, Steps 5 and 6 identify the conditional limit \(q_\alpha(p)^k\).

**Step 7: pass to the Poisson expectation.** Every product in Eq. (1) lies in \([0,1]\). Conditional convergence at every fixed \(k\), convergence of the binomial wall count to Poisson, and a uniform tail bound on \(K_n\) imply
\[
\lim_{n\to\infty}P_n=\mathbb E\bigl[q_\alpha(p)^K\bigr]
=\exp\bigl(2\lambda(q_\alpha(p)-1)\bigr),
\]
which proves Eq. (2), including \(\lambda=0\).

**Step 8: resolve the critical logarithmic window.** Set \(\alpha=2\) and \(p_n=c/\log n\). On the separated-wall configurations for fixed \(k\), the bound of Step 4 shows that
\[
\sum_{r=1}^{n-1}\frac{C_r}{r^2}=k\log n+O_{k,\delta}(1).
\]
Uniformly for large \(n\), Taylor expansion of the logarithms yields
\[
2\sum_{r=1}^{n-1}C_r\log\!\left(1-\frac{2c}{r^2\log n}\right)
=-\frac{4c}{\log n}\sum_{r=1}^{n-1}\frac{C_r}{r^2}
+O_{k,c}\!\left(\frac1{(\log n)^2}\sum_{r=1}^{\infty}r^{-3}\right).
\]
The error goes to zero, and the principal term tends to \(-4ck\). Hence the conditional product tends to \(e^{-4ck}\). Averaging over the limiting Poisson wall count proves Eq. (3).

**Step 9: check the finite-size benchmarks.** With only nearest-neighbor pair noise, Eq. (1) factorizes independently over the Bernoulli bond walls, each contributing \((1-h)+h|1-2p|^2=1-4p(1-p)h\), which yields Eq. (4). For \(\alpha>1\) and \(p=1/2\), the pair factor at distance one is zero whenever a wall is present, so the only surviving words have no walls. Their total probability is \((1-h)^{n-1}\), equal to Eq. (5).

## Verification

Run the companion standard-library-only Python program `verify_purity.py` with a Python 3 interpreter. It reconstructs matrix-product amplitudes directly from the source's two matrices and boundary vectors, computes the dephased finite density matrices independently, and compares their Hilbert–Schmidt purities with the wall expectation (1). It also tests the exact identities (4) and (5), directly enumerates pair crossings for every single-wall location in chains through length 24, and compares large finite single-wall products with the product and critical-window limits. The test invocation returned `VERIFY_OK 5095 MPS amplitudes, quantum-channel matrices, Markov-wall sums, and boundary products`.

These are finite corroborations of the analytic derivation; in particular they do not establish any infinite-volume limit without Steps 3–8. No numerical truncation of the infinite product is used as a theorem premise.

## Relationship to prior work

Fechisin, Lu, Wei, Shah, Wang, Gorshkov, and Lin define the matrix-product states, their symmetric boundary conditions, and the power-law dephasing channel (reference 1, Sec. II, Eqs. (1), (2), (7), (16), (17)). They observe numerically that choosing small fixed \(g\) raises global purity in experimentally relevant finite systems (Sec. V.3 and Fig. 5). Their Appendix G, Eqs. (125)–(132), **already derives the crossing-pair attenuation mechanism and its exponent-two summability boundary for a linear string operator**. This established mechanism is not claimed here as new. Their Appendix H, Eq. (137), gives an exact purity formula in the different product-state setting \(g=1,\alpha=0\). Their general doubled-state statistical-mechanics mapping informs the calculation but does not state the dilute \(g_n=\lambda/n\) purity limit or Eq. (3).

The present contribution is the exact global-purity representation (1), its Poisson asymptotics (2) for the dilute-wall family, and the critical vanishing-strength interpolation (3). These concern a quadratic mixed-state observable and differ from the source's linear string-order expectation and its fixed-parameter purity numerics. Earlier work on matrix-product quantum phase transitions (reference 2) concerns pure-state critical transfer structures rather than the same dephased purity limit; mixed-state quantum-channel constructions from measurement and feedback (reference 3) use a different channel. No claim of an unexplored generic exponent-two boundary is made.

## Limitations

The theorem applies to a special one-parameter open-chain input family and a single layer of independent commuting pair dephasings, not to arbitrary states or correlated channels. It excludes \(\alpha=1\) because the cited channel does not specify that normalization. Nonzero limiting global purity does **not** establish persistence of mixed SPT order, strong-to-weak symmetry breaking, a nonzero decoding rate, or a finite sampling advantage for every observable. The input parameter \(g_n\) approaches the pure-state critical point with system size, rather than staying in a fixed thermodynamic phase. The result does not prove uniformity in \(\lambda,p,\alpha\), nor analyze other microscopic noise, finite-rate preparation, or experimental imperfections. Exhaustive bibliographic priority is not asserted; equivalent unpublished or unindexed calculations remain possible.

## References

1. C. Fechisin, T.-C. Lu, Z.-Y. Wei, J. Shah, Y.-X. Wang, A. V. Gorshkov, C.-J. Lin, *Mixed-state phases induced by power-law quantum channels*, arXiv:2610.00480v1 (first public version 2026-09-30), https://arxiv.org/html/2610.00480v1 .
2. M. M. Wolf, G. Ortiz, F. Verstraete, J. I. Cirac, *Quantum phase transitions in matrix product systems*, arXiv:cond-mat/0512180v1 (2005), https://arxiv.org/abs/cond-mat/0512180 .
3. T.-C. Lu, Z. Zhang, S. Vijay, T. H. Hsieh, *Mixed-State Long-Range Order and Criticality from Measurement and Feedback*, PRX Quantum **4**, 030318 (2023), https://doi.org/10.1103/PRXQuantum.4.030318 .
