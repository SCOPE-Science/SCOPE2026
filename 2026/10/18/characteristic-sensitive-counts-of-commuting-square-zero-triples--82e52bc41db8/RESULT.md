# Characteristic-sensitive counts of commuting square-zero triples in diamond incidence algebras

## Finding

Let \(q\) be any prime power and \(m\ge1\). Let \(P_m\) have unique bottom \(0\), unique top \(1\), and \(m\) incomparable elements \(z_1,\ldots,z_m\) strictly between them. Let \(J_m\) be the Jacobson radical of \(I(P_m,\mathbb F_q)\). Write \(T_m(q)\) for the number of **ordered** triples of elements of \(J_m\) that each square to zero and pairwise commute. This is also the count of such ordered triples in the full incidence algebra: every square-zero element has zero diagonal and is therefore in \(J_m\).

For \(s\in\{0,2,3\}\), define
\[
F_{m,q}(s)=\sum_{r=s}^{\min(m,3)}{3-s\brack r-s}_q
\left(\prod_{i=0}^{r-1}(q^m-q^i)\right)q^{3(m-r)},
\]
where the bracket is a Gaussian coefficient, an empty product is one, and an empty sum is zero. Set \(\delta_q=0\) in characteristic two and \(\delta_q=(q-1)^3\) in odd characteristic. Then
\[
\boxed{T_m(q)=q^3\bigl(F_{m,q}(0)+(q^3-1-\delta_q)F_{m,q}(2)+\delta_qF_{m,q}(3)\bigr).}
\]
This holds for all \(m\ge1\), including \(m<3\), and for nonprime finite fields.

## Assumptions and scope

The incidence-algebra units satisfy \(e_{xy}e_{uv}=\mathbf1_{y=u}e_{xv}\). The diagonal entries of a product are the coordinatewise products of the diagonal entries of its factors. In particular, if \(X^2=0\), every diagonal entry of \(X\) is zero because a field has no nonzero square-zero scalar. The kernel of the diagonal map is \(J_m\): it is a nilpotent ideal, and the diagonal quotient is a product of fields. Every radical element therefore has unique coordinates
\[
X(a,b,c)=\sum_{j=1}^m a_j e_{0z_j}+\sum_{j=1}^m b_j e_{z_j1}+c e_{01},
\qquad a,b\in\mathbb F_q^m,\quad c\in\mathbb F_q.
\]

## Proof

**Multiplication.** The matrix-unit law gives \(X(a,b,c)X(a',b',c')=(a\cdot b')e_{01}\). Stack \(a_1,a_2,a_3\) and \(b_1,b_2,b_3\) in the rows of \(3\times m\) matrices \(A,B\), respectively. Each \(X_i^2=0\) if and only if the corresponding diagonal entry of \(M=AB^{\mathsf T}\) is zero. Pairwise commutativity means that \(M\) is symmetric. The three \(c_i\) are independent free parameters, giving the multiplier \(q^3\).

**Rank law for hollow symmetric matrices.** The allowed matrices are
\[
M=\begin{pmatrix}0&u&v\\u&0&w\\v&w&0\end{pmatrix}.
\]
A nonzero off-diagonal entry gives a nonzero principal \(2\times2\) minor, so any nonzero \(M\) has rank at least two. The determinant is \(2uvw\); thus among the \(q^3\) matrices exactly one has rank zero, exactly \(\delta_q\) have rank three, and the remaining \(q^3-1-\delta_q\) have rank two. Although rank three cannot occur for \(AB^{\mathsf T}\) when \(m<3\), the fiber formula automatically assigns it weight zero.

**Factorization fiber.** Fix \(M\) of rank \(s\). If \(A\) has rank \(r\), its image \(U\subseteq\mathbb F_q^3\) must contain \(\operatorname{im}M\). There are \({3-s\brack r-s}_q\) choices of \(U\), and \(\prod_{i=0}^{r-1}(q^m-q^i)\) surjections \(\mathbb F_q^m\to U\), as counted by independent rows in a basis of \(U\). For each such \(A\), each column of \(B^{\mathsf T}\) has \(q^{m-r}\) possible values, because its image under \(A\) is prescribed and lies in \(U\). The three choices are independent, giving \(q^{3(m-r)}\). Summing proves the fiber formula. Applying the three rank frequencies and the free central multiplier yields \(T_m(q)\).

The characteristic correction comes from moving \((q-1)^3\) product matrices from the rank-two stratum of the formal alternating-matrix count to rank three in odd characteristic. For \(m\ge2\) the two weights differ by exactly the rank-two-\(A\) term
\[
F_{m,q}(2)-F_{m,q}(3)=(q^m-1)(q^m-q)q^{3(m-2)}.
\]
For \(m=1\) both weights are zero.

## Verification

The unchanged package scripts `artifacts/verify_diamond.py` and `artifacts/verify_gf4.py` implement exhaustive finite cases \((m,q)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2),(1,4)\), with polynomial-basis field multiplication for \(\mathbb F_4\). Examples are \(T_1(2)=120\), \(T_1(3)=1431\), \(T_2(2)=2528\), \(T_2(3)=135675\), and \(T_3(2)=77568\). The proof, not the finite tests, establishes the general formula. The equality of the full incidence-algebra count and the radical count is a diagonal calculation and needs no enumeration.

## Relationship to prior work and limitations

Quinn's incidence-algebra multiplication law is the structural input; the rank-frequency law and matrix fiber count use elementary linear algebra. Gargate and Gargate count involutions on rhombus-shaped posets in odd characteristic, a different equation. The rank-spectrum census for three-block parabolic radicals in Resultary record `d1f94ed041a2` includes the single-element square-zero count for the block sizes \((1,m,1)\), not the joint commuting conditions. The supported distinction is the joint, ordered triple count and its characteristic correction, not a new general matrix factorization formula or a result about all posets. The formula does not count triples without the commutativity condition, unordered triples, or larger tuples. The comparison with specialized literature is bounded; no publication priority is asserted.

## References

1. D. Quinn, “The incidence algebra of posets and acyclic categories,” *Kyushu J. Math.* **67** (2013), 117–127, Definition 2.5, https://doi.org/10.2206/kyushujm.67.117.
2. I. Gargate and M. Gargate, “Involutions on incidence algebras of finite posets,” arXiv:1907.06805v1, Theorem 1.3, https://arxiv.org/abs/1907.06805.
