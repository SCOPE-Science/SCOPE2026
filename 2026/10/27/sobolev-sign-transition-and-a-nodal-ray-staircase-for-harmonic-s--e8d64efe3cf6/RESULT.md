# Sobolev-sign transition and a nodal-ray staircase for harmonic Steklov kernels

## Finding
Let \(\mathcal H_\sigma\) be the real reproducing-kernel Hilbert space of harmonic functions on the unit disk obtained by completing real harmonic polynomials for the boundary Fourier norm
\[
\|h\|_\sigma^2=a_0^2+\frac12\sum_{n=1}^\infty(n+1)^\sigma(a_n^2+b_n^2),\qquad \sigma\in\mathbb R,
\]
where \(h(re^{i\phi})=a_0+\sum_{n\ge1}r^n(a_n\cos n\phi+b_n\sin n\phi)\). At a pair of disk points the kernel depends on \(z=x\overline y\in\mathbb D\) through
\[
K_\sigma(z)=1+2\sum_{n=1}^\infty(n+1)^{-\sigma}\operatorname{Re}(z^n)
=2\operatorname{Re}\frac{\operatorname{Li}_\sigma(z)}z-1,
\]
with the quotient continued at \(z=0\) by \(1\).

**Sharp positivity transition.** For every real \(\sigma\ge0\), \(K_\sigma(z)>0\) at every \(|z|<1\). For every real \(\sigma<0\) and every neighborhood of \(z=1\) within the disk, \(K_\sigma\) has both signs and a zero. Thus the zero-free parameter range is exactly \([0,\infty)\).

**Complete boundary-local nodal census and first drift.** Fix \(\sigma<0\) with \(\sigma\notin\{-2,-4,-6,\ldots\}\), and put \(\mu=1-\sigma>1\). Define
\[
J_\mu=\{j\in\mathbb Z_{\ge0}:2j+1<\mu\},\qquad
\theta_j=\frac{(2j+1)\pi}{2\mu}.
\]
There is \(\varepsilon_\sigma>0\) such that for every \(0<\rho<\varepsilon_\sigma\), the entire kernel-zero set on the **interior** of the small circle \(|1-z|=\rho\) consists of exactly \(2|J_\mu|\) distinct points
\[
z_{j,\pm}(\rho)=1-\rho e^{\pm i\Theta_j(\rho)},\qquad j\in J_\mu,
\]
with \(0<\Theta_j(\rho)<\arccos(\rho/2)\). They lie on real-analytic nonsingular nodal arcs for \(0<\rho<\varepsilon_\sigma\), and satisfy the **first-order angular law**
\[
\Theta_j(\rho)=\theta_j+\left(\frac1\mu-\frac12\right)\sin(\theta_j)\,\rho+o(\rho).
\]
Hence the boundary-local nodal-arc count (two sides together) is
\[
2|J_\mu|=2\left\lceil\frac{-\sigma}{2}\right\rceil
\qquad(\sigma<0,\ \sigma\notin-2\mathbb N).
\]
The excluded negative even integers are **grazing-exponent boundaries** of this stable-count formula; the global positivity transition still applies to them. No assertion of the exact arc count is made at those exponents.

## Assumptions and scope
All Fourier coefficients, real Hilbert-space inner products, and kernels use the normalization displayed above. The completion permits generalized boundary traces when \(\sigma<0\); nevertheless every interior evaluation is continuous because \(\sum_{n\ge1}(n+1)^{-\sigma}r^{2n}<\infty\) for \(r<1\). The kernel formula applies to all pairs \(x,y\in\mathbb D\); every \(z\in\mathbb D\) is realizable as \(x\overline y\), for example by choosing \(|x|=|y|=\sqrt{|z|}\). The nodal census concerns \(|1-z|=\rho\) intersected with the *open disk*, not the full Euclidean circle or the entire global zero set.

## Proof
**1. Kernel normalization.** The constant harmonic function has squared norm one. For each integer \(n\ge1\), the real harmonic basis vectors \(r^n\cos(n\phi)\) and \(r^n\sin(n\phi)\) have squared norm \((n+1)^\sigma/2\). Summing their evaluation rank-one kernels gives \(1+2\sum_{n\ge1}(n+1)^{-\sigma}\operatorname{Re}(z^n)\). Polynomial growth of its coefficients proves locally uniform convergence for every real \(\sigma\); this both identifies the reproducing kernel and establishes the claimed interior regularity of the Hilbert-space completion.

**2. Positivity for all nonnegative orders.** At \(\sigma=0\), the series is the Poisson kernel
\[
K_0(z)=\frac{1-|z|^2}{|1-z|^2}>0.
\]
For \(\sigma>0\) define the probability measure on \((0,1)\)
\[
d\nu_\sigma(s)=\frac{(-\log s)^{\sigma-1}}{\Gamma(\sigma)}\,ds.
\]
Gamma integration gives \(\int_0^1s^n\,d\nu_\sigma(s)=(n+1)^{-\sigma}\). Interchanging an absolutely and locally uniformly convergent series with this probability integral yields
\[
K_\sigma(z)=\int_0^1\frac{1-s^2|z|^2}{|1-sz|^2}\,d\nu_\sigma(s)>0
\]
for every \(|z|<1\). Positivity is strict because the integrand is strictly positive.

**3. Uniform complex-power expansion.** Put \(w=1-z\) and \(\mu=1-\sigma>1\). The standard local polylogarithm expansion at its branch point, with \(\lambda=-\log z\) on the principal branch, reads
\[
\operatorname{Li}_\sigma(z)=\Gamma(\mu)\lambda^{-\mu}+\zeta(\sigma)+O(\lambda),
\qquad \lambda=w+\tfrac12 w^2+O(w^3).
\]
For every fixed real \(\sigma<0\), this expansion is locally convergent for small nonzero \(\lambda\) in the slit neighborhood relevant to \(|z|<1\), including negative-integer orders. Multiplication by \(z^{-1}=(1-w)^{-1}\) yields
\[
\frac{\operatorname{Li}_\sigma(z)}z
=\Gamma(\mu)w^{-\mu}\left[1+\left(1-\frac\mu2\right)w+O(w^2)\right]+O(1).
\]
The remainders and their derivatives with respect to \(\arg w\) are uniform for \(w=\rho e^{i\theta}\) with \(|\theta|\le\pi/2\), as \(\rho\downarrow0\). Indeed all remainder functions are analytic in a common slit neighborhood, and the differentiated power series are uniformly bounded on this closed angular sector.

Consequently, setting
\[
\mathcal Q_\rho(\theta)=\frac{\rho^\mu}{2\Gamma(\mu)}K_\sigma(1-\rho e^{i\theta}),
\]
one has, uniformly with first angular derivatives,
\[
\mathcal Q_\rho(\theta)=\cos(\mu\theta)
+\left(1-\frac\mu2\right)\rho\cos((\mu-1)\theta)
+O(\rho^2+\rho^\mu).
\]
The admissible angles for which \(1-\rho e^{i\theta}\in\mathbb D\) are exactly \(|\theta|<\arccos(\rho/2)\).

**4. Sharp converse and completeness.** For every \(\mu>1\) choose fixed angles \(0<\theta_+<\pi/(2\mu)<\theta_-<\min\{3\pi/(2\mu),\pi/2\}\). The cosine leading term is positive at \(\theta_+\) and negative at \(\theta_-\), so sufficiently small circles carry positive and negative kernel values and a zero in between. This proves the converse for *all* \(\sigma<0\), including the exceptional negative even orders.

When \(\mu\notin\{3,5,7,\ldots\}\), the zeros of \(\cos(\mu\theta)\) in the closed interval \([-\pi/2,\pi/2]\) are exactly the interior, simple points \(\pm\theta_j\), \(j\in J_\mu\). The uniform \(C^1\) approximation shows, by a compactness gap argument outside disjoint neighborhoods of those points and strict monotonicity in each neighborhood, that for all sufficiently small \(\rho\) there is exactly one zero near each and no others in the admissible angular interval. The derivative with respect to \(\theta\) does not vanish there. The real-analytic implicit-function theorem applies on \(\rho>0\), giving the claimed disjoint nonsingular arcs.

**5. First-order drift.** At a positive limiting angle \(\theta_j\), write \(\Theta_j(\rho)=\theta_j+a_j\rho+o(\rho)\). Substitute into the expansion and compare linear terms:
\[
-\mu a_j\sin(\mu\theta_j)
+\left(1-\frac\mu2\right)\cos((\mu-1)\theta_j)=0.
\]
Since \(\cos(\mu\theta_j)=0\), the identity \(\cos((\mu-1)\theta_j)=\sin(\mu\theta_j)\sin\theta_j\) yields \(a_j=(1/\mu-1/2)\sin\theta_j\). The negative angles follow by complex conjugation. Counting positive odd integers strictly below \(\mu\) gives \(|J_\mu|=\lceil(\mu-1)/2\rceil=\lceil-\sigma/2\rceil\) outside the excluded thresholds.

## Verification
An accompanying standalone program evaluates the polylogarithmic kernel with high-precision arithmetic and brackets all upper-half-circle zeros for representative negative orders. Its ten local circle tests cover one, two, and three nodal-ray pairs (respectively) and check the first angular drift at small radius. Twenty further evaluations verify positivity at representative nonnegative orders and disk points. The program checks a *finite set* of instances; the analytical proof establishes the all-parameter theorem. To reproduce: install the versions or compatible versions described in `requirements.txt` and run `python check.py`; compare with `check-output.txt`.

## Relationship to prior work
Engliš, Lukkassen, Peetre and Persson (2004) develop Lions-type reproducing kernels for harmonic functions and explicitly treat disk examples. Auchmuty (2009, Theorem 8.2) constructs spectral Steklov reproducing kernels on general domains. Wood (1992, Section 9) provides the local polylogarithm expansion used as a classical special-function input. The contribution claimed here is **not** the Fourier expansion of these kernels, Poisson-kernel positivity, or the polylogarithm expansion independently. It is their combination into the exact sign threshold, the complete boundary-local nodal-ray count across real Sobolev orders, and the first-order drift for a specified normalized harmonic kernel. The literature comparison is subject to the material-access limitations described in the review.

## Limitations
The local count intentionally excludes negative even \(\sigma\), where a limiting ray grazes the disk boundary; the universal sign transition still holds. No classification of global nodal connections, boundary zeros away from \(z=1\), or sharp uniform lower bounds is asserted. The formulas do not establish historical publication priority or address alternative normalizations of the boundary Sobolev norm.

## References
1. M. Engliš, D. Lukkassen, J. Peetre and L.-E. Persson, *On the formula of Jacques-Louis Lions for reproducing kernels of harmonic and other functions*, J. Reine Angew. Math. **570** (2004), 89–129, DOI: 10.1515/crll.2004.035.
2. G. Auchmuty, *Reproducing Kernels for Hilbert Spaces of Real Harmonic Functions*, SIAM J. Math. Anal. **41** (2009), 1994–2009, DOI: 10.1137/080739628 (especially Section 8).
3. D. C. Wood, *The Computation of Polylogarithms*, Technical Report 15-92, University of Kent (1992), especially Section 9; institutional copy: https://kar.kent.ac.uk/21052/.
