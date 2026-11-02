# An exact characteristic-two rank stratification for a genus-four cyclic trigonal family

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). For all \(a,b\in k\), let \(C_{a,b}\) denote the smooth projective model of
\[
y^3=f_{a,b}(x),\qquad f_{a,b}(x)=x^5+ax^3+bx+1.
\]
Every member is a smooth genus-four curve. Its geometric Jacobian \(2\)-rank \(f_2\) and its \(a\)-number satisfy the **complete coefficient-marked classification**
\[
(f_2(C_{a,b}),a(C_{a,b}))=
\begin{cases}(0,2),&a=0,\\(2,2),&a\ne0.\end{cases}
\]
Equivalently, the **set-theoretic** rank-zero locus in the smooth coefficient plane \(\mathbb A_k^2\) is \(\{a=0\}\), with reduced underlying subscheme a line; this does not claim a scheme-theoretic determinantal multiplicity. More geometrically, if \(r(a,b)\) is the number of distinct roots over \(k\) of the ordinary derivative \(f'_{a,b}\), then
\[
f_2(C_{a,b})=2(r(a,b)-1).
\]
In particular, for each \(q=2^m\) there are exactly \(q\) ordered coefficient pairs giving geometric rank zero and \(q(q-1)\) giving rank two over \(\mathbb F_q\). These are marked-equation counts, not counts of isomorphism classes.

## Assumptions and scope
All geometric invariants refer to the Jacobian after base change to \(k\), not solely rational torsion over a finite base field. The cyclic degree-three map is \(x:C_{a,b}\to\mathbb P^1\); its characteristic-two polynomial critical points are the roots of \(f'_{a,b}\), **not** ramification points of the map \(x\). The \(a\)-number is \(\dim_k\ker\mathcal C\), where \(\mathcal C\) is the Cartier operator on global regular differentials. The \(2\)-rank is the eventual rank of the iterated Cartier operator, equivalently \(\operatorname{rk}\mathcal C^4\) in genus four.

## Proof
**Smoothness and genus.** In characteristic two,
\[
f'_{a,b}(x)=x^4+ax^2+b,\qquad f_{a,b}(x)=x f'_{a,b}(x)+1.
\]
Thus \(f_{a,b}\) and its derivative are relatively prime for every \((a,b)\), even when \(f'_{a,b}\) has repeated roots. The polynomial has five distinct geometric zeroes. Because \(3\) is prime to the characteristic and to the pole order \(5\), the degree-three Kummer map is totally (tamely) ramified above these five points and infinity. Riemann–Hurwitz yields
\[
2g-2=3(-2)+6(3-1)=6,
\]
so \(g=4\); the smooth projective normalization exists and the affine curve is smooth.

**Differential basis.** The four regular forms are
\[
e_1=\frac{dx}{y},\quad e_2=\frac{dx}{y^2},\quad e_3=\frac{x\,dx}{y^2},\quad e_4=\frac{x^2\,dx}{y^2}.
\]
At a finite branch point with parameter \(y\), \(\operatorname{ord}(dx)=2\), so each form is regular. At infinity, the valuations of \((x,y,dx)\) are \((-3,-5,-4)\), giving form orders \((1,6,3,0)\), respectively. At unramified finite points the forms are regular. They are linearly independent (the coefficients of \(1/y\) and \(1/y^2\) belong to distinct eigenspaces for the cyclic automorphism), hence form a basis of the four-dimensional space of regular differentials.

**Exact Cartier action.** Cartier is additive and \(2^{-1}\)-linear: \(\mathcal C(h^2\omega)=h\mathcal C(\omega)\), \(\mathcal C(dx)=0\), and \(\mathcal C(x\,dx)=dx\). Since \(y^3=f_{a,b}(x)\),
\[
\mathcal C\left(\frac{dx}{y}\right)
=\frac{1}{y^2}\mathcal C(f_{a,b}(x)\,dx)
=\frac{(x^2+\sqrt a\,x+\sqrt b)\,dx}{y^2}.
\]
The second identity extracts odd powers of \(x\) in \(f_{a,b}\). The remaining three images follow immediately from factoring the squares of \(1/y\):
\[
\mathcal C(e_1)=e_4+\sqrt a\,e_3+\sqrt b\,e_2,\qquad
\mathcal C(e_2)=0,\quad\mathcal C(e_3)=e_1,\quad\mathcal C(e_4)=0.
\]
Write \(w=e_4+\sqrt a\,e_3+\sqrt b\,e_2\). The vectors \(e_1,w\) are independent for every \(a,b\), so \(\operatorname{Im}\mathcal C=\langle e_1,w\rangle\) has dimension two and \(a(C_{a,b})=4-2=2\). On this image,
\[
\mathcal C(e_1)=w,\qquad \mathcal C(w)=a^{1/4}e_1.
\]
If \(a=0\), iteration gives ranks \((2,1,0,0)\) for \(\mathcal C,\mathcal C^2,\mathcal C^3,\mathcal C^4\), hence geometric \(2\)-rank zero. If \(a\ne0\), the restriction to \(\langle e_1,w\rangle\) is bijective, so all four iterated ranks are two and the geometric \(2\)-rank is two.

**Critical-point interpretation.** There is a factorization
\[
f'_{a,b}(x)=(x^2+\sqrt a\,x+\sqrt b)^2.
\]
When \(a=0\), this derivative has one distinct geometric root (with multiplicity four). When \(a\ne0\), the quadratic has nonzero derivative \(\sqrt a\) and thus two distinct roots (each doubled in \(f'_{a,b}\)). The preceding rank calculation gives \(f_2=2(r-1)\). Counting coefficient pairs in \(\mathbb F_q^2\) by whether \(a=0\) yields the finite-field formulas.

## Verification
Run `python3 verify_cartier.py` in a Python 3 environment with the standard library; no external packages or external data are required. The verifier independently constructs finite fields of cardinalities \(2,4,8,16,32\) and checks the exact semilinear Cartier ranks for all 1,364 ordered coefficient pairs. It also computes sample zeta numerators from point counts over extensions of \(\mathbb F_2\). Its terminating marker is `ODD_TRIGONAL_CHAR2_CARTIER_STABLE_RANK_AND_ZETA_OK`. These computations corroborate, but are not used to infer, the unrestricted proof above.

## Relationship to prior work
Dragutinović (2023), especially Section 5, studies Newton and Ekedahl–Oort strata of genus-four curves in characteristic two and supplies a general method for Hasse–Witt calculations of genus-four canonical models. The present result gives the complete characteristic-two \(2\)-rank stratification of this specific two-parameter smooth cyclic trigonal family, including its polynomial critical-point interpretation and exact marked coefficient counts.

Sankar (2019/2020), Section 2.2, building on Elkin, proves a general characteristic-two superelliptic \(a\)-number formula and an ordinarity criterion. **The constant \(a\)-number two and non-ordinarity in our family are compatible with, and already implicit in, that general theorem. They are not independent novelty claims.** The added statement concerns the *stable*, not one-step, Cartier rank and its exact parameter divisor; the cited general \(a\)-number formula does not imply which parameter values have geometric \(2\)-rank zero.

## Limitations
This result is about the given coefficient-marked family, not all cyclic trigonal genus-four curves or unmarked moduli isomorphism classes. Rank zero is not asserted to imply supersingularity; no Newton polygon or full Ekedahl–Oort type is determined. Critical points refer only to the polynomial \(f_{a,b}\). The published-priority comparison cannot exclude every unindexed previous specialization of general Cartier formulas.

## References
- D. Dragutinović, *Supersingular curves of genus four in characteristic two*, arXiv:2301.12897v1 (first public 2023-01-30), Sections 1 and 5. https://arxiv.org/abs/2301.12897
- S. Sankar, *Proportion of ordinarity in some families of curves over finite fields*, arXiv:1904.12173v1 (first public 2019-04-27), Section 2.2, revised v2 2020. https://arxiv.org/abs/1904.12173
