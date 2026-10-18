# Exact tensor-resonance census for commuting algebra retractions

## Finding

Let \(q\) be any prime power, \(d\geq1\), \(k\geq1\), and let
\[
A=\mathbb F_q\langle x_1,\ldots,x_d\rangle/(x_1,\ldots,x_d)^3.
\]
This is the unital truncated free *noncommutative* associative algebra. Write \(J=(x_1,\ldots,x_d)\), \(V=J/J^2\cong\mathbb F_q^d\), and identify \(J^2\cong V\otimes V\). A retraction means a unital \(\mathbb F_q\)-algebra endomorphism \(e\) satisfying \(e^2=e\).

For each bit vector \(a\in\{0,1\}^k\), choose an integer \(r_a\geq0\) with \(\sum_a r_a=d\). Define bitwise AND \(b\wedge c\) by \((b\wedge c)_i=b_ic_i\), and set
\[
w_a=\sum_{b\wedge c=a}r_br_c,\qquad H(r)=\sum_{a\in\{0,1\}^k}r_aw_a.
\]
There are **exactly**
\[
\boxed{N_q(r)=\frac{|\operatorname{GL}_d(\mathbb F_q)|}{\prod_{a\in\{0,1\}^k}|\operatorname{GL}_{r_a}(\mathbb F_q)|}\,q^{d^3-H(r)}}
\]
ordered, pairwise-commuting \(k\)-tuples \((e_1,\ldots,e_k)\) of retractions with common tangent-space decomposition \(V=\bigoplus_a V_a\), where \(\dim V_a=r_a\) and \(e_i\) acts as multiplication by \(a_i\) on \(V_a\). The convention is \(|\operatorname{GL}_0(\mathbb F_q)|=1\). Every such tuple is conjugate by an algebra automorphism to the tuple of linear retractions on \(V\) induced by this decomposition. The \(r_a\) are complete conjugacy invariants. Thus the number of automorphism-conjugacy classes is
\[
\boxed{\binom{d+2^k-1}{2^k-1}}.
\]
For each subset \(S\subseteq\{1,\ldots,k\}\), define \(e_S=\prod_{i\in S}e_i\) (with the empty product the identity) and
\[
r_S=\sum_{a:\,a_i=1\ \forall i\in S}r_a.
\]
Then \(e_S\) is a retraction onto the intersection of the images of the \(e_i\) for \(i\in S\); its image is isomorphic to the same truncated free algebra on \(r_S\) generators and has precisely \(q^{1+r_S+r_S^2}\) elements. Hence \(N_q(r)\) is also a **complete joint image-intersection census**.

For the first nontrivial simultaneous case, \(d=k=2\), the total number of ordered commuting retraction pairs is
\[
\boxed{4+q(q+1)(5q^4+q^6)}.
\]
For \(q=2,3,5\), the values are respectively \(868\), \(13612\), and \(562504\).

## Assumptions and scope

All elements of the tuples are algebra endomorphisms of the fixed labelled algebra \(A\), not merely \(\mathbb F_q\)-linear endomorphisms. The endomorphisms preserve the unit and scalars. The tuple order matters, and conjugation is simultaneous by \(\operatorname{Aut}_{\mathbb F_q}(A)\). The statement holds in every characteristic, including characteristic two, because \(t^2-t\) has distinct roots over every field. No assertion is made about other truncation degrees.

## Proof

**1. Endomorphism coordinates.** Since \(J\) is the nilpotent radical of the local algebra \(A\), every unital algebra endomorphism preserves \(J\). Every choice of images for the generators in \(J\) gives a unique endomorphism, because every word of degree at least three vanishes. Thus an endomorphism \(e\) is uniquely described by linear maps \(F:V\to V\) and \(Q:V\to V\otimes V\), with \(e(v)=Fv+Qv\). On \(J=V\oplus(V\otimes V)\), its matrix is
\[
T(F,Q)=\begin{pmatrix}F&0\\Q&F\otimes F\end{pmatrix}.
\]
Composition of endomorphisms agrees with composition of these block operators on \(J\), and equality on \(J\) implies equality on \(A\). Hence \(e_i^2=e_i\) and \(e_ie_j=e_je_i\) hold if and only if the matrices \(T(F_i,Q_i)\) are commuting idempotents. In particular the \(F_i\) are commuting idempotents on \(V\).

**2. Common eigenvectors, including characteristic two.** The commuting projections \(F_1,\ldots,F_k\) determine the simultaneous eigenspace decomposition \(V=\bigoplus_{a\in\{0,1\}^k}V_a\). Indeed the algebra
\[
B=\mathbb F_q[t_1,\ldots,t_k]/(t_i^2-t_i\ :\ 1\le i\le k)
\]
is a product of \(2^k\) copies of \(\mathbb F_q\); the displayed generators commute. Every \(B\)-module is therefore semisimple. The action of \(T(F_i,Q_i)\) on \(J\) makes
\[
0\longrightarrow J^2\longrightarrow J\longrightarrow V\longrightarrow0
\]
a short exact sequence of \(B\)-modules. It admits a \(B\)-linear splitting. In the chosen word-degree decomposition, the splitting is a graph \(v\mapsto v+C(v)\) for some \(C\in\operatorname{Hom}(V,V\otimes V)\). Writing \(G_i=F_i\otimes F_i\), invariance of this graph is equivalent to
\[
\boxed{Q_i=CF_i-G_iC\quad\text{for every }i.}
\]
Conversely any choice of \(C\) and commuting idempotent \(F_i\) produces commuting idempotent \(T(F_i,Q_i)\): these operators are conjugate, by the invertible block matrix \(\left(\begin{smallmatrix}I&0\\C&I\end{smallmatrix}\right)\), to the diagonal operators \(\operatorname{diag}(F_i,G_i)\). That block matrix is induced by the actual algebra automorphism \(u_C:v\mapsto v+C(v)\), whose inverse is \(u_{-C}\), since \(J^3=0\). This proves simultaneous *algebraic* linearization, not only linear splitting.

**3. Exact number of nonlinear lifts.** With the \(F_i\) fixed, the \(k\)-tuple \((Q_i)\) is the image of the linear map
\[
\Phi:\operatorname{Hom}(V,V\otimes V)\longrightarrow \operatorname{Hom}(V,V\otimes V)^k,
\qquad C\longmapsto(CF_i-G_iC)_i.
\]
Its kernel is \(\operatorname{Hom}_B(V,V\otimes V)\). Under the simultaneous decomposition, the common \(a\)-eigenspace of \(V\otimes V\) has dimension \(w_a=\sum_{b\wedge c=a}r_br_c\), because \(G_i\) acts by \(b_ic_i\) on \(V_b\otimes V_c\). Therefore
\[
\dim\ker\Phi=\sum_a r_aw_a=H(r),\qquad \dim\operatorname{im}\Phi=d^3-H(r).
\]
The number of distinct compatible quadratic corrections is exactly \(q^{d^3-H(r)}\). This counts maps, not choices of the nonunique splitting \(C\).

**4. Tangent decompositions and conjugacy.** All ordered decompositions of a fixed \(d\)-space with dimensions \((r_a)\) form one \(\operatorname{GL}_d(\mathbb F_q)\)-orbit with stabilizer \(\prod_a\operatorname{GL}_{r_a}(\mathbb F_q)\). Multiplying this orbit size by the result of Step 3 proves \(N_q(r)\). The change of linear generators and the automorphisms \(u_C\) show that every tuple with fixed \((r_a)\) is simultaneously conjugate to the linear model. Different \((r_a)\) cannot be conjugate because tangent eigenspace dimensions are preserved. Counting weak compositions of \(d\) into \(2^k\) parts gives the orbit count.

**5. Intersections and small formula.** Products of commuting idempotents are idempotents whose images equal the intersections of the corresponding images. After conjugating to the linear model, \(e_S\) projects onto \(\bigoplus_{a:\,a_i=1\ \forall i\in S}V_a\). Its image has the free truncated word basis of degrees zero, one and two on that subspace, hence dimension \(1+r_S+r_S^2\), proving the cardinality assertion. For \(d=k=2\), four profiles concentrate both dimensions in a single bit pattern and each contributes one tuple. The remaining six profiles place one dimension in each of two different patterns, each having \(q(q+1)\) decompositions. The pairs of patterns \((00,01),(00,10),(00,11),(01,11),(10,11)\) have \(d^3-H=4\), while \((01,10)\) has \(d^3-H=6\). Summing yields \(4+q(q+1)(5q^4+q^6)\), as claimed.

## Verification

Execute the accompanying standalone file with `python3 check_commuting_retractions.py`. It requires Python 3 and no third-party packages. The checker enumerates all pairs of commuting idempotent tangent matrices in dimension two over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) (respectively 40, 76, and 184 ordered tangent pairs), forms the linear constraints for the two quadratic corrections directly from composition, and compares their independently row-reduced solution dimensions and the full joint-profile counts with the theorem. It also enumerates all 98 individual idempotent algebra endomorphisms in the binary dimension-two case and all their 9,604 ordered pairs, finding 868 commuting pairs. All comparisons pass. These are finite checks, not proofs for arbitrary fields or dimensions; the proof above supplies the general argument.

## Relationship to prior work

Ebrahim and Facchini (2023) examine idempotent pre-endomorphisms, a broader notion than genuine algebra endomorphisms, and relate an individual idempotent map to a kernel/image decomposition. That structural connection motivates the question here but their Theorem 6.1 does not give the tensor-resonance multiplicity formula or a census of arbitrary commuting tuples of associative-algebra retractions. Militaru (2021) gives a universal description of automorphism groups and gradings of finite-dimensional associative algebras; his conjugacy of group gradings differs from the present action of noninvertible commuting idempotent endomorphisms. Huang (2024) studies counting commuting matrix representations and finite-module enumerations, principally over commutative rings, rather than endomorphism tuples of this fixed noncommutative algebra. The linear-algebra fact that commuting idempotent operators split simultaneously is classical and is not claimed as new. The claimed contribution is their *algebraic* simultaneous linearization in this family and the explicit finite-field joint orbit/fiber formula with its tensor-product resonance statistic.

## Limitations

Originality is assessed against the identified and inspected sources, not certified against all historical literature; an equivalent formula may occur in older semisimple-representation or nilpotent-algebra work. The result concerns the particular cubically truncated free associative algebra and preserves labelled algebra generators; it makes no claim for arbitrary nilpotent algebras, arbitrary endomorphisms, higher powers of \(J\), or noncommuting retractions. Computational tests cover finite small cases only. Independent mathematical audit has not been performed.

## References

1. F. A. Ebrahim and A. Facchini, *Idempotent Pre-Endomorphisms of Algebras*, arXiv:2304.05079v1, publicly posted 2023-04-11, Sections 1 and 6. https://arxiv.org/abs/2304.05079
2. G. Militaru, *The automorphisms group and the classification of gradings of finite dimensional associative algebras*, arXiv:2105.12669v1, publicly posted 2021-05-26, especially Theorems 2.1 and 2.4. https://arxiv.org/abs/2105.12669
3. Y. Huang, *Commuting matrices via commuting endomorphisms*, arXiv:2404.19483v1, publicly posted 2024-04-30, Section 1. https://arxiv.org/abs/2404.19483
