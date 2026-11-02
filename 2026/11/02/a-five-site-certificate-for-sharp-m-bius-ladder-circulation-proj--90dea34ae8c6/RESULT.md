# A five-site certificate for sharp Möbius-ladder circulation projections

## Finding
For each integer \(n\ge10\), let \(M_{2n}\) have vertex set \(\mathbb Z/(2n)\mathbb Z\), cycle edges joining successive vertices, and antipodal chords joining \(i\) to \(i+n\). Orient the \(2n\) cycle edges consecutively and the \(n\) chords from \(i\) to \(i+n\) for \(0\le i<n\). Let \(B:\mathbb R^{3n}\to\mathbb R^{2n}\) be the signed incidence operator, and endow the edge space with its ordinary real \(\ell_1\) norm. For its circulation space \(Z_n=\ker B\), the **minimum over every real linear projection**, without an equivariance restriction, is
\[
\boxed{\inf\{\|P\|_{1\to1}:P^2=P,\ \operatorname{ran}P=Z_n\}=\frac{12}{5}-\frac{16}{5n}.}
\]
The infimum is attained by an explicit dihedrally invariant projection. In particular its limit is \(12/5\), with an exact correction \(16/(5n)\). This agrees, in the stated range, with the previously determined value for the planar circular ladder \(C_n\square K_2\), even though the Möbius ladder is nonplanar. No assertion for \(3\le n<10\) is part of the theorem.

## Assumptions and scope
Everything is over the **real** field, with the unsigned edge lengths all equal to one. In the chosen orientation, \(B e_{uv}=\mathbf1_v-\mathbf1_u\). The operator norm is the largest \(\ell_1\)-norm of a column. We write \(a=1/(2n)\) and use a cyclic vertex rotation \(R\) acting by signed edge permutations. A reflection fixing vertex zero reverses the cycle-edge orientations. The dihedral action is isometric in \(\ell_1\), preserves \(Z_n\), and has two edge orbits (cycle edges and chords).

## Proof
**1. Invariant reduction and one flow.** Average any projection onto \(Z_n\) over the dihedral group. Its average remains a projection onto \(Z_n\) and cannot have larger norm. If \(P\) is invariant, \(I-P=KB\) for the unique map \(K:\mathbf1^\perp\to\mathbb R^{3n}\) induced by \(I-P\); extend it by \(K\mathbf1=0\). Since \(BP=0\), \(BK=I-J\), where \(J\) averages vertex coordinates. Put \(h=K\mathbf1_0\). Then \(Bh=\mathbf1_0-a\mathbf1\), \(K\mathbf1_j=R^jh\), and \(h\) is fixed by the reflection through vertex zero.

Write the chord coordinates of \(h\) as \(g_0,\ldots,g_{n-1}\), where reflection invariance means \(g_{n-i}=-g_i\) for \(1\le i<n\). Write its cycle-edge coordinates as \(h_0,\ldots,h_{2n-1}\). The divergence and reflection conditions are precisely
\[
h_0=-\frac{1-a+g_0}{2},\quad
h_j=h_{j-1}+a-g_j\ (1\le j<n),\quad
h_{2n-1-j}=-h_j\ (0\le j<n).
\]
Conversely, every such choice of \(g\) gives \(Bh=\mathbf1_0-a\mathbf1\), a reflection-invariant \(h\), and an equivariant \(K\) defined by \(K\mathbf1_j=R^jh\). Its sum over all vertex rotations vanishes (the chord part cancels under a half-turn, and the rotation-invariant cycle part is reflection-odd). Hence \(K\mathbf1=0\), \(BK=I-J\), and \(P=I-KB\) is a projection onto \(Z_n\). Thus this parameterization is both necessary and sufficient for invariant projections.

**2. Exact column norms.** Define
\[
S_j=\sum_{i=1}^{j}g_i\quad(S_0=0),\qquad
R_i^{\pm}=a\pm g_i,\quad
T_0=g_0-g_1,\quad T_j=g_{j+1}-g_j\ (1\le j\le n-2),
\]
\[
Z_j=\frac12+g_0+2S_j\quad(0\le j<n),\qquad
C_0=1+2g_0,\quad C_j=g_j\quad(1\le j<n).
\]
Using \(P e=e+K\mathbf1_{\mathrm{tail}(e)}-K\mathbf1_{\mathrm{head}(e)}\) and the signed antipodal action, the cycle-edge and chord-edge column norms are respectively
\[
H=\sum_{i=0}^{n-1}(|R_i^-|+|R_i^+|)+2|T_0|+\sum_{j=1}^{n-2}|T_j|,
\]
\[
V=2\sum_{j=0}^{n-1}|Z_j|+|C_0|+2\sum_{j=1}^{n-1}|C_j|.
\]
All columns within each edge orbit have these same norms, so \(\|P\|_{1\to1}=\max(H,V)\). The antipodal reflection gives \(S_{n-1-j}=S_j\), an identity used below.

**3. A uniform five-site lower certificate.** For \(n\ge10\), use \(w|x|\ge s x\) whenever \(|s|\le w\), assigning signed coefficients to the summands in \(4H+V\) as follows. For \(4|R_i^-|\), select \(+4\) for \(0\le i\le n-3\), zero for \(i=n-2\), and \(-4\) for \(i=n-1\). For \(4|R_i^+|\), select \(-4\) at \(i=0,1\), zero at \(i=2\), and \(+4\) at \(3\le i<n\). Select \(-8\) for \(8|T_0|\), and \(+4\) for \(4|T_i|\) when \(i\in\{1,2,3,n-4,n-3,n-2\}\), zero otherwise. For \(2|Z_j|\), select \(+2\) when \(j\in\{0,1,2,3,n-4,n-3,n-2,n-1\}\), \(-2\) at \(j=4\), and zero otherwise. For \(|C_0|\) select \(+1\). For \(2|C_i|\), select \(-2\) at \(i=1,2,3,4\), \(+2\) at \(i=n-4,n-3,n-2,n-1\), and zero elsewhere. The relevant index sets are disjoint in every stated dimension.

Substitution leaves the constant \((8n-32)a+7+1=12-16/n\). To check that no free variable remains, the five groups (two \(R\) groups combined, \(T\), \(Z\), and \(C\)) contribute respectively the following affine variable expressions:
\[
(-8g_0-16g_1-8g_2),\quad(-8g_0+8g_4),\quad
(14g_0+20g_1+12g_2+4g_3-4g_4),\quad
(2g_0-4g_1-4g_2-4g_3-4g_4).
\]
Their sum is zero. Consequently
\[
4H+V\ge12-\frac{16}{n},\qquad
\max(H,V)\ge\frac{4H+V}{5}\ge\frac{12}{5}-\frac{16}{5n}.
\]
This is a global bound: no assumption on the signs, size, or support of the \(g_i\) was used.

**4. Attainment in both parameter regimes.** Set \(g_0=-u\), \(g_i=-x_i\) for \(i=1,2,3\), \(g_{n-i}=x_i\), and all other \(g_i=0\). In each of the following regimes \(u\ge x_1\ge x_2\ge x_3\ge0\) and \(q:=1/2-u=2(x_1+x_2+x_3)\). The direct absolute-value evaluations in part 2 then simplify to
\[
H=4u+4\sum_{i=1}^{3}\max(a,x_i)+2(n-7)a,\qquad
V=4q+8(x_1+2x_2+3x_3).
\]
For \(10\le n\le16\), take
\[
q=\frac{3+22a}{20},\quad u=\frac12-q,\quad
(x_1,x_2,x_3)=\left(a,a,\frac{3-58a}{40}\right).
\]
Here \(0\le x_3\le a\), and substitution gives \(H=V=12/5-16/(5n)\). For \(n\ge17\), take
\[
u=\frac15+\frac{19a}{5},\quad q=\frac12-u,\quad
(x_1,x_2,x_3)=\left(\frac3{20}-\frac{39a}{10},a,a\right).
\]
Here \(a\le x_1\le u\), and again direct substitution gives the identical equality. The constructed invariant projection therefore attains the global lower bound for every \(n\ge10\), completing the proof.

## Verification
A dependency-free Python checker accompanies this proof. It uses exact rational arithmetic to verify the two closed-form norm evaluations and the signed certificate for \(10\le n\le150\), and explicitly constructs graph incidence matrices and the projections for \(10\le n\le18\), checking zero divergence, idempotence and every column norm exactly. Its successful output is `CHECK_OK rational_formula_orders=141 exact_matrix_projection_orders=9`. The quantified proof above, especially the signed coefficient cancellation and regime inequalities, is the basis for the all-dimensional claim; finite runs are not an infinite proof.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii developed the invariant-projection framework for real cycle spaces in \(\ell_1\) and studied diamond/Laakso graphs, tori, and Hamming graphs [1–3]. The present calculation treats the distinct Möbius-ladder graph family and derives an explicit uniform extremal supporting hyperplane. Heinig's paper on Möbius ladders and cycle spaces [4] instead considers generation of the \(\mathbb F_2\)-cycle space by Hamilton circuits; that is a different question, field, and norm. The exact circular-ladder constant \(12/5-16/(5n)\) is known from a separate calculation; its agreement here does not imply equality of the circulation subspaces under signed-coordinate isometries (the circular ladders are planar, while these Möbius ladders are nonplanar). An equivalent older extremal-norm computation under another name is a remaining priority risk.

## Limitations
This theorem neither identifies all minimizing projections nor settles \(3\le n<10\), weighted edges, complex-linear projections, or the complementary cut-space projection norm. Independent mathematical validation has not been performed. The exact match with circular ladders is an equality of a particular norm invariant, **not** an isometric identification of the two cycle spaces.

## References
[1] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, first arXiv version 2018-07-10, arXiv:1807.03814, https://arxiv.org/abs/1807.03814.

[2] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, first arXiv version 2020-07-15, arXiv:2007.07949, https://arxiv.org/abs/2007.07949.

[3] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, first arXiv version 2023-05-21, arXiv:2305.12582, https://arxiv.org/abs/2305.12582.

[4] P. C. Heinig, *On prisms, Möbius ladders and the cycle space of dense graphs*, first arXiv version 2011-12-21, arXiv:1112.5101, https://arxiv.org/abs/1112.5101.
