# Exact all-height Mahler product of the symmetric double-corner-apex four-cube

## Finding

For each real \(t>0\), define the origin-symmetric four-polytope
\[
P_t=\operatorname{conv}\bigl([-1,1]^4\cup\{\pm(1,1,1+t,1),\ \pm(1,1,1,1+t)\}\bigr),
\quad \mathcal M(t)=\operatorname{vol}_4(P_t)\operatorname{vol}_4(P_t^\circ).
\]
Its Mahler product is given **exactly for every positive height** by the following two rational branches:
\[
\mathcal M(t)=\begin{cases}
-\displaystyle\frac{2(t^2+12t+24)(t^5+4t^4-44t^3-272t^2-464t-256)}{9(t+2)^3(t+4)^2},&0<t\le2,\\[7pt]
\displaystyle\frac{32(t^2+6t+10)(3t^6+26t^5+80t^4+72t^3-88t^2-64t+128)}{9t^3(t+2)^3(t+4)^2},&t\ge2.
\end{cases}
\]
The two branches agree at \(t=2\). For every \(t>0\),
\[
\boxed{\mathcal M(t)>\frac{32}{3}},
\]
with the sharp limiting equalities \(\lim_{t\downarrow0}\mathcal M(t)=\lim_{t\to\infty}\mathcal M(t)=32/3\). Thus this entire one-parameter family obeys the sharp four-dimensional symmetric Mahler lower bound, beyond the interval \(0<t\le12/7\) certified in its motivating source. A combinatorial transition at \(t=2\) changes both the volume polynomials and the polar vertex count: it is 20 for \(0<t<2\), 18 at \(t=2\), and 24 for \(t>2\).

## Assumptions and scope

The polar is always taken about the origin, which lies in the interior of \(P_t\). Volume means four-dimensional Lebesgue volume, and \(t\) is any positive real number. At \(t=0\) the body is exactly the cube. This theorem concerns the displayed two-apex-pair family only, not all centrally symmetric four-polytopes.

## Proof

**1. Explicit vertex-and-facet description.** Let \(C=[-1,1]^4\), \(a=(1,1,1+t,1)\), and \(b=(1,1,1,1+t)\). The primal vertex candidates are the sixteen sign vectors of \(C\), together with \(a,-a,b,-b\). The polar is the finite halfspace intersection
\[
P_t^\circ=\bigl\{y\in\mathbb R^4:\; \epsilon\cdot y\le1\quad(\epsilon\in\{-1,1\}^4),\quad |a\cdot y|\le1,\quad|b\cdot y|\le1\bigr\}.
\]
In each open interval \((0,2)\) and \((2,\infty)\), the determinant-based facet computation in `verification.py` gives a complete polyhedral volume certificate: start with all combinations of four active halfspaces and isolate feasible polar vertices; use sample parameters 1 and 3 to specify the fixed boundary triangulations. Each symbolic polar candidate satisfies **every** defining inequality throughout its whole interval; each primal and polar simplex lies in a supporting hyperplane of the opposite body; and all signed simplex determinants retain strictly positive sign throughout the interval. The checked supporting-face triangulations form closed polyhedral boundaries at their sample values, and their strict determinant signs and supporting incidences preserve the face triangulations throughout the parameter intervals. The proof uses finite exact inequalities in the height parameter, not inference from the sample parameters alone.

**2. Volume formulas.** Taking the oriented sum of four-simplex volumes with the origin as apex, namely \(|\det(v_1,v_2,v_3,v_4)|/24\) over the supporting boundary tetrahedra, and simplifying gives
\[
\operatorname{vol}_4(P_t)=\begin{cases}
\frac23(t^2+12t+24),&0<t\le2,\\[3pt]
\frac43(t^2+6t+10),&t\ge2,
\end{cases}
\]
and
\[
\operatorname{vol}_4(P_t^\circ)=\begin{cases}
-\frac{t^5+4t^4-44t^3-272t^2-464t-256}{3(t+2)^3(t+4)^2},&0<t\le2,\\[4pt]
\frac{8(3t^6+26t^5+80t^4+72t^3-88t^2-64t+128)}{3t^3(t+2)^3(t+4)^2},&t\ge2.
\end{cases}
\]
At the transition \(t=2\), these volumes agree and equal \(104/3\) and \(79/216\), respectively. Their products yield the claimed branches.

**3. Strict Mahler gap, with exact sign certificates.** Subtracting \(32/3\) yields
\[
\mathcal M(t)-\frac{32}{3}=\begin{cases}
-\dfrac{2t\,A(t)}{9(t+2)^3(t+4)^2},&0<t\le2,\\[5pt]
\dfrac{64\,B(t)}{9t^3(t+2)^3(t+4)^2},&t\ge2,
\end{cases}
\]
where
\[
A(t)=t^6+16t^5+76t^4-32t^3-1136t^2-2752t-1920,
\]
\[
B(t)=t^7+19t^6+106t^5+188t^4-128t^3-568t^2+64t+640.
\]
The signs are elementary **polynomial identities**, not numerical observations. With \(t=2u/(1+u)\), \(u\ge0\),
\[
-(1+u)^6 A\bigl(2u/(1+u)\bigr)
=10432u^6+55040u^5+110656u^4+111872u^3+60864u^2+17024u+1920>0.
\]
With \(t=2+u\), \(u\ge0\),
\[
B(2+u)=u^7+33u^6+418u^5+2668u^4+9216u^3+16888u^2+14848u+5216>0.
\]
The denominator factors are positive. This proves strictness for all finite \(t>0\). Substituting the endpoint limits in the rational formulas proves sharpness. \(\square\)

## Verification

Run `python verification.py` with SymPy, NumPy and SciPy installed. It generates the exact signed determinant formulas, checks every proposed polar vertex against all inequalities symbolically over each full parameter interval, checks positive supporting boundary orientations, verifies matching opposite supporting hyperplanes for the primal and polar triangulations, and simplifies the rational volume and Mahler-gap formulas. Numerical convex hulls select combinatorial seeds at \(t=1\) and \(t=3\), but are not used as evidence for polynomial inequalities over intervals: those signs are certified by symbolic nonnegative-coefficient identities. This code checks the finite combinatorial certificate; it is not external proof certification.

## Relationship to prior work

Shen and Dubovski, *A sharp minimum for cube-apex bodies in every dimension* (arXiv:2610.11014v1, first public October 7, 2026), Corollary 4, define exactly the family \(P_t\) above and establish \(\mathcal M(t)>32/3\) only through \(0<t\le12/7\) with a sufficient volume lower certificate. Their paper provides neither the full exact volume-product formulas nor strictness for every positive \(t\), and explicitly bounds the stated corollary at \(12/7\). The present result evaluates the exact primal and polar volumes across the genuine \(t=2\) combinatorial transition, thereby extending that concrete example's sharp Mahler comparison to every height. Existing four-dimensional Mahler results for different symmetry families do not automatically imply it.

## Limitations

The established inequality concerns only the explicit symmetric two-apex-pair family; it makes no claim about the unresolved general four-dimensional symmetric Mahler conjecture. The combinatorial exact-volume calculation depends on the supplied finite symbolic checker, which a reader can replay or translate into an independent polyhedral derivation. Other historical derivations of the same one-parameter volume product may exist; no independent external audit or exhaustive priority certification is claimed.

## References

1. H. Shen and P. B. Dubovski, *A sharp minimum for cube-apex bodies in every dimension*, arXiv:2610.11014v1 (October 7, 2026), Theorem 3 and Corollary 4.
2. R. Karasev, *Mahler’s conjecture for some hyperplane sections*, Israel J. Math. 241 (2021), 795–815. Background for some other cube-apex configurations; no all-height two-apex-pair formula asserted here.
3. F. Fradelizi, M. Meyer and A. Zvavitch, *Volume product*, in *Harmonic Analysis and Convexity* (2023), pp. 163–222. Background on the Mahler problem.
