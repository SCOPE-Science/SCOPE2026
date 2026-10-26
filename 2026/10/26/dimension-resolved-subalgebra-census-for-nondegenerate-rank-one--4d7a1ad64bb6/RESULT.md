# Dimension-resolved subalgebra census for nondegenerate rank-one evolution algebras

## Finding

Let \(q\) be an odd prime power, \(V\) an \(n\)-dimensional vector space over \(\mathbb F_q\) with \(n\ge2\), \(B\) a nondegenerate symmetric bilinear form, and \(0\ne u\in V\). Equip \(V\) with the commutative multiplication
\[
xy=B(x,y)u.
\]
This is exactly the class of nondegenerate evolution algebras with one-dimensional square. Let \(N_r\) denote the number of ordinary \(r\)-dimensional subalgebras, for \(0\le r\le n\). Put \(\delta=1\) if \(B(u,u)=0\), and \(\delta=0\) otherwise. For even \(n=2m\), put \(\varepsilon=\chi_q((-1)^m\det B)\in\{1,-1\}\), where \(\chi_q\) is the quadratic character; for odd \(n\) no sign is required.

Define the Gaussian binomial coefficient \({d\brack j}_q\), equal to zero outside \(0\le j\le d\), in the usual way. Define \(T_0(d,q,\varepsilon)=1\), \(T_j(d,q,\varepsilon)=0\) for \(j<0\) or \(j>\lfloor d/2\rfloor\), and for \(1\le j\le\lfloor d/2\rfloor\),
\[
T_j(d,q,\varepsilon)=
\frac{\displaystyle\prod_{i=0}^{j-1}I(d-2i,q,\varepsilon)}
{\displaystyle\prod_{i=1}^{j}\frac{q^i-1}{q-1}},
\]
where the number of isotropic lines in a nondegenerate \(d\)-space is
\[
I(d,q,\varepsilon)=
\begin{cases}
\dfrac{q^{d-1}-1}{q-1},&d\text{ odd},\\[3pt]
\dfrac{(q^{d/2-1}+\varepsilon)(q^{d/2}-\varepsilon)}{q-1},&d\text{ even}.
\end{cases}
\]
The sign of every nondegenerate even-dimensional quotient is inherited unchanged when a hyperbolic plane is removed. Then the complete, dimension-resolved census is
\[
\boxed{N_0=1,\qquad N_r={n-1\brack r-1}_q+T_r(n,q,\varepsilon)-\delta\,T_{r-1}(n-2,q,\varepsilon),\quad 1\le r\le n.}
\]
Every subalgebra is **either** a subspace containing \(\mathbb F_q u\) **or** a totally \(B\)-isotropic subspace; the subtraction removes their intersection. In particular, for fixed \(q,n\), the single count \(N_1\) determines both the even-dimensional Witt sign (when applicable) and whether the square generator is isotropic.

The subalgebra lattice is modular precisely when \(n\le2\). In dimension two it is distributive precisely when either \(B\) is anisotropic, or \(B\) is hyperbolic and \(u\) is isotropic. For \(n\ge3\) it is not modular. The modularity assertion for the *solvable*, isotropic-generator portion was previously established; here it is incorporated into the full structural census, and the non-solvable portion is also handled.

## Assumptions and scope

A subalgebra means an \(\mathbb F_q\)-linear subspace closed under multiplication, not necessarily one admitting its own natural basis. A symmetric bilinear form is nondegenerate when its Gram matrix is invertible. An evolution algebra has a basis \(e_1,\ldots,e_n\) with \(e_ie_j=0\) whenever \(i\ne j\). Its annihilator is zero exactly when no natural-basis square vanishes. If its square is the line \(\mathbb F_q u\), one has \(e_i^2=a_i u\) with every \(a_i\ne0\); the diagonal form \(B(e_i,e_i)=a_i\), \(B(e_i,e_j)=0\) for \(i\ne j\), recovers multiplication. Conversely, every nondegenerate symmetric form in odd characteristic has an orthogonal basis, giving an evolution-algebra natural basis. Thus the hypotheses describe exactly the stated class, not a proper special case.

The determinant sign is independent of the basis. In odd dimension, only the dimension enters the isotropic-line counts. In even dimension, the quadratic-form sign distinguishes the split and nonsplit types; it remains unchanged under replacement of \(B\) by a nonzero scalar multiple.

## Proof

**1. Subalgebra dichotomy.** For any subspace \(W\subseteq V\), its product span is
\[
WW=\operatorname{span}\{B(x,y)u:x,y\in W\}.
\]
If \(u\in W\), then automatically \(WW\subseteq W\). If \(u\notin W\), closure forces \(B(x,y)=0\) for every \(x,y\in W\), and conversely this condition makes \(WW=0\). In odd characteristic, vanishing on every pair is equivalent to vanishing of the quadratic form on \(W\). Thus the subalgebra poset is the union of the interval \([\mathbb F_q u,V]\) and the lattice-ordered set of totally isotropic subspaces, with intersections and generated-algebra joins taken in the ambient subalgebra lattice.

**2. Counting the interval and intersection.** The interval \([\mathbb F_q u,V]\) has \({n-1\brack r-1}_q\) members of dimension \(r\), by passing to \(V/\mathbb F_q u\). If \(B(u,u)\ne0\), no totally isotropic subspace can contain \(u\). If \(B(u,u)=0\), the totally isotropic \(r\)-subspaces containing \(u\) are precisely the inverse images of totally isotropic \((r-1)\)-subspaces of the nondegenerate quotient \(u^\perp/\mathbb F_q u\), whose dimension is \(n-2\). Its even-dimensional Witt sign is the same as that of \(V\), because a hyperbolic plane has been removed. Therefore the intersection count is \(\delta T_{r-1}(n-2,q,\varepsilon)\). Inclusion–exclusion proves the boxed formula once \(T_r\) is evaluated.

**3. Derivation of the polar-space counts.** Diagonalize \(B\), write \(Q(x)=B(x,x)\), and let \(Z_d\) be the number of zeros of \(Q\) on a nondegenerate \(d\)-dimensional space. Summing a nontrivial additive character \(\psi\) against the zero indicator gives
\[
Z_d=q^{-1}\sum_{t\in\mathbb F_q}\sum_{x\in\mathbb F_q^d}\psi(tQ(x)).
\]
For \(t\ne0\), the inner sum is \(\chi_q(t)^d\chi_q(\det B)G^d\), where the standard one-dimensional quadratic Gauss sum satisfies \(G^2=\chi_q(-1)q\). Hence
\[
Z_d=\begin{cases}
q^{d-1},&d\text{ odd},\\
q^{d-1}+(q-1)\varepsilon q^{d/2-1},&d\text{ even}.
\end{cases}
\]
Removing the zero vector and dividing by \(q-1\) gives exactly \(I(d,q,\varepsilon)\). To enumerate totally isotropic subspaces, count incidences between a totally isotropic \((j-1)\)-space \(U\) and a totally isotropic \(j\)-space containing it. By \(U^\perp/U\), the number of possible extending isotropic lines is \(I(d-2j+2,q,\varepsilon)\), independent of \(U\). Every \(j\)-space contains \((q^j-1)/(q-1)\) hyperplanes, so
\[
T_j(d,q,\varepsilon)\frac{q^j-1}{q-1}
=T_{j-1}(d,q,\varepsilon)I(d-2j+2,q,\varepsilon).
\]
Starting at \(T_0=1\), this proves the finite product stated above, including the automatic vanishing beyond the Witt index.

**4. Lattice threshold.** When \(n=2\), every proper nonzero subalgebra is a line, so the lattice has height two with \(N_1=1+I(2,q,\varepsilon)-\delta\) atoms. It is always modular and is distributive exactly when it has at most two atoms. A nonsplit plane has no isotropic lines, giving one atom; a split plane has two isotropic lines, giving two atoms if \(u\) is isotropic and three atoms if \(u\) is anisotropic. The latter case has the nondistributive diamond.

For \(n\ge3\), choose an isotropic vector \(w\) outside \(\mathbb F_q u\); there are at least \(q+1\) isotropic lines in every nondegenerate space of such dimension. Choose an isotropic \(f\) with \(B(w,f)=1\), and write \(V=\operatorname{span}(w,f)\perp V_0\), where \(\dim V_0=n-2\). There are exactly \(q^{n-2}\) normalized isotropic vectors
\[
x=f+v-\tfrac12 B(v,v)w,\qquad v\in V_0,
\]
with \(B(w,x)=1\). The plane \(Z=\operatorname{span}(u,w)\) contains at most one such \(x\): all vectors of \(Z\) with \(B(w,x)=1\), if any, form an affine line in the direction \(w\), along which \(Q\) has exactly one zero. Since \(q^{n-2}>1\), choose an \(x\notin Z\). Let \(U=\mathbb F_q w\), \(X=\mathbb F_q x\). Both are subalgebras, \(U\subseteq Z\) (a subalgebra containing \(u\)), and \(X\cap Z=0\). Because \(B(w,x)=1\), their generated subalgebra contains \(u\), so \(U\vee X=\operatorname{span}(w,x,u)\). It follows that
\[
(U\vee X)\cap Z=Z\ne U=U\vee(X\cap Z),
\]
violating the modular identity. This proves the sharp dimension threshold. For \(n=1\), outside the stated range, the two-element lattice is distributive.

**5. Parameter recovery.** The line count is \(N_1=1+I(n,q,\varepsilon)-\delta\). When \(n\) is odd, \(I\) depends only on \(q,n\), so \(N_1\) determines \(\delta\). When \(n=2m\), the two signs have isotropic-line counts differing by \(2q^{m-1}\ge2\). The correction \(\delta\) changes the value by at most one, so the sets of possible \(N_1\)-values for the two signs do not overlap, and \(N_1\) also determines \(\delta\). Nothing here asserts the algebra itself is classified by this census.

## Verification

The included dependency-free `verify.py` enumerates all vector subspaces in reduced row-echelon form and tests closure under actual products \(B(x,y)u\) on their basis vectors. It separately computes the Gaussian and polar-space formulas. Prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7\) and the nonsplitting field \(\mathbb F_9=\mathbb F_3[\omega]/(\omega^2+1)\) were tested, with multiple determinant signs and both isotropic and anisotropic choices of \(u\) where available. Running `python verify.py` produced `VERIFY_OK cases= 75 subspaces_examined= 81142`.

For example, with \(q=3\), \(n=3\), and \(B\) the identity form, the counts \((N_0,N_1,N_2,N_3)\) are \((1,5,4,1)\) for anisotropic \(u\) and \((1,4,4,1)\) for isotropic \(u\). These computations check finite instances only; the proof above gives the unrestricted claims.

## Relationship to prior work

The finite-field result is prompted by Question 13 on subalgebra lattices in Kaygorodov–Martín González–Viruel's October 2026 survey. Earlier classification of commutative algebras with one-dimensional square supplies the bilinear-form framework, not the dimension-resolved subalgebra counts. Ladra–Páez-Guillán–Pérez-Rodríguez (2025), Lemma 6.1, already proves the modular/distributive threshold for the **solvable nonnilpotent** one-dimensional-derived case; this is explicitly acknowledged rather than claimed as new. Ladra–Pérez-Rodríguez (2026) extends modularity results primarily in nilpotent and supersolvable regular settings. González Nevado (2025) analyzes order structures of evolution subalgebras and ideals, but its examined sections do not give the finite-field polar-space subalgebra census.

The new quantitative statement is the complete finite-field subalgebra rank profile across both isotropic- and anisotropic-generator cases, with overlap subtraction; the non-solvable lattice conclusion and line-count recovery accompany it. Standard Gaussian coefficients and finite orthogonal-space point counts are used as established ingredients and reproved in the needed normalization.

## Limitations

The hypotheses require finite fields of odd characteristic, a zero annihilator, and a one-dimensional square; characteristic two and degenerate bilinear forms require different counting. The result concerns ordinary subalgebras, not exclusively natural-basis evolution subalgebras. Previously known modularity in the solvable portion is not a new contribution. The literature search and examined primary texts do not establish global novelty, and equivalent formulas in unindexed sources remain possible. The accompanying verifier is finite and not an independent proof or audit.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, first posted 2026-10-15, Question 13. https://arxiv.org/abs/2610.22248
2. M. Ladra, P. Páez-Guillán and A. Pérez-Rodríguez, *On the subalgebra lattice of solvable evolution algebras*, arXiv:2502.05619v1 (2025), Lemma 6.1. https://arxiv.org/abs/2502.05619
3. M. Ladra and A. Pérez-Rodríguez, *Further results on modularity in evolution algebras*, arXiv:2604.01111v1 (2026). https://arxiv.org/abs/2604.01111
4. A. González Nevado, *Order Structures around Evolution Algebras*, arXiv:2505.01444v1 (2025). https://arxiv.org/abs/2505.01444
5. *Commutative Algebras with One-Dimensional Square*, Mediterranean Journal of Mathematics 22, 48 (2025), DOI:10.1007/s00009-025-02812-7. https://doi.org/10.1007/s00009-025-02812-7
