# Affine-plane fibers of diagonalizable square-zero perturbations of a three-dimensional Jordan block

## Finding
Let \(K=\mathbb F_q\), where \(q\) is an even prime power, and let \(J=J_3(0)\) be the three-dimensional regular nilpotent Jordan matrix with ones on the first superdiagonal. Put
\[
\mathcal D_J=\{N\in M_3(K):N^2=0,\ J+N\text{ is diagonalizable over }K\}.
\]
For a monic cubic \(f(T)\) split into three **distinct** linear factors over \(K\), its spectral fiber
\[
\mathcal D_J(f)=\{N\in\mathcal D_J:\det(TI_3-(J+N))=f(T)\}
\]
is nonempty exactly when the sum of its three roots is zero. In that case its constant coefficient is nonzero and \(\mathcal D_J(f)\) is isomorphic, by explicit polynomial mutually inverse coordinate maps, to the affine plane \(\mathbb A_K^2\). No repeated-root spectrum occurs in \(\mathcal D_J\).

Consequently, the exact number of decompositions \(J=D+N\) with \(D\) diagonalizable over \(K\) and \(N^2=0\), counting actual ordered summands (not similarity classes), is
\[
\boxed{\#\mathcal D_J=\frac{q^2(q-1)(q-2)}6}.\tag{1}
\]
For \(q=2\) the set is empty. For \(q=4,8,16\), it has respectively \(16,448,8960\) elements. For \(q\to\infty\) over powers of two, the fraction of all square-zero \(3\times3\) matrices \(N\) with \(J+N\) diagonalizable tends to \(1/6\).

## Assumptions and scope
Characteristic is exactly two; \(K\) is a finite field of order \(q=2^m\), \(m\ge1\). The Jordan block is
\[
J=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}.
\]
Diagonalizability is over the *ground field* \(K\), not its algebraic closure. A square-zero perturbation means \(N^2=0\), not merely nilpotence. The map from perturbations to decompositions \(N\mapsto(D=J+N,N)\) is bijective in characteristic two. Every asserted count is for labeled matrices in this fixed basis. An affine-plane fiber means a scheme-theoretic polynomial parametrization with polynomial inverse after its characteristic-polynomial coefficients are fixed.

## Proof
**1. The only possible spectra are three distinct roots.** Since \(\operatorname{tr}J=0\) and a square-zero matrix is nilpotent, \(\operatorname{tr}(J+N)=0\). In dimension three a nonzero square-zero matrix has rank one; if \(N=0\), the matrix \(J\) is not diagonalizable. Suppose \(D=J+N\) is diagonalizable with a repeated eigenvalue. In characteristic two, trace zero forces its eigenvalue multiset either to be \(\{0,0,0\}\), or to be \(\{\lambda,\lambda,0\}\) with \(\lambda\ne0\). In the first case diagonalizability gives \(D=0\), hence \(N=J\), whose square is nonzero, a contradiction. In the second case \(D+\lambda I_3\) has rank one, while \(J+\lambda I_3\) is invertible. Since \(D+\lambda I_3=(J+\lambda I_3)+N\) and \(\operatorname{rank}N\le1\), the elementary rank inequality gives \(\operatorname{rank}(D+\lambda I_3)\ge2\), again a contradiction. Thus the eigenvalues are pairwise distinct. Their sum is zero; therefore none is zero (otherwise the other two would coincide). Conversely a matrix whose characteristic polynomial splits into distinct linear factors over \(K\) is diagonalizable over \(K\).

**2. A normal form for each characteristic-polynomial fiber.** A rank-one square-zero matrix has a presentation \(N=uv^{\mathsf T}\), with column vectors \(u,v\in K^3\) and \(v^{\mathsf T}u=0\). The determinant lemma, valid over every field, applied to \(TI_3-J\) shows that in characteristic two
\[
\det(TI_3-(J+N))=T^3+(v^{\mathsf T}Ju)T+v^{\mathsf T}J^2u.
\]
Indeed \((TI_3-J)^{-1}=T^{-1}I+T^{-2}J+T^{-3}J^2\) in the rational-function field, and \(v^{\mathsf T}u=0\) kills its quadratic term. Write the required polynomial as \(T^3+\alpha T+\beta\), \(\beta\ne0\). From \(v^{\mathsf T}J^2u=v_1u_3=\beta\), both \(v_1\) and \(u_3\) are nonzero. Rescale \(u,v\) uniquely so that \(u_3=1\). Put \(u=(x,y,1)^{\mathsf T}\). Then the conditions \(v^{\mathsf T}Ju=\alpha\) and \(v^{\mathsf T}u=0\) force
\[
 v=\begin{pmatrix}\beta\\ \alpha+\beta y\\ \beta x+\alpha y+\beta y^2\end{pmatrix}.
\]
Conversely, for each \((x,y)\in K^2\), these formulas give a rank-one square-zero \(N=uv^{\mathsf T}\) with that exact characteristic polynomial. Since \(N_{31}=\beta\), the coordinates can be recovered as \(x=N_{11}/\beta\), \(y=N_{21}/\beta\). This is a polynomial inverse over \(K\), proving a fiber isomorphic to \(\mathbb A_K^2\) and containing exactly \(q^2\) matrices.

**3. Count spectral fibers.** A triple of pairwise distinct elements of \(K\) with sum zero is exactly \(\{a,b,a+b\}\), where \(a\ne0\), \(b\ne0\), \(a\ne b\). Each unordered triple has six ordered enumerations. There are \((q-1)(q-2)/6\) triples. Their associated cubics are distinct, each with nonzero constant coefficient, and Step 2 contributes \(q^2\) matrices per triple. This proves (1), including integrality for even prime powers.

**4. Limiting probability.** A nonzero square-zero matrix in \(M_3(K)\) has rank one, and can be specified by a projective image line (\(q^2+q+1\) choices) and a nonzero linear functional annihilating the chosen image vector (\(q^2-1\) choices, after fixing one representative per line). Including zero, the total number of square-zero matrices is \(1+(q^2+q+1)(q^2-1)=q^4+q^3-q\). Divide (1) by this total to obtain the probability and limit \(1/6\).

## Verification
The accompanying self-contained `verify.py` implements arithmetic in fields of orders \(2,4,8,16\), directly enumerates the normalized rank-one square-zero matrices, computes characteristic polynomials by a full determinant expansion, and checks diagonalizability by summing eigenspace dimensions computed by Gaussian elimination. It independently confirms the determinant-lemma coefficients and exact cardinalities of every spectral fiber. Its recorded output was:

```
q=2: square_zero=22, diagonalizable_sums=0, distinct_spectra=0, fiber=4, PASS
q=4: square_zero=316, diagonalizable_sums=16, distinct_spectra=1, fiber=16, PASS
q=8: square_zero=4600, diagonalizable_sums=448, distinct_spectra=7, fiber=64, PASS
q=16: square_zero=69616, diagonalizable_sums=8960, distinct_spectra=35, fiber=256, PASS
VERIFY_OK
```

Run `python3 verify.py`. These four finite experiments are consistency checks; the general theorem is proved above for every even prime power.

## Relationship to prior work
Danchev, García, and Gómez Lozano established ground-field diagonalizable plus square-zero *existence* for matrices over sufficiently large finite fields in characteristic two (arXiv:2604.15286v1, first posted 16 April 2026), including an explicit nonderogatory three-dimensional construction. Their earlier decomposition paper gives an existence theorem in other field-size regimes. Those constructions provide at least one perturbation but do not classify all perturbations according to their characteristic polynomials or determine every fiber's affine geometry and cardinality. A published finite binary three-dimensional classification shows that \(J_3(0)\) does not decompose over \(\mathbb F_2\); that boundary is acknowledged rather than claimed as new. The result here counts and parametrizes all such decompositions uniformly across all even extension fields, refining the existence question for the canonical obstruction. No equivalent fiber-count theorem was identified in the checked sources.

## Limitations
The theorem is specific to a single regular nilpotent three-dimensional Jordan similarity class over finite fields of characteristic two, and does not count decompositions for all three-dimensional matrices. The finite-field count is not a classification up to simultaneous similarity. A plausible 2022 publisher article on matrix decompositions was accessible only via abstract and cross-referenced theorem statements; its complete text was not inspected, so older overlapping enumerations cannot be excluded definitively. The result does not claim historical uniqueness and has not been independently audited.

## References
1. P. Danchev, E. García, and M. Gómez Lozano, *Matrices over Finite Fields of Characteristic 2 as Sums of Diagonalizable and Square-Zero Matrices*, arXiv:2604.15286v1 (16 April 2026).
2. P. Danchev, E. García, and M. Gómez Lozano, *On some special matrix decompositions over fields and finite commutative rings*, arXiv:2106.10865 (2021).
3. P. Danchev, E. García, and M. Gómez Lozano, *Decompositions of matrices into diagonalizable and square-zero matrices*, Linear and Multilinear Algebra 70 (2022), 4056–4070, DOI 10.1080/03081087.2020.1862742.
4. *Exact three-by-three binary boundary for diagonalizable-plus-square-zero decomposition*, public mathematical record identifier `71d12e506077` (2026).
