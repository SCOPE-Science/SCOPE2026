# Exact concurrence and optimal entanglement at quarter-turn resonances of a resetting two-qubit gate

## Finding
For the four-level two-qubit entangling gate specified below at either nontrivial quarter-turn resonance \(\theta=\pi/4\) or \(\theta=3\pi/4\), with independent Bernoulli resetting of **both** qubits to \(|\uparrow\uparrow\rangle\) with probability \(p\in(0,1)\) at each step, the unique stationary density operator \(\rho_p\) has Wootters concurrence
\[
\boxed{\mathcal C(\rho_p)=\frac{p(1-p)}{1+(1-p)^2}.}
\]
At the intermediate quarter turn \(\theta=\pi/2\), concurrence instead vanishes identically for all \(p\in(0,1)\). At either nontrivial quarter turn the stationary state is entangled at every interior reset probability, and its concurrence has **exactly one global maximum** over \(0<p<1\):
\[
\boxed{p_*=2-\sqrt2,\qquad \mathcal C_{\max}=\frac{\sqrt2-1}{2}.}
\]
These formulas classify all three quarter-turn angles \(\theta\in\{\pi/4,\pi/2,3\pi/4\}\) at every interior reset probability; they do not optimize over gate angle or over a family of reset states.

## Assumptions and scope
Use the ordered two-qubit basis \((|\uparrow\uparrow\rangle,|\uparrow\downarrow\rangle,|\downarrow\uparrow\rangle,|\downarrow\downarrow\rangle)\). The gate family is \(U_\theta=\exp(i\theta H)\), restricted to \(\theta\in\{\pi/4,\pi/2,3\pi/4\}\), where the entangling generator introduced by Wald, Yao, Platini, Hooley and Carollo has the explicit matrix
\[
H=\begin{pmatrix}
2-\sqrt2&2-\sqrt2&-i-\sqrt2&i-\sqrt2\\
2-\sqrt2&2-\sqrt2&i-\sqrt2&-i-\sqrt2\\
i-\sqrt2&-i-\sqrt2&2+\sqrt2&2+\sqrt2\\
-i-\sqrt2&i-\sqrt2&2+\sqrt2&2+\sqrt2
\end{pmatrix}.
\]
Write \(U=U_{\pi/4}\). Then \(U_{\pi/2}=U^2\) and \(U_{3\pi/4}=U^3\). Starting from the pure reset state \(\rho_0=|\uparrow\uparrow\rangle\langle\uparrow\uparrow|\), independently at every step the state is either reinitialized to \(\rho_0\), with probability \(p\), or updated by \(\rho\mapsto U_\theta\rho U_\theta^\dagger\), with probability \(1-p\). The reported state is the **unconditioned stationary state** of this discrete-time channel. Concurrence is Wootters' standard two-qubit concurrence, not negativity or a postselected trajectory statistic.

## Proof
Set \(q=1-p\in(0,1)\). The eigenvalues of \(H\) are \(-2,0,2,8\). Substituting their phase factors at \(\theta=\pi/4\) in the corresponding spectral projectors gives
\[
U=\frac12\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
-1&1&1&1\\
1&-1&1&1
\end{pmatrix},\qquad U^4=I.
\]
Starting from the coordinate vector \(e_0=(1,0,0,0)^T\), its four-element orbit consists of
\[
\begin{aligned}
\psi_0&=(1,0,0,0)^T,\\
\psi_1&=\tfrac12(1,1,-1,1)^T,\\
\psi_2&=(0,1,0,0)^T,\\
\psi_3&=\tfrac12(1,1,1,-1)^T.
\end{aligned}
\]
For the first quarter-turn angle, the contraction mapping \(\rho\mapsto p\rho_0+qU\rho U^\dagger\) has a unique fixed point, obtained by summing the geometric renewal series. Four-periodicity yields the **exact finite expression**
\[
\rho_p=p\sum_{n\ge0}q^nU^n\rho_0U^{-n}
=\frac{\sum_{j=0}^3q^j|\psi_j\rangle\langle\psi_j|}{1+q+q^2+q^3}.
\]
Let \(S=\sigma_y\otimes\sigma_y\) and \(R=\rho_pS\overline{\rho_p}S\), where overline denotes componentwise conjugation in this basis. Direct multiplication of the **displayed four projectors**, without truncating an infinite sum, shows that the characteristic polynomial of \(R\) is
\[
\det(zI-R)=z^2(z^2-Tz+P),
\]
where
\[
T=\operatorname{tr}R
=\frac{q(2q^4-q^3+q^2+q+1)}{2(q+1)(q^2+1)^2}
\]
and
\[
P=\frac{(\operatorname{tr}R)^2-\operatorname{tr}(R^2)}2
=\frac{q^2(q^3+3q^2-q+1)^2}{16(q+1)^2(q^2+1)^4}.
\]
The two nonzero eigenvalues of \(R\) are nonnegative: they coincide with those of the positive semidefinite operator \(\sqrt{\rho_p}(S\overline{\rho_p}S)\sqrt{\rho_p}\). Wootters' formula therefore gives
\[
\mathcal C(\rho_p)^2=T-2\sqrt P.
\]
Since \(q^3+3q^2-q+1=(1-q)+q^2(q+3)>0\), the square root is unambiguous. Factoring exactly,
\[
T-2\sqrt P=\frac{q^2(1-q)^2}{(1+q^2)^2},
\qquad \mathcal C(\rho_p)=\frac{q(1-q)}{1+q^2}>0.
\]
For \(\theta=3\pi/4\), the gate becomes \(U^3\), whose orbit from \(e_0\) exchanges \(\psi_1\) and \(\psi_3\) while leaving \(\psi_0,\psi_2\) unchanged. Direct evaluation of its corresponding spin-flip matrix yields the **same** \(T\) and \(P\) displayed above and therefore the identical concurrence function. At \(\theta=\pi/2\), \(U^2=I\otimes\sigma_x\); the stationary state is a convex mixture of \(|\uparrow\uparrow\rangle\) and \(|\uparrow\downarrow\rangle\), hence it is separable and its concurrence is zero.

Finally
\[
\frac{d}{dq}\frac{q(1-q)}{1+q^2}=
\frac{1-2q-q^2}{(1+q^2)^2}.
\]
Its only zero in \((0,1)\) is \(q_*=\sqrt2-1\); the derivative is strictly positive before that zero and strictly negative after it. The two endpoint limits of the concurrence are zero. Thus this is the unique global optimizer at **each of the two nontrivial quarter turns** and yields the announced \(p_*=1-q_*\) and maximal value. This proves the claim for **all** \(p\in(0,1)\).

## Verification
The accompanying standalone `verify.py` reconstructs the gate exactly from the spectral projectors of the stated \(H\), checks its period-four orbit, derives the exact spin-flip trace and characteristic polynomial at both nontrivial quarter turns, checks the separable half-turn, and verifies the concurrence and derivative identities symbolically. Independently it recomputes the stationary state from the numerical matrix exponential and a truncated, error-controlled geometric series at ten reset probabilities, comparing direct Wootters concurrence with the theorem. Run `python verify.py` with SymPy, NumPy and SciPy. This is supplementary reproducibility: the infinite-parameter assertion is proved algebraically above, not by the finite numerical tests.

## Relationship to prior work
Wald, Yao, Platini, Hooley and Carollo derived the general geometric stationary density operator and the specific entangling generator, and numerically exhibited nonvanishing concurrence at the resonance \(\theta=\pi/4\), including its continuous disappearance as resetting becomes rare. Those facts, including qualitative absence of a finite-reset entanglement threshold, are **not claimed as new**. The additional result here is a complete exact concurrence law at all three quarter-turn resonances and the algebraic **unique concurrence-maximizing reset probability** at the two nontrivial ones, which are not given by the source's plots, its spectral resonance condition, or a partial-transpose sign calculation alone. Work on continuous-time quantum resetting and on other spin-chain entanglement models supplies related motivation but not this gate-specific optimization.

## Limitations
The global optimality is **only over the Bernoulli reset probability at fixed** \(\theta=\pi/4\) or \(3\pi/4\), fixed initial/reset state and fixed two-qubit gate. It neither characterizes neighboring detuned gate angles nor establishes an optimum over arbitrary controls, initial states, gate costs or non-Poissonian reset protocols. At \(p=0\) the unitary trajectory need not possess a unique stationary state, although the formula extends continuously to a zero-concurrence limiting mixture. Definitive publication priority beyond the compared literature remains uncertain.

## References
1. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, "Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems", first preprint arXiv:2410.11497v1, 15 October 2024; *Quantum* **9**, 1742 (2025), https://arxiv.org/html/2410.11497v1 and https://doi.org/10.22331/q-2025-05-13-1742.
2. W. K. Wootters, "Entanglement of formation of an arbitrary state of two qubits", *Physical Review Letters* **80**, 2245–2248 (1998), https://doi.org/10.1103/PhysRevLett.80.2245.
3. M. Kulkarni and S. N. Majumdar, "Generating entanglement by quantum resetting", *Physical Review A* **108**, 062210 (2023), arXiv:2307.07485, https://arxiv.org/abs/2307.07485.
