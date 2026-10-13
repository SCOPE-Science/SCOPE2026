# A complete D-optimal sensor phase diagram for four-vertex weighted diffusion paths

## Finding
Consider the four-vertex path with positive conductances \(p,q,r\), and continuous-time diffusion generator
\[
Q=\begin{pmatrix}
-p&p&0&0\\
p&-p-q&q&0\\
0&q&-q-r&r\\
0&0&r&-r
\end{pmatrix}.
\]
For every observation horizon \(T>0\), let \(W_j(T)=\int_0^T e^{Qt}e_je_j^{\mathsf T}e^{Qt}\,dt\) denote the information Gramian for observing state coordinate \(j\in\{1,2,3,4\}\) with one unit-strength scalar sensor. Write
\[
A=p^2-pq-2pr+qr,\qquad B=pq-2pr-qr+r^2.
\]
There is a positive factor \(F(T,p,q,r)\), independent of the observation vertex, such that
\[
\big(\det W_1,\det W_2,\det W_3,\det W_4\big)
=F(T,p,q,r)\,p^2q^4r^2\big(p^4,A^2,B^2,r^4\big).
\]
Thus the complete set of D-optimal vertices is horizon-independent, with the following explicit *conductance phase diagram*.

If \(p=r\), all four vertices are exactly tied, for every \(q>0\). If \(p>r\), define
\[
\Delta=p^2-4pr+r^2,\qquad
\theta=\frac{p^2+2pr-r^2}{p-r}.
\]
The maximizing vertices are:

- When \(\Delta<0\) (equivalently \(1<p/r<2+\sqrt3\)): exactly vertex \(1\) if \(q<2p\); exactly \(\{1,2\}\) if \(q=2p\); exactly vertex \(2\) if \(q>2p\).
- When \(\Delta=0\) (equivalently \(p/r=2+\sqrt3\)): vertex \(1\) if \(q<2p\); \(\{1,2,3\}\) if \(q=2p\); and \(\{2,3\}\) if \(q>2p\).
- When \(\Delta>0\) (equivalently \(p/r>2+\sqrt3\)): vertex \(1\) if \(q<\theta\); \(\{1,3\}\) if \(q=\theta\); and vertex \(3\) if \(q>\theta\).

When \(p<r\), interchange \(p,r\) and reflect the vertices by \(j\mapsto5-j\). Every boundary tie stated above is exact and there are no other maximizers.

Among all weighted paths with at most four vertices, four is the minimum size for which a strictly interior vertex can uniquely maximize the one-sensor determinant: on three vertices the middle vertex is never uniquely optimal, whereas both vertex \(2\) and vertex \(3\) can be uniquely optimal on four vertices.

## Assumptions and scope
All conductances satisfy \(p,q,r>0\). The state dynamics are \(\dot x=Qx\), the sensor has no control action and observes \(y=e_j^{\mathsf T}x\), the observation noise intensity is equal across sites, and the optimization variable is one of the four vertices. The criterion is the ordinary determinant of the finite-horizon continuous-time observability Gramian, not its trace, minimum eigenvalue or a multi-sensor score. There is no assumption of an infinite observation horizon or an asymptotically stable generator: \(Q\) has one zero eigenvalue, and the finite-time Gramian is well defined.

## Proof
**Step 1: Factorization without integrating a Gramian.** Because \(Q\) is a real symmetric irreducible Jacobi matrix, its eigenvalues \(\lambda_1,\ldots,\lambda_4\) are distinct and real. Choose orthogonal \(U\) with \(Q=U\operatorname{diag}(\lambda_1,\ldots,\lambda_4)U^{\mathsf T}\). For the sensor at vertex \(j\), put \(c_j=U^{\mathsf T}e_j\) and define the strictly positive definite exponential Gram matrix
\[
(H_T)_{ab}=\int_0^T e^{(\lambda_a+\lambda_b)t}\,dt.
\]
Then \(W_j=U\operatorname{diag}(c_j)H_T\operatorname{diag}(c_j)U^{\mathsf T}\), hence \(\det W_j=(\prod_a(c_j)_a)^2\det H_T\). The strict positivity of \(H_T\) follows from linear independence of distinct real exponentials on every positive-length interval.

Define the Krylov matrix \(K_j=[e_j,Qe_j,Q^2e_j,Q^3e_j]\). If \(V\) denotes the nonsingular Vandermonde matrix with entries \(V_{ak}=\lambda_a^{k-1}\), then \(K_j=U\operatorname{diag}(c_j)V\), and therefore
\[
\det W_j=\frac{\det H_T}{(\det V)^2}\,(\det K_j)^2.
\]
The factor \(F=\det H_T/(\det V)^2\) is strictly positive and independent of \(j\). This fixed-sensor determinant factorization is established in general by earlier spectral-Gramian work; it is not asserted to be new here.

**Step 2: Explicit weighted-path volumes.** Direct multiplication of the four powers of \(Q\) gives the exact Krylov determinants
\[
(\det K_1,\det K_2,\det K_3,\det K_4)
=pq^2r\,(p^2,-A,-B,r^2).
\]
Squaring proves the common-factor formula. This polynomial identity also has an exact, finite interpolation certificate in the accompanying checker: both sides have degree at most six in each conductance, and they agree for every triple chosen from seven distinct rational values in each variable. This exact interpolation verifies the identities for all real conductances, rather than treating sampling as evidence for an infinite claim.

**Step 3: All comparison regimes.** By path reflection it is enough to consider \(p>r\). In this case \(p^4>r^4\); the fourth site cannot be optimal. Write
\[
A=p(p-2r)-(p-r)q,\quad
B=r(r-2p)+(p-r)q,\quad A+B=\Delta.
\]
At \(q=0\), both \(|A|\) and \(|B|\) are strictly below \(p^2\). Each is affine in \(q\), with \(A\) strictly decreasing and \(B\) strictly increasing. For every \(q>0\), the first interior score reaches or exceeds \(p^4\) exactly when \(q\ge2p\); the second reaches or exceeds it exactly when \(q\ge\theta\). Their threshold displacement is
\[
\theta-2p=-\frac{\Delta}{p-r}.
\]
Above both thresholds \(A<0<B\), so \(|A|-|B|=-\Delta\). If \(\Delta<0\), vertex \(2\) crosses first and thereafter stays better than vertex \(3\). If \(\Delta>0\), vertex \(3\) crosses first and thereafter stays better than vertex \(2\). If \(\Delta=0\), both cross simultaneously and their scores remain equal. This yields all three regimes and every tie set. For \(p=r\), direct substitution gives \(A=B=-p^2\), establishing the universal four-way tie. Reflecting treats \(p<r\).

**Step 4: Minimality.** A two-vertex path has symmetric endpoint observation volumes. On a three-vertex path with positive edge weights \(p,q\), the three Krylov determinants are \(p^2q,-pq(p-q),-pq^2\). Consequently its observation-determinant ratio is \(p^2:(p-q)^2:q^2\). Since \(|p-q|<\max\{p,q\}\) for positive \(p,q\), its middle vertex cannot strictly maximize. Four vertices suffice: with \((p,q,r)=(2,5,1)\), the determinant score ratio is \(16:25:4:1\), uniquely favoring vertex \(2\); with \((p,q,r)=(4,10,1)\), it is \(256:484:529:1\), uniquely favoring vertex \(3\).

## Verification
Run \(\texttt{python3 verify.py}\) with Python's standard library. The checker reconstructs each Krylov matrix directly from the displayed generator and proves its four determinant identities by exact integer arithmetic on a seven-by-seven-by-seven interpolation grid, using the proved degree bound. It separately checks every regime for 26,460 positive integer conductance triples, rational boundary cases, both interior-optimal witnesses, and the three-vertex minimality inequality. The exact mathematical proof above supplies the all-positive-real phase classification; the large finite grid is an additional regression check, not a substitute for Step 3.

## Relationship to prior work
Optimal Gramian-based sensor placement and trace modularity were treated by Summers and Lygeros (2013). Summers, Cortesi and Lygeros (2014) established log-determinant submodularity for sets of actuators/sensors. Most importantly, Dilip (2019), Lemma 2, Theorem 3 and Remark 7, gives an exact spectral-product solution to single-input/single-output determinant placement for symmetric systems, so **the determinant factorization and horizon independence are prior results**. Dilip also discusses an unweighted six-vertex path example. The present statement is confined to the explicit, *all-positive-weight* classification for the smallest weighted path with a potentially strictly optimal interior sensor: the critical ratio \(2+\sqrt3\), the distinct boundaries \(2p\) and \(\theta\), the three-way boundary tie and the minimal-size phenomenon. No priority is claimed for the general Gramian method or sensor–actuator duality.

## Limitations
The phase diagram is specific to a symmetric four-vertex path with one equally weighted scalar sensor. General spectral-product placement criteria already cover the evaluation of any fixed candidate; the additional contribution here is the closed parameter-space classification. The checker verifies the polynomial identities exactly and samples the inequalities, while the analytic proof handles the continuum and all boundary cases. No claim is made about other graph topologies, unequal sensor noise, more than one sensor, or alternative optimality criteria. A residual literature risk remains that a weighted-path-specific analysis or graph-polynomial formulation already states the same complete phase diagram.

## References
1. T. H. Summers and J. Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks*, arXiv:1306.2491, first public submission 2013-06-11. https://arxiv.org/abs/1306.2491
2. T. H. Summers, F. L. Cortesi and J. Lygeros, *On Submodularity and Controllability in Complex Dynamical Networks*, arXiv:1404.7665 (2014). https://arxiv.org/abs/1404.7665
3. A. S. A. Dilip, *The Controllability Gramian, the Hadamard Product, and the Optimal Actuator/Leader and Sensor Selection Problem*, IEEE Control Systems Letters **3** (2019), 883–888. DOI:10.1109/LCSYS.2019.2919278. Author-uploaded manuscript: https://www.researchgate.net/publication/333408055_The_Controllability_Gramian_the_Hadamard_Product_and_the_Optimal_ActuatorLeader_and_Sensor_Selection_Problem
