# Exact average-mixing spectrum, parity nullity, and spectral gap of folded hypercubes

## Finding

For every integer \(d\geq 3\), let \(F_d\) be the *folded \(d\)-cube*: the simple graph obtained from the binary \(d\)-cube by identifying each vertex with its antipode. Write \(N=2^{d-1}\) for its number of vertices and \(A_d\) for its unweighted adjacency matrix. Define its standard continuous-time quantum average mixing matrix by
\[
\widehat M_d=\lim_{T\to\infty}\frac1T\int_0^T
  \bigl(e^{\mathrm{i}tA_d}\circ e^{-\mathrm{i}tA_d}\bigr)\,dt.
\]
Here \(\circ\) denotes entrywise multiplication. Every eigenvalue of \(\widehat M_d\), **with multiplicity**, is given as follows, indexed by even integers \(0\leq w\leq d\):
\[
\boxed{
\begin{aligned}
\mu_0&=1,\\
\mu_w&=\frac{\binom{w}{w/2}}{2^w}
  &&(0<w<d,\quad w\ \text{even}),\\
\mu_d&=\begin{cases}
 \frac{\binom{d}{d/2}}{2^{d-1}},&4\mid d,\\
 0,&d\equiv2\pmod 4
 \end{cases}
 &&(d\ \text{even}),
\end{aligned}}
\]
where the indexed eigenvalue \(\mu_w\) has multiplicity \(\binom{d}{w}\). Multiplicities are added whenever different indices give the same numerical eigenvalue. In particular,
\[
\boxed{\operatorname{rank}\widehat M_d
 =\begin{cases}2^{d-1}-1,&d\equiv2\pmod4,\\
 2^{d-1},&\text{otherwise},\end{cases}}
\]
and the entire kernel in the deficient case is the one-dimensional space spanned by the character that is \(+1\) on even-weight vertex classes and \(-1\) on odd-weight vertex classes.

More quantitatively, let \(k=\lfloor(d-1)/2\rfloor\). The **smallest strictly positive** eigenvalue is exactly
\[
\boxed{\gamma_d=\frac{\binom{2k}{k}}{4^k}.}
\]
Thus for all dimensions \(d\not\equiv2\pmod4\), the matrix is positive definite with the sharp bound \(\widehat M_d\succeq\gamma_d I_N\); the same lower bound holds on the orthogonal complement of the explicitly described kernel when \(d\equiv2\pmod4\). The sharp positive spectral gap is of order \(d^{-1/2}\); the positive-spectrum condition number is exactly \(4^k/\binom{2k}{k}\).

The odd-dimensional folded cubes form an infinite family of nonbipartite, distance-regular graphs, and the theorem supplies a full-rank family relevant to the primitive distance-regular average-mixing rank question. For comparison, \(F_5\) is the Clebsch graph, \(F_6\) has \(32\) vertices and rank \(31\), and \(F_8\) has \(128\) vertices and full rank.

## Assumptions and scope

All integers \(d\geq3\) are included; no simplicity, distinct-eigenvalue, genericity, or numerical nondegeneracy assumption is made beyond the stipulated graph construction. Let \(V=\mathbb F_2^d\), \(\mathbf 1=(1,\ldots,1)\), and set
\[
X=V/\langle\mathbf 1\rangle,
\qquad
S=\{[e_1],\ldots,[e_d]\}\subset X.
\]
The folded cube is the Cayley graph \(\operatorname{Cay}(X,S)\). For \(d\geq3\), the elements of \(S\) are distinct and nonzero, so this is an ordinary simple, unweighted graph of degree \(d\). Its adjacency Hamiltonian acts on complex-valued functions on \(X\).

The limit in the definition of \(\widehat M_d\) is the **uniform-in-time Cesàro mean**. It is not the transition matrix at an individual observation time, an optimized randomized-time average, a discrete-time coined quantum walk, or a Laplacian walk.

## Proof

**1. Characters and adjacency projectors.** A character of the quotient \(X\) has the form
\[
\chi_a([x])=(-1)^{a\cdot x},\qquad a\in\mathbb F_2^d,
\]
and is well-defined precisely when \(a\cdot\mathbf1=0\) in \(\mathbb F_2\), namely when the Hamming weight \(|a|\) is even. There are \(N=2^{d-1}\) such orthogonal characters. Acting with the adjacency matrix gives
\[
A_d\chi_a=\sum_{j=1}^d\chi_a(\,\cdot+[e_j]\,)
 =\bigl(d-2|a|\bigr)\chi_a.
\]
In this displayed expression, \(\chi_a(\,\cdot+[e_j]\,)\) denotes translation of the argument by \([e_j]\). Since distinct even weights give distinct eigenvalues, the orthogonal projector onto the \(d-2r\) eigenspace, for each even \(r\in[0,d]\), is
\[
(E_r)_{x,y}=
 \frac1N\sum_{\substack{a\in\mathbb F_2^d\\|a|=r}}
 \chi_a(x+y).
\]
The spectral projectors are real and mutually orthogonal.

**2. The average and its Fourier multipliers.** Spectral decomposition of the continuous-time transition matrix, followed by Cesàro averaging, gives the exact identity
\[
\widehat M_d=\sum_{r\ \mathrm{even}}E_r\circ E_r.
\]
Indeed, the cross terms between distinct adjacency eigenvalues have zero infinite-time Cesàro mean. Consequently \(\widehat M_d\) is translation invariant on \(X\). Each character \(\chi_b\) diagonalizes it. Orthogonality of the finite-group characters gives, for \(w=|b|\) even,
\[
\begin{aligned}
\widehat M_d(x,y)&=
 \frac1{N^2}\sum_{r\ \mathrm{even}}
  \sum_{\substack{|a|=|c|=r}}\chi_{a+c}(x+y),\\
\mu_w&=\frac1N
\#\{(a,c):|a|=|c|\ \mathrm{even},\ a+c=b\}.
\end{aligned}
\]
This identity counts **ordered** pairs, which fixes the normalization.

**3. Exact parity count.** Suppose \(w=|b|\) is even. On the \(w\) coordinates supporting \(b\), exactly \(w/2\) must be selected into \(a\) for \(|a|=|a+b|\). On the remaining \(d-w\) coordinates let \(j\) be the number selected into \(a\). The common weight is \(w/2+j\); the requirement that it be even is precisely \(j\equiv w/2\pmod2\). Hence
\[
\mu_w=\frac1N\binom{w}{w/2}
\sum_{\substack{0\le j\le d-w\\j\equiv w/2\ (\mathrm{mod}\ 2)}}
 \binom{d-w}{j}.
\]
When \(w<d\), the parity-restricted binomial sum equals \(2^{d-w-1}\), and therefore
\[
\mu_w=\frac{\binom{w}{w/2}}{2^w}.
\]
For \(w=0\), the same formula gives \(\mu_0=1\), also confirming that the stochastic matrix has constant row sum one. The exceptional endpoint \(w=d\) only exists as a character when \(d\) is even. Then there are no coordinates outside the support, so the common weight is \(d/2\), which is even exactly when \(4\mid d\). The count is then \(\binom{d}{d/2}\); otherwise it is zero. Since characters of weight \(w\) number \(\binom dw\), this proves the entire eigenvalue multiset.

**4. Kernel and rank.** Every interior even-weight multiplier is positive. The zero-weight multiplier is one. At the endpoint, a zero multiplier exists exactly for \(d\equiv2\pmod4\). The sole character at that weight is \(\chi_{\mathbf1}([x])=(-1)^{|x|}\), which is well-defined because \(d\) is even. All remaining Fourier multipliers are positive. This gives the stated kernel and both cases of the rank formula, without relying on finite-dimensional extrapolation.

**5. Sharp smallest-positive eigenvalue.** For \(j\ge0\) put \(c_j=\binom{2j}{j}/4^j\). Then
\[
\frac{c_{j+1}}{c_j}=\frac{2j+1}{2j+2}<1.
\]
Consequently, among interior even weights, the minimum occurs at the largest available even index \(2k\), where \(k=\lfloor(d-1)/2\rfloor\). If \(4\mid d\), its extra endpoint eigenvalue satisfies
\[
\frac{\mu_d}{\mu_{d-2}}=
 \frac{2(d-1)}{d}>1,
\]
so it does not lower the minimum. If \(d\equiv2\pmod4\), the endpoint is zero and is excluded from the positive-spectrum minimum. This proves \(\gamma_d=c_k\) sharply: an actual nonzero Fourier eigenvector realizes the bound. The standard central-binomial asymptotic gives \(\gamma_d\sim(\pi k)^{-1/2}\), hence order \(d^{-1/2}\).

## Verification

The standalone `verify.py` constructs the quotient graph from the \(d\) distinct connection vectors, verifies every adjacency Fourier eigenpair, builds the Cesàro matrix from the exact integer Walsh-projector entries, and independently transforms that matrix into its Fourier spectrum. It checks the formula, multiplicities, nullity, and sharp positive gap for each \(d=3,4,5,6,7,8,9\), using only Python integers and exact rational arithmetic.

Run `python3 verify.py` from the directory containing this document and the checker. The exact replay concludes:

`VERIFY_OK dimensions=3..9 adjacency_tests=87376 eigenmodes=508`

The checker is finite evidence, not an infinite proof. The proof above handles all integers \(d\ge3\).

## Relationship to prior work

Godsil's account of folded cubes discusses their quotient construction and **instantaneous** uniform mixing (Section 17 in *State Transfer on Graphs*). Fan and Luo's cubelike-graph treatment and Chan's association-scheme work likewise address instantaneous uniformity or complex Hadamard matrices; these statements do not determine the long-time Cesàro spectrum. General results by Godsil and by Coutinho, Godsil, Guo and Zhan give the projector-Schur-square definition and commutant interpretation of average mixing but do not identify the folded-cube multipliers above.

Coutinho, Ferreira Baptista, Godsil, Spier and Werner give exact methods for average mixing for integral adjacency Hamiltonians; that method is foundational here and does not assert the folded-cube rank classification. The 2024 survey by Coutinho and Guo explicitly poses full rank for primitive distance-regular graphs as Open Problem 4.1. Odd-dimensional folded cubes provide one motivated infinite subfamily, while the even-dimensional cases show a distinct one-mode parity obstruction.

A result for the ordinary hypercube's average mixing does **not** give this quotient's spectrum just by deleting vertices: quotienting combines antipodal transition amplitudes before their squared moduli are averaged. The proof uses the parity-filtered **quotient projectors** and an additional pair-counting argument. Previously characterized small cases, including the Clebsch graph and the complete bipartite folded four-cube, are not claimed as newly classified individually. The contribution is the complete dimension-uniform spectrum, nullity transition, and sharp positive spectral gap.

## Limitations

This theorem concerns only the standard unweighted folded hypercubes with \(d\ge3\), their adjacency-generated continuous-time walks, and uniform-in-time Cesàro averages. It does not solve the full primitive distance-regular rank problem, characterize average-mixing matrices of arbitrary cubelike graphs, or infer instantaneous uniform mixing from positive definiteness. A more general unlocated Fourier/association-scheme theorem might imply the special family result; the literature comparison cannot establish universal uniqueness. The quantitative asymptotic describes the sharp smallest **positive** eigenvalue; when \(d\equiv2\pmod4\), the matrix still has one exact zero eigenvalue.

## References

1. C. Godsil, *Average Mixing of Continuous Quantum Walks*, Journal of Combinatorial Theory A **120** (2013), 1649–1662; arXiv:1103.2578.
2. G. Coutinho, C. Godsil, K. Guo and H. Zhan, *A New Perspective on the Average Mixing Matrix*, Electronic Journal of Combinatorics **25** (2018), P4.14; arXiv:1709.03591.
3. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational Quantum Walks*, arXiv:2208.08971, first posted 2022-08-18, primary MSC2020 81P68.
4. C. Godsil, *State Transfer on Graphs*, arXiv:1102.4898, Section 17 (folded-cube quotient construction and instantaneous mixing).
5. G. Coutinho and K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236, §4, Open Problem 4.1.
6. X. Fan and Y. Luo, *Mixing of Continuous Quantum Walks on Cubelike Graphs*, Journal of Lanzhou University (Natural Sciences), **49**(1) (2013) (instantaneous mixing; folded-cube nomenclature shifted by one dimension).
7. A. Chan, *Complex Hadamard Matrices, Instantaneous Uniform Mixing and Cubes*, arXiv:1305.5811.
