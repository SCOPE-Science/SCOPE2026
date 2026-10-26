# A linear–quadratic rank law for higher-distance hypercube parity dynamics

## Finding
For each integer \(n\ge4\), let the state space be the binary vector space of functions on \(\mathbb F_2^n\), of dimension \(N=2^n\). For every distance \(4\le d\le n\), define
\[
(F_{n,d}x)(v)=\sum_{w\in\mathbb F_2^n:\,d_H(v,w)=d}x(w)\pmod2.
\]
Set \(c_j=\binom{n-j}{d-j}\bmod2\) for \(j=0,1,2\), and \(U=F_{n,d}+c_0I\). Then \(U^2=0\). In the following two exhaustive cases of nonzero linear or quadratic jet,
\[
\operatorname{rank}_{\mathbb F_2}(U)=
\begin{cases}
2^{n-1},&c_1=1,\\
2^{n-1}-2^{(n-1)/2},&c_1=0,\ c_2=1.
\end{cases}
\]
The second case forces \(n\) odd. Writing this rank as \(r\), there are only two dynamical alternatives. If \(c_0=0\), every state reaches zero within two updates and the exact numbers of states whose first periodic-entry times are zero, one, and two are respectively
\[
1,\quad 2^{N-r}-1,\quad 2^N-2^{N-r}.
\]
If \(c_0=1\), every state is already periodic; the number of fixed states is \(2^{N-r}\), and the number of primitive two-cycles is \((2^N-2^{N-r})/2\).

As a uniform high-distance consequence, for \(n=2^a+1\), \(a\ge3\), all layers \(4\le d\le2^a-1\) have \((c_0,c_1,c_2)=(0,0,1)\), so their complete transient-depth counts agree despite differing adjacency graphs. Layer \(d=2^a\) instead has \((c_0,c_1,c_2)=(1,0,1)\), with the same shifted rank and an exact one-/two-cycle census. These conclusions hold at all such dimensions, not merely in sampled examples.

## Assumptions and scope
The graph is the simple distance-exactly-\(d\) Hamming graph on binary \(n\)-tuples. Arithmetic and states are over \(\mathbb F_2\). The theorem classifies all distances \(d\ge4\) for which \(c_1=1\) or \(c_1=0,c_2=1\); no rank formula is asserted for the remaining parameters \(c_1=c_2=0\). The distance-one through distance-three cases are deliberately excluded from the new high-distance assertion because earlier adjacency-code literature treats them.

## Proof
Let \(X_i\) denote translation by the \(i\)-th coordinate of \(\mathbb F_2^n\). The group algebra of the translations, acting on the regular representation of dimension \(N\), is
\[
R_n=\mathbb F_2[y_1,\ldots,y_n]/(y_1^2,\ldots,y_n^2),\qquad y_i=X_i+1.
\]
The distance-\(d\) adjacency operator is multiplication by
\[
a=\sum_{|S|=d}\prod_{i\in S}(1+y_i)
=\sum_{j=0}^d\left(\binom{n-j}{d-j}\bmod2\right)e_j(y).
\]
Thus its scalar term is \(c_0\), its linear term is \(c_1e_1\), and its quadratic term is \(c_2e_2\). Because every positive-degree element of \(R_n\) has square zero in characteristic two, \(U^2=0\).

Suppose \(c_1=1\). The linear part of the multiplication element \(u=a+c_0\) is \(e_1(y)\), which is nonzero. Any replacement of a coordinate by an element with nonzero linear coefficient extends (after choosing the remaining linear coordinates) to an automorphism of this finite filtered square-zero algebra: it induces an invertible map modulo the ideal of terms of degree at least two; successive ideal powers force surjectivity, hence bijectivity. Consequently multiplication by \(u\) is conjugate, as a linear map on the regular module, to multiplication by a coordinate \(y_1\). Exactly half the standard squarefree monomials are in its image, giving rank \(2^{n-1}\).

Now suppose \(c_1=0,c_2=1\). We first show \(n\) is odd. If \(n\) were even and \(d\) odd, then \(\binom{n-2}{d-2}\) would be even because its upper index is even and its lower index odd (Lucas' theorem). If \(n\) were even and \(d\) even, Pascal's identity and the same parity observation would give \(c_1=c_2\). Both contradict \((c_1,c_2)=(0,1)\).

Write \(n=2m+1\). The quadratic part \(q=e_2(y)\) has polar form with off-diagonal matrix entries one and diagonal entries zero, namely \(J+I\), of rank \(n-1=2m\). A linear coordinate change of \(R_n\) (valid because the square of any linear form is zero) puts this quadratic part into the standard form
\[
q=u_1v_1+\cdots+u_mv_m,
\]
with one radical coordinate \(w\). Every term of degree at least three contains some active coordinate \(u_i\) or \(v_i\), since \(w^2=0\). Inductively remove the homogeneous degree-\(k\) part of \(u-q\), for each \(k\ge3\), by replacing the active coordinates with themselves plus homogeneous polynomials of degree \(k-1\): a monomial of degree \(k\) divisible by \(u_i\) (respectively \(v_i\)) is introduced or cancelled through the \(u_iv_i\) term by altering \(v_i\) (respectively \(u_i\)). Corrections quadratic in those substitutions have degree \(2k-2\ge k+1\), so earlier homogeneous terms stay fixed. All substitutions induce the identity on linear terms and hence are algebra automorphisms. The finite filtration therefore conjugates multiplication by \(u\) to multiplication by \(q\).

To calculate its rank, classify a squarefree monomial by the \(t\) active pairs for which it contains either both members or neither member. At each of the remaining \(m-t\) pairs it contains exactly one member, with \(2^{m-t}\) choices. For fixed such choices and a fixed set of \(t\) active pairs, multiplication by \(q\) acts on \(\mathbb F_2[z_1,\ldots,z_t]/(z_i^2)\) as multiplication by \(z_1+\cdots+z_t\), of rank \(2^{t-1}\) if \(t\ge1\), or zero for \(t=0\). The unused variable \(w\) doubles all dimensions. Therefore
\[
\operatorname{rank}(U)=2\sum_{t=1}^m\binom mt2^{m-t}2^{t-1}=4^m-2^m
=2^{n-1}-2^{(n-1)/2}.
\]

Finally, if \(c_0=0\) then \(F=U\) and \(F^2=0\). Its kernel has size \(2^{N-r}\); zero itself has entry time zero, the other kernel vectors have entry time one, and every vector outside the kernel has entry time two. If \(c_0=1\), then \(F=I+U\) and \(F^2=I\); its fixed vectors are exactly \(\ker U\), and every other point belongs to a primitive two-cycle.

For the stated dimension family \(n=2^a+1\), Lucas' theorem applied to the binary expansions of \(n,n-1,n-2\) gives \((c_0,c_1,c_2)=(0,0,1)\) for \(4\le d\le2^a-1\) and \((1,0,1)\) for \(d=2^a\), completing the proof.

## Verification
The accompanying standalone \(\texttt{verify.py}\) builds the exact binary adjacency matrix independently, computes its row rank over \(\mathbb F_2\) by integer-bit elimination, and checks all parameter pairs meeting either jet condition for \(2\le n\le10\). It reports \(\texttt{VERIFY_OK}\) with 45 eligible pairs. These calculations validate finite cases but are not substitutes for the unrestricted algebraic proof.

## Relationship to prior work
Fish, Key, and Mwambene (2009) investigate adjacency codes of the binary distance-\(d\) hypercube for \(d=1,2,3\); those cases are pre-existing and are not claimed here as new. Seneviratne (2016), Section 4, establishes the parity-square relation \(A^2\in\{0,I}\) for generalized hypercube adjacency matrices, and its introduction confirms the earlier three-distance range. That square relation alone supplies no rank of \(A+c_0I\) for higher distances, hence neither the exact finite-state counts nor the common-rank high-distance family here. Key, Fish, and Mwambene (2011) study codes of incidence matrices and line graphs of Hamming graphs, which are distinct matrices. The new content is the all-high-distance linear/quadratic-jet rank classification and the resulting state-dynamics census, not the previously known square relation.

## Limitations
The theorem intentionally makes no claim about \(c_1=c_2=0\), and it determines state preperiods or orbit counts rather than describing each individual orbit label. Full historical priority against unindexed algebraic coding-theory literature is not established. The full Fish–Key–Mwambene original PDF could not be retrieved in this examination; its abstract and the explicit older-range statement in Seneviratne's full article were checked. An independently performed mathematical audit has not occurred.

## References
1. P. Seneviratne, “Generalized hypercube graph \(\mathcal Q_n(S)\), graph products and self-orthogonal codes,” *Journal of Algebra Combinatorics Discrete Structures and Applications* **3** (2016), 37–44, DOI 10.13069/jacodesmath.13099. https://jacodesmath.com/index.php/jacodesmath/article/download/29/24/45
2. W. Fish, J. D. Key, E. Mwambene, “Graphs, designs and codes related to the \(n\)-cube,” *Discrete Mathematics* **309** (2009), 3255–3269, DOI 10.1016/j.disc.2008.09.024. https://uwcscholar.uwc.ac.za/items/feb59a6a-b4ae-4062-af74-b85ffeeda721
3. J. D. Key, W. Fish, E. Mwambene, “Codes from the incidence matrices and line graphs of Hamming graphs \(H^k(n,2)\) for \(k\ge2\),” *Advances in Mathematics of Communications* **5** (2011), 373–394, DOI 10.3934/amc.2011.5.373. https://doi.org/10.3934/amc.2011.5.373
