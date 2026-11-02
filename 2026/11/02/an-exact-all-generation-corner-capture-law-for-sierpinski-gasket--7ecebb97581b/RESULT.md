# An exact all-generation corner-capture law for Sierpinski-gasket quantum transport

## Finding

Let \(G_m\) be the finite level-\(m\) Sierpinski-gasket graph, starting with a triangle at \(m=0\), and let \(B_m\) be the three-column matrix of its outer-corner vertex vectors. Its number of vertices is \(N_m=(3^{m+1}+3)/2\). For the adjacency matrix \(A_m\), define the corner-generated invariant subspace
\[
\mathcal K_m=\operatorname{span}\{A_m^k B_m u:k\ge0,\ u\in\mathbb C^3\}.
\]
Then, for every integer \(m\ge0\),
\[
\dim\mathcal K_m=\begin{cases}3,&m=0,\\5\cdot 2^{m-1}+1,&m\ge1.\end{cases}
\]
Consequently, if a single excitation evolves coherently under \(H=J A_m+B_m V B_m^*\) with real \(J\ne0\) and any Hermitian \(3\times3\) matrix \(V\), while each corner has an arbitrary strictly positive Markovian absorption rate, an initially maximally mixed state is eventually captured with probability
\[
P_m=\frac{\dim\mathcal K_m}{N_m}.
\]
In particular, \(P_m\sim\frac53(\frac23)^m\) as \(m\to\infty\). The exact dark-space dimension is \(N_m-\dim\mathcal K_m\). This classification includes arbitrary corner onsite detunings and the combinatorial-Laplacian Hamiltonian.

## Assumptions and scope

Construct \(G_0\) as the undirected three-cycle. Each level replaces every elementary triangle by three half-size corner triangles, identifying shared vertices and retaining their perimeter bonds. Thus the three outer corners have degree two, all other vertices degree four, and every old edge belongs to exactly one elementary triangle. There are \(3^{m+1}\) bonds and \((3^{m+1}+3)/2\) vertices.

The hopping is uniform, real, and nonzero on each edge. The matrix \(V=V^*\) acts only within the three-dimensional corner subspace. The effective no-jump Hamiltonian is \(H_{\mathrm{eff}}=H-\frac{i}{2}B_m\Gamma B_m^*\), where \(\Gamma=\operatorname{diag}(\kappa_1,\kappa_2,\kappa_3)\) and every \(\kappa_j>0\). We define eventual capture by total lost no-jump norm, averaged over the maximally mixed initial state \(I/N_m\). No infinite graph or finite-time absorption-rate assertion is made.

## Proof

**1. Boundary Weyl matrix.** Put \(G_m(z)=B_m^*(zI-A_m)^{-1}B_m\) and \(K_m(z)=G_m(z)^{-1}\), regarded as matrices of rational functions in \(z\). Permutation symmetry of the three corners gives the decomposition
\[
K_m(z)=s_m(z)P_{\mathrm{sym}}+t_m(z)P_{\mathrm{std}},\qquad P_{\mathrm{sym}}=\tfrac13\mathbf1\mathbf1^*,\quad P_{\mathrm{std}}=I-P_{\mathrm{sym}}.
\]
At level zero, \(s_0(z)=z-2\) and \(t_0(z)=z+1\).

**2. Exact spectral decimation.** In a subdivided old elementary triangle with old vertex values \(f_a,f_b,f_c\), the newly inserted midpoint values at spectral parameter \(z\) solve a matrix equation with coefficient matrix \((z+1)I-\mathbf1\mathbf1^*\). With \(Q(z)=(z+1)(z-2)\), the solution at the midpoint of \(ab\) is
\[
f_{ab}=\frac{z(f_a+f_b)+2f_c}{Q(z)}.
\]
Inserting these midpoint values into the spectral equations at old vertices, and using that each interior old vertex belongs to two elementary triangles but each corner belongs to one, yields the following exact Schur complement on all old vertices:
\[
\frac{z+2}{Q(z)}\bigl(R(z)I-A_m\bigr)+\frac{2z}{Q(z)}B_mB_m^*,\qquad R(z)=z(z-3).
\]
Taking a second Schur complement onto the three old corners proves the rational identity
\[
K_{m+1}(z)=\frac{z+2}{Q(z)}K_m(R(z))+\frac{2z}{Q(z)}I_3.
\]
Although derived away from \(z=-1,2\) and from intermediate resolvent poles, it extends uniquely as an identity of rational matrices. In particular each scalar sector \(k_m\in\{s_m,t_m\}\) obeys
\[
k_{m+1}(z)=\frac{(z+2)k_m(R(z))+2z}{(z+1)(z-2)}.
\]

**3. Exact degree count, including cancellations.** Write \(s_m=S_m/U_m\) and \(t_m=T_m/W_m\) as reduced monic rational functions with integer polynomial numerators and denominators. The special evaluations are
\[
s_m(4)=2,\qquad t_m(4)=2+3(3/5)^m,\qquad t_m(-2)=-1,\qquad s_m(-2)=-1\quad(m\ge1),
\]
with \(s_0(-2)=-4\). They follow directly by substituting \(z=4,-2\) in the recursion (at \(z=-2\), the term involving the previous level vanishes). Because \(R(-1)=4\) and \(R(2)=-2\), the raw numerator and denominator in the next recursion share exactly the factor \(z-2\) for every standard sector step, exactly \(z+1\) in the first symmetric step, and exactly \((z+1)(z-2)\) in every subsequent symmetric step.

Here is why there are *no hidden additional cancellations*. If an old reduced denominator vanishes at \(R(z)\), the raw new numerator equals \((z+2)\) times the old, nonvanishing numerator; this can vanish simultaneously only at \(z=-2\). But \(R(-2)=10\), and every old reduced denominator is nonzero at \(10\). Likewise the old denominators are nonzero at \(4\) and \(-2\), so the exceptional factors at \(-1\) and \(2\) occur only to first order. Indeed the recurrences establish explicitly
\[
U_m(z)=R^{\circ(m-1)}(z)-2\quad(m\ge1),\qquad W_m(z)=\prod_{j=0}^{m-1}\bigl(R^{\circ j}(z)+1\bigr),
\]
with \(U_0=W_0=1\); direct substitution shows all these evaluations are nonzero at \(4,-2,10\). Thus all claimed reduced pairs remain coprime inductively. Every \(k_m\) behaves as \(z+O(1)\) at infinity, so the numerator has degree one larger than the denominator.

The standard numerator degrees therefore satisfy \(b_0=1\), \(b_{m+1}=2b_m\), giving \(b_m=2^m\). For the symmetric numerator, \(a_0=1\), \(a_1=2\), and \(a_{m+1}=2a_m-1\) for \(m\ge1\), giving \(a_m=2^{m-1}+1\) for \(m\ge1\).

**4. Spectral rank and absorption.** By the spectral theorem for the finite real-symmetric matrix \(A_m\), every pole of the scalar Green functions \(1/s_m\) and \(1/t_m\) is a real simple pole with positive spectral weight. Since the rational expressions are reduced, their pole counts are respectively \(a_m\) and \(b_m\). At each energy, the boundary spectral-measure matrix has a one-dimensional symmetric block and a two-dimensional standard block. The rank of its residue equals the number of independent boundary-generated eigenvectors at that energy. Summing those ranks, *even if sector eigenvalues coincide*, gives
\[
\dim\mathcal K_m=a_m+2b_m.
\]
This is \(3\) at \(m=0\) and \(5\cdot 2^{m-1}+1\) otherwise.

The subspace \(\mathcal K_m\) is unchanged by scaling \(A_m\) by \(J\ne0\) or adding \(B_m V B_m^*\): the least invariant subspace containing the corner vectors for one Hamiltonian is also invariant for the other, in both directions. The orthogonal complement consists precisely of eigenmodes of the Hermitian Hamiltonian with zero overlap at all absorbers and is perfectly dark. Conversely, an eigenvector of \(H_{\mathrm{eff}}\) with nondecaying eigenvalue must have zero corner population, because the negative imaginary part of its Rayleigh quotient is \(-\tfrac12\sum_j\kappa_j|\langle c_j,\psi\rangle|^2\). In finite dimension, all modes outside the dark invariant subspace consequently decay, including any nonnormal Jordan contributions. Hence the maximally mixed capture probability is the accessible dimension divided by \(N_m\).

Finally, \(5\cdot2^{m-1}+1\sim(5/2)2^m\), while \(N_m\sim(3/2)3^m\), which yields the stated exact exponential scale.

## Verification

The standalone `check_sierpinski.py` builds the actual finite graphs independently of the boundary-decimation proof and computes the three-corner block-Krylov ranks by modular Gaussian elimination at two distinct primes. It checks every level \(0\le m\le5\), with vertex counts \(3,6,15,42,123,366\) and ranks \(3,6,11,21,41,81\). It also checks the boundary resolvent recurrence by exact rational inversion of the direct adjacency matrices at levels zero, one, and two, at spectral parameter \(z=10\). The script reports that all tests pass. These finite computations are cross-checks; the unlimited-generation statement follows from the rational recurrence and the coprimality proof above.

## Relationship to prior work

Darázs, Anishchenko, Kiss, Blumen and Mülken (2014, arXiv:1405.5078) studied the same three outer-corner traps on finite Sierpinski gaskets using the graph-Laplacian Hamiltonian, and numerically tabulated dark-mode counts through the graph with \(366\) sites. Under their generation convention, these counts are \(0,4,21,82,285\), corresponding exactly to the finite cases of the formula here. Those finite counts and the observation of poor quantum transport are prior results, not discoveries claimed here. The present contribution is the all-generation closed form, the boundary-resolvent proof, the exact exponential capture fraction and the stated rate/corner-perturbation invariance. In fact, the earlier Laplacian Hamiltonian is \(4I-A_m-2B_mB_m^*\), so its corner-accessible subspace coincides with the adjacency one.

Novo, Chakraborty, Mohseni, Neven and Omar (2014/2015, arXiv:1412.7209) explain the general Krylov-subspace method for quantum transport, including applications to other graphs. The general method is acknowledged; it does not supply the specific Sierpinski three-corner dimension formula in the examined text. Classical random-walk absorption on Sierpinski gaskets and general fractal-Laplacian spectral-decimation research answer other questions or provide broader techniques, but are not presented as new here.

## Limitations

This is an idealized finite, coherent, homogeneous-edge, single-excitation model. The result concerns eventual capture from the maximally mixed state and not mean capture time, arbitrary initial-state capture probability, disorder in internal edges, dephasing, interactions, or an infinite-graph dynamical limit. Three positive-rate outer-corner absorbers are required; the all-generation one- or two-corner formula is not established here. Historical priority remains provisional: general spectral-decimation literature may yield equivalent representations, and independent expert verification has not been performed.

## References

- Z. Darázs, A. Anishchenko, T. Kiss, A. Blumen and O. Mülken, “Transport properties of continuous-time quantum walks on Sierpinski fractals,” arXiv:1405.5078, first posted 2014-05-20; *Physical Review E* **90**, 032113 (2014), https://arxiv.org/abs/1405.5078.
- L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, “Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs,” arXiv:1412.7209, first posted 2014-12-22, https://arxiv.org/abs/1412.7209.
- H. Qiu, “Exact spectrum of the Laplacian on a domain in the Sierpinski gasket,” arXiv:1206.1381, first posted 2012-06-07, https://arxiv.org/abs/1206.1381 (different fractal domain and boundary problem).
