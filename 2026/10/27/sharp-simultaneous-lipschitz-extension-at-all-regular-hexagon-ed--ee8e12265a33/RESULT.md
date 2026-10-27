# Sharp simultaneous Lipschitz extension at all regular-hexagon edge midpoints

## Finding

Let \(v_j=(\cos(j\pi/3),\sin(j\pi/3))\), with indices in \(\mathbb Z/6\mathbb Z\), be the vertices of a regular Euclidean hexagon of side length \(1\). Put \(m_j=(v_j+v_{j+1})/2\), \(X=\{v_0,\ldots,v_5\}\), and \(Y=X\cup\{m_0,\ldots,m_5\}\). Equip both sets with **ambient Euclidean distance**. For real-valued functions, use the usual Lipschitz seminorm and let \(\lambda(X,Y)\) be the infimum of operator norms of all real-linear, constant-preserving extension operators \(T:\operatorname{Lip}(X)\to\operatorname{Lip}(Y)\) reproducing the data on \(X\). Equivalently, use the corresponding based Lipschitz Banach spaces.

Then

\[
\boxed{\lambda(X,Y)=\frac{2(2+\sqrt3)}{1+\sqrt7+\sqrt{13}}=1.029346317585\ldots.}
\]

This minimum is attained by an explicit **positive**, dihedrally equivariant operator. Its interpolation weights are strictly positive on all six vertices. In contrast, arithmetic averaging of the two endpoints of each hexagon edge has the strictly larger norm
\[
\frac{2+\sqrt3}{\sqrt{13}}=1.035084657640\ldots.
\]

The optimal operator is also nonexpansive when restricted to the six added midpoint points: for every \(i,j\), the associated probability measures satisfy \(W_1(\mu_i,\mu_j)\le\lVert m_i-m_j\rVert_2\). This is a separate structural property, not an assertion that the full operator has norm one.

## Assumptions and scope

All functions and operators are real-linear. The metric is the *Euclidean chord metric*, not the shortest-path metric around the hexagon. The optimum is over **all** linear extension operators, without any positivity or symmetry hypothesis. Normalizing the side length to \(1\) does not change the norm. Indices are read modulo \(6\).

Write \(t=\sqrt3\), \(u=\sqrt7\), \(w=\sqrt{13}\), and \(L=2(2+t)/(1+u+w)\). Set
\[
B=\frac{1+t-Lu}{t-1},\qquad D=\frac{L(w-1)}{1+t},\qquad
A=\frac{1-B+D}{2},\qquad C=\frac{1-B-D}{2},
\]
\[
a=\frac A2,\quad b=\frac B2,\quad c=\frac C2.
\]
These quantities satisfy \(a>b>c>0\) and \(2(a+b+c)=1\). Numerically, \(a=0.492465141558\ldots\), \(b=0.005912457298\ldots\), \(c=0.001622401144\ldots\).

For \(f:X\to\mathbb R\), define \((Tf)(v_j)=f(v_j)\) and
\[
(Tf)(m_i)=a(f(v_i)+f(v_{i+1}))+b(f(v_{i+2})+f(v_{i+5}))+c(f(v_{i+3})+f(v_{i+4})).
\]

## Proof

**Lower bound, allowing signed and asymmetric operators.** Let \(S\) be any real-linear extension with finite Lipschitz operator norm \(K\). Its action on constants is necessarily constant and reproduces them, since constants have zero Lipschitz seminorm. Average \(S\) over the twelve Euclidean symmetries of the hexagon. Averaging preserves the extension property and does not increase the operator norm, hence the value at \(m_0\) takes the form
\[
(Sf)(m_0)=a_0(f(v_0)+f(v_1))+b_0(f(v_2)+f(v_5))+c_0(f(v_3)+f(v_4)),
\]
where the coefficients may be signed but \(2(a_0+b_0+c_0)=1\). For each \(j\in\{0,2,3\}\), the datum \(f_j(v_k)=\lVert v_k-v_j\rVert_2\) is \(1\)-Lipschitz and vanishes at \(v_j\). Consequently,
\[
\sum_k \omega_k\lVert v_k-v_j\rVert_2\le K\lVert m_0-v_j\rVert_2,
\]
where \((\omega_0,\ldots,\omega_5)=(a_0,a_0,b_0,c_0,c_0,b_0)\). The three distances from \(m_0\) to \(v_0,v_2,v_3\) are respectively \(1/2,\sqrt7/2,\sqrt{13}/2\). Each of the three reflection-paired coefficient columns has the same **sum** of its distances to these three vertices, namely \(4+2\sqrt3\). Summing the three inequalities therefore gives
\[
2+\sqrt3=(4+2\sqrt3)(a_0+b_0+c_0)
\le \frac K2(1+\sqrt7+\sqrt{13}),
\]
so \(K\ge L\). No probability assumption enters this argument.

**Positive equioscillating extension.** The definitions above give \(A+B+C=1\) and the following exact linear identities:
\[
\begin{pmatrix}1&1+t&2+t\\1+t&2&1+t\\2+t&1+t&1\end{pmatrix}
\begin{pmatrix}A\\B\\C\end{pmatrix}
=L\begin{pmatrix}1\\u\\w\end{pmatrix}.
\]
Indeed, the row sums of this matrix are all \(4+2t\), the middle row gives the formula for \(B\), and the third-minus-first row gives the formula for \(D=A-C\). Exact radical inequalities yield \(a>b>c>0\); for example, the independently reproducible rational square-root enclosures in the accompanying checker establish \(0.4924<a<0.4925\), \(0.0058<b<0.0060\), and \(0.0015<c<0.0018\). Thus the coefficients define probability measures
\[
\mu_i=a(\delta_{v_i}+\delta_{v_{i+1}})+b(\delta_{v_{i+2}}+\delta_{v_{i+5}})+c(\delta_{v_{i+3}}+\delta_{v_{i+4}}).
\]
For every vertex \(v_j\), the distance-to-a-point transportation formula and the displayed matrix identities show
\[
W_1(\mu_i,\delta_{v_j})=\sum_k\mu_i(\{v_k\})\lVert v_k-v_j\rVert_2
=L\lVert m_i-v_j\rVert_2.
\]
Reflection and rotation cover all six vertex positions for each midpoint.

**Midpoint-pair bound.** Regard vertex indices as the cyclic group \(\mathbb Z/6\mathbb Z\). Define \(\nu_i=(\delta_{v_i}+\delta_{v_{i+1}})/2\). With the nonnegative probability vector
\[
\eta=(2a-2b+2c,\ 2b-2c,\ 2c,\ 0,\ 2c,\ 2b-2c),
\]
we have \(\mu_i=\nu_i*\eta\), where convolution uses cyclic shifts. Translation invariance and convexity of \(W_1\) give
\[
W_1(\mu_i,\mu_j)\le W_1(\nu_i,\nu_j).
\]
For cyclic midpoint separations \(1,2,3\), explicit couplings of \(\nu_0\) with \(\nu_j\) have respective costs
\[
\tfrac12\lVert v_0-v_2\rVert_2=\tfrac{\sqrt3}{2},\quad
\tfrac12(\lVert v_0-v_3\rVert_2+\lVert v_1-v_2\rVert_2)=\tfrac32,\quad
\tfrac12(\lVert v_0-v_4\rVert_2+\lVert v_1-v_3\rVert_2)=\sqrt3.
\]
These are exactly \(\lVert m_0-m_j\rVert_2\). Rotations and reflections handle the remaining midpoint pairs. Finally, vertex pairs are reproduced isometrically. Kantorovich–Rubinstein duality therefore bounds \(\operatorname{Lip}(Tf)\le L\operatorname{Lip}(f)\), and the lower bound shows equality.

**Improvement over simple midpoint averaging.** Ordinary averaging corresponds to \(a=1/2\) and \(b=c=0\). Vertex–midpoint pairs yield the worst ratio \((2+\sqrt3)/\sqrt{13}\), while the preceding midpoint-pair couplings remain valid. The inequality \(L<(2+\sqrt3)/\sqrt{13}\) is equivalent to \(\sqrt{13}<1+\sqrt7\), which follows from \(\sqrt7>5/2\).

## Verification

The included standard-library checker `verify_hexagonal_midpoints.py` uses integer-square-root-certified rational intervals for \(\sqrt3,\sqrt7,\sqrt{13}\), verifies strict weight positivity, the orbit-sum dual certificate, the six-by-six vertex–midpoint distance equalities, the six nonnegative convolution coefficients, and all three geometrically distinct midpoint couplings. It checks 36 vertex–midpoint pairs and 15 midpoint pairs via symmetry, as well as the strict gain over arithmetic averaging. Execute with `python3 verify_hexagonal_midpoints.py`. The proof above is analytic; finite interval checks are independently reproducible corroboration, not an independent mathematical audit.

## Relationship to prior work

Ambrosio and Puglisi (2016) establish linear Lipschitz extensions via transport-based random projections; Bruè, Di Marino and Stra (2018) develop general linear extension constructions; Basso (2021) relates finite Lipschitz extension moduli to relative projection constants and linear programs. The present statement is an exact sharp scalar linear extension constant on a specific twelve-point Euclidean refinement, including a positive optimizer and explicit signed-operator lower bound; the cited general constructions and optimization frameworks do not state this formula. The regular-polygon extension problem with **one added center** is different from extending to all six edge midpoints. Existing sharp interpolation calculations for simplex edges, square/cube midpoints, and cross-polytope midpoints have different input-point configurations and cannot be specialized to this twelve-point hexagon.

## Limitations

The conclusion concerns one regular hexagon and its six edge midpoints, real scalars, and the inherited Euclidean metric. It does not classify other polygon orders, arbitrary edge locations, all optimizers, nonlinear extensions, or extensions on the entire hexagonal region. Undetected equivalent literature remains a residual originality risk. Independent mathematical validation has not been performed.

## References

- L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (initial public version 2016-09-06).
- E. Bruè, S. Di Marino and F. Stra, *Linear Lipschitz and C1 extension operators through random projection*, arXiv:1801.07533 (initial public version 2018-01-23), especially the transport preliminaries and Section 4.1.
- G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (initial public version 2021-04-29), especially Section 5.2.
