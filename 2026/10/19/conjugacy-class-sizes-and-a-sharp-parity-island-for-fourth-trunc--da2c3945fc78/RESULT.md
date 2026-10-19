# Conjugacy-class sizes and a sharp parity island for fourth-truncated cyclic quiver algebra groups

## Finding

Let \(Q_n\) be the directed cycle with vertices \(\mathbb Z/n\mathbb Z\), with every arrow oriented from \(i\) to \(i+1\), let \(J\) be the arrow ideal in its path algebra, and for every prime power \(q\) put
\[
A_n(q)=\mathbb F_qQ_n/J^4,\qquad G_n(q)=1+\operatorname{rad}(A_n(q)),\qquad n\ge3.
\]
This is an algebra group of nilpotency class exactly three. For \(n=4\), define \(k_r(q)\) as the number of conjugacy classes in \(G_4(q)\) containing precisely \(q^r\) elements. Then, over every finite field including characteristic two,
\[
\boxed{
\sum_{r\ge0}k_r(q)T^r
=q^4+q^2(q-1)(q+1)^2T^2
+\bigl(q(q-1)^2(q+1)+2q^4(q^2-1)\bigr)T^4
+q^2(q^2-1)^2T^6.
}
\]
In particular the only conjugacy-class sizes in \(G_4(q)\) are \(1,q^2,q^4,q^6\), and its number of conjugacy classes is
\[
\boxed{3q^6+q^5-q^4-2q^3-q^2+q.}
\]
Moreover this even-power phenomenon is isolated within the family: for \(n=3\), the group \(G_3(q)\) has a class of size \(q\), while for every \(n\ge5\), \(G_n(q)\) has a class of size \(q^3\). Thus all conjugacy-class sizes are even powers of \(q\) if and only if \(n=4\) (among \(n\ge3\)).

## Assumptions and scope

The field is an arbitrary finite field \(\mathbb F_q\), of any positive characteristic, including nonprime finite fields. In the path algebra, distinct oriented paths are a basis and the ideal \(J^4\) kills paths of length at least four. The radical of \(A_n(q)\) is \(J/J^4\), spanned by paths of lengths one, two and three. It has vector-space dimension \(3n\), and its third power is nonzero whereas the fourth power vanishes. The group \(1+J/J^4\) therefore has \(q^{3n}\) elements. Its lower central series has third term nonzero: the iterated commutator of three consecutive arrow generators has a nonzero length-three leading part. No logarithm, division by two or three, or characteristic restriction is used.

## Proof

All subscripts below are taken modulo \(n\). Denote the length-one, length-two and length-three paths starting at vertex \(i\) by \(\alpha_i,\beta_i,\gamma_i\), respectively. For elements of the radical write
\[
x=\sum_i(a_i\alpha_i+b_i\beta_i+c_i\gamma_i),\qquad
y=\sum_i(u_i\alpha_i+v_i\beta_i+w_i\gamma_i).
\]
The path-concatenation rule gives the length-two commutator coefficient
\[
[x,y]_{\beta_i}=a_i u_{i+1}-a_{i+1}u_i
\]
and the length-three coefficient
\[
[x,y]_{\gamma_i}=a_i v_{i+1}-a_{i+2}v_i+b_i u_{i+2}-b_{i+1}u_i.
\]
All \(c_i,w_i\) disappear, because paths of total length at least four vanish. For \(n=4\), the associated linear commutator map has, in the ordered coordinates \((u_0,\ldots,u_3;v_0,\ldots,v_3)\), block matrix
\[
M(a,b)=\begin{pmatrix}A_a&0\\ L_b&B_a\end{pmatrix},
\]
where
\[
(A_a u)_i=a_i u_{i+1}-a_{i+1}u_i,\quad
(B_a v)_i=a_i v_{i+1}-a_{i+2}v_i,\quad
(L_b u)_i=b_i u_{i+2}-b_{i+1}u_i.
\]
The full linear map from the twelve-dimensional radical has the same rank as this eight-by-eight matrix because the four length-three coordinates of its input are central. As \(1+x\) commutes with \(1+y\) exactly when \([x,y]=0\), its group centralizer has order \(q^{12-\operatorname{rank}M(a,b)}\) and its conjugacy class has size \(q^{\operatorname{rank}M(a,b)}\).

We now classify every rank uniformly in \(q\). First suppose \(a=0\). Then \(M\) has rank \(\operatorname{rank}L_b\). Reordering rows and columns by parity decomposes \(L_b\) into the blocks
\[
\begin{pmatrix}-b_1&b_0\\b_2&-b_3\end{pmatrix},\qquad
\begin{pmatrix}-b_2&b_1\\b_3&-b_0\end{pmatrix}.
\]
Both have determinant, up to a sign, \(\Delta=b_0b_2-b_1b_3\). Hence \(L_b\) has rank zero when \(b=0\), rank two when \(b\ne0\) and \(\Delta=0\), and rank four when \(\Delta\ne0\). Regarding \((b_0,b_1,b_2,b_3)\) as the entries of a two-by-two matrix, the respective numbers of \(b\)'s are
\[
1,\quad (q-1)(q+1)^2,\quad |\operatorname{GL}_2(\mathbb F_q)|=q(q-1)^2(q+1).
\]
These familiar counts also hold in characteristic two.

Suppose next \(a\ne0\) and its support is an independent set of the four-cycle: it consists of a singleton or one of the two opposite pairs. Then both \(A_a\) and \(B_a\) have rank two. If the support is contained in the even-position pair, \(\ker A_a\) consists exactly of vectors supported on even positions, and \(\operatorname{im}B_a\) consists exactly of vectors supported on even output positions; since \(L_b\) preserves parity, \(L_b(\ker A_a)\subseteq\operatorname{im}B_a\). The same argument applies to odd positions. Thus the rank of the block matrix is \(2+2=4\), independent of \(b\). There are
\[
4(q-1)+2(q-1)^2=2(q^2-1)
\]
such nonzero vectors \(a\).

For the remaining nonzero \(a\)'s, its support contains two adjacent cycle vertices. Then \(A_a\) has rank three and \(\ker A_a=\mathbb F_q a\): the equations \(a_i u_{i+1}-a_{i+1}u_i=0\) force a common scalar on each nonzero connected support component, while the adjacent pair forces all zero positions to vanish; on the four-cycle the only possible connected support component in this case is the whole nonzero support (or all vertices). Also \(B_a\) has rank three: its kernel contains the nonzero vector whose entries are \(a_i a_{i+1}\); the remaining three ranks follow by solving its cyclic equations on a support of two, three or four vertices (each yields a three-by-three nonzero minor). Finally, the identity
\[
L_b(a)=-B_a(b)
\]
shows \(L_b(\ker A_a)\subseteq\operatorname{im}B_a\), so the block matrix has rank \(3+3=6\), again independently of \(b\). The number of such \(a\) is
\[
q^4-1-2(q^2-1)=(q^2-1)^2.
\]

The four cases give the following exhaustive rank counts for the eight coordinates \((a,b)\):
\[
\begin{array}{c|c}
\operatorname{rank}M(a,b)&\text{number of }(a,b)\\\hline
0&1\\
2&(q-1)(q+1)^2\\
4&q(q-1)^2(q+1)+2q^4(q^2-1)\\
6&q^4(q^2-1)^2.
\end{array}
\]
Each such pair extends to \(q^4\) choices of central \(c\), and each element with rank \(r\) belongs to a class of size \(q^r\). Multiplying the element counts by \(q^4/q^r\) gives the asserted conjugacy-class polynomial. Evaluating at \(T=1\) gives the class-number polynomial. As an independent normalization, weighting each class by its size produces \(q^{12}\), the group order.

For the parity boundary, use \(a=0\), \(c=0\), and only length-two coefficients \(b\). In \(G_3(q)\), take \(b_0=1\), all others zero; the nonzero length-three outputs of the commutator map are \(u_2\) and \(-u_2\), giving rank one and a class of size \(q\). For every \(n\ge5\), take \(b_0=b_1=1\), all others zero. Then the nonzero commutator outputs are \(u_2-u_0\), \(u_3\), and \(-u_{n-1}\), in three distinct output coordinates and on linearly independent input forms. The rank is three, giving a conjugacy class of size \(q^3\). This proves the if-and-only-if statement for every field.

## Verification

The accompanying standalone C11 checker constructs each eight-by-eight commutator matrix directly from the displayed path-product equations and performs exact modular Gaussian elimination. It exhausts every \((a,b)\in\mathbb F_q^8\) for \(q=2,3,5\), rather than sampling, obtaining rank-frequency quadruples (for ranks \(0,2,4,6\)) respectively
\[
(1,9,102,144),\quad (1,32,1344,5184),\quad (1,144,30480,360000).
\]
The corresponding class counts are \(190\), \(2289\), and \(49105\). The program checks every forbidden rank has zero occurrences and validates the closed class-number formula. Reproduce with `cc -O2 -std=c11 verify.c -o verify && ./verify`; the successful final line is `VERIFY_OK`. It uses only the C standard library. Computational enumeration is corroboration, not an infinite-field proof, and it does not enumerate all groups at \(n\ge5\), for which explicit rank witnesses suffice.

## Relationship to prior work

The algebra-group construction and superclass/ordinary-class distinction are established in Diaconis–Thiem (2006), particularly their introduction and sections on general algebra groups. Their formulas concern supercharacters on superclasses, which may be unions of ordinary conjugacy classes, and do not give this cyclic radical's complete ordinary class-size polynomial. O'Brien–Voll (2012) give general methods to enumerate classes and characters of groups associated with Lie algebras; they do not state the above cyclic-path specialization, and characteristic restrictions in Lie correspondence do not supply the all-characteristics conclusion. Rossmann (2021) determines conjugacy-class counts for graphical groups via graph polynomials; those groups have nilpotency class at most two. Here the triple commutator is nonzero and the class-three length-three path equations are essential, so those graphical-group formulas do not specialize to the current group. A separate contemporaneous classification of square-zero elements in the same truncated path-algebra family studies \(x^2=0\), not conjugacy classes, and does not imply the class-size distribution. The elementary algebra-group centralizer/rank reduction is not claimed as new; the support-stratified calculation, explicit full polynomial, and sharp parity boundary are the proposed contributions.

## Limitations

The full class-size distribution is determined for the four-vertex cycle only; for other cycle lengths only existence of odd-exponent classes is asserted. No claim is made about irreducible character-degree distributions or classification of all groups from this invariant. The formulas are proved without a hypothesis on field characteristic, but experimental replay covers only three prime fields. A potentially relevant older paper by G. R. Robinson, “Counting conjugacy classes of unitriangular groups associated to finite-dimensional algebras” (1998), could not be inspected in complete text. An equivalent exact specialization or stronger result in that source or elsewhere would affect originality; failed searches do not establish universal novelty. No independent external audit has been performed.

## References

1. P. Diaconis and N. Thiem, “Supercharacter formulas for pattern groups,” arXiv:math/0610161v1, first public version 4 October 2006; *Transactions of the American Mathematical Society* **361** (2009), 3501–3533. https://arxiv.org/abs/math/0610161
2. E. A. O'Brien and C. Voll, “Enumerating classes and characters of \(p\)-groups,” arXiv:1203.3050, first submitted 14 March 2012; *Transactions of the American Mathematical Society* **367** (2015), 7775–7796. https://arxiv.org/abs/1203.3050
3. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1, first submitted 12 July 2021; *Bulletin of the London Mathematical Society* **54** (2022), 1830–1846. https://arxiv.org/abs/2107.05564
4. G. R. Robinson, “Counting conjugacy classes of unitriangular groups associated to finite-dimensional algebras,” *Journal of Group Theory* **1** (1998), 271–274. Complete text not inspected.
