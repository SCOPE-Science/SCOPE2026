# Staggered two-circle Szegő sampling optimizes both Hardy interpolation bounds

## Finding
Fix any integer \(k\ge2\) and two different radii \(0<r<s<1\). Let \(H^2(\mathbb D)\) be the analytic Hardy space with coefficient norm \(\|\sum_{n\ge0}a_nz^n\|^2=\sum_{n\ge0}|a_n|^2\). Choose \(2k\) sample points in the open disk on two concentric regular polygons:
\[
 z_{0,m}=r e^{2\pi i m/k},\qquad
 z_{1,m}=s e^{i\theta}e^{2\pi i m/k},\qquad 0\le m<k.
\]
Consider the normalized evaluation map
\[
 E_\theta f=\big(\sqrt{1-|z_{a,m}|^2}\,f(z_{a,m})\big)_{a=0,1;\,0\le m<k}:H^2(\mathbb D)\longrightarrow\mathbb C^{2k}
\]
and its positive definite Gram matrix \(G_\theta=E_\theta E_\theta^*\). With \(\kappa(G)=\lambda_{\max}(G)/\lambda_{\min}(G)\), the **unique optimal relative orientation**, modulo rotating one regular polygon through \(2\pi/k\), is
\[
 \boxed{\theta=\pi/k\pmod{2\pi/k}.}
\]
It *simultaneously* maximizes the smallest eigenvalue, minimizes the largest eigenvalue, and minimizes \(\kappa(G_\theta)\). All three extremizers are strict modulo this equivalence.

The complete spectrum can be computed with \(k\) explicit two-by-two blocks. For \(0\le j<k\), put
\[
 A_j=\frac{k(1-r^2)r^{2j}}{1-r^{2k}},\quad
 B_j=\frac{k(1-s^2)s^{2j}}{1-s^{2k}},\quad
 C_j(\theta)=\frac{k\sqrt{(1-r^2)(1-s^2)}(rs)^j}{|1-(rs)^ke^{ik\theta}|}.
\]
Then the \(2k\) eigenvalues, counted with multiplicity, are
\[
 \lambda_j^{\pm}(\theta)=\frac{A_j+B_j\pm\sqrt{(A_j-B_j)^2+4C_j(\theta)^2}}2.
\]
The extremal eigenvalues lie in the *known* Fourier sectors, at every angle:
\[
 \lambda_{\max}(G_\theta)=\lambda_0^+(\theta),\qquad
 \lambda_{\min}(G_\theta)=\lambda_{k-1}^-(\theta).
\]
Thus the worst-case interpolation cost is exactly \(\lambda_{k-1}^-(\theta)^{-1/2}\), and the spectral condition number of the sampling map is \(\sqrt{\lambda_0^+(\theta)/\lambda_{k-1}^-(\theta)}\).

For the optimal offset, with the two radii held fixed and \(k\to\infty\), the constants are *sharp*:
\[
 \boxed{\lambda_{\min}(G_{\pi/k})\sim
 k\frac{1-r^2}{r^2}(rs)^{2k},\qquad
 \lambda_{\max}(G_{\pi/k})\sim k(2-r^2-s^2).}
\]
Consequently
\[
 \boxed{\kappa(G_{\pi/k})\sim
 \frac{r^2(2-r^2-s^2)}{1-r^2}(rs)^{-2k}.}
\]
The staggering is the exact finite-design optimum; the displayed large-degree rate quantifies the exponential ill-conditioning that remains even at that optimum.

## Assumptions and scope
All radii are real and strictly between zero and one, with \(r<s\), and both circles contain exactly \(k\) equally weighted, equally spaced nodes. The circles are different; the coincident-radius limit has a different large-degree asymptotic constant and is not asserted. Sample normalization is exactly \(\sqrt{1-|z|^2}\) rather than an unweighted point value. The Gram matrix is \(EE^*\), not an infinite-dimensional frame operator; it is positive definite because Szegő kernels at distinct disk points are linearly independent. The relative angle is considered modulo \(2\pi/k\). The finite spectral and optimization identities hold for every \(k\ge2\), while the asymptotic expressions require fixed \(r,s\) with \(0<r<s<1\).

## Proof
**1. Exact cyclic block decomposition.** Normalized Szegő kernels have scalar products
\[
 \langle K_z,K_w\rangle=\frac{\sqrt{(1-|z|^2)(1-|w|^2)}}{1-\bar z w}.
\]
With \(\omega=e^{2\pi i/k}\), apply the same cyclic discrete Fourier transform on the node index of both rings. The elementary geometric sum
\[
 \sum_{m=0}^{k-1}\frac{\omega^{-jm}}{1-u\omega^m}
 =\frac{ku^j}{1-u^k},\qquad |u|<1,\quad 0\le j<k
\]
shows that the transform makes the Gram matrix a direct sum of Hermitian two-by-two blocks. Their diagonals are \(A_j,B_j\), and their off-diagonal entry equals
\[
 D_j(\theta)=\frac{k\sqrt{(1-r^2)(1-s^2)}(rs e^{i\theta})^j}{1-(rs e^{i\theta})^k}.
\]
Its modulus is \(C_j(\theta)\). Diagonalizing these blocks proves the complete eigenvalue formula. Positivity follows either from linear independence of the distinct Cauchy kernels or the strictly positive determinant in Step 3.

**2. The extremal Fourier sectors.** Each block is unitarily similar to
\[
 H_j(\theta)=\begin{pmatrix}A_j&C_j(\theta)\\ C_j(\theta)&B_j\end{pmatrix}>0.
\]
Writing \(D=\operatorname{diag}(r,s)\), the exact relation \(H_{j+1}=DH_jD\) holds for \(0\le j<k-1\). Because \(\|D\|=s<1\), the Rayleigh quotient gives
\[
 \lambda_{\max}(H_{j+1})\le s^2\lambda_{\max}(H_j)<\lambda_{\max}(H_j).
\]
For a unit eigenvector \(v\) minimizing the Rayleigh quotient of \(H_j\), test \(H_{j+1}\) with \(D^{-1}v/\|D^{-1}v\|\). As \(\|D^{-1}v\|^2\ge s^{-2}\),
\[
 \lambda_{\min}(H_{j+1})\le s^2\lambda_{\min}(H_j)<\lambda_{\min}(H_j).
\]
Hence the global smallest and largest eigenvalues occur at \(j=k-1\) and \(j=0\), respectively.

**3. Angular optimum and exact determinant.** For fixed radii, all diagonal entries are independent of \(\theta\), while every off-diagonal modulus is proportional to
\[
 \frac1{|1-(rs)^ke^{ik\theta}|}.
\]
The denominator has its unique maximum modulo \(2\pi/k\) at \(\theta=\pi/k\). For a positive Hermitian two-by-two matrix with fixed diagonal entries and positive off-diagonal modulus, its smaller eigenvalue strictly decreases, and its larger one strictly increases, with that modulus. Thus staggered placement simultaneously increases every lower block eigenvalue and decreases every upper block eigenvalue, establishing the three unique extremizers.

For completeness, elementary simplification gives the exact nonnegative determinant at *every* offset:
\[
 \det H_j(\theta)=
 \frac{k^2(1-r^2)(1-s^2)(rs)^{2j}
 |r^k-s^ke^{ik\theta}|^2}
 {(1-r^{2k})(1-s^{2k})|1-(rs)^ke^{ik\theta}|^2}.
\]
It is strictly positive for \(r<s\), and at the staggered offset the numerator factor is \((r^k+s^k)^2\).

**4. Sharp large-degree conditioning.** At the staggered offset and Fourier index \(j=k-1\), the ratios \(A_j/B_j\) and \(C_j/B_j\) tend to zero since \(r<s\). Therefore \(\lambda_{k-1}^+\sim B_{k-1}\), and the determinant identity yields
\[
 \lambda_{k-1}^-
 =\frac{\det H_{k-1}}{\lambda_{k-1}^+}
 \sim \frac{k(1-r^2)r^{2k-2}(r^k+s^k)^2}
 {(1-r^{2k})(1+(rs)^k)^2}
 \sim k\frac{1-r^2}{r^2}(rs)^{2k}.
\]
For \(j=0\), the normalized block \(k^{-1}H_0\) converges to the rank-one matrix
\[
 \begin{pmatrix}
 1-r^2&\sqrt{(1-r^2)(1-s^2)}\\
 \sqrt{(1-r^2)(1-s^2)}&1-s^2
 \end{pmatrix},
\]
whose top eigenvalue is \(2-r^2-s^2\). Dividing the two asymptotic eigenvalues proves the condition-number formula. No finite numerical computation is used for this infinite-degree conclusion.

## Verification
The standalone, standard-library Python 3 file `check_two_circle_hardy.py` recomputes the cyclic Fourier blocks directly from the full normalized kernel Gram entries for multiple node counts, pairs of radii, relative angles, and Fourier sectors. It also checks block positivity, trace/determinant identities, strict eigenvalue ordering, uniqueness among nonoptimal angle samples, and large-degree asymptotic convergence. Run `python3 check_two_circle_hardy.py`; the test prints `PASS: 6099 standard-library numerical assertions`. These finite consistency tests corroborate the exact algebra; they are not a substitute for the analytic all-degree proof.

## Relationship to prior work
Speransky and Terekhin [1] and Baranov and Batenev [2] construct representing systems in Hardy spaces using concentric layers of equally spaced Szegő kernels. Their objectives are existence and approximation; their theorems do not quantify the exact worst-case singular value of two adjacent layers as a function of the relative angle. Groenewald, ter Horst and Woerdeman [3] treat minimal-norm Hardy interpolation in a general reproducing-kernel Banach-space framework and give algorithms, not this sharp angular-design law. An existing result on Szegő orbit frames [4] gives a determinant stability inequality and complete seed spectrum for points on a **single** circle with equal radius; its claims do not imply the two-different-radii spectral block formula, simultaneous extremizers, or sharp mixed-radius large-degree constant. General Cauchy determinant identities explain some determinants but do not by themselves establish the eigenvalue extrema or conditioning. These comparisons support a provisional distinction, not a claim that every historical source has been exhausted.

## Limitations
The result optimizes only a relative rotation of two *individually regular* polygons with preassigned, different radii, rather than optimizing all \(2k\) node positions or radii. No claim is made about infinite-layer frames, other reproducing kernels, unequal node counts, perturbations of individual node positions, or the singular spectrum of arbitrary sampling sets. The large-degree formula is pointwise for fixed distinct radii, not uniform as the two radii coalesce or approach the boundary. Historical-priority uncertainty remains; no independent mathematical audit has been performed.

## References
[1] K. S. Speransky and P. A. Terekhin, *A representing system generated by the Szegö kernel for the Hardy space*, arXiv:1803.05492v1 (14 March 2018), https://arxiv.org/abs/1803.05492.

[2] A. Baranov and T. Batenev, *Representing systems of reproducing kernels in spaces of analytic functions*, arXiv:2207.08985v1 (18 July 2022), https://arxiv.org/abs/2207.08985.

[3] G. J. Groenewald, S. ter Horst and H. J. Woerdeman, *Optimal interpolation in Hardy and Bergman spaces: a reproducing kernel Banach space approach*, arXiv:2412.11473v1 (16 December 2024), https://arxiv.org/abs/2412.11473.

[4] *Sharp determinant stability and conditioning of concentric Szegő orbit frames*, public research record 44f30fce73fa (11 October 2026), single-radius result; comparison restricted to the theorem and proof of that record.
