# Simultaneous Peirce-operator normal forms in modular Alexander quandle algebras

## Finding

**Theorem.** Let \(p\) be a prime, \(d\ge 1\), \(K\) a field of characteristic \(p\), and \(V=\mathbb F_p^d\). Choose an arbitrary \(\alpha\in\operatorname{GL}_{\mathbb F_p}(V)\) and put \(\beta=I-\alpha\) (not necessarily invertible). Give the \(K\)-space \(A\) with basis \([v]\), \(v\in V\), the Alexander quandle-algebra multiplication \([v]\star[w]=[\alpha v+\beta w]\). On the same vector space let \(R=K[V]\) be the ordinary associative commutative group algebra, with its ordinary product written by juxtaposition. For a linear map \(\gamma:V\to V\), define \(T_\gamma([v])=[\gamma(v)]\). For \(u\in A\), put \(L_u(z)=u\star z\), \(R_u(z)=z\star u\), and let \(M_u(z)=uz\) denote ordinary multiplication.

Every idempotent of \(A\) is either zero or has augmentation one and is a unit of \(R\). For **every** nonzero idempotent \(u\), the same invertible operator \(M_u\) simultaneously conjugates its two Peirce multiplication operators:

\[
M_u^{-1}L_uM_u=T_\beta,\qquad M_u^{-1}R_uM_u=T_\alpha.
\]

In particular \(L_uR_u=R_uL_u\), and all nonzero idempotents have identical, explicitly computable **joint similarity type** of their left and right multiplication operators, even when \(\beta\) is singular or \(\alpha\) has order divisible by \(p\).

Define for a linear endomorphism \(\gamma\) and positive integer \(\ell\)
\[
c_\ell(\gamma)=\frac1\ell\sum_{s\mid\ell}\mu(\ell/s)\,p^{\dim_{\mathbb F_p}\ker(\gamma^s-I)}.
\]
This is the number of cycles of length \(\ell\) in the periodic part of the finite map \(\gamma:V\to V\). With \(r_j=\operatorname{rank}_{\mathbb F_p}(\beta^j)\) and \(r_0=d\), the characteristic polynomials are
\[
\chi_{R_u}(z)=\prod_{\ell\ge1}(z^\ell-1)^{c_\ell(\alpha)},\qquad
\chi_{L_u}(z)=z^{p^d-p^{r_d}}\prod_{\ell\ge1}(z^\ell-1)^{c_\ell(\beta)}.
\]
Both products have finite support. Moreover \(\operatorname{rank}_K(L_u^j)=p^{r_j}\) for every \(j\ge0\); hence the number of size-\(j\) zero-eigenvalue Jordan blocks in \(L_u\) is exactly
\[
b_j=p^{r_{j-1}}-2p^{r_j}+p^{r_{j+1}},\qquad 1\le j\le d.
\]
The remaining Jordan blocks are read off from cycles: a cycle of length \(\ell=p^h e\), \(p\nmid e\), contributes over an algebraic closure one block of size \(p^h\) for every \(e\)-th root of unity. The same cycle rule gives the entire Jordan form of \(R_u\). Thus **both complete Jordan forms**, not only the eigenvalue sets, are independent of the nonzero idempotent.

## Assumptions and scope

The ground field need only have characteristic \(p\), not necessarily be finite or algebraically closed. The vector group is elementary abelian and \(\alpha\) is invertible; \(\beta\) need not be. The zero idempotent is excluded from the similarity statement: both its multiplication operators are zero. Characteristic polynomials lie in \(K[z]\) and the Jordan-block statement is over an algebraic closure. Nonzero idempotents always exist because each basis element is one.

## Proof

1. **Pass to a commutative group algebra.** The bilinear multiplication in \(A\) satisfies the exact identity \(a\star b=T_\alpha(a)T_\beta(b)\) for all \(a,b\in R\), because it holds for basis elements. Both induced maps preserve ordinary augmentation \(\varepsilon:R\to K\) and the augmentation ideal \(J\).

2. **Exclude nonunits.** If \(u\star u=u\), augmentation gives \(\varepsilon(u)^2=\varepsilon(u)\), so \(\varepsilon(u)\in\{0,1\}\). If \(\varepsilon(u)=0\), then \(u\in J\) and the idempotency identity \(u=T_\alpha(u)T_\beta(u)\) puts \(u\) in \(J^2\). Inductively \(u\in J^{2^k}\) for every nonnegative integer \(k\). Writing \(R\cong K[t_1,\ldots,t_d]/(t_1^p-1,\ldots,t_d^p-1)\), with \(t_i-1\) the augmentation generators, shows \(J^{d(p-1)+1}=0\). Hence \(u=0\). Otherwise \(u=1+j\) with \(j\in J\), and the finite geometric series \(1-j+j^2-\cdots\) gives its inverse in \(R\).

3. **The same explicit conjugator on both sides.** If \(u\ne0\) is idempotent, the identity \(T_\alpha(u)T_\beta(u)=u\) holds in the commutative ring \(R\). Consequently \(T_\beta(u)=uT_\alpha(u)^{-1}\) and \(T_\alpha(u)=uT_\beta(u)^{-1}\). Thus for each \(z\in R\),
\[
R_u(z)=T_\alpha(z)T_\beta(u)=u\,T_\alpha(u^{-1}z)=M_uT_\alpha M_u^{-1}(z),
\]
and similarly \(L_u(z)=u\,T_\beta(u^{-1}z)=M_uT_\beta M_u^{-1}(z)\). The operators \(T_\alpha,T_\beta\) commute because \(\alpha\beta=\beta\alpha\), proving the joint commutation claim as well.

4. **The functional-map decomposition.** Relative to the group basis, \(T_\gamma\) is the linearization of the self-map \(v\mapsto\gamma v\) of the finite set \(V\). The induced linear map has rank equal to the number of distinct images, so \(\operatorname{rank}(T_\beta^j)=|\beta^jV|=p^{r_j}\). Since \(\beta^dV=\beta^{d+1}V\), the eventual permutation part acts on \(W=\beta^dV\), with \(|W|=p^{r_d}\); the complement has only zero as an eigenvalue. For any positive integer \(s\), fixed points of \(\gamma^s\) are exactly the vectors in \(\ker(\gamma^s-I)\). Möbius inversion of the counts of fixed points gives \(c_\ell(\gamma)\), and a cycle of length \(\ell\) has characteristic polynomial \(z^\ell-1\). This proves both characteristic-polynomial formulas.

5. **All Jordan blocks.** In the primary decomposition of \(T_\beta\), the invertible part has constant rank \(p^{r_d}\). If \(b_j\) is the number of zero Jordan blocks of size \(j\), then the ranks of consecutive powers satisfy \(b_j=\operatorname{rank}(T_\beta^{j-1})-2\operatorname{rank}(T_\beta^j)+\operatorname{rank}(T_\beta^{j+1})\). All zero blocks have size at most \(d\) by stabilization. Finally, over characteristic \(p\), \(z^{p^h e}-1=(z^e-1)^{p^h}\) with distinct roots for \(p\nmid e\), and the permutation matrix of one cycle is cyclic, giving exactly one block of size \(p^h\) at every \(e\)-th root. This completes the stated full Jordan form.

## Verification

The standalone script `verify_peirce_pairs.py` explicitly evaluates \(\star\) from the basis-operation table and independently evaluates ordinary group-algebra multiplication. It exhaustively enumerates all coefficient vectors over seven specified prime-field test cases, checks every discovered idempotent, proves computationally that every nonzero one has augmentation one and is an ordinary unit, and checks the left/right intertwining identities on every group-basis vector. Cases include invertible and singular \(\beta\), nonsemisimple \(\alpha\), and non-basis modular idempotents. It also checks the zero-Jordan-block formula from the rank sequence. The recorded output ends with `VERIFY_OK`.

For example, when \(p=3\), \(d=2\), and \(\alpha=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\), exactly \(243\) nonzero idempotents occur. Every one has left zero-Jordan blocks of sizes \(1\) (four blocks) and \(2\) (two blocks), together with a one-dimensional eigenvalue-one block; the right operator has three size-one and two size-three eigenvalue-one blocks. The first statement follows from the image counts \((9,3,1,1)\), while the second follows from three fixed vectors and two three-cycles. These calculations illustrate nonsemisimple Peirce structure without relying on numerical extrapolation for the theorem.

## Relationship to prior work

Elhamdadi, Nunez and Singh (2022) investigate Peirce operators for finite complex quandle algebras and give a general trace formula; their Section 7 calculates selected order-three examples. Zhang (2026) develops group-ring methods for Alexander quandle rings and obtains the complex right Peirce **eigenvalue set** for odd-order core quandles. The present result works in the distinct modular characteristic, permits all invertible Alexander parameters including non-Latin operations, and simultaneously determines the complete similarity types of both multiplication operators at **every** nonzero idempotent. Its primary contribution is the explicit shared-conjugator theorem and the consequent Jordan-block formulas, not previously known special eigenvalue sets or modular idempotent counts.

## Limitations

The result does not enumerate idempotents, classify arbitrary coefficient characteristics, or address nonabelian racks. Earlier algebra-isotope identities may subsume part of the shared-conjugator observation; historical priority remains subject to external specialist review. The 2026 Zhang paper's full text was not available in this inspection, so its exact overlap beyond the accessible abstract is a residual risk. Finite verification cannot certify the universal theorem independently; the proof above is symbolic.

## References

- M. Elhamdadi, B. Nunez and M. Singh, *Enhancements of link colorings via idempotents of quandle rings* (2022), arXiv:2207.09257, Section 7, DOI: 10.48550/arXiv.2207.09257.
- Z.-L. Zhang, *Group-ring methods for Alexander quandle rings* (first public October 6, 2026), arXiv:2610.08204.
- B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras* (2026), arXiv:2608.01550.
