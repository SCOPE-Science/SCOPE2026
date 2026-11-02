# The square-zero derivation cone of finite Heisenberg Lie algebras

## Finding

Let \(k\) be an arbitrary field, let \(r\geq 1\), and let \(\mathfrak h_{2r+1}(k)=V\oplus kz\) be the Heisenberg Lie algebra of a split symplectic space \((V,\omega)\), where \(\dim V=2r\) and \([v,w]=\omega(v,w)z\). Define the reduced affine variety
\[
\mathcal Z_r(k)=\{D\in\operatorname{Der}_k(\mathfrak h_{2r+1}):D^2=0\}_{\mathrm{red}}.
\]
For every field, \(\mathcal Z_r\) is geometrically irreducible and rational, of dimension \(r(r+2)\). Its open locus of derivations whose induced map on \(V\) has rank \(r\) is a bundle of invertible symmetric bilinear forms and \(r\)-dimensional central-functionals over the Lagrangian Grassmannian.

For each prime power \(q\) (including even powers), put
\[
I_{r,j}(q)=\prod_{i=0}^{j-1}\frac{q^{2r-2i}-1}{q^{j-i}-1},\qquad
S_j(q)=q^{j(j+1)/2}\prod_{i=1}^{\lceil j/2\rceil}(1-q^{-(2i-1)}),
\]
with empty products equal to \(1\). The exact number of square-zero ordinary derivations whose **full** linear rank is \(s\), for every integer \(0\leq s\leq r\), is
\[
\boxed{T_{r,s}(q)=\sum_{j=0}^{r}I_{r,j}(q)S_j(q)\left(q^j\mathbf 1_{s=j}+(q^{2r-j}-q^j)\mathbf 1_{s=j+1}\right).}
\]
In particular, the total number of such derivations is
\[
\boxed{\sum_{j=0}^{r}I_{r,j}(q)S_j(q)q^{2r-j}.}
\]
No square-zero derivation has rank greater than \(r\). These statements concern ordinary Lie derivations, not derivations compatible with a chosen restricted \(p\)-map.

At \(r=1\), the projectivization of the nonzero square-zero derivation cone is the smooth cubic rational normal scroll \(S(1,2)\subset\mathbb P^4\), in every characteristic. Consequently the affine cone is singular only at its vertex, and its finite-field point count is \(1+(q-1)(q+1)^2\).

## Assumptions and scope

All vector spaces and derivations are defined over the indicated field. The Lie bracket is alternating, including in characteristic \(2\); the chosen symplectic form is nondegenerate. Square-zero means \(D\circ D=0\) as a linear map. The formulas enumerate labelled derivations, not their automorphism-conjugacy classes. The variety assertion is about the underlying reduced locus after base change to an algebraic closure, and not about the possibly nonreduced subscheme cut out by the coordinate equations.

## Proof

**1. Derivation normalization.** The center and derived algebra of \(\mathfrak h\) equal \(kz\), so every derivation has a unique form
\[
D(v)=Av+f(v)z,\qquad D(z)=\lambda z,
\]
with \(A\in\operatorname{End}(V)\), \(f\in V^*\), and \(\lambda\in k\). The Leibniz identity on \(v,w\in V\) is equivalent to
\[
\omega(Av,w)+\omega(v,Aw)=\lambda\omega(v,w).
\]
Now \(D^2(z)=\lambda^2z\), hence \(D^2=0\) forces \(\lambda=0\) over any field. The remaining necessary and sufficient equations are
\[
A\in\mathfrak{sp}(V,\omega),\qquad A^2=0,\qquad f\circ A=0.
\]
There are no additional conditions because the bracket has image in the center.

**2. Isotropic images and symmetric forms.** For such a symplectic \(A\), skew-adjointness gives
\[
\omega(Au,Av)=-\omega(u,A^2v)=0.
\]
Thus \(U=\operatorname{im}A\) is isotropic, \(0\leq j=\dim U\leq r\), and
\[
\ker A=U^\perp.
\]
The latter equality follows from skew-adjointness and dimension. The perfect symplectic pairing identifies \(V/U^\perp\) with \(U^*\), and \(A\) induces an isomorphism \(U^*\to U\). The skew-adjoint condition is precisely symmetry of the associated nondegenerate bilinear form on \(U^*\). Conversely, an isotropic \(j\)-plane and a nondegenerate symmetric bilinear form produce one and only one such \(A\) of rank \(j\). This argument works unchanged in characteristic \(2\); symmetry does **not** mean alternation.

**3. Finite symplectic and symmetric counts.** The number of isotropic \(j\)-planes in dimension \(2r\) is \(I_{r,j}(q)\). Indeed, count ordered independent orthogonal \(j\)-tuples by successively choosing vectors from \(U_i^\perp\setminus U_i\), obtaining factors \(q^{2r-i}-q^i\); divide by the usual number \(\prod_{i=0}^{j-1}(q^j-q^i)\) of ordered bases.

Write \(S_j(q)\) for the number of nonsingular symmetric \(j\times j\) matrices. For a symmetric block matrix with top-left entry \(a\), the case \(a\ne0\) contributes \((q-1)q^{j-1}S_{j-1}\) via the Schur complement. In the case \(a=0\), the adjoining vector must be nonzero. After a change of basis it becomes the first coordinate vector, and nonsingularity is equivalent to that of an independent \((j-2)\)-square symmetric block. This contributes \((q^{j-1}-1)q^{j-1}S_{j-2}\). Hence for \(j\ge2\),
\[
S_j=(q-1)q^{j-1}S_{j-1}+(q^{j-1}-1)q^{j-1}S_{j-2},
\quad S_0=1,\quad S_1=q-1.
\]
Induction gives the displayed product expression, valid in all characteristics.

**4. Functional fibers and full ranks.** For a fixed \(A\) with image \(U\) of dimension \(j\), the equation \(fA=0\) says precisely \(f|_U=0\). There are \(q^{2r-j}\) such functionals. Since \(\ker A\) has dimension \(2r-j\), exactly \(q^j\) of these functionals also vanish on \(\ker A\). For these, the map \(D:V\to V\oplus kz\) has image dimension \(j\); for each other functional it has image dimension \(j+1\). Its value on \(z\) is zero. Multiplication by \(I_{r,j}S_j\) and summation proves the rank and total formulas. When \(j=r\), the second contribution vanishes, as required for a square-zero map on the odd-dimensional space \(\mathfrak h\).

**5. Geometric irreducibility and rationality.** Over an algebraic closure, consider incidence triples \((L,B,f)\), where \(L\subset V\) is Lagrangian, \(B:V/L\to L\) is a symmetric linear map under the symplectic identification \(V/L\cong L^*\), and \(f|_L=0\). They form the total space of a vector bundle of rank \(r(r+1)/2+r\) over the irreducible, rational Lagrangian Grassmannian of dimension \(r(r+1)/2\). The map \((L,B,f)\mapsto(A,f)\), with \(A\) the composition \(V\to V/L\to L\hookrightarrow V\), lands in \(\mathcal Z_r\) and is one-to-one on the open set where \(B\) is invertible, because then \(L=\operatorname{im}A\).

It is also surjective on the underlying geometric points, as follows. Given \((A,f)\), set \(U=\operatorname{im}A\), with \(f|_U=0\). Represent \(f\) by a vector \(w\) under the symplectic pairing. Since \(w\in U^\perp\), the span \(U+kw\) is isotropic and extends to a Lagrangian \(L\). It satisfies \(U\subseteq L\subseteq U^\perp=\ker A\), \(f|_L=0\), and therefore \(A\) factors as a symmetric map \(V/L\to L\). Replacing \(B\) by \(B+tB'\), with \(B'\) suitably chosen to be generically invertible, deforms the given point within the incidence image to points in the full-rank open stratum while keeping \(L\) and \(f\) fixed. Thus the reduced target is the closure of the image of an irreducible open subset; it is geometrically irreducible. On that open set the incidence map is an isomorphism, establishing rationality and
\[
\dim\mathcal Z_r=\frac{r(r+1)}2+\frac{r(r+1)}2+r=r(r+2).
\]
This proof does not assert that the original defining scheme is reduced.

**6. The first projective cone.** For \(r=1\), take coordinates \((a,b,c,u,v)\) with
\[
A=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad f=(u,v).
\]
The conditions are \(a^2+bc=0\), \(au+cv=0\), and \(bu-av=0\). Each nonzero solution has a unique isotropic line \(L\): it is \(\operatorname{im}A\) if \(A\ne0\), or \(\ker f\) otherwise. Its projective coordinates are therefore parametrized by
\[
[a:b:c:u:v]=[-\alpha st:\alpha s^2:-\alpha t^2:-\beta t:\beta s],
\qquad [s:t]\in\mathbb P^1.
\]
With \(\alpha\) and \(\beta\) having respectively degree-two and degree-one coefficient weights, this is the complete scroll embedding of \(\mathbb P(\mathcal O_{\mathbb P^1}(2)\oplus\mathcal O_{\mathbb P^1}(1))\) in \(\mathbb P^4\). Thus the projectivized cone is the smooth rational normal cubic scroll \(S(1,2)\). The affine cone over this smooth non-linear projective variety is smooth away from the vertex and singular at the vertex (its tangent space there is the whole five-dimensional linear span, whereas the cone dimension is three). Finally, \(\#S(1,2)(\mathbb F_q)=(q+1)^2\), giving \(1+(q-1)(q+1)^2\) affine points.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It checks all possible linear maps on the three-dimensional Heisenberg Lie algebra over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) against the original Leibniz identity and the composition-square equations. It also enumerates every quotient-map matrix and compatible central term for \(\mathfrak h_5(\mathbb F_2)\), directly checks the Leibniz identity, and compares the resulting full rank distribution with the formula. It separately enumerates nonsingular symmetric matrices of sizes one through three over each of these fields. Its actual output is recorded in `VERIFICATION.md`.

The checked rank spectra are \((1,9)\), \((1,32)\), and \((1,75)\) for the three-dimensional cases, and \((1,45,330)\) for the five-dimensional binary case. Such finite checks corroborate but do not prove the arbitrary-field geometric result or the all-prime-power formula.

## Relationship to prior work

Feldvoss, Siciliano, and Weigel (2011) investigate the existence of **outer restricted** square-zero derivations and identify a characteristic-two Heisenberg exception; this is a different property from the enumeration and geometry of **all ordinary** square-zero derivations. Barnea and Melnikov (2015) study Borel orbits within the square-zero locus of the **symplectic nilradical** over the complex field. That theory supplies context for the symplectic quadratic condition but does not classify the square-zero derivation cone of Heisenberg algebras with its central-functional fibers. La Rosa and Mancini (2023) describe derivation Lie algebras for two-step nilpotent Leibniz algebras, and cite earlier descriptions for Heisenberg Lie derivations; the formulas here count a nonlinear square-zero subset and describe its geometry over all characteristics. The classifications of isotropic spaces and nonsingular symmetric forms used in the proof are standard inputs and are not separately claimed as discoveries.

## Limitations

This is a statement about ordinary derivations and their linear ranks, not outer-derivation cosets, restricted derivations, conjugacy orbits, or derivations of all two-step nilpotent Lie algebras. The geometric theorem is about reduced varieties; it does not describe the nonreduced scheme structure. No general singular-locus description in dimensions above three is asserted. Related symplectic counts and classical scroll geometry already occur independently in the literature; the claimed combination is specific to Heisenberg derivation cones and is not an assertion of exhaustive publication priority. Independent mathematical audit has not occurred.

## References

1. J. Feldvoss, S. Siciliano, and T. Weigel, *Outer restricted derivations of nilpotent restricted Lie algebras*, arXiv:1102.2629 (first publicly submitted 2011-02-13), https://arxiv.org/abs/1102.2629.
2. N. Barnea and A. Melnikov, *B-orbits of square zero in nilradical of the symplectic algebra*, arXiv:1509.06008 (2015-09-20), https://arxiv.org/abs/1509.06008.
3. G. La Rosa and M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058 (2023-01-26), https://arxiv.org/html/2301.11058v3.
