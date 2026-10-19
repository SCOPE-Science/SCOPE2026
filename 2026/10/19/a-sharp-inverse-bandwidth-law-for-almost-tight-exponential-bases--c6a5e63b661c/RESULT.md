# A sharp inverse-bandwidth law for almost-tight exponential bases on a nonspectral three-segment measure

## Finding
Let \(\mathcal L\) denote Lebesgue measure and define the probability measure
\[
\mu=\frac13\,\mathcal L|_{[0,1]}\otimes(\delta_0+\delta_1+\delta_{\sqrt2})
\]
on three disjoint horizontal segments in \(\mathbb R^2\). For each real \(t\), set
\[
\mathcal E_t=\{e^{2\pi i(nx+jty)}:n\in\mathbb Z,\ j\in\{0,1,2\}\}.
\]
If \(\mathcal E_t\) is a Riesz basis for \(L^2(\mu)\), let \(\kappa(t)\) be its **optimal** upper-to-lower squared-norm Riesz-bound ratio; otherwise let \(\kappa(t)=+\infty\). For \(R>0\), define the optimal vertical-coset-bandwidth ratio
\[
K(R)=\inf_{0<2|t|\le R}\kappa(t).
\]
The following assertions hold together:

1. The measure \(\mu\) is **not spectral**. Indeed, every orthogonal family of exponentials in \(L^2(\mu)\) is incomplete.
2. For every real \(t\), \(\kappa(t)>1\), whereas \(\inf_{t\in\mathbb R}\kappa(t)=1\). There exist absolute constants \(c,C,R_0>0\) such that
\[
1+\frac cR\le K(R)\le1+\frac CR\qquad(R\ge R_0).
\]
Thus the inverse-bandwidth exponent is exact **within the stated three-coset family**, despite nonspectrality.
3. For the explicit integer sequences \(p_j,q_j\) defined for \(j\ge0\) by
\[
p_j+q_j\sqrt2=(2+\sqrt2)(17+12\sqrt2)^j,
\]
the systems \(\mathcal E_{q_j/3}\) are Riesz bases for every sufficiently large \(j\), and their leading deterioration is exactly
\[
\lim_{j\to\infty}q_j\bigl(\kappa(q_j/3)-1\bigr)=\frac{4\pi}{3\sqrt3}.
\]

## Assumptions and scope
The measure has total mass one, with three **distinct** parallel unit-length segments at heights \(0,1,\sqrt2\). The frequencies in \(\mathcal E_t\) consist of three vertical cosets \(0,t,2t\), combined with every horizontal integer. The bandwidth \(R\) controls *only* their vertical displacement, not the unbounded horizontal integer frequencies. Riesz bounds refer to the synthesis inequality for all square-summable coefficients. The theorem does not minimize over arbitrary exponential Riesz bases with unrelated frequency patterns.

Put \(h_0=0,h_1=1,h_2=\sqrt2\), and define the normalized three-by-three matrix
\[
V(t)_{kj}=\frac{e^{2\pi i jt h_k}}{\sqrt3},\quad 0\le k,j\le2,
\qquad G(t)=V(t)^*V(t).
\]
Write \(\lambda_-(t),\lambda_+(t)\) for its extremal eigenvalues. When \(V(t)\) is invertible, \(\kappa(t)=\lambda_+(t)/\lambda_-(t)\).

## Proof
**Tensor reduction.** Fourier series in \(x\in[0,1]\) identify \(L^2(\mu)\) with the Hilbert direct sum of three-dimensional fibers indexed by \(n\in\mathbb Z\). The three vectors within each fiber are exactly the columns of \(V(t)\). Consequently, completeness and the Riesz property are respectively equivalent to invertibility of \(V(t)\), and its optimal squared Riesz bounds are the smallest and largest eigenvalues of \(G(t)\).

**Absolute obstruction to orthogonality.** The vertical Fourier factor is
\[
\widehat\nu(u)=\frac{1+e^{-2\pi iu}+e^{-2\pi i\sqrt2u}}3.
\]
A sum of three unit complex numbers can vanish only when the last two, in some order, are the two primitive cube roots of unity. If \(\widehat\nu(u)=0\), this forces both \(3u\) and \(3\sqrt2u\) to be integers not divisible by three, impossible by irrationality of \(\sqrt2\). Thus \(\widehat\nu\) has **no real zero**. On the other hand,
\[
\widehat\mu(\xi,u)=\left(\int_0^1e^{-2\pi i\xi x}\,dx\right)\widehat\nu(u),
\]
so orthogonal distinct exponential frequencies must have horizontal difference in \(\mathbb Z\setminus\{0\}\). Their horizontal frequencies lie in a single translated integer lattice, with at most one frequency at each integer. In the associated horizontal Fourier decomposition, each occupied channel therefore contains at most one vector in a three-dimensional fiber. Every such orthogonal family is incomplete. In particular \(G(t)\ne I\) for every \(t\), so every finite \(\kappa(t)>1\).

**A universal inverse-bandwidth obstruction.** Let \(\zeta=e^{2\pi i/3}\), and consider the smooth map on the two-torus
\[
F(u,v)=1+e^{2\pi iu}+e^{2\pi iv}.
\]
Its only zeros modulo integers are \((1/3,2/3)\) and \((2/3,1/3)\). At each zero its real two-by-two derivative is invertible, with absolute determinant \(2\pi^2\sqrt3\). By local invertibility at both zeros and compactness elsewhere, there are absolute \(\eta,C_0>0\) such that \(|F(u,v)|<\eta\) implies the existence of integers \(q,p\), respectively congruent to \(1,2\) or \(2,1\) modulo three, satisfying
\[
|3u-q|+|3v-p|\le C_0|F(u,v)|.
\]
(Here \(u,v\) are unwrapped real variables, and the lifted zero neighborhoods are used.)

Every diagonal entry of \(G(t)\) equals one, so its eigenvalues average to one. If \(\kappa(t)=1+\delta<\infty\), the extreme eigenvalues lie between \((1+\delta)^{-1}\) and \(1+\delta\); hence \(\|G(t)-I\|\le\delta\). An off-diagonal entry equals \(F(t,\sqrt2t)/3\) (up to conjugation), and therefore \(|F(t,\sqrt2t)|\le3\delta\). If \(\delta\) is below a fixed absolute threshold, the preceding lemma gives integers \(q,p\) of complementary nonzero cube-root residues with
\[
|3t-q|+|3\sqrt2t-p|\le3C_0\delta.
\]
Since \(p^2-2q^2\) is a nonzero integer,
\[
|p-\sqrt2q|=\frac{|p^2-2q^2|}{|p+\sqrt2q|}\ge\frac1{|p|+\sqrt2|q|}.
\]
The two approximation inequalities imply \(|p-\sqrt2q|\le C_1\delta\), while \(2|t|\le R\) implies \(|p|+\sqrt2|q|\le C_2(1+R)\). Thus \(\delta\ge c_1/(1+R)\). If \(\delta\) exceeds the fixed threshold, the same lower bound holds after reducing \(c_1\). Therefore \(K(R)\ge1+c/R\) for all sufficiently large \(R\).

**Constructive matching rate.** Define \(p_0=2,q_0=1\) and
\[
p_{j+1}=17p_j+24q_j,\qquad q_{j+1}=12p_j+17q_j.
\]
They satisfy \(p_j^2-2q_j^2=2\), while their residue classes modulo three alternate between \((p_j,q_j)\equiv(2,1)\) and \((1,2)\). Consequently at \(t_j=q_j/3\), the phases \(e^{2\pi it_j}\) and \(e^{2\pi i\sqrt2t_j}\) approach the two distinct cube roots of unity, and
\[
|\sqrt2q_j-p_j|=\frac2{p_j+\sqrt2q_j}=O(q_j^{-1}).
\]
Hence \(G(t_j)=I+O(q_j^{-1})\) in operator norm and \(\kappa(t_j)=1+O(q_j^{-1})\); in particular these matrices are invertible for all large \(j\). Since \(p_j/q_j\le2\), the recurrence gives \(q_{j+1}\le41q_j\). For each sufficiently large \(R\), choose the largest \(j\) with \(2q_j/3\le R\). Then \(q_j\ge3R/82\) and therefore \(K(R)\le1+C/R\). The same Pell family shows \(\inf_t\kappa(t)=1\), but the obstruction above shows this infimum is never attained.

**Exact coefficient on the Pell sequence.** In the case \(q_j\equiv1\pmod3\), let \(\theta_j=2\pi(\sqrt2q_j-p_j)/3\). A first-order expansion gives
\[
G(q_j/3)=I+\frac{\theta_j}{3}H+O(\theta_j^2),\qquad
H=\begin{pmatrix}0&i\zeta^2&2i\zeta\\-i\zeta&0&i\zeta^2\\-2i\zeta^2&-i\zeta&0\end{pmatrix}.
\]
The Hermitian matrix \(H\) has trace zero, determinant zero and \(\operatorname{tr}(H^2)=12\), and hence eigenvalues \(-\sqrt6,0,\sqrt6\). The complementary residue case is its conjugate orientation and has the same eigenvalue deviations. Thus
\[
\kappa(q_j/3)-1=\frac{2\sqrt6}{3}|\theta_j|+O(\theta_j^2).
\]
Because \(q_j(p_j-\sqrt2q_j)\to1/\sqrt2\), multiplication by \(q_j\) yields the claimed constant \(4\pi/(3\sqrt3)\).

## Verification
The accompanying `VERIFY.py` checks the exact Pell invariant and residue alternation for an initial range, the exact Hermitian expansion-matrix characteristic polynomial, and high-precision Gram eigenvalues with the predicted limiting coefficient. Run `python VERIFY.py` with Python 3 and installed `sympy` and `mpmath`. It is a reproducibility check, **not** a replacement for the torus inverse-function argument or the all-bandwidth Diophantine proof.

## Relationship to prior work
Sha Wu, *Spectrality of Weighted Measures on Two Line Segments* (arXiv:2609.27364v1, publicly posted September 23, 2026), proves density rigidity and characterizes spectrality for two parallel weighted segments; its Corollary 2 gives a necessary common-density condition for any finite parallel family. The present measure satisfies that condition but is nonetheless nonspectral, and the quantitative Riesz-conditioning law is a different assertion not supplied by those results.

Kolountzakis, Shi and Wu (arXiv:2512.19872) classify two-segment spectra and exhibit larger spectral collections without line spectra. Their Section 4 bounds the growth of **orthogonal** sets, not near-orthogonal Riesz ratios on a three-segment nonspectral measure.

Kolountzakis and C.-K. Lai (arXiv:2507.00581) prove non-spectrality for certain closed polygonal and intersecting three-ray geometries; those configurations are different from three disjoint parallel segments and supply no Riesz-ratio estimate.

Ferguson, Mayeli and Sothanaphan (arXiv:1904.04487) develop quantitative Riesz ratios for **finite abelian-group subsets**. Their near-spectral finite framework motivates a spectrality-versus-conditioning distinction but does not yield the real irrational three-fiber inverse-bandwidth assertion. Kolountzakis, C.-K. Lai, Kailing Lai and Li (arXiv:2607.01500) establish a product spectrality equivalence under hypotheses encompassing an interval factor, but this is qualitative; their complete manuscript was not available for a whole-text comparison.

## Limitations
The rate \(K(R)-1\asymp R^{-1}\) is proved only for the explicitly defined three-coset product Fourier bases, not for **all** conceivable exponential Riesz bases or all possible frequency-density constraints. No exact closed formula for \(K(R)\) at individual values of \(R\) is claimed. The leading coefficient is proved only along the displayed Pell subsequence. An equivalence in unindexed prior work remains possible; independent review has not been performed.

## References
1. Sha Wu, *Spectrality of Weighted Measures on Two Line Segments*, arXiv:2609.27364v1 (September 23, 2026), especially Theorem 3 and Corollary 2. https://arxiv.org/abs/2609.27364
2. M. N. Kolountzakis, R. Shi, S. Wu, *Spectra for finite unions of line segments*, arXiv:2512.19872 (2025), especially Sections 1, 3, 4. https://arxiv.org/abs/2512.19872
3. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487 (2019), especially Sections 1, 5. https://arxiv.org/abs/1904.04487
4. M. N. Kolountzakis, C.-K. Lai, K. Lai, J. Li, *Spectrality of factors of product spectral measures*, arXiv:2607.01500 (2026), abstract. https://arxiv.org/abs/2607.01500
5. M. N. Kolountzakis and C.-K. Lai, *Non-spectrality of some piecewise smooth curves and unions of line segments*, arXiv:2507.00581 (2025), Theorem 1. https://arxiv.org/abs/2507.00581
