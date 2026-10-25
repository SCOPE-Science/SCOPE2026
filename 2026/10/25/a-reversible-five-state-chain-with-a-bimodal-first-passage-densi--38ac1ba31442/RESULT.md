# A reversible five-state chain with a bimodal first-passage density

## Finding

Among finite irreducible reversible continuous-time Markov chains with one target state, at least five total states are necessary for the first-passage density from a fixed non-target state to have two distinct interior local maxima. This lower bound is attained by the explicit five-state chain below. Thus the unimodality of birth-death passage-time densities does not extend to all finite reversible chains.

## Assumptions and scope

The states are \(0,1,2,3,\dagger\), and \(\dagger\) is the target. The nonzero off-diagonal rates are symmetric and are
\[
q_{03}=q_{30}=100,\quad q_{12}=q_{21}=10,\quad
q_{13}=q_{31}=1,\quad q_{1\dagger}=q_{\dagger1}=1,\quad
q_{23}=q_{32}=10,\quad q_{3\dagger}=q_{\dagger3}=1.
\]
All other off-diagonal rates are zero and each diagonal rate is minus its row's total outgoing rate. The full five-state chain is connected and reversible with uniform stationary distribution. Let \(T=\inf\{t\geq0:X_t=\dagger\}\) for \(X_0=0\). The claim concerns the density \(f\) of \(T\), not the density conditional on a selected path.

## Proof

**Minimality.** Let \(m\) be the number of non-target states and let \(Q\) be the killed subgenerator. Reversibility makes \(Q\) similar to a real symmetric matrix, so it is diagonalizable with real negative eigenvalues. Consequently \(f(t)=e_0^\top e^{Qt}r\), where \(r_i=q_{i\dagger}\), is a linear combination of at most \(m\) real exponentials. Its derivative is also such a combination. A nonzero sum of \(m\) exponentials with distinct real exponents has at most \(m-1\) distinct zeros: multiply by the exponential with the smallest exponent, differentiate, and apply Rolle's theorem inductively. Repeated eigenvalues combine into one exponential because \(Q\) is diagonalizable. Two distinct interior local maxima force at least three distinct zeros of \(f'\) (a maximum, an intervening minimum, and a second maximum). Hence \(m\geq4\), so at least five total states are required.

**Attainment.** For the stated chain, the transient subgenerator and target-rate vector are
\[
Q=\begin{pmatrix}
-100&0&0&100\\
0&-12&10&1\\
0&10&-20&10\\
100&1&10&-112
\end{pmatrix},
\qquad r=\begin{pmatrix}0\\1\\0\\1\end{pmatrix}.
\]
Thus \(f(t)=e_0^\top e^{Qt}r\) and \(f'(t)=e_0^\top e^{Qt}Qr\), with \(Qr=(100,-11,20,-111)^\top\).

For \(N=400\), define the exact rational Taylor sum
\[
S_N(t)=\sum_{k=0}^{N}\frac{e_0^\top Q^kQr}{k!}\,t^k.
\]
Exact rational arithmetic gives
\[
\begin{aligned}
S_{400}(1/100)&\in(11.15,11.17),\\
S_{400}(3/100)&\in(-0.68,-0.66),\\
S_{400}(1/10)&\in(0.024,0.026),\\
S_{400}(3/10)&\in(-0.138,-0.135).
\end{aligned}
\]
The standalone verification script computes these sums exactly and checks all four interval inclusions.

For the remainder, \(\|Q\|_2\leq224\), \(\|Qr\|_2=\sqrt{22842}\), and \(0\leq t\leq0.3\) gives \(\|Qt\|_2\leq67.2\). The exponential-series tail bound
\[
\left\|e^{Qt}-\sum_{k=0}^{400}\frac{(Qt)^k}{k!}\right\|_2
\leq e^{67.2}\frac{67.2^{401}}{401!}<10^{-109}
\]
therefore bounds \(|f'(t)-S_{400}(t)|\) by less than \(2\times10^{-107}\). The four strict signs of \(f'\) are consequently \(+,-,+,-\) at the four displayed times. Continuity gives two distinct interior local maxima, proving attainment of the five-state lower bound.

## Verification

The rational Taylor sums are recomputed from the displayed matrix in `verification/check_derivative_signs.py`, using only Python's standard-library `fractions.Fraction`. The script asserts interval containment using exact integer-ratio arithmetic; the analytic remainder bound above converts these finite checks into rigorous derivative signs. The lower-bound argument is independent of the numerical witness.

## Relationship to prior work

Fill's birth-death passage-time theorem represents the passage time from state \(0\) to state \(d\) as a sum of independent exponential variables; this supports unimodality in the birth-death setting, whose state graph is a path. Keilson's work proves unimodality for passage times in birth-death processes. The present graph contains the triangle \(1\!-\!2\!-\!3\!-\!1\) and is not a birth-death chain.

Hartich and Godec give spectral interlacing and a spectral representation for first-passage distributions in reversible discrete-state dynamics. The representation does not itself imply unimodality when its exponential weights have mixed signs. Kijima's paper on spectral structure for first-passage densities of reversible chains is closely relevant; only its abstract was accessible during this work, so a more detailed comparison remains a limitation rather than a claim of non-coverage.

## Limitations

The result is an exact state-minimal counterexample, not a classification of graphs or rate assignments that yield multiple modes. It does not assert that every non-path reversible chain has a multimodal first-passage density. The full text of Kijima's 1987 article could not be accessed; only its abstract was compared.

## References

1. J. A. Fill, “The passage time distribution for a birth-and-death chain: Strong stationary duality gives a first stochastic proof,” arXiv:0707.4042, first posted 2007-07-27; *Journal of Theoretical Probability* 22 (2009), 543–557.
2. J. Keilson, “On the unimodality of passage time densities in birth-death processes,” *Statistica Neerlandica* 35 (1981), 49–55. DOI: 10.1111/j.1467-9574.1981.tb00710.x.
3. M. Kijima, “Spectral structure of the first-passage-time densities for classes of Markov chains,” *Journal of Applied Probability* 24 (1987), 631–643. DOI: 10.2307/3214095.
4. D. Hartich and A. Godec, “Interlacing Relaxation and First-Passage Phenomena in Reversible Discrete and Continuous Space Markovian Dynamics,” arXiv:1802.10049, first posted 2018-02-27.
