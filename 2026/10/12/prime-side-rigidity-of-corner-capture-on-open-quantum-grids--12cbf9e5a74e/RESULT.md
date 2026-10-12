# Prime-side rigidity of corner capture on open quantum grids

## Finding
Let \(p,q\ge 3\) be odd primes, and let \(G=P_{p-1}\square P_{q-1}\) be the Cartesian product of two open path graphs. Place one absorbing site at the corner \(c=(1,1)\). For real nonzero uniform hopping \(\kappa\) and absorption strength \(\gamma>0\), put
\[
H=\kappa(A_{p-1}\otimes I+I\otimes A_{q-1}),\qquad K=H-i\gamma|c\rangle\langle c|.
\]
The subspace of states detectable by this absorber is \(\mathcal B=\operatorname{span}\{H^j|c\rangle:j\ge0\}\). Its dimension is exactly
\[
\dim\mathcal B=\begin{cases}(p-1)(q-1),&p\ne q,\\\frac{(p-1)^2}{2}+1,&p=q.\end{cases}
\]
Consequently every initial density matrix \(\rho\) satisfies
\[
\lim_{t\to\infty}\operatorname{Tr}(e^{-itK}\rho e^{itK^\dagger})
=\operatorname{Tr}[(I-P_{\mathcal B})\rho].
\]
For the uniform incoherent mixture on the \(N=(p-1)(q-1)\) vertices, its eventual absorption probability is exactly
\[
P_{\rm abs}=\begin{cases}1,&p\ne q,\\\frac12+\frac{1}{(p-1)^2},&p=q.\end{cases}
\]
In particular, a square with prime-shifted side length is generally *not* transport-equivalent to a prime-sided rectangle: equality of the primes produces a dark subspace of dimension \((p-1)^2/2-1\), while distinct primes permit complete eventual absorption.

## Assumptions and scope
Paths \(P_n\) have vertex set \(\{1,\ldots,n\}\), nearest-neighbor adjacency \(A_n\), and open (nonperiodic) boundaries. There are no onsite potentials, edge defects, other absorbers, or internal coin degrees of freedom. One absorbing corner is monitored by a time-independent imaginary potential; its strength may be any strictly positive real number. The finite-dimensional survival function uses the unnormalized no-detection evolution \(e^{-itK}\). Odd primality is required of \(p=n+1\) and \(q=m+1\), not of the numbers of vertices. The conclusion applies to all density operators, including coherent and mixed states.

## Proof
**Step 1: absorption is determined by corner spectral support.** For an arbitrary finite Hermitian \(H\), define \(\mathcal B\) as above. Its orthogonal complement consists of precisely those \(H\)-eigenvectors (and their spans) orthogonal to \(c\). This follows by the spectral theorem and polynomial interpolation on the distinct eigenvalues: \(\mathcal B=\operatorname{span}\{P_Ec:P_Ec\ne0\}\), where \(P_E\) denotes the spectral projection at a distinct energy \(E\). Both \(\mathcal B\) and \(\mathcal B^\perp\) reduce \(H\) and the rank-one loss projection. On \(\mathcal B^\perp\), \(K=H\) and evolution is unitary. If \(Kv=zv\) with \(v\in\mathcal B\), then
\[
\operatorname{Im}z=-\gamma\frac{|\langle c,v\rangle|^2}{\|v\|^2}\le0.
\]
Equality forces \(v\) to be an \(H\)-eigenvector perpendicular to \(c\), hence in \(\mathcal B^\perp\), a contradiction. Therefore every eigenvalue of the restriction of \(K\) to \(\mathcal B\) has strictly negative imaginary part. Its finite-dimensional semigroup decays exponentially in norm (possibly after decreasing the exponent to absorb Jordan-polynomial factors). The stated survival limit follows. For \(\rho=I_N/N\), eventual absorption is \(\dim\mathcal B/N\).

**Step 2: visible spectrum of the Cartesian grid.** The path \(P_{p-1}\) has simple eigenvalues and normalized eigenvectors
\[
\lambda_a^{(p)}=2\cos\left(\frac{\pi a}{p}\right),\quad
u_a(x)=\sqrt{\frac2p}\sin\left(\frac{\pi ax}{p}\right),
\qquad 1\le a,x\le p-1.
\]
Its endpoint amplitude \(\nu_a(1)\) never vanishes. The product eigenvectors on the grid therefore all have nonzero amplitude at \(c\). For every distinct value of the sum \(\lambda_a^{(p)}+\lambda_b^{(q)}\), the spectral projection of \(c\) is nonzero, even if the value is degenerate, because its orthogonal product-eigenvector components cannot cancel. Multiplication by the common nonzero hopping \(\kappa\) does not alter equality of sums. Thus \(\dim\mathcal B\) equals the *number of distinct sums*.

**Step 3: independent positive-index cosine basis.** Fix an odd prime \(p\), set \(m=(p-1)/2\), and let \(\zeta=e^{2\pi i/p}\). Put \(t_j=\zeta^j+\zeta^{-j}\), \(1\le j\le m\). These \(m\) numbers are linearly independent over \(\mathbb Q\). Indeed, a relation \(\sum_jr_jt_j=0\) yields
\[
Q(\zeta)=0,\qquad Q(X)=\sum_{j=1}^{m}r_j(X^j+X^{p-j})\in\mathbb Q[X].
\]
Here \(\deg Q\le p-1\), \(Q(0)=0\), and the minimal polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\) has degree \(p-1\) and constant term one. Hence \(Q\) must be zero, so each \(r_j=0\). Moreover \(\{\lambda_a^{(p)}:1\le a\le p-1\}=\{\pm t_j:1\le j\le m\}\) as sets (not necessarily with positive-valued \(t_j\)).

**Step 4: equal primes.** For \(p=q\), every sum of two spectral values is represented by an integer coefficient vector in the independent \(t_j\)'s, and two such sums coincide exactly when their coefficient vectors agree. The distinct values are \(0\), the \(2m\) elements \(\pm2t_j\), and the \(4\binom m2\) elements \(\pm t_i\pm t_j\) with \(i<j\). Their total is
\[
1+2m+4\binom m2=2m^2+1=\frac{(p-1)^2}{2}+1.
\]
This counts all eigenvalue collisions, including zero and the exchange symmetry; no further collisions are possible by linear independence.

**Step 5: distinct primes.** Let \(p\ne q\) be odd primes and suppose
\[
\lambda_a^{(p)}+\lambda_b^{(q)}=\lambda_{a'}^{(p)}+\lambda_{b'}^{(q)}.
\]
The difference on the \(p\)-side lies in \(\mathbb Q(\zeta_p)\), and its negative on the \(q\)-side in \(\mathbb Q(\zeta_q)\). These cyclotomic fields intersect in \(\mathbb Q\): their compositum is \(\mathbb Q(\zeta_{pq})\) of degree \((p-1)(q-1)\), the product of their respective degrees. The common difference is thus rational, and, being an algebraic integer, is an integer \(k\).

For \(p\ge7\), every \(\lambda_a^{(p)}\) belongs to the real cyclotomic field \(F_p=\mathbb Q(\zeta_p+\zeta_p^{-1})\), of degree \(m\), and has field trace either \(1\) or \(-1\). Indeed, \(\lambda_a^{(p)}\) is plus or minus a Galois conjugate of \(\zeta_p+\zeta_p^{-1}\), whose trace equals \(-1\). Thus, if \(\lambda_a^{(p)}-\lambda_{a'}^{(p)}=k\in\mathbb Z\), taking traces gives \(mk\in\{-2,0,2\}\); since \(m\ge3\), necessarily \(k=0\). When \(p=5\), the identical trace argument gives \(|k|\le1\). When \(p=3\), the only two eigenvalues are \(1\) and \(-1\), so each nonzero difference equals \(\pm2\). Consequently, among two *distinct* odd primes, no nonzero integer can be a difference of eigenvalues on *both* sides: at least one prime is at least seven, unless the pair is \(3,5\), whose possible nonzero integer differences have different magnitudes. Hence \(k=0\). Since each path spectrum is simple, \(a=a'\), \(b=b'\); there are exactly \((p-1)(q-1)\) distinct sums.

Combining the five steps proves all assertions.

## Verification
A standalone NumPy/SciPy script `verify.py` independently constructs the path and grid adjacency matrices and checks the predicted ranks for all ordered odd-prime pairs from \(\{3,5,7,11,13\}\). It additionally compares spectral corner overlap, non-Hermitian loss spectra, and finite-time density-matrix survival on smaller grids. The actual replay reports `VERIFY_OK prime_pairs=25 independent_operator_tests=7 long_time_survival=3`. These are finite consistency tests; the field-theoretic argument in the proof is what establishes the result for all odd primes and all positive absorption strengths.

## Relationship to prior work
The identity of the absorbing subspace with the Krylov space generated by a trap and the accompanying dark-state principle are established tools, for instance in Novo et al. (2014). Agliari, Blumen and Mülken (2008) considered continuous-time quantum-walk dynamics on restricted geometries including periodic square lattices; Anishchenko, Blumen and Mülken (2013) studied trapping on randomly restricted planar structures using whole-column sinks. Razzoli, Paris and Bordone (2020) describe general transport efficiency in graph walks with trapping. These sources motivate the setting or its methods, but the inspected treatments do not give the exact two-prime corner rank dichotomy for open grids. The contribution here is the arithmetic evaluation of the entire corner-visible spectrum and the resulting all-state asymptotic absorption law, not the general Krylov criterion or the elementary path eigenbasis.

## Limitations
This theorem does not determine the optimal finite-time transport or an absorption-rate lower bound uniform in lattice size. Its complete-absorption result applies to rectangular open grids with *distinct odd-prime shifted lengths* and uniform hopping, one corner absorber, and positive fixed loss. It is not claimed for general composite lengths, multiple traps, onsite disorder, other boundaries, or non-Markovian detection. The absence of a located equivalent published result does not establish publication priority; a spectral-graph theorem not identified here could subsume the arithmetic component. Independent scholarly assessment remains outstanding.

## References
1. E. Agliari, A. Blumen, O. Mülken, *Dynamics of continuous-time quantum walks in restricted geometries*, arXiv:0810.1184v1 (public 2008-10-07), https://arxiv.org/abs/0810.1184.
2. A. Anishchenko, A. Blumen, O. Mülken, *Geometrical aspects of quantum walks on random two-dimensional structures*, arXiv:1309.2827v1 (public 2013-09-11), https://arxiv.org/abs/1309.2827.
3. L. Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (public 2014-12-22), https://arxiv.org/abs/1412.7209.
4. L. Razzoli, M. G. A. Paris, P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794v1 (public 2020-11-27), https://arxiv.org/abs/2011.13794.
