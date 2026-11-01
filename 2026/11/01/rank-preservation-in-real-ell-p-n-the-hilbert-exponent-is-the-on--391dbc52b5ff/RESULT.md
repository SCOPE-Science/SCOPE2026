# Rank preservation in real \(\ell_p^n\): the Hilbert exponent is the only one

## Finding

For every integer \(n\geq3\), every integer \(4\leq k\leq n+1\), and every real exponent \(1<p<\infty\), the rank-preservation property \(\mathrm{RP}_k\) of the smooth real normed space \(\ell_p^n\) holds **if and only if** \(p=2\).

Here \(\mathrm{RP}_k\) means that the norm's unit-sphere duality map \(J\) sends every affinely independent \(k\)-tuple of unit vectors to an affinely independent \(k\)-tuple of contact covectors. More explicitly, if \(S_p=\{u\in\mathbb R^n:\|u\|_p=1\}\), then
\[
\mathrm{RP}_k:\quad
\dim\operatorname{aff}\{u_1,\ldots,u_k\}=k-1
\ \Longrightarrow\
\dim\operatorname{aff}\{J(u_1),\ldots,J(u_k)\}=k-1
\]
for all \(u_1,\ldots,u_k\in S_p\). The map \(J(u)=D\|\cdot\|_p(u)\) is regarded as a vector in \(\mathbb R^n\) by the standard coordinate pairing.

For every \(p\ne2\) and every \(0<c<1\), the proof gives four explicit primal unit vectors spanning a nondegenerate tetrahedron whose image covectors all lie in one affine plane. Their nonzero oriented-volume determinant is
\[
-2a^2T\bigl(1-2^{2-q}\bigr),\qquad
q=\frac{p}{p-1},\quad a=c^{q-1},\quad
T=\left(1-2^{1-q}c^q\right)^{(q-1)/q}.
\]
In particular, the corresponding tetrahedral volume is
\[
\frac{a^2T}{3}\,\bigl|1-2^{2-q}\bigr|,
\]
which is positive exactly when \(p\ne2\). The four-point witness extends explicitly to every admissible \(k\) and \(n\).

## Assumptions and scope

All spaces are real and finite dimensional. Fix \(n\ge3\) and \(1<p<\infty\). The norm is \(\|x\|_p=(\sum_{j=1}^n|x_j|^p)^{1/p}\); it is strictly convex and continuously differentiable off zero. The conjugate exponent \(q=p/(p-1)\) satisfies \(q>1\). The dual sphere is \(S_q\), and on the primal sphere the unique norming covector has coordinates
\[
J(u)_j=\operatorname{sgn}(u_j)|u_j|^{p-1}.
\]
The inverse duality map on \(S_q\) has coordinates \(J^{-1}(w)_j=\operatorname{sgn}(w_j)|w_j|^{q-1}\).

The classification concerns precisely the rank-preservation property of the duality map. It neither asserts that the ordinary \(k\)-medial axis is nonrectifiable in \(\ell_p^n\) nor characterizes all arbitrary smooth normed spaces with \(\mathrm{RP}_k\).

## Proof

**1. A coplanar dual-sphere family.** Choose any \(c\in(0,1)\) and put
\[
s=(1-c^q)^{1/q},\qquad
 t=(1-2^{1-q}c^q)^{1/q}.
\]
Both are strictly positive. In the first three coordinates of \(\mathbb R^n\), define
\[
\begin{aligned}
w_1&=(c,0,s),&w_2&=(0,c,s),\\
w_3&=(c/2,c/2,t),&w_4&=(c/2,c/2,-t).
\end{aligned}
\]
All other coordinates are zero. Each vector lies on \(S_q\): for the first pair the \(q\)-th power sum is \(c^q+s^q=1\), and for the second pair it is \(2(c/2)^q+t^q=1\). All four satisfy \(w_{i,1}+w_{i,2}=c\). Their affine span has dimension exactly two because \(w_1-w_2\) is a nonzero horizontal vector and \(w_3-w_4\) is a nonzero vertical vector.

**2. Inverse images are a tetrahedron except at the Hilbert exponent.** Let \(u_i=J^{-1}(w_i)\), and abbreviate
\[
a=c^{q-1},\quad b=(c/2)^{q-1}=2^{1-q}a,\quad
S=s^{q-1},\quad T=t^{q-1}>0.
\]
In their first three coordinates,
\[
\begin{aligned}
u_1&=(a,0,S),&u_2&=(0,a,S),\\
u_3&=(b,b,T),&u_4&=(b,b,-T).
\end{aligned}
\]
Since \(p(q-1)=q\), each \(u_i\) belongs to \(S_p\), and the coordinate formula for \(J\) gives \(J(u_i)=w_i\). Direct expansion of the oriented affine-volume determinant gives
\[
\begin{aligned}
\det[u_2-u_1,\,u_3-u_1,\,u_4-u_1]
&=-2aT(a-2b)\\
&=-2a^2T(1-2^{2-q}).
\end{aligned}
\]
As \(a,T>0\), the determinant vanishes exactly when \(2^{2-q}=1\), equivalently \(q=2\), equivalently \(p=2\). Thus for every non-Hilbert exponent the primal vectors are affinely independent while their four dual images are affinely dependent. This disproves \(\mathrm{RP}_4\) in \(\ell_p^3\) and yields the stated exact tetrahedron volume.

**3. Every dimension and rank.** Regard the four vectors as vectors in the first three coordinates of \(\mathbb R^n\). For \(5\le k\le n+1\), add \(e_4,e_5,\ldots,e_{k-1}\), where \(e_j\) is the \(j\)-th coordinate unit vector. Each added vector is a primal unit vector fixed by \(J\). The original four have affine span of dimension three; each new coordinate unit vector increases its affine dimension by one. Hence all \(k\) primal vectors have affine dimension \(k-1\). The first four image covectors span an affine plane, so adding the \(k-4\) coordinate vectors increases the dual-image affine dimension by at most \(k-4\), leaving it at most \(k-2\). Thus \(\mathrm{RP}_k\) fails for all \(k\ge4\) whenever \(p\ne2\).

**4. The converse.** At \(p=2\), the Euclidean Riesz identification gives \(J(u)=u\) on the unit sphere, preserving every affine dimension. Hence \(\mathrm{RP}_k\) holds for every \(k\). These four steps prove the equivalence for all claimed parameters.

As a geometric consequence, for \(p\ne2\) choose the constructed \(k\) unit vectors as a finite closed set \(E\). The origin is at common nearest-point distance one, and its nearest-point set has affine dimension \(k-1\); however, the associated contact covectors have affine dimension at most \(k-2\). Therefore \(0\in M_k(E)\setminus M_k^J(E)\) for the ordinary and dual medial axes as defined in the motivating literature. This is a single-point witness, not a claim about the size of that locus.

## Verification

The formulas require no numerical approximation. Their critical exact identities are \(p(q-1)=q\), \(2(c/2)^q=2^{1-q}c^q\), the coordinate duality identity, and the displayed determinant. Every parameter boundary in the statement is explicit: \(n\ge3\), \(4\le k\le n+1\), \(1<p<\infty\), \(0<c<1\).

The accompanying self-contained program `verify.py` computes the four dual and primal points, checks unit norms and the duality map, and independently expands the determinant numerically for 44 exponent/shape pairs, including values on each side of and at \(p=2\). It verifies the sign transition but is not used to infer the theorem from finite samples. Run with `python3 verify.py` in a standard Python 3 environment.

## Relationship to prior work

Durand, Liang and Zhang (2026, arXiv:2610.30878v1) introduce \(\mathrm{RP}_k\) explicitly in Definition 5.1 and ask in their Question 1 which smooth strictly convex norms satisfy it for \(k\ge4\), including whether \(\mathrm{RP}_{n+1}\) forces an inner-product norm. They prove the property for inner-product norms and construct specially perturbed smooth norms that fail it, without giving a complete result for the entire real \(\ell_p\) scale. The theorem above classifies that canonical non-Hilbert family for every dimension and rank, and does not answer the general characterization question.

Icking, Klein, Lê and Ma (1995) exhibit non-Euclidean four-site Voronoi/circumsphere phenomena, notably several \(\ell_4\)-spheres through a tetrahedral configuration. That work supplies important historical context for the failure of Euclidean four-site rigidity; its accessible abstract does not state an all-exponent duality-map rank classification. Blömer and Kohn (2018) analyze the complexity of Voronoi cells for smooth norms, including \(\ell_3\), but address lattice-cell complexity rather than the affine rank of the duality map.

## Limitations

The endpoints \(p=1\) and \(p=\infty\) are excluded because the smooth single-valued duality map used here need not exist at all unit vectors. The result classifies real coordinate \(\ell_p\) norms, not every nonellipsoidal smooth norm. Failure of \(\mathrm{RP}_k\) does not by itself establish nonrectifiability of the ordinary \(k\)-medial axis for any finite set. The older Icking–Klein–Lê–Ma article was not available for full-text inspection, leaving a residual historical-priority risk beyond its accessible abstract. No external independent mathematical audit has been performed.

## References

1. A. Durand, X. Liang and S. Zhang, *Dual medial axes in finite-dimensional normed spaces*, arXiv:2610.30878v1 (first submitted 22 October 2026), https://arxiv.org/html/2610.30878v1, Definition 5.1; Theorems 1.3–1.4; Question 1.
2. C. Icking, R. Klein, N.-M. Lê and L. Ma, *Convex distance functions in 3-space are different*, Fundamenta Informaticae **22** (1995), 331–352, https://doi.org/10.3233/FI-1995-2242.
3. J. Blömer and K. Kohn, *Voronoi Cells of Lattices with Respect to Arbitrary Norms*, SIAM Journal on Applied Algebra and Geometry **2** (2018), 314–338, https://arxiv.org/abs/1512.00720.
