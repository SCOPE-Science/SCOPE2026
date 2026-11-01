# Exact Fourier sampling spectra and a thin-side conditioning transition for bipartite colourings

## Finding
For integers \(q\ge3\) and \(r,s\ge1\), let \(\Omega_{r,s,q}\) be the set of all proper \(q\)-colourings of the complete bipartite graph \(K_{r,s}\), with the uniform probability measure. Identify colours with \(\mathbb Z/q\mathbb Z\). Take the constant function and, for each vertex \(v\) and nonzero frequency \(t\in\{1,\ldots,q-1\}\), the character \(\phi_{v,t}(c)=\exp(2\pi i t c_v/q)\). Their probability-normalized Gram matrix is positive definite, and its complete spectrum is given explicitly below.

Define \(Z_{r,s}=\sum_{k=1}^{\min(r,q-1)}(q)_k\,S(r,k)(q-k)^s\), where \(S(\cdot,\cdot)\) is a Stirling number of the second kind and \((q)_k=q!/(q-k)!\). For \(r>1\) put \(\rho_A=(q Z_{r-1,s}/Z_{r,s}-1)/(q-1)\), and set \(\rho_A=0\) for \(r=1\); similarly for \(s>1\) put \(\rho_B=(q Z_{r,s-1}/Z_{r,s}-1)/(q-1)\), and set \(\rho_B=0\) for \(s=1\). Define \(a=1+(r-1)\rho_A\), \(b=1+(s-1)\rho_B\), and
\[
\mu_\pm=\frac{a+b\pm\sqrt{(a-b)^2+4rs/(q-1)^2}}2.
\]
The spectrum consists of the value \(1\) once, \(1-\rho_A\) with multiplicity \((r-1)(q-1)\), \(1-\rho_B\) with multiplicity \((s-1)(q-1)\), and each of \(\mu_-\) and \(\mu_+\) with multiplicity \(q-1\). Zero-multiplicity sectors are omitted and coincident levels have summed multiplicity. Every listed positive-multiplicity eigenvalue is strictly positive.

A sharp asymptotic distinction holds for fixed \(q\ge3\) and fixed \(r\ge1\), with \(s\to\infty\). The squared singular-value condition number of the complete frame satisfies
\[
\kappa_{1,s,q}^2\sim\frac{s^2}{q(q-2)(q-1)^2},
\]
whereas for each fixed \(r\ge2\),
\[
\boxed{\ \kappa_{r,s,q}^2\sim\frac{s}{q\,2^{r-2}(q-1)^2}\left(\frac{q-1}{q-2}\right)^s.\ }
\]
Thus increasing the smaller side from one vertex to two changes the order of squared conditioning from quadratic to exponential in the other part's size. The exact finite-size condition number is the quotient of the largest to smallest eigenvalues in the displayed spectrum.

## Assumptions and scope
Both sides of \(K_{r,s}\) have strictly positive cardinalities. A proper colouring assigns distinct colours to endpoints of every edge; equivalently, the sets of colours appearing on the two sides are disjoint. For \(q\ge3\) this support is nonempty, as required for the uniform probability law. Gram entries use \(\mathbb E[\overline{f}g]\); the corresponding singular values are the square roots of the Gram eigenvalues. The characters form a subfamily of the standard degree-one Fourier basis on \((\mathbb Z/q\mathbb Z)^{r+s}\), without any non-prime restriction on \(q\). No normalization factors beyond the probability average are imposed. For \(r=1\) or \(s=1\), the corresponding within-side sector has multiplicity zero and its auxiliary \(\rho\) value has no statistical meaning.

## Proof
**Colouring count.** If precisely \(k\) distinct colours occur on side \(A\), there are \((q)_k S(r,k)\) onto maps from its \(r\) vertices to the selected labelled colours; every vertex on side \(B\) may independently receive any of the remaining \(q-k\) colours. Summing over \(1\le k\le\min(r,q-1)\) gives \(Z_{r,s}\). Identifying the colours at any two distinct vertices of the first side produces exactly the proper colourings of \(K_{r-1,s}\), so for \(r\ge2\) their equality probability is \(Z_{r-1,s}/Z_{r,s}\). By symmetry the corresponding probability on side \(B\) is \(Z_{r,s-1}/Z_{r,s}\); an across-side equality has probability zero.

**Frequency blocks.** Simultaneously permuting the \(q\) colour labels leaves the measure invariant. Hence each individual colour is uniform. For distinct vertices \(v,w\) let \(p\) be their colour-equality probability. Their joint law is \(p/q\) on each diagonal ordered colour pair and \((1-p)/(q(q-1))\) on each off-diagonal ordered pair. Summing roots of unity gives, for nonzero frequencies \(t,u\),
\[
\mathbb E[\overline{\phi_{v,t}}\phi_{w,u}]
=\mathbf1_{t=u}\frac{qp-1}{q-1}.
\]
For identical vertices the corresponding moment equals \(\mathbf1_{t=u}\). The constant function is orthogonal to every nonconstant character. Consequently each of the \(q-1\) frequency blocks equals
\[
M=\begin{pmatrix}
(1-\rho_A)I_r+\rho_A J_r&-J_{r,s}/(q-1)\\
-J_{s,r}/(q-1)&(1-\rho_B)I_s+\rho_B J_s
\end{pmatrix}.
\]
The spaces of coordinate contrasts inside the two parts have eigenvalues \(1-\rho_A\), respectively \(1-\rho_B\). On the normalized constant vectors of the two sides, \(M\) acts as
\[
\begin{pmatrix}a&-\sqrt{rs}/(q-1)\\-\sqrt{rs}/(q-1)&b\end{pmatrix},
\]
whose eigenvalues are the stated \(\mu_\pm\). This gives all \(1+(r+s)(q-1)\) Gram eigenvalues, counting multiplicities.

**Strict positivity for every finite parameter.** Suppose a constant plus a linear combination of the nonconstant one-site Fourier characters vanishes on all proper colourings. Fourier inversion on each one-site alphabet rewrites it as \(c+\sum_v h_v(c_v)=0\), where each \(h_v\) has zero average over \(\mathbb Z/q\mathbb Z\). Fix any colour \(b\) at every vertex on side \(B\) and arbitrarily choose permitted colours for the other vertices on side \(A\). Varying one \(A\) coordinate forces its \(h_v\) to take the same value on the \(q-1\) colours different from \(b\). As \(q\ge3\), any pair of colours can be simultaneously different from some \(b\); therefore \(h_v\) is globally constant, hence zero. Repeat with the sides reversed to see that every \(B\)-side \(h_v\) vanishes, and finally \(c=0\). Thus the Gram matrix is positive definite, including its less obvious two-dimensional sector.

**Asymptotic distinction.** Fix \(q\ge3\) and \(r\ge1\), and set \(\tau=(q-2)/(q-1)<1\). In the colouring formula the \(k=1\) term is \(q(q-1)^s\), and all \(k\ge2\) terms are smaller by at least \(O(\tau^s)\). Hence \(\rho_A\to1\) when \(r\ge2\), and \(\rho_B\to(q-1)^{-2}\); correspondingly \(a\to r\), \(b/s\to(q-1)^{-2}\), and the largest spectral value satisfies \(\mu_+\sim s/(q-1)^2\). Its partner follows from the determinant identity \(\mu_+\mu_-=ab-rs/(q-1)^2\): using the exponentially fast convergence of \(\rho_A\) and \(\rho_B\), this determinant converges to \(r(1-(q-1)^{-2})\), so \(\mu_-\sim r q(q-2)/s\). Further, when \(r\ge2\), the two first terms of the Stirling expansion give
\[
Z_{r,s}-Z_{r-1,s}\sim q(q-1)\bigl(S(r,2)-S(r-1,2)\bigr)(q-2)^s
=q(q-1)2^{r-2}(q-2)^s.
\]
Therefore \(1-\rho_A=q(Z_{r,s}-Z_{r-1,s})/((q-1)Z_{r,s})\sim q2^{r-2}\tau^s\), which is eventually the smallest eigenvalue, because \(1-\rho_B\) tends to a positive constant and \(\mu_-\) decays only like \(1/s\). This proves the exponential formula. For \(r=1\), the \(A\)-contrast sector does not exist; in fact \(\rho_B=(q-1)^{-2}\) exactly, and \(\mu_-\sim q(q-2)/s\) is the smallest eigenvalue. Combining with \(\mu_+\) gives the quadratic formula. These asymptotics are pointwise for fixed \(r,q\), not uniform as they grow.

## Verification
The included standalone `verify.py` (Python 3 and NumPy) enumerates proper colourings for \(q\in\{3,4,5\}\) and \(1\le r,s\le3\). It checks the chromatic count and all two-site equality probabilities exactly, then forms the complex Fourier evaluation matrix independently and compares its complete numerical Gram spectrum to the theorem. It also tests the leading exponential term for ninety larger parameter choices using exact rational counting. Reproduce with `python3 verify.py`. The observed completion message is `VERIFY_OK cases=27 colour_pairs=180 eigenvalues=324 words=6630 asymptotic_cases=90`. The proof above establishes the infinite family; no finite check is used to infer an unproved universal assertion.

## Relationship to prior work
Borgs and Chayes studied covariance eigenspaces of Potts spins in ordered and disordered phases on lattice models and their random-cluster representation; their formula for colour-symmetric two-point functions is a useful context. Their lattice correlation-length and boundary-condition results do not calculate the across-all-sites, finite-support first Fourier-band Gram spectrum for proper colourings of \(K_{r,s}\), nor the asymptotic contrast-mode transition proved here. Gebhard and Sagan developed noncommutative chromatic symmetric functions, encompassing colour-pattern enumerators, but their graph-polynomial theorems do not give the present spectral decomposition or conditioning result. Ehler developed general probabilistic tight frames and random frame theory, and Thill--Hassibi constructed group Fourier frames; neither paper states the finite complete-bipartite proper-colouring spectrum. The counting formula and the colour-permutation decomposition are elementary classical ingredients, not claimed as novel in isolation.

## Limitations
The theorem covers only the constant-plus-degree-one Fourier family and only the uniform measure on proper colourings of complete bipartite graphs; no analogous claim is made for higher Fourier degrees or general graphs. The condition-number asymptotics hold when \(q\) and the thinner-side size \(r\) are fixed. The exact Gram eigenvalues are given for all finite parameters, but no globally sharp finite-parameter conditioning maximum is asserted. A historical spin-covariance or graph-colouring formula expressed using different terminology could imply the result; the inspected works do not show such an implication, and exhaustive historical priority is not established. Independent validation has not been performed.

## References
1. C. Borgs and J. T. Chayes, *The covariance matrix of the Potts model: A random cluster analysis*, arXiv:adap-org/9411001v1, first public 1994-11-14, especially Sections 1 and 3.2. https://arxiv.org/html/adap-org/9411001v1
2. D. D. Gebhard and B. E. Sagan, *A Noncommutative Chromatic Symmetric Function*, arXiv:math/9907076v1, first public 1999-07-12, especially Sections 1 and 3. https://arxiv.org/html/math/9907076v1
3. M. Ehler, *Random Tight Frames*, arXiv:1102.4080v1, first public 2011-02-20; primary MSC 42C15. https://arxiv.org/html/1102.4080v2
4. M. Thill and B. Hassibi, *Low-Coherence Frames from Group Fourier Matrices*, arXiv:1509.05739v1, first public 2015-09-18. https://arxiv.org/html/1509.05739v1
