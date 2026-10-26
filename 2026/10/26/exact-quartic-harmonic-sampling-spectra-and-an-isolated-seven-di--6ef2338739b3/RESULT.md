# Exact quartic harmonic sampling spectra and an isolated seven-dimensional defect on type-\(D\) roots

## Finding

For each integer \(d\ge5\), take one representative from each antipodal pair of normalized type-\(D_d\) roots:
\[
 X_d=\left\{x_{ij,s}=\frac{e_i+s e_j}{\sqrt2}:1\le i<j\le d,\quad s\in\{-1,1\}\right\}\subset S^{d-1}.
\]
It has \(N=d(d-1)\) points. Let \(\mathcal H_4(S^{d-1})\) be the degree-exactly-four spherical harmonics with normalized surface-measure \(L^2\) inner product and dimension
\[
 h_{d,4}=\binom{d+3}{4}-\binom{d+1}{2}.
\]
Define \(E_d:\mathcal H_4(S^{d-1})\to\mathbb C^{X_d}\) by \((E_df)(x)=f(x)/\sqrt{h_{d,4}}\). The squared singular values of \(E_d\), including zeros in its \(N\)-dimensional output Gram matrix \(G_d=E_dE_d^*\), are precisely

| Eigenvalue | Multiplicity |
| --- | ---: |
| \(\displaystyle A_d=\frac{d^2-4}{d^2-1}\) | \(\binom d2\) |
| \(\displaystyle B_d=\frac{(d-4)^2(d+4)}{4(d^2-1)}\) | \(1\) |
| \(\displaystyle C_d=\frac{(d-8)^2(d+2)}{8(d^2-1)}\) | \(d-1\) |
| \(\displaystyle D_d=\frac{3(d+2)(d+4)}{4(d^2-1)}\) | \(\frac{d(d-3)}2\) |

Thus \(E_d\) is onto exactly when \(d\ne8\). At \(d=8\) it has rank \(49\) and a seven-dimensional output obstruction, explicitly
\[
 \ker G_8=\left\{v_{ij,s}=a_i+a_j:\ \sum_{i=1}^{8}a_i=0\right\}.
\]
All its other eigenvalues are positive. Across every integer \(d\ge5\), including the positive spectrum at \(d=8\), the sharp dimension-uniform lower bound is
\[
 \boxed{\lambda_{\min}^{+}(G_d)\ge\frac{11}{640}.}
\]
Equality occurs exactly in the standard vertex-incidence sector at \(d=9\). Accordingly, whenever \(d\ne8\), arbitrary samples \(y\in\mathbb C^{X_d}\) admit a degree-four harmonic interpolant \(f\) with
\[
 E_df=y,\qquad \|f\|_{L^2(S^{d-1})}\le\sqrt{640/11}\,\|y\|_{\ell^2(X_d)}.
\]
The operator norm bound is attained at \(d=9\). For \(d=8\) the same bound holds for data orthogonal to \(\ker G_8\), and such orthogonality is necessary for interpolation.

## Assumptions and scope

The dimension is an integer \(d\ge5\). Roots are normalized Euclidean vectors; signs \(s=\pm1\) label distinct antipodal classes, and no opposite point is also sampled. The harmonics are restrictions of complex homogeneous Euclidean harmonic polynomials of exact degree four, not degrees at most four. The output space has the standard unweighted Euclidean inner product, while the sphere uses probability surface measure. With the factor \(1/\sqrt{h_{d,4}}\), the zonal Gram has diagonal entries equal to one. Multiplicities refer to this output Gram and not to the full harmonic-space operator \(E_d^*E_d\).

## Proof

**1. Spherical addition formula.** For an orthonormal basis \(\{Y_m\}_{m=1}^{h_{d,4}}\) of \(\mathcal H_4\), the addition theorem gives
\[
 G_d(x,y)=\frac1{h_{d,4}}\sum_mY_m(x)\overline{Y_m(y)}=P_{d,4}(x\cdot y),
\]
where the normalized Gegenbauer polynomial is
\[
 P_{d,4}(t)=\frac{(d+2)(d+4)t^4-6(d+2)t^2+3}{(d-1)(d+1)},\qquad P_{d,4}(1)=1.
\]
The only inner products among representatives are \(1,0,\pm1/2\). Set
\[
 u=P_{d,4}(1/2)=\frac{d^2-18d+8}{16(d^2-1)},\qquad v=P_{d,4}(0)=\frac3{d^2-1}.
\]
Since \(P_{d,4}\) is even, all distinct pairs with one common coordinate have Gram entry \(u\), independent of their signs. Distinct points on the same support, and points with disjoint supports, have entry \(v\).

**2. Symmetric and antisymmetric sign sectors.** Decompose \(\mathbb C^{X_d}\) orthogonally into functions antisymmetric or symmetric under \(s\mapsto-s\) on every unordered support \(\{i,j\}\). The antisymmetric sector has dimension \(\binom d2\), and every vector there has eigenvalue \(1-v=A_d\): contributions from different supports cancel, and the same-support \(2\times2\) block has diagonal \(1\), off-diagonal \(v\).

Identify the symmetric sector with \(\mathbb C^{\binom d2}\) using orthonormal pair-sum vectors. Its matrix \(H\) is \(1+v\) on the diagonal, \(2u\) for supports meeting in one index, and \(2v\) for disjoint supports. In terms of the adjacency matrix \(J_1\) of the Johnson graph on two-subsets and its disjointness matrix \(J_2\),
\[
 H=(1+v)I+2uJ_1+2vJ_2.
\]

**3. Exact Johnson decomposition.** The two-subset space is the orthogonal sum of constants (dimension one); the standard vertex-incidence subspace \(\{b_{ij}=a_i+a_j:\sum_i a_i=0\}\) (dimension \(d-1\)); and the common-vertex-sums-zero complement (dimension \(d(d-3)/2\)). To verify these dimensions and eigenvalues directly, let \(B\) be the unsigned vertex-edge incidence matrix of the complete graph on \(d\) vertices. Then \(B^*B=2I+J_1\) and \(BB^*=(d-2)I+\mathbf1\mathbf1^*\), so \(B\) has full row rank. Consequently \(J_1\) has eigenvalues \(2(d-2),d-4,-2\) on the three spaces. Because \(J_2=\mathbf1\mathbf1^*-I-J_1\), its eigenvalues are \(\binom{d-2}{2},-(d-3),1\). Substitution gives
\[
 \begin{aligned}
 B_d&=1+v+4(d-2)u+(d-2)(d-3)v,\\
 C_d&=1+v+2(d-4)u-2(d-3)v,\\
 D_d&=1+3v-4u.
 \end{aligned}
\]
Inserting the displayed rational \(u,v\) and factoring yields the three closed forms in the theorem, with the stated multiplicities. These multiplicities sum to \(d(d-1)\), exhausting the Gram spectrum.

**4. Rank and obstruction.** For integers \(d\ge5\), the quantities \(A_d,B_d,D_d\) are strictly positive. The only zero of \(C_d\) occurs at \(d=8\), where its standard subspace has dimension seven, yielding precisely the displayed nullspace and rank \(8\cdot7-7=49\). No other defects occur.

**5. Optimal uniform stability.** Regard the four rational eigenvalues as real functions of \(d\ge5\). One has \(A_d\ge7/8\) and \(D_d>3/4\). The function \(B_d\) increases strictly on \([5,\infty)\), since
\[
 \frac{dB_d}{dd}=\frac{(d-4)(d^3+4d^2+29d-4)}{4(d-1)^2(d+1)^2}>0,
\]
and it has minimum \(B_5=3/32\). For \(C_d\), direct differentiation yields
\[
 \frac{dC_d}{dd}=\frac{(d-8)(d^3+8d^2+29d+4)}{8(d-1)^2(d+1)^2}.
\]
It decreases on \([5,8]\) and increases on \([8,\infty)\). Among the admissible integer dimensions excluding the zero at eight, its minimum is \(\min\{C_7,C_9\}=\min\{3/128,11/640\}=11/640\). All other branches are strictly larger. The equality at \(d=9\) is realized by a nonzero standard vertex-incidence vector. For onto maps, the minimum-norm interpolant is \(f=E_d^*G_d^{-1}y\) and has norm at most \(\|y\|/\sqrt{\lambda_{\min}(G_d)}\), proving the sharp norm estimate. The Moore-Penrose pseudoinverse gives the range statement at \(d=8\).

## Verification

The standalone `checker.py` uses exact rational arithmetic. It independently constructs the full Gram matrix from all normalized signed-pair inner products and checks every predicted eigenspace directly for dimensions \(3\) through \(12\), including all antisymmetric support vectors, standard incidence vectors, and four-cycle vectors in the edge space. It separately verifies rank and the claimed lower bound through dimension \(500\) by the closed forms; that finite range is a regression test only. Its recorded output is in `checker_output.txt`. The analytic Johnson decomposition and derivative inequalities prove the theorem for every integer \(d\ge5\).

## Relationship to prior work

Bannai, Okuda, and Tagami (2013) develop harmonic-index spherical designs and Gegenbauer reproducing kernels; their treatment supplies a classical starting point, not the degree-four type-\(D_d\) Gram spectrum or sharp sampling bounds. Zhu, Bannai, Bannai, Kim, and Yu (2015) analyze tight harmonic-index designs and related Gegenbauer criteria, but their stated classifications do not supply the present dimension-wise interpolation operator. Hirao, Nozaki, and Tasaka (2023) characterize the harmonic-design strength and uniqueness of the \(D_4\) root system, a different dimension that is deliberately excluded from the theorem. The signed-pair geometry, Johnson graph eigenvalues, and addition formula are classical; novelty is claimed only for the combined all-dimension degree-four sampling classification, the seven-dimensional dimension-eight obstruction, and the sharp dimension-uniform interpolation constant.

## Limitations

No assertion concerns degrees other than four, arbitrary subsets of roots, perturbed roots, or optimal stability under alternative normalizations. The formula follows by a short exact association-scheme computation, so a broader published spectral statement for the signed-pair root association scheme could subsume it; this publication-priority risk has not been eliminated by targeted searches. It is a self-review, not an independent audit. Numeric tests are not the infinite-dimensional proof. The known dimension-four root configuration is outside the claimed domain.

## References

1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index \(t\)*, arXiv:1308.5101v1 (first public August 23, 2013), https://arxiv.org/abs/1308.5101 .
2. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index \(t\)*, arXiv:1507.05373v1 (first public July 20, 2015), https://arxiv.org/abs/1507.05373 .
3. M. Hirao, H. Nozaki, K. Tasaka, *Spherical designs and modular forms of the \(D_4\) lattice*, arXiv:2303.09000v3 (originally public March 16, 2023), https://arxiv.org/abs/2303.09000 .
4. Classical Johnson association-scheme eigenvalues for two-subsets, derived from the unsigned complete-graph incidence matrix in the proof.
