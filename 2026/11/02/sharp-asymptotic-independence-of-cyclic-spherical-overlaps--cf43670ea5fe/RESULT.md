# Sharp asymptotic independence of cyclic spherical overlaps

## Finding

Fix an integer \(d\ge3\). For every integer \(m\ge4\), let \(U_1,\ldots,U_m\) be independent uniform random vectors on the Euclidean sphere \(S^{d-1}\), set \(U_{m+1}=U_1\), and observe the consecutive inner products
\[
Z_j=\langle U_j,U_{j+1}\rangle,\qquad 1\le j\le m.
\]
Let \(\nu_d\) be the one-edge law, with density
\[
w_d(z)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-z^2)^{(d-3)/2}\mathbf1_{(-1,1)}(z).
\]
Every strict subcollection of the \(m\) observed edges is **exactly independent** with marginal \(\nu_d\). Nevertheless, the entire cycle is dependent, and its law \(\mu_{d,m}\) has the following exact \(L^2(\nu_d^{\otimes m})\) density:
\[
\boxed{\frac{d\mu_{d,m}}{d\nu_d^{\otimes m}}(z_1,\ldots,z_m)
=1+\sum_{\ell=1}^{\infty}D_{d,\ell}\prod_{j=1}^mQ_{d,\ell}(z_j).}
\]
Here \(Q_{d,\ell}(z)=C_\ell^{((d-2)/2)}(z)/C_\ell^{((d-2)/2)}(1)\), \(Q_{d,0}=1\), and
\[
D_{d,\ell}=\frac{(2\ell+d-2)(\ell+d-3)!}{\ell!(d-2)!},\quad \ell\ge0.
\]
In particular, the exact chi-square divergence from the law of independent edges is
\[
\boxed{\chi^2(\mu_{d,m}\Vert\nu_d^{\otimes m})
=\sum_{\ell=1}^{\infty}D_{d,\ell}^{\,2-m}\sim d^{\,2-m}\quad(m\to\infty).}
\]
Put
\[
a_d=\int_{-1}^1|z|\,\nu_d(dz)
=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
D_{d,2}=\frac{(d-1)(d+2)}2.
\]
The total variation distance has the **sharp** first-order asymptotic, with an explicit remainder,
\[
\boxed{\left|\|\mu_{d,m}-\nu_d^{\otimes m}\|_{\rm TV}
-\frac d2a_d^m\right|
\le\frac12\left(\sum_{\ell=2}^{\infty}D_{d,\ell}^{\,2-m}\right)^{1/2}
=O_d(D_{d,2}^{-m/2}),}
\]
and \(\|\mu_{d,m}-\nu_d^{\otimes m}\|_{\rm TV}\sim(d/2)a_d^m\). The asymptotic is for **fixed** \(d\) and increasing cycle length \(m\); it is not claimed uniformly in dimension.

For independent Haar-random pure **qubit** states \(\psi_j\in\mathbb C^2\), put \(F_j=|\langle\psi_j,\psi_{j+1}\rangle|^2\) around a closed cycle. The Bloch-sphere identity \(2F_j-1=Z_j\) with \(d=3\) makes every strict subcollection of the \(F_j\) independent uniforms on \([0,1]\), while
\[
\boxed{\left\|\mathcal L(F_1,\ldots,F_m)-\operatorname{Unif}[0,1]^{\otimes m}\right\|_{\rm TV}
\sim \frac{3}{2^{m+1}}.}
\]

## Assumptions and scope

All sphere points are independent with normalized rotation-invariant surface measure. The graph of observations is the *simple labelled cycle* with \(m\ge4\) distinct vertices. The real ambient dimension is an integer \(d\ge3\); the complex qubit specialization uses the standard Bloch representation, not a dimension substitution for higher-dimensional quantum states. Total variation is \(\|P-Q\|_{\rm TV}=\frac12\int|dP/dQ-1|\,dQ\) when \(P\ll Q\). The chi-square divergence here is Pearson's \(\int(dP/dQ-1)^2dQ\). All convergence in the displayed density is in \(L^2\), and no unsupported assertion of pointwise or uniform convergence is made.

## Proof

**1. Forest marginal independence.** Removing at least one edge from a simple cycle produces a forest. Given the endpoints of the other edges, a leaf's sole observed inner product has law \(\nu_d\), independently of its neighbor's location, by rotational invariance. Iterating leaf integration proves exact independence of every edge set forming a forest, hence of every strict subcollection.

**2. Harmonic trace identity.** For each \(\ell\ge0\), let \(\mathcal H_{d,\ell}\) be the degree-\(\ell\) spherical harmonic subspace of \(L^2(S^{d-1},\sigma)\), of dimension \(D_{d,\ell}\), and let \(\Pi_{d,\ell}\) be its orthogonal projection. Its kernel is \(D_{d,\ell}Q_{d,\ell}(\langle u,v\rangle)\) by the spherical addition formula (with \(\sigma\) normalized). Consequently the integral operator whose kernel is \(Q_{d,\ell}(\langle u,v\rangle)\) is exactly \(D_{d,\ell}^{-1}\Pi_{d,\ell}\).

For arbitrary nonnegative integers \(\ell_1,\ldots,\ell_m\), independence of the vertices and cyclic integration therefore give
\[
\begin{aligned}
\mathbb E\prod_{j=1}^m Q_{d,\ell_j}(Z_j)
&=\operatorname{tr}\prod_{j=1}^m(D_{d,\ell_j}^{-1}\Pi_{d,\ell_j})\\
&=\begin{cases}D_{d,\ell}^{\,1-m},&\ell_1=\cdots=\ell_m=\ell,\\0,&\text{otherwise.}\end{cases}
\end{aligned}
\]
The last equality uses mutual orthogonality of different harmonic degrees. This holds for every \(m\ge3\); the restriction \(m\ge4\) enters at the density step.

**3. Reconstruction and exact chi-square divergence.** Gegenbauer orthogonality under \(\nu_d\) reads
\[
\int Q_{d,\ell}(z)Q_{d,k}(z)\,\nu_d(dz)
=\frac{\mathbf1_{\{\ell=k\}}}{D_{d,\ell}}.
\]
Set \(h_N=1+\sum_{\ell=1}^N D_{d,\ell}\prod_{j=1}^mQ_{d,\ell}(z_j)\). The summands are mutually orthogonal in \(L^2(\nu_d^{\otimes m})\) and have squared norms \(D_{d,\ell}^{2-m}\). Since \(D_{d,\ell}\asymp_d\ell^{d-2}\), this series is square summable for \(d\ge3,m\ge4\). Thus \(h_N\to h\) in \(L^2\), also in \(L^1\), with \(\int h=1\). For every product of Gegenbauer polynomials, integration against \(h\nu_d^{\otimes m}\) agrees with the exact spherical-cycle mixed moment from step 2. These polynomial products span a dense subalgebra of \(C([-1,1]^m)\), so uniqueness of finite signed measures shows \(h\nu_d^{\otimes m}=\mu_{d,m}\). In particular \(h\ge0\) almost everywhere; this positivity is established by equality with the genuine joint law rather than incorrectly assumed from a truncated series. Orthogonality gives the chi-square identity. As \(m\to\infty\), the \(\ell=1\) term is \(D_{d,1}^{2-m}=d^{2-m}\), while the remaining terms decay faster because \(D_{d,\ell}\) is strictly increasing.

**4. Sharp total variation.** We have \(Q_{d,1}(z)=z\), \(D_{d,1}=d\), and therefore
\[
h-1=d\prod_{j=1}^m z_j+R_{d,m},\qquad
\|R_{d,m}\|_2^2=\sum_{\ell\ge2}D_{d,\ell}^{2-m}.
\]
The reverse triangle inequality in \(L^1\), followed by Cauchy–Schwarz, gives the claimed explicit TV remainder. Moreover \(\|d\prod z_j\|_1/2=(d/2)a_d^m\). Monotonicity of \(D_{d,\ell}\) and convergence of \(\sum_{\ell\ge2}D_{d,\ell}^{-2}\) imply
\[
\sum_{\ell\ge2}D_{d,\ell}^{2-m}
\le D_{d,2}^{4-m}\sum_{\ell\ge2}D_{d,\ell}^{-2},
\qquad m\ge4.
\]
It remains to show \(a_d\sqrt{D_{d,2}}>1\) for **every** integer \(d\ge3\). Directly, \(D_{3,2}a_3^2=5/4>1\), \(D_{4,2}a_4^2=16/\pi^2>1\), and the gamma recurrence gives
\[
\frac{D_{d+2,2}a_{d+2}^2}{D_{d,2}a_d^2}
=\frac{d^2(d+4)}{(d-1)(d+1)(d+2)}>1.
\]
The two base cases and induction on parity establish the strict inequality, making the error \(o_d(a_d^m)\) and completing the TV asymptotic.

**5. Qubits and moment consistency.** A Haar qubit has a uniform Bloch vector on \(S^2\), and \(F_j=(1+Z_j)/2\). Since \(\nu_3\) is uniform on \([-1,1]\), changing variables in the total variation statement gives \((3/2)(1/2)^m=3/2^{m+1}\). The forest argument also yields, for every \(m\ge3\),
\[
\mathbb E\prod_{j=1}^m F_j
=2^{-m}(1+3^{1-m})=2^{-m}+3\,6^{-m},
\]
which agrees with the independent complex-state cyclic Bargmann modulus-square moment of Zhang's Theorem 6.7, because \(\prod F_j=|\Delta_m|^2\). This moment checks one projection of the full joint density, but does not itself imply the total-variation result.

## Verification

The bundled \(\texttt{verify.py}\) runs under Python 3 using only the standard library. Execute \(\texttt{python3 verify.py}\) and compare with \(\texttt{verification_output.txt}\). It checks exact rational Gegenbauer orthogonality in several dimensions and degrees, the degree-one and degree-two normalizations, exact qubit cyclic-moment identities, harmonic-dimension monotonicity and the strict two-step rate comparison, alongside finite diagnostic values of the spectral remainder. This program establishes finite algebraic consistency, not completeness of the harmonic basis, infinite-series convergence or the asymptotic result; those are proved above.

## Relationship to prior work

Zhang (2026), Theorems 6.7 and 6.10, computes cyclic Bargmann moments and long-cycle laws for the *product* of complex overlaps; its moment formula is explicitly reconciled in step 5. This work instead determines the **entire joint law of individually observed consecutive real spherical inner products** and its sharp approach to the independent-edge product in total variation, including the qubit-fidelity specialization. Huang and Li (2026) establish forest edge-indicator independence and use traces of spherical kernel operators for random geometric graph testing, primarily in growing dimension; the cycle density and fixed-dimensional length-asymptotic sharp TV constant are not stated there. Jones and Potechin (2021/2022) develop graph-based spherical inner-product polynomial bases and combinatorial moments, but their inspected statements do not give this full density or the sharp TV rate. All are related mechanisms and are credited; priority over every possibly implicit application of those general techniques is not claimed.

## Limitations

The result assumes independent spherical vertices, simple cycles, fixed integer \(d\ge3\), and \(m\ge4\). It does not address repeated vertices, nonuniform spherical laws, high-dimensional complex pure states beyond the qubit Bloch identification, or a dimension-uniform rate. The density is asserted only in \(L^2\), not absolutely or pointwise; the exact total variation distance is bounded sharply to first order, not evaluated by a finite closed expression for each \(m\). The harmonic kernel and operator trace identities are classical. Historical priority is subject to further checking for implicit consequences of general random-geometric-graph and polynomial-chaos frameworks. No independent mathematical review has been carried out.

## References

1. Lin Zhang, *Exact probability laws of random inner products: Dirichlet splines, overlaps, uncertainty, and Bargmann invariants*, arXiv:2610.25196v1, first posted 2026-10-18, https://arxiv.org/abs/2610.25196.
2. Dong Huang and Shuangping Li, *Detecting Random Geometric Graphs with General Kernel*, arXiv:2610.12765v1, first posted 2026-10-08, https://arxiv.org/abs/2610.12765.
3. Chris Jones and Aaron Potechin, *Almost-Orthogonal Bases for Inner Product Polynomials*, arXiv:2107.00216, first posted 2021-07-01; ITCS 2022, DOI:10.4230/LIPIcs.ITCS.2022.89, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2022.89.
4. Classical spherical-harmonic addition formula and Funk–Hecke eigenvalue decomposition; standard orthogonality of normalized Gegenbauer polynomials.
