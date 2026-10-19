# A four-to-five-colour reversal in the weak metastable entropy of clock chains

## Finding

For an \(n\)-site cyclic cosine clock ferromagnet with labelled sites and \(n\ge3\), let \(B_{n,q}\) count spin assignments stable against **every** single-site recolouring that would **strictly lower** the energy. Neutral recolourings are allowed, so this is a *weak energetic* rather than an absorbing-state notion of stability.

Write \(\varphi=(1+\sqrt5)/2\) and \(\zeta=e^{2\pi i/5}\). The four-colour count is exactly
\[
B_{n,4}=\bigl[\varphi^n+(-\varphi^{-1})^n+2\cos(n\pi/3)\bigr]^2.
\]
For five colours, define the nonnegative integer matrix and its unit-modulus twists
\[
T=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix},\qquad
D_r=\operatorname{diag}(1,\zeta^r,\zeta^{-r}),\quad r=0,1,2,3,4.
\]
Then the **finite-size count**, including the global colour-winding constraint, is
\[
B_{n,5}=\sum_{r=0}^4\operatorname{tr}\bigl[(D_rT)^n\bigr].
\]
The asymptotic weak-metastable entropies are
\[
\lim_{n\to\infty}\frac{\log B_{n,4}}n=2\log\varphi,
\qquad
\lim_{n\to\infty}\frac{\log B_{n,5}}n=\log(1+\sqrt2).
\]
Since \(1+\sqrt2<\varphi^2=(3+\sqrt5)/2\), increasing the available number of orientations from four to five **reduces** the exponential number of weakly blocked configurations. More precisely,
\[
\frac{B_{n,5}}{B_{n,4}}
=\left(\frac{1+\sqrt2}{\varphi^2}\right)^n(1+o(1)).
\]

## Assumptions and scope

Fix \(q\in\{4,5\}\), \(n\ge3\), and \(J>0\). Sites are the labelled vertices of a simple \(n\)-cycle, and spin values lie in \(\mathbf Z/q\mathbf Z\). The nearest-neighbour energy is
\[
H_q(s)=-J\sum_{i=0}^{n-1}\cos\!\left(\frac{2\pi(s_{i+1}-s_i)}q\right),
\quad s_n=s_0.
\]
The global spin rotation is **not** quotiented out; cyclic translations of configurations are also distinct. A state is weakly blocked precisely when, for every site and every alternative clock value, the resulting energy is no smaller. The count is not a claim about the states reached under zero-temperature dynamics that accepts neutral moves.

## Proof

**Four-colour reduction.** Identify the four clock orientations with the four pairs \((\sigma,\tau)\in\{\pm1\}^2\) ordered around the unit circle. The edge interaction has the exact identity
\[
\cos\!\left(\frac{\pi(s_i-s_j)}2\right)
=\frac{\sigma_i\sigma_j+\tau_i\tau_j}{2}.
\]
Every recolouring changes either the first component, the second component, or both. Hence a configuration is weakly blocked exactly when **each** component separately has no strictly energy-decreasing Ising flip. Indeed, both individual component flip costs are then nonnegative, so their sum (the simultaneous flip cost) is also nonnegative.

In a ferromagnetic Ising cycle a spin can lower the energy exactly when it is isolated between two opposite-valued neighbours. Let \(w_i\in\{0,1\}\) record whether bond \((i,i+1)\) is a domain wall. Absence of isolated spins means \(w_{i-1}w_i=0\) for every cyclic index. Furthermore \(\sum_i w_i\) must be even, since the Ising chain closes. Each admissible wall vector of even parity yields exactly two spin assignments. The signed hard-core transfer matrices
\[
A(z)=\begin{pmatrix}1&1\\z&0\end{pmatrix}
\]
count cyclic wall patterns with weight \(z^{\sum_i w_i}\). Therefore the Ising component count is
\[
P_n=\operatorname{tr}(A(1)^n)+\operatorname{tr}(A(-1)^n).
\]
The eigenvalues of \(A(1)\) are \(\varphi,-\varphi^{-1}\) and those of \(A(-1)\) are \(e^{i\pi/3},e^{-i\pi/3}\). This proves the stated \(P_n\) and the exact identity \(B_{n,4}=P_n^2\).

**Five-colour local classification.** For a fixed pair of neighbour directions, replacing the middle spin maximizes the sum of its two cosine alignments. Among the five equally spaced directions, the maximizers are: the common neighbour if both coincide; either endpoint if they are adjacent on the five-cycle; and the unique short-arc midpoint if their angular separation is two steps. This follows directly from the sum-of-cosines identity or from the direction of the sum of the two neighbour unit vectors (their angular separation is always less than \(\pi\)). Consequently a weakly blocked configuration has oriented increments
\[
d_i=s_{i+1}-s_i\pmod5\in\{0,+1,-1\}
\]
at every edge, and whenever \(d_{i-1},d_i\) are both nonzero, they have the **same sign**. Conversely, every cyclic increment word with this property reconstructs a weakly blocked configuration provided it winds back to its starting colour: \(\sum_i d_i\equiv0\pmod5\). The adjacency matrix for increment values in the order \((0,+1,-1)\) is exactly \(T\).

For each admissible cyclic increment word with zero winding there are five choices of the initial absolute colour. Root-of-unity filtering of the zero-winding condition gives
\[
B_{n,5}=5\cdot\frac15\sum_{r=0}^{4}\sum_{\text{cyclic admissible }d}
\zeta^{r\sum_i d_i}=\sum_{r=0}^{4}\operatorname{tr}[(D_rT)^n].
\]
This identity is exact for every \(n\ge3\); no open-chain boundary condition was substituted for the periodic one.

**Spectral asymptotics.** Matrix \(T\) is primitive, symmetric, and has eigenvalues \(1+\sqrt2,1,1-\sqrt2\). For each nonzero \(r\pmod5\), \(D_rT\) has spectral radius strictly smaller than the Perron root \(\rho=1+\sqrt2\). To see this, if equality held in the standard irreducible Perron–Frobenius comparison \(|D_rT|=T\), the phase of every nonzero entry would have the form \(\eta h_i\overline h_j\); all three diagonal entries of \(T\) are positive, so their phases would have to agree. But those phases are \(1,\zeta^r,\zeta^{-r}\), which do not agree when \(r\ne0\). Hence all four twisted traces are exponentially smaller than \(\rho^n\), and the untwisted trace equals \(\rho^n+1+(1-\sqrt2)^n\). This proves \(B_{n,5}=\rho^n(1+o(1))\). Similarly \(P_n=\varphi^n(1+o(1))\) gives \(B_{n,4}=\varphi^{2n}(1+o(1))\). Since \(2.41421356\ldots<2.61803398\ldots\), the strict entropy reversal follows.

## Verification

The companion self-contained `verify.py` independently tests the energetic definition by brute-force recolouring of every labelled spin word for both alphabets and each length \(3\le n\le7\), and separately computes the exact four-colour count by signed hard-core transfer matrices and the five-colour count by an integer dynamic programme that tracks increments and winding modulo five. These independent counts agree:

| \(n\) | \(B_{n,4}\) | \(B_{n,5}\) |
|---:|---:|---:|
| 3 | 4 | 5 |
| 4 | 36 | 25 |
| 5 | 144 | 65 |
| 6 | 400 | 185 |
| 7 | 900 | 495 |

For \(8\le n\le16\), the code also evaluates exact transfer counts and checks their inequality. Numerical finite computations corroborate but are not used to establish the asymptotic theorem. Run `python verify.py` with Python 3 (standard library only).

## Relationship to prior work

Baek and Minnhagen (2010) study the very same cosine clock potential and contrast four- and five-state behaviour, but on **two-dimensional equilibrium** lattices through helicity moduli and finite-temperature transition structure. Their complete accessible preprint's model, simulation, and conclusion sections do not present one-dimensional zero-temperature weak-metastability counts. Spirin, Krapivsky, and Redner (2001) study zero-temperature **Ising** freezing and metastable stripe counts in higher-dimensional systems. Their dynamics permits neutral flips with positive probability, so their observation that one-dimensional Ising has no dynamically frozen metastable states does not contradict the present weak energetic classification. Both the familiar Ising/clock correspondence and the general transfer-matrix method are background, not claimed as new. The claimed addition is the exact periodic winding-filtered five-colour count and the mathematically strict four-to-five entropy reversal for weakly blocked configurations.

## Limitations

This is a statement about the count of energy-nondecreasing single-site recolouring minima, *not* dynamically absorbing states when energy-neutral updates are allowed. It does not describe quench probabilities, equilibrium phase transitions, relaxation times, higher spatial dimensions, or general numbers of clock states. The five-colour finite-size formula includes complex numbers in intermediate traces but yields nonnegative integers. Bibliographic uniqueness is not certified; a specialized older enumeration not present in the sources inspected could independently contain an equivalent result.

## References

1. S. K. Baek and P. Minnhagen, “Non-Kosterlitz-Thouless transitions for the \(q\)-state clock models,” *Physical Review E* 82, 031102 (2010). Preprint arXiv:1009.0356v1 (2 September 2010), https://arxiv.org/abs/1009.0356.
2. V. Spirin, P. L. Krapivsky, and S. Redner, “Freezing in Ising Ferromagnets,” arXiv:cond-mat/0105037v1 (2 May 2001), https://arxiv.org/html/cond-mat/0105037v1.
