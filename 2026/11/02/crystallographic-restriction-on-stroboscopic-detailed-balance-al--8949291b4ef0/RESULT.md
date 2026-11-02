# Crystallographic restriction on stroboscopic detailed-balance aliasing in biased Markov rings

## Finding
For a homogeneous, finite, biased nearest-neighbor continuous-time random walk on a ring, **exactly the ring sizes \(n\in\{3,4,6\}\)** can become reversible when observed at a finite, positive fixed sampling interval. Their complete resonance times, the two distinct embedding regimes, and the impossibility for every other ring size are classified below. This is exact loss of time-direction information even when every ring state is observed, rather than coarse-graining of states.

## Assumptions and scope
Let \(n\) be any integer with \(n\ge3\), let \(a,b>0\) with \(a\ne b\), and index states by \(\mathbb Z/n\mathbb Z\). The generator \(Q\), acting on row-indexed transition probabilities, has \(Q_{i,i+1}=a\), \(Q_{i,i-1}=b\), and \(Q_{ii}=-(a+b)\), with all other entries zero. Let \(S\) denote the cyclic forward transition matrix, so \(Q=a(S-I)+b(S^{-1}-I)\). Write \(P(t)=e^{tQ}\) for \(t>0\). The unique stationary law is \(\pi_i=1/n\). Because \(P(t)\) is a strictly positive circulant matrix, its stationary detailed-balance property is equivalent to \(P(t)=P(t)^{\mathsf T}\).

**Classification.** Under the stated assumptions, \(P(t)\) is reversible if and only if one of the following holds:

- \(n=3\) or \(n=6\), and \(t=2m\pi/(\sqrt3\,|a-b|)\) for an integer \(m\ge1\);
- \(n=4\), and \(t=m\pi/|a-b|\) for an integer \(m\ge1\).

At an even-index resonance, \(P(t)=e^{tQ_{\mathrm{sym}}}\), where \(Q_{\mathrm{sym}}=\frac{a+b}{2}(S+S^{-1}-2I)\) is reversible. At an odd-index resonance, \(P(t)\) has a strictly negative real eigenvalue, so it cannot be the exponential of any reversible continuous-time Markov generator. Non-resonant times and all ring sizes outside \(\{3,4,6\}\) yield strictly nonreversible sampled chains.

## Proof
**1. Fourier diagonalization.** Let \(\theta_k=2\pi k/n\) for \(k=0,\ldots,n-1\). Since \(S\) is a cyclic permutation, the discrete Fourier basis simultaneously diagonalizes \(S\), \(S^{-1}\), \(Q\) and \(P(t)\). The eigenvalues of \(Q\) are, with a consistent Fourier convention,
\[
\lambda_k=(a+b)(\cos\theta_k-1)+i(a-b)\sin\theta_k.
\]
The corresponding eigenvalues of \(P(t)\) are \(e^{t\lambda_k}\). A real circulant matrix is symmetric precisely when each of its Fourier eigenvalues is real: one direction follows from symmetry; conversely, a real circulant is a normal matrix and real Fourier eigenvalues imply it is symmetric by its unitary Fourier diagonalization. Therefore
\[
P(t)=P(t)^{\mathsf T}\quad\Longleftrightarrow\quad
(a-b)t\sin(2\pi k/n)\in\pi\mathbb Z
\quad\text{for every }k=1,\ldots,n-1.
\]

**2. Arithmetic obstruction.** Assume \(n\ge5\). Then the sine factors for \(k=1,2\) are nonzero. If a positive \(t\) satisfies the criterion, the ratio of their (nonzero integer) phase multiples must be rational. Using the double-angle identity, this ratio is
\[
\frac{\sin(4\pi/n)}{\sin(2\pi/n)}=2\cos(2\pi/n)\in\mathbb Q.
\]
Write \(\zeta=e^{2\pi i/n}\). The number \(\zeta+\zeta^{-1}=2\cos(2\pi/n)\) is an algebraic integer, hence if it is rational it must be an ordinary integer. For \(n\ge5\), \(0<2\cos(2\pi/n)<2\); the only possible integer is \(1\), forcing \(2\pi/n=\pi/3\), or \(n=6\). Thus no ring size \(n\ge5\), except \(n=6\), admits a positive reversible sampling time. This is an exact all-size argument, not an inference from numerical enumeration.

**3. Exact exceptional sets.** For \(n=3\), the nonzero sine factors are \(\pm\sqrt3/2\); for \(n=4\) they are \(0,\pm1\); for \(n=6\) they are \(0,\pm\sqrt3/2\). Substitution in the criterion in Step 1 gives exactly the resonance times stated above, with no omitted positive solutions.

**4. Two kinds of resonance.** At the \(m\)-th resonance, each Fourier eigenvalue of \(P(t)\) has imaginary phase \(0\) or an integer multiple of \(m\pi\). If \(m\) is even, every phase factor is \(+1\); the real parts of the eigenvalues are exactly the eigenvalues of \(Q_{\mathrm{sym}}\), hence Fourier diagonalization proves \(P(t)=e^{tQ_{\mathrm{sym}}}\). If \(m\) is odd, the \(k=1\) mode has phase \(\pm m\pi\), so its eigenvalue is \(-e^{t(a+b)(\cos(2\pi/n)-1)}<0\). Every reversible real Markov generator is similar, by the square root of its stationary diagonal matrix, to a real symmetric generator; its exponential has exclusively positive real eigenvalues. Consequently no reversible continuous-time generator can produce \(P(t)\) at odd \(m\), even though \(P(t)\) is a reversible stochastic matrix.

**5. Physical irreversibility and sampled entropy.** The stationary clockwise-minus-counterclockwise current on every edge is \((a-b)/n\), and the total steady entropy-production rate (in units with Boltzmann's constant equal to one) is
\[
\sigma=(a-b)\log(a/b)>0.
\]
The sampled one-step entropy production rate, defined from all stationary state-pair frequencies as
\[
\sigma_t=\frac1{nt}\sum_{i,j=0}^{n-1}P_{ij}(t)\log\frac{P_{ij}(t)}{P_{ji}(t)},
\]
is nonnegative by the Kullback–Leibler inequality and is zero exactly when \(P(t)\) is symmetric, since all entries of \(P(t)\) are strictly positive. Hence the arithmetic classification also exactly describes the zeros of this sampled irreversibility statistic. This completes the proof.

## Verification
Run `python CHECK.py` with Python 3, NumPy, and SciPy. The independent finite-generator/matrix-exponential checker verifies the exceptional resonance matrices, stationarity, symmetry, parity-dependent signs, the even-index symmetric semigroup identity, and selected nonexceptional samples against explicit Fourier eigenvalues. It passes 182 numerical assertions on the stated dependency versions available at verification. Numerical finite-size examples are corroboration only: the algebraic-integer argument proves the assertion for every integer \(n\ge3\).

## Relationship to prior work
The use of matrix exponentials and Fourier modes for Markov dynamics is established. Yong and Jianmin Chen (2010) analyze three-state embeddability with coincident negative eigenvalues, covering the three-state negative-eigenvalue mechanism. Jia (2016) gives general reversible Markov embedding criteria. Bauer, Seifert and van der Meer (2024/2025) explicitly show that equilibrium and nonequilibrium three-state generators may give the same stroboscopic propagator; their general aliasing analysis motivates the distinction between observation-time reversibility and continuous-time generator reversibility. Baake, Baake and Sumner (2025) discuss reversible matrices with negative eigenvalues, including three-state cyclic and four-state examples. These works are not claimed to be newly derived here. The specific all-ring classification \(\{3,4,6\}\), exact resonance lattice, and impossibility for all other ring sizes arise from a cyclotomic commensurability obstruction, which was not identified in those inspected sources. This is a provisional originality comparison, not proof of priority.

## Limitations
The theorem assumes a single particle, constant clockwise and counterclockwise rates, exact regular sampling, the full state observed, and a finite nearest-neighbor ring. For heterogeneous rates, longer-range jumps, inaccurate transition estimates or random sampling intervals, the arithmetic restriction need not apply. A nearly symmetric propagator at large finite time is not exactly reversible. Odd-index sampled matrices are valid reversible *discrete-time* chains even though no *reversible continuous-time* embedding exists. Historical priority remains open to wider specialized sources; no independent scientific audit has been performed.

## References
- Yong Chen and Jianmin Chen, *On the Imbedding Problem for Three-state Time Homogeneous Markov Chains with Coinciding Negative Eigenvalues* (first public 2010-09-11), https://arxiv.org/abs/1009.2152 .
- Chen Jia, *A solution to the reversible embedding problem for finite Markov chains* (first public 2016-05-11), https://arxiv.org/abs/1605.03502 .
- M. T. Bauer, U. Seifert and J. van der Meer, *Stroboscopic measurements in Markov networks: Exact generator reconstruction vs. thermodynamic inference* (first public 2024-12-20), https://arxiv.org/abs/2412.15642 .
- E. Baake, M. Baake and J. Sumner, *Embedding of reversible Markov matrices* (first public 2025-11-27), https://arxiv.org/abs/2511.22800 .
