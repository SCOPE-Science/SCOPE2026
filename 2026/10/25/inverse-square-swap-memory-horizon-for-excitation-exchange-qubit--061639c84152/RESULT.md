# Inverse-square-SWAP memory horizon for excitation-exchange qubit collisions

## Finding
For each fixed environmental memory retention \(0<\lambda<1\), the number of successive-step increases in the trace distance between the two energy-basis inputs of a partially reset qubit collision process diverges at a sharp inverse-square-SWAP rate. With \(\varepsilon=\cos^2\theta\) and \(u=\sqrt\lambda\), write \(R_\lambda(\varepsilon)\) for this number. Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon R_\lambda(\varepsilon)
=\frac{u(1-u^2)}{2(1+6u^2+u^4)}\log\frac{1+u}{1-u}.
\]
For every fixed \(0<\lambda<1\) and all sufficiently small \(\varepsilon>0\), the number is finite. At the endpoint \(\varepsilon=0\), there are infinitely many backflow events. This describes **the fixed input pair**, not the optimization defining the full Breuer--Laine--Piilo measure.

## Assumptions and scope
System \(S\) and environment \(E\) are qubits with basis \(|0\rangle,|1\rangle\). Initially \(E\) is in \(|0\rangle\langle0|\). The comparison system preparations are \(|1\rangle\langle1|\) and \(|0\rangle\langle0|\). At every collision, the excitation-preserving unitary \(U_\theta\) fixes \(|00\rangle\) and \(|11\rangle\), and on the ordered one-excitation basis \((|10\rangle,|01\rangle)\) acts as
\[
U_\theta=\begin{pmatrix}\cos\theta&-i\sin\theta\\-i\sin\theta&\cos\theta\end{pmatrix}.
\]
Between collisions, the completely positive trace-preserving map on joint operators is
\[
\mathcal R_\lambda(X)=\lambda X+(1-\lambda)\operatorname{Tr}_E(X)\otimes|0\rangle\langle0|,
\]
where \(0<\lambda<1\). Applying this map after the last collision does not change the reduced system state. Let \(p_n\) be the excitation probability of \(S\) after \(n\) collisions with initial excited system. Define \(R_\lambda(\varepsilon)=\#\{n\in\mathbb Z_{\ge0}:p_{n+1}>p_n\}\) where \(\varepsilon=\cos^2\theta\in(0,1)\). All asymptotics hold with \(\lambda\) fixed, and \(\varepsilon\downarrow0\).

## Proof
The one-excitation subspace and vacuum are invariant. Following the reset, denote the joint one-excitation populations by \(P=\rho_{10,10}\), \(Q=\rho_{01,01}\), and its imaginary coherence by \(y=\operatorname{Im}\rho_{10,01}\). If \(c=\sqrt\varepsilon\), \(s=\sqrt{1-\varepsilon}\), the exact collision/reset recursion is
\[
\begin{pmatrix}P_{n+1}\\Q_{n+1}\\y_{n+1}\end{pmatrix}
=T_{\lambda,\varepsilon}\begin{pmatrix}P_n\\Q_n\\y_n\end{pmatrix},\quad
T_{\lambda,\varepsilon}=\begin{pmatrix}
 c^2&s^2&-2cs\\
 \lambda s^2&\lambda c^2&2\lambda cs\\
 \lambda cs&-\lambda cs&\lambda(c^2-s^2)
\end{pmatrix},\quad (P_0,Q_0,y_0)=(1,0,0).
\]
The reduced excitation probability is \(p_n=P_n\). From the initial ground-system, vacuum-environment preparation the joint state stays \(|00\rangle\langle00|\); hence \(\tfrac12\|\rho_S^{(1)}(n)-\rho_S^{(0)}(n)\|_1=p_n\) exactly. Thus a strict increase of \(p_n\) is a trace-distance revival.

A direct determinant gives the characteristic polynomial
\[
f_{\lambda,\varepsilon}(x)
=x^3+[\lambda-(1+3\lambda)\varepsilon]x^2
+[\lambda(3\varepsilon-1)+\lambda^2\varepsilon]x-\lambda^2.
\]
Set \(u=\sqrt\lambda\). At \(\varepsilon=0\), this factors as \((x^2-u^2)(x+u^2)\), with three distinct roots \(u,-u,-u^2\). The implicit-function theorem and differentiation of \(f=0\) give three real analytic eigenvalue branches for sufficiently small positive \(\varepsilon\):
\[
r_+=u+\frac{(1-u)^3}{2(1+u)}\varepsilon+O(\varepsilon^2),\qquad
r_-=-u+\frac{(1+u)^3}{2(1-u)}\varepsilon+O(\varepsilon^2),\qquad
r_3=-u^2+O(\varepsilon).
\]
In particular \(0<|r_3|<|r_-|<r_+<1\) once \(\varepsilon\) is small enough. Distinct-eigenvalue interpolation applied to \(p_0=1\), \(p_1=\varepsilon\) and \(p_2=\lambda-4\lambda\varepsilon+(3\lambda+1)\varepsilon^2\) yields
\[
p_n=C_+r_+^n+C_-r_-^n+C_3r_3^n,\qquad C_+=\tfrac12+O(\varepsilon),\quad C_-=\tfrac12+O(\varepsilon),\quad C_3=O(\varepsilon).
\]
The \(C_\pm\) are positive for sufficiently small \(\varepsilon\). Define \(\Delta_n=p_{n+1}-p_n\). For even \(n\), both leading terms \(C_+(r_+-1)r_+^n\) and \(C_-(r_--1)r_-^n\) are negative. The remainder \(C_3(r_3-1)r_3^n\) is uniformly smaller than the first in absolute value, since its ratio is at most \(O(\varepsilon)(|r_3|/r_+)^n\). Therefore every even-indexed \(\Delta_n\) is strictly negative.

For odd \(n\), the positive term \(C_-(1-r_-)|r_-|^n\) competes with the negative term \(C_+(1-r_+)r_+^n\). Their positive ratio is
\[
Q_\varepsilon(n)=\frac{C_-(1-r_-)}{C_+(1-r_+)}\left(\frac{|r_-|}{r_+}\right)^n.
\]
Using the root expansions, uniformly for \(n\varepsilon\) in compact subsets of \([0,\infty)\),
\[
\log Q_\varepsilon(n)=\log\frac{1+u}{1-u}
-\frac{1+6u^2+u^4}{u(1-u^2)}n\varepsilon+O(\varepsilon+n\varepsilon^2).
\]
Let
\[
K(u)=\frac{u(1-u^2)}{1+6u^2+u^4}\log\frac{1+u}{1-u}>0.
\]
For every fixed \(0<\delta<K(u)\), and all sufficiently small \(\varepsilon\), all odd \(n\le(K(u)-\delta)/\varepsilon\) have \(\Delta_n>0\), while all odd \(n\ge(K(u)+\delta)/\varepsilon\) have \(\Delta_n<0\). To make these inequalities uniform, use \(|r_3|/r_+\le q<1\), \(C_3=O(\varepsilon)\), and the fact that \(Q_\varepsilon(n)\) strictly decreases in \(n\). Near either fixed-\(\delta\) boundary, the two main terms are separated by a fixed relative factor, and the third mode is bounded by \(O(\varepsilon)q^n\); for larger \(n\), that bound only improves. The count therefore lies between the numbers of positive odd integers below the two boundaries, up to an additive constant. After multiplying by \(\varepsilon\) and then letting \(\delta\downarrow0\), one obtains \(\varepsilon R_\lambda(\varepsilon)\to K(u)/2\), as claimed. The negative tail also proves finiteness at each sufficiently small positive \(\varepsilon\).

Finally, at exact exchange \(\varepsilon=0\) the collision swaps the single excitation while the intervening reset retains it with probability \(\lambda\); therefore \(p_{2m}=\lambda^m\) and \(p_{2m+1}=0\), so there are infinitely many positive steps \(p_{2m+2}-p_{2m+1}>0\).

## Verification
Run `python3 revival_proof_check.py` with Python 3. The program directly evolves the full four-dimensional joint density matrix under the specified unitary and completely positive reset and compares it with the independently written three-variable recurrence at 20 parameter combinations and 35 steps. It checks the two-step polynomial and representative small-\(\varepsilon\) counts against the limiting coefficient. In the packaged execution, 1,432 assertions passed. These finite computations do not prove any infinite-\(n\) or \(\varepsilon\downarrow0\) assertion; the proof above supplies those conclusions.

## Relationship to prior work
Bhoi and Shaji's June 2026 work [1] develops repeated collisions with an environmentally modified qubit, and analyzes non-Markovian regimes and divisibility, including explicit dynamics for partial-reset variants. The source does not determine the number of fixed-state-pair trace-distance revivals or its sharp near-perfect-exchange law. Ciccarello and Giovannetti [2] develop incoherent partial-swap collision memory and a general renewal/master-equation description, without a discrete inverse-square-SWAP backflow-count limit. Megier and collaborators [3] study the number of trace-distance revivals in different quantum renewal processes and provide different finite event bounds. The established trace-distance interpretation of backflow is due to Breuer, Laine and Piilo [4]. The claim here is only the new **explicit asymptotic counting law for the stated repeated finite-environment model**; none of these general frameworks, observables or reset mechanisms are attributed as novel.

## Limitations
The model assumes ideal resonant exchange, a fixed qubit environment initially in vacuum, a state-independent probabilistic partial reset, exact collision counting and no additional decoherence. The limit is pointwise in each fixed \(0<\lambda<1\), not uniform as \(\lambda\to0\) or \(\lambda\to1\). The count concerns one prescribed orthogonal input pair, not the optimized non-Markovianity measure; it ignores finite measurement resolution, and the theorem does not provide a universal finite-\(\varepsilon\) exact count away from the near-SWAP regime. Scientific priority remains subject to independent literature checking.

## References
[1] G. Bhoi and A. Shaji, *Collision models for open quantum systems coupled to finite environments*, arXiv:2606.14163v1, first submitted 12 June 2026, https://arxiv.org/html/2606.14163v1 .

[2] F. Ciccarello and V. Giovannetti, *A quantum non-Markovian collision model: incoherent swap case*, arXiv:1305.0225v1 (2013), https://arxiv.org/html/1305.0225v1 .

[3] N. Megier et al., *Memory Effects in Quantum Dynamics Modelled by Quantum Renewal Processes*, *Entropy* **23**, 905 (2021), https://doi.org/10.3390/e23070905 .

[4] H.-P. Breuer, E.-M. Laine and J. Piilo, *Measure for the Degree of Non-Markovian Behavior of Quantum Processes in Open Systems*, *Physical Review Letters* **103**, 210401 (2009), https://doi.org/10.1103/PhysRevLett.103.210401 .
