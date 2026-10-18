# Exact two-cycle rigidity and a doubly superattracting resonance in a rational planar map

## Finding

Consider the rational planar family
\[
F_{a,c}(x,y)=\left(x\left(1+\frac{a}{1+y^2}\right),\ y+cx\right),\qquad (x,y)\in\mathbb R^2,
\]
for arbitrary real \(a\) and nonzero real \(c\). This is the zero-offset subfamily of the map introduced in [1]. **There is precisely one primitive period-two orbit if \(a<-2\), and none if \(a\ge-2\).** For \(a<-2\), put
\[
u=\sqrt{-\frac a2-1}>0,\qquad
P=\left(-\frac{2u}{c},u\right),\qquad Q=\left(\frac{2u}{c},-u\right).
\]
The unique two-cycle is \(P\mapsto Q\mapsto P\). Its return Jacobian at either point is exactly a scalar matrix:
\[
D(F_{a,c}^{\,2})(P)=D(F_{a,c}^{\,2})(Q)
=\mu(a)I_2,\qquad
\mu(a)=-7-\frac{16}{a}.
\]
Thus **the orbit is a hyperbolic attracting two-cycle precisely for \(-8/3<a<-2\)**, is a hyperbolic repelling two-cycle for \(a<-8/3\), and has both return multipliers equal to \(-1\) at \(a=-8/3\). At the unique parameter \(a=-16/7\), both return multipliers vanish and the full return derivative is the zero matrix. Consequently the return map converges at least quadratically from sufficiently close initial conditions at that parameter. The endpoints \(a=-8/3\) and \(a=-2\) are not claimed to possess nonlinear stability properties beyond those explicitly proved.

## Assumptions and scope

The phase space is the entire real plane, no positivity or boundedness restriction. Parameters satisfy \(a\in\mathbb R\), \(c\in\mathbb R\setminus\{0\}\), and the additive coefficients of the parent four-parameter family are identically zero. A *primitive two-cycle* is an unordered pair of distinct points satisfying \(F(P)=Q\) and \(F(Q)=P\); fixed points are excluded. Every point on \(x=0\) is fixed. Hyperbolic attraction/repulsion refers to the map's two-step derivative, not a claim that every initial point lies in its basin. The linear rescaling \((x,y)\mapsto(cx,y)\) conjugates every nonzero choice of \(c\) to the same \(c=1\) map.

## Proof

Let a primitive two-cycle have consecutive points \((x_0,y_0)\) and \((x_1,y_1)\). From the second coordinate of the map and its return,
\[
y_1-y_0=c x_0,\qquad y_0-y_1=c x_1,
\]
so \(x_1=-x_0\). If \(x_0=0\), then both points are equal and fixed, contrary to primitivity. Hence \(x_0\ne0\). The first-coordinate equations give
\[
1+\frac{a}{1+y_0^2}=-1,
\qquad 1+\frac{a}{1+y_1^2}=-1,
\]
so \(a=-2(1+y_0^2)=-2(1+y_1^2)\). Because \(c x_0\ne0\), the two ordinate values are distinct and have the same square. Necessarily \(y_1=-y_0\ne0\). With \(u=|y_0|\), one obtains \(a=-2(1+u^2)<-2\) and \(x_0=-2y_0/c\). Both signs of \(y_0\) describe the same unordered orbit \(\{P,Q\}\). Conversely these two explicit points map to one another for every \(a<-2\), proving the global classification, including exclusions at \(a=-2\).

The derivative of the map at any finite point is
\[
DF_{a,c}(x,y)=
\begin{pmatrix}
1+\dfrac{a}{1+y^2}&-\dfrac{2axy}{(1+y^2)^2}\\
c&1
\end{pmatrix}.
\]
At the two-cycle points, \(xy=-2u^2/c\), so both one-step Jacobians coincide with
\[
M=\begin{pmatrix}-1&-\dfrac{8u^2}{c(1+u^2)}\\ c&1\end{pmatrix},
\qquad \operatorname{tr}M=0.
\]
Multiplication, or Cayley–Hamilton in dimension two, gives
\[
M^2=\frac{1-7u^2}{1+u^2}I_2
=\left(-7-\frac{16}{a}\right)I_2.
\]
The multiplier \(\mu\) decreases strictly from \(1\) to \(-7\) as \(u^2\) increases from zero to infinity, because
\[
\frac{\mathrm d}{\mathrm d(u^2)}\frac{1-7u^2}{1+u^2}
=-\frac{8}{(1+u^2)^2}<0.
\]
It equals zero only at \(u^2=1/7\), equivalently \(a=-16/7\), and equals \(-1\) only at \(u^2=1/3\), equivalently \(a=-8/3\). These identities give precisely the attracting and repelling ranges stated above, by the standard local contraction and inverse-function criteria for hyperbolic sinks and sources. At \(a=-16/7\), differentiability of \(F^2\) with locally bounded second derivatives and \(D(F^2)(P)=0\) imply \(\|F^2(P+h)-P\|\le C\|h\|^2\) for small \(h\), and analogously at \(Q\). The quadratic estimate itself implies sufficiently local superattraction. At \(a=-8/3\), the return derivative is \(-I_2\) and is nonhyperbolic; the argument makes no nonlinear classification there.

## Verification

The accompanying `verify.py` checks the return-matrix identity symbolically, the two exact degeneracy parameters, the derivative of the multiplier, and 28 parameter points with exact-rational orbit and Jacobian arithmetic. It also compares exact contraction conditions at 200 parameter samples. Executed with SymPy 1.14.0, it reported `PASS: 544 exact symbolic and rational checks`. These finite checks do not establish the global theorem; the unrestricted parameter range and global orbit census follow from the equations proved above. The check can be rerun with `python verify.py` after installing `requirements.txt`.

## Relationship to prior work

Zhang, Liu, Wei, Jiang and Bi [1] introduce the parent rational map, analyze its fixed lines and fixed-point Jacobians, and numerically exhibit an attracting two-cycle around \(a=-2.1\) for \(b=d=0\), \(c=0.1\). Their numerical phase portraits show higher-period behavior near \(a=-2.7\). Those observations, the model, and the fixed-line geometry are prior art, not new findings. The present theorem turns that observed period-two window into a full-plane, all-parameter count and exact two-step stability law. Crucially, the return derivative is scalar, so both multipliers simultaneously cross \(-1\), with a doubly superattracting point at \(a=-16/7\). The parameter dependence of \(c\) disappears by explicit conjugacy.

Other exact two-cycle studies of the Duffing, Rulkov, Tinkerbell and Bogdanov maps concern different recurrences and neither imply nor contain this family-specific cancellation. Related investigations of this very rational family at \(-1\le a<0\) in a positive quadrant and at \(a>0\) describe global orbit escape, rather than the \(a<-2\) periodic regime. The classification tools (solving return equations and linearizing) are standard; novelty is claimed only for the exact statement about this particular map.

## Limitations

No period-four existence or stability at the double \(-1\) point is established, and no attractor basin, chaos, global invariant probability, or stability of the line of fixed points is classified. The theorem requires exactly zero additive offsets; no persistence is asserted when they are perturbed. A search of the accessible indexed literature found no earlier equivalent result, but an unindexed calculation or a broader theorem specializing to this map could affect historical priority. The dates printed on the publisher's various landing pages distinguish issue publication from manuscript acceptance inconsistently; the first unambiguous public issue-release date of February 17, 2022 is used for source dating.

## References

[1] L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, and Q.-S. Bi, “A class of two-dimensional rational maps with self-excited and hidden attractors,” *Chinese Physics B* **31** (2022), 030503, DOI: 10.1088/1674-1056/ac4025. Full open text: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml ; publisher issue metadata: https://cpb.iphy.ac.cn/CN/10.1088/1674-1056/ac4025 .
