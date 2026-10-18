# One pendant-edge defect and arithmetic single-site controllability of weighted sunlet graphs

## Finding
For \(n\ge3\), one nonuniform pendant-edge weight in a sunlet \(C_n\circ K_1\) makes the weighted Laplacian spectrum simple. Except for a finite explicitly computable set of defect weights, a single cycle or leaf vertex at index \(j\) controls the full consensus network exactly when
\[
\gcd\!\left(j,\frac{n}{\gcd(n,2)}\right)=1.
\]
Precisely \(2\gcd(n,2)\varphi(n/\gcd(n,2))\) of the \(2n\) vertices satisfy this condition, where \(\varphi\) is Euler's totient. The exceptional defect weights are genuine, not merely an artifact of the proof.

## Assumptions and scope
Let \(n\ge3\) be an integer. Write \(u_j\) for cycle vertices and \(v_j\) for private leaves, indexed modulo \(n\). Every cycle edge \(u_ju_{j+1}\) has conductance \(a>0\). Every spoke \(u_jv_j\) has conductance \(b>0\), except \(u_0v_0\) with conductance \(c>0\). The weighted Laplacian is \(L(c)\), with diagonal entries equal to the sum of incident conductances and off-diagonal entries minus the conductance. Control means Kalman controllability of the real continuous-time system \(\dot x=-L(c)x+e_s\eta(t)\), with a single, freely time-varying scalar input at one vertex \(s\). The eigenvalues of \(L(c)\), rather than a normalized Laplacian, are used throughout.

Let \(L_0=L(b)\), \(w=e_{u_0}-e_{v_0}\), and \(M=n/\gcd(n,2)\). Thus
\[
L(c)=L_0+(c-b)ww^{\mathsf T}.
\]
For each individual vertex \(s\), let \(\Sigma_0=\operatorname{spec}(L_0)\) and, for \(z\in\mathbb R\setminus\Sigma_0\), define the rational functions
\[
F(z)=w^{\mathsf T}(L_0-zI)^{-1}w,\qquad H_s(z)=e_s^{\mathsf T}(L_0-zI)^{-1}w.
\]
Define the finite, computable set
\[
\mathcal E_s=\left\{b-\frac1{F(z)}:\ z\in\mathbb R\setminus\Sigma_0,\ H_s(z)=0,\ F(z)\ne0,\ b-\frac1{F(z)}>0,\ b-\frac1{F(z)}\ne b\right\}.
\]
These conditions involve exact characteristic polynomials and rational functions of finite matrices, so \(\mathcal E_s\) is algebraically computable for algebraic conductances \(a,b\), without floating-point eigenvector thresholds.

**Exact statement.** If \(c=b\), no single-vertex input controls the system. If \(c>0\), \(c\ne b\), the spectrum of \(L(c)\) is simple. If \(\gcd(j,M)>1\), neither \(u_j\) nor \(v_j\) controls the system for any such \(c\). If \(\gcd(j,M)=1\), vertex \(s\in\{u_j,v_j\}\) controls the system **if and only if** \(c\notin\mathcal E_s\). Each set \(\mathcal E_s\) is finite.

## Proof
**1. Uniform spectral channels.** Let \(Q_n\) be the unweighted cycle Laplacian. In the core-then-leaf ordering,
\[
L_0=\begin{pmatrix}aQ_n+bI&-bI\\-bI&bI\end{pmatrix}.
\]
For each cycle eigenvalue \(d_k=2a(1-\cos(2\pi k/n))\), the two associated eigenvalues of \(L_0\) are
\[
\lambda_\pm(d_k)=\frac{d_k+2b\pm\sqrt{d_k^2+4b^2}}2.
\]
Both branches are strictly increasing in \(d_k\). The lower branch is in \([0,b)\) and the upper branch in \([2b,\infty)\), hence different cycle-frequency magnitudes and different branches never collide. For \(k=1,\ldots,\lfloor(n-1)/2\rfloor\), each frequency yields an even cosine and an odd sine eigenvector in each vertical branch. The zero frequency and (for even \(n\)) the alternating frequency occur only in the even sector. Thus the restriction of \(L_0\) to reflection-even vectors has *simple* spectrum, and each odd-sector eigenvalue is also represented by exactly one positive even-sector eigenvector. The eigenvalue \(0\) is simple because the graph is connected.

**2. The defect removes every spectral degeneracy.** Reflection through index \(0\), applied simultaneously to the core and the leaves, fixes \(w\). Therefore the perturbation leaves the odd-sector eigenvectors unchanged. At \(u_0\), all even cosine modes are nonzero. For any positive eigenvalue, the core and leaf amplitudes of the corresponding vertical eigenvector differ, as is immediate from the two-by-two eigenvalue equations; hence \(w\) has nonzero overlap with *every* positive even-sector eigenvector. Its overlap with the constant zero mode is zero. A rank-one perturbation of a simple symmetric matrix by a vector with nonzero components in each nonzero eigendirection yields simple moving eigenvalues. More explicitly, the determinant lemma gives the secular factor \(1+(c-b)F(z)\), and at each positive even-sector eigenvalue the characteristic polynomial of the perturbed even block is nonzero because the associated spectral residue of \(F\) is nonzero. Thus, for \(c\ne b\), no moving even eigenvalue equals an old positive even eigenvalue or an unchanged odd eigenvalue. Finally \(0\) remains simple for \(c>0\), by connectedness. All \(2n\) eigenvalues are therefore distinct.

**3. Permanent arithmetic obstructions.** An odd-sector eigenvector at frequency \(k\) has both core and leaf amplitudes nonzero, each proportional at index \(j\) to \(\sin(2\pi kj/n)\). Thus either input at index \(j\) misses an odd eigenvector precisely when \(n\mid 2kj\) for some \(1\le k\le\lfloor(n-1)/2\rfloor\). This is equivalent to \(\gcd(n,2j)>\gcd(n,2)\), or \(\gcd(j,M)>1\). For \(c=b\), the two-dimensional uniform Fourier eigenspaces alone rule out single-input controllability.

**4. The finite exceptional set and sufficiency.** When \(c\ne b\), the eigenvectors associated with the moving even eigenvalues \(z\notin\Sigma_0\) are scalar multiples of \((L_0-zI)^{-1}w\), and their eigenvalue equation is \(1+(c-b)F(z)=0\). A moving eigenvector vanishes at \(s\) exactly when \(H_s(z)=0\), equivalently \(c\in\mathcal E_s\). This proves the proposed necessary-and-sufficient condition by the symmetric-matrix Popov–Belevitch–Hautus criterion, once the zeros of \(H_s\) are known to be finite.

To see finiteness, expand at infinity:
\[
H_s(z)=-\sum_{r\ge0}z^{-r-1}e_s^{\mathsf T}L_0^r w.
\]
For \(s=u_j\), the shortest path from \(u_0\) has length \(\min(j,n-j)\); for \(s=v_j\) with \(j\ne0\), it has one extra step. The nearest contribution from \(v_0\) starts at least one step later. The first relevant coefficient is the nonzero signed sum of shortest-path conductance products (for \(s=v_0\), the zeroth coefficient is \(-1\)). Thus \(H_s\) is not the zero rational function, and has finitely many real zeros away from its poles. Only finitely many \(c\) arise from the stated secular equation. The number of admissible indices is \(\gcd(n,2)\varphi(M)\); the two layers double the count.

**5. A real isolated resonance.** At \(n=5\), \(a=b=1\), \(c=1/2\), the characteristic polynomials of \(L(c)\) and its principal minor obtained by deleting core vertex \(u_1\) share the factor \(z^2-3z+1\). Hence an eigenvector vanishes at \(u_1\), although \(\gcd(1,5)=1\). At \(c=2\), exact controllability-rank computation instead gives rank \(10\) for that leader. This shows the finite exclusions cannot generally be omitted.

## Verification
The standalone standard-library program `verify.py` constructs the Laplacian and the complete Kalman matrix and computes modular and exact rational ranks. It reports `VERIFY_OK 1100 controllability-rank checks over finite fields and exact rationals`. The finite checks cover cycle orders \(3\) through \(12\), both leader layers, uniform and nonuniform conductances, and the nontrivial five-cycle exceptional weight. They confirm specific instances but do **not** prove the all-orders theorem, which rests on the spectral and resolvent argument above. The program tests only selected defect weights, so it does not enumerate the entire exceptional set at arbitrary real conductances.

## Relationship to prior work
Barik, Pati and Sarma (2007), Theorem 3.2, give the Laplacian spectrum of *uniform* graph corona products, including a cycle with one identical pendant leaf at each core vertex. Parlangeli and Notarstefano (2011), Section IV.B, give reachability and observability criteria for cycle networks and the obstruction to one leader on a uniform cycle. Hsu (2018), Theorem 3.4, proves single-input controllability transfer for interconnected copies of *identical* graph cells. These results inform the spectral decomposition and motivation but do not state the one-spoke perturbation theorem, the fixed arithmetic eligibility rule across both vertex layers, or the finite secular-resonance exclusion. General spectral simplicity under independent multi-edge perturbations also does not itself imply a classification for **one prescribed edge** with every positive weight except one. The rank-one method is standard; its exact application and arithmetic classification here are the assessed contribution.

## Limitations
The classification concerns the symmetric *combinatorial* weighted Laplacian, a single scalar vertex input, identical cycle conductances, and exactly one exceptional positive pendant conductance. Exceptional weights are given as zeros of explicit rational functions, rather than a universal short closed-form root list. The claim does not cover multiple inputs, heterogeneous remaining spokes, directed dynamics, normalized Laplacians, or uncertain independently time-varying weights. The originality assessment cannot eliminate equivalent formulations in unindexed literature; no independent mathematical audit has been completed.

## References
1. S. Barik, S. Pati, B. K. Sarma, *The Spectrum of the Corona of Two Graphs*, SIAM J. Discrete Math. 21 (2007), 47–56, DOI:10.1137/050624029 (online 2007-01-12).
2. G. Parlangeli, G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (2011-09-16), IEEE Trans. Automat. Control 57 (2012), 743–748.
3. S.-P. Hsu, *Laplacian Controllability of Interconnected Graphs*, arXiv:1808.03022v1 (2018-08-09), Theorems 3.3–3.4.
4. C. Poignard, T. Pereira, J. P. Pade, *Spectra of Laplacian matrices of weighted graphs: structural genericity properties*, arXiv:1704.01677 (2017), generic weighted-graph spectral perturbations; distinct from the fixed single-edge family treated here.
