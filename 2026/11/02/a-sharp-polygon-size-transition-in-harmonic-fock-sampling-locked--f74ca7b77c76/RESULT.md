# A sharp polygon-size transition in harmonic Fock sampling: locked and recurrent weakest modes

## Finding
Consider the Gaussian harmonic Fock Hilbert space \(\mathcal H_{\mathrm h}\), with reproducing kernel \(R(z,w)=e^{z\overline w}+e^{\overline z w}-1\). For every integer \(k\ge2\) and \(t>0\), sample at the vertices \(w_a=\sqrt t\,e^{2\pi i a/k}\) with normalized evaluation \((S_{k,t}f)_a=k^{-1/2}e^{-t/2}f(w_a)\). The \(k\) nonzero squared singular values, indexed by cyclic Fourier modes \(j\in\{0,\ldots,k-1\}\), are exactly
\[
\lambda_j(t)=P_{k,j}(t)+P_{k,-j}(t)-e^{-t}\mathbf1_{j=0},\qquad
P_{k,j}(t)=e^{-t}\sum_{\substack{n\ge0\\n\equiv j\ ({\rm mod}\ k)}}\frac{t^n}{n!}.
\]
The following dichotomy is sharp in the polygon size.

1. For \(k=2\), the least-sampled Fourier mode changes *exactly once*: it is the nonconstant mode for \(0<t<\log2\), the constant mode for \(t>\log2\), and both modes tie at \(t=\log2\). At the tie the sampling Gram matrix is a scalar multiple of the identity.
2. For \(k=3\), the least-sampled mode likewise changes *exactly once*, from the conjugate pair \(j=1,2\) to \(j=0\), at the unique positive \(t_*\) satisfying
\[
2e^{-t_*/2}\cos(\sqrt3\,t_*/2)=1,\qquad 0<t_*<2\log2.
\]
At \(t_*\), **all three** sampling singular values coincide; hence normalized sampling is tight on its three-dimensional sample range.
3. For every \(k\ge4\), the least-sampled cyclic Fourier mode switches **infinitely often** as the radius grows. For \(k=4\), the unique minimizing mode is \(j=2\) at \(t=2\pi n\) and \(j=0\) at \(t=(2n+1)\pi\), for every positive integer \(n\). For each \(k\ge5\), write \(\theta=2\pi/k\), \(c=1-\cos\theta\) and \(s=\sin\theta\). For all sufficiently large positive integers \(n\), the minimizers at \(t=2\pi n/s\) are exactly the modes minimizing \(\cos(j\theta)\) (one antipodal mode if \(k\) is even, an antipodal pair if odd); at \(t=(2n+1)\pi/s\) the unique minimizer is \(j=0\).

Thus polygon sizes two and three admit a permanently locked least-observable mode after one finite transition, whereas every larger polygon has recurrent asymptotic instability of the identity of that mode. The statements concern the **nonzero** singular values of the point-sampling map, not a positive lower frame bound on the infinite-dimensional ambient space.

## Assumptions and scope
Use \(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). The space consists of complex-valued harmonic functions square-integrable for \(d\mu\); its orthonormal basis is \(1,z^n/\sqrt{n!},\overline z^{\,n}/\sqrt{n!}\) for \(n\ge1\). All polygon vertices are distinct because \(t>0\). The index \(-j\) in \(P_{k,-j}\) is interpreted modulo \(k\). Here \(k\) is fixed when large-radius asymptotics are taken, and a tie between modes means equality of eigenvalues, not coincidence of Fourier eigenvectors.

## Proof
**Kernel and exact diagonalization.** The orthonormal basis gives \(R(z,w)=e^{z\overline w}+e^{\overline z w}-1\), with the subtraction correcting double counting of the constant function. The normalized sample Gram matrix is
\[
G_{ab}=\frac{e^{-t}}k\left(e^{t\omega^{a-b}}+e^{t\omega^{b-a}}-1\right),
\qquad \omega=e^{2\pi i/k}.
\]
It is circulant. Writing the Poisson-residue probabilities \(P_{k,j}\) above and applying the discrete Fourier transform gives exactly the displayed \(\lambda_j\). The analytic monomials of degrees \(0,1,\ldots,k-1\) have independent evaluation vectors on the distinct vertices (Vandermonde), so \(G\) is positive definite. Moreover \(\lambda_{k-j}=\lambda_j\) and \(\sum_j\lambda_j=2-e^{-t}\).

**Two vertices.** Direct root-of-unity evaluation yields
\[
\lambda_0=1+e^{-2t}-e^{-t},\qquad\lambda_1=1-e^{-2t},\qquad
\lambda_0-\lambda_1=e^{-t}(2e^{-t}-1).
\]
There is exactly one positive zero, \(t=\log2\). The unique small-\(t\) minimum is \(j=1\); the large-\(t\) minimum is \(j=0\); at the crossing the two eigenvalues are \(3/4\).

**Three vertices.** Conjugate Fourier modes satisfy \(\lambda_1=\lambda_2\) identically. The Poisson roots-of-unity filter gives
\[
\lambda_0-\lambda_1=2e^{-3t/2}\cos(\sqrt3\,t/2)-e^{-t}.
\]
The sign equals that of \(F(t)-1\), for \(F(t)=2e^{-t/2}\cos(\sqrt3\,t/2)\). On \([0,2\log2]\), the cosine is positive since \(\sqrt3\log2<\pi/2\), and \(F\) strictly decreases from \(2\) to a value less than \(1\). For all \(t>2\log2\), \(F(t)\le2e^{-t/2}<1\). This establishes the unique positive crossing and global sign classification. At the crossing the three Fourier eigenvalues are equal, each to \((2-e^{-t_*})/3\).

**Four vertices.** The same filter gives
\[
\begin{aligned}
\lambda_0&=\tfrac12+e^{-t}(\cos t-1)+\tfrac12e^{-2t},\\
\lambda_1=\lambda_3&=\tfrac12-\tfrac12e^{-2t},\\
\lambda_2&=\tfrac12-e^{-t}\cos t+\tfrac12e^{-2t}.
\end{aligned}
\]
For every positive integer \(n\), substituting \(t=2\pi n\) gives \(\lambda_2<\lambda_1,\lambda_0\), while substituting \(t=(2n+1)\pi\) gives \(\lambda_0<\lambda_1,\lambda_2\). Thus infinitely many distinct minimizing-mode regimes occur.

**All larger polygons.** The exact roots-of-unity identity
\[
P_{k,j}(t)=\frac1k\sum_{\ell=0}^{k-1}\exp\big(t(\omega^\ell-1)\big)\omega^{-\ell j}
\]
shows, uniformly over the finite cyclic mode index at fixed \(k\ge5\),
\[
\lambda_j(t)=\frac2k+\frac4k e^{-ct}\cos(st)\cos(j\theta)+o(e^{-ct})\quad(t\to\infty).
\]
Indeed the conjugate roots \(\ell=1,k-1\) have slowest exponential decay \(c=1-\cos\theta<1\); all remaining nontrivial roots have strictly larger decay rates, and the vacuum correction \(-e^{-t}\mathbf1_{j=0}\) decays faster. On the two displayed sequences \(\cos(st)=+1\) and \(-1\), respectively. Since the distinct values in the finite list \(\{\cos(j\theta)\}\) are separated by positive gaps, the uniform little-oh remainder cannot change the strict comparisons between the minimum cosine class and every other mode, or between \(j=0\) and every nonconstant mode. For odd \(k\), the two conjugate antipodal modes are equal *exactly* by \(\lambda_{k-j}=\lambda_j\), proving the precise equality cases. The alternating minimizing sets prove infinitely many switches for every \(k\ge5\).

## Verification
A standalone checker directly constructs the normalized complex Hermitian sample Gram matrix, compares its eigenvalues with independently summed Poisson congruence classes, verifies positivity, cyclic symmetry and the trace over polygon sizes \(2\le k\le14\) at eight positive radii, and tests the exact two- and three-vertex transitions and multiple large-radius alternating-mode witnesses. It completed 456 deterministic assertions successfully. The infinite switching theorem uses the exact Fourier formula and a uniform exponential asymptotic, not the finite computations.

## Relationship to prior work
The harmonic Fock reproducing kernel and the radial Toeplitz framework are classical ingredients reviewed by Sun, Du and Qi (2024); the basic spectral formula here starts from that kernel but instead studies finite **atomic**, nonradial point sampling on a circular orbit. Gou and collaborators' work on Toeplitz operators with positive measures addresses boundedness and Schatten-class questions, not the explicit eigenvalue-order classification for regular finite polygons. The Poisson roots-of-unity filter and circulant diagonalization are standard identities; the distinction between unique mode locking for \(k\le3\) and recurrent minimizing-mode switching for every \(k\ge4\), with the explicit critical tight radii, is the present complete structural statement. Priority beyond the inspected sources is not certified.

## Limitations
The asymptotic alternation is for each fixed finite \(k\); no uniform-in-\(k\) large-radius threshold is asserted. Tight sampling at the specified two- and three-vertex radii does not imply any full-space frame bound; the map has finite rank. No classification of tight configurations with \(k\ge4\), unequal weights, irregular point sets, or other Gaussian normalizations is claimed. No independent mathematical audit has been performed.

## References
1. Z.-L. Sun, W.-S. Du and F. Qi, *Toeplitz Operators on Harmonic Fock Spaces with Radial Symbols*, Mathematics **12** (2024), 565, first public 2024-02-13, https://doi.org/10.3390/math12040565.
2. X. Gou and collaborators, *Toeplitz Operators with Positive Measures on Harmonic Fock Spaces*, arXiv:2410.06538, https://arxiv.org/abs/2410.06538 (used only as secondary background; earlier public version exists).

