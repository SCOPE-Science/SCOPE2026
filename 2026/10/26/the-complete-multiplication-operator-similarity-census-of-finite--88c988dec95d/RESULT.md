# The complete multiplication-operator similarity census of finite-field permutation evolution algebras

## Finding
For every prime power \(q\), every permutation \(\pi\in S_n\), every nonzero weight vector \(a=(a_1,\ldots,a_n)\in(\mathbb F_q^\times)^n\), and every \(x\in E_{\pi,a}\), let \(L_x(y)=xy\). We determine **how many** \(x\) give each exact similarity class of \(L_x\) over \(\mathbb F_q\), not only the characteristic polynomial or the rank.

Write \(V_{d,c}=\mathbb F_q[t]/(t^d-c)\) for \(c\in\mathbb F_q^\times\); and for a partition \(\lambda\vdash d\), write \(N_\lambda=\bigoplus_{r\ge1}(\mathbb F_q[t]/(t^r))^{m_r(\lambda)}\), where \(m_r(\lambda)\) is the number of parts of size \(r\) and \(z=\ell(\lambda)=\sum_rm_r(\lambda)\). In the free commutative semiring of finite-dimensional \(\mathbb F_q[t]\)-module isomorphism classes, with basis elements \([M]\) and multiplication \([M][N]=[M\oplus N]\), define
\[
\mathcal C_{d,q}= (q-1)^{d-1}\sum_{c\in\mathbb F_q^\times}[V_{d,c}]
+\sum_{\lambda\vdash d}\frac{d(\ell(\lambda)-1)!}{\prod_{r\ge1}m_r(\lambda)!}(q-1)^{d-\ell(\lambda)}[N_\lambda].
\]
The factorial fraction is always integral. If the disjoint cycles of \(\pi\) have lengths \(d_1,\ldots,d_s\), then the **complete similarity distribution** is
\[
\boxed{\mathcal C_{E,q}=\mathcal C_{d_1,q}\cdots\mathcal C_{d_s,q}.}
\]
The coefficient of a module class \([M]\) is exactly the number of \(x\in E\) for which the \(\mathbb F_q[t]\)-module with \(t\) acting as \(L_x\) is isomorphic to \(M\). All nonzero weight choices give the **same** distribution. The formula includes every characteristic, even when \(\operatorname{char}\mathbb F_q\mid d\), so that \(t^d-c\) need not be separable.

This invariant is not complete for algebra isomorphism: over \(\mathbb F_7\), the two-dimensional algebras with \(e_1^2=e_2,\ e_2^2=c e_1\) for \(c=1\) and \(c=2\) have identical complete distributions, but have respectively \(4\) and \(1\) idempotents, hence are nonisomorphic.

## Assumptions and scope
Let \(n\ge1\). Define the commutative, not necessarily associative, evolution algebra \(E=E_{\pi,a}\) by the displayed basis multiplication and require every \(a_i\ne0\). An element \(x=\sum_i x_i e_i\) determines the \(\mathbb F_q\)-linear map \(L_x(y)=xy\). “Similarity class” always means ordinary \(\mathrm{GL}_n(\mathbb F_q)\)-conjugacy of linear operators, equivalently the **full** \(\mathbb F_q[t]\)-module structure on their underlying vector spaces. No splitting or semisimplicity is assumed. Repeated cycle components can yield coincident module types, in which case coefficients of identical basis terms in the stated semiring are combined.

## Proof
**1. One cycle and its weights.** Relabel the cycle as \(1\to2\to\cdots\to d\to1\), and put \(w_i=a_ix_i\). Relative to the natural basis,
\[
L_x(e_i)=w_i e_{i+1}\quad(1\le i<d),\qquad L_x(e_d)=w_d e_1.
\]
Multiplication by nonzero \(a_i\) is a bijection of \(\mathbb F_q\), so the vectors \((w_1,\ldots,w_d)\) range independently and uniformly over \(\mathbb F_q^d\), regardless of \(a\).

**2. No zero edge.** If every \(w_i\ne0\), then \(L_x^d=c\operatorname{id}\), where \(c=\prod_iw_i\ne0\). The vectors \(e_1,L_xe_1,\ldots,L_x^{d-1}e_1\) form a basis. Therefore \(e_1\) is a cyclic module generator and its annihilator is precisely \((t^d-c)\), proving the module is \(V_{d,c}\) even when the polynomial is inseparable. The product condition leaves \((q-1)^{d-1}\) choices of nonzero \(w_i\) for every fixed \(c\).

**3. At least one zero edge.** Let the zero edge positions be \(z\ge1\) distinct positions around the directed \(d\)-cycle. Cutting at each zero edge decomposes the weighted graph into \(z\) disjoint directed paths, with positive vertex lengths \(r_1,\ldots,r_z\) adding to \(d\). Each path has nonzero internal weights, removable by diagonal change of basis; its operator is one nilpotent Jordan block of size \(r_j\). Thus its module is \(N_\lambda\) for the sorted partition \(\lambda=(r_1,\ldots,r_z)\). The number of ordered \(z\)-tuples of positive run lengths with a fixed partition \(\lambda\) is \(z!/\prod_r m_r(\lambda)!\). Choosing one of \(d\) labeled zero edges as the distinguished starting point and then dividing by \(z\), because every resulting zero-edge set has exactly \(z\) choices of starting edge, yields exactly
\[
\frac{d}{z}\frac{z!}{\prod_r m_r(\lambda)!}=\frac{d(z-1)!}{\prod_r m_r(\lambda)!}
\]
zero-edge sets. Each such set admits \((q-1)^{d-z}\) assignments to nonzero edges. This proves every nilpotent term with its exact integer coefficient.

**4. Arbitrary permutation and normalization.** Distinct cycles of \(\pi\) support invariant direct summands. Operators \(L_x\) restrict to the previously counted weighted cycles and their module classes add under direct sum. Disjoint coordinates vary independently, hence their class-counting polynomials multiply. There are no hidden overlapping cycle interactions, and coincidence of module isomorphism classes is handled by collecting formal like terms. As a numerical check, evaluating every module symbol at \(1\) yields \(q^{d}\) on one cycle and \(q^{n}\) for the full permutation.

**5. The isomorphism obstruction.** Over \(\mathbb F_7\) put \(E_c:\ e_1^2=e_2,\ e_2^2=c e_1\) with \(c\in\{1,2\}\). An element \(x=u e_1+v e_2\) is idempotent exactly when \(u=cv^2,\ v=u^2\). Besides \(u=v=0\), solutions require \(u^3=c^{-1}\). The nonzero cubes of \(\mathbb F_7\) are precisely \(\{1,6\}\), and each has three cube roots. Hence \(E_1\) has four idempotents, whereas \(E_2\) has only zero. They cannot be isomorphic. However, all \(L_{u e_1+v e_2}\) are precisely the matrices \(\begin{pmatrix}0&cv\\u&0\end{pmatrix}\), each exactly once as \((u,v)\) range over \(\mathbb F_7^2\). The operator pencils are therefore identical as multisets, so their similarity-class distributions coincide.

## Verification
The accompanying standalone `verify_operator_census.py` computes the predicted single-cycle multiplicities directly from integer factorials and independently enumerates all element coordinates for 34 prime-field parameter instances: \(q=2\), \(1\le d\le8\); \(q=3\), \(1\le d\le6\); \(q=5\), \(1\le d\le4\); \(q=7\), \(1\le d\le3\), with one or two distinct nonzero coefficient vectors per dimension. For singular operators it computes ranks of powers over the field and reconstructs nilpotent Jordan partitions by second rank differences; for invertible operators it records the cycle-product parameter. The script confirms exact equality of the full class histograms, total counts, and the \(\mathbb F_7\) idempotent obstruction. These finite checks are not used as a proof for arbitrary finite fields.

## Relationship to prior work
Khudoyberdiyev–Omirov–Qaralleh (2013), Sections 2–4, define single-permutation evolution algebras and multiplication operators and study decomposition, idempotents, and their associative enveloping algebra. This work supplies the natural objects and confirms that the **multiplication-operator family** is prior; its results examined do not give the number of elements realizing each similarity module. Narkuziyev (2018, 2020) studies idempotents, absolute nilpotents, and decompositions for a broader two-permutation construction, rather than full finite-field similarity-class counts. Paniello (2021), Example 2.4 and its operator discussion, treats Markov evolution algebras and permutation examples over the reals; it does not state the present finite-field partition-weighted distribution. Costoya and coauthors (2022) treat automorphism groups of Cayley evolution algebras, a different invariant. Wei–Zou (2023) study isomorphism classes of low-dimensional idempotent evolution algebras, not the distribution of all multiplication-operator rational canonical types. In all cases, these are **claim-to-claim** comparisons, not assertions of bibliographic exhaustiveness. Classical cyclic weighted-shift and Jordan-chain linear algebra underlies Steps 2 and 3; the new claimed output is the consolidated full finite-field algebraic operator-census formula and its algebra-isomorphism obstruction.

## Limitations
The theorem applies to **nonzero** structural weights and exactly one permutation per basis square; coefficients are uniform over all \(x\). It does not count arbitrary two-permutation evolution algebras, nonuniform sampling, or field-dependent algebra-isomorphism classes. The similarity census is insensitive to nonzero weights but does not classify algebras. Full prior-art exhaustiveness, including possible earlier equivalent weighted-monomial-matrix enumerations outside evolution-algebra terminology, is not claimed; priority should be independently checked. Computational verification covers specified prime fields, not all prime powers, and independent mathematical audit has not been performed.

## References
1. Khudoyberdiyev, A. Kh.; Omirov, B. A.; Qaralleh, I., *Few remarks on evolution algebras* (2013), arXiv:1307.0993; particularly Sections 2–4.
2. Narkuziyev, B. A., *On absolute nilpotent and idempotent elements of an evolution algebra corresponding to permutations* (2018), arXiv:1803.11415.
3. Narkuziyev, B. A., *Some remarks on evolution algebras corresponding to permutations* (2020), arXiv:2005.05793.
4. Paniello, I., *Markov evolution algebras* (first public 2021-02-28), DOI: 10.1080/03081087.2021.1893636.
5. Costoya et al., *Automorphism groups of Cayley evolution algebras* (first public 2022-07-04), arXiv:2207.01335.
6. Wei, Y.; Zou, Y., *Isomorphism classes of idempotent evolution algebras* (first public 2023-10-18), arXiv:2310.12368.
