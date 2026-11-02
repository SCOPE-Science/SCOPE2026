# Sharp path–cycle size cutoffs for unconditional fourth-order Padé positivity

## Finding

Let \(G\) be the undirected simple path \(P_n\), \(n\ge2\), or simple cycle \(C_n\), \(n\ge3\), where each edge has the **same** positive conductance \(c\). Define the fourth-order two-stage Gauss–Legendre / \([2/2]\) Padé one-step matrix
\[
M_G(h)=\left(I+\frac h2L+\frac{h^2}{12}L^2\right)^{-1}
\left(I-\frac h2L+\frac{h^2}{12}L^2\right),\qquad h\ge0,
\]
where \(L\) is the weighted graph Laplacian. Then the following sharp classification holds:
\[
\boxed{M_{P_n}(h)\ge0\text{ entrywise for all }h\ge0\iff 2\le n\le3,}
\]
\[
\boxed{M_{C_n}(h)\ge0\text{ entrywise for all }h\ge0\iff 3\le n\le5.}
\]
For every finite step, regardless of graph size, the matrix is symmetric, has row sums one and is positive definite. For every excluded graph size, however, an adjacent matrix entry becomes negative at every sufficiently large step. Thus spectral stability and stochastic positivity separate at different sharp size cutoffs for path and periodic geometries.

More explicitly, for the adjacent endpoint pair \((0,1)\) on a path,
\[
M_{P_n}(h)_{0,1}= -\frac{2(n-1)(2n-7)}{nch}+O_{n,c}(h^{-2})\quad(n\ge4),
\]
and for an adjacent pair \((0,1)\) on a cycle,
\[
M_{C_n}(h)_{0,1}= -\frac{(n-1)(n-5)}{nch}+O_{n,c}(h^{-2})\quad(n\ge6).
\]
At the five-cycle boundary, \(t=ch\) and
\[
D(t)=25t^4+150t^3+360t^2+360t+144
\]
give the **exact** entries, distinguished by cyclic distance:
\[
M_{C_5}(h)_{00}=\frac{25t^4+30t^3+72t^2+72t+144}{D(t)},
\]
\[
M_{C_5}(h)_{01}=\frac{72t(t+2)}{D(t)},\qquad
M_{C_5}(h)_{02}=\frac{12t^2(5t+6)}{D(t)}.
\]
All these entries are strictly positive for \(h>0\), and the adjacent entry is \(72/[25(ch)^2]+O(h^{-3})\) as \(h\to\infty\). At \(h=0\), \(M_G(0)=I\).

## Assumptions and scope

The graph is finite, connected, undirected and simple. On paths, vertices are labeled \(0,\ldots,n-1\) in path order; on cycles, labels are taken modulo \(n\). Every edge conductance equals the same fixed \(c>0\), so \(L_{ii}\) is the weighted degree and \(L_{ij}=-c\) for adjacent distinct vertices. Matrix inequalities such as \(M\ge0\) mean **entrywise** inequalities, not positive semidefiniteness. The timestep \(h\) ranges over all finite real values \(h\ge0\). There are no graph-size assumptions beyond the ranges in the theorem. Neither heterogeneous edge conductances nor nonconservative boundary generators are included.

## Proof

**1. Spectral structure and large-step obstruction.** Put
\[
r(z)=\frac{12-6z+z^2}{12+6z+z^2},\qquad Q(z)=z^2+6z+12.
\]
The denominator is positive for \(z\ge0\), while \(12-6z+z^2=(z-3)^2+3>0\). Moreover \(1-r(z)=12z/Q(z)\). Therefore \(0<r(z)\le1\) for all \(z\ge0\), with \(r(0)=1\). Because \(L\) is symmetric positive semidefinite and \(L\mathbf1=0\), the given matrix is \(r(hL)\), is positive definite at every finite step, and satisfies \(M_G(h)\mathbf1=\mathbf1\). Its off-diagonal signs are the only issue.

For each positive eigenvalue \(\lambda\) of \(L\),
\[
r(h\lambda)=1-\frac{12}{h\lambda}+O_{\lambda}(h^{-2}).
\]
Since the zero-eigenvalue projector contributes exactly the identity on its eigenspace, the spectral theorem gives, for fixed connected \(G\),
\[
M_G(h)=I-\frac{12}{h}L^{\dagger}+O_G(h^{-2}),
\]
where \(L^{\dagger}\) is the Moore–Penrose pseudoinverse. The remainder is entrywise bounded for fixed graph and fixed conductance. Thus any strictly positive off-diagonal entry of \(L^{\dagger}\) forces negativity of the corresponding Padé entry for every sufficiently large finite \(h\).

For any connected undirected conductance network, write \(R\) for its matrix of effective resistances and \(H=I-\mathbf1\mathbf1^{\mathsf T}/n\). The standard resistance-centering identity is
\[
L^{\dagger}=-\tfrac12 HRH,
\quad
(L^{\dagger})_{ij}=-\tfrac12(R_{ij}-\bar R_i-\bar R_j+\bar R),
\]
where \(\bar R_i=n^{-1}\sum_j R_{ij}\) and \(\bar R=n^{-2}\sum_{i,j}R_{ij}\). This identity follows directly by double-centering \(R_{ij}=(L^{\dagger})_{ii}+(L^{\dagger})_{jj}-2(L^{\dagger})_{ij}\), using \(L^{\dagger}\mathbf1=0\).

On a path, \(R_{ij}=|i-j|/c\). For the endpoint and its neighbor,
\[
\bar R_0=\frac{n-1}{2c},\qquad
\bar R_1=\frac{n^2-3n+4}{2nc},\qquad
\bar R=\frac{n^2-1}{3nc}.
\]
Hence
\[
(L^{\dagger}_{P_n})_{0,1}=\frac{(n-1)(2n-7)}{6nc},
\]
which is strictly positive for every integer \(n\ge4\). The asserted path asymptotic and eventual negative entry follow from the spectral expansion above.

On a cycle, if \(d\in\{0,\ldots,n-1\}\) is the cyclic label separation, the parallel-resistor formula gives \(R_{0d}=d(n-d)/(nc)\). Every resistance-row mean and the global mean equal \((n^2-1)/(6nc)\). Thus
\[
(L^{\dagger}_{C_n})_{0,1}
=-\frac12\left(\frac{n-1}{nc}-\frac{n^2-1}{6nc}\right)
=\frac{(n-1)(n-5)}{12nc},
\]
which is positive for every integer \(n\ge6\). This gives the asserted cycle asymptotic and eventual negative entry. These are infinite-family deductions, not extrapolations from finite tests.

**2. Safe small paths and cycles.** We use a direct spectral lemma. Consider an unweighted complete multipartite graph with part sizes \(s_1,\ldots,s_k\), \(k\ge2\), order \(N\), and common cross-part conductance \(c\). The orthogonal spectral decomposition consists of the constant space (eigenvalue zero), part-constant vectors orthogonal to constants (eigenvalue \(Nc\)), and zero-sum vectors within part \(i\) (eigenvalue \((N-s_i)c\)). For \(t=ch>0\), the Padé matrix has, at distinct vertices \(u,v\) in different parts,
\[
M_{uv}=\frac{1-r(Nt)}N=\frac{12t}{Q(Nt)}>0.
\]
At distinct vertices \(u,v\) in the same part of size \(s\ge2\), put \(k=N-s\). The same projection calculation gives
\[
M_{uv}=\frac{1-r(Nt)}N+\frac{r(Nt)-r(kt)}s
=\frac{12kt}{s}\left(\frac1{Q(kt)}-\frac1{Q(Nt)}\right)>0,
\]
because \(0<k<N\) and \(Q\) increases strictly on positive arguments. Diagonal entries are positive by the positive-definiteness argument above. Thus **every** such complete multipartite graph has a strictly positive Padé transition matrix for every \(h>0\). In particular, \(P_2=K_{1,1}\), \(P_3=K_{1,2}\), \(C_3=K_{1,1,1}\), and \(C_4=K_{2,2}\) are safe for every step.

**3. The five-cycle boundary.** Directly multiplying the matrices \(12I\pm6tL_0+t^2L_0^2\), where \(L_0\) is the unit-conductance five-cycle Laplacian, or equivalently applying its three Fourier eigenspaces, gives exactly the three rational expressions in the Finding section. The denominator \(D(t)\) has strictly positive coefficients, and all three numerators are positive for \(t>0\). Cyclic symmetry accounts for every matrix entry. Therefore \(C_5\) is safe for every step. For \(t\to\infty\), the adjacent numerator has degree two and the denominator degree four, giving the stated positive critical \(t^{-2}\) tail.

Combining Steps 1–3 proves the classification with equality boundaries \(n=3\) and \(n=5\), including \(h=0\). \(\square\)

## Verification

The standalone file `verify.py` uses Python 3 standard-library `fractions.Fraction` and exact rational Gaussian elimination. It reproduces the \(C_5\) closed kernel, checks the resistance-centered pseudoinverse formulas, and compares direct fourth-order Padé matrices on selected paths, cycles and complete multipartite graphs. Running `python3 verify.py` produced:

`VERIFY_OK {'exact_matrix_instances': 114, 'pseudoinverse_identities': 17, 'c5_kernel_identities': 15, 'multipartite_checks': 21}`

The finite checks support reproducibility; the proof above is what establishes all integer graph sizes and all real timesteps. A matrix being positive definite does **not** imply that its entries are nonnegative.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2010) provide foundational sufficient conditions and counterexamples for positivity under diagonal Padé discretizations of positive systems; their complete conference preprint was examined. Their 2012 extended author preprint develops general positivity and stability conditions and contains nonpositive examples, including an eight-state nilpotent construction; it was examined in full-text sections relevant to positivity. Neither text states the sharp path-versus-cycle size cutoffs, the five-cycle rational kernel, or the adjacent pseudoinverse asymptotics above. The 2015 finite-element heat-equation positivity literature concerns different spatial discretizations and does not supply these fixed-graph all-step classifications. The general spectral decomposition, resistor formulas, and Padé rational function are standard inputs, not claimed as new.

## Limitations

The classification is for homogeneous conductances and the exact \([2/2]\) Padé / two-stage Gauss–Legendre *end-step*, not its internal Runge–Kutta stages. It does not determine the largest **finite** admissible timestep in the graph-size regimes that eventually fail, nor claim that the set of admissible timesteps is connected. It is not a characterization of arbitrary graph families, arbitrary positive weights, other Padé orders or nonconservative boundary conditions. The large-step conclusions are asymptotic with fixed graph size, not a joint uniform limit. Specialized earlier publications might contain an equivalent statement despite the reported comparisons. Independent validation has not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the Preservation of Co-positive Lyapunov Functions under Padé Discretization for Positive Systems*, MTNS 2010. Open repository record and full-text preprint: https://mural.maynoothuniversity.ie/id/eprint/2195/ (repository deposit 2010-10-15).
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications **436** (2012), 3425–3442; DOI: 10.1016/j.laa.2011.12.021. Author-hosted full text: https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf .
3. P. Chatzipantelidis, Z. Horváth and V. Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, Computational Methods in Applied Mathematics **15** (2015), 417–437; DOI: 10.1515/cmam-2015-0018; bibliographic record https://research.chalmers.se/en/publication/224734 .
