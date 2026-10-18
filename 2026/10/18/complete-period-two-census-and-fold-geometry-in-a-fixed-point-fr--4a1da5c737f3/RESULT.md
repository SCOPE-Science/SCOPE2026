# Complete period-two census and fold geometry in a fixed-point-free planar map

## Finding

Consider the real planar map introduced by Huynh, Ouannas, Wang, Pham, Nguyen, and Alsaadi:
\[
F(x,y)=\bigl(x+y,\;y-a|y|-xy+bx^2-cy^2+d\bigr),
\qquad a,b,c,d>0.
\]
Set
\[
c_0=\frac12+\frac b4,\qquad
C=d+\frac{4b}{(1+b)^2},\qquad
Q(t)=(c-c_0)t^2+at-C.
\]
There are no fixed points. The **entire set of primitive period-two orbits** consists of precisely one orbit for each positive zero \(t\) of \(Q\):
\[
\left(\frac2{1+b}-\frac t2,t\right)
\longleftrightarrow
\left(\frac2{1+b}+\frac t2,-t\right).
\]
Thus the number of distinct period-two orbits is exactly:

* one if \(c\ge c_0\);
* zero, one, or two if \(c<c_0\), according as
  \[
  \Delta=a^2-4(c_0-c)C
  \]
  is negative, zero, or positive.

For \(c<c_0\) and \(\Delta=0\), the unique period-two orbit is the merger of the two real period-two branches and its second-iterate derivative has a multiplier equal to \(+1\). When \(\Delta>0\), the larger-amplitude branch has a real multiplier strictly greater than \(1\), so it cannot attract locally. For fixed \(a,b,d>0\), as \(c\uparrow c_0\) through \(c<c_0\), the two positive amplitudes obey
\[
t_{\mathrm{small}}=\frac Ca+O(c_0-c),\qquad
 t_{\mathrm{large}}=\frac{a}{c_0-c}-\frac Ca+O(c_0-c).
\]
Hence one branch persists with finite amplitude while the other escapes to infinity; this loss at infinity is distinct from the finite two-cycle merger.

The return multipliers are determined exactly. Define
\[
\alpha=\frac{b-1}{b+1},\qquad
h=\frac{4b}{b+1},\qquad
w=(1+b)t,\qquad
z=a+\left(2c-\frac12\right)t.
\]
The derivative of \(F^2\) on the orbit has trace and determinant
\[
\tau=1+2h+\alpha^2-z^2,\qquad
\delta=(\alpha-h)^2-(w-z)^2.
\]
It is **linearly asymptotically stable**, hence a locally attracting period-two orbit, if and only if all three strict Schur inequalities hold:
\[
1-\tau+\delta>0,\qquad
1+\tau+\delta>0,\qquad
1-\delta>0.
\]
These conditions yield an exact algebraic test at every positive parameter choice and at every period-two root. On a unit-circle multiplier boundary they do not assert nonlinear stability.

For the rational parameters
\[
(a,b,c,d)=\left(2,\frac12,\frac12,\frac{23}{288}\right),
\]
there are exactly two period-two orbits, with amplitudes \(t=1/2\) and \(t=31/2\). The smaller-amplitude cycle is attracting, with Schur expressions \(45/16\), \(35/144\), and \(17/36\); the other is unstable because its first expression is \(-1395/16\). This exhibits coexisting attracting and unstable period-two cycles in a map without any fixed point.

## Assumptions and scope

All coordinates are real and all four parameters \(a,b,c,d\) are strictly positive. An orbit of *primitive period two* is an unordered pair of distinct points exchanged by \(F\); the two points on one cycle are not counted as two cycles. The formula uses \(t>0\), the positive value of the alternating second coordinate. The map is smooth at both points of every such cycle, since neither second coordinate vanishes. All counts include nonhyperbolic merger cases. No global-basin or higher-period classification is claimed.

## Proof

First, a fixed point would have \(y=0\) from its first coordinate, and its second coordinate would then require \(bx^2+d=0\), impossible for positive \(b,d\).

For any primitive two-cycle, write its two points \((u,t)\) and \((v,-t)\). Indeed, the first-coordinate equation along a two-cycle gives \(v-u=y_0\) and \(u-v=y_1\), so the second coordinates are opposite. Their common absolute value cannot vanish, since vanishing would make the pair a fixed point. Exchange the two points if needed so that \(t>0\), giving \(v-u=t\).

The two equations for the second coordinate are
\[
-2t=-at-ut+bu^2-ct^2+d,
\qquad
2t=-at+vt+bv^2-ct^2+d.
\]
Subtracting them gives \((1+b)(u+v)=4\). Since \(v-u=t\), the coordinates are exactly
\[
u=\frac2{1+b}-\frac t2,\qquad
v=\frac2{1+b}+\frac t2.
\]
Adding the two second-coordinate equations then yields
\[
0=-2at+\left(1+\frac b2-2c\right)t^2
 +\frac{8b}{(1+b)^2}+2d,
\]
which is equivalent to \(Q(t)=0\). Conversely, substitute the displayed coordinates into \(F\) on the branches \(y=t>0\) and \(y=-t<0\): in either second-coordinate equation the residual from the desired image is exactly \(-Q(t)\). Hence every positive root produces an actual primitive two-cycle, with no omitted sign or switching cases.

Since \(C>0\), if \(c>c_0\), \(Q\) increases strictly on the nonnegative half-line from \(-C\) to infinity, yielding one root. If \(c=c_0\), the unique root is \(C/a\). For \(c<c_0\), \(Q\) is a concave quadratic with negative value at zero and positive derivative \(a\) there. Its maximum is \(\Delta/[4(c_0-c)]\), giving the exact zero/one/two count by the discriminant sign. In the two-root regime, the roots are
\[
t_{\mathrm{small,large}}=
\frac{a\mp\sqrt{a^2-4(c_0-c)C}}{2(c_0-c)}.
\]
Expansion of the square root at \(c_0-c=0^+\) gives both asserted asymptotics.

For \(y\ne0\) the one-step Jacobian is
\[
J(x,y)=\begin{pmatrix}1&1\\-y+2bx&1-a\operatorname{sgn}(y)-x-2cy\end{pmatrix}.
\]
Put \(P=J(v,-t)J(u,t)\). Direct matrix multiplication using the exact orbit coordinates gives the stated trace \(\tau\) and determinant \(\delta\), and the exact identity
\[
\det(I-P)=1-\tau+\delta
 =2(1+b)t\bigl[a+2(c-c_0)t\bigr]
 =2(1+b)tQ'(t).
\]
At the double root \(Q'(t)=0\), therefore \(+1\) is a return multiplier. For \(c<c_0\) at the larger root, \(Q'(t)<0\), so \(\det(I-P)<0\). The real characteristic polynomial \(\lambda^2-\tau\lambda+\delta\) is then negative at \(\lambda=1\) and positive for sufficiently large positive \(\lambda\), forcing a real eigenvalue \(\lambda>1\). Finally, the three displayed Schur inequalities are the necessary and sufficient conditions that both zeros of this real quadratic lie strictly inside the unit disk, which is exactly linear asymptotic stability of the two-cycle.

For the rational example, \(C=31/32\), \(c-c_0=-1/8\), and
\[
Q(t)=-\frac{(2t-1)(2t-31)}{32}.
\]
The exact orbit points at \(t=1/2\) are \((13/12,1/2)\) and \((19/12,-1/2)\). Substitution in the Jacobian product gives \(\tau=-185/144\) and \(\delta=19/36\), hence the three positive Schur expressions displayed in the finding. For \(t=31/2\) the identity for \(\det(I-P)\) gives \(-1395/16\), proving instability.

## Verification

Run `python3 checks/check_period_two.py` with SymPy available. It verifies symbolically the two orbit substitution identities, the return trace and determinant, and the \(\det(I-P)\) factorization. Exact rational checks cover a zero-cycle regime, a double-root regime, and the two coexisting cycles including the stated Schur signs. The checker reports `PERIOD_TWO_EXACT_IDENTITIES_AND_RATIONAL_EXAMPLES_OK`. Universal root counts, multiplier implications, and the asymptotic branches follow from the proof above, not from finite experiments.

## Relationship to prior work

Huynh et al. introduced this exact map in 2019, proved that it has no fixed points, and numerically observed a period-two beginning to a period-doubling route as \(c\) varies (their equation (1), Section 2.1, Figure 2). That observation does **not** provide the exact all-positive-parameter census, the second coexisting branch, the finite coalescence criterion, escape of that branch through infinity, or the explicit Schur stability formulas. These are the contributions proved here. General algorithms for solving quadratic two-cycles and general Schur criteria supply methods, not the source-specific statements. García Grimaldo and coauthors' 2023 FPGA study concerns a one-dimensional piecewise-linear map without fixed points, not this two-dimensional quadratic map. Searches did not identify a published statement covering the exact present formulas, but absence of a search hit is not a proof of publication priority.

## Limitations

The result classifies only primitive two-cycles, not the basin geometry, all bounded orbits, higher-period cycles, or chaotic attractors. On an equality in the Schur criteria, linear eigenvalue information alone does not establish nonlinear attraction or repulsion. At a double-root collision the return map has a \(+1\) multiplier, but no universal nondegenerate saddle-node normal form is asserted; additional eigenvalue degeneracies are not excluded. The diverging branch is a family of periodic points under parameter variation, not a proof that any individual forward trajectory diverges in time. Historical priority remains subject to independent literature audit.

## References

1. V. V. Huynh, A. Ouannas, X. Wang, V.-T. Pham, X. Q. Nguyen, and F. E. Alsaadi, *Chaotic Map with No Fixed Points: Entropy, Implementation and Control*, **Entropy** 21 (2019), 279. DOI: 10.3390/e21030279. Publicly released March 14, 2019. https://doi.org/10.3390/e21030279
2. C. A. García Grimaldo and collaborators, *FPGA Implementation of a Chaotic Map with No Fixed Point*, **Electronics** 12 (2023), 444. DOI: 10.3390/electronics12020444. https://doi.org/10.3390/electronics12020444 (different one-dimensional piecewise-linear map, compared to avoid title-level conflation).
