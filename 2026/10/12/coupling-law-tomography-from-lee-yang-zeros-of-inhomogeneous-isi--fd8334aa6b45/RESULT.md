# Coupling-law tomography from Lee–Yang zeros of inhomogeneous Ising stars

## Finding

An increasing-degree Ising star with heterogeneous ferromagnetic bonds has a limiting Lee–Yang zero measure that determines the entire asymptotic distribution of its bond strengths. The zero density is an explicit mixture of Poisson kernels, and even before taking limits each fixed-order bond moment is recoverable from the Lee–Yang zero power sums with an exponentially small *unnormalized* discrepancy.

Precisely, let \(q_{i,m}=e^{-2J_{i,m}}\) for \(J_{i,m}>0\), and set
\[
Z_m(z)=\prod_{i=1}^{m}(1+q_{i,m}z)
      +z\prod_{i=1}^{m}(q_{i,m}+z).
\]
All \(m+1\) zeros \(\zeta_{1,m},\ldots,\zeta_{m+1,m}\) are simple and lie on \(\lvert z\rvert=1\). Fix \(q_*<1\) with \(0<q_{i,m}\leq q_*\), and set
\[
\tau=\frac{q_*+1/2}{1+q_*/2}<1.
\]
For **every** positive integer \(k\), with the exact normalization shown,
\[
\left|\sum_{j=1}^{m+1}\zeta_{j,m}^{k}
 -(-1)^k\sum_{i=1}^{m}q_{i,m}^{k}\right|
 \leq k\,2^{k}\tau^{m}. \tag{1}
\]
If \(\mu_m=m^{-1}\sum_i\delta_{q_{i,m}}\) converges weakly to \(\mu\) on \([0,q_*]\), then \(\nu_m=(m+1)^{-1}\sum_j\delta_{\zeta_{j,m}}\) converges weakly to the probability law with angular density
\[
\rho_\mu(\theta)=\frac{1}{2\pi}
 \int_{[0,q_*]}\frac{1-q^2}{1+q^2+2q\cos\theta}\,d\mu(q),
 \qquad 0\leq\theta<2\pi. \tag{2}
\]
For every positive integer \(k\), its Fourier moment is
\[
\int_{\mathbb T} z^k\,d\nu(z)
   =(-1)^k\int_{[0,q_*]}q^k\,d\mu(q). \tag{3}
\]
Because these are all the Hausdorff moments on a compact interval, the map \(\mu\mapsto\nu\) is injective. Thus the limiting zero spectrum identifies the limiting **distribution**, not labels, of the physical couplings via \(J=-\tfrac12\log q\) on \(q>0\).

For example, the two coupling laws \(\mu_A=\delta_{2/5}\) and \(\mu_B=(\delta_{1/5}+\delta_{3/5})/2\) have the same first coupling moment, \(2/5\), but different second moments, \(4/25\) and \(1/5\). Their first zero Fourier moments agree, whereas the second Fourier moments distinguish their heterogeneity.

There is also a sharp low-angle law. For each fixed positive integer \(j\), let \(\theta_{j,m}\in(0,2\pi)\) be the \(j\)-th smallest zero angle. Put
\[
r_\mu=\int_{[0,q_*]}\frac{1-q}{1+q}\,d\mu(q)>0.
\]
Then
\[
 m\theta_{j,m}\longrightarrow\frac{(2j-1)\pi}{r_\mu}. \tag{4}
\]

## Assumptions and scope

The graph has one central spin and \(m\geq1\) leaves. Spins take values \(\pm1\), the inverse temperature is absorbed into the positive dimensionless edge interactions \(J_{i,m}\), and the complex field \(h\) acts **uniformly on every spin**. The change of variable is \(z=e^{-2h}\). The polynomial above equals the partition function after division by a nonzero prefactor and hence has the same nonzero Lee–Yang zeros. The edge interactions may vary arbitrarily with the leaf and with \(m\); no randomness, exchangeability, or periodicity is assumed.

The finite zero-location and phase formulas require only \(J_{i,m}>0\). Bound (1), weak convergence (2), identifiability (3), and edge asymptotics (4) require a uniform constant \(q_*<1\), equivalent to a uniform strictly positive lower bound on edge interaction strengths. The limiting distribution \(\mu\) may have mass at \(q=0\), representing arbitrarily strong interactions along the sequence; each finite interaction remains finite.

## Proof

**Polynomial normalization.** Condition on the central spin. For central spin \(+1\), each leaf contributes a factor proportional to \(1+q_{i,m}z\); for central spin \(-1\), the central field adds a factor \(z\), and leaf \(i\) contributes \(q_{i,m}+z\). This yields the displayed polynomial. Its constant and leading coefficients both equal one, and its coefficients are real and reciprocal.

**Lee–Yang circle and simple zeros.** Write \(q_i=q_{i,m}\) temporarily and form
\[
B_m(z)=z\prod_{i=1}^m\frac{z+q_i}{1+q_i z}.
\]
Where its denominator is nonzero, \(Z_m(z)=0\) is equivalent to \(B_m(z)=-1\). Each factor is an automorphism of the open unit disk for \(0<q_i<1\). Thus \(\lvert B_m(z)\rvert<1\) for \(\lvert z\rvert<1\) and \(\lvert B_m(z)\rvert>1\) for \(\lvert z\rvert>1\) away from poles; poles cannot be zeros of \(Z_m\). All zeros therefore lie on \(\mathbb T\). On \(z=e^{i\theta}\), choose the continuously increasing argument \(\Phi_m\) satisfying \(\Phi_m(0)=0\). Explicitly,
\[
\Phi_m(\theta)=\theta+
  \sum_{i=1}^{m}2\operatorname{atan2}\!\left(
  (1-q_i)\sin\frac\theta2,\,(1+q_i)\cos\frac\theta2\right)
\]
for \(0\leq\theta\leq2\pi\), with the \(\operatorname{atan2}\) branch in \([0,\pi]\). Differentiating gives
\[
\Phi_m'(\theta)=1+
\sum_{i=1}^{m}\frac{1-q_i^2}{1+q_i^2+2q_i\cos\theta}>0.
\]
The phase traverses \([0,2\pi(m+1)]\) once and each equation \(\Phi_m(\theta)=(2j-1)\pi\), \(1\leq j\leq m+1\), has exactly one solution. These provide all \(m+1\) distinct zeros.

**Exponentially accurate power sums.** Put \(P_m(z)=\prod_i(1+q_i z)\) and \(R_m(z)=z\prod_i(z+q_i)/(1+q_i z)\), so \(Z_m=P_m(1+R_m)\). For \(\lvert z\rvert=1/2\), the disk automorphism inequality is
\[
\left|\frac{z+q_i}{1+q_i z}\right|
\leq\frac{q_i+1/2}{1+q_i/2}\leq\tau.
\]
Consequently \(\lvert R_m(z)\rvert\leq\tfrac12\tau^m\). The branch of \(\log(1+R_m)\) that vanishes at the origin satisfies \(\lvert\log(1+R_m(z))\rvert\leq\tau^m\) on this circle, by the logarithmic power series. Cauchy's coefficient estimate shows that the coefficient of \(z^k\) in \(\log Z_m-\log P_m\) has modulus at most \(2^k\tau^m\).

Because all zeros of \(Z_m\) lie on \(\mathbb T\), and coefficients of \(Z_m\) are real, inverse and ordinary zero power sums agree: \(\sum_j\zeta_{j,m}^{-k}=\sum_j\zeta_{j,m}^{k}\). The coefficient of \(z^k\) in \(\log Z_m\) is \(-k^{-1}\sum_j\zeta_{j,m}^{-k}\); the corresponding coefficient in \(\log P_m\) is \((-1)^{k+1}k^{-1}\sum_iq_i^k\). Multiplication by \(k\) proves (1), for any fixed or varying integer \(k\geq1\). No finite numerical enumeration enters this argument.

**Density, inverse law, and edge spacing.** Dividing (1) by \(m+1\), using weak convergence of \(\mu_m\), and recalling \(m/(m+1)\to1\) gives the Fourier moments in (3). The Poisson kernel identity
\[
\frac{1-q^2}{1+q^2+2q\cos\theta}
=1+2\sum_{k\geq1}(-q)^k\cos(k\theta)
\]
holds uniformly for \(0\leq q\leq q_*<1\). Hence the right side of (2) is a probability density with exactly these Fourier coefficients. Trigonometric-polynomial density in continuous functions on the circle proves weak convergence and uniqueness. Equality of two limiting zero laws forces equality of every moment of the corresponding coupling measures; Weierstrass polynomial approximation on \([0,q_*]\) proves equality of these measures.

Finally, let \(r_i=(1-q_i)/(1+q_i)\). At small positive \(\theta\), uniformly in \(q_i\leq q_*\),
\[
\Phi_m(\theta)=\left(1+\sum_{i=1}^{m}r_i\right)\theta
   +O\!\left(m\theta^3\right).
\]
Since \(\Phi'_m\geq1+m(1-q_*)/(1+q_*)\), for each fixed \(j\) the root \(\Phi_m(\theta_{j,m})=(2j-1)\pi\) has \(\theta_{j,m}=O_j(m^{-1})\). Substitution and the derivative lower bound sharpen this to
\[
\theta_{j,m}=\frac{(2j-1)\pi}{1+\sum_i r_i}+O_j(m^{-3}).
\]
As \(m^{-1}\sum_i r_i\to r_\mu\), (4) follows.

## Verification

The included `verify.py` reconstructs the finite partition polynomials using exact rational coefficients, checks reciprocity and the logarithmic Fourier-error inequality via exact Newton power sums in ten heterogeneous parameter sets, and independently solves the unit-circle phase equation by bisection for five further heterogeneous examples. The program also compares the resulting numerical Fourier moments with the coupling moments and checks the first-angle scaling. It prints a `VERIFY_OK` diagnostic only when every test passes. These are finite reproductions of intermediate identities, **not** a proof of the all-size assertion.

The analytical derivation verifies all polynomial factors, branch choices, quantifiers, and the bound's dependence on the uniform coupling parameter. The proof does not require roots computed numerically or any unproved asymptotic spectral theorem.

## Relationship to prior work

Chio, He, Ji and Roeder [1] obtain Lee–Yang limiting measures for **fixed-branching, increasing-depth** Cayley trees via iterated Blaschke products. Their Proposition 1.1 already yields the uniform-bond finite star equation as a depth-one specialization. Here that equation is treated as established motivation, not claimed novelty. Our setting instead has **depth one and increasing heterogeneous degree**; the assessed claim is the explicit arbitrary-bond mixture, exponential coupling-moment recovery, inverse identifiability and boundary scaling.

Hou, Jiang and Newman [2] study motion and monotonicity of Ising Lee–Yang zeros when bonds vary, and Simon [3] establishes general analytic consequences of Lee–Yang zero-freeness. Neither provides an implication covering the combination of heterogeneous increasing-degree star zero-density inversion and the explicit finite moment error in (1). The classical finite Blaschke boundary-phase and Poisson-kernel formulas are used as known complex-analysis inputs rather than claimed independently new techniques.

## Limitations

The result applies to ferromagnetic stars under **uniform external field** and a **uniform positive lower bound** on edge interaction strength. It does not give a corresponding law for fixed-degree growing-depth trees, frustrated bonds, nonuniform external fields, or sequences with coupling parameters accumulating at one. Inverse uniqueness concerns only the limiting *unlabeled bond distribution*, not recovery of individual finite-star edge labels; Hausdorff moment inversion can be numerically ill-conditioned. No experimental robustness estimate, independent external review, or novel theorem for arbitrary Blaschke products is claimed.

## References

[1] I. Chio, C. He, A. L. Ji, R. K. W. Roeder, *Limiting Measure of Lee–Yang Zeros for the Cayley Tree*, arXiv:1806.00403 (first public 2018-06-01), Proposition 1.1 and Theorems A–D. https://arxiv.org/html/1806.00403v2

[2] Y. Hou, J. Jiang, C. M. Newman, *Motion of Lee–Yang zeros*, arXiv:2208.00917 (2022). https://arxiv.org/abs/2208.00917

[3] B. Simon, *The Strong Gauss Lucas Theorem and Analyticity of Correlation Functions via the Lee–Yang Theorem*, arXiv:2111.00650 (2021), especially Section 3. https://arxiv.org/html/2111.00650v1
