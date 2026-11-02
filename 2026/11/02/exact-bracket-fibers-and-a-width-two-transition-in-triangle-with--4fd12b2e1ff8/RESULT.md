# Exact bracket fibers and a width-two transition in triangle-with-leaves Lie algebras

## Finding

For every field \(k\) and integer \(r\geq 0\), let \(G_r\) consist of a triangle on vertices \(1,2,3\) and \(r\) additional leaves, each joined only to vertex \(1\). Define its graphical two-step nilpotent Lie algebra \(L_r=V\oplus Z\), where \(V=k^{r+3}\), \(Z\) has basis \(z_{12},z_{13},z_{23},z_{1,4},\ldots,z_{1,r+3}\), the latter space is central, and \([e_i,e_j]=z_{ij}\) on graph edges in increasing order. Thus \(\dim L_r=2(r+3)\), and \([L_r,L_r]=Z\).

Write an arbitrary element of \(Z\) as
\[
 z=a z_{12}+b z_{13}+c z_{23}+\sum_{j=1}^{r}d_jz_{1,j+3},
 \qquad \mathbf d=(d_1,\ldots,d_r).
\]
The image of the single-bracket map \(L_r\times L_r\to Z\) is *exactly* the complement of
\[
 \left\{z:a=b=0,\quad c\ne0,\quad \mathbf d\ne\mathbf0\right\}.
\]
Hence the bracket width of \(L_r\) is \(1\) when \(r=0\) and precisely \(2\) when \(r\geq1\). Here bracket width means the maximum over \(Z\) of the minimal number of brackets whose sum is the prescribed element; the zero element has length zero.

Now suppose \(k=\mathbb F_q\). Let \(F_{q,r}(z)\) be the number of ordered pairs \((v,w)\in V^2\) satisfying \([v,w]=z\). Its complete, disjoint fiber formula is
\[
 F_{q,r}(z)=
 \begin{cases}
 q^{r+1}(q^2-1), & (a,b)\ne(0,0),\\
 0, & a=b=0,\ c\ne0,\ \mathbf d\ne\mathbf0,\\
 q^{2r+1}(q^2-1), & a=b=0,\ c\ne0,\ \mathbf d=\mathbf0,\\
 q^{r+2}(q^2-1), & a=b=c=0,\ \mathbf d\ne\mathbf0,\\
 q^{r+2}(q^2-1)+q^{2r}(q^3+q^2-q), & z=0.
 \end{cases}
\]
This also covers \(r=0\), with the empty leaf vector interpreted as zero. In particular,
\[
 |\operatorname{im}[\cdot,\cdot]|=q^{r+3}-(q-1)(q^r-1).
\]
If ordered pairs are counted in the **full Lie algebra** \(L_r^2\), rather than in \(V^2\), every displayed fiber must be multiplied by \(q^{2(r+3)}\), because both central coordinates are free.

## Assumptions and scope

The field is arbitrary for the image and width assertions, including characteristic two. Finite-field fiber formulas require a prime power \(q\ge2\). The graph is simple, with one triangle and all leaves attached to the same triangle vertex. No assertion is made about general graphs or any group commutator law. The zero-bracket pair count is not the number of nonzero commuting pairs, and ordered pairs include zeros.

The vertex basis and central edge basis specify the bracket without sign ambiguity: for \(v=\sum_i x_i e_i\) and \(w=\sum_i y_i e_i\), the coefficient of \(z_{ij}\), for \(i<j\), is \(x_i y_j-x_j y_i\). This defines an alternating Lie bracket even in characteristic two because the derived subspace is central.

## Proof

Set \(h_i=(x_i,y_i)\in k^2\), and let \(\det(h_i,h_j)=x_i y_j-x_j y_i\). The prescribed equations are
\[
 a=\det(h_1,h_2),\quad b=\det(h_1,h_3),\quad c=\det(h_2,h_3),
 \quad d_j=\det(h_1,h_{j+3}).
\]

**Step 1: geometric image.** If \((a,b)\ne(0,0)\), then \(h_1\ne0\). Every triple \((a,b,c)\) with \((a,b)\ne(0,0)\) occurs as the three minors of a \(2\)-by-\(3\) matrix: every nonzero element of \(\bigwedge^2 k^3\) is decomposable. Once \(h_1\ne0\), each leaf equation can attain an arbitrary \(d_j\), independently. If \(a=b=0\) but \(c\ne0\), then \(h_2,h_3\) are linearly independent, so orthogonality of \(h_1\) to both under determinant forces \(h_1=0\). Consequently every leaf coefficient is zero. Conversely, this case with all leaves zero is obtained by taking \(h_1=0\) and a pair \(h_2,h_3\) with determinant \(c\). If \(a=b=c=0\), choose any nonzero \(h_1\), take \(h_2,h_3\) in its span and freely prescribe the leaf determinants. Thus the displayed excluded set is exact.

**Step 2: nonzero triangle minors.** For any fixed nonzero triple \((a,b,c)\), the set of ordered \(2\)-by-\(3\) matrices with these three minors is a torsor for \(\mathrm{SL}_2(\mathbb F_q)\). The group has order \(q(q^2-1)\). If \((a,b)\ne(0,0)\), each of the \(r\) leaf coordinates has exactly \(q\) solutions, giving \(q^{r+1}(q^2-1)\). If \(a=b=0\), \(c\ne0\), then \(h_1=0\) and each leaf is unrestricted in \(\mathbb F_q^2\), yielding \(q^{2r+1}(q^2-1)\) for zero leaf target, and zero otherwise.

**Step 3: vanishing triangle minors.** Suppose \(a=b=c=0\). If \(\mathbf d\ne0\), then \(h_1\ne0\), the vectors \(h_2,h_3\) must each belong to its one-dimensional span, and each leaf determinant equation has exactly \(q\) solutions. Therefore the fiber has \((q^2-1)q^2q^r=q^{r+2}(q^2-1)\) elements. For \(z=0\), this same \(h_1\ne0\) stratum contributes \((q^2-1)q^{r+2}\). If \(h_1=0\), the remaining triangle equation is \(\det(h_2,h_3)=0\), with exactly \(q^2+(q^2-1)q=q^3+q^2-q\) solutions; the leaves then contribute \(q^{2r}\). This gives the stated zero fiber.

**Step 4: image cardinality and width.** The excluded values have \((q-1)(q^r-1)\) choices. For any field, every triangle-only element is a bracket because \(\bigwedge^2 k^3\) consists of decomposable two-vectors, and every leaf-only element \(\sum_jd_jz_{1,j+3}\) equals \([e_1,\sum_jd_je_{j+3}]\). Thus any target is a sum of at most two brackets. When \(r\ge1\), the element \(z_{23}+z_{14}\) has the excluded coefficient pattern, so the bound is attained. For \(r=0\), every target is one bracket. This completes the proof.

## Verification

The standalone `verify.py` directly enumerates ordered pairs of vertex-coordinate vectors and computes all edge determinants, independently of the case-split proof. It compares the complete fiber table to the theorem over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), with \(r\) from zero to four in thirteen specified cases; \(\mathbb F_4\) uses polynomial arithmetic. All thirteen cases passed. The program also checks that fibers sum to \(q^{2(r+3)}\) and that the missing-output count is exact.

For example, when \(q=3\) and \(r=2\), there are \(243\) possible central outputs, of which exactly \(16\) are impossible. The \(227\) attained outputs account for all \(59049\) ordered pairs in the vertex space. The zero fiber has \(3321\) pairs. The printed marker is `TRIANGLE_LEAF_BRACKET_FIBERS_OK 13`.

## Relationship to prior work

Dani and Mainkar introduced graph-associated two-step nilpotent Lie algebras. Mainkar's 2013 public preprint gives the construction and addresses graph reconstruction from Lie isomorphism, not which derived elements occur as one bracket or their finite-field preimage multiplicities. The graph-to-bracket construction itself is not asserted new.

Gregory, Vander Meulen and Shader (1996) study decompositions of **fully specified** skew-symmetric matrices supported on a graph into rank-two matrices also supported there. Their Theorem 2.5 characterizes the supports of rank-two skew matrices, and their later decomposition results cover graph families. The problem here is different: only the graph-edge entries of a rank-two skew matrix are prescribed, and *nonedge entries are free*. Therefore their support-constrained decomposition criterion neither gives the exact image of this projected rank-two cone nor its \(q\)-dependent fiber counts. The classical Plücker/rank-two perspective is explicitly acknowledged as foundational, not presented as original.

Dubouloz, Kunyavskii and Regeta (2021) discuss bracket width, focused on simple Lie algebras of vector fields over characteristic zero. Their theorems do not concern these two-step graphical algebras, the characteristic-two case, or prescribed finite-field bracket fibers.

## Limitations

No general bracket-image criterion for arbitrary graphs is claimed. The fiber enumeration concerns *ordered* pairs, not simultaneous conjugacy classes, and it includes all pairs with zero coordinates. The proof is elementary but independent of the exhaustive finite experiments; those experiments do not establish the infinite family. Publication-priority checks cannot exclude an unlocated equivalent result from earlier rank-two matrix-completion or graphical Lie literature. Independent review has not been performed.

## References

1. S. G. Dani and M. G. Mainkar, “Anosov automorphisms on compact nilmanifolds associated with graphs,” *Transactions of the American Mathematical Society* **357** (2005), 2235–2251, DOI: 10.1090/S0002-9947-04-03518-4.
2. M. G. Mainkar, “Graphs and two-step nilpotent Lie algebras,” arXiv:1310.3414v1 (first posted 2013-10-12); *Groups, Geometry, and Dynamics* **9** (2015), 55–65, DOI: 10.4171/GGD/305.
3. D. A. Gregory, K. N. Vander Meulen and B. L. Shader, “Skew rank decompositions,” *Linear Algebra and its Applications* **244** (1996), 123–154, DOI: 10.1016/0024-3795(94)00217-7.
4. A. Dubouloz, B. Kunyavskii and A. Regeta, “Bracket width of simple Lie algebras,” arXiv:2102.08674 (2021).
