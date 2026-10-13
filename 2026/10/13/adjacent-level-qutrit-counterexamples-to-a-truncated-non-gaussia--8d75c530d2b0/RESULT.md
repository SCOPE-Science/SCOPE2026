# Adjacent-level qutrit counterexamples to a truncated non-Gaussian minimum-output-entropy conjecture

## Finding
Memarzadeh and Mancini conjectured that, after truncating their amplitude-damping/dephasing channel to dimension \(K+1\), the minimum output entropy under a fixed mean-energy constraint is achieved either by a binomial state or by their farthest-separated two-number state. In the qutrit truncation \(K=2\), that conjecture fails on an explicit interval.

Fix the mean energy \(N=3/2\), set \(\epsilon=1\) (pure dephasing), and write
\[
q=e^{-t}.
\]
For every \(0<t\le \log(4/3)\), so that \(3/4\le q<1\), the admissible state
\[
|\chi\rangle=\frac{|1\rangle+|2\rangle}{\sqrt2}
\]
has strictly smaller output von Neumann entropy than both classes permitted by the conjecture.

At \(K=2\) and \(N=3/2\), the energy constraint leaves only one binomial state: \(M=2\), \(\mu=3/4\). The second conjectured class is
\[
|\kappa_\alpha\rangle=\frac12|0\rangle+\frac{\sqrt3}{2}e^{2i\alpha}|2\rangle,
\]
whose output entropy is independent of \(\alpha\). Thus this comparison exhausts the conjectured candidates.

## Assumptions and scope
The channel is exactly the channel defined by Memarzadeh and Mancini from amplitude damping and pure dephasing, with their parameter \(\epsilon\in[0,1]\). At \(\epsilon=1\), their coefficient formula reduces to
\[
(\Phi_{1,t}(\rho))_{mn}=e^{-(m-n)^2t}\rho_{mn}.
\]
The Hilbert space is truncated to \(\operatorname{span}\{|0\rangle,|1\rangle,|2\rangle\}\), and input states obey
\[
\operatorname{Tr}(\rho\,a^\dagger a)=\frac32.
\]
The result disproves the stated candidate-family conjecture. It does not determine the true global minimizer for every \(t\), every energy, or the mixed amplitude-damping/dephasing regime.

## Proof
Put \(q=e^{-t}\). Pure dephasing multiplies the \((m,n)\) coherence by \(q^{(m-n)^2}\).

For \(|\chi\rangle\), the output is supported on \(\operatorname{span}\{|1\rangle,|2\rangle\}\) and equals
\[
\rho_\chi(q)=
\begin{pmatrix}
0&0&0\\
0&1/2&q/2\\
0&q/2&1/2
\end{pmatrix}.
\]
Its eigenvalues are
\[
0,\qquad \frac{1-q}{2},\qquad \frac{1+q}{2}.
\]
Writing \(h_2\) for the binary entropy,
\[
S(\rho_\chi(q))=h_2\!\left(\frac{1-q}{2}\right).
\]
Set
\[
L(q)=\frac{1+q}{2},\qquad
T(q)=L(q)^2+\frac{(1-L(q))^2}{2}=\frac{3q^2+2q+3}{8}.
\]
For any three-dimensional density matrix with largest eigenvalue at least \(L(q)\), convexity of the square gives
\[
\operatorname{Tr}(\rho^2)\ge T(q).
\]
Therefore \(\operatorname{Tr}(\rho^2)<T(q)\) forces \(\lambda_{\max}(\rho)<L(q)\).

For the unique admissible binomial state, \(M=2\) and \(\mu=3/4\), hence its Fock probabilities are \(1/16,6/16,9/16\). Directly from the dephasing factors,
\[
P_B(q):=\operatorname{Tr}(\rho_B(q)^2)=\frac{9q^8+60q^2+59}{128}.
\]
A factorization gives
\[
T(q)-P_B(q)=\frac{(1-q)\left(9q^7+9q^6+9q^5+9q^4+9q^3+9q^2+21q-11\right)}{128}.
\]
For \(3/4\le q<1\), the parenthesis is strictly positive already from \(21q-11>0\). Hence \(P_B(q)<T(q)\).

For \(|\kappa_\alpha\rangle\), phase covariance makes the output spectrum independent of \(\alpha\), and
\[
P_\kappa(q):=\operatorname{Tr}(\rho_\kappa(q)^2)=\frac{3q^8+5}{8}.
\]
Likewise,
\[
T(q)-P_\kappa(q)=\frac{(1-q)\left(3q^7+3q^6+3q^5+3q^4+3q^3+3q^2-2\right)}{8}.
\]
For \(q\ge3/4\), the parenthesis is at least
\[
3(q^2+q^3)-2\ge \frac{61}{64}>0,
\]
so \(P_\kappa(q)<T(q)\).

Thus both conjectured candidate outputs have largest eigenvalue strictly below \(L(q)\). If such a largest eigenvalue \(\lambda\) is at least \(1/2\), then splitting the remaining spectral weight can only increase entropy, so
\[
S(\rho)\ge h_2(\lambda)>h_2(L(q))=S(\rho_\chi(q)).
\]
If \(\lambda<1/2\), then \(S(\rho)\ge-\log_2\lambda>1>S(\rho_\chi(q))\). Hence \(|\chi\rangle\) strictly beats every conjectured candidate throughout \(0<t\le\log(4/3)\).

## Verification
The bundled `verify.py` checks the exact purity formulas, both polynomial factorizations, the endpoint positivity bounds used on \(q\in[3/4,1)\), and the explicit strict purity gaps at \(q=3/4\) using rational arithmetic only. The proof of the interval statement is symbolic and does not depend on finite sampling or numerical optimization.

At the endpoint \(q=3/4\), the competitor \(|\chi\rangle\) has output spectrum \(\{0,1/8,7/8\}\). The two conjectured candidates satisfy the strict purity inequalities
\[
\frac{6137513}{8388608}<\frac{99}{128},
\qquad
\frac{347363}{524288}<\frac{99}{128},
\]
which instantiate the general argument.

## Relationship to prior work
Memarzadeh and Mancini define the channel, derive the pure-dephasing matrix-element law as a special case of their coefficient formula, introduce the binomial family, and state Conjecture 1 that in a truncated space the minimum output entropy is achieved either by a binomial state or by \(|\kappa_\alpha\rangle\). They support the conjecture by a random search over \(10^5\) states for a four-dimensional example with \(N=0.6\). The counterexample above uses the same channel and constraint but a three-dimensional truncation with \(N=3/2\).

Later work on the bosonic dephasing channel studies quantum capacity and LOCC-assisted quantum capacity under energy constraints. Those objectives optimize coherent-information or entanglement quantities and do not imply the candidate-family statement for minimum output entropy. Targeted searches for the source identifier, the conjecture, qutrit pure dephasing, adjacent Fock states, and fixed-energy minimum output entropy did not locate this counterexample or an implication-equivalent result.

## Limitations
The proof is a counterexample family, not a classification of the true minimum-output-entropy state. It covers pure dephasing \(\epsilon=1\), the qutrit truncation \(K=2\), mean energy \(N=3/2\), and \(0<t\le\log(4/3)\). It does not assert what happens for \(t>\log(4/3)\), other energies or truncations, or \(\epsilon<1\). A differently phrased later observation could have escaped the literature searches.

## References
1. L. Memarzadeh and S. Mancini, “Minimum output entropy of a non-Gaussian quantum channel,” *Physical Review A* **94**, 022341 (2016), arXiv:1605.04525, DOI: 10.1103/PhysRevA.94.022341.
2. A. Arqand, L. Memarzadeh, and S. Mancini, “Quantum capacity of bosonic dephasing channel,” *Physical Review A* **102**, 042413 (2020), arXiv:2007.03897.
3. A. Arqand, L. Memarzadeh, and S. Mancini, “Energy-Constrained LOCC-Assisted Quantum Capacity of the Bosonic Dephasing Channel,” *Entropy* **25**, 1001 (2023), arXiv:2111.04173, DOI: 10.3390/e25071001.
