# Sharp two-observable fiber stability and a three-observable Pauli obstruction

## Finding
Let \(H\) be a finite-dimensional complex Hilbert space with \(\dim H\ge2\). For Hermitian \(A_1,\ldots,A_m,B\), define the **pure-state information defect**
\[
\Delta_{\mathbf A}(B)=\max_{\substack{\|x\|=\|y\|=1\\\langle A_jx,x\rangle=\langle A_jy,y\rangle\ (1\le j\le m)}}|\langle Bx,x\rangle-\langle By,y\rangle|.
\]
The main assertion has two linked parts.

**Sharp stability for two observations.** For all Hermitian \(A_1,A_2,B\), with no commutation hypothesis,
\[
\boxed{\Delta_{A_1,A_2}(B)=2\inf_{a_0,a_1,a_2\in\mathbb R}\|B-a_0I-a_1A_1-a_2A_2\|.}
\]
Whenever the right side is positive, an **orthogonal** unit pair attains the maximum on the left. The same assertion holds with only one or zero observations.

**Sharp failure with three observations.** Let \(\sigma_1,\sigma_2,\sigma_3\) be the standard three Hermitian Pauli matrices on \(\mathbb C^2\). On \(\mathbb C^4=\mathbb C^2\oplus\mathbb C^2\), for each \(0\le r\le1\) put
\[
A_j(r)=\sigma_j\oplus r\sigma_j\quad(j=1,2,3),\qquad B=I_2\oplus(-I_2).
\]
Then
\[
\boxed{\Delta_{A_1(r),A_2(r),A_3(r)}(B)=\frac{4r}{1+r},\qquad\operatorname{dist}\left(B,\operatorname{span}_{\mathbb R}\{I_4,A_1(r),A_2(r),A_3(r)\}\right)=1.}
\]
In particular, at \(r=0\), the numerical expectation of \(B\) factors through the three numerical expectations by the **nonaffine** formula
\[
\langle Bx,x\rangle=2\left(\sum_{j=1}^3\langle A_j(0)x,x\rangle^2\right)^{1/2}-1,\qquad\|x\|=1.
\]
Hence the exact two-observation distance identity fails already for three observations on \(\mathbb C^4\), even to every uniform positive lower-bound multiple of operator distance.

## Assumptions and scope
Inner products are complex Hilbert-space inner products and all observables are Hermitian. The symbol \(\|\cdot\|\) means operator norm. The maximum in \(\Delta\) is over two unit vectors; **mixed density matrices are not substituted for pure states**. Finite dimensionality guarantees compact numerical ranges, spectral eigenvectors, and attainment of minimizers. A real affine span includes the identity and is not a nonlinear functional calculus. No statement is made for general tuples with more than two observables or infinite-dimensional operator-distance identity.

## Proof
**Part I: the exact two-observation identity.** Write \(\mathcal R=\operatorname{span}_{\mathbb R}\{I,A_1,A_2\}\). For any \(C\in\mathcal R\), two unit vectors having the same \(A_1,A_2\) expectations have the same \(C\) expectation, so their \(B\)-expectations differ by at most \(2\|B-C\|\). Thus \(\Delta\le2\operatorname{dist}(B,\mathcal R)\).

Remove linear dependencies among \(A_1,A_2\) modulo the identity, leaving \(k\le2\) independent Hermitian observables \(C_1,\ldots,C_k\). For each \(t\in\mathbb R^k\), put \(D_t=B-\sum_{j=1}^kt_jC_j\), and define its spectral width \(w(t)=\lambda_{\max}(D_t)-\lambda_{\min}(D_t)\). The best scalar approximation to a Hermitian matrix is its spectral midpoint; therefore
\[
2\operatorname{dist}(B,\mathcal R)=\min_{t\in\mathbb R^k}w(t).
\]
The width is continuous and convex. If \(k>0\), it is coercive: the width of a Hermitian linear combination is a norm on the space of combinations modulo scalars, and the \(C_j\) are independent there. Hence a minimizer \(t_*\) exists (the case \(k=0\) is immediate).

Let \(E_+\) and \(E_-\) be the top and bottom eigenspaces of \(D_{t_*}\). For a unit vector \(u\) in an eigenspace define its \(k\)-component expectation vector \(F(u)=(\langle C_1u,u\rangle,\ldots,\langle C_ku,u\rangle)\). Spectral max/min variational formulas give the exact convex subdifferential
\[
\partial w(t_*)=-\operatorname{conv}F(S(E_+))+\operatorname{conv}F(S(E_-)).
\]
Optimality says \(0\in\partial w(t_*)\), so these two convex hulls intersect. **Because \(k\le2\), each set \(F(S(E_\pm))\) is already compact and convex:** for \(k=2\) this is the Toeplitz–Hausdorff convexity theorem applied to the compression of \(C_1+iC_2\) to \(E_\pm\); for smaller \(k\) it follows from the Rayleigh-quotient interval. Thus there are unit vectors \(x\in E_+\), \(y\in E_-\) satisfying \(F(x)=F(y)\). Their \(A_1,A_2\) expectations agree, and
\[
\langle Bx,x\rangle-\langle By,y\rangle=\lambda_{\max}(D_{t_*})-\lambda_{\min}(D_{t_*})=w(t_*).
\]
This supplies the matching lower bound. If \(w(t_*)>0\), distinct eigenspaces are orthogonal, proving the rigidity claim. If \(w(t_*)=0\), then \(B\in\mathcal R\) and both sides are zero.

**Part II: three Pauli observations.** A pure normalized qubit vector has a Pauli expectation vector on the unit sphere \(S^2\), and every point of \(S^2\) is attained. For a unit vector \(x=(u,v)\in\mathbb C^2\oplus\mathbb C^2\), put \(p=\|u\|^2\). Its three recorded expectations are
\[
a=p\,m+r(1-p)n,\qquad m,n\in S^2\quad\text{when the associated block is nonzero},
\]
while its \(B\)-expectation is \(2p-1\). At a fixed \(p\in[0,1]\), all radii of the vector \(a\) in the interval
\[
L_r(p)=|(1+r)p-r|\ \le\ |a|\ \le\ U_r(p)=r+(1-r)p
\]
are attained. This statement also holds at the zero-weight endpoints as a single radius. Rotational symmetry makes the entire spherical shell attainable.

If two states have block masses \(p\ge q\), their three observation vectors can coincide precisely when the two radial intervals overlap. Since \(U_r\) is increasing and \(L_r(q)\le U_r(q)\le U_r(p)\), this overlap is equivalent to \(L_r(p)\le U_r(q)\). If \(p\le r/(1+r)\) the bound \(p-q\le2r/(1+r)\) is immediate. Otherwise the overlap condition implies
\[
(1+r)p-r\le r+(1-r)q\ \Longrightarrow\ p-q\le\frac{2r}{1+r}(1-q)\le\frac{2r}{1+r}.
\]
The bound is sharp: take \(q=0\), \(p=2r/(1+r)\), choose the top and bottom qubit Bloch vectors antiparallel, and compare to a lower-block state in the direction of their resultant. Both recorded triples coincide and the \(B\)-expectation gap is \(2p=4r/(1+r)\).

For any \(a_0\in\mathbb R\) and \(t\in\mathbb R^3\), the two diagonal qubit blocks of \(B-a_0I_4-\sum_jt_jA_j(r)\) have operator norms \(|1-a_0|+\|t\|_2\) and \(|-1-a_0|+r\|t\|_2\). Their maximum is at least one; choosing \(a_0=0\), \(t=0\) attains one. This proves the distance identity. At \(r=0\), the expectation vector is \(a=p m\), hence \(\|a\|_2=p\) and \(2p-1=2\|a\|_2-1\), the announced nonlinear dependence.

## Verification
The proof uses only finite-dimensional convex analysis, spectral min-max, Toeplitz–Hausdorff, and elementary two-qubit Bloch geometry. The supplementary `CHECK.py` executes deterministic exact-rational shell-overlap tests and explicit state-vector witnesses. These are finite consistency checks, **not** a replacement for the quantified proof. Execute with `python CHECK.py`; no third-party packages are required.

## Relationship to prior work
Dylan Johnson, *Numerical Information of Hilbert Space Operators* (arXiv:2610.29826, first public 2026-10-21), proves qualitative affine rigidity for the numerical information of a single complex operator, equivalent to two real Hermitian observations. The first part here is a sharp **quantitative operator-norm formula with orthogonal optimizers**; the second establishes precisely how that property breaks at three observations. Gutkin and Życzkowski (arXiv:1207.1227) develop joint numerical ranges/shadows and their quantum geometry. Pikul, Spitkovsky, Szymański, Weis, and Życzkowski (arXiv:2510.27670) classify face geometry of joint ranges for triples of four-by-four Hermitian matrices. These geometric results and the Bloch-sphere facts are prior tools, not claimed contributions. The new assertions concern **pure-state fibers, operator-distance exactness, and the complete parameterized obstruction**.

## Limitations
The universal distance formula is established in finite dimensions for **at most two** Hermitian observations. The three-observation computation concerns the explicit scaled Pauli-block family and does not classify all triples. The factorization at zero scaling applies to unit vectors, not arbitrary mixed density operators; replacing pure-state fibers by mixed-state fibers can alter the conclusion. Independent validation and exhaustive historical priority confirmation have not been performed.

## References
1. D. Johnson, *Numerical Information of Hilbert Space Operators*, arXiv:2610.29826v1 (21 October 2026), https://arxiv.org/abs/2610.29826.
2. E. Gutkin and K. Życzkowski, *Joint numerical ranges, quantum maps, and joint numerical shadows*, arXiv:1207.1227 (2012), https://arxiv.org/abs/1207.1227.
3. P. Pikul, I. Spitkovsky, K. Szymański, S. Weis, and K. Życzkowski, *The joint numerical range of three 4×4 matrices*, arXiv:2510.27670 (2025), https://arxiv.org/abs/2510.27670.
4. Toeplitz–Hausdorff theorem (convexity of the numerical range) and standard Hermitian eigenvalue variational principles.
