# Negative covariance across two levels of metastability in a random-bond Ising ring

## Finding
For every integer \(n\ge 11\), put independent identically distributed positive continuous random couplings \(J_0,\ldots,J_{n-1}\) on the edges of the periodic Ising chain, and let \(S_1\) and \(S_2\) count configurations for which every flip of respectively one spin, or any connected block of one or two spins, *strictly raises* the Hamiltonian. Then, with natural logarithms,
\[
\mathbb E\begin{pmatrix}\log S_1\\ \log S_2\end{pmatrix}
=n\log 2\begin{pmatrix}1/3\\1/5\end{pmatrix},
\quad
\operatorname{Cov}\begin{pmatrix}\log S_1\\ \log S_2\end{pmatrix}
=n(\log 2)^2
\begin{pmatrix}2/45&-1/315\\-1/315&13/450\end{pmatrix}.
\]
In particular, the covariance of the logarithms is **strictly negative for every \(n\ge11\)**, although \(S_2\le S_1\) for every coupling realization. The correlation is exactly
\[
-\frac{1/315}{\sqrt{(2/45)(13/450)}}\approx-0.0885962389923.
\]
The centered vector divided by \(\sqrt n\log2\) converges in distribution, as \(n\to\infty\), to the nondegenerate centered bivariate normal with the displayed rational covariance matrix. All statements are universal over atomless iid positive bond distributions.

## Assumptions and scope
The vertex indices and bond indices lie in \(\mathbb Z/n\mathbb Z\). A spin configuration is \(\sigma_i\in\{-1,+1\}\), with Hamiltonian
\[H(\sigma)=-\sum_{i=0}^{n-1}J_i\sigma_i\sigma_{i+1}.\]
For \(k\in\{1,2\}\), a configuration is \(k\)-stable if flipping every nonempty contiguous block of at most \(k\) spins strictly increases \(H\). For \(k=2\), requiring strict increase also for *all* two-spin subsets is equivalent: flips at nonadjacent sites have additive positive single-site energy increments. The atomless iid hypothesis excludes equal coupling values almost surely, and no finite moment assumption on couplings is needed. Results concern the number of potential metastable configurations, not their dynamical attraction probabilities.

For \(k\in\{1,2\}\), define the weak-bond indicator
\[I_i^{(k)}=\mathbf1\{J_i<J_{i+d}\ \text{for every }d\in\{-k,\ldots,-1,1,\ldots,k\}\},\qquad M_k=\sum_i I_i^{(k)}.\]

## Proof
**1. Exact weak-bond representation.** Put \(\tau_i=\sigma_i\sigma_{i+1}\). For a contiguous block of \(\ell\) spins, its two boundary edges \(a-1\) and \(a+\ell-1\) are precisely the bonds whose satisfaction signs change, giving
\[\Delta H=2\bigl(J_{a-1}\tau_{a-1}+J_{a+\ell-1}\tau_{a+\ell-1}\bigr).\]
Call a bond with \(\tau_i=-1\) a wall. If two walls were separated by \(1\le d\le k\) bonds, flipping the intervening \(d\) spins would lower energy. If a wall at \(i\) were next to a satisfied bond at distance \(1\le d\le k\) with \(J_{i+d}<J_i\), the corresponding block flip would lower energy as well. Thus every wall is a strict radius-\(k\) minimum of the coupling landscape. Conversely, radius-\(k\) minima cannot occur within \(k\) bonds of one another. Hence for every block of length at most \(k\), either both boundary bonds are satisfied (positive increment), or there is one wall and the other bond is stronger (again positive). This proves the exact characterization.

The product \(\prod_i\tau_i=1\) forces the number of walls to be even, and each admissible even wall set gives two spin configurations, interchanged by global spin reversal. There is at least one radius-\(k\) minimum (the global minimum). Therefore
\[S_k=2\sum_{j\text{ even}}\binom{M_k}{j}=2^{M_k},\qquad k=1,2.\]
This is a finite-volume identity, not an asymptotic approximation.

**2. Disorder means and exact local pair probabilities.** For iid atomless couplings, every ordering of a finite set of distinct bonds has equal probability, so \(\mathbb E I_i^{(k)}=1/(2k+1)\). Write \(p_{rs}(d)=\mathbb P(I_0^{(r)}=I_d^{(s)}=1)\), for \(r,s\in\{1,2\}\) and nonnegative separations \(d\le r+s\). The complete required table is

| \((r,s)\) | \(p_{rs}(0)\) | \(p_{rs}(1)\) | \(p_{rs}(2)\) | \(p_{rs}(3)\) | \(p_{rs}(4)\) |
|---|---|---|---|---|---|
| \((1,1)\) | \(1/3\) | \(0\) | \(2/15\) | — | — |
| \((1,2)\) | \(1/5\) | \(0\) | \(1/18\) | \(8/105\) | — |
| \((2,2)\) | \(1/5\) | \(0\) | \(0\) | \(1/20\) | \(2/45\) |

At larger distances the windows are disjoint and the indicators independent. Here is a direct integral derivation of the nontrivial entries, rather than reliance on a numerical table. By the probability-integral transform the \(J_i\) can be taken iid uniform on \((0,1)\). Conditioning on the two central values \(x,y\) gives
\[
\begin{aligned}
p_{11}(2)&=\int_0^1\!\int_0^1(1-x)(1-y)[1-\max(x,y)]\,dx\,dy=2/15,\\
p_{12}(2)&=\int_0^1\!\int_0^x(1-x)^2(1-y)^2\,dy\,dx=1/18,\\
p_{12}(3)&=\int_0^1\!\int_0^1(1-x)(1-y)^3[1-\max(x,y)]\,dx\,dy=8/105,\\
p_{22}(3)&=\int_0^1\!\int_0^1(1-x)^2(1-y)^2[1-\max(x,y)]^2\,dx\,dy=1/20,\\
p_{22}(4)&=\int_0^1\!\int_0^1(1-x)^3(1-y)^3[1-\max(x,y)]\,dx\,dy=2/45.
\end{aligned}
\]
The zero entries for neighboring centers follow from incompatible inequalities. The same-site entry for \((1,2)\) is \(1/5\) because radius-two minimality implies radius-one minimality. For \(n\ge11\), cyclic wrapping introduces no exceptional local-overlap identifications. Summing the finitely many nonzero displacement covariances,
\[
\frac{1}{n}\operatorname{Var}(M_1)=\frac{2}{45},\qquad
\frac{1}{n}\operatorname{Cov}(M_1,M_2)=-\frac{1}{315},\qquad
\frac{1}{n}\operatorname{Var}(M_2)=\frac{13}{450}.
\]
Combining with \(\log S_k=(\log2)M_k\) proves the finite-size formulas and negative sign.

**3. Joint Gaussian limit.** Construct iid couplings on the doubly infinite chain. The bounded stationary vector process \((I_i^{(1)},I_i^{(2)})\) is 4-dependent, since its value depends only on the five couplings with indices \(i-2,\ldots,i+2\). The standard central limit theorem for stationary bounded finite-dependent sequences, applied to every linear combination and followed by Cramér–Wold, gives a bivariate Gaussian with covariance equal to the displacement sum computed above. Replacing the infinite-chain windows by cyclic windows changes only a bounded number of indicators near a chosen cut, so after \(\sqrt n\)-normalization this difference vanishes. The determinant \((2/45)(13/450)-(1/315)^2>0\) ensures nondegeneracy.

## Verification
The standalone `verify_nested_stability.py` reconstructs the Hamiltonian independently for each spin configuration, enumerates all single-spin and adjacent-pair flips, and checks \(S_k=2^{M_k}\) in 144 tests across sizes 5–10 and random distinct coupling permutations. It enumerates all relative orders on each critical union of local windows to check the five nontrivial rational probabilities, reconstructs all three covariance coefficients, and independently enumerates all \(9!\) cyclic bond rankings to check the finite exact covariance matrix at \(n=9\). Run with `python verify_nested_stability.py` using Python 3 standard library. These finite tests do not replace the infinite-volume CLT proof.

## Relationship to prior work
Newman and Stein, *Metastable States in Spin Glasses and Disordered Ferromagnets* (arXiv:cond-mat/9908455v1, 1999), discuss weak-bond isolation and the previously known \(2^{n/3}\) typical one-spin metastable-state scale; their Section 5 also discusses two-spin-flip stability through dynamics. Those are established results, not claimed here. Masui, Southern, and Jacobs (1989) studied one-spin metastable-state distributions in random Ising chains. Wacław and Burda (2008) studied one-spin stable-state numbers on arbitrary graphs using Gaussian-coupling methods. The finding here concerns the **joint disorder law of two nested stability levels**: the exact *negative* cross-covariance and the associated bivariate limit, neither implied by a one-level count or a separate marginal normal approximation. The local weak-bond correspondence is used as a starting point, not claimed as an independent discovery.

## Limitations
Only iid atomless positive couplings and ring lengths \(n\ge11\) are covered by the displayed exact finite covariance formulas. The joint CLT concerns the zero-field count of *potential* strictly stable states, not their basin sizes, dynamics, or energy distributions. It does not extend as stated to correlated or tied bond strengths. The nonstandard exact cross-window overlap calculation was checked analytically and by exhaustive finite ranking enumeration; no claim of independent auditing is made. Earlier work could conceivably contain a specialized equivalent covariance identity under other terminology: the full 1989 Masui–Southern–Jacobs article could not be inspected, although its available abstract concerns one-spin distributions rather than two-level covariance.

## References
1. C. M. Newman and D. L. Stein, *Metastable States in Spin Glasses and Disordered Ferromagnets*, arXiv:cond-mat/9908455v1 (first posted 1999-08-30), https://arxiv.org/abs/cond-mat/9908455.
2. S. Masui, B. W. Southern, and A. E. Jacobs, *Metastable states of Ising spin glasses and random ferromagnets*, Phys. Rev. B **39** (1989), 6925–6933, https://doi.org/10.1103/PhysRevB.39.6925.
3. B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224v1 (2008), https://arxiv.org/abs/0801.1224.
4. S. Schnabel and W. Janke, *Counting metastable states of Ising spin glasses on hypercubic lattices*, Eur. Phys. J. B **93** (2020), 53, https://doi.org/10.1140/epjb/e2020-100480-4.
5. W. Hoeffding and H. Robbins, *The central limit theorem for dependent random variables*, Duke Math. J. **15** (1948), 773–780, https://doi.org/10.1215/S0012-7094-48-01568-3.
