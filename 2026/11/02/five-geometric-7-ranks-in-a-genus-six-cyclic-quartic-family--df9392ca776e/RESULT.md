# Five geometric \(7\)-ranks in a genus-six cyclic-quartic family

## Finding
Let \(k=\overline{\mathbb F}_7\). For every \((a,b,c)\in k^3\) for which \(F(x)=x^5+ax^3+bx+c\) is squarefree, let \(C_{a,b,c}\) be the smooth projective model of \(y^4=F(x)\). Put
\[
P=a^4b+6a^2b^2+6ac^2+2b^3,\qquad E=ab^2+c^2,\qquad W=c(a^2+2b).
\]
The Jacobian's geometric \(7\)-rank is
\[
f_7(C_{a,b,c})=2\mathbf1_{P\ne0}+\begin{cases}
2,&aE\ne0,\\
1,&aE=0,\ W\ne0,\\
0,&aE=W=0.
\end{cases}
\]
Every value \(0,1,2,3,4\) occurs, but no member has \(7\)-rank \(5\) or \(6\). The entire smooth rank-zero locus is \(\{a=b=0,\ c\ne0\}\), and the entire smooth rank-one locus is the disjoint union of two irreducible smooth curves
\[
L_r^\circ=\{(a,b,c)=(t^2,rt^4,2t^5):t\in k^\times\},\qquad r^2=3.
\]
Each closure \(\overline{L_r^\circ}\subset\mathbb A^3\) is a rational monomial cusp \(\operatorname{Spec}k[t^2,t^5]\), cut out by \(b=ra^2\) and \(c^2=4a^5\). The two closures meet only at the singular-model parameter \((0,0,0)\). In particular, neither rank-one curve specializes to a smooth rank-zero fiber inside this coefficient space.

For the Jacobian \(a\)-number, define \(\rho=2\) if \(aE\ne0\), \(\rho=0\) if \(a=c=0\), and \(\rho=1\) otherwise. Then
\[
a(C_{a,b,c})=5-\mathbf1_{(c,P)\ne(0,0)}-\rho.
\]
Only \(a\)-numbers \(2,3,4\) occur on the smooth locus. In particular, rank-zero fibers have \(a\)-number \(3\), and the \(a\)-number-four locus is exactly \(\{a=c=0,\ b\ne0\}\).

## Assumptions and scope
All assertions are geometric over the algebraic closure of \(\mathbb F_7\), for coefficient-marked members of the stated three-parameter family; no identification of isomorphism classes is claimed. The smooth locus is \(U=\{\Delta\ne0\}\), where the quintic discriminant is
\[
\begin{aligned}
\Delta={}&3a^5c^2+2a^4b^3+3a^3bc^2-2a^2b^4\\
&-2ab^2c^2-3b^5+3c^4\quad\text{in }\mathbb F_7[a,b,c].
\end{aligned}
\]
Because the quintic has five simple finite roots and one point over infinity, the tame degree-four cover has six fully ramified branch points. Riemann--Hurwitz gives \(2g-2=-8+6(3)=10\), so \(g=6\).

## Proof
Write \(\omega_{j,i}=x^i\,dx/y^j\). The six regular differentials are \(\omega_{1,0}\), \(\omega_{2,0}\), \(\omega_{2,1}\), \(\omega_{3,0}\), \(\omega_{3,1}\), \(\omega_{3,2}\), because their valuations at infinity are \(5j-4i-5\ge0\). Their number equals the genus, so they form a basis.

For each input \(\omega_{j,i}\), set \(j'\in\{1,2,3\}\) by \(7j'\equiv j\pmod4\) and set \(s=(7j'-j)/4\). Cartier's coefficient-extraction identity gives
\[
\mathcal C(\omega_{j,i})=\sum_{\ell}\bigl([x^{7(\ell+1)-1-i}]F(x)^s\bigr)^{1/7}\omega_{j',\ell}.
\]
The summation includes only basis indices in the target character. This is \(7^{-1}\)-semilinear, so its stable image, rather than its first image, computes \(7\)-rank.

The \(j=3\) to \(j=1\) block is the row \((0,1,0)\), since the relevant coefficients of \(F\) are those of degrees \(6,5,4\). The \(j=1\) to \(j=3\) block is a column with entries the seventh roots of the coefficients of degrees \(6,13,20\) in \(F^5\). Its middle entry has seventh power \(5P\), and its last entry has seventh power \(5c\). The resulting two-character cyclic block has stable dimension two if \(P\ne0\) and zero if \(P=0\): after two Cartier steps, the only potentially invertible scalar is \((5P)^{1/7}\). The first-step rank of this block is \(1+\mathbf1_{(c,P)\ne(0,0)}\). When \(c=P=0\), its first map from \(j=1\) vanishes because the degree-six coefficient also vanishes.

The self-mapped two-dimensional \(j=2\) block has its coefficient matrix (before entrywise seventh roots)
\[
3\begin{pmatrix}W&E\\a&0\end{pmatrix}.
\]
Its determinant is \(-9aE\). For \(aE\ne0\) it is semilinearly invertible, contributing stable rank two. When \(aE=0\), its matrix has rank at most one: if \(W\ne0\), its image is preserved nontrivially by further Cartier steps and contributes stable rank one; if \(W=0\), its square is zero and it contributes zero. Its first-step rank is \(2\) when \(aE\ne0\), \(0\) when \(a=c=0\), and \(1\) otherwise. The direct-sum decomposition proves both asserted invariant formulas and their boundary cases.

For the deeper strata, suppose \(f_7=0\). Then \(P=0\), \(aE=W=0\). If \(a=0\), these equations imply \(b=0\) unless \(c=0\), in which latter case \(P=2b^3\) forces \(b=0\) and the polynomial is inseparable at the origin. Hence in \(U\), \(a=b=0\) and \(c\ne0\). If \(a\ne0\), then \(E=0\). Smoothness forces \(b,c\ne0\); \(W=0\) gives \(b=-a^2/2\). The identity \(P=b(a^4+2b^2)+6aE\) gives \(P=3a^4b/2\ne0\), a contradiction. Conversely all \((0,0,c)\), \(c\ne0\), are smooth and rank zero.

For \(f_7=1\), necessarily \(P=aE=0\) and \(W\ne0\). The possibility \(a=0\) would force \(bc\ne0\), hence \(P=2b^3\ne0\); therefore \(a\ne0\), \(E=0\), \(b,c\ne0\). The same identity gives \(b^2=3a^4\); putting \(r=b/a^2\) gives \(r^2=3\), and then \(c^2=4a^5\). Conversely, these equations give \(P=E=0\), with \(W\ne0\), because \(r^2=3\) excludes \(r=-1/2\). On these curves the discriminant simplifies to \(\Delta=(-2r-3)a^{10}\), nonzero for \(a\ne0\), since \(r=2\) is not a root of \(r^2=3\). The parametrizations by \(t\ne0\) follow; each coordinate ring is \(k[t^2,t^5]\), which is integral, and deleting its cusp at \(t=0\) leaves a smooth curve.

To see all ranks occur, smooth prime-field witnesses for \((f_7,a\text{-number})\) include \((a,b,c)=(0,0,1)\mapsto(0,3)\), \((0,1,0)\mapsto(2,4)\), \((0,1,2)\mapsto(3,3)\), and \((1,0,1)\mapsto(4,2)\). Rank one occurs at \((1,r,2)\) for either root \(r^2=3\) in \(\mathbb F_{49}\). Finally, the first-step rank formula and smoothness show that \(a=4\) exactly when \(a=c=0\) and \(b\ne0\); no larger \(a\)-number is possible.

## Verification
Run `python3 verify_symbolic.py` and `python3 verify_fields.py` using Python and SymPy. The first independently expands the required powers, checks their key coefficients and discriminant specialization in characteristic seven. The second independently constructs all six Cartier matrix entries by finite-field polynomial multiplication, iterates the semilinear operator, and compares stable rank and first-step rank with both formulas. It exhaustively examines the \(343\) coefficient triples over \(\mathbb F_7\) and checks \(3500\) deterministic triples over \(\mathbb F_{49}\), including explicit rank-one witnesses.

The geometric assertions over \(k\) follow from exact identities and the case analysis; finite-field tests are consistency checks only.

## Relationship to prior work
Borges and Gonçalves's `arXiv:2212.03987` supplies general methods and explicit arithmetic of Fermat-type \(p\)-ranks, but its main theorem concerns \(y^m=x^n+1\), with additional examples of other forms; it does not state this three-parameter cyclic-quartic stratification. General Cartier identities are classical and not claimed new. A related explicit genus-six family \(y^4=x^5+ux^2+vx+1\) has a different monomial support and rank-degeneration geometry; its classification does not imply these formulas or the two cuspidal rank-one components. The new content is the precise stratification and geometry for the constant-shifted odd-quintic family.

## Limitations
This does not classify geometric isomorphism classes, Newton polygons, Ekedahl--Oort types, or all cyclic-quartic genus-six curves. The rank-one components are described only on the coefficient-marked parameter space. The precise priority status depends on the completeness of indexed and inspected prior literature; unindexed equivalent coefficient calculations remain possible.

## References
- H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, first public version 2022-12-07, https://arxiv.org/abs/2212.03987.
- E. Özman, R. Pries, and C. Weir, *The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line*, Nagoya Mathematical Journal 248 (2022), 865–887, https://doi.org/10.1017/nmj.2022.12 (studies prime-degree cyclic covers; different from this degree-four family).
