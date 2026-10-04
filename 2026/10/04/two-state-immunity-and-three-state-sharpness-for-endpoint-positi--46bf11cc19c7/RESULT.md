# Two-state immunity and three-state sharpness for endpoint positivity of SSP-SDIRK2(2)
## Finding
Consider the two-stage, second-order SSP-optimal singly diagonally implicit Runge--Kutta method with
\[
a_{11}=a_{22}=\frac14,\qquad a_{21}=\frac12,\qquad b_1=b_2=\frac12.
\]
It is exactly two consecutive applications of the implicit midpoint rule with substep length \(h/2\). For a continuous-time Markov chain written in row-vector form
\[
p'(t)=p(t)Q,
\]
where \(Q\) has nonnegative off-diagonal entries and zero row sums, its endpoint update is
\[
p_{n+1}=p_nR_h(Q),\qquad
R_h(Q)=\left[(I+hQ/4)(I-hQ/4)^{-1}\right]^2.
\]

The endpoint-positivity behavior has a sharp state-dimension boundary.

For every two-state Markov generator and every \(h\ge0\), \(R_h(Q)\) is entrywise nonnegative and row-stochastic. By contrast, for the three-state pure-birth generator
\[
Q=\begin{pmatrix}-1&1&0\\0&-1&1\\0&0&0\end{pmatrix},
\]
endpoint positivity holds exactly for \(0\le h\le4\) and fails for every \(h>4\). Therefore three states are the smallest dimension in which endpoint positivity can fail for this method. The classical SSP coefficient \(4\) is already sharp within three-state Markov generators, even though the two-state class is endpoint-positive for arbitrarily large steps.

## Assumptions and scope
A Markov generator means a real square matrix \(Q\) with \(q_{ij}\ge0\) for \(i\ne j\) and \(Q\mathbf 1=0\). Endpoint positivity means that the one-step transition matrix \(R_h(Q)\) is entrywise nonnegative. Since \(Q\mathbf 1=0\), every rational function here preserves row sums whenever it is defined. For \(h\ge0\), \(I-hQ/4\) is invertible because every eigenvalue of a finite-state Markov generator has nonpositive real part.

The result concerns the endpoint only. It does not claim unconditional nonnegativity of the intermediate midpoint stage. Indeed, intermediate-stage positivity can fail even in two states for sufficiently unbalanced rates and sufficiently large \(h\).

## Proof
For a two-state generator write
\[
Q=\begin{pmatrix}-a&a\\b&-b\end{pmatrix},\qquad a,b\ge0.
\]
If \(a=b=0\), the update is the identity. Otherwise set \(s=a+b\) and
\[
\Pi=\frac1s\begin{pmatrix}b&a\\b&a\end{pmatrix}.
\]
Then \(\Pi^2=\Pi\), \(Q=-s(I-\Pi)\), and the midpoint half-step matrix is
\[
M_h(Q)=(I+hQ/4)(I-hQ/4)^{-1}
      =\Pi+r(I-\Pi),
\]
where
\[
r=\frac{1-hs/4}{1+hs/4}.
\]
Because \(-1<r\le1\) for finite \(h\ge0\), one has \(0\le r^2\le1\). Squaring and using \(\Pi(I-\Pi)=0\) gives
\[
R_h(Q)=M_h(Q)^2=\Pi+r^2(I-\Pi).
\]
Hence
\[
R_h(Q)=\frac1s
\begin{pmatrix}
b+r^2a & a(1-r^2)\\
b(1-r^2) & a+r^2b
\end{pmatrix}.
\]
All four entries are nonnegative and each row sums to one. This proves unconditional endpoint positivity for every two-state chain. The cancellation is genuinely an endpoint phenomenon: for example, when \(b=0\) and \(h>4/a\), the first midpoint matrix has top-left entry \(r<0\), whereas the full two-substep endpoint has top-left entry \(r^2\ge0\).

Now take the three-state pure-birth generator
\[
Q=\begin{pmatrix}-1&1&0\\0&-1&1\\0&0&0\end{pmatrix}.
\]
Direct triangular inversion gives
\[
R_h(Q)=
\begin{pmatrix}
\dfrac{(h-4)^2}{(h+4)^2} &
\dfrac{16h(4-h)}{(h+4)^3} &
\dfrac{32h^2}{(h+4)^3}\\[2ex]
0&\dfrac{(h-4)^2}{(h+4)^2}&\dfrac{16h}{(h+4)^2}\\[2ex]
0&0&1
\end{pmatrix}.
\]
Every displayed denominator is positive for \(h\ge0\), all entries except the \((1,2)\) entry are nonnegative for all such \(h\), and
\[
(R_h(Q))_{12}=\frac{16h(4-h)}{(h+4)^3}.
\]
Thus this endpoint matrix is nonnegative exactly for \(0\le h\le4\), and it has a negative entry for every \(h>4\). Its row sums are one. Since one state is trivial and all two-state chains are unconditionally endpoint-positive, dimension three is minimal for endpoint-positivity failure.

For this witness, forward Euler is positivity-preserving exactly for \(0\le h\le1\). Therefore the failure boundary \(h=4\) realizes the method's known SSP coefficient \(4\) within the Markov-generator class.

## Verification
The accompanying `verify.py` uses exact rational arithmetic and a dependency-free Gauss--Jordan inverse. It reconstructs the numerical one-step matrix from the midpoint formula for representative rational two-state generators, verifies equality with the projector formula, checks nonnegativity and unit row sums for large steps, and independently reconstructs the three-state pure-birth formula at rational step sizes on both sides of \(h=4\). It also checks that the three-state \((1,2)\) entry is zero at \(h=4\), positive below it, and negative above it.

These finite exact checks verify the algebraic implementation. The claims for all rates and all step sizes follow from the analytic formulas in the proof, not from enumeration.

## Relationship to prior work
Ferracina and Spijker proved that the two-stage second-order SDIRK method above is SSP-optimal and has characteristic coefficient \(4\). Their theory is deliberately worst-case: it guarantees strong stability, including intermediate stages, for arbitrary convex functionals and arbitrary problems satisfying the forward-Euler hypothesis. It does not imply that a restricted problem class must lose endpoint positivity immediately beyond that coefficient, nor does it classify the smallest Markov-chain dimension realizing failure.

Bonaventura and Della Rocca explicitly identify this same SDIRK method as two consecutive implicit-midpoint applications and again record absolute-monotonicity radius \(4\). Their full discussion treats positivity through the general absolute-monotonicity framework and numerical PDE/kinetics tests, not the exact finite-state Markov endpoint classification proved here.

Earlier positivity work of Horváth develops sharp step-size thresholds for broad classes of positive initial-value problems. The accessible primary metadata and abstracts establish that broader setting, but the full text of the most directly relevant 1998 and 2005 articles was not available through the lawful routes inspected here. An equivalent two-state/three-state Markov specialization in that literature therefore remains a residual originality risk.

A separate recent result gives an eight-state minimal obstruction for endpoint positivity of the fourth-order \([2/2]\) Padé/two-stage Gauss--Legendre map. That concerns a different rational approximation and does not imply the present dimension-three theorem for the square of the implicit-midpoint map.

## Limitations
The theorem is specific to finite-state autonomous Markov generators and to endpoint nonnegativity. It does not give unconditional SSP, total-variation, or intermediate-stage positivity. It also does not address time-dependent generators, splitting errors, floating-point roundoff, or higher-dimensional classifications beyond the explicit three-state sharp witness.

The strongest literature risk is that the exact two-state immunity or the three-state pure-birth sharpness may already be embedded in older matrix-positivity analyses whose full text was not recovered in the bounded search. The claim therefore concerns the explicit theorem and proof given here, not a priority assertion over inaccessible literature.

## References
1. L. Ferracina and M. N. Spijker, *Strong Stability of Singly-Diagonally-Implicit Runge-Kutta Methods*, Leiden Mathematical Institute Report 2007-11, public report index dated June 1, 2007; Applied Numerical Mathematics 58 (2008), 1675--1686, DOI 10.1016/j.apnum.2007.10.004.
2. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303v1, October 14, 2015; MOX Report 56/2015.
3. Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309--326, DOI 10.1016/S0168-9274(98)00050-6.
4. Z. Horváth, *On the positivity step size threshold of Runge-Kutta methods*, Applied Numerical Mathematics 53 (2005), 341--356, DOI 10.1016/j.apnum.2004.08.026.
