# Automorphism Orders of Radical-Square-Zero Quiver Algebras

## Finding

For every finite quiver \(Q=(Q_0,Q_1,s,t)\) and finite field \(k=\mathbb F_q\), let \(J\) be the arrow ideal and \(A=kQ/J^2\). Write \(m_{uv}=|\{\alpha\in Q_1:s(\alpha)=u,\ t(\alpha)=v\}|\), \(E=|Q_1|\), \(L=\sum_{v\in Q_0}m_{vv}\), and \(\Gamma_Q=\{\sigma\in\operatorname{Sym}(Q_0):m_{uv}=m_{\sigma(u)\sigma(v)}\text{ for all }u,v\}\). The map induced on \(A/J\) has image \(\Gamma_Q\), its kernel is isomorphic to \((J/(Z(A)\cap J),+)\rtimes\prod_{u,v\in Q_0}\operatorname{GL}_{m_{uv}}(k)\), and hence \(\left|\operatorname{Aut}_{k\text{-alg}}(A)\right|=q^{E-L}|\Gamma_Q|\prod_{u,v\in Q_0}|\operatorname{GL}_{m_{uv}}(\mathbb F_q)|\), with \(\operatorname{GL}_0(\mathbb F_q)\) trivial.

Here \(\Gamma_Q\) counts only vertex permutations preserving the arrow-multiplicity matrix; permutations and linear changes inside each arrow block are already counted by the general linear group factors.

## Assumptions and scope

The quiver is finite and may have loops, parallel arrows, isolated vertices, or disconnected components. The algebra is the split path-algebra quotient \(A=\mathbb F_q Q/J^2\), and automorphisms are required to be \(\mathbb F_q\)-linear. Put \(m_{uv}=\dim_{\mathbb F_q}(e_uJe_v)\), \(E=|Q_1|\), and \(L=\sum_v m_{vv}\). By convention, \(\operatorname{{GL}}_0(\mathbb F_q)\) has order one.

## Proof

Let \(e_v\) be the vertex idempotents. Since \(J^2=0\), the radical is the arrow span, \(A/J\cong \mathbb F_q^{Q_0}\), and every product of two arrows is zero.

1. Any algebra automorphism preserves \(J\), so it induces an automorphism of \(A/J\). The primitive coordinate idempotents of \(A/J\) are permuted. If the induced permutation is \(\sigma\), then \(\dim(e_uJe_v)=\dim(e_{\sigma(u)}Je_{\sigma(v)})\), hence \(m_{uv}=m_{\sigma(u)\sigma(v)}\). Conversely, every such vertex permutation lifts: map each vertex idempotent to its permuted idempotent and choose any vector-space isomorphism on each arrow block. Therefore the image of the induced map is exactly \(\Gamma_Q\).

2. Let \(K\) be its kernel. For \(\phi\in K\), put \(f_v=\phi(e_v)\). Then \(f_v\equiv e_v\pmod J\), and \(u=\sum_v f_v e_v\equiv1\pmod J\) is a unit. Orthogonality gives \(f_vu=ue_v\), so \(f_v=ue_vu^{-1}\). Conjugating \(\phi\) by \(u^{-1}\) makes it fix every \(e_v\). Thus every element of \(K\) is a product of an inner automorphism induced by an element of \(1+J\) and an automorphism fixing all vertex idempotents.

3. An automorphism fixing all \(e_v\) preserves each block \(e_uJe_v\), and every independent invertible linear map on these blocks extends to such an automorphism. This subgroup therefore has order \(\prod_{u,v}|\operatorname{{GL}}_{m_{uv}}(\mathbb F_q)|\).

4. Because \(J^2=0\), the group \(1+J\) is additively isomorphic to \(J\) and has order \(q^E\). The subspace \(Z(A)\cap J\) is exactly the span of loops: loops commute with all vertex idempotents and all arrows, while a non-loop arrow fails to commute with at least one endpoint idempotent. Hence the inner automorphisms induced by \(1+J\) form a group of order \(q^{E-L}\), naturally isomorphic to the additive group \(J/(Z(A)\cap J)\). Its intersection with the subgroup fixing every \(e_v\) is trivial, since an inner automorphism fixing all \(e_v\) is induced by a central loop combination and is therefore the identity. The kernel is the indicated semidirect product.

5. The fibers of the induced map all have size \( |K| \). Multiplying by \( |\Gamma_Q| \) yields the stated order formula.

## Verification

The symbolic proof handles arbitrary finite \(Q\) and arbitrary prime powers \(q\). The included verifier exhaustively enumerates all invertible linear maps over \(\mathbb F_2\) for six small quivers. The observed and predicted automorphism-group orders agree: one arrow, 2; two parallel arrows, 24; a directed 2-cycle, 8; one loop plus one non-loop arrow, 2; two isolated vertices, 2; one vertex with two loops, 6. These finite checks corroborate the proof but do not replace it.

## Relationship to prior work

Adachi’s 2014 preprint studies \(\tau\)-rigid-finiteness for algebras with radical square zero using separated quivers. Nasr-Isfahani’s 2016 preprint studies singular equivalence for quotients \(kQ/J^2\). The inspected main statements concern representation-theoretic and singular-equivalence invariants, not the automorphism-group kernel or its finite-field order. A nearby published result on truncated coordinate-cross algebras gives an automorphism formula for a special family; its one-vertex square-zero case is recovered here, but it does not cover arbitrary quivers with arbitrary arrow multiplicities and vertex symmetries.

## Limitations

The formula concerns \(\mathbb F_q\)-linear automorphisms of the split algebra \(\mathbb F_qQ/J^2\). It does not count semilinear ring automorphisms, algebras with nonsplit semisimple quotient, or arbitrary radical-square-zero algebras whose semisimple quotient is not a product of copies of \(\mathbb F_q\). The literature search did not establish absolute novelty; a formula stated as folklore in an unindexed source remains a residual risk. Independent audit has not been performed.

## References

1. Takahide Adachi, “Characterizing \(\tau\)-rigid-finite algebras with radical square zero,” arXiv:1401.1438, first posted 2014-01-07. https://arxiv.org/abs/1401.1438.
2. Alireza Nasr-Isfahani, “Singular equivalence of finite dimensional algebras with radical square zero,” arXiv:1603.04191, first posted 2016-03-14. https://arxiv.org/abs/1603.04191.
