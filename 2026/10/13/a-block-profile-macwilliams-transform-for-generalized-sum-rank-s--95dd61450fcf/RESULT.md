# A block-profile MacWilliams transform for generalized sum-rank subcode distributions

## Finding
Let \(q\) be a prime power, \(m\ge 1\), \(Q=q^m\), and let \(n_1,\ldots,n_\ell\) be positive integers with \(n_i\le m\) and \(n=\sum_{i=1}^{\ell}n_i\). For every \(\mathbb F_Q\)-linear code \(C\le\mathbb F_Q^n\) of dimension \(k\), its complete joint distribution of dimensions of blockwise \(\mathbb F_q\)-supports of all linear subcodes determines, by the explicit finite transformation below, the corresponding distribution of its Euclidean dual \(C^\perp\). This applies to arbitrary linear codes, not just MSRD codes.

For a support-dimension profile \(\mathbf s=(s_1,\ldots,s_\ell)\), \(0\le s_i\le n_i\), define the Gaussian-binomial moment counts
\[
B_r(C,\mathbf s)=\sum_{\substack{L_i\le \mathbb F_q^{n_i}\\\dim_qL_i=s_i}}G_Q\!\left(\dim_Q(C\cap V_{\mathbf L}),r\right),
\qquad
\Psi_C(\mathbf s;z)=\sum_{r=0}^{k}Q^{\binom r2}B_r(C,\mathbf s)z^r.
\]
Here \(V_{\mathbf L}\) is the blockwise extension-of-scalars support space and \(G_z(a,b)\) is the Gaussian binomial coefficient. Put \(\mathbf n-\mathbf s=(n_1-s_1,\ldots,n_\ell-s_\ell)\), \(\delta=k+\sum_i s_i-n\), and \(P_d(z)=\prod_{j=0}^{d-1}(1+Q^jz)\) for nonnegative integer \(d\). Then
\[
\boxed{\quad
\Psi_C(\mathbf s;z)=P_\delta(z)\,\Psi_{C^\perp}(\mathbf n-\mathbf s;Q^\delta z)
\quad\text{when }\delta\ge0,\quad}
\]
whereas
\[
\boxed{\quad
\Psi_{C^\perp}(\mathbf n-\mathbf s;z)=P_{-\delta}(z)\,\Psi_C(\mathbf s;Q^{-\delta}z)
\quad\text{when }\delta<0.\quad}
\]

These are identities of polynomials with nonnegative integer coefficients. They determine the exact-support profile counts, since, if \(N_r(C,\mathbf t)\) counts \(r\)-dimensional \(\mathbb F_Q\)-subcodes with blockwise support dimensions \(\mathbf t\), then
\[
\boxed{\quad
B_r(C,\mathbf s)=\sum_{\mathbf 0\le\mathbf t\le\mathbf s}
N_r(C,\mathbf t)\prod_{i=1}^{\ell}G_q(n_i-t_i,s_i-t_i).\quad}
\]
The matrix of this last system is unitriangular for profiles ordered by total support dimension, so inversion is unique and integral. Together, these formulas give an explicit, reversible generalized sum-rank MacWilliams transform for **every** subcode dimension and every block-support profile.

## Assumptions and scope
Throughout, \(\mathbb F_q\subseteq\mathbb F_Q\) has extension degree \(m\), and \(C^\perp\) means the ordinary \(\mathbb F_Q\)-Euclidean dual. Choose an \(\mathbb F_q\)-basis matrix for each \(L_i\le\mathbb F_q^{n_i}\); its row span over \(\mathbb F_Q\) defines the \(i\)-th coordinate block of \(V_{\mathbf L}\). This is independent of the chosen basis and satisfies
\[
\dim_QV_{\mathbf L}=\sum_i\dim_qL_i,\qquad
V_{\mathbf L}^{\perp}=V_{\mathbf L^\perp}.
\]
For a subcode \(D\le C\), its support \(\operatorname{Supp}(D)\) is the smallest tuple of \(\mathbb F_q\)-subspaces whose extension-of-scalars space contains \(D\); equivalently each block is the row span of the coordinate matrices of all words of \(D\) in any extension-field basis. The number \(N_r(C,\mathbf t)\) counts distinct subcodes, not their ordered generating sets. For integers \(0\le b\le a\), set
\[
G_z(a,b)=\prod_{j=0}^{b-1}\frac{z^{a-j}-1}{z^{b-j}-1},
\]
and take \(G_z(a,b)=0\) outside \(0\le b\le a\), with the empty product equal to one. The formulas include \(r=0\) by counting the zero subcode once, with zero support, and otherwise apply to every \(1\le r\le k\) or \(1\le r\le n-k\) as appropriate. The block lengths need not be equal.

## Proof
**Complementary shortening identity.** Fix \(\mathbf L\) and let \(s=\sum_i s_i\). The standard dimension formula and \(V_{\mathbf L}^\perp=V_{\mathbf L^\perp}\) give
\[
\begin{aligned}
\dim_Q(C\cap V_{\mathbf L})
&=\dim_Q C+\dim_QV_{\mathbf L}-\dim_Q(C+V_{\mathbf L})\\
&=k+s-n+\dim_Q(C^\perp\cap V_{\mathbf L^\perp}).
\end{aligned}
\]
Writing these two intersection dimensions as \(a\) and \(b\), respectively, shows \(a-b=\delta\), independent of the particular support tuple.

**The finite-dimensional subspace generating polynomial.** The Gaussian binomial theorem, with the convention \(G_Q(a,r)=0\) for \(r>a\), gives for every nonnegative integer \(a\)
\[
P_a(z)=\prod_{j=0}^{a-1}(1+Q^jz)
=\sum_{r=0}^{a}Q^{\binom r2}G_Q(a,r)z^r.
\]
Thus \(\Psi_C(\mathbf s;z)\) is precisely the sum of \(P_a(z)\) over all blockwise support tuples \(\mathbf L\) having profile \(\mathbf s\). If \(\delta\ge0\), then \(a=b+\delta\), so
\[
P_a(z)=P_\delta(z)P_b(Q^\delta z).
\]
Blockwise orthogonal complementation maps support tuples of profile \(\mathbf s\) bijectively onto tuples of profile \(\mathbf n-\mathbf s\). Summing the last factorization proves the first boxed identity. When \(\delta<0\), instead use \(b=a-\delta\) and the factorization \(P_b(z)=P_{-\delta}(z)P_a(Q^{-\delta}z)\); complementation proves the second identity. No division by a polynomial and no genericity assumption are involved.

**Recovering exact subcode supports.** Fix an \(r\)-dimensional subcode \(D\le C\) with exact support tuple \(\mathbf T\) having profile \(\mathbf t\). For a prescribed profile \(\mathbf s\ge\mathbf t\), the number of tuples \(\mathbf L\) having profile \(\mathbf s\) and containing \(\mathbf T\) is
\[
\prod_{i=1}^{\ell}G_q(n_i-t_i,s_i-t_i),
\]
since it amounts to choosing an \((s_i-t_i)\)-dimensional subspace of the quotient \(\mathbb F_q^{n_i}/T_i\) in each block. Count pairs \((D,\mathbf L)\) by first fixing \(\mathbf L\), giving \(B_r(C,\mathbf s)\), and then fixing \(D\), giving the third boxed identity. Its diagonal coefficients are exactly one, and all strictly lower terms involve a smaller total support dimension; recursive inversion therefore uniquely recovers \(N_r(C,\mathbf t)\). Applying the same inversion to the dual moments establishes the claimed full enumerator transformation.

For example, when \(\delta\ge0\), extracting the coefficient of \(z^r\) also yields the explicit nonnegative-moment relation
\[
B_r(C,\mathbf s)=\sum_{j=\max(0,r-\delta)}^{r}
Q^{j(\delta-r+j)}G_Q(\delta,r-j)
B_j(C^\perp,\mathbf n-\mathbf s),
\]
with out-of-range dual moments taken as zero. The negative-shift relation follows by exchanging the two codes.

## Verification
The standalone standard-library program `verify.py` implements exact arithmetic in \(\mathbb F_4\), constructs the two-dimensional code generated by \((1,0,\alpha,1)\) and \((0,\alpha,1,1)\), where \(\alpha^2+\alpha+1=0\), and independently enumerates its Euclidean dual. It enumerates all subcodes of dimensions zero, one and two, all 25 product support spaces for block sizes \((2,2)\), and all nine possible block-support dimension profiles. It independently checks the exact-support-to-moment double-counting identities and both signs and zero of the complementary-shift polynomial identity. The run prints `VERIFY_OK`. This finite check tests implementation and boundary cases; the universal claim follows from the proof, not from enumeration.

## Relationship to prior work
Molina's February 2026 paper proves MacWilliams identities for **generalized rank-weight** distributions, specifically a one-block support lattice, and explicitly identifies generalized sum-rank weight enumerators and corresponding MacWilliams identities as unanswered in its introduction. The present result retains each block-support dimension separately, rather than replacing the product support lattice by one rank parameter. Martínez-Peñas established sum-rank support spaces, complementary shortening dimensions, and duality in 2018. Those earlier dimension identities are an essential premise here, but do not themselves present the explicit all-subcode-dimensional polynomial transform and its invertible block-profile support enumerator reconstruction. Santonastaso and Sheekey present the sum-rank distribution of **codewords** and generalized-weight geometry; it does not count higher-dimensional subcodes. Xia and Fu derive distributions of codewords of quasi-MSRD codes and generalized minimum weights, rather than this arbitrary-code higher-subcode duality. The source and implication comparison is described further in `REVIEW.md`.

## Limitations
The identity concerns finite fields, extension-field-linear codes and the standard Euclidean dual; no assertion is made about nonlinear codes, arbitrary additive subgroups or Galois-twisted duals. The transform determines the dual enumerator from a known original enumerator; it does not determine either for an arbitrary code solely from length and dimension. It does not provide efficient evaluation of all enumerator coefficients for large parameters. The proof uses standard shortening duality and the Gaussian binomial theorem; whether an equivalent full multiblock transform appeared earlier in a different language remains a literature risk.

## References
1. Julien Molina, *MacWilliams identities for the generalized rank weights*, arXiv:2602.10929v1, 11 February 2026, especially Introduction/Table 3 and Theorem 3.10.
2. Umberto Martínez-Peñas, *Theory of supports for linear codes endowed with the sum-rank metric*, arXiv:1808.02468, 2018, especially Sections 2–4 and Proposition 2.
3. Paolo Santonastaso and John Sheekey, *On MSRD codes, h-designs and disjoint maximum scattered linear sets*, arXiv:2308.00378v1, 2023, especially Section 2.5.
4. Eduardo Camps-Moreno and coauthors, *Optimal anticodes, MSRD codes, and generalized weights in the sum-rank metric*, arXiv:2107.13611v1, 2021.
5. Qingfeng Xia and Fang-Wei Fu, *Quasi-MSRD Codes and Their Properties*, arXiv:2608.09085v1, 10 August 2026.
