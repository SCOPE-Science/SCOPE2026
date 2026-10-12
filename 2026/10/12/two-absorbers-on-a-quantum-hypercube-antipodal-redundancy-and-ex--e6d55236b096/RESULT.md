# Two absorbers on a quantum hypercube: antipodal redundancy and exact survival

## Finding
Let \(d\ge2\), and place two strictly positive continuous absorbers at distinct vertices of the binary \(d\)-cube. For uniform nearest-neighbor coherent hopping, the space of initial quantum amplitudes that can eventually be absorbed has dimension
\[
\dim \mathcal B=\begin{cases}d+1,&\text{absorbers antipodal},\\2d,&\text{otherwise}.
\end{cases}
\]
Thus the second absorber is *spectrally redundant* precisely at antipodal placement, whereas every other placement enlarges the absorbing space by exactly \(d-1\) dimensions. For the uniform incoherent mixture of all \(2^d\) initial sites, the total absorption probability is \((d+1)/2^d\) or \(2d/2^d\), respectively. All these values are independent of the positive absorption rates.

There is also a complete sitewise law. In nonantipodal placement, exactly the two traps and their two bitwise complements have unit total absorption. Every other localized preparation has strictly positive residual survival. If the traps are antipodal, precisely those two trap vertices have unit total absorption.

## Assumptions and scope
Identify the vertices with \(V=\{0,1\}^d\), with the group operation \(\oplus\), bitwise complement \(\bar x=x\oplus\mathbf1\), and Hamming weight \(|x|\). By cube translation and permutation symmetry, put the absorbing vertices at \(0\) and \(u\), where \(r=|u|\in\{1,\ldots,d\}\). On the Hilbert space \(\mathbb C^{2^d}\), use the adjacency Hamiltonian \(H=\sum_{j=1}^d X_j\), where \(X_j\) flips the \(j\)-th bit. Let
\[
K=H-i\gamma_0|0\rangle\langle0|-i\gamma_u|u\rangle\langle u|,\qquad \gamma_0,\gamma_u>0.
\]
The unconditional (unnormalized) wavefunction from vertex \(x\) is \(e^{-itK}|x\rangle\), and its squared norm is the probability that no absorption has occurred by time \(t\). Define \(s(x)=\lim_{t\to\infty}\|e^{-itK}|x\rangle\|^2\). No statement is made about conditional postselection, discrete-time coined walks, arbitrary disorder, or finite observation times.

Define the binary Krawtchouk sums, including the convention \(\binom ab=0\) when \(b\notin\{0,\ldots,a\}\), by
\[
C_k=\binom dk,\qquad K_k(a)=\sum_{j=0}^{k}(-1)^j\binom aj\binom{d-a}{k-j},\qquad 0\le k,a\le d.
\]
For antipodal separation \(r=d\), the exact survival probability is
\[
s(x)=1-\frac1{\binom d{|x|}}.
\]
For every nonantipodal separation \(1\le r<d\), with \(h=|x|\) and \(\ell=|x\oplus u|\), it is
\[
s(x)=1-\frac1{2^d}\left[2+\sum_{k=1}^{d-1}\frac{C_k\bigl(K_k(h)^2+K_k(\ell)^2\bigr)-2K_k(r)K_k(h)K_k(\ell)}{C_k^2-K_k(r)^2}\right].
\]
Every denominator in this finite expression is strictly positive under the displayed assumptions.

## Proof
**1. Dissipative survival is an orthogonal spectral projection.** Let \(E_k=\ker(H-(d-2k)I)\) be the distinct eigenspaces of \(H\). Put
\[
\mathcal D=\bigoplus_{k=0}^d\{v\in E_k:\langle0|v\rangle=\langle u|v\rangle=0\},\qquad \mathcal B=\mathcal D^\perp.
\]
The space \(\mathcal D\) reduces \(H\); since both absorber vectors belong to \(\mathcal B\), the two rank-one loss projections reduce the same decomposition. On \(\mathcal D\), \(K=H\) is self-adjoint. On \(\mathcal B\), an eigenvector of \(K\) with a real eigenvalue would satisfy
\[
0=-\operatorname{Im}\langle v,Kv\rangle=\gamma_0|\langle0|v\rangle|^2+\gamma_u|\langle u|v\rangle|^2,
\]
so it would be an eigenvector of \(H\) in \(\mathcal D\), a contradiction. For every eigenvalue of this finite dissipative restriction, the imaginary part is therefore strictly negative. Its exponential tends to zero, even in the presence of nontrivial Jordan blocks. Orthogonality of the invariant decomposition yields
\[
s(x)=\|P_{\mathcal D}|x\rangle\|^2=1-\|P_{\mathcal B}|x\rangle\|^2.
\]
This proves existence of the limit and independence from the strictly positive rate magnitudes.

**2. Projected trap vectors and the rank dichotomy.** The Walsh vectors \(\chi_T=2^{-d/2}\sum_{x\in V}(-1)^{|T\cap x|}|x\rangle\), where \(T\subseteq\{1,\ldots,d\}\), form an orthonormal basis and satisfy \(H\chi_T=(d-2|T|)\chi_T\). Let \(P_k\) project onto \(E_k\), and set \(a_k=P_k|0\rangle\), \(b_k=P_k|u\rangle\). Direct summation over all \(k\)-subsets gives
\[
\begin{pmatrix}\langle a_k,a_k\rangle&\langle a_k,b_k\rangle\\\langle b_k,a_k\rangle&\langle b_k,b_k\rangle\end{pmatrix}
=2^{-d}\begin{pmatrix}C_k&K_k(r)\\K_k(r)&C_k\end{pmatrix}.
\]
The absorbing subspace is the orthogonal direct sum \(\mathcal B=\bigoplus_k\operatorname{span}\{a_k,b_k\}\). For \(k=0,d\), the span has dimension one. If \(r=d\), every Walsh character of weight \(k\) has value \((-1)^k\) at \(u\), so \(b_k=(-1)^ka_k\); consequently \(\dim\mathcal B=d+1\).

If \(1\le r<d\) and \(1\le k\le d-1\), choose a \(k\)-subset containing a coordinate in the support of \(u\) but excluding one outside the support. Replacing the included coordinate by the excluded coordinate reverses \((-1)^{|T\cap u|}\), without changing \(k\). Thus both signs occur and \(|K_k(r)|<C_k\). The displayed Gram matrix is positive definite and each of these \(d-1\) spans has dimension two. Hence \(\dim\mathcal B=2+2(d-1)=2d\). Averaging \(s(x)\) over the complete computational basis gives \(1-\dim\mathcal B/2^d\).

**3. Exact sitewise expression.** In an interior \(k\)-eigenspace for \(r<d\), the inner products of \(P_k|x\rangle\) against \(a_k,b_k\) form \(2^{-d}(K_k(h),K_k(\ell))\). The squared norm of its projection onto their span is the quadratic form with the inverse of their nonsingular \(2\times2\) Gram matrix. This equals
\[
\frac{C_k\{K_k(h)^2+K_k(\ell)^2\}-2K_k(r)K_k(h)K_k(\ell)}{2^d\{C_k^2-K_k(r)^2\}}.
\]
The two one-dimensional endpoint eigenspaces contribute \(2/2^d\). Summing gives the nonantipodal formula. For \(r=d\), the span of projected traps in every eigenspace is identical to the span of the projection of \(|0\rangle\) alone. Equivalently, the full bright space is the span of normalized uniform Hamming-shell states \(\binom dh^{-1/2}\sum_{|x|=h}|x\rangle\); therefore a vertex of weight \(h\) has bright projection squared norm \(1/\binom dh\), proving the antipodal formula.

**4. Exactly which localized starts are completely absorbed.** For nonantipodal \(r\), if \(s(x)=0\), then in particular \(P_1|x\rangle\in\operatorname{span}\{P_1|0\rangle,P_1|u\rangle\). The degree-one Walsh coefficients of \(P_1|x\rangle\) are the sign vector \(((-1)^{x_j})_{j=1}^d\). This belongs to the span of the all-ones sign vector and \(((-1)^{u_j})_j\) only when it is constant on the support of \(u\) and constant on its nonempty complement. Being a sign vector, this forces \(x\in\{0,u,\bar0,\bar u\}\). Conversely, both trap vertices lie in \(\mathcal B\), and \(P_k|\bar y\rangle=(-1)^kP_k|y\rangle\) for every \(k\), so their bitwise complements also lie in \(\mathcal B\). This proves necessity and sufficiency, including \(d=2\). In the antipodal case, \(1-1/\binom d{|x|}=0\) precisely for \(|x|=0,d\), completing the classification.

## Verification
The accompanying standalone checker evaluates the Krawtchouk formula using exact rational arithmetic and independently reconstructs the same probability by projecting Walsh-sign vectors in every eigenspace. It checks all \(640\) localized preparations for every pair separation in dimensions \(2\) through \(6\), along with the predicted total bright rank and every zero-survival site. Five additional non-Hermitian matrix exponentials with positive unequal absorber strengths reproduce the asymptotic norm formula with maximum absolute discrepancy approximately \(1.26\times10^{-13}\) for the specified test cases. The exact proof above, rather than those finite checks, establishes the statement for all \(d\ge2\).

Run `python artifacts/verify.py` with Python 3.10 or newer for the exact checks. Installing the optional dependencies in `artifacts/requirements.txt` also enables the finite-time matrix exponential comparisons.

## Relationship to prior work
Moore and Russell introduced spectral analysis of continuous-time quantum walks on the hypercube (arXiv:quant-ph/0104137). Novo and collaborators (arXiv:1412.7209; Scientific Reports 5, 13304) analyzed invariant-subspace transport with a single absorbing vertex and identified Hamming-shell reduction for a one-trap hypercube. Novo, Mohseni and Omar (Scientific Reports 6, 18142) studied noise-assisted hypercube transport with a single trap. Razzoli, Paris and Bordone (arXiv:2011.13794; Entropy 23, 85) also formulated coherent transport efficiencies with a single trap. Lugão and collaborators (arXiv:2203.14384) developed a multimarked *Hermitian search* framework, focused on Johnson graphs, which differs from continuous irreversible absorption.

The present result determines the previously unaddressed two-absorber Hamming-distance dichotomy, the exact rational survival kernel for **every** localized initial site, and all unit-capture site classes. The general method of projecting onto trap-visible eigenspaces is an established input, not claimed as new. A literature search cannot rule out equivalent special-purpose derivations, and independent priority evaluation has not been performed.

## Limitations
This concerns finite binary hypercubes, uniform nonzero hopping, loss at exactly two distinct vertices, and strictly positive fixed absorption strengths. It does not provide finite-time mixing, trapping-time distributions, estimates uniform in \(d\), or conclusions for disorder, other topologies, discrete-time coined walks, monitored returns, or coherent source injections. The \(d=2\) nonantipodal case is included and has zero survival from all four sites. Computational checks through \(d=6\) are non-exhaustive outside their declared range. Published general spectral-projection principles remain necessary antecedents, and bibliographic uniqueness is not independently certified.

## References
1. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137 (first public 2001-04-29), https://arxiv.org/abs/quant-ph/0104137.
2. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (first public 2014-12-22); Scientific Reports 5, 13304 (2015), https://www.nature.com/articles/srep13304.
3. L. Novo, M. Mohseni and Y. Omar, *Disorder-assisted quantum transport in suboptimal decoherence regimes*, Scientific Reports 6, 18142 (2016), https://www.nature.com/articles/srep18142.
4. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, arXiv:2011.13794 (2020), Entropy 23, 85 (2021), https://arxiv.org/abs/2011.13794.
5. P. H. G. Lugão, R. Portugal, M. Sabri and H. Tanaka, *Multimarked Spatial Search by Continuous-Time Quantum Walk*, arXiv:2203.14384 (2022), ACM Transactions on Quantum Computing 5, article 28 (2024), https://doi.org/10.1145/3706064.
