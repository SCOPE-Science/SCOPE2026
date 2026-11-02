# Square-zero elements in Loewy-length-four cyclic Nakayama algebras: a universal fourth-order recurrence

## Finding

For every integer \(n\ge3\) and finite field \(k=\mathbb F_q\), let \(Q_n\) be the uniformly oriented cycle on \(n\) vertices, let \(J\) be the arrow ideal of the path algebra \(kQ_n\), and put \(A_n=kQ_n/J^4\). Write \(D_n(q)=|\{u\in A_n:u^2=0\}|\), counting all square-zero elements, including zero. Then the complete count is given by an independence-set formula with nonlocal interaction statistics:

\[
D_n(q)=\sum_{\substack{S\subseteq\mathbb Z/n\mathbb Z\\S\cap(S+1)=\varnothing}}
  (q-1)^{|S|}q^{2n-2|S|+t_2(S)+t_3(S)},
\qquad
 t_j(S)=\sum_{i\in\mathbb Z/n\mathbb Z}\mathbf1_{i\in S}\mathbf1_{i+j\in S}.
\]

In particular, **all field sizes, all characteristics and all cycle lengths** obey the same recurrence for \(n\ge7\):

\[
\boxed{D_n(q)=q^2D_{n-1}(q)+q^3(q-1)D_{n-2}(q)-q^6(q-1)^2D_{n-4}(q).}
\]

Its four necessary starting values are

\[
\begin{aligned}
D_3(q)&=q^5(4q-3), &D_4(q)&=q^6(3q^2-2),\\
D_5(q)&=q^9(6q-5), &D_6(q)&=q^9(6q^3-9q+4).
\end{aligned}
\]

Equivalently, put \(w=(q-1)/q^2\), and index a matrix by the allowed binary triples \(000,001,010,100,101\), in that order. Then

\[
T_q=\begin{pmatrix}
1&w&0&0&0\\
0&0&1&0&0\\
0&0&0&1&qw\\
1&qw&0&0&0\\
0&0&1&0&0
\end{pmatrix},\qquad D_n(q)=q^{2n}\operatorname{tr}(T_q^n),\quad n\ge3.
\]

The recurrence follows from the characteristic determinant
\[\det(I-tT_q)=1-t-qwt^2+(q-1)wt^4.\]
The field size \(q\) is numerical in these counting polynomials; matrices are not asserted to act over characteristic zero.

## Assumptions and scope

The algebra \(A_n\) has as a basis the residue classes of all oriented paths of lengths zero, one, two and three. For \(i\in\mathbb Z/n\mathbb Z\) write \(p_{i,d}\) for the unique length-\(d\) path starting at \(i\). Multiplication is concatenation when endpoints meet and is zero otherwise or when the combined length is at least four. In particular \(\dim_k A_n=4n\), and the Jacobson radical has dimension \(3n\). There are no assumptions about \(q\) beyond being a prime power. The theorem concerns rational points of the square-zero locus and does not assert a reducedness or irreducible-component classification for its scheme.

## Proof

**Step 1 (nilpotents lie in the radical).** The quotient \(A_n/J\cong k^n\) has no nonzero square-zero elements, so a square-zero \(u\) necessarily has zero coefficient on every path of length zero. Thus it has a unique expansion
\[u=\sum_{i\in\mathbb Z/n\mathbb Z}(a_i p_{i,1}+b_i p_{i,2}+c_i p_{i,3}).\]
The degree-three coefficients \(c_i\) cannot occur in \(u^2\). Concatenating paths shows that \(u^2=0\) if and only if for every \(i\),
\[a_i a_{i+1}=0,\qquad a_i b_{i+1}+b_i a_{i+2}=0.\]
The first equation says that \(S=\{i:a_i\ne0\}\) is an independent set of the cycle (where adjacency is cyclic even for \(n=3\)). Each occupied site has \(q-1\) choices for its nonzero coefficient.

**Step 2 (support-only rank of the middle layer).** For fixed \(a\) with independent support \(S\), the equations in \(b\) are represented by the \(n\)-by-\(n\) matrix
\[M(a)_{i,j}=a_i\mathbf1_{j=i+1}+a_{i+2}\mathbf1_{j=i},\]
all indices taken cyclically. We prove
\[\operatorname{rank}M(a)=2|S|-t_2(S)-t_3(S).\]
Make a bipartite incidence graph with a vertex for each row and column and an edge for each nonzero matrix entry. Each occupied \(a_i\) gives two distinct edges, so the graph has exactly \(2|S|\) edges. A row has degree two precisely when \(i,i+2\in S\), yielding \(t_2(S)\) such rows. A column has degree two precisely when \(j-1,j+2\in S\), yielding \(t_3(S)\) such columns. By independence of \(S\), a degree-two row is not adjacent to a degree-two column: the two possible incidences would force consecutive occupied sites. Therefore every nontrivial connected component is a star with at most two edges. Its weighted matrix has rank exactly one, because all its edges have nonzero weights. The number of stars is the number of edges minus the number of degree-two row or column vertices. This proves the rank formula in every characteristic, independent of the chosen nonzero \(a_i\) values.

**Step 3 (disjoint finite-field count).** Given \(S\), there are \((q-1)^{|S|}\) choices for \(a\), \(q^{n-2|S|+t_2(S)+t_3(S)}\) choices for the linear-system solution \(b\), and \(q^n\) free choices for \(c\). Summing over the mutually disjoint supports proves the displayed independence-set formula.

**Step 4 (transfer matrix and recurrence).** Encode independent supports by cyclic binary strings \(x_i\) without consecutive ones. The weight of a support, after extracting \(q^{2n}\), is
\[w^{\sum_i x_i}q^{\sum_i x_ix_{i+2}+\sum_i x_ix_{i+3}}.\]
A transition from the three-bit state \((a,b,c)\) to \((b,c,d)\) receives weight \(w^dq^{d(a+b)}\). The five allowable states give exactly the displayed \(T_q\). For \(n\ge3\), cyclic words correspond bijectively to closed walks of length \(n\) in this state graph, with exactly the desired weights, proving the trace identity. Expanding the displayed determinant, the Cayley–Hamilton identity gives
\[\operatorname{tr}(T_q^n)=\operatorname{tr}(T_q^{n-1})+qw\operatorname{tr}(T_q^{n-2})-(q-1)w\operatorname{tr}(T_q^{n-4})\]
for \(n\ge5\). Multiplying by \(q^{2n}\) yields the stated order-four recurrence, in particular for every \(n\ge7\). Evaluating the independent-support sum for \(n=3,4,5,6\) supplies the listed starting values. This completes the proof.

## Verification

The standalone script `nakayama_square_zero_verify.py` performs independent path-basis multiplication and finite-field row reduction; it exhaustively enumerates every degree-one and degree-two coefficient assignment in eleven configurations, including genuine \(\mathbb F_4\) arithmetic. It verifies the predicted rank in every tested independent degree-one support, recomputes counts using an independent-support sum and an integral transfer matrix, and checks the fourth-order recurrence at lengths three through fifteen for six field sizes. It prints `CYCLIC_NAKAYAMA_LENGTH4_SQUARE_ZERO_OK 11 6x13`. The experiments are finite checks, not the justification for the general theorem.

## Relationship to prior work

Cyclic and truncated path algebras are classical objects. Shen, *The singularity category of a Nakayama algebra* (2014 preprint), studies their singularity categories and resolution quivers, not finite-field cardinalities of their elementwise square-zero loci. Jonsson, *Cell Structure of Bimodules over Radical Square Zero Nakayama Algebras* (2018), treats bimodule cell structure for algebras with square-zero radical rather than the Loewy-length-four elementwise equations above. Existing studies of homological invariants of truncated quiver algebras likewise do not by themselves imply this arithmetic recurrence. The new content claimed here is only the explicit all-field square-zero count, support-rank reduction, and universal recurrence; no novelty is claimed for the path-algebra construction or generic transfer-matrix techniques.

## Limitations

The cycle is uniformly oriented and has at least three vertices; arbitrary quivers and different truncation lengths need separate analysis. The result counts elements satisfying \(u^2=0\), not involutions of the unit group in odd characteristic. No irreducible-component theorem, higher nilpotency-index census, or scheme-theoretic reducedness claim is made. An exact historical-equivalence claim would require further bibliographic coverage beyond the inspected sources; independent mathematical validation has not been performed.

## References

- Dawei Shen, *The singularity category of a Nakayama algebra*, arXiv:1404.2451, initial public submission 2014-04-09, https://arxiv.org/abs/1404.2451.
- Helena Jonsson, *Cell Structure of Bimodules over Radical Square Zero Nakayama Algebras*, arXiv:1804.07082, https://arxiv.org/abs/1804.07082.
- Yunge Xu, Yang Han and Wenfeng Jiang, *Hochschild cohomology of truncated quiver algebras*, arXiv:math/0509202, https://arxiv.org/abs/math/0509202.
