# A modulo-four cycle law for minimum Walsh projection constants

## Finding
Let \(G=(V,E)\) be any finite connected simple unicyclic graph with \(m=|E|=|V|\ge3\), and let its unique simple cycle have length \(3\le\ell\le m\). On the sign cube \(\Omega_V=\{-1,1\}^V\), write \(\chi_{uv}(x)=x_ux_v\) for each edge \(uv\). The real Banach space \(W_G=\operatorname{span}\{\chi_{uv}:uv\in E\}\) carries the supremum norm inherited from \(C(\Omega_V)\). Its **absolute minimum projection constant** (and its relative projection constant in \(C(\Omega_V)\)) is
\[
\lambda(W_G)=B_m+\Delta_{m,\ell},\qquad
B_m=\frac{m}{2^{m-1}}\binom{m-1}{\lfloor(m-1)/2\rfloor}.
\]
For odd \(\ell\), \(\Delta_{m,\ell}=0\). For even \(\ell=2k\), put \(h=\lfloor m/2\rfloor\) and
\[
q_m=\begin{cases}
\displaystyle\frac{m}{2^m}\binom{m}{m/2},&m\text{ even},\\[3pt]
\displaystyle\frac{m+1}{2^m}\binom{m}{(m-1)/2},&m\text{ odd}.
\end{cases}
\qquad
\boxed{\Delta_{m,2k}=(-1)^{k-1}\frac{q_m}{2k-1}\frac{\binom hk}{\binom m{2k}}.}
\]
Thus the projection constant depends **only** on the edge count and unique cycle length, not the attached trees. Odd cycles give exactly the independent-sign baseline \(B_m\); cycles of length divisible by four lower the constant strictly; even cycles of length congruent to two modulo four raise it strictly. For example \(\lambda(W_{C_4})=1\), whereas the four-independent-character benchmark is \(3/2\); \(\lambda(W_{C_6})=9/4\), whereas its benchmark is \(15/8\). For each fixed even \(\ell=2k\), as \(m\to\infty\),
\[
\Delta_{m,2k}=(-1)^{k-1}\sqrt{\frac2\pi}(2k-3)!!\,m^{1/2-k}\bigl(1+O_k(m^{-1})\bigr).
\]
Here \((2k-3)!!=1\cdot3\cdots(2k-3)\). The same formulas hold for complex-valued functions and their complex Walsh subspaces.

## Assumptions and scope
Every graph is finite, undirected, connected, simple and has exactly one cycle; loops and multiple edges are excluded. The sign cube uses probability-normalized counting measure. The **absolute** projection constant is the supremum of least projection norms across all isometric embeddings of this Banach space into ambient Banach spaces. The **relative** constant is the least norm of a bounded linear projection \(C(\Omega_V)\to W_G\). The two constants coincide for the present Walsh subspace because of the standard invariant-subspace projection theorem (see first reference); the direct averaging argument below independently establishes relative minimality. Binomial coefficients have their usual integer meanings. The fixed-cycle asymptotic allows arbitrary attached trees and holds separately along either parity of \(m\).

## Proof
**1. Minimum projection norm.** Let \(H=\{-1,1\}^V\) act on \(C(\Omega_V)\) by translations \(U_yf(x)=f(xy)\), all isometries. The canonical Fourier projection \(P_Gf=\sum_{uv\in E}\widehat f(\{u,v\})\chi_{uv}\) has convolution kernel \(K_G(x)=\sum_{uv\in E}x_ux_v\). Its norm is \(\|P_G\|=\mathbb E|K_G|\): convolution gives the upper bound and the function \(f=\operatorname{sgn}K_G\), translated if necessary, attains it. Averaging an arbitrary projection onto \(W_G\) against every \(U_y\) preserves its range and does not increase its norm. Orthogonality of distinct characters forces the averaged projection to be \(P_G\), proving relative minimality. The known integral formula for absolute projection constants of Walsh-supported spaces (Defant et al., Theorem 3.1) identifies the absolute constant with the same integral. This last general equality, rather than its specialization to graphs, is prior work.

**2. Edge variables.** Given uniform vertex signs \(x_v\), set \(\eta_{uv}=x_ux_v\). The image of the map from vertex signs to edge signs is exactly the set of edge signings satisfying \(\prod_{e\in C}\eta_e=1\), where \(C\) is the unique cycle. Indeed, on a spanning tree the vertex signs are reconstructed from any chosen root sign, while the last edge imposes the one cycle relation. Every admissible edge assignment has exactly two preimages. For \(m\) independent fair edge signs \(\eta_1,\ldots,\eta_m\) and \(S_m=\sum_j\eta_j\), conditioning on the product of the \(\ell\) cyclic edge signs being \(+1\) therefore gives
\[
\lambda(W_G)=\mathbb E\left[|S_m|\left(1+\prod_{i=1}^{\ell}\eta_i\right)\right]
=\mathbb E|S_m|+\widehat{|S_m|}(\{1,\ldots,\ell\}).\tag{1}
\]
This also establishes dependence only on \((m,\ell)\). The first term is the classical binomial first absolute moment \(B_m\), obtained by summing the symmetric random walk distribution or by \(\mathbb E|S_m|-\mathbb E|S_{m-1}|=\Pr(S_{m-1}=0)\). If \(\ell\) is odd, simultaneous negation of all edge signs changes the cyclic product's sign and preserves \(|S_m|\), so the second term vanishes.

**3. The even-cycle correction.** Define \(L f(\eta)=\sum_{j=1}^m[f(\eta^{(j)})-f(\eta)]\), where \(\eta^{(j)}\) reverses the \(j\)-th sign. If \(m\) is even, a direct count of upward and downward flips gives
\[
(L+2)|S_m|=2m\,\mathbf1_{\{S_m=0\}}.
\]
If \(m\) is odd, the corresponding identity is
\[
(L+2)|S_m|=(m+1)\mathbf1_{\{|S_m|=1\}}.
\]
For a Walsh character \(\chi_A(\eta)=\prod_{j\in A}\eta_j\) with \(|A|=2k\), one has \(L\chi_A=-4k\chi_A\). Taking the Fourier coefficient on both sides of the displayed identities gives
\[
2(1-2k)\widehat{|S_m|}(A)=
\begin{cases}
2m\Pr(S_m=0)\mathbb E[\chi_A\mid S_m=0],&m\text{ even},\\
(m+1)\Pr(|S_m|=1)\mathbb E[\chi_A\mid |S_m|=1],&m\text{ odd}.
\end{cases}\tag{2}
\]
The conditional product moments are both exactly
\[
\mathbb E[\chi_A\mid S_m=0]\quad(m\text{ even}),\qquad
\mathbb E[\chi_A\mid |S_m|=1]\quad(m\text{ odd})
\quad=\quad(-1)^k\frac{\binom{\lfloor m/2\rfloor}{k}}{\binom m{2k}}.\tag{3}
\]
To verify (3) without asymptotics, when \(m=2h\) take the coefficient of degree \(2k\) in \((1+z)^h(1-z)^h=(1-z^2)^h\) and divide by \(\binom m{2k}\). When \(m=2h+1\), for \(S_m=+1\) take the same coefficient in \((1+z)^{h+1}(1-z)^h=(1+z)(1-z^2)^h\), and note that \(S_m=-1\) has the identical even-degree coefficient. Combining (2) and (3) gives the stated \(q_m\) and \(\Delta_{m,2k}\). All factors except \((-1)^{k-1}\) are positive, proving the strict modulo-four alternatives.

**4. Fixed-cycle scale.** Stirling's formula yields \(q_m=\sqrt{2m/\pi}\,(1+O(m^{-1}))\). At fixed \(k\), \(\binom{\lfloor m/2\rfloor}{k}/\binom m{2k}=(2k-1)!!\,m^{-k}(1+O_k(m^{-1}))\). Substitute in the exact correction, using \((2k-1)!!/(2k-1)=(2k-3)!!\). This completes the proof for both real and complex scalars.

## Verification
The accompanying standard-library `verify.py` calculates the formula using exact rational arithmetic, and enumerates every vertex sign assignment for a cycle with a pendant path, as well as the corresponding independent-edge Walsh moments. It checks all \(45\) pairs \((m,\ell)\) with \(3\le m\le11\) and \(3\le\ell\le m\), including \(\lambda(W_{C_4})=1\) and \(\lambda(W_{C_6})=9/4\). Executing `python3 verify.py` prints `UNICYCLIC_WALSH_EXACT_OK 45`. These finite tests corroborate but do not prove the all-size identity; the proof is the exact Fourier and conditional-counting argument above.

## Relationship to prior work
Defant, Galicer, Mansilla, Mastyło and Muro (arXiv:2302.00233, Theorem 3.1) already prove the projection-constant expectation formula for **every** Walsh spectral family, and obtain homogeneous-degree limits; the first step here is expressly not new. Their whole-text argument does not specialize to sparse graph-edge supports or give a cycle-length formula. Published related work on graph-supported quadratic Walsh polynomials gives sharp fourth-moment bounds and square localization, which are \(L^2\)-to-\(L^4\) questions about optimizing coefficients, not minimum \(L^\infty\) projections with unit coefficients. Similarly, homogeneous-degree-two projection results average over **all** pairs rather than a unicyclic graph's edges. The proposed contribution is the complete closed unicyclic evaluation, the exact modulo-four sign law, and quantified persistence/decay under adding tree edges.

## Limitations
The formula requires cyclomatic number one; multiple independent cycles lead to several interacting parity constraints and are not covered. It treats unweighted edge characters, not arbitrary coefficients or higher-degree graph interactions. The projection-kernel identity was already known; originality is limited to the graph-specific evaluation and classification. Earlier equivalent unicyclic formulas under Ising-energy or Boolean Fourier terminology are possible. No independent mathematical review is claimed.

## References
1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, and S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v1, first posted 2023-02-01, particularly Theorem 3.1 and Section 4; https://arxiv.org/html/2302.00233v2.
2. B. B. Bhattacharya, S. Das, S. Mukherjee, and S. Mukherjee, *Fluctuations of Quadratic Chaos*, arXiv:2203.02850v1, first posted 2022-03-06; https://arxiv.org/abs/2203.02850.
3. *Sharp fourth moments and square localization for graph-supported Walsh spaces*, published mathematical record 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-and-square-localization-for-graph-supported--0c3ab0087865.
4. *A lattice-phase second term for second-chaos projection constants on the Boolean cube*, published mathematical record 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-lattice-phase-second-term-for-second-chaos-projection-constant--ec79809353f9.
