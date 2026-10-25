# Universal endpoint Hodge norms for symmetric design incidence graphs

## Finding

Let \(\mathcal D\) be an existing, nontrivial symmetric \(2\)-\((v,k,\lambda)\) block design with \(2\leq\lambda\leq k-2\). Its (simple, unweighted) point–block incidence graph \(G\) has \(2v\) vertices and \(vk\) edges. Orient every edge from a point to a block. Write \(D\) for the resulting signed vertex–edge incidence matrix and let
\[
Q=D^{\mathsf T}(DD^{\mathsf T})^+D,\qquad P=I-Q
\]
be the canonical real Euclidean-orthogonal cut and cycle projections on \(\mathbb R^{E(G)}\). Define the positive parameter expression
\[
A=(\lambda-1)(2k-\lambda)+2(k-\lambda)^2.
\]
Then both endpoint operator norms are **exact**:
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}
 =1+\frac{2(k-1)A}{k\lambda v}},
\]
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}
 =2+\frac{2(k-1)A}{k\lambda v}
 -\frac{2\bigl(2k(k-1)+\lambda\bigr)}{k\lambda v}}.
\]
**Every edge column has the corresponding absolute column sum**, regardless of whether the design admits a flag-transitive automorphism group. In the stated nontrivial range,
\[
\boxed{\|P\|-\|Q\|=
\frac{k(k-1)(k-4)+(k-2)\lambda}{k\lambda v}>0}.
\]
The formulas depend only on the design parameters, not on its incidence realization.

## Assumptions and scope

A symmetric \(2\)-\((v,k,\lambda)\) design consists of \(v\) points and \(v\) distinct \(k\)-element blocks, with each point on exactly \(k\) blocks and each pair of distinct points on exactly \(\lambda\) common blocks. The assumed inequalities \(2\leq\lambda\leq k-2\) imply \(k\geq4\) and \(1<k<v-1\). The design identity
\[
\lambda(v-1)=k(k-1),\qquad \lambda v=k^2-k+\lambda
\]
is used throughout. Claims are conditional on the design's existence; numerical parameter admissibility does not imply existence. No graph-transitivity, polarity or automorphism assumption is made. These are real, unweighted edge-coordinate operator norms for the specified **orthogonal** projections, not minimum norms over arbitrary projections.

## Proof

**1. Incidence identities and electrical projection.** Let \(M\) be the \(v\)-by-\(v\) zero–one point–block incidence matrix. Its row and column sums are \(k\), and the design law gives
\[
MM^{\mathsf T}=(k-\lambda)I+\lambda J.
\]
Since \(k>\lambda\), \(M\) is invertible. Thus the same identity holds for \(M^{\mathsf T}M\): the all-ones vector has singular value \(k\), while the orthogonal complement has squared singular value \(k-\lambda\). In particular, for every block \(B\), the number of points in \(B\cap C\) is \(k\) when \(C=B\) and \(\lambda\) when \(C\neq B\). The graph Laplacian is
\[
L=\begin{pmatrix}kI&-M\\-M^{\mathsf T}&kI\end{pmatrix}.
\]
The graph is connected because every pair of distinct points lies together on at least one block, and every block contains points. Consequently the unit-current potential for a point–block incidence \(e=(p,B)\), unique up to a constant, is the solution of
\[
L\binom{x}{y}=\binom{\mathbf1_{\{p\}}}{-\mathbf1_{\{B\}}}.
\]
An explicit solution is
\[
x_q=\frac{k\mathbf1_{\{q=p\}}-\mathbf1_{\{q\in B\}}}{\lambda v},
\qquad
y_C=\frac{\mathbf1_{\{p\in C\}}}{\lambda v}
-\frac1{kv}-\frac{k\mathbf1_{\{C=B\}}}{\lambda v}.
\]
Indeed, eliminating \(y\) gives
\[
(k^2I-MM^{\mathsf T})x=k\mathbf1_{\{p\}}-\mathbf1_B,
\]
and on the zero-sum subspace the matrix on the left is \(\lambda v I\). Substitution into the block equations yields the stated \(y\). Since \(Q\mathbf1_{\{e\}}=D^{\mathsf T}(x,y)\), its coordinate at any incidence \((q,C)\) equals \(x_q-y_C\).

**2. Seven current classes with fixed signs.** Put \(T=k\lambda v\). Partition point vertices into \(P_0=\{p\}\), \(P_1=B\setminus\{p\}\), and \(P_2=\mathcal P\setminus B\). Partition block vertices into \(B_0=\{B\}\), \(B_1=\{C\neq B:p\in C\}\), and \(B_2=\{C:p\notin C\}\). The scaled voltages \(T(x,y)\) are
\[
\begin{array}{c|ccc|ccc}
& P_0&P_1&P_2&B_0&B_1&B_2\\\hline
T\text{ times potential}&k(k-1)&-k&0&-k(k-1)-\lambda&k-\lambda&-\lambda
\end{array}.
\]
There are precisely seven nonempty incidence types. The signs and counts of the point-to-block current are:

| Edge type | Count | \(T\) times current |
|---|---:|---:|
| \(P_0B_0\) | \(1\) | \(2k(k-1)+\lambda\) |
| \(P_0B_1\) | \(k-1\) | \(k(k-2)+\lambda\) |
| \(P_1B_0\) | \(k-1\) | \(k(k-2)+\lambda\) |
| \(P_1B_1\) | \((k-1)(\lambda-1)\) | \(\lambda-2k\) |
| \(P_1B_2\) | \((k-1)(k-\lambda)\) | \(\lambda-k\) |
| \(P_2B_1\) | \((k-1)(k-\lambda)\) | \(\lambda-k\) |
| \(P_2B_2\) | \((v-k)(k-\lambda)\) | \(\lambda\) |

For instance, each point \(q\in P_1\) lies on \(\lambda-1\) blocks in \(B_1\), since the pair \(p,q\) lies on \(\lambda\) blocks including \(B\). Each block in \(B_1\) meets \(B\) in exactly \(\lambda\) points. All other counts follow by subtracting from the common degree \(k\). Their sum is \(vk\). The inequalities in the assumptions make the first three and last currents positive and the middle three negative, without zero-sign ambiguity.

**3. Sum of absolute electrical currents.** The total oriented current across *all* incidences is \(1\), since the explicit voltages satisfy \(\sum_q x_q=0\), \(\sum_C y_C=-1/k\), and every point and block has degree \(k\):
\[
\sum_{(q,C):\,q\in C}(x_q-y_C)=k\sum_qx_q-k\sum_Cy_C=1.
\]
Thus the absolute-current sum is \(1\) plus twice the total magnitude of the three negative classes, namely
\[
\sum_{f\in E(G)}|Q_{fe}|=
1+\frac{2(k-1)}{k\lambda v}
\bigl((\lambda-1)(2k-\lambda)+2(k-\lambda)^2\bigr).
\]
The calculation applies to an *arbitrary* incidence \(e\); therefore every column has the same sum and this equals \(\|Q\|_{1\to1}\).

**4. Complementary projection and dominance.** The diagonal entry is the effective resistance of the incidence edge:
\[
Q_{ee}=x_p-y_B=R:=\frac{2k(k-1)+\lambda}{k\lambda v}.
\]
It obeys \(0<R<1\), because
\[
k\lambda v-(2k(k-1)+\lambda)
=(k-1)\bigl(k(k-2)+\lambda\bigr)>0.
\]
The complementary column \(P\mathbf1_{\{e\}}=\mathbf1_{\{e\}}-Q\mathbf1_{\{e\}}\) therefore has absolute sum
\[
(1-R)+\sum_{f\neq e}|Q_{fe}|=\|Q\|_{1\to1}+1-2R,
\]
yielding the second formula. Both matrices are real symmetric, so their maximum absolute row and column sums agree, hence the claimed \(\ell_\infty\) identities. Finally,
\[
1-2R=\frac{k(k-1)(k-4)+(k-2)\lambda}{k\lambda v}>0
\]
for \(k\ge4\), proving strict cycle dominance. This completes the proof.

## Verification

A standalone standard-library Python checker, `check.py`, constructs incidence graphs from the quadratic-residue difference set on eleven points and the nonzero-vector point/hyperplane design over \(\mathbb F_2^4\), along with the complementary designs. It independently inverts a grounded vertex Laplacian in exact rational arithmetic and recomputes **all** cut and cycle projection column sums, not just one representative column. It checks four designs and \(346\) complete columns. Run with `python3 check.py`; the expected final line is `SYMMETRIC_DESIGN_ENDPOINT_EXACT_OK designs=4 columns=346`. These finite tests corroborate the algebra but do not substitute for the unrestricted proof.

For the biplane \((v,k,\lambda)=(11,5,2)\), the norms are \(\|Q\|=159/55\) and \(\|P\|=172/55\). For the point–hyperplane incidence design \((15,7,3)\), they are \(\|Q\|=107/35\) and \(\|P\|=368/105\).

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii study invariant cycle-space projections and calculate norms for Hamming graphs and discrete tori; their results provide the operator-theoretic motivation, but their graph families and results do not directly give the design-incidence expressions here. The incidence-matrix spectrum and symmetric-design combinatorics are classical; Shramchenko and Shramchenko develop spectra of mutual incidence matrices, not absolute electrical-current sums. General electrical-flow localization theorems bound current magnitudes, but do not provide this exact parameter-only endpoint norm classification. Bailey's work on symmetric-design incidence graphs concerns metric dimension rather than cut–cycle operator norms. No minimum-norm property is asserted for the canonical orthogonal projections on these designs.

## Limitations

The result covers only existing **symmetric** designs in \(2\le\lambda\le k-2\); it does not cover general nonsymmetric \(2\)-designs, whose block intersections need not be uniform. It treats real unit-edge \(\ell_1\)/\(\ell_\infty\) norms and the canonical Euclidean-orthogonal projection, not arbitrary projection constants, edge weights, or intermediate \(\ell_p\) norms. It is a theorem conditional on the combinatorial design axioms and does not classify which parameter triples admit a design. Overlap with projective-plane or crown-graph boundary families is avoided by the parameter range.

## References

- S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first publicly posted 2023-05-21, https://arxiv.org/abs/2305.12582.
- A. Shramchenko and V. Shramchenko, *Mutual incidence matrix of two balanced incomplete block designs*, arXiv:2312.03937, https://arxiv.org/html/2312.03937v3.
- R. F. Bailey, *On the metric dimension of incidence graphs*, arXiv:1707.02899, https://arxiv.org/abs/1707.02899.
- A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632, https://arxiv.org/abs/1708.01632.
