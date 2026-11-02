# Exact timestep-invariant circulation and increasing entropy production for stochastically rounded Euler rotation

## Finding
For a damped planar linear rotation evaluated by forward Euler followed by independent, unbiased nearest-integer stochastic rounding of the **completed** Euler update, a four-point integer lattice cell carries an exact irreversible stationary circulation for every admissible positive step. The stationary probability current per unit physical time is **exactly** \(c/4\), independent of step size \(h\), whereas the stationary entropy production **per physical time** is strictly increasing in \(h\):
\[
\frac{\Sigma_h}{h}=c\log\!\left(\frac{(1+c)[2-h(1-c)]}{(1-c)[2-h(1+c)]}\right),\qquad
\frac{d}{dh}\frac{\Sigma_h}{h}=\frac{4c^2}{[2-h(1-c)][2-h(1+c)]}>0.
\]
Here \(0<c<1\) and \(0<h<1/(1+c)\). The uniform four-corner stationary measure and positive error floor are exact, despite geometric convergence of the expected state to the ordinary differential equation equilibrium. A continuous-time four-state Markov limit is given explicitly, but the mere existence and current of that limit also follow from earlier asymmetric-spin models and are **not claimed as an independent novelty**.

## Assumptions and scope
Let \(\theta=(1/2,1/2)^\mathsf{T}\), \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), and \(F(x)=(-I+cJ)(x-\theta)\). The continuous system \(\dot x=F(x)\) contracts to \(\theta\) at radial rate \(e^{-t}\). Write \(B_h=(1-h)I+hcJ\), with \(0<c<1\), \(0<h<1/(1+c)\). Starting from **any** of the four corners of \(\{0,1\}^2\), form the exact Euler proposal \(y=\theta+B_h(X_k-\theta)\), then independently and freshly round each of its two coordinates to \(0\) or \(1\), with probability of rounding up equal to the coordinate's fractional part. This is fixed-unit-grid stochastic nearest rounding of the single completed Euler update; it is **not** a model of every intermediate floating-point operation, IEEE variable-spacing grids, or arbitrary starting states. All probabilities are conditional on \(X_k\); \(X_k\in\{0,1\}^2\) for all \(k\).

Define a spin state \(s=2(x-\theta)\in\{-1,1\}^2\). Label the corners clockwise as \(s^{(0)}=(-1,-1)\), \(s^{(1)}=(-1,1)\), \(s^{(2)}=(1,1)\), \(s^{(3)}=(1,-1)\). Let \(P_h(s,t)\) be the transition matrix, \(\pi\) its stationary law and \(J_h=\pi(s^{(i)})P_h(s^{(i)},s^{(i+1)})-\pi(s^{(i+1)})P_h(s^{(i+1)},s^{(i)})\) the oriented edge current (indices modulo four). Define standard stationary entropy production in natural logarithm units by
\[
\Sigma_h=\sum_{s,t}\pi(s)P_h(s,t)\log\frac{\pi(s)P_h(s,t)}{\pi(t)P_h(t,s)}.
\]
All summands are defined because each transition probability is positive.

## Proof
Put \(a=1-h\), \(b=hc\). For spins \(s,t\), the proposal mean spins are \(m_1=as_1+bs_2\) and \(m_2=-bs_1+as_2\), so coordinatewise stochastic rounding gives exactly
\[
P_h(s,t)=\frac14(1+t_1m_1)(1+t_2m_2).
\]
Because \(0<h<1/(1+c)\), one has \(a>b>0\), \(a+b=1-h(1-c)<1\) and therefore \(|m_i|<1\). All sixteen transitions are strictly positive, yielding a unique stationary law and geometric convergence.

For each fixed \(t\), summing the preceding product over the four \(s\) gives one: the averages of \(m_1\) and \(m_2\) vanish, while \(\sum_s m_1m_2=0\) because \(m_1m_2=(a^2-b^2)s_1s_2+ab(s_2^2-s_1^2)=(a^2-b^2)s_1s_2\). Thus \(P_h\) is doubly stochastic and its unique invariant probability is \(\pi(s)=1/4\).

Direct substitution into \(P_h\), for **each** oriented neighboring pair of the clockwise order, gives
\[
 p_+=P_h(s^{(i)},s^{(i+1)})=\frac{h(1+c)[2-h(1-c)]}{4},\quad
 p_-=P_h(s^{(i+1)},s^{(i)})=\frac{h(1-c)[2-h(1+c)]}{4}.
\]
Subtracting yields \(p_+-p_-=hc\), hence \(J_h=(p_+-p_-)/4=hc/4\) and **\(J_h/h=c/4\) identically at every admissible step**. Transitions between opposite corners have equal probability in both directions, and self-transitions carry no current. Summing the four nearest-edge contributions to the entropy production gives \(\Sigma_h=(p_+-p_-)\log(p_+/p_-)=hc\log(p_+/p_-)\). Substitution yields the stated entropy formula. Its derivative is obtained by differentiating the two elementary logarithms, and is strictly positive; as \(h\downarrow0\), \(\Sigma_h/h\to c\log((1+c)/(1-c))>0\).

Unbiasedness of rounding implies \(\mathbb E[X_{k+1}-\theta\mid X_k]=B_h(X_k-\theta)\), so \(\mathbb E[X_k]-\theta=B_h^k(X_0-\theta)\). Since the eigenvalues of \(B_h\) are \(a\pm ib\) and \(a^2+b^2<1\), the mean converges geometrically to the continuous equilibrium. However, each corner has squared Euclidean distance \(1/2\) from \(\theta\), so \(\mathbb E\|X_k-\theta\|_2^2=1/2\) for **every** \(k\), independently of \(h\). On the spin basis \(1,s_1,s_2,s_1s_2\), the Markov operator has eigenvalues \(1,a\pm ib,a^2-b^2\), establishing convergence of the full law geometrically to the uniform measure.

Finally, as \(h\downarrow0\), expansion of the exact transition matrix gives \(P_h=I+hQ+O(h^2)\). The off-diagonal entries of \(Q\) are \((1+c)/2\) for clockwise neighbors, \((1-c)/2\) for counterclockwise neighbors, zero for opposite corners, and each diagonal is \(-1\). Standard finite-matrix convergence yields \(P_h^{\lfloor t/h\rfloor}\to e^{tQ}\) for fixed \(t\ge0\). This also shows that the limiting physical-time current is \(c/4\); that limiting-current calculation is covered by the earlier two-spin asymmetric switching-rate framework described below.

## Verification
The standalone script `verify_rounding_circulation.py`, using only the Python standard library, checks the exact rational transition probabilities, positive row sums, double stochasticity, conditional spin moments, all four forward/backward edge probabilities, zero opposite-corner currents, and the finite-step entropy identity across 532 independent rational parameter pairs. It reproduces the message `VERIFY_OK 532 exact rational four-state transition systems, plus entropy calculations`. The proof above supplies parameter-uniform algebra and convergence; finite tests alone cannot establish that theorem. The monotonic entropy derivative and continuous-time limit follow analytically from the displayed formulas.

## Relationship to prior work
El Arar, Sohier, de Oliveira Castro and Petit (arXiv:2207.03837v1, July 8, 2022), in sections 2–3 and their Euler-motivated discussion, establish unbiased stochastic-nearest rounding and assess its accumulation of numerical error; they do **not** derive this finite-state stationary flux and entropy law. Apollonio et al. (arXiv:1904.06257, §§2–4) analyze parallel spin-update Markov algorithms and exact invariant measures; their primary reversible shaken dynamics do not give the antisymmetric rounded-Euler transition identities here. Han et al. (Phys. Rev. Research 6, 023162 (2024), especially its two-spin switching-rate model and current formula) **already derive nonzero circulation for asymmetric two-spin continuous-time chains**. Their model encompasses the **\(h\to0\)** generator here by choosing asymmetric interactions \(K_{12}=\operatorname{atanh}(c)\) and \(K_{21}=-\operatorname{atanh}(c)\), with base flip rate \(\sqrt{1-c^2}/2\). Accordingly, neither nonzero two-spin circulation nor the limiting coefficient \(c/4\) is asserted original. The specific result assessed here is the **all-admissible-finite-step**, independently rounded Euler map's exact \(h\)-invariant physical-time current **together with its strictly increasing entropy production at fixed stationary law**. Finite-step simultaneous coordinate flips, of order \(h^2\), distinguish its transition kernel from Han et al.'s single-flip continuous-time generator. Known general four-state Markov-chain identities are used as background, not claimed novel.

## Limitations
This is an analytically solvable four-corner fixed-grid benchmark, not a theorem for general dimension, floating-point formats, iterative algorithms with rounding at every elementary operation, or other rounding correlations. The square-centered equilibrium is not representable on the selected integer grid. Its uniform invariant law and nonzero current do not imply biased first moments; they coexist with exact convergence of the mean. Independent publication-priority validation has not been performed; a specialized earlier finite-step stochastic-rounding or probabilistic-cellular-automaton calculation might be equivalent.

## References
1. E.-M. El Arar, D. Sohier, P. de Oliveira Castro, E. Petit, *The Positive Effects of Stochastic Rounding in Numerical Algorithms*, arXiv:2207.03837v1 (first posted July 8, 2022), https://arxiv.org/html/2207.03837v1.
2. V. Apollonio, R. D'Autilia, B. Scoppola, E. Scoppola, A. Troiani, *Shaken dynamics: an easy way to parallel Markov Chain Monte Carlo*, arXiv:1904.06257, https://arxiv.org/html/1904.06257v5.
3. C. Han, M. Wang, B. Zhang, M. I. Dykman, H. B. Chan, *Coupled parametric oscillators: From disorder-induced current to asymmetric Ising model*, Physical Review Research **6**, 023162 (May 13, 2024), https://doi.org/10.1103/PhysRevResearch.6.023162.
