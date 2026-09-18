# A one-minimum curvature screen for hexahedral face quartics

## Result

Consider the face polynomial used in the boundary-minimum reduction for a trilinear hexahedron,
\[
f(s,t)=a(t)s^2+b(t)s+c(t),\qquad (s,t)\in[0,1]^2,
\]
with
\[
a(t)=a_0+a_1t,\qquad
b(t)=b_0+b_1t+b_2t^2,\qquad
c(t)=c_0+c_1t+c_2t^2.
\]
On the interval where \(a(t)>0\), define the parabola vertex and its reduced value by
\[
s_*(t)=-\frac{b(t)}{2a(t)},\qquad
h(t)=f(s_*(t),t)=c(t)-\frac{b(t)^2}{4a(t)}.
\]
The quartic stationarity polynomial of Zhang is
\[
P(t)=4a(t)^2c'(t)-2a(t)b(t)b'(t)+a'(t)b(t)^2.
\]
Then:

1. \(h'(t)=P(t)/(4a(t)^2)\).
2. On every interval where \(a>0\),
   \[
   \boxed{h^{(4)}(t)\le 0.}
   \]
3. If \(P\not\equiv0\), then \(P\) has at most **three** distinct roots on the interval \(a>0\), not four.
4. Among the feasible stationary roots
   \[
   P(t)=0,\qquad a(t)>0,\qquad 0<s_*(t)<1,
   \]
   at most **one** can be an interior local minimum of \(f\).
5. At any simple feasible stationary root \(t_0\),
   \[
   \boxed{
   \det \nabla^2 f(s_*(t_0),t_0)
   =\frac{P'(t_0)}{2a(t_0)}.
   }
   \]
   Hence \(P'(t_0)>0\) is exactly the strict-local-minimum condition, while \(P'(t_0)<0\) makes the stationary point a saddle.  For a multiple root, the exact criterion is that \(P\) changes sign from negative to positive across the root.

Consequently, when \(P\not\equiv0\), a face minimum strictly below its perimeter minimum can occur at **at most one** interior stationary candidate.  When \(P\equiv0\), Zhang's Lemma 3 already shows that the perimeter candidates suffice.  Thus an exact boundary-minimum implementation may replace the source paper's set of up to four retained interior points per face by at most one minimum-capable point, without changing the quartic root solve itself.

## Proof

The first identity is immediate from the chain rule.  Along the vertex curve, \(f_s(s_*(t),t)=0\), so
\[
h'(t)=f_t(s_*(t),t)=\frac{P(t)}{4a(t)^2}.
\]

The fourth-derivative sign is the structural point.  If \(a_1=0\), then \(a(t)=a_0>0\) and
\[
h(t)=c(t)-\frac{b(t)^2}{4a_0},
\]
so
\[
\boxed{h^{(4)}(t)=-\frac{6b_2^2}{a_0}\le0.}
\]

Now suppose \(a_1\ne0\).  Divide the quadratic \(b\) by the affine polynomial \(a\):
\[
b(t)=a(t)\ell(t)+r,
\]
where \(\ell\) is affine and \(r\) is constant.  Then
\[
h(t)=c(t)-\frac{a(t)\ell(t)^2}{4}-\frac{r\ell(t)}2-rac{r^2}{4a(t)}.
\]
All terms except the last have degree at most three.  Therefore
\[
\boxed{
 h^{(4)}(t)=-\frac{6r^2a_1^4}{a(t)^5}\le0
}
\qquad(a(t)>0).
\]
In particular, \(h''\) is concave.

If the displayed fourth derivative is strictly negative, four distinct zeros of \(h'\) would, by repeated Rolle's theorem, force a zero of \(h^{(4)}\), a contradiction.  If it vanishes identically, then \(h\) is a polynomial of degree at most three in the \(a_1\ne0\) case, or of degree at most two when \(a_1=0\) and \(b_2=0\).  Hence \(h'\) still has at most three distinct zeros unless \(h'\equiv0\), which is exactly the already-separated \(P\equiv0\) case.  Since \(h'\) and \(P\) have the same zeros where \(a>0\), the three-root bound follows.

To prove uniqueness of a minimum-capable root, suppose instead that the nonconstant analytic function \(h\) had two distinct interior local minima.  Each isolated minimum makes \(h'\) change sign from negative to positive.  Between the two upward crossings, \(h'\) must also pass from positive to negative.  The mean-value theorem would then produce three ordered points at which
\[
h''>0,\qquad h''<0,\qquad h''>0.
\]
That is impossible because \(h''\) is concave: a concave function that is positive at two endpoints of a subinterval cannot be negative at an interior point.  Thus there is at most one negative-to-positive zero of \(P\) where \(a>0\).

Finally, at a stationary point on the vertex curve, the Schur complement identity gives
\[
h''=f_{tt}-\frac{f_{st}^2}{f_{ss}},\qquad f_{ss}=2a>0.
\]
Hence
\[
\det\nabla^2f=2a\,h''.
\]
Differentiating \(h'=P/(4a^2)\) and using \(P(t_0)=0\) gives
\[
h''(t_0)=\frac{P'(t_0)}{4a(t_0)^2},
\]
and therefore
\[
\det\nabla^2 f(s_*(t_0),t_0)=\frac{P'(t_0)}{2a(t_0)}.
\]
Because \(f_{ss}=2a>0\), a positive determinant is equivalent to positive definiteness of the Hessian, while a negative determinant gives a saddle.

A global face minimizer strictly below the face perimeter cannot occur at \(a=0\): the source paper proves that such a value is then also attained on the perimeter.  Therefore any strictly better interior minimum lies on the vertex curve with \(a>0\), and the preceding argument leaves at most one candidate.

## Sharpness within the face-polynomial class

The three-stationary-root bound cannot be reduced using only the coefficient structure above.  Take
\[
a(t)=1,
\qquad
b(t)=t^2-t-\frac1{10},
\qquad
c(t)=\frac{13}{100}t(1-t).
\]
Then
\[
P(t)=-4\left(t-\frac15\right)
        \left(t-\frac12\right)
        \left(t-\frac45\right),
\]
and all three stationary vertices are strictly inside the square:
\[
s_*\!\left(\frac15\right)=\frac{13}{100},\quad
s_*\!\left(\frac12\right)=\frac7{40},\quad
s_*\!\left(\frac45\right)=\frac{13}{100}.
\]
Moreover,
\[
P'\!\left(\frac15\right)=-\frac{18}{25},\qquad
P'\!\left(\frac12\right)=\frac9{25},\qquad
P'\!\left(\frac45\right)=-\frac{18}{25}.
\]
Thus the two outer stationary points are saddles and the middle point is the unique strict local minimum.  This example establishes sharpness for the algebraic face class; it is not asserted here that this particular coefficient tuple is realized by a physical trilinear hexahedron.

## Algorithmic consequence

Zhang's face procedure computes all distinct real roots of \(P\), applies the feasibility tests \(a(t)>0\) and \(0<s_*(t)<1\), and may retain up to four interior candidates; the implementation reported in the paper deliberately retains feasible stationary points of negative curvature.  The theorem above permits the following exact screen after root isolation:

- discard every feasible simple root with \(P'(t)<0\);
- retain a feasible simple root with \(P'(t)>0\);
- for a multiple root, retain it only if \(P\) changes sign from negative to positive;
- if \(P\equiv0\), retain no interior point, as in the source paper.

At most one root survives.  Therefore the worst-case number of interior jacdet evaluations after the root solve drops from four per face to one per face, and from twenty-four to six over the six faces.  The quartic root-solving cost itself is unchanged.  For strict validity, discarding saddles remains sound because any negative value anywhere on a compact face implies a negative global face minimum, which must be on the perimeter or at the unique minimum-capable interior root.

## Relation to prior work

Zhang's 2026 boundary theorem reduces exact hexahedral boundary minimization to edge quadratics and one polynomial \(P\) of degree at most four per face.  It explicitly states that up to four feasible interior stationary points may be retained and that some can be saddles; its reported implementations retain points of negative curvature and do not use concavity screening.  The identities above sharpen that candidate structure by exploiting the special rational vertex-value function \(h=c-b^2/(4a)\), rather than treating \(P\) as an arbitrary quartic.

Earlier hexahedron-validation work by Johnen, Weill and Remacle uses Bernstein bounds/subdivision rather than this exact face-quartic reduction.  The 2022 hex-meshing survey likewise describes Bernstein determinant bounds as the standard certified approach.  To the best of our knowledge, the one-minimum theorem, the global three-root bound on the positive-\(a\) interval, and the formula \(\det\nabla^2f=P'/(2a)\) at a stationary vertex have not previously been stated for this hexahedral face reduction.

## Limitations

The result sharpens only the **candidate filtering and evaluation** stage.  It does not lower the algebraic degree of Zhang's quartic equation, provide a faster certified quartic root isolator, or by itself establish a finite-precision speedup.  The three-root sharpness example is for the abstract coefficient class of the face formula and is not claimed to be geometrically realizable by a trilinear hexahedron.  The result concerns trilinear-hexahedron jacdet face restrictions; it does not extend automatically to higher-order elements.  Originality is asserted only to the best of our knowledge.

## Reproducibility

`artifacts/verify_face_screen.py` symbolically checks the derivative identity, the stationary Hessian-determinant identity, both fourth-derivative formulas, and the rational three-root example.  `artifacts/verification_output.txt` records its exact output.

## References

1. Paul Zhang, *Validating Hexahedra through their Boundaries*, arXiv:2609.19926, 2026.
2. Amaury Johnen, Jean-Christophe Weill, Jean-François Remacle, *Robust and efficient validation of the linear hexahedral element*, arXiv:1706.01613; Procedia Engineering 203 (2017), 271–281.
3. Nico Pietroni et al., *Hex-Mesh Generation and Processing: A Survey*, ACM Transactions on Graphics 42(2), Article 16, 2023, DOI: 10.1145/3554920.
