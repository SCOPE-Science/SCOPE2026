# Exact order-two RIU entropy and maximizing product bases of the Higuchi–Sudbery state
## Finding
For the four-qubit Higuchi–Sudbery state
\[
|HS\rangle=\frac{1}{\sqrt6}\Bigl(|0011\rangle+|1100\rangle+\omega(|0101\rangle+|1010\rangle)+\omega^2(|0110\rangle+|1001\rangle)\Bigr),
\qquad \omega=e^{2\pi i/3},
\]
the order-two minimal Rényi–Ingarden–Urbanik entropy is exactly
\[
S^{\mathrm{RIU}}_2(HS)=\log 6.
\]
Equivalently, every local product measurement basis gives probabilities \(p_s\) satisfying
\[
\sum_{s\in\{\pm1\}^4}p_s^2\le \frac16.
\]
Equality holds exactly when the four local measurement axes lie on a single common Bloch line, up to independent outcome relabelings. The computational basis is one such equality basis.

## Assumptions and scope
A local qubit projective basis is represented by a unit Bloch vector \(n_i\in\mathbb R^3\); its two outcomes are the eigenstates of \(n_i\cdot\sigma\). Reversing \(n_i\) only relabels the two outcomes and does not change the collision probability.

For a product measurement with axes \(n_1,n_2,n_3,n_4\), write
\[
g_{ij}=n_i\cdot n_j,
\qquad
D_{ijk}=\det(n_i,n_j,n_k),
\]
and
\[
Q=g_{12}g_{34}+g_{13}g_{24}+g_{14}g_{23}.
\]
Natural logarithms are used, as in the defining source.

The theorem concerns the exact value of the order-two RIU entropy of this one state and the complete equality condition for its optimizing product bases. It does not prove that \(|HS\rangle\) is a global maximizer over all four-qubit states, and it does not determine the minimal RIU entropy at other Rényi orders.

## Proof
For the outcome signs \(s_i\in\{\pm1\}\), Fourier expansion on the four-dimensional Boolean cube gives
\[
p_s=\frac1{16}\sum_{A\subseteq\{1,2,3,4\}}
\left(\prod_{i\in A}s_i\right)E_A,
\]
where
\[
E_A=\left\langle HS\left|\prod_{i\in A}(n_i\cdot\sigma_i)\right|HS\right\rangle.
\]
Parseval's identity therefore yields
\[
\sum_s p_s^2=\frac1{16}\sum_A E_A^2. \tag{1}
\]

A direct exact evaluation of the Pauli correlations of \(|HS\rangle\) gives the following tensors. All one-body correlations vanish. For every pair,
\[
\langle\sigma_i^a\sigma_j^b\rangle=-\frac13\delta_{ab}. \tag{2}
\]
For every triple, the tensor is a sign times the Levi-Civita tensor,
\[
\langle\sigma_i^a\sigma_j^b\sigma_k^c\rangle
=\varepsilon_{ijk}\frac1{\sqrt3}\epsilon_{abc},
\qquad \varepsilon_{ijk}\in\{\pm1\}, \tag{3}
\]
where the triple-dependent sign disappears after squaring. Finally,
\[
\langle\sigma_1^a\sigma_2^b\sigma_3^c\sigma_4^d\rangle
=\frac13\bigl(\delta_{ab}\delta_{cd}+\delta_{ac}\delta_{bd}+\delta_{ad}\delta_{bc}\bigr). \tag{4}
\]
The accompanying exact checker verifies equations \((2)\)–\((4)\) for every Pauli component directly from the six amplitudes of \(|HS\rangle\).

Put
\[
S=\sum_{i<j}g_{ij}^2,
\qquad
T=\sum_{i<j<k}D_{ijk}^2.
\]
Substituting \((2)\)–\((4)\) into \((1)\) gives the exact collision formula
\[
16\sum_s p_s^2
=1+\frac{S}{9}+\frac{T}{3}+\frac{Q^2}{9}. \tag{5}
\]
Thus it remains to prove
\[
S+3T+Q^2\le15. \tag{6}
\]

Let
\[
P=g_{12}^2g_{34}^2+g_{13}^2g_{24}^2+g_{14}^2g_{23}^2.
\]
The Gram determinant of the four unit vectors vanishes because they lie in \(\mathbb R^3\). Expanding that determinant gives
\[
Q^2=T+S+2P-3. \tag{7}
\]
Consequently
\[
S+3T+Q^2=2S+4T+2P-3. \tag{8}
\]

Now define the positive semidefinite frame operator
\[
M=\sum_{i=1}^4 n_i n_i^{\mathsf T}.
\]
If its eigenvalues are \(\lambda_1,\lambda_2,\lambda_3\ge0\), then \(\lambda_1+\lambda_2+\lambda_3=4\). Moreover,
\[
\operatorname{tr}(M^2)=4+2S,
\qquad
\det M=T,
\]
the second identity being Cauchy–Binet. Therefore
\[
S+2T\le6 \tag{9}
\]
is equivalent to
\[
\operatorname{tr}(M^2)+4\det M\le16.
\]
Writing the latter in terms of the eigenvalues reduces it to
\[
2\lambda_1\lambda_2\lambda_3
\le
\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3. \tag{10}
\]
If one eigenvalue vanishes, \((10)\) is immediate. Otherwise division by their product reduces \((10)\) to
\[
2\le\frac1{\lambda_1}+\frac1{\lambda_2}+\frac1{\lambda_3},
\]
while Cauchy's inequality gives the stronger bound
\[
\frac1{\lambda_1}+\frac1{\lambda_2}+\frac1{\lambda_3}\ge\frac94.
\]
Hence \((9)\) holds. Also each \(|g_{ij}|\le1\), so
\[
P\le3. \tag{11}
\]
Combining \((8)\), \((9)\), and \((11)\) proves \((6)\). Equation \((5)\) then gives
\[
\sum_s p_s^2\le\frac16.
\]

For equality, both \((9)\) and \((11)\) must be equalities. Equality in \((9)\) forces \(M\) to have rank one, because it is strict for positive rank two or three. Thus all four axes are collinear. Conversely, collinear axes give equality in every displayed bound. In the computational basis the six nonzero probabilities are all \(1/6\), so the collision probability is \(1/6\). Therefore
\[
S^{\mathrm{RIU}}_2(HS)=-\log\left(\frac16\right)=\log6,
\]
and the maximizing product bases are exactly those with a common Bloch line, modulo local outcome relabelings.

## Verification
Run `python3 artifacts/verify.py` from the package directory. The checker uses only the Python standard library and exact arithmetic in \(\mathbb Q(i,\sqrt3)\). It reconstructs the six unnormalized Higuchi–Sudbery amplitudes, evaluates every one-, two-, three-, and four-body Pauli expectation exactly, and verifies equations \((2)\)–\((4)\). It also verifies the expanded four-vector Gram identity \((7)\) as a polynomial identity with rational coefficients.

The finite checker is a replay of algebra used in the proof; it is not used to infer the universal optimization over continuous measurement axes. The infinite statement follows from the analytic inequalities \((7)\)–\((11)\).

## Relationship to prior work
Enríquez, Puchała, and Życzkowski introduced the minimal Rényi–Ingarden–Urbanik entropy and identified the order-two case with the maximal collision probability of outcomes in a local product basis. Their four-qubit section states that further numerical tests support the Higuchi–Sudbery conjecture and reports \(S^{\mathrm{RIU}}_2(HS)=\log6\), but supplies no analytic optimization over all local bases. Their paper also emphasizes that exact multipartite RIU minimization generally lacks a constructive method.

The 2016 survey by Enríquez, Wintrowicz, and Życzkowski lists the Higuchi–Sudbery value \(\log6\) at order two with a star; the table caption explicitly says that starred values are conjectured from numerical calculations. Thus the numerical value itself is not presented here as a new numerical discovery. The new statement is the exact continuous-basis proof together with the equality characterization.

Higuchi and Sudbery's original paper studies average entanglement across two-versus-two bipartitions, not minimal product-basis collision entropy. Hilling and Sudbery study the geometric measure, which is governed by a single largest product overlap and corresponds to the \(q\to\infty\) end of the RIU family, not the order-two sum of squared product-basis probabilities. Neither result implies the bound proved here.

Targeted searches for the state name together with order-two RIU entropy, decomposition entropy, collision probability, index of coincidence, local product bases, and the value \(1/6\) did not locate a later analytic proof or an implication-equivalent equality classification. Search failure is not treated as proof of novelty; a differently phrased or poorly indexed derivation remains a residual risk.

## Limitations
The theorem does not settle the broader conjecture that the Higuchi–Sudbery state globally maximizes minimal RIU entropy among four-qubit states for \(q\ge2\). It proves only the exact order-two value for the fixed state and identifies all product measurements attaining the associated collision maximum.

The originality comparison included the defining RIU paper, the 2016 survey, the original Higuchi–Sudbery paper, geometric-measure literature, and targeted semantic literature searches. A later proof using substantially different terminology could have escaped those searches.

## References
1. M. Enríquez, Z. Puchała, and K. Życzkowski, “Minimal Rényi–Ingarden–Urbanik entropy of multipartite quantum states,” arXiv:1506.04788, first submitted 2015-06-15; Entropy 17 (2015), 5063–5084, DOI:10.3390/e17075063.
2. M. Enríquez, I. Wintrowicz, and K. Życzkowski, “Maximally Entangled Multipartite States: A Brief Survey,” Journal of Physics: Conference Series 698 (2016), 012003, DOI:10.1088/1742-6596/698/1/012003.
3. A. Higuchi and A. Sudbery, “How entangled can two couples get?”, arXiv:quant-ph/0005013; Physics Letters A 273 (2000), 213–217.
4. J. J. Hilling and A. Sudbery, “The geometric measure of multipartite entanglement and the singular values of a hypermatrix,” arXiv:0905.2094; Journal of Mathematical Physics 51 (2010), 072102, DOI:10.1063/1.3451264.
