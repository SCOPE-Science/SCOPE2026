# A sharp real–complex cyclic Fourier–Sobolev dichotomy

## Finding
For every integer \(N\ge3\), let \(a:\mathbb Z/N\mathbb Z\to\mathbb R\) have \(\sum_{j=0}^{N-1}a_j=0\), with cyclic differences \((Da)_j=a_{j+1}-a_j\). The **optimal**, attained coefficient in
\[
\left(\sum_{j=0}^{N-1}|a_j|\right)^2\le \Lambda_N^{\mathbb R}\sum_{j=0}^{N-1}|a_{j+1}-a_j|^2
\]
is
\[
\boxed{\Lambda_N^{\mathbb R}=\begin{cases}N(N^2+8)/48,&N\text{ even},\\ (N^2-1)(N^2+7)/(48N),&N\text{ odd}.\end{cases}}
\]
For complex mean-zero sequences the optimal constant is instead
\[
\boxed{\Lambda_N^{\mathbb C}=\frac{N}{4\sin^2(\pi/N)}.}
\]
The real coefficient is strictly smaller than the complex one except when \(N=4\). Their optimal **norm** constants have the asymptotic ratio
\[
\lim_{N\to\infty}\sqrt{\Lambda_N^{\mathbb R}/\Lambda_N^{\mathbb C}}=\pi/\sqrt{12}.
\]

## Assumptions and scope
All sums use counting measure, not normalized averages; all indices are modulo \(N\). The real theorem applies to arbitrary real mean-zero sequences, with no positivity or support restriction. The complex theorem permits arbitrary complex mean-zero sequences. The two squared-norm constants concern the **same** first-order cyclic difference operator. No assertion is made about higher differences, other graphs, or equality classification of every real optimizer.

## Proof
**1. Green kernel and norm duality.** Write \(L=D^*D\) for the unnormalized cycle Laplacian. It has kernel equal to the constants and is positive definite on zero-mean real sequences. Its zero-mean inverse has entries \(G_N(j-k)\), where
\[
G_N(r)=\frac{N^2-1}{12N}-\frac{r(N-r)}{2N},\qquad r=0,1,\dots,N-1.
\]
Indeed \(\sum_{r=0}^{N-1}G_N(r)=0\) and the cyclic second-difference identity is
\(2G_N(r)-G_N(r-1)-G_N(r+1)=\mathbf1_{r=0}-1/N\).
The equality \(\|a\|_1=\max_{\sigma\in\{\pm1\}^N}\sum_j\sigma_ja_j\), followed by Cauchy–Schwarz in the \(L\)-energy inner product, gives the exact dual formula
\[
\Lambda_N^{\mathbb R}=\max_{\sigma\in\{\pm1\}^N}\sigma^TL^+\sigma.
\]
The maximum is exact: for any maximizing \(\sigma\), choose \(a=L^+\sigma\); the energy duality lower bound and the already proved universal upper bound coincide. If \(A=\{j:\sigma_j=1\}\) and \(|A|=m\), the zero row sums of \(G_N\) yield
\[
\sigma^TL^+\sigma=4\sum_{i,j\in A}G_N(i-j).
\]
The empty and full sets give zero and cannot maximize when \(N\ge3\).

**2. Why consecutive sign blocks optimize.** Regard the real circle as \(\mathbb R/N\mathbb Z\), put \(d_N(s)=\min_{k\in\mathbb Z}|s-kN|\in[0,N/2]\), and define the continuous, circularly symmetric kernel
\[
K_N(s)=\frac N{12}-\frac{d_N(s)(N-d_N(s))}{2N}.
\]
It is strictly decreasing in geodesic distance on \([0,N/2]\); adding \(N/24\) makes it nonnegative. For each vertex subset \(A\), let \(E_A=\bigcup_{j\in A}[j,j+1)\) as a subset of the circle. Integrating the quadratic on each off-diagonal unit-square and the absolute-distance expression on the diagonal gives exactly
\[
\iint_{E_A\times E_A}K_N(x-y)\,dx\,dy
=\sum_{i,j\in A}G_N(i-j)+\frac{m(m-N)}{6N}.
\]
For completeness, off-diagonal integrals equal \(G_N(i-j)+1/(6N)\), while diagonal integrals equal \(G_N(0)-(N-1)/(6N)\). These follow from \(\mathbb E(U-V)^2=1/6\) and \(\mathbb E|U-V|=1/3\) for independent uniform \(U,V\in[0,1]\). The additive correction depends only on \(m\).

The **circle Riesz rearrangement inequality** for a nonnegative radial nonincreasing kernel says that, among measurable subsets of fixed length \(m\), the displayed double integral is maximized by an interval of length \(m\). Applying it to \(K_N+N/24\) is legitimate because the additive constant contributes the same \((N/24)m^2\) for all sets of measure \(m\). That interval can be taken as \([0,m)\), which is exactly the union of \(m\) consecutive unit cells. Therefore a consecutive \(A\) maximizes the *discrete* quadratic form at every cardinality; no discrete rearrangement equality theorem is needed.

**3. Evaluate the blocks and optimize cardinality.** For \(A=\{0,\dots,m-1\}\), each distance \(h\in\{1,\dots,m-1\}\) occurs as an ordinary positive index difference \(m-h\) times, in both orders. Consequently
\[
\sum_{i,j\in A}r_{ij}(N-r_{ij})
=2\sum_{h=1}^{m-1}(m-h)h(N-h)
=\frac{m(m^2-1)(2N-m)}6,
\]
where \(r_{ij}\) is the residue of \(i-j\) in \(\{0,\dots,N-1\}\). Substitution into the Green kernel yields
\[
4\sum_{i,j\in A}G_N(i-j)
=\frac{m(N-m)\,[m(N-m)+2]}{3N}.
\]
This is strictly increasing in \(m(N-m)>0\). Thus the maximizing block length is \(m=\lfloor N/2\rfloor\) or \(\lceil N/2\rceil\), giving the stated even and odd constants. For an explicit real extremizer, fix such a block \(A\), put \(\sigma=2\mathbf1_A-\mathbf1\), and take \(a_j=2\sum_{k\in A}G_N(j-k)\). It is mean-zero, satisfies \(La=\sigma-\overline\sigma\mathbf1\), and equality follows from the exact dual formula above.

**4. Complex coefficient and strict field gap.** Fourier characters of the cycle diagonalize \(L\). On the mean-zero subspace its smallest eigenvalue is \(4\sin^2(\pi/N)\). Thus
\[
\|a\|_1\le\sqrt N\,\|a\|_2\le\frac{\sqrt N}{2\sin(\pi/N)}\,\|Da\|_2.
\]
Both equalities hold for the first nonconstant character \(a_j=e^{2\pi i j/N}\), proving \(\Lambda_N^{\mathbb C}\). If a *real* nonzero vector attained this complex sharp constant, equality in both steps would require all \(|a_j|\) to be equal and \(a\) to lie in the real first-eigenvalue space. Hence \(a_j\in\{\pm c\}\) for some \(c>0\), and its eigenvector recurrence demands \(2\cos(2\pi/N)\in\{-2,0,2\}\). For \(N\ge3\), this happens only for \(N=4\); the block formula gives equality there. Otherwise the real constant is strictly smaller. Taking the leading cubic asymptotics yields the asserted \(\pi/\sqrt{12}\) norm-constant ratio.

## Verification
The accompanying standard-library Python program `verify.py` uses exact rational arithmetic to check the cyclic Green identity, exact unit-cell integration identities, interval-block formula, maximizing sign vectors on small complete cycles, and exact extremizing profiles across many larger cycles. Its finite checks supplement—not replace—the circle rearrangement theorem and the universal algebra above. The complex constant follows analytically from Fourier spectral diagonalization.

## Relationship to prior work
Frank and Ivanisvili (arXiv:2605.29035v1, first public May 27, 2026) establish a sharp logarithmic Sobolev inequality on finite cycles using a cubic inequality and the cycle's Fourier spectral gap. Chen, Lam and Lu (arXiv:2610.05347v1, first public October 4, 2026) establish sharp *quartic stability* for that logarithmic inequality. Neither gives a sharp linear first-difference **real \(\ell^1\)-to-\(\ell^2\)** embedding or its comparison with complex scalars. The later zero-boundary discrete \(\ell^1\)-to-\(\ell^2\) theorem of Hindov–Nitzan–Olsen–Rydhe (arXiv:2610.19010v1, October 13, 2026) uses sequences extended by zero, not periodic mean-zero sequences; its constants and boundary conditions do not imply the present cyclic formula. Classical cyclic \(\ell^2\) Wirtinger inequalities concern a different left-hand norm; their first Fourier eigenspaces provide the complex benchmark here. The circle Riesz rearrangement theorem is a **cited established input**, not a claimed new result.

## Limitations
The proof uses the standard circle Riesz rearrangement theorem. It does not characterize all real extremizers beyond explicitly constructed ones. The numerical script is finite and cannot establish universal validity. An indexed literature search cannot exclude older unindexed formulations of the exact cyclic \(\ell^1\) constant; historical priority remains a material risk. Independent validation has not been performed.

## References
1. Rupert L. Frank and Paata Ivanisvili, *The sharp log Sobolev inequality on finite cycles*, arXiv:2605.29035v1, May 27, 2026. https://arxiv.org/abs/2605.29035
2. Lu Chen, Nguyen Lam and Guozhen Lu, *Sharp uniform stability of the logarithmic Sobolev inequality on finite cycles and stability of the cubic Sobolev inequality*, arXiv:2610.05347v1, October 4, 2026. https://arxiv.org/abs/2610.05347
3. Raul Hindov, Shahaf Nitzan, Jan-Fredrik Olsen and Eskil Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1, October 13, 2026. https://arxiv.org/abs/2610.19010
4. Jarmila Novotná, *Variations of discrete analogues of Wirtinger's inequality*, Časopis pro pěstování matematiky 105 (1980), 278–285. https://doi.org/10.21136/CPM.1980.118070
5. Albert Baernstein II, *Convolution and rearrangement on circle*, Complex Variables 12 (1989), 33–37. https://doi.org/10.1080/17476938908814351
6. Xavier Cabré, Gyula Csató and Albert Mas, *Periodic solutions to integro-differential equations: variational formulation, symmetry, and regularity*, arXiv:2404.06462, especially its discussion of the circle Riesz rearrangement theorem. https://arxiv.org/abs/2404.06462
7. A. A. Ilyin, A. Laptev and S. Zelik, *Sharp interpolation inequalities for discrete operators and applications*, Bulletin of Mathematical Sciences 5 (2015), 19–57. https://doi.org/10.1007/s13373-014-0060-8
