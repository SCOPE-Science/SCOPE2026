# Infinite expected conditioning in two-column Gaussian-sketched biorthogonalization

## Finding

For the Gaussian-sketch two-sided Gram--Schmidt process with a finite number \(s\ge2\) of sketch rows, a nonparallel first input pair has a sharply heavy-tailed first normalization. More consequentially, there are two-column input matrices with **orthonormal columns individually** and an ordinary, well-conditioned cross-Gram matrix for which the random output basis has **infinite expected spectral condition number**. This happens for every fixed finite sketch size, even when more sketch rows than ambient dimensions are used. The statement is about the random output of the specified unsafeguarded, signed, real normalization; it does not say that a typical realization is badly conditioned.

For unit \(x,y\in\mathbb R^n\), write \(c=x^{\mathsf T}y\) and \(Z=(\Omega x)^{\mathsf T}(\Omega y)\), where \(\Omega\) has independent \(N(0,1/s)\) entries. If \(|c|<1\), the density at zero exists and is
\[
f_Z(0)=\frac{s\,\Gamma(s-1)}{2^{s-1}\Gamma(s/2)^2}(1-c^2)^{(s-2)/2}>0.
\]
In particular \(f_Z(0)=1\) when \(s=2\), independent of the nontrivial angle. Hence \(\mathbb E|Z|^{-p}<\infty\) holds exactly when \(0<p<1\). If \(q_1=x/\sqrt{|Z|}\), then \(\mathbb E\|q_1\|_2^r<\infty\) holds exactly when \(0<r<2\). When \(|c|=1\), the corresponding threshold is \(0<r<s\).

For the fixed two-column matrices
\[
X=[e_1,e_3],\qquad Y=[(e_1+e_2)/\sqrt2,e_3]\in\mathbb R^{n\times2},\qquad n\ge3,
\]
both \(X^{\mathsf T}X=Y^{\mathsf T}Y=I_2\) and \(Y^{\mathsf T}X=\operatorname{diag}(1/\sqrt2,1)\). Nevertheless, the Gaussian-sketched two-sided Gram--Schmidt output \(Q\) after two columns satisfies, for every finite integer \(s\ge2\),
\[
\mathbb P\bigl(\kappa_2(Q)>t\bigr)\ge\frac{C_s}{t}\quad(t\ge t_s),
\qquad \mathbb E\bigl[\kappa_2(Q)^r\bigr]=+\infty\quad(r\ge1),
\]
for finite positive constants \(C_s,t_s\) depending on \(s\). The nonsketched, symmetrically normalized two-sided Gram--Schmidt output for these same inputs has finite condition number \(2^{1/4}\).

## Assumptions and scope

Fix integers \(n\ge3\), \(s\ge2\). Let \(\Omega\in\mathbb R^{s\times n}\) have independent centered real Gaussian entries of variance \(1/s\). All operations use exact arithmetic. By "signed real normalization", for any nonzero real pivot \(d=(\Omega \widetilde q)^{\mathsf T}(\Omega\widetilde p)\), we take \(q=\widetilde q/\sqrt{|d|}\) and \(p=\operatorname{sign}(d)\widetilde p/\sqrt{|d|}\), so that \((\Omega q)^{\mathsf T}(\Omega p)=1\). The first and second unnormalized columns use the sketched oblique projectors of Algorithm 3.1 in Grigori--Piccinini--Simunec. This explicitly fixes the real-valued signed-normalization convention used for both signs of a nonzero pivot.

The spectral condition number \(\kappa_2(Q)\) means the ratio of the largest to smallest nonzero singular value of the full-rank \(n\times2\) matrix \(Q\). Random zero pivots have probability zero for the fixed inputs below. No Gaussian subspace-embedding event is conditioned upon. For the first-pivot general formula, \(x\) and \(y\) are unit vectors and \(c\in[-1,1]\), with \(|c|=1\) treated separately.

## Proof

**First-pivot distribution.** For \(|c|<1\), set \(u=(x+y)/\sqrt{2(1+c)}\) and \(v=(x-y)/\sqrt{2(1-c)}\). These vectors are orthonormal. Independent Gaussian rotational invariance gives independent \(U,V\sim\chi_s^2\) satisfying
\[
Z\overset{\mathrm d}=\frac{(1+c)U-(1-c)V}{2s}.
\]
Equivalently, the positive summands have gamma densities with common shape \(k=s/2\) and scales \(\theta_+=(1+c)/s\), \(\theta_-=(1-c)/s\). Their difference has continuous density at zero for \(s\ge2\), equal to the convolution integral
\[
\frac{1}{\Gamma(k)^2\theta_+^k\theta_-^k}
\int_0^\infty t^{2k-2}\exp[-t(1/\theta_++1/\theta_-)]\,dt
=\frac{s\Gamma(s-1)}{2^{s-1}\Gamma(s/2)^2}(1-c^2)^{(s-2)/2}.
\]
The integrand is nonnegative, and its behavior at zero and infinity gives a bounded density near zero. Since the density is positive and continuous there, \(\mathbb E|Z|^{-p}\) is finite precisely for \(0<p<1\): the integral near zero is comparable on both sides to \(\int_0^1 t^{-p}\,dt\), while outside the unit interval its integrand is at most one. At \(|c|=1\), one has \(|Z|=U/s\), so the chi-square density behaves as \(t^{s/2-1}\) at zero and the inverse-moment threshold is \(p<s/2\). First-column norms are \(|Z|^{-1/2}\), giving the stated thresholds for all \(r>0\).

**Two-column conditioning.** Let \(x_1=e_1\), \(y_1=(e_1+e_2)/\sqrt2\) and \(x_2=y_2=e_3\). For compact notation set \(a=\Omega x_1\), \(b=\Omega y_1\), \(g=\Omega e_3\) and write
\[
z=a^{\mathsf T}b,\quad h=b^{\mathsf T}g,\quad k=a^{\mathsf T}g,\quad v=g^{\mathsf T}g.
\]
These three sketched vectors have a joint nondegenerate Gaussian density on \((\mathbb R^s)^3\): their unsketched generating vectors are linearly independent. The first signed normalization followed by the second sketched biorthogonal projection gives the **unnormalized** next columns
\[
\widetilde q_2=e_3-(h/z)e_1,
\qquad \widetilde p_2=e_3-(k/z)y_1,
\qquad d=(\Omega\widetilde q_2)^{\mathsf T}(\Omega\widetilde p_2)=v-hk/z.
\]
The identities hold for \(z\ne0\); the second pivot \(d\ne0\) almost surely, since \(zd=zv-hk\) is a polynomial that is nonzero at, for example, \(a=e_1,b=e_1,g=e_2\) in sketch coordinates. In the orthonormal physical coordinate frame \([e_1,e_3]\), the two output columns form the upper-triangular matrix
\[
\begin{pmatrix}
|z|^{-1/2}&-h/(z\sqrt{|d|})\\
0&|d|^{-1/2}
\end{pmatrix}.
\]
Therefore \(|\det Q_{\mathrm{frame}}|=1/\sqrt{|zd|}\) and \(\sigma_{\max}(Q)\ge |z|^{-1/2}\). Since, for a nonsingular two-by-two matrix, \(\sigma_{\min}=|\det|/\sigma_{\max}\),
\[
\kappa_2(Q)=\sigma_{\max}(Q)^2\sqrt{|zd|}\ge\sqrt{|d|/|z|}.
\]

**Quantitative lower tail.** For any fixed finite \(s\ge2\), the joint Gaussian density of \((a,b,g)\) is strictly positive and continuous near the point \((e_1,e_2,e_1+e_2)\) of sketch space. Choose a small bounded open neighborhood there on which \(h\ge1/2\), \(k\ge1/2\), \(v\le10\), and the first coordinate of \(a\) is at least \(1/2\). Whenever also \(0<|z|<1/80\),
\[
|d|=|v-hk/z|\ge1/(8|z|),\qquad
\kappa_2(Q)\ge 1/(\sqrt8|z|).
\]
Inside a sufficiently small rectangular neighborhood, \(z=a^{\mathsf T}b\) is a transverse local coordinate: its derivative with respect to the first coordinate of \(b\) is the first coordinate of \(a\), uniformly bounded away from zero. Integrating the joint density over fixed-width transverse coordinates and an interval \(|z|<\varepsilon\) therefore yields, for sufficiently small \(\varepsilon>0\),
\[
\mathbb P\bigl((a,b,g)\text{ belongs to this neighborhood},\ 0<|z|<\varepsilon\bigr)\ge c_s\varepsilon
\]
for some \(c_s>0\). Combining the last two inequalities proves \(\mathbb P(\kappa_2(Q)>t)\ge C_s/t\) for all sufficiently large \(t\). The tail integral identity
\[
\mathbb E\kappa_2(Q)^r=r\int_0^\infty t^{r-1}\mathbb P(\kappa_2(Q)>t)\,dt
\]
then diverges for every \(r\ge1\). Finally, the unsketched pivot is \(1/\sqrt2\), and its second sketched-free pivot is \(1\). The corresponding basis is \([2^{1/4}e_1,e_3]\), hence has condition number \(2^{1/4}\), confirming the example is not created by ill-conditioned deterministic input bases. This finishes the proof.

## Verification

Run `python verify.py` under Python 3 with the standard library. It checks the gamma-convolution density coefficient by independent numerical integration, exactly verifies the Schur-complement pivot \(d=v-hk/z\) and triangular-Gram condition lower bound on rational input triples, and exhibits rational near-breakdown sequences with condition growth at least inverse-linear in \(|z|\). The execution reported `VERIFY_OK: 986 exact Schur-complement and triangular-Gram tests; 25 density quadratures; 48 near-breakdown witnesses`. Numerical quadrature does not prove the gamma identity; finite rational examples do not prove the lower probability-tail bound. Those facts are proved analytically above.

## Relationship to prior work

Grigori, Piccinini and Simunec (2025, arXiv:2509.04386, Algorithm 3.1 and Proposition 4.1) introduced and analyzed randomized two-sided Gram--Schmidt, including a uniform upper small-ball bound of order \(s\delta\) for Gaussian sketched inner products and experiments showing typically improved conditioning. They quote the standard Bessel-function density for a **single** product of correlated Gaussians. The exact density **of the sum of products** at zero, its sharp inverse-moment cutoff, and the stated two-column unconditional condition-number lower tail do not follow from an upper small-ball estimate alone and are not stated there. Simoncini and Wang (2025) analyze sketched and whitened nonsymmetric Krylov recurrences; that construction is distinct from the signed two-sided pivot normalization used here. The normal/gamma and inverse-moment calculations use established probability identities and are not claimed to introduce a new probability law in isolation.

## Limitations

The result concerns exact-arithmetic Gaussian sketches with a fixed finite sketch size, no conditioning on a successful subspace embedding, no rejection or truncation of small pivots, and only the unsafeguarded two-column process. A large or infinite mean does not imply a high-probability practical failure; robust numerical implementations may use safeguards or reorthogonalization. The result establishes a lower tail for output conditioning, not an exact condition-number distribution or a general positive-moment threshold for conditioning below first order. The normalization is stated explicitly for either pivot sign. Full historical equivalence searches are necessarily bounded; older results for ratios of correlated Gaussian products could encode an equivalent special case.

## References

1. L. Grigori, L. Piccinini, and I. Simunec. *Randomized biorthogonalization through a two-sided Gram--Schmidt process*. arXiv:2509.04386v1 (first posted 4 September 2025), Algorithm 3.1, Proposition 4.1, Section 6 and Appendix A. https://arxiv.org/pdf/2509.04386
2. V. Simoncini and Y. Wang. *Stabilized Krylov Subspace Recurrences via Randomized Sketching*. Numerical Linear Algebra with Applications 32 (2025), e70022. https://doi.org/10.1002/nla.70022
