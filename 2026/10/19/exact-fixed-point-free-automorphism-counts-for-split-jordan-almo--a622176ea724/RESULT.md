# Exact fixed-point-free automorphism counts for split-Jordan almost-abelian Lie algebras
## Finding
Let \(q\) be any prime power, let \(V\) be a nonzero \(N\)-dimensional vector space over \(\mathbb F_q\), and suppose that \(T\in\operatorname{GL}(V)\) has characteristic polynomial split over \(\mathbb F_q\). Define the centerless almost-abelian Lie algebra
\[
L_T=\mathbb F_q e\ltimes V,\qquad [e,v]=Tv,\quad [V,V]=0.
\]
For each \(\lambda\in\Lambda\subseteq\mathbb F_q^\times\), let \(m_{\lambda,j}\) be the multiplicity of the Jordan block of size \(j\) and eigenvalue \(\lambda\). Set \(\mathbf m_\lambda=(m_{\lambda,j})_{j\ge1}\). Define the **scalar stabilizer of Jordan types**
\[
G_T=\{a\in\mathbb F_q^\times:\mathbf m_{\lambda}=\mathbf m_{\lambda/a}\ \text{for all }\lambda\in\mathbb F_q^\times\},
\]
where absent eigenvalues have the zero Jordan partition. For any nonzero partition multiplicity vector \(\mathbf m=(m_j)\), put
\[
E(\mathbf m)=\sum_{i,j\ge1}\min(i,j)m_i m_j,\qquad
H_q(\mathbf m)=q^{E(\mathbf m)-\sum_jm_j^2}\prod_j|\operatorname{GL}_{m_j}(\mathbb F_q)|,
\]
\[
\delta_q(d)=\sum_{r=0}^{d}\frac{(-1)^r q^{\binom r2}}{|\operatorname{GL}_r(\mathbb F_q)|},\qquad
R_q(\mathbf m)=\prod_{j:m_j>0}\delta_q(m_j),
\]
with \(|\operatorname{GL}_0(\mathbb F_q)|=1\). For \(a\in G_T\), let \(\Lambda/\langle a\rangle\) denote the orbits of scalar multiplication by \(a\) on \(\Lambda\). Then the **exact number** of fixed-point-free Lie algebra automorphisms is
\[
\boxed{F(L_T)=q^N\!\left(\prod_{\lambda\in\Lambda}H_q(\mathbf m_\lambda)\right)
\sum_{a\in G_T\setminus\{1\}}\ \prod_{O\in\Lambda/\langle a\rangle}R_q(\mathbf m_{\lambda_O}),}
\]
where \(\lambda_O\) is any representative of \(O\). The total automorphism-group order is
\[
\boxed{|\operatorname{Aut}(L_T)|=q^N |G_T|\prod_{\lambda\in\Lambda}H_q(\mathbf m_\lambda).}
\]
Consequently, the proportion of fixed-point-free automorphisms is exactly
\[
\frac{1}{|G_T|}\sum_{a\in G_T\setminus\{1\}}\ \prod_{O\in\Lambda/\langle a\rangle}R_q(\mathbf m_{\lambda_O}).
\]
A fixed-point-free automorphism exists **if and only if** \(G_T\ne\{1\}\). The formula includes nonsemisimple Jordan types and all finite characteristics.

## Assumptions and scope
The field has order \(q\), not necessarily prime. The vector space \(V\) has positive finite dimension \(N\); \(T\) is invertible and its characteristic polynomial splits over the **base field**, but \(T\) need not be diagonalizable. An automorphism is fixed-point-free if \(\ker(\varphi-I)=0\). Jordan partitions are taken separately at each nonzero eigenvalue; factors with zero multiplicity are omitted. The zero-eigenvalue and nonsplit-primary cases are outside this claim.

For a positive integer \(d\), the standard factor in the formula is
\[
|\operatorname{GL}_d(\mathbb F_q)|=\prod_{i=0}^{d-1}(q^d-q^i).
\]
The rational number \(\delta_q(d)\) equals the proportion of invertible \(d\)-by-\(d\) matrices having no eigenvalue \(1\), and lies strictly between zero and one when \(q>2\) and \(d>0\).

## Proof
**1. Intrinsic block form.** Since \(T\) is onto, \([L_T,L_T]=V\). Thus every automorphism preserves \(V\) and uniquely has the form
\[
\varphi(e)=ae+w,\qquad\varphi|_V=S,\qquad a\in\mathbb F_q^\times,\ w\in V,\ S\in\operatorname{GL}(V).
\]
Preservation of the one nonzero bracket is equivalent to
\[
ST=aTS.\tag{1}
\]
Conversely, (1) is sufficient. In the decomposition \(\mathbb F_q e\oplus V\), \(\varphi-I\) is block triangular, so
\[
\varphi\text{ is fixed-point-free}\quad\Longleftrightarrow\quad a\ne1\ \text{and}\ \det(S-I)\ne0.\tag{2}
\]
There are \(q^N\) unrestricted choices of \(w\).

**2. Scalar orbits of Jordan types.** Equation (1) maps the generalized \(\lambda\)-eigenspace \(V_\lambda\) of \(T\) isomorphically to \(V_{\lambda/a}\), carrying each Jordan block of size \(j\) to a block of the same size (the nilpotent operator is scaled by the nonzero scalar \(a\)). Therefore such an \(S\) exists precisely when \(a\in G_T\). Fixing such an \(a\), each restriction from one \(V_\lambda\) to its successor is a torsor for
\[
C_\lambda=\operatorname{Aut}_{\mathbb F_q[u]}\left(\bigoplus_{j\ge1}(\mathbb F_q[u]/u^j)^{m_{\lambda,j}}\right).
\]
Hence there are exactly \(\prod_\lambda|C_\lambda|\) admissible intertwiners \(S\) for each \(a\in G_T\).

**3. Centralizer size and its eigenvalue-one test.** For a fixed multiplicity vector \(\mathbf m\), let \(M=\bigoplus_j(\mathbb F_q[u]/u^j)^{m_j}\) and \(E=\operatorname{End}_{\mathbb F_q[u]}(M)\). Each homomorphism from a block of length \(i\) to a block of length \(j\) is determined by \(\min(i,j)\) coefficients. Thus \(\dim_{\mathbb F_q}E=E(\mathbf m)\). The canonical map onto the same-length block-head matrices has nilpotent kernel \(J=\operatorname{rad}(E)\) and induces
\[
E/J\cong\prod_{j:m_j>0}M_{m_j}(\mathbb F_q).\tag{3}
\]
For completeness, the off-length maps lie in the radical because any round trip between unequal block lengths is divisible by \(u\) on its original block; same-length maps with zero constant coefficient are likewise divisible by \(u\). A sufficiently long composite of such radical maps vanishes, while arbitrary constant-term matrices among equal-length blocks lift. This establishes (3) and its nilpotence without any semisimplicity hypothesis on \(T\).

Taking units in (3) gives
\[
|C_\lambda|=q^{E(\mathbf m_\lambda)-\sum_jm_{\lambda,j}^2}\prod_j|\operatorname{GL}_{m_{\lambda,j}}(\mathbb F_q)|=H_q(\mathbf m_\lambda).\tag{4}
\]
For a unit \(P\in E\), the difference \(P-I\) is invertible as a linear operator on \(M\) exactly when it is a unit of \(E\), which by the nilpotence of \(J\) holds exactly when every component in (3) has no eigenvalue \(1\). As the fibers of \(C_\lambda\to\prod_j\operatorname{GL}_{m_j}(\mathbb F_q)\) are equinumerous, the proportion is
\[
\prod_{j:m_j>0}\delta_q(m_j)=R_q(\mathbf m).\tag{5}
\]
To compute \(\delta_q(d)\), apply Möbius inversion to the lattice of subspaces of \(\mathbb F_q^d\): a fixed \(r\)-space has \(q^{r(d-r)}|\operatorname{GL}_{d-r}(\mathbb F_q)|\) pointwise-fixing units, and its subspace-lattice Möbius coefficient is \((-1)^rq^{\binom r2}\). Summing over Gaussian-binomially many \(r\)-spaces yields precisely the displayed formula for \(\delta_q(d)\).

**4. Cyclic intertwiner blocks.** Fix \(a\in G_T\setminus\{1\}\) and one orbit \(O=(\lambda,\lambda/a,\ldots,\lambda/a^{s-1})\). The condition \(a^s=1\) holds because \(\lambda\ne0\). The map \(S\) cyclically permutes these \(s\) generalized eigenspaces. A fixed vector of \(S\) exists on their direct sum exactly when the return map \(P=S^s|_{V_\lambda}\) fixes a vector. Equation (1) implies \(P\in C_\lambda\). Choosing the first \(s-1\) intertwiners arbitrarily and varying the final intertwiner makes \(P\) range once over all of \(C_\lambda\). Hence the fraction of such cyclic intertwiners with no nonzero fixed vector is exactly \(R_q(\mathbf m_\lambda)\). Choices from distinct scalar orbits are independent. Combining this with (2), (4), and the unrestricted \(w\) gives both enumerations.

Finally, if \(G_T\ne\{1\}\) then \(q>2\); for every positive \(d\) a scalar matrix \(cI_d\) with \(c\in\mathbb F_q^\times\setminus\{1\}\) has no eigenvalue \(1\), so every \(\delta_q(d)>0\). Thus a nonidentity scalar symmetry contributes positively. If \(G_T=\{1\}\), equation (2) excludes all automorphisms. This proves the existence criterion.

## Verification
The standalone `verify.py` uses finite-field Gaussian elimination and independently checks the Lie bracket on all basis pairs for every invertible linear map in four small cases. It also enumerates centralizer units and eigenvalue-one exclusions for Jordan partitions \((2)\), \((2,1)\), \((1,1)\), plus both cyclic intertwiner families with block size \(1\) or \(2\) over \(\mathbb F_3\). All comparisons with the symbolic formula pass with `VERIFY_OK`. For \(T=\operatorname{diag}(1,2)\) over \(\mathbb F_3\), there are \(72\) automorphisms and \(18\) fixed-point-free ones. For \(T=J_2(1)\oplus J_2(2)\), there are \(5832\) automorphisms and \(1458\) fixed-point-free ones. For \(T=J_2(1)\oplus J_1(1)\oplus J_2(2)\oplus J_1(2)\), the formula gives \(17006112\) automorphisms, of which \(2125764\) are fixed-point-free.

The verifier's prime-field experiments do not enumerate all finite fields, all dimensions, or all Jordan partitions. The arbitrary-prime-power claim follows from the algebraic proof and standard finite local-endomorphism-ring structure.

## Relationship to prior work
Burde and Dekimpe (2026), Theorem 5.4, establish the existence criterion for **complex** centerless almost-abelian Lie algebras in terms of cyclotomic operators, without finite-field multiplicity counts. Avetisyan (2016/2022), Proposition 9, establishes the general block shape of almost-abelian Lie algebra automorphisms; this structural input is not claimed as new. The new count refines the finite-field case by combining scalar symmetry of complete Jordan partitions with the centralizer radical and linear-derangement factors. The already published calculation for the three-dimensional Heisenberg Lie algebra treats nilpotent defining \(T\) and does not imply the present invertible-\(T\) theorem; the published rank-only commutativity-spectrum theorem for almost-abelian Lie algebras concerns a different invariant. Searches for identical, equivalent and stronger finite-field enumerations did not find a published statement covering the displayed product-sum formula. A prior implicit derivation from general automorphism and finite-module literature remains possible.

## Limitations
The theorem excludes \(T\) with zero eigenvalues or nonsplit characteristic polynomial over \(\mathbb F_q\); it does not classify fixed-point-free automorphisms by finite order. The explicit formula depends on the complete Jordan partitions, not just eigenvalue multiplicities or rank. A historical equivalence formulated in terms of centralizers of primary modules could still predate this presentation. Finite code checks are consistency tests, not exhaustive proofs in unbounded dimension. Independent mathematical review has not been carried out.

## References
1. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916v1, 2026-04-30, Theorem 5.4, Section 5.
2. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365v2 (initial public version 2016-10-17); *International Journal of Mathematics* 33 (2022), article 2250057, Proposition 9.
3. *Exact fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra*, public mathematical research record 17f0de4cb789 (2026).
4. *Almost-abelian Lie algebras have rank-only commutativity spectra*, public mathematical research record fa54681b2170 (2026).
