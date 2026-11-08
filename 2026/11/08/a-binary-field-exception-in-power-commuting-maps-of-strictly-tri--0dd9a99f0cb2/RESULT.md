# A binary-field exception in power-commuting maps of strictly triangular matrices

## Finding
Let \(N_5(k)\) denote the algebra of strictly upper-triangular \(5\times5\) matrices over the finite field \(k=\mathbb F_q\). Let \(\mathcal P_q\) be the vector space of \(k\)-linear maps \(f:N_5(k)\to N_5(k)\) for which
\[
 [f(X),X^2]=0\quad\text{for every }X\in N_5(k).
\]
Write \(E_{ij}\) for a matrix unit, \(x_{ij}\) for the corresponding coordinate of \(X\), and
\[
\Psi=\operatorname{span}\{E_{14},E_{15},E_{24},E_{25}\}.
\]
For every \(q>2\), the *unique* description of \(\mathcal P_q\) is
\[
 f(X)=\lambda X+\mu(X),\quad \lambda\in k,\quad
 \mu\in\operatorname{Hom}_k(N_5(k),\Psi),
\]
so that \(\dim_k\mathcal P_q=41\) and \(|\mathcal P_q|=q^{41}\).

Over \(\mathbb F_2\) there are precisely four additional independent directions, namely
\[
\begin{aligned}
 T_1(X)&=(x_{34}+x_{45})E_{13},&T_2(X)&=(x_{34}+x_{45})E_{23},\\
 T_3(X)&=(x_{12}+x_{23})E_{34},&T_4(X)&=(x_{12}+x_{23})E_{35}.
\end{aligned}
\]
More precisely, every binary power-commuting map has the **unique** form
\[
 f(X)=\lambda X+\mu(X)+\sum_{a=1}^4\alpha_aT_a(X),
 \quad \lambda,\alpha_a\in\mathbb F_2,\quad
 \mu\in\operatorname{Hom}_{\mathbb F_2}(N_5,\Psi).
\]
Consequently \(\dim_{\mathbb F_2}\mathcal P_2=45\) and \(|\mathcal P_2|=2^{45}\). This is a field-size exception, not an exception for all fields of characteristic two: \(\mathbb F_4\) already has the standard dimension \(41\).

The four directions have analogues in every \(N_n(\mathbb F_2)\), \(n\ge5\): replace their respective outputs by \(E_{1,n-2}\), \(E_{2,n-2}\), \(E_{3,n-1}\), \(E_{3,n}\), and replace the terminal input coordinates by \(x_{n-2,n-1}+x_{n-1,n}\), leaving the initial input pair \(x_{12}+x_{23}\) unchanged. These are independent, nonstandard binary examples for all such sizes. **No complete higher-size classification is asserted here.**

## Assumptions and scope
All maps are linear over the specified ground field; the ring is nonunital and matrix multiplication is ordinary. The condition is *power commuting*, not commuting or centralizing: it is \([f(X),X^2]=0\), not \([f(X),X]=0\). Both scalar and map parameters in the displayed normal forms are unrestricted. The exact classification concerns matrix size five; the final construction is only an existence statement for larger sizes.

## Proof
First, \(\Psi N_5^2=N_5^2\Psi=0\). Thus every \(\mu\) with image in \(\Psi\), as well as every scalar multiple of the identity map, satisfies the equation. The corresponding \(40+1=41\) maps form a linearly independent family (their image coordinates outside \(\Psi\) separate the scalar map).

For the binary exception, matrix multiplication gives
\[
 E_{13}X^2=x_{34}x_{45}E_{15},\quad
 E_{23}X^2=x_{34}x_{45}E_{25},\quad
 X^2E_{34}=x_{12}x_{23}E_{14},\quad
 X^2E_{35}=x_{12}x_{23}E_{15},
\]
with the opposite products all zero. In \(\mathbb F_2\), \(ab(a+b)=0\) for all \(a,b\). Hence each \(T_a\) satisfies the original identity. The four output positions are mutually distinct and outside \(\Psi\); together with the scalar identity direction they give exactly \(45\) independent maps.

It remains to prove completeness, uniformly for all finite fields. Number the ten matrix units by the lexicographically ordered list
\[
 (12),(13),(14),(15),(23),(24),(25),(34),(35),(45).
\]
Expand \(f(E_v)=\sum_u c_{uv}E_u\), with \(100\) unknown coefficients. The \((i,j)\) coordinate of the defining identity is
\[
 [f(X),X^2]_{ij}=\sum_{i<a<b<j}
 \bigl(f_{ia}(X)x_{ab}x_{bj}-x_{ia}x_{ab}f_{bj}(X)\bigr).
\]
Collecting ordinary commuting degree-three monomials in the ten input coordinates produces an integral coefficient matrix \(C\) with \(93\) nonzero rows and \(100\) columns. The included exact certificate identifies a \(59\times59\) submatrix of determinant \(-1\). Thus \(\operatorname{rank}_k C\ge59\) over **every** field, not just the fields used for testing. The already constructed \(41\) independent solutions imply \(\operatorname{rank}_k C\le59\), hence equality over every field.

For \(q>2\), the polynomial \([f(X),X^2]_{ij}\) has degree at most two *in each individual input coordinate*. Since \(2<q\), the finite-field polynomial interpolation lemma says it vanishes at every input exactly when every formal coefficient vanishes. Thus its solution space is \(\ker C\), of dimension \(41\).

For \(q=2\), instead impose \(x_{ij}^2=x_{ij}\) and collect the resulting square-free monomials. This produces an \(83\times100\) binary coefficient matrix \(B\). The included certificate specifies a nonsingular \(55\times55\) binary submatrix, giving \(\operatorname{rank}B\ge55\). The \(45\) explicit independent maps found above give \(\operatorname{rank}B\le100-45=55\). Therefore the rank is exactly \(55\), proving completeness and uniqueness of the binary decomposition.

The certificates are integer and binary linear-algebra witnesses, not inferences from sample data: every entry of \(C\) and \(B\) is generated from the displayed multiplication formula by the supplied standalone code. The determinant is evaluated by exact integer Bareiss elimination; the binary minor by bitwise Gaussian elimination. For the higher-size construction, the only possibly nonzero commutator terms are the corresponding two endpoint products \(x_{n-2,n-1}x_{n-1,n}(x_{n-2,n-1}+x_{n-1,n})\) and \(x_{12}x_{23}(x_{12}+x_{23})\), which vanish over \(\mathbb F_2\).

## Verification
Run `python3 verify.py` in a directory containing `rank_certificate.json`; the program reconstructs the \(93\)- and \(83\)-row systems, verifies the unit determinant and invertible binary minor, checks the formal and binary ranks, and independently tests all \(45\) proposed solution vectors against the reduced system. Its expected final marker is `VERIFY_OK`.

Run `python3 verify_direct.py` in the same directory. This independent check enumerates all \(2^{10}=1024\) binary matrices, evaluates ordinary matrix multiplication for the original equation, confirms that the \(45\) exhibited linear maps obey it, and obtains a rank \(55\) pointwise linear constraint system. Its expected marker is `VERIFY_OK_DIRECT`. Both checks were executed from the included files. These exact finite computations establish the finite certificate, while the separate interpolation argument supplies the all-field conclusion for \(q>2\).

## Relationship to prior work
Bounds, *Centralizing maps on the ring of strictly upper triangular matrices*, arXiv:2301.03422, first publicly posted January 9, 2023, studies the same matrix algebra under a different functional identity. The paper's November 2025 revision, titled *Power commuting and centralizing maps on the ring of strictly upper triangular matrices*, Theorem 1.2, proves the standard form for power-commuting maps under **characteristic zero**. Its statement does not cover finite fields; its proof uses a division by two. The present theorem does not claim that characteristic-zero standard form as new. Rather, it proves the sharp all-finite-field dichotomy in size five and identifies the four genuinely binary directions.

Lan and Liu, *Commuting additive maps on upper triangular and strictly upper triangular infinite matrices*, Electronic Journal of Linear Algebra 40 (2024), 361–369, treats the stronger condition \([f(X),X]=0\) on infinite triangular rings, even over finite fields. It does not imply the classification for \([f(X),X^2]=0\) on finite \(5\times5\) niltriangular rings. Related work on bilinear commuting maps concerns a different equation and its cited 2025 preprint was withdrawn. Searches of the published mathematical records and the checked prior-claim collection did not identify a theorem furnishing the two kernel dimensions or these four explicit exceptional directions. Publication priority remains provisional.

## Limitations
This is a complete exact classification only at matrix size five. The all-size statement gives four independent nonstandard binary examples but does not establish their completeness in higher dimensions. The proof concerns field-linear maps, not arbitrary additive maps or arbitrary coefficient rings. The bibliographic overlap investigation is not a proof of global novelty; independent audit remains outstanding.

## References
1. J. Bounds, *Centralizing maps on the ring of strictly upper triangular matrices*, arXiv:2301.03422v1, January 9, 2023; revised title *Power commuting and centralizing maps on the ring of strictly upper triangular matrices*, arXiv:2301.03422v3, November 20, 2025, especially Theorem 1.2 and the proof in Sections 2–3. https://arxiv.org/abs/2301.03422.
2. D.-C. Lan and C.-K. Liu, *Commuting additive maps on upper triangular and strictly upper triangular infinite matrices*, Electronic Journal of Linear Algebra 40 (2024), 361–369, Theorem 1.1 and Corollary 1.2. https://journals.uwyo.edu/index.php/ela/article/view/8381.
3. J. Bounds, S. Dayton, R. Richardson, and Y. Yau, *Bilinear maps on the ring of strictly upper triangular matrices*, arXiv:2502.11263, withdrawn February 22, 2025. https://arxiv.org/abs/2502.11263.
