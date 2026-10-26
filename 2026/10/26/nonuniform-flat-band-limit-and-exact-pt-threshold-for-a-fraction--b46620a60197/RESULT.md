# Nonuniform flat-band limit and exact PT threshold for a fractional square lattice

## Finding

Consider the infinite square lattice with balanced staggered gain and loss of magnitude \(\gamma\), coupling \(V>0\), and fractional exponent \(0<s<1\). For Bloch wavevector \(k=(k_1,k_2)\in[-\pi,\pi]^2\), define

\[
q(k)=4-2\cos k_1-2\cos k_2\in[0,8].
\]

The exact Bloch branches are

\[
\lambda_\pm(k)=\pm\sqrt{V^2\bigl(4-q(k)^s\bigr)^2-\gamma^2}.
\]

Consequently, if \(\gamma>0\), the spectrum is real for every Bloch wavevector if and only if

\[
0<s<\frac23,\qquad 0<\gamma\le V(4-8^s).
\]

For \(\gamma=0\), the spectrum is real for every \(0<s<1\). The infinite-lattice zero-order limit is nonuniform: for every fixed \(k\ne(0,0)\) modulo reciprocal lattice periods, \(q(k)^s\to1\) as \(s\downarrow0\), so the band-edge magnitude tends to \(\sqrt{9V^2-\gamma^2}\) when \(\gamma<3V\), not \(\sqrt{16V^2-\gamma^2}\). The latter expression is the value at the isolated wavevector \(k=(0,0)\), not the band edge for positive \(s<2/3\).

## Assumptions and scope

The operator is the translation-invariant, infinite-volume Bloch model in which the nearest-neighbor square-lattice coupling is rewritten as a local coefficient \(4V\) plus the fractional discrete-Laplacian term defined by the positive kernel

\[
K^s(r)=\frac{1}{|\Gamma(-s)|}\int_0^\infty e^{-4t}I_{r_1}(2t)I_{r_2}(2t)t^{-1-s}\,dt,\qquad r\in\mathbb Z^2\setminus\{0\}.
\]

Here \(I_j\) is the modified Bessel function. The gain/loss signs alternate between the two sublattices. The result concerns the reality of the Bloch eigenvalues, not diagonalizability or bounded time evolution at an exceptional point. It does not assert that a finite matrix obtained by truncating the infinite-range kernel has the same small-\(s\) limit.

## Proof

**1. Exact Fourier multiplier.** The Bessel generating identity gives, for \(t>0\),

\[
\sum_{r\in\mathbb Z^2}e^{-4t}I_{r_1}(2t)I_{r_2}(2t)e^{ik\cdot r}
=e^{-q(k)t}.
\]

The corresponding sum at \(k=0\) is \(1\). Since \(1-\cos(k\cdot r)\ge0\), the positive-kernel representation permits the sum and integral to be interchanged. Therefore

\[
\begin{aligned}
\sum_{r\ne0}(\cos(k\cdot r)-1)K^s(r)
&=\frac{1}{|\Gamma(-s)|}\int_0^\infty(e^{-q(k)t}-1)t^{-1-s}\,dt\\
&=-q(k)^s,
\end{aligned}
\]

where the last identity follows by integration by parts (equivalently, \(\int_0^\infty(e^{-qt}-1)t^{-1-s}dt=\Gamma(-s)q^s\) for \(q\ge0\), with the value at \(q=0\) understood by continuity).

**2. Bloch determinant.** In the two-sublattice basis, the eigenvalue equations have off-diagonal coupling \(V(4-q(k)^s)\) and diagonal entries \(-\lambda+i\gamma\) and \(-\lambda-i\gamma\). Their determinant vanishes precisely when

\[
\lambda^2+\gamma^2-V^2(4-q(k)^s)^2=0,
\]

which proves the displayed dispersion relation.

**3. Exact reality region.** The continuous function \(q(k)\) attains every value in \([0,8]\). Thus \(q(k)^s\) attains every value in \([0,8^s]\). If \(s<2/3\), then \(8^s<4\), so \(4-q^s\) is nonnegative and its minimum is \(4-8^s\), attained at \(k=(\pi,\pi)\). Every radicand is nonnegative exactly when \(\gamma\le V(4-8^s)\). If \(s\ge2/3\), then \(4^{1/s}\le8\); choose a wavevector with \(q(k)=4^{1/s}\). At that wavevector \(4-q(k)^s=0\), so \(\lambda_\pm=\pm i\gamma\), which is nonreal for every \(\gamma>0\). For \(s<2/3\) and \(\gamma>V(4-8^s)\), the corner wavevector \((\pi,\pi)\) already has negative radicand. This proves both directions, including equality at the threshold.

**4. Nonuniform zero-order limit.** For fixed \(k\ne(0,0)\), one has \(q(k)>0\), hence \(q(k)^s\to1\). The corner value \(q=8\) gives the positive band edge \(\sqrt{V^2(4-8^s)^2-\gamma^2}\), which tends to \(\sqrt{9V^2-\gamma^2}\) when \(\gamma<3V\). At \(k=(0,0)\), however, \(q=0\) and \(q^s=0\) for every \(s>0\), leaving the distinct value \(\sqrt{16V^2-\gamma^2}\) when \(\gamma<4V\). Thus the limit is not uniform in wavevector; taking \(s\downarrow0\) inside each fixed-offset kernel coefficient cannot be exchanged with the infinite sum over offsets.

## Verification

The included standard-library script `verify_spectrum.py` checks representative exponents on a dense grid of \(q\in[0,8]\), verifies that the threshold boundary has nonnegative radicand and that a slightly larger gain/loss value has a negative radicand at \(q=8\), checks an explicit nonreal witness for \(s\ge2/3\), and tests the distinct fixed-\(q>0\) and \(q=0\) limits numerically. The script is a reproducibility check for the stated formulas; the proof above establishes the universal statements, so no finite grid is used as an exhaustive proof.

## Relationship to prior work

Molina's square-lattice study gives the same kernel representation and Bloch dispersion in closed form, but estimates the critical exponent numerically and describes the small-\(s\) gap as tending to \(2\sqrt{16V^2-\gamma^2}\). The exact Fourier multiplier above shows that this value belongs to \(k=(0,0)\), whereas the band edge for every \(0<s<2/3\) occurs at \(k=(\pi,\pi)\) and has limiting magnitude \(\sqrt{9V^2-\gamma^2}\) in the real-spectrum regime. The result is therefore a correction to the infinite-volume limiting interpretation, not a claim of novelty for the dispersion relation itself.

A later one-dimensional fractional \(\mathcal{PT}\)-symmetric transmission-line study explicitly notes that finite and infinite kernel sums can have different small-exponent limits. Its dynamical matrix and dispersion relation differ from the two-dimensional square-lattice Bloch operator, so it does not imply the threshold \(V(4-8^s)\) or the two-dimensional band-edge correction proved here.

## Limitations

The analysis assumes the infinite translation-invariant square lattice and the kernel normalization written above. It does not establish convergence rates for finite-volume approximations, nor does it classify boundary-localized states. At \(\gamma=V(4-8^s)>0\), the corner Bloch fiber has a zero eigenvalue with a defective two-by-two matrix; spectral reality at equality therefore does not imply bounded evolution. The density-of-states statement is only the consequence of the almost-everywhere fixed-wavevector limit, not a theorem about every finite-size histogram.

## References

1. M. I. Molina, “Fractionality and \(\mathcal{PT}\) symmetry in a square lattice,” arXiv:2211.02796v1 (first submitted 2022-11-05); *Physical Review A* **106**, L040202 (2022), DOI 10.1103/PhysRevA.106.L040202.
2. M. I. Molina, “Fractionality and \(\mathcal{PT}\) symmetry in an electrical transmission line,” arXiv:2307.00375v1 (first submitted 2023-07-01); *Physical Review A* **108**, 013515 (2023), DOI 10.1103/PhysRevA.108.013515.
