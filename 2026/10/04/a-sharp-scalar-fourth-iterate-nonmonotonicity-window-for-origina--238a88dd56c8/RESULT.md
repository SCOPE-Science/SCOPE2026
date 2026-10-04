# A sharp scalar fourth-iterate nonmonotonicity window for original FISTA

## Finding
Consider the original constant-majorization FISTA recurrence on the smooth quadratic
\[
F(u,v)=\frac{L}{2}\left(q u^2+v^2\right),\qquad L>0,\quad 0<q<1,
\]
with no nonsmooth term and initialization
\[
x_0=(u_0,0),\qquad u_0\ne0.
\]
The exact global Lipschitz constant of the gradient is \(L\), and the coordinate axis \(v=0\) is invariant. Therefore the first coordinate is a genuine scalar eigendirection of a quadratic on which FISTA uses its exact global majorization constant, not an artificially enlarged scalar stepsize.

Let
\[
t_1=1,\qquad
t_{k+1}=\frac{1+\sqrt{1+4t_k^2}}{2},\qquad
\beta_k=\frac{t_k-1}{t_{k+1}},
\]
and put
\[
r=1-q.
\]
Define
\[
c=(1+\beta_2)(1+\beta_3),\qquad
d=(1+\beta_3)\beta_2+\beta_3,
\]
\[
r_-=\frac{\beta_2}{c},
\]
and
\[
r_+=\frac{d-(1+\beta_2)+
\sqrt{(1+\beta_2-d)^2+4c\beta_2}}{2c}.
\]
Numerically,
\[
r_-=0.1532860840991754\ldots,\qquad
r_+=0.2890103091146904\ldots.
\]

Then \(F(x_1)<F(x_0)\), \(F(x_2)<F(x_1)\), and \(F(x_3)<F(x_2)\) for every \(0<q<1\), while
\[
F(x_4)>F(x_3)
\]
holds if and only if
\[
r_-<r<r_+,
\]
or equivalently
\[
0.7109896908853096\ldots<q<
0.8467139159008246\ldots.
\]
Hence \(x_4\) is the earliest possible objective-increasing point for this scalar FISTA eigendirection, and the displayed interval is the exact sharp window for that first rise.

Inside the interval is the resonance
\[
r_0=\frac{\beta_2}{1+\beta_2}
=0.2198188026030769\ldots,
\qquad
q_0=\frac{1}{1+\beta_2}
=0.7801811973969231\ldots.
\]
At \(q=q_0\), the third FISTA point is exactly the unique minimizer:
\[
x_3=(0,0).
\]
Nevertheless, if the mathematical iteration is continued without a stopping test, the next extrapolation leaves the minimizer and
\[
x_4=\left(-\beta_3 r_0^3u_0,0\right)\ne(0,0).
\]
Thus the familiar nonmonotonicity of FISTA already has a sharp, finite-horizon mechanism on a single invariant quadratic eigendirection: the method can hit the exact solution and immediately move away from it.

## Assumptions and scope
The recurrence is exactly the constant-\(L\) FISTA scheme introduced by Beck and Teboulle. Their smooth special case is obtained by taking the nonsmooth term to be zero. The parameter \(L\) here is the exact global gradient-Lipschitz constant of the two-dimensional quadratic, whose Hessian has eigenvalues \(qL\) and \(L\).

The conclusion concerns the uninterrupted mathematical recurrence. A practical implementation that checks stationarity or terminates once \(x_3=(0,0)\) is detected would stop at the resonance and would not compute \(x_4\).

The theorem classifies only the first possible objective rise along this invariant scalar eigendirection. It does not assert that later objective rises occur only in the same curvature interval.

## Proof
On the invariant axis \(v=0\), a proximal-gradient step with majorization constant \(L\) multiplies the active coordinate by
\[
1-\frac{qL}{L}=r.
\]
Write the active coordinate of \(x_k\) again as \(x_k\). The original FISTA initialization gives \(\beta_1=0\), so
\[
x_1=rx_0,\qquad x_2=r^2x_0.
\]
For the next point,
\[
x_3=r^2 A(r)x_0,
\qquad
A(r)=(1+\beta_2)r-\beta_2.
\]
For \(0<r<1\), the affine quantity \(A(r)\) runs strictly between \(-\beta_2\) and \(1\). Since \(0<\beta_2<1\),
\[
|A(r)|<1.
\]
Therefore the first three objective comparisons are all strict decreases:
\[
|x_1|<|x_0|,\qquad
|x_2|<|x_1|,\qquad
|x_3|<|x_2|.
\]

For the fourth point,
\[
x_4=r^3 B(r)x_0,
\]
where
\[
B(r)=(1+\beta_3)A(r)-\beta_3
=cr-d.
\]
Because \(F\) is a positive multiple of the square of the active coordinate,
\[
F(x_4)>F(x_3)
\]
is equivalent to
\[
|rB(r)|>|A(r)|.
\]
Squaring and factoring reduces this to
\[
\bigl(rB(r)-A(r)\bigr)
\bigl(rB(r)+A(r)\bigr)>0.
\]

The first factor is
\[
rB(r)-A(r)
=cr^2-(d+1+\beta_2)r+\beta_2.
\]
Since \(A(1)=B(1)=1\), one root is \(r=1\). The other is the product-of-roots value
\[
r_-=\frac{\beta_2}{c}.
\]
Thus this factor is negative on \(r_-<r<1\).

The second factor is
\[
rB(r)+A(r)
=cr^2+(1+\beta_2-d)r-\beta_2.
\]
Its constant term is negative and its leading coefficient is positive, so it has exactly one positive root. That root is
\[
r_+=\frac{d-(1+\beta_2)+
\sqrt{(1+\beta_2-d)^2+4c\beta_2}}{2c}.
\]
Moreover,
\[
r_-<
\frac{\beta_2}{1+\beta_2}
<r_+<1.
\]
Indeed the middle quantity is \(r_0\); the first inequality follows from \(1+\beta_3>1\), while at \(r=r_0\) one has \(A(r_0)=0\) and hence \(rB(r)+A(r)=-r_0\beta_3<0\), forcing the positive root \(r_+\) to lie to its right. Also the second factor equals \(2\) at \(r=1\), so \(r_+<1\).

Consequently the product of the two factors is positive exactly on
\[
r_-<r<r_+.
\]
This proves the sharp objective-rise window.

At the resonance
\[
r_0=\frac{\beta_2}{1+\beta_2},
\]
one has \(A(r_0)=0\), hence \(x_3=0\). But \(B(r_0)=-\beta_3\), so
\[
x_4=-\beta_3 r_0^3x_0\ne0.
\]
In the two-dimensional embedding this is precisely the displayed departure from the unique minimizer.

## Verification
The accompanying `check.py` computes \(t_2,t_3,t_4\), \(\beta_2,\beta_3\), the two sharp boundary roots, and the resonance at high decimal precision. It checks the factorization identities, verifies the root ordering, evaluates the sign pattern on every interval, and directly replays the first four FISTA points for samples on both sides of and inside the window. It also checks that the resonance gives \(x_3=0\) and \(x_4\ne0\).

The finite computation is a replay of the formulas. The all-parameter if-and-only-if statement rests on the algebraic sign proof above, not on numerical sampling.

## Relationship to prior work
Beck and Teboulle's 2009 FISTA paper gives exactly the recurrence used here and proves the global \(O(1/k^2)\) objective bound. Its full text was inspected, including the algorithm, proof, and numerical sections. It does not give a scalar first-rise classification or an exact minimizer-hit-and-leave example.

In their 2009 follow-up on constrained total-variation problems, Beck and Teboulle explicitly state that, unlike ISTA, FISTA is not guaranteed to have nonincreasing function values and introduce a monotone FISTA variant. That establishes the broad nonmonotonicity phenomenon, but not the sharp fourth-point curvature window above.

Liang, Fadili, and Peyre later analyze inertial forward-backward schemes and FISTA, explaining local oscillation through the spectrum of the local linearization. Their analysis shows that FISTA can oscillate and can be locally slower than forward-backward splitting. The inspected material does not state the exact earliest-rise interval, nor a parameter at which the original FISTA recurrence reaches the exact minimizer and immediately leaves it.

Targeted published-finding corpus searches for FISTA reaching a minimizer and leaving it, scalar fourth-iterate nonmonotonicity, and equivalent accelerated-gradient overshoot statements returned no implication-equivalent published finding. The closest indexed results concern objective spikes for other Nesterov parameterizations, heavy-ball root regimes, and unrelated one-step monotonicity frontiers.

## Limitations
The finding is a finite-horizon classification for one invariant eigendirection of a smooth quadratic. It does not characterize every later nonmonotone episode of FISTA, nonsmooth active-set effects, or behavior under backtracking.

At the resonance, any sensible exact stationarity check would terminate at \(x_3\). The point of the statement is structural: the bare FISTA recurrence itself does not make the optimizer an absorbing state when inertial history is retained.

The originality assessment is based on the full primary paper, the monotone-FISTA follow-up, a later full-text local-oscillation analysis, the current private ledger, and targeted published-finding corpus searches. A differently worded or unindexed note could contain the same low-dimensional calculation.

## References
1. A. Beck and M. Teboulle, *A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems*, SIAM Journal on Imaging Sciences 2 (2009), 183--202. DOI 10.1137/080716542. Published electronically 2009-03-04.
2. A. Beck and M. Teboulle, *Fast Gradient-Based Algorithms for Constrained Total Variation Image Denoising and Deblurring Problems*, IEEE Transactions on Image Processing 18 (2009), 2419--2434. DOI 10.1109/TIP.2009.2028250.
3. J. Liang, J. Fadili, and G. Peyre, *Activity Identification and Local Linear Convergence of Forward--Backward-type Methods*, arXiv:1503.03703.
