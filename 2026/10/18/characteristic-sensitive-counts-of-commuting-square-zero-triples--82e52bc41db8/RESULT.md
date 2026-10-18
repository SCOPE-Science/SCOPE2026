# Characteristic-sensitive counts of commuting square-zero triples in diamond incidence algebras

## Finding
Let \(q\) be any prime power and \(m\ge1\). Let \(P_m\) have unique bottom \(0\), unique top \(1\), and \(m\) pairwise incomparable elements \(z_1,\dots,z_m\) strictly between them. For the radical \(J_m\) of the incidence algebra \(I(P_m,\mathbb F_q)\), write \(T_m(q)\) for the number of **ordered** triples of elements that are each square-zero and pairwise commute.

For \(s\in\{0,2,3\}\), put
\[
F_{m,q}(s)=\sum_{r=s}^{\min(m,3)} {3-s\brack r-s}_q\left(\prod_{i=0}^{r-1}(q^m-q^i)\right)q^{3(m-r)},
\]
where the Gaussian coefficient is zero if its lower argument is outside the allowed range. Set \(\delta_q=0\) in characteristic two, and \(\delta_q=(q-1)^3\) in odd characteristic. Then
\[
\boxed{T_m(q)=q^3\bigl(F_{m,q}(0)+(q^3-1-\delta_q)F_{m,q}(2)+\delta_qF_{m,q}(3)\bigr).}
\]
The formulas hold without any restriction on \(m\) relative to three, and over nonprime finite fields. They count radical triples, not all square-zero triples of the full incidence algebra.

## Assumptions and scope
The coefficient field is \(\mathbb F_q\), \(q\) a prime power, and \(m\) a positive integer. The incidence-algebra matrix units \(e_{xy}\) satisfy \(e_{xy}e_{uv}=\mathbf 1_{y=u}e_{xv}\). Its radical has basis \(e_{0z_j},e_{z_j1},e_{01}\). Thus a radical element has unique coordinates
\[
X(a,b,c)=\sum_{j=1}^m a_j e_{0z_j}+\sum_{j=1}^m b_j e_{z_j1}+c e_{01}.
\]
No assumption of commutativity is made about the incidence algebra itself.

## Proof
**Step 1 (multiplication).** Direct multiplication of matrix units gives
\[
X(a,b,c)X(a',b',c')=(a\cdot b')e_{01}.
\]
Write the three vectors \(a_i\) as the rows of a \(3\times m\) matrix \(A\), and the \(b_i\) as the rows of \(B\). Then the \(3\times3\) matrix \(M=AB^{\mathsf T}\) has entries \(M_{ij}=a_i\cdot b_j\). Square-zero of each \(X_i\) is precisely \(M_{ii}=0\); pairwise commutativity is precisely \(M_{ij}=M_{ji}\). The three central parameters \(c_i\) are unconstrained, giving the factor \(q^3\).

**Step 2 (hollow symmetric rank law).** Every admissible matrix is
\[
M=\begin{pmatrix}0&u&v\\u&0&w\\v&w&0\end{pmatrix}.
\]
If one of \(u,v,w\) is nonzero, a principal \(2\times2\) minor is its negative square and hence nonzero. Thus no such nonzero matrix has rank one. Its determinant is \(2uvw\). Therefore the rank frequencies are: rank zero once; rank two \(q^3-1\) times in characteristic two, or \(q^3-1-(q-1)^3\) times in odd characteristic; rank three zero times in characteristic two, or \((q-1)^3\) times in odd characteristic.

**Step 3 (factorization fiber).** Fix any \(3\times3\) matrix \(M\) of rank \(s\). Count factorizations \(AB^{\mathsf T}=M\), \(A,B\in\mathrm{Mat}_{3\times m}(\mathbb F_q)\). For a factor \(A\) of rank \(r\), the image \(U\subseteq\mathbb F_q^3\) of \(A\) must contain \(\operatorname{im}M\). There are \({3-s\brack r-s}_q\) choices of such \(U\), and exactly \(\prod_{i=0}^{r-1}(q^m-q^i)\) surjections \(\mathbb F_q^m\twoheadrightarrow U\) realizing \(A\). For every such \(A\), each of the three columns of \(B^{\mathsf T}\) solves an affine system with \(m-r\) free parameters. Hence there are \(q^{3(m-r)}\) choices of \(B\). Summing over \(r\) gives \(F_{m,q}(s)\), which depends only on the rank of \(M\).

**Step 4 (sum).** Multiply the factorization fiber by the number of admissible \(M\) of each rank and by the \(q^3\) free central coordinates. This yields exactly the displayed formula, for every prime power and every positive integer \(m\). No experiment is used to infer the general statement.

## Verification
The self-contained Python scripts `artifacts/verify_diamond.py` and `artifacts/verify_gf4.py` independently enumerate pairs of row-matrices satisfying the quadratic and commutation constraints for the finite test cases \((m,q)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\) and \((1,4)\). They compare the counts with the closed formula; the nonprime field \(\mathbb F_4\) uses explicit polynomial-basis multiplication, not arithmetic modulo four. The corresponding radical-triple counts include \(T_1(2)=120\), \(T_1(3)=1431\), \(T_2(2)=2528\), \(T_2(3)=135675\), and \(T_3(2)=77568\). The symbolic proof covers all remaining fields and dimensions.

## Relationship to prior work
Incidence-algebra matrix units and the quotient-of-path-algebra perspective are established; Quinn (2013), Section 2.2, supplies the explicit multiplication law but studies shellability and Gröbner bases rather than the commuting square-zero triple count. Britnell–Wildon (2011) concerns the existence of commuting representatives of similarity classes of full matrices; it does not provide this fixed-poset radical enumeration. Gargate–Gargate (2019) counts involutions in incidence algebras (including rhombus-shaped posets) for odd characteristic, a different equation from square-zero, and its full text could not be checked here. The enumeration also follows after combining the new incidence interpretation with elementary rank-factorization and hollow-symmetric rank facts; those constituents alone are not asserted novel.

## Limitations
The formula applies only to ordered triples in the Jacobson radical of the specified bounded diamond family. It does not count arbitrary square-zero elements of the full algebra, unordered triples, tuples of larger length, or general posets. No independent external mathematical audit has been performed. Specialized literature on commuting nilpotent varieties or rhombus incidence-algebra enumerations may contain a stronger formula; this remains a residual originality risk.

## References
1. D. Quinn, "The incidence algebra of posets and acyclic categories," *Kyushu J. Math.* **67** (2013), 117–127, https://doi.org/10.2206/kyushujm.67.117 (released online 2013-07-25).
2. J. R. Britnell and M. Wildon, "On types and classes of commuting matrices over finite fields," *J. London Math. Soc.* **83** (2011), 470–492, https://doi.org/10.1112/jlms/jdq088.
3. I. Gargate and M. Gargate, "Involutions on incidence algebras of finite posets," arXiv:1907.06805 (2019), https://arxiv.org/abs/1907.06805 (relevant comparison, later than the archival source).
