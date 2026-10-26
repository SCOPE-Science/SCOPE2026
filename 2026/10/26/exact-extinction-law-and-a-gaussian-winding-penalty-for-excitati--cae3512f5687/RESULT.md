# Exact extinction law and a Gaussian winding penalty for excitation on circular prisms

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the labelled circular prism with upper and lower rims and \(n\) rungs. Under deterministic simultaneous three-state Greenberg–Hastings dynamics, an excited vertex moves \(1\to2\), a refractory vertex moves \(2\to0\), and a resting vertex moves \(0\to1\) exactly when at least one neighbour is excited. Let \(E_n\) count initial configurations eventually reaching the all-rest state. Put \(S=\{0,1,2\}^2\), and define \(g(a,b)=\mathbf1_{(a,b)=(0,1)}-\mathbf1_{(a,b)=(1,0)}\). For \(u=(a,b)\), \(v=(c,d)\) in \(S\), define the Laurent matrix \(M(z)\) by
\[
M(z)_{u,v}=\begin{cases}
z^{g(a,c)},&g(a,c)+g(c,d)-g(b,d)-g(a,b)=0,\\
0,&\text{otherwise}.
\end{cases}
\]
Then the **exact extinction count for every circumference** is
\[
\boxed{E_n=[z^0]\operatorname{tr}(M(z)^n)}.
\]
In particular, \(E_3=261\), \(E_4=1485\), \(E_5=8409\), \(E_6=49215\). Writing
\[
\lambda=\frac{7+\sqrt{33}}2,\qquad
\sigma^2=\frac{2(3\lambda^3+21\lambda-16)}{\lambda(\lambda-2)^2(\lambda+1)^2(2\lambda-7)},
\]
we obtain the **sharp asymptotic law**
\[
\boxed{\frac{E_n}{9^n}\sim\frac{1}{\sqrt{2\pi\sigma^2 n}}\left(\frac{\lambda}{9}\right)^n},
\qquad \lambda\approx6.3722813233,\quad\sigma^2\approx0.04701457047.
\]
Thus the extinction probability for a uniformly random initial configuration is asymptotic to \(1.839898348\,n^{-1/2}(0.7080312581)^n\). The square-root correction comes from the one surviving global winding condition after all local square circulations vanish.

## Assumptions and scope
There are precisely \(2n\) distinguishable vertices, with independent uniform initial states in \(\{0,1,2\}\). Edges join consecutive vertices in each cyclic rim and the two vertices of each rung; for \(n=3\), the graph is the triangular prism. The Greenberg–Hastings update is synchronous and deterministic with excitation threshold one. Extinction means reaching the all-zero configuration in finite time. No claim is made for asynchronous updates, other thresholds, or other numbers of states.

## Proof
**Circulation criterion.** For an oriented edge \(x\to y\) with initial states \(a,b\), assign \(g(a,b)\) as above. The finite-graph synchronization theorem of Gravner–Lyu–Sivakoff states that the synchronous three-state Greenberg–Hastings system synchronizes if and only if this integer antisymmetric edge 1-form has zero integral on every graph cycle [2, Theorem 3 and equation (5)]. A synchronized configuration reaches all-zero within at most two additional updates, and an unsynchronized orbit never reaches all-zero. Hence extinction is equivalent to zero circulation on all cycles.

**Complete independent cycle tests.** The prism has \(3n\) edges and \(2n\) vertices, so its cycle space has dimension \(n+1\). The \(n\) rung squares together with the upper rim generate all cycles over \(\mathbb Z\): each lower-rim edge can be replaced by the corresponding upper-rim edge and the two rungs using a square, after which the remaining upper-rim circulation is determined by one rim cycle. In particular, vanishing square circulations and upper-rim circulation imply vanishing on every cycle. Write the state of rung \(i\) as \(u_i=(a_i,b_i)\). The oriented square from \(u_i\) to \(u_{i+1}\), downward, backward along the bottom rim and upward equals
\[
g(a_i,a_{i+1})+g(a_{i+1},b_{i+1})-g(b_i,b_{i+1})-g(a_i,b_i).
\]
The upper-rim circulation is \(\sum_i g(a_i,a_{i+1})\). Thus a cyclic sequence of \(n\) rung states has all square circulations zero exactly when each corresponding matrix entry \(M(z)_{u_i,u_{i+1}}\) is nonzero; the exponent of the product is the upper-rim circulation. Taking the trace enforces cyclic closure, and coefficient extraction at exponent zero enforces the final independent cycle constraint. This proves the exact formula.

**Spectral growth.** Let \(A=M(1)\). Direct finite matrix arithmetic gives
\[
\det(xI-A)=(x-2)^3(x+1)^4(x^2-7x+4).
\]
The directed graph of the nine rung states with allowed transitions is strongly connected (also checked directly from the displayed transition test) and has self-loops, so \(A\) is primitive. Its simple Perron root is \(\lambda=(7+\sqrt{33})/2\). In the analytic characteristic polynomial \(Q(x,t)=\det(xI-M(e^t))\), exact differentiation at \(t=0\) yields
\[
\partial_t Q(x,0)=0,\qquad
\partial_{tt}Q(x,0)=-2(x-2)(x+1)^2(3x^3+21x-16).
\]
Interchanging colors \(0\) and \(1\) reverses every edge weight and preserves all zero-curl transition conditions. The Perron eigenvalue \(\lambda(t)\) of \(M(e^t)\) is therefore even near zero. Implicit differentiation of \(Q(\lambda(t),t)=0\) yields \(\lambda'(0)=0\) and \(\lambda''(0)/\lambda=\sigma^2\) exactly as above; all factors in \(\sigma^2\) are positive.

**Fourier uniqueness and Gaussian coefficient.** The state \((0,0)\) has an allowed weight-zero self-loop. The allowed directed three-cycle \((0,0)\to(1,1)\to(2,2)\to(0,0)\) has total weight one. Perron equality for the complex weighted matrix therefore implies \(\rho(M(e^{it}))<\lambda\) whenever \(t\not\equiv0\pmod{2\pi}\): equality would force one common edge-phase coboundary, the self-loop fixes its global phase, and the three-cycle then forces \(e^{it}=1\). The same witnesses show that the additive edge observable has positive asymptotic variance. Finally Fourier coefficient extraction gives
\[
E_n=\frac1{2\pi}\int_{-\pi}^{\pi}\operatorname{tr}(M(e^{it})^n)\,dt.
\]
Near zero the unique leading eigenvalue is \(\lambda(e^{it})=\lambda\exp(-\sigma^2t^2/2+O(t^4))\), while all other spectral contributions are exponentially smaller uniformly away from zero. Gaussian integration proves \(E_n\sim\lambda^n/\sqrt{2\pi\sigma^2n}\), and division by the \(3^{2n}=9^n\) equally likely initial configurations gives the probability claim.

## Verification
The standalone script `verify_finite.py` independently builds the nine-state matrix, computes the Laurent trace coefficient and exhaustively iterates all \(9^n\) initial configurations for \(3\le n\le6\), comparing each extinction event with both the direct cycle-curl test and the matrix count. It checks \(261,1485,8409,49215\), respectively. The independent script `verify_symbolic.py` builds the Laurent matrix and checks the full exact characteristic polynomial at \(z=1\) and its second logarithmic-weight derivative using SymPy. Both were executed on the accompanying source code; see `CHECKS.txt`. The finite enumerations serve as corroboration, not as a substitute for the all-size proof.

## Relationship to prior work
The original Greenberg–Hastings model and its spatial waves date to [1] and the early excitable cellular-automata literature [3]. The precise finite-graph circulation criterion employed as an antecedent is [2]. The latter characterizes whether a given configuration synchronizes but does not state the circular-prism extinction sequence, this nine-state weighted transfer matrix, its algebraic Perron constant, or the \(n^{-1/2}\) extinction prefactor. Work on probabilistic GH dynamics on small-world graphs [4] addresses a distinct stochastic update and different graphs. The new contribution here is the exact infinite-family extinction count and sharp asymptotic under a global winding constraint; the circulation criterion itself is not claimed as new.

## Limitations
This result classifies initial configurations by eventual extinction versus persistence, not the periodic attractor classes of persistent trajectories or their activities. The full underlying 1993-era lattice papers and original 1978 article were not inspected in full; an unindexed equivalent prism enumeration is a residual originality risk. The proof relies on the published finite-graph synchronization theorem [2], and its transfer/spectral calculations are independently reproducible. A finite checker alone would not establish the asymptotic.

## References
[1] J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM J. Appl. Math. 34 (1978), 515–523, DOI: 10.1137/0134040 (journal issue dated May 1978; exact original public day not established).

[2] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first posted 2016-10-24, Theorem 3; https://arxiv.org/html/1610.07320v1 .

[3] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002v1, first posted 1993-03-22; https://arxiv.org/abs/patt-sol/9303002 .

[4] L. I. Reyes, *Greenberg-Hastings dynamics on a small-world network: the collective extinct-active transition*, arXiv:1505.00182v1, first posted 2015-05-01; https://arxiv.org/abs/1505.00182 .
