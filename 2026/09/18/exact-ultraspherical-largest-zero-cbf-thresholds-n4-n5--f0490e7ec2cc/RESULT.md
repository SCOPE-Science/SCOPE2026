# Exact complete-Bernstein thresholds for the largest ultraspherical zero in degrees four and five

## Statement

Let \(z_{n,1}(\lambda)\) be the largest positive zero of the Gegenbauer polynomial
\(C_n^\lambda\), initially for \(\lambda>-1/2\), with the usual reduced interpretation
at \(\lambda=0\). For \(d\ge 1/2\), set
\[
G_{n,d}(\lambda)=\sqrt{\lambda+d}\,z_{n,1}(\lambda),\qquad
F_{n,d}(s)=G_{n,d}(s-\tfrac12),\quad s>0 .
\]

For the two first degrees not exactly classified in Appendix A.3 of
Castillo, arXiv:2609.19186v1, the complete-Bernstein range is exact:
\[
\boxed{
F_{4,d}\in\mathrm{CBF}\iff \frac12\le d\le 3,
\qquad
F_{5,d}\in\mathrm{CBF}\iff \frac12\le d\le 4 .
}
\]
Consequently, combining these two cases with the degree-\(2\) and degree-\(3\)
classifications already given in that paper,
\[
F_{n,d}\in\mathrm{CBF}\iff \frac12\le d\le n-1
\qquad (2\le n\le5).
\]

For \(n=4,5\), the endpoint functions at \(d=3,4\) respectively are nonconstant;
hence all Bernstein sign inequalities are strict:
\[
(-1)^{r-1}F_{n,d}^{(r)}(s)>0
\quad (r\ge1,\ s>0,\ n=4,5,\ \tfrac12\le d\le n-1).
\]

The new point is that the sufficient upper endpoint
\(d\le \lceil n/2\rceil\) in Proposition A.4 of arXiv:2609.19186v1 is not optimal
already for \(n=4,5\): it can be increased from \(2\) to \(3\) in degree \(4\),
and from \(3\) to \(4\) in degree \(5\).

## Explicit largest-zero branches

Write \(Y_n(\lambda)=z_{n,1}(\lambda)^2\). Removing the parameter factors that do
not affect the nonzero zeros gives
\[
C_4^\lambda(x)\propto
4(\lambda+2)(\lambda+3)x^4-12(\lambda+2)x^2+3,
\]
and
\[
C_5^\lambda(x)\propto
x\bigl(4(\lambda+3)(\lambda+4)x^4
      -20(\lambda+3)x^2+15\bigr).
\]
Therefore the largest branches are
\[
Y_4(\lambda)=
\frac{3(\lambda+2)+\sqrt{3(\lambda+2)(2\lambda+3)}}
     {2(\lambda+2)(\lambda+3)},
\tag{1}
\]
\[
Y_5(\lambda)=
\frac{5(\lambda+3)+\sqrt{5(\lambda+3)(2\lambda+3)}}
     {2(\lambda+3)(\lambda+4)}.
\tag{2}
\]
In each formula the square root is normalized to be positive for
\(\lambda>-1/2\), and \(z_{n,1}=\sqrt{Y_n}\) is normalized positive there.

For a square root of \((\lambda-a)(\lambda-b)\) normalized positive to the right
of both real branch points, the upper boundary value is positive to their right,
positive imaginary between them, and negative real to their left. Hence the
radical in (1) is negative real for \(a<-2\), and the radical in (2) is negative
real for \(a<-3\).

It follows directly from (1) that on
\[
-3<a<-2
\]
both numerator and denominator of \(Y_4(a+i0)\) are negative, so
\(Y_4(a+i0)>0\) and the continued largest branch satisfies
\[
z_{4,1}(a+i0)>0.
\tag{3}
\]
Similarly, (2) gives
\[
z_{5,1}(a+i0)>0,\qquad -4<a<-3.
\tag{4}
\]
Thus the positive-boundary behavior survives one degree-loss point farther than
the general argument in Appendix A.3 detects.

## The next pole is the sharp obstruction

At the next real singularity, (1) and (2) give
\[
Y_4(\lambda)=\frac{3}{\lambda+3}+O(1),
\qquad \lambda\to-3,
\tag{5}
\]
and
\[
Y_5(\lambda)=\frac{5}{\lambda+4}+O(1),
\qquad \lambda\to-4.
\tag{6}
\]
On the right of these points the continued \(z_{n,1}\) is positive. Continuing
through the upper half-plane therefore fixes the half-power branches as
\[
z_{4,1}(\lambda)\sim \sqrt3\,(\lambda+3)^{-1/2},
\qquad
z_{5,1}(\lambda)\sim \sqrt5\,(\lambda+4)^{-1/2}.
\tag{7}
\]
Consequently, just to the left of the pole,
\[
\operatorname{Im} z_{4,1}(a+i0)<0\quad(a<-3,\ a\approx-3),
\]
and
\[
\operatorname{Im} z_{5,1}(a+i0)<0\quad(a<-4,\ a\approx-4).
\tag{8}
\]

If \(d>3\), choose \(a\in(-d,-3)\) sufficiently close to \(-3\). Then
\(\sqrt{a+d}>0\), so (8) gives
\[
\operatorname{Im}G_{4,d}(a+i0)<0.
\]
A complete Bernstein function has a unique slit-plane continuation that maps the
upper half-plane into itself. Hence \(F_{4,d}\) cannot be complete Bernstein.
The same argument with \(a\in(-d,-4)\) proves that \(F_{5,d}\) is not complete
Bernstein for \(d>4\).

## Sufficiency up to the sharp endpoints

We use the Pick characterization of complete Bernstein functions: a nonnegative
function on \((0,\infty)\) is complete Bernstein if its holomorphic continuation
to the slit plane maps the upper half-plane into itself.

The continuation theory in arXiv:2609.19186v1 gives, for the positive zero
branch,
\[
\operatorname{Re}z_{n,1}(\lambda)>0
\quad(\operatorname{Im}\lambda>0),
\tag{9}
\]
and its boundary argument proves
\[
\operatorname{Im}z_{4,1}(a+i0)\ge0\quad(a>-2),
\qquad
\operatorname{Im}z_{5,1}(a+i0)\ge0\quad(a>-3),
\tag{10}
\]
away from the finite singular set. Equations (3)--(4) extend (10) to
\(a>-3\) for \(n=4\) and to \(a>-4\) for \(n=5\).

Now fix \(n=4\), \(1/2\le d\le3\). On the real boundary:

* if \(a>-d\), then \(\sqrt{a+d}\) is positive real, while the preceding paragraph
  gives \(\operatorname{Im}z_{4,1}(a+i0)\ge0\);
* if \(a<-d\), then \(\sqrt{a+d+i0}=i\sqrt{|a+d|}\), so by (9),
  \[
  \operatorname{Im}G_{4,d}(a+i0)
  =\sqrt{|a+d|}\,\operatorname{Re}z_{4,1}(a+i0)\ge0 .
  \]

The same argument works for \(n=5\), \(1/2\le d\le4\).

To pass from nonnegative boundary values to the upper-half-plane Pick property,
one may use the boundary minimum principle employed in arXiv:2609.19186v1.
The algebraic singularities have exponent strictly smaller than one. At infinity,
the paper's Hermite-zero expansion is
\[
G_{n,d}(\lambda)
=
h_n+
\frac{h_n\{4d-(2h_n^2+2n-1)\}}{8(\lambda+d)}
+O(\lambda^{-2}),
\tag{11}
\]
where \(h_n\) is the largest positive zero of the physicists' Hermite polynomial.
For the two degrees,
\[
h_4^2=\frac{3+\sqrt6}{2},
\qquad
h_5^2=\frac{5+\sqrt{10}}2 .
\]
At the proposed sharp endpoints the numerator in (11) is respectively
\[
12-(10+\sqrt6)=2-\sqrt6<0,
\qquad
16-(14+\sqrt{10})=2-\sqrt{10}<0.
\]
It is therefore strictly negative throughout \(d\le3\) for \(n=4\) and throughout
\(d\le4\) for \(n=5\). The boundary minimum principle yields
\[
\operatorname{Im}G_{n,d}(\lambda)>0
\quad(\operatorname{Im}\lambda>0)
\]
in these ranges. Translating \(\lambda=s-\tfrac12\) gives the required Pick
property of \(F_{n,d}\), hence the complete-Bernstein conclusion.

At \(d=3\) and \(d=4\), respectively, the factor \(\sqrt{\lambda+d}\) cancels
the half-order blow-up in (7); this is why the endpoint itself remains admissible.

## Interpretation

In degrees four and five the first degree-loss point is not the obstruction to
complete-Bernstein scaling. The continued largest-zero sheet stays on the
nonnegative boundary side after that point. The obstruction occurs at the next
simple pole, where the square-root continuation rotates to the negative imaginary
axis. This explains exactly why the sufficient range from the general
degree-loss argument can be enlarged in these two degrees.

The calculation also shows a low-degree pattern:
\[
d_{\max}(n)=n-1,\qquad 2\le n\le5.
\]
No claim is made that this formula persists for \(n\ge6\).

## Limitations

1. The exact classification proved here is only for \(n=4,5\); the all-degree
   optimal largest-zero threshold remains open.
2. Failure for \(d>3\) or \(d>4\) is failure of the complete-Bernstein/Pick
   property. It does not by itself prove failure of the weaker ordinary
   Bernstein property.
3. The detailed comparison was made with arXiv:2609.19186v1. A current metadata
   index reports an update dated 2026-09-18, while the updated full text was not
   available for inspection here. The current abstract remains unchanged and
   does not state the degree-\(4,5\) exact thresholds. If the updated version
   contains these thresholds, the originality assessment must be revised.
4. Standard facts about complete Bernstein functions, Gegenbauer polynomials,
   and square-root boundary continuation are not claimed as new.

## References

1. K. Castillo, *Complete Bernstein functions and scaled ultraspherical zeros*,
   arXiv:2609.19186v1 (2026), especially the complex continuation, boundary
   minimum principle, Hermite asymptotics, and Appendix A.3.
   https://arxiv.org/abs/2609.19186v1
2. R. L. Schilling, R. Song, Z. Vondraček, *Bernstein Functions: Theory and
   Applications*, 2nd ed., De Gruyter, 2012, Chapter 6.
   https://doi.org/10.1515/9783110269338
