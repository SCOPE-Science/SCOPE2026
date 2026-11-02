# Arithmetic return resonances and product-mixing equality on prism graphs

## Finding
For each integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the unweighted circular ladder (prism), with one quantum excitation at a vertex \(v\). Let \(A_n\) be its adjacency matrix, let \(U_n(t)=\exp(-itA_n)\), and define the Cesàro return probability
\[
R_n=\lim_{T\to\infty}\frac1T\int_0^T|\langle v,U_n(t)v\rangle|^2\,dt.
\]
The limit exists, is independent of \(v\), and equals
\[
\boxed{R_n=\frac1n-\frac{1+\mathbf 1_{\{2\mid n\}}}{2n^2}+\frac{2}{n^2}\big(\mathbf 1_{\{4\mid n\}}+\mathbf 1_{\{6\mid n\}}\big).}
\]
Here \(\mathbf 1_{\{d\mid n\}}\) denotes the indicator that \(d\) divides \(n\). Thus each divisibility resonance contributes exactly \(2/n^2\) to return. For example, \(R_4=5/16\), \(R_6=7/36\), and \(R_{12}=5/48\).

More structurally, let \(\widehat M(G)\) denote the average mixing matrix for the adjacency continuous-time quantum walk on \(G\). The known Cartesian-product inequality
\[
\widehat M(C_n\square K_2)\succeq\widehat M(C_n)\otimes\widehat M(K_2)
\]
is an **equality of matrices if and only if** \(4\nmid n\) and \(6\nmid n\). It is strict (the difference is nonzero positive semidefinite) otherwise. The exact diagonal excess is \(2(\mathbf 1_{\{4\mid n\}}+\mathbf 1_{\{6\mid n\}})/n^2\).

## Assumptions and scope
The graph is the simple Cartesian product with unit hopping along every edge; \(n\ge3\). The walk is coherent and continuous time, with one vertex-localized initial pure state, no measurement or decoherence during evolution, and \(\hbar=1\). The average is a continuous-time Cesàro limit; it is not an instantaneous return, a randomly refreshed graph, or convergence of the quantum state. The formula is invariant under a global change of sign of the Hamiltonian or addition of a scalar multiple of the identity. The matrix inequality uses the positive-semidefinite Loewner order.

## Proof
**1. Spectral return identity.** For any finite graph with adjacency spectral projectors \(E_\lambda\), the amplitude \(\langle v,U(t)v\rangle\) equals \(\sum_\lambda e^{-it\lambda}(E_\lambda)_{vv}\). Averaging its absolute square removes all terms with unequal eigenvalues. Hence
\[
R(v)=\sum_\lambda ((E_\lambda)_{vv})^2.
\]
The prism is vertex-transitive, so each diagonal entry of the projector of multiplicity \(m_\lambda\) equals \(m_\lambda/(2n)\). Therefore \(R_n=(4n^2)^{-1}\sum_\lambda m_\lambda^2\).

**2. Two spectral branches.** The Fourier eigenvalues of \(C_n\) are \(c_k=2\cos(2\pi k/n)\), \(0\le k<n\). The spectrum of the prism consists of \(c_k+1\) and \(c_k-1\). Within either branch, \(c_k=c_\ell\) if and only if \(k\equiv\pm\ell\pmod n\). Each branch consequently contributes \(2n-1\) to the sum of squared multiplicities when \(n\) is odd, and \(2n-2\) when \(n\) is even. Doubling gives the uncoupled baseline \(4n-2-2\mathbf1_{\{2\mid n\}}\).

**3. Exhaustive cross-branch resonance lemma.** Suppose two branch eigenvalues coincide, so for two \(n\)-th roots of unity \(z,w\) one has
\[
(z+z^{-1})-(w+w^{-1})=2.
\]
Put \(a=z+z^{-1}\) and \(b=w+w^{-1}\). Under every embedding of the cyclotomic splitting field into \(\mathbb C\), both conjugates are real in \([-2,2]\), and \(a'=b'+2\); hence \(a'\ge0\). Let \(m\) be the order of \(z\). If \(m>2\) and \(a\ne0\), all conjugates of the algebraic integer \(a\) over \(\mathbb Q\) are strictly positive. Their norm is a nonzero integer, so their geometric mean is at least \(1\), and their trace is at least their degree \(d=\varphi(m)/2\). But the trace of \(z+z^{-1}\) in the maximal real cyclotomic subfield is \(\mu(m)\), whose value is at most \(1\). Thus \(d=1\). This restricts \(m\) to \(3,4,6\); nonnegative possibilities yield only \(a=0\) for \(m=4\), or \(a=1\) for \(m=6\). For \(m=1,2\), the nonnegative possibility is \(a=2\) for \(m=1\). Because \(b=a-2\), the only pairs are
\[
(a,b)\in\{(2,0),(1,-1),(0,-2)\}.
\]
All occur precisely when the orders required by them divide \(n\): the first and last require \(4\mid n\), and the middle requires \(6\mid n\). There are no other cross-branch collisions. (Here \(\varphi\) is Euler's totient and \(\mu\) is the Möbius function.)

**4. Multiplicity increments and matrix equality.** When \(4\mid n\), the collisions at distinct eigenvalues \(+1\) and \(-1\) each merge branch multiplicities \(1\) and \(2\). Each contributes \((1+2)^2-1^2-2^2=4\) to the squared-multiplicity sum, for a total \(8\). When \(6\mid n\), a collision at eigenvalue \(0\) merges multiplicities \(2\) and \(2\), contributing \((2+2)^2-2^2-2^2=8\). These three eigenvalues are distinct even when \(12\mid n\), so contributions add. The preceding baseline plus the increments yields the boxed return formula.

Without cross-branch collisions, each prism spectral projector is a tensor product \(E_j\otimes F_s\), where \(E_j\) and \(F_s\) are spectral projectors of \(C_n\) and \(K_2\). Therefore \(\widehat M(G_n)=\sum_{j,s}(E_j\otimes F_s)^{\circ2}=\widehat M(C_n)\otimes\widehat M(K_2)\). With collisions, the prism projectors merge distinct tensor projectors. If two mutually orthogonal real spectral projectors \(P,Q\) merge, their Schur-square contribution changes by \(2(P\circ Q)\), a positive-semidefinite matrix by the Schur product theorem. Applying this to each disjoint collision gives the product-mixing positive-semidefinite inequality directly, and the strictly positive diagonal excess calculated above proves the two matrices unequal. This establishes the exact equality criterion.

## Verification
Run `python prism_checker.py` with NumPy installed. The checker independently constructs the adjacency matrix of \(C_n\square K_2\) for \(3\le n\le50\), diagonally decomposes it, and compares the resulting squared-multiplicity return to the exact formula. It separately checks the analytic two-branch spectral enumeration for \(3\le n\le600\). These finite checks are diagnostics only: the all-\(n\) collision classification and return identity are proved above.

## Relationship to prior work
Godsil (2011, arXiv:1103.2578) establishes the spectral-projector formula for average mixing and evaluates paths and cycles, not the entire circular-ladder family. Coutinho, Godsil, Guo, and Zhan (2017, arXiv:1709.03591) provide the commutant formulation. Godsil, Guo, and Sobchuk (2019, arXiv:1910.02039, Lemma 4.2) establish the general Cartesian-product positive-semidefinite inequality, but do not identify which prism sizes attain equality or evaluate the arithmetic resonance excess. The result here supplies precisely that missing family-wide cyclotomic comparison; the general average-mixing formula and product inequality are prior results, not new claims.

## Limitations
The result is confined to unweighted, undirected prisms and adjacency quantum walks. Unequal rung and rail hopping would change the branch separation and hence the resonance arithmetic. No relaxation rate, temporal sampling error bound, or average mixing matrix entries other than the diagonal excess are computed. The historical-priority assessment is based on searched and inspected sources, not an exhaustive proof that no equivalent formula has appeared elsewhere.

## References
1. C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578, first publicly posted 2011-03-14, https://arxiv.org/abs/1103.2578.
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591, first publicly posted 2017-09-11, https://arxiv.org/abs/1709.03591.
3. C. Godsil, K. Guo, M. Sobchuk, *Diagonal entries of the average mixing matrix*, arXiv:1910.02039, first publicly posted 2019-10-04, https://arxiv.org/abs/1910.02039.
