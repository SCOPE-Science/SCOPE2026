# Horocyclic Toeplitz symbol tomography on homogeneous trees with a sharp inverse constant

## Finding
Fix an integer \(q\ge2\) and \(\alpha>1\). On the combinatorial-harmonic Bergman space of the \((q+1)\)-regular tree with horocyclic measure, every bounded horocycle-dependent multiplication symbol \(\varphi:\mathbb Z\to\mathbb C\) has a **diagonal** Toeplitz compression. Its labelled diagonal sequence is an explicitly invertible one-sided convolution. The inverse has the **sharp** uniform norm
\[
\kappa(q,\alpha)=\frac{(1+r)(1+rs)^2(1+rs^2)}{(1-r)(1-rs)^2(1-rs^2)},
\qquad r=q^{1-\alpha},\quad s=q^{-1}.
\]
More precisely, if \(P_\alpha\) is the orthogonal harmonic Bergman projection and \(T_\varphi=P_\alpha M_{\varphi\circ h}|_{\mathcal B^2_\alpha}\), then with \(S\varphi(k)=\varphi(k+1)\),
\[
\begin{split}
\Lambda\varphi(k)&=\frac{1}{W(1)}\sum_{m\ge1}r^m(1-s^m)^2\varphi(k+m),\\
W(z)&=\sum_{m\ge1}r^m(1-s^m)^2z^m
=\frac{r(1-s)^2z(1+rsz)}{(1-rz)(1-rsz)(1-rs^2z)}.
\end{split}
\]
The eigenvalue of \(T_\varphi\) on each wavelet rooted at horocyclic index \(k\) is \(\Lambda\varphi(k)\). Each such eigenvalue has infinite multiplicity, hence
\[
\sigma(T_\varphi)=\sigma_{\mathrm{ess}}(T_\varphi)
=\overline{\{\Lambda\varphi(k):k\in\mathbb Z\}},\qquad
\|T_\varphi\|=\|\Lambda\varphi\|_\infty.
\]
The map \(\Lambda:\ell^\infty(\mathbb Z)\to\ell^\infty(\mathbb Z)\) is a bounded linear bijection, with exact inverse
\[
\Lambda^{-1}=\frac{W(1)}{r(1-s)^2}\,S^{-1}(I-rS)(I-rsS)(I-rs^2S)(I+rsS)^{-1}.
\]
In particular, uniformly for **all bounded complex** symbols,
\[
\boxed{\kappa(q,\alpha)^{-1}\|\varphi\|_\infty\le\|T_\varphi\|\le\|\varphi\|_\infty.}
\]
Both constants are attained. Constants attain the upper bound, and \(\varphi(k)=(-1)^k\) attains the lower bound. The family of horocyclic Toeplitz compressions is precisely the algebra of bounded diagonal operators that act by a common scalar on all wavelets rooted at a given horocyclic index. It is therefore a commutative unital \(C^*\)-algebra; its nonzero elements are never compact. **The spectrum as an unlabelled set does not generally recover the symbol:** reconstruction requires the eigenvalue profile indexed by \(k\).

## Assumptions and scope
Let \(\mathcal X_q\) be the infinite \((q+1)\)-regular tree, choose an end \(\omega\), and denote by \(p(v)\) the parent toward \(\omega\) and by \(S(v)\) its \(q\) forward children. Normalize a horocyclic index \(h:\mathcal X_q\to\mathbb Z\) by \(h(x)=h(v)+1\) for \(x\in S(v)\). Define
\[
\sigma_\alpha(v)=q^{-\alpha h(v)},\qquad
\mathcal B^2_\alpha=\left\{f\in\ell^2(\mathcal X_q,\sigma_\alpha):
(q+1)f(v)=f(p(v))+\sum_{x\in S(v)}f(x)\ \forall v\right\}.
\]
All statements hold for each integer \(q\ge2\), each real \(\alpha>1\), and every \(\varphi\in\ell^\infty(\mathbb Z)\), with no positivity or periodicity assumptions. Here \(\sigma_{\mathrm{ess}}\) is the Fredholm essential spectrum. The eigenvalue profile retains the labels of the horocycles, not merely the unordered spectrum.

## Proof
**1. Levelwise orthogonality of the known basis.** By Theorem 14 and Corollary 15 of De Mari–Monti–Rizzo [1], a complete orthogonal family consists of harmonic wavelets \(g_{v,j}\), one for each vertex \(v\) and each of \(q-1\) orthonormal zero-sum child vectors \(a_{v,j}\). At a descendant \(x\) a distance \(m\ge1\) below \(v\), if \(x\) lies below the first child \(i\), the wavelet is
\[
g_{v,j}(x)=c_m a_{v,j}(i),\qquad
c_m=\sum_{t=0}^{m-1}q^{-t}=\frac{1-s^m}{1-s};
\]
and \(g_{v,j}\) is zero outside the strict forward cone of \(v\). There are \(q^{m-1}\) descendants below each first child at distance \(m\). Consequently the total squared wavelet amplitude at level \(h(v)+m\) is exactly \(q^{m-1}c_m^2\).

Crucially, distinct wavelets are orthogonal **separately on every horocycle**, not only after summing across horocycles. For disjoint cones the assertion is immediate. If the wavelet roots coincide, orthogonality holds at each level by \(\sum_i a_{v,j}(i)\overline{a_{v,j'}(i)}=0\). For nested roots, the ancestral wavelet has the same value on all descendants of the lower root within any fixed horocycle, whereas the lower wavelet sums to zero on that horocycle because \(\sum_i a_{w,j}(i)=0\). This establishes the levelwise cancellation rigorously in all cases. Thus every bounded horocycle multiplier remains diagonal after compression.

**2. Exact diagonal and spectrum.** The norm calculation is
\[
\|g_{v,j}\|^2=\sum_{m\ge1}q^{-\alpha(h(v)+m)}q^{m-1}c_m^2
=\frac{q^{-\alpha h(v)}}{q(1-s)^2}W(1).
\]
The same calculation with the extra factor \(\varphi(h(v)+m)\) gives the claimed diagonal eigenvalue \(\Lambda\varphi(h(v))\), independently of \(j\) and \(v\) at the same level. Theorem 14 gives completeness. Every horocycle contains infinitely many roots, so each displayed value occurs with infinite multiplicity. The standard spectral theorem for bounded diagonal operators gives exactly the claimed ordinary and Fredholm essential spectra and norm. In particular a nonzero compression cannot be compact.

**3. Exact transfer function and inversion.** Expanding \((1-s^m)^2\) and summing three convergent geometric series yields
\[
W(z)=\frac{rz}{1-rz}-\frac{2rsz}{1-rsz}+\frac{rs^2z}{1-rs^2z}
=\frac{r(1-s)^2z(1+rsz)}{(1-rz)(1-rsz)(1-rs^2z)}
\]
for \(|z|\le1\). Since \(\|rS\|,\|rsS\|,\|rs^2S\|<1\) and \(\|rsS\|<1\), the factors in the displayed formula for \(\Lambda^{-1}\) act boundedly on \(\ell^\infty(\mathbb Z)\), and multiplication of commuting factors proves \(\Lambda^{-1}\Lambda=\Lambda\Lambda^{-1}=I\).

**4. Sharp inverse norm.** Put
\[
Q(z)=\frac{(1-rz)(1-rsz)(1-rs^2z)}{1+rsz}.
\]
All Taylor coefficients of \(Q(-z)=(1+rz)(1+rsz)(1+rs^2z)/(1-rsz)\) are strictly positive, so the coefficients of \(Q(z)\) alternate in sign. The \(\ell^\infty\) norm of an absolutely summable bilateral-shift convolution is the \(\ell^1\) norm of its coefficients (choose an input matching their signs at one output coordinate). Hence
\[
\|\Lambda^{-1}\|=\frac{W(1)}{r(1-s)^2}Q(-1)
=\frac{(1+r)(1+rs)^2(1+rs^2)}{(1-r)(1-rs)^2(1-rs^2)}=\kappa(q,\alpha).
\]
This is attained by the alternating sequence because \(\Lambda((-1)^k)=\frac{W(-1)}{W(1)}(-1)^k=-\kappa^{-1}(-1)^k\). As \(W\) has nonnegative coefficients and \(\Lambda1=1\), \(\|\Lambda\|=1\); this proves both sharp inequalities. The diagonal form and surjectivity imply the full block-constant diagonal algebra claim. No equality is asserted between \(T_\varphi T_\psi\) and \(T_{\varphi\psi}\): the symbol product is instead transported through \(\Lambda^{-1}\).

**5. Parameter behavior.** For fixed \(q\), expansion of the exact product shows
\[
\kappa(q,\alpha)\sim\frac{2(1+s)^2(1+s^2)}{(1-s)^2(1-s^2)(\alpha-1)\log q}
\quad(\alpha\downarrow1),
\]
and
\[
\kappa(q,\alpha)=1+2(1+s)^2q^{1-\alpha}+O(q^{2(1-\alpha)})
\quad(\alpha\to\infty).
\]
These show a sharp degeneration of uniform symbol recovery at the Bergman-weight endpoint.

## Verification
The supplied `checker.py` uses symbolic polynomial identities to check the rational transfer function and inverse constant. It also directly enumerates finite-depth tree wavelets to verify levelwise Gram cancellations, tests the inverse sign pattern at rational parameters and compares truncated convolution against the exact alternating extremizer for sixteen parameter pairs. Running `python checker.py` reports `PASS`. These finite checks are supplementary: completeness and all infinite-dimensional assertions follow from the wavelet basis and the analytical argument above.

For a concrete exactly reproducible case, \(q=2\), \(\alpha=2\) gives \(r=s=1/2\), \(W(1)=10/21\), \(W(-1)=-2/45\), and \(\kappa=75/7\). The alternating symbol then has compressed norm \(7/75\), while its own supremum norm equals \(1\).

## Relationship to prior work
De Mari, Monti and Rizzo [1] establish the complete orthogonal harmonic-wavelet basis and the Bergman projection, which are essential prior inputs. The new step is orthogonality **on each individual horocycle** and the resulting full Toeplitz symbol-to-diagonal transfer, rational convolution inverse, sharp stability and operator-algebra classification. Sections 3–5 and Theorem 14 of [1] do not formulate this invertible Toeplitz-symbol theorem. Ottazzi and Santagati [2] study a different **forward/probabilistic Laplacian** on locally finite trees and obtain boundedness of other Toeplitz-type kernels; their estimates do not give the above combinatorial-harmonic compression spectrum. Published diagonal Bergman or Fock Toeplitz results use other spaces and parameters. Searches for equivalent formulations and possible inherited implications remain subject to historical-priority uncertainty.

## Limitations
The tree is homogeneous, the harmonicity is for the **combinatorial** Laplacian, \(\alpha>1\), and symbols depend only on the horocyclic index. The inverse estimate concerns the **labelled eigenvalue sequence** \(k\mapsto\Lambda\varphi(k)\); the unordered spectral set alone cannot identify \(\varphi\). The results do not assert stability to arbitrary changes in the wavelet basis or non-horocyclic symbols, and no claims are made about nonsymmetric trees or the weight endpoint \(\alpha=1\). Prior publication could contain an unindexed equivalent or stronger specialization. Independent mathematical validation has not been performed.

## References
[1] F. De Mari, M. Monti, E. Rizzo, *Horocyclic harmonic Bergman spaces on homogeneous trees*, arXiv:2309.15047v1, first public 2023-09-26, especially Section 3, Theorem 14 and Corollary 15. https://arxiv.org/pdf/2309.15047

[2] A. Ottazzi, F. Santagati, *Harmonic Bergman spaces on locally finite trees*, arXiv:2505.03479v1, first public 2025-05-06, especially Introduction and Section 3 on forward-harmonic Toeplitz-type operators. https://arxiv.org/pdf/2505.03479
