# Complete topological reversibility boundary for discrete Huygens rings

## Finding
For every integer \(n\ge3\), let \(C_n\) be the unweighted cycle with oriented incidence matrix \(B\), and let \(K=B^{\mathsf T}B\) be its edge Laplacian. On the connected edge-difference torus
\[
\mathcal Z_n=\{z\in(\mathbb R/2\pi\mathbb Z)^n:\sum_{j=1}^n z_j\equiv0\pmod{2\pi}\},
\]
consider the discrete Huygens phase map \(F_h(z)=z+hK\sin z\), where sine is componentwise and \(h>0\). Set
\[
\Lambda_n=\begin{cases}4,&n\text{ even},\\2+2\cos(\pi/n),&n\text{ odd},\end{cases}
\qquad h_n^*=\Lambda_n^{-1}.
\]
Then **the exact global injectivity regime is \(0<h\le h_n^*\)**. For \(0<h<h_n^*\), \(F_h\) is a real-analytic diffeomorphism; at \(h=h_n^*\), it is a homeomorphism with singular differential and hence is not a \(C^1\) diffeomorphism. For **every** \(h>h_n^*\), there is a nonempty open subset of \(\mathcal Z_n\) each of whose points has at least **three distinct regular preimages** under \(F_h\).

In particular, invertibility never returns at stronger coupling, even far beyond the interval in which the dynamics admits a decreasing potential. The three-preimage conclusion concerns an open set of *targets* and holds for arbitrary positive coupling exceeding the threshold, not merely near the first bifurcation.

## Assumptions and scope
The graph is the unweighted, unoriented cycle of length \(n\ge3\). The edge orientation only determines coordinates; the induced map and conclusions are orientation-invariant. The phases are modulo \(2\pi\); the sole quotient is by simultaneous rotation of every vertex phase. The parameter \(h\) may be arbitrarily large; no stability or convergence hypothesis is imposed. A regular preimage is a source at which the derivative on the \((n-1)\)-dimensional quotient tangent space is nonsingular. The conclusion does **not** specify the complete number of preimages at every target and does not concern trajectories after iteration.

## Proof
**1. The sharp closed homeomorphism regime.** Orient each edge and let its column in \(B\) equal the difference of its endpoint basis vectors. Write \(L=BB^{\mathsf T}\), the vertex Laplacian, and \(E=\mathbf1^\perp\). The vertex phase lift is
\[
\widetilde F_h(\theta)=\theta+hB\sin(B^{\mathsf T}\theta),\qquad\theta\in\mathbb R^n.
\]
Its differential is \(I+hB\operatorname{diag}(\cos(B^{\mathsf T}\theta))B^{\mathsf T}\). It descends to the vertex torus and commutes with common-phase translations; the induced quotient map is exactly \(F_h\) through the identification \(z=B^{\mathsf T}\theta\).

For real \(s\ne t\),
\[
(s-t)(\sin s-\sin t)>-(s-t)^2,
\]
because \(1+\cos u\) is nonnegative and does not vanish identically on any interval of positive length. For distinct \(\theta,\phi\in\mathbb R^n\), put \(d=\theta-\phi\) and \(\delta=B^{\mathsf T}d\). If \(\delta\ne0\), summing the strict scalar inequalities gives
\[
\begin{split}
 d\cdot\bigl(\widetilde F_h(\theta)-\widetilde F_h(\phi)\bigr)
 &>\|d\|^2-h\|B^{\mathsf T}d\|^2\\
 &\ge(1-h\Lambda_n)\|d\|^2\ge0
\end{split}
\]
for \(0<h\le h_n^*\). If \(\delta=0\), the left side equals \(\|d\|^2>0\). Thus the lift is injective. Since it satisfies \(\widetilde F_h(\theta+2\pi k)=\widetilde F_h(\theta)+2\pi k\) for every \(k\in\mathbb Z^n\), it is injective on the vertex torus; its degree is one by homotopy to the identity, so compactness makes it a homeomorphism. Equivariance under common-phase shifts shows that its induced map on \(\mathcal Z_n\) is likewise a homeomorphism.

For \(h<h_n^*\), the vertex differential is uniformly positive definite because the bottom eigenvalue of \(BDB^{\mathsf T}\) is at least \(-\Lambda_n\) whenever \(-I\le D\le I\). The quotient differential is therefore invertible everywhere, yielding an analytic diffeomorphism.

For \(h=h_n^*\), if \(n\) is even, choose all edge phases \(\pi\), which satisfy circle closure. The quotient differential, represented on \(E\), is \(I-L/\Lambda_n\) and has a zero eigenvalue. If \(n\) is odd, choose one edge phase \(0\) and all remaining edge phases \(\pi\); their sum is an even multiple of \(\pi\) and hence satisfies closure. Denoting the exceptional edge-incidence column by \(b\), the differential is \(I-L/\Lambda_n+2bb^{\mathsf T}/\Lambda_n\). The highest eigenspace of the odd-cycle Laplacian has dimension two; its intersection with \(b^\perp\) contains a nonzero vector, which the displayed differential annihilates. Therefore no \(C^1\) inverse exists at the threshold.

**2. Negative Jacobian orientation at every supercritical coupling.** Fix \(h>h_n^*\) and define \(c_*=-1/(h\Lambda_n)\in(-1,0)\). For \(c\) slightly below \(c_*\), let \(a=\arccos c\).

If \(n\) is even, assign phase differences \(+a\) to half the edges and \(-a\) to the other half. The sum vanishes, all edge cosines equal \(c\), and the vertex differential on \(E\) is \(J(c)=I+hcL\). The highest cycle eigenvalue \(\Lambda_n\) is simple for even \(n\). At \(c=c_*\), \(J(c_*)\) has a simple zero eigenvalue and all others are positive. At any sufficiently close \(c<c_*\), it therefore has exactly one negative eigenvalue and no zero eigenvalues.

If \(n\) is odd, assign \(+a\) and \(-a\) each to \((n-1)/2\) edges, and \(0\) to the remaining edge, whose incidence column is \(b\). Again the sum vanishes, and
\[
J(c)=I+h\bigl(cL+(1-c)bb^{\mathsf T}\bigr)\quad\text{on }E.
\]
At \(c=c_*\), this becomes
\[
J(c_*)=I-L/\Lambda_n+h(1-c_*)bb^{\mathsf T}.
\]
Both summands on the right are positive semidefinite. Their common kernel equals \(V_{\max}(L)\cap b^\perp\), where the highest-eigenvalue space \(V_{\max}(L)\) has dimension two. This intersection is one-dimensional: the projection of any edge-incidence vector onto \(V_{\max}(L)\) is nonzero, as follows immediately from the nonzero edge difference of a highest-frequency Fourier character. Hence \(J(c_*)\) has precisely one zero eigenvalue, all others positive. Its kernel vector \(v\) satisfies \(b^{\mathsf T}v=0\) and \(Lv=\Lambda_n v\), so
\[
J(c)v=(1+hc\Lambda_n)v.
\]
For \(c<c_*\) sufficiently close, this eigenvalue is negative and the remaining eigenvalues stay strictly positive. Thus in both parities there is a regular source with **negative** Jacobian determinant. At the zero phase configuration the quotient differential is \(I+hL|_E\), which has positive determinant.

**3. Degree forces three regular preimages on an open set.** The maps \(F_h\) are homotopic to the identity via \(F_{th}\), so their degree on the oriented torus \(\mathcal Z_n\) is \(+1\). Take a small inverse-function neighbourhood of the constructed negative-determinant source; its image \(W\) is nonempty and open. By Sard's theorem, \(W\) contains a regular value \(y\) of the full map. Every preimage of this value is regular and, by compactness, there are finitely many. If \(N_+(y)\) and \(N_-(y)\) count the positive- and negative-orientation preimages, respectively, the degree identity gives
\[
N_+(y)-N_-(y)=1.
\]
The chosen negative inverse branch shows \(N_-(y)\ge1\); hence \(N_+(y)\ge2\), and \(y\) has at least three distinct regular preimages. The critical-value set is closed because the source is compact. Shrinking \(W\) around \(y\), the inverse branches persist and the target values remain regular. This proves the claimed nonempty open set.

## Verification
Running `python3 verify.py` with NumPy checks the exact cycle-Laplacian top eigenvalues and the negative-Jacobian construction numerically at \(228\) parameter pairs: \(3\le n\le40\) and six coupling ratios for each \(n\), including couplings just above the threshold and one hundred times the threshold. The program also checks positivity at the zero configuration. Successful output is `VERIFY_OK negative_orientation_samples=228 ring_sizes=38`. These finite floating-point checks are *not* a proof of the all-\(n\), all-\(h\) statement. The strict secant inequality, Fourier top-eigenspace calculation, rank-one inertia argument, and degree identity above constitute the proof.

## Relationship to prior work
Buescu and Oliveira (2026), Theorem 2.1, establish global diffeomorphism when \(h<1/\Lambda_n\) and examine convergence for \(h<2/\Lambda_n\). They do not state that the endpoint map is still a homeomorphism, nor do they classify the noninjective region at arbitrarily large coupling. Buescu, D'Aniello and Oliveira (2026), Theorem 3.2 and Remark 3.3, provide a sufficient invertibility bound for general reciprocal graphs, with an optimality statement for sinusoidal **trees**, not this all-parameter ring multiplicity result. Local singularity and three-branch calculations near the first threshold do not imply persistence of noninjectivity for all larger \(h\); the global orientation-and-degree argument addresses precisely that extra question.

## Limitations
The theorem concerns unweighted cyclic graphs, not general weighted networks. For supercritical coupling it gives a robust lower bound of three regular preimages, not an exact complete inverse-count formula. No claims are made about attractors or almost-everywhere convergence above the Lyapunov interval. An equivalent global parameter classification might preexist in degree-theoretic or phase-network terminology; independent historical-priority assessment has not been performed.

## References
1. Jorge Buescu and Henrique M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, publicly submitted 2026-10-14, especially §§2.1–2.3 and Theorem 2.1. https://arxiv.org/html/2610.19953v1
2. Jorge Buescu, Emma D'Aniello and Henrique M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, publicly submitted 2026-10-07, especially Theorem 3.2, Remark 3.3 and §5. https://arxiv.org/html/2610.10993v1
