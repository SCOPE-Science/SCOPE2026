# An exact algebraic upper obstruction for Liu's pedal-inradius parameter problem
## Finding
Let \(k_{\max}\) be the supremum of real parameters \(k\) for which
\[
2(k+2)r_p\le R+kr
\]
holds for every nondegenerate Euclidean triangle and every interior point. Here \(R\) and \(r\) are the circumradius and inradius of the reference triangle, and \(r_p\) is the inradius of the pedal triangle. Then
\[
k_{\max}\le \kappa,
\qquad
27\kappa^3-108\kappa^2-720\kappa-800=0,
\]
where the cubic has exactly one real root and
\[
\kappa=7.867924903656\ldots .
\]
This supplies an exact algebraic upper obstruction close to the numerical value about \(7.88\) reported with the original problem.

More explicitly, let \(u_*\in(0,1)\) be the positive root of
\[
125u^6-81u^4+39u^2-11=0,
\]
and set
\[
v_*=\frac{153-250u_*^5+1125u_*^4-88u_*^3-354u_*^2-166u_*}{120}.
\]
Then \(0<v_*<u_*<1\). Define
\[
h_*=\frac{2u_*}{1-u_*^2},
\qquad
y_*=\frac{2v_*}{1-v_*^2}.
\]
For the isosceles triangle \(A=(-1,0)\), \(B=(1,0)\), \(C=(0,h_*)\) and the interior point \(P=(0,y_*)\), equality holds at \(k=\kappa\). The same configuration violates the inequality for every \(k>\kappa\).

## Assumptions and scope
The triangle is nondegenerate and Euclidean, and \(P\) is strictly interior. The pedal triangle is formed from the perpendicular feet from \(P\) to the three side lines. The statement gives an explicit rigorous upper bound for the universal parameter in Liu's Problem 1; it does not prove that this upper bound is globally sharp.

The dated source used for the problem is the RGMIA Research Report Collection, Volume 14 (2011), Article 35. The collection states that its preprints are listed in increasing order of submission date, and the public preprint is stamped `Received 03/05/11`; the date is recorded as 2011-05-03. The later journal version is Jian Liu, *Some new inequalities for an interior point of a triangle*, Journal of Mathematical Inequalities 6(2) (2012), 195--204, DOI `10.7153/jmi-06-20`, primary MSC 51M16.

## Proof
For \(h>0\) and \(0<y<h\), take
\[
A=(-1,0),\qquad B=(1,0),\qquad C=(0,h),\qquad P=(0,y).
\]
Write \(s=\sqrt{1+h^2}\) and \(t=\sqrt{1+y^2}\). The reference triangle has
\[
R=\frac{1+h^2}{2h},
\qquad
r=\frac{h}{s+1}.
\]
The perpendicular foot on \(AB\) is \(D=(0,0)\), while the other two feet are
\[
E=\left(-\frac{h(h-y)}{1+h^2},\frac{h(1+hy)}{1+h^2}\right),
\qquad
F=\left(\frac{h(h-y)}{1+h^2},\frac{h(1+hy)}{1+h^2}\right).
\]
Hence
\[
DE=DF=\frac{h t}{s},
\qquad
EF=\frac{2h(h-y)}{1+h^2},
\]
and the area of \(DEF\) is
\[
\frac{h^2(h-y)(1+hy)}{(1+h^2)^2}.
\]
Dividing by its semiperimeter gives
\[
r_p=\frac{h(h-y)(1+hy)}{(1+h^2)(s t+h-y)}.
\]

Now make the half-angle rationalization
\[
h=\frac{2u}{1-u^2},\quad s=\frac{1+u^2}{1-u^2},
\qquad
y=\frac{2v}{1-v^2},\quad t=\frac{1+v^2}{1-v^2},
\]
with \(0<v<u<1\). Then \(r=u\), and all quantities are rational functions of \(u,v\). The stationary equations for the ratio
\[
K(u,v)=\frac{R-4r_p}{2r_p-r}
\]
on this symmetric two-parameter family have a nontrivial algebraic branch whose Gröbner reduction is
\[
125u^6-81u^4+39u^2-11=0,
\]
\[
250u^5-1125u^4+88u^3+354u^2+166u+120v-153=0.
\]
On that branch the same exact reduction gives
\[
K=\frac{5(125u^4-31u^2+20)}{18}.
\]
Eliminating \(u\) yields
\[
27K^3-108K^2-720K-800=0.
\]
The two cubics involved have negative discriminant, so each has exactly one real root. Exact rational bracketing gives \(0.6405<u_*<0.6406\); the displayed linear relation then gives \(0<v_*<u_*\). Thus the corresponding \(P\) is strictly interior.

Substituting \(v=v_*\) and \(k=K=\kappa\) into
\[
R+kr-2(k+2)r_p
\]
and reducing its numerator by \(125u^6-81u^4+39u^2-11\) gives the zero polynomial. Therefore equality is exact at the stated configuration.

Finally, at equality
\[
2r_p-r=\frac{R-2r}{\kappa+2}.
\]
For the present non-equilateral triangle, Euler's radius inequality is strict; in these coordinates
\[
R-2r=\frac{(3u^2-1)^2}{4u(1-u^2)}>0.
\]
Thus \(2r_p-r>0\). The defect \(R+kr-2(k+2)r_p\) is affine in \(k\) with negative slope \(r-2r_p\), so it is negative for every \(k>\kappa\). This proves \(k_{\max}\le\kappa\).

## Verification
The bundled `verify.py` uses exact symbolic polynomial arithmetic. It checks the algebraic remainders establishing the equality, the elimination polynomial for \(\kappa\), the uniqueness and rational bracketing of the relevant roots, and the strict interior inequalities. It also prints high-precision diagnostic values
\[
u_*=0.6405528403296\ldots,\quad
v_*=0.3393975832095\ldots,
\]
\[
h_*=2.172499462489\ldots,\quad
y_*=0.767165513936\ldots,
\]
without using floating point in the proof certificates.

## Relationship to prior work
Liu's 2011 RGMIA preprint and 2012 journal article pose exactly the problem of maximizing \(k\) in \(2(k+2)r_p\le R+kr\) and state only that computer exploration suggests a value about \(7.88\). The present statement does not claim the global optimum; it gives a closed algebraic configuration proving the rigorous upper bound \(k_{\max}\le7.867924903656\ldots\).

A later full paper by Liu, *On inequality \(R_p<R\) of the pedal triangle*, Mathematical Inequalities & Applications 16(3) (2013), 701--715, DOI `10.7153/mia-16-53`, was inspected because it studies the same pedal-triangle radii. Its main results concern \(R_p<R\), refinements, and a different list of conjectures; targeted full-text checks found no occurrence of the \(7.88\) parameter or the Problem 1 formula as a solved result. Searches of published-finding corpus for the exact inequality, the numerical endpoint, the cubic, and algebraic-obstruction aliases likewise returned no statement implying the result here.

## Limitations
No lower bound proving validity for every configuration up to \(\kappa\) is established, so the global sharpness of \(\kappa\) remains unproved. The exact algebraic configuration may encode the computer extremizer behind Liu's original approximate remark even though no exact form is stated there. Unindexed or differently phrased prior literature remains a residual originality risk.

## References
1. Jian Liu, *Some New Inequalities for an Interior Point of a Triangle*, RGMIA Research Report Collection 14 (2011), Article 35, `https://rgmia.org/papers/v14/v14a35.pdf`.
2. Jian Liu, *Some new inequalities for an interior point of a triangle*, Journal of Mathematical Inequalities 6(2) (2012), 195--204, DOI `10.7153/jmi-06-20`.
3. Jian Liu, *On inequality \(R_p<R\) of the pedal triangle*, Mathematical Inequalities & Applications 16(3) (2013), 701--715, DOI `10.7153/mia-16-53`.
