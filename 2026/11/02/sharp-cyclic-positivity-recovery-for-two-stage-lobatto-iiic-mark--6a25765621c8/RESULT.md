# Sharp cyclic-positivity recovery for two-stage Lobatto IIIC Markov steps

## Finding

For every integer \(n\ge2\), let \(P_n\) denote the directed forward cyclic-shift permutation matrix, with \((P_n)_{i,i+1\pmod n}=1\), and set \(Q_n=P_n-I_n\). The unmodified two-stage Lobatto IIIC endpoint update is
\[
M_n(h)=R(hQ_n),\qquad R(z)=\frac{1}{1-z+z^2/2},\qquad h\ge0.
\]
The following is an **exact, necessary-and-sufficient, all-dimension entrywise-positivity classification**:
\[
M_n(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad
\begin{cases}
h\ge0,&2\le n\le4,\\[2pt]
h=0\ \text{or}\ h\ge\cot(\pi/n)-1,&n\ge5.
\end{cases}
\]
For every \(h>0\), the matrix has row and column sums one. It is strictly positive for every \(h>0\) when \(n\le4\). For \(n\ge5\), at the positive threshold \(h_n=\cot(\pi/n)-1\), precisely the cyclic-displacement coefficient associated with \(P_n^{n-1}\) is zero; all other cyclic-displacement coefficients are positive. For \(h>h_n\), every entry is strictly positive; for \(0<h<h_n\), at least one entry is strictly negative. Moreover,
\[
h_n=\frac{n}{\pi}-1-\frac{\pi}{3n}+O(n^{-3})\qquad(n\to\infty).
\]

## Assumptions and scope

The state space consists of \(n\) vertices on a directed cycle; from each vertex there is a unit-rate continuous-time transition to the next vertex modulo \(n\). The end-step matrix is the *unmodified* rational stability map, not a projection, clipping, SSP decomposition, or internally constrained stage update. Rates, topology and step size are exactly as stated. In particular, a cycle is **not** an absorbing pure-birth chain. We use row-generator convention, but the transpose convention has identical entrywise signs. The statement concerns endpoint entrywise nonnegativity and mass conservation, not time-discretization accuracy at large steps or nonnegativity of internal Runge--Kutta stages.

The two-stage Lobatto IIIC coefficients are
\[
A=\begin{pmatrix}\tfrac12&-\tfrac12\\\tfrac12&\tfrac12\end{pmatrix},
\qquad b=\begin{pmatrix}\tfrac12\\\tfrac12\end{pmatrix},
\]
which give \(R(z)=1+zb^\mathsf T(I-zA)^{-1}\mathbf1=(1-z+z^2/2)^{-1}\).

## Proof

**1. Exact cyclic inverse kernel.** Fix \(h>0\) and define
\[
\theta=\arctan\frac{1}{h+1}\in(0,\pi/4),\qquad
\rho=\cos\theta-\sin\theta=\frac{h}{\sqrt{h^2+2h+2}}\in(0,1),
\qquad \alpha=\rho e^{i\theta}=\frac{h}{h+1-i}.
\]
Write \(A_h=1+h+h^2/2\). For an indeterminate \(x\),
\[
1-h(x-1)+\tfrac{h^2}{2}(x-1)^2
=A_h(1-\alpha x)(1-\bar\alpha x).
\]
The factor is invertible for \(x=P_n\), because \(\lvert\alpha\rvert=\rho<1\). Since \(P_n^n=I_n\), geometric-series reduction modulo \(x^n-1\) gives
\[
M_n(h)=\sum_{j=0}^{n-1}c_{n,j}(h)P_n^j,
\]
with the **exact real coefficient formula**
\[
\boxed{\displaystyle
c_{n,j}(h)=\frac{2\rho^{j+1}}{h\left(1-2\rho^n\cos(n\theta)+\rho^{2n}\right)}
\left[\sin((j+1)\theta)+\rho^n\sin((n-j-1)\theta)\right]},
\quad0\le j<n.\tag{1}
\]
Indeed, the coefficient of \(x^m\) in
\(1/[A_h(1-\alpha x)(1-\bar\alpha x)]\) is
\((\alpha^{m+1}-\bar\alpha^{m+1})/[A_h(\alpha-\bar\alpha)]\); aliasing all indices congruent to \(j\) modulo \(n\) yields
\[
c_{n,j}=\frac{1}{A_h(\alpha-\bar\alpha)}
\left(\frac{\alpha^{j+1}}{1-\alpha^n}-\frac{\bar\alpha^{j+1}}{1-\bar\alpha^n}\right).
\]
Taking imaginary parts and using \(A_h\operatorname{Im}\alpha=h/2\) produces (1). Its denominator is \(\lvert1-\alpha^n\rvert^2>0\). For \(n=2\), the reduction correctly combines powers modulo two. Since \(Q_n\mathbf1=0\) and \(R(0)=1\), every row sums to one; circulancy gives column sums one.

**2. Sufficiency and boundary.** If \(n\theta\le\pi\), then both angles in the bracket in (1) belong to \([0,\pi]\), so all coefficients are nonnegative. When \(n\theta<\pi\), the first sine is strictly positive for every \(j\), giving strict positivity. At \(n\theta=\pi\), exactly \(j=n-1\) makes both sine terms zero; the other \(n-1\) coefficients are strictly positive. Because \(\theta<\pi/4\), all positive timesteps satisfy \(n\theta<\pi\) when \(n\le4\).

**3. Necessity.** Suppose \(n\ge5\) and \(n\theta>\pi\). If \(\pi<n\theta<2\pi\), the coefficient with \(j=n-1\) has the sign of \(\sin(n\theta)<0\). If \(n\theta\ge2\pi\), put \(k=\lceil3\pi/(2\theta)\rceil\). Then \(1\le k\le n\) and \(3\pi/2\le k\theta<3\pi/2+\theta<7\pi/4\), so
\[
\sin(k\theta)\le-\cos\theta\le-1/\sqrt2.
\]
Furthermore, \(\log\rho\le-\theta\) because the derivative of \(\log(\cos\theta-\sin\theta)\) is
\(-\frac{\sin\theta+\cos\theta}{\cos\theta-\sin\theta}\le-1\), and its value at zero is zero. Thus \(\rho^n\le e^{-n\theta}\le e^{-2\pi}<1/\sqrt2\). Hence the bracket in (1) at \(j=k-1\) is strictly negative, regardless of its second sine. Both cases prove that \(n\theta>\pi\) forces a negative entry.

**4. Threshold and asymptotics.** For \(n\ge5\), since \(\theta=\arctan(1/(h+1))\) is strictly decreasing in \(h\), the inequality \(n\theta\le\pi\) is equivalent to \(h\ge\cot(\pi/n)-1>0\). At \(h=0\), \(M_n(0)=I_n\), which is entrywise nonnegative. Finally the standard local expansion \(\cot x=x^{-1}-x/3+O(x^3)\) gives the stated asymptotic threshold. This proves every assertion.

## Verification

The self-contained Python standard-library program `verify.py` evaluates the exact generator polynomial and inverts it over rational numbers for \(2\le n\le17\) at twelve positive rational steps. It compares all nonzero and negative entries with independent trigonometric coefficients, verifies stochastic mass conservation, independently reconstructs the method's stability function from its Butcher tableau, tests the predicted zero/positive boundary sign pattern through \(n=200\), and probes the large-phase negative coefficient. The actual execution yielded **25,420 passed assertions**. These finite computations check the algebra and boundary behavior; they are not offered as proof for arbitrary \(n\), which is established by the argument above. Run with `python3 verify.py`; no external packages or input files are required.

## Relationship to prior work

Lóczi and Ketcheson (public preprint 2013-03-26, arXiv:1303.6651) study rational absolute-monotonicity radii for Runge--Kutta methods, including generic positivity and contractivity implications. Those general sufficient conditions do not state the exact sign pattern of this particular directed-cycle resolvent, nor its large-step recovery boundary. Bharali and Holtz (2005, arXiv:math/0511325) characterize entire functions preserving entrywise nonnegativity of arbitrary circulant nonnegative matrices. Their Fourier/circulant framework is related but treats a different matrix class and entire functions; neither the rational Lobatto IIIC map on \(P_n-I_n\) nor its sharp parameter threshold follows directly from that characterization.

Previously studied absorbing pure-birth generators differ mathematically from directed cycles: replacing the terminal absorbing state with a return edge changes the generator spectrum and adds modular aliasing to the inverse coefficients. Likewise, the two-stage Radau IIA method has a different rational stability map. Neither provides the present sharp cyclic Lobatto IIIC interval by merely relabelling an endpoint. The novelty assessment is qualified by the possibility of an older equivalent result in specialist matrix-function or numerical-positivity literature.

## Limitations

Only the unmodified two-stage Lobatto IIIC end-step for unit-rate directed cycles is covered. The method is second-order accurate locally, but large timesteps that restore nonnegative matrix entries need not be accurate approximations of the exact Markov semigroup. No claim about internal-stage positivity, nonuniform rates, general directed graphs, simultaneous contractivity in other norms, or an independently certified literature-uniqueness theorem is made. Specialist historical overlap cannot be categorically excluded; no independent mathematical audit has been performed.

## References

1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, initial public arXiv version 2013-03-26, https://arxiv.org/abs/1303.6651.
2. G. Bharali and O. Holtz, *Functions preserving nonnegativity of matrices*, initial public arXiv version 2005-11-13, https://arxiv.org/abs/math/0511325, especially its circulant-matrix discussion.
3. A. Baum, *Positivity preserving discretizations of differential-algebraic equations*, lecture slides (2011), https://www3.math.tu-berlin.de/multiphysics/Publications/Talks/110923_ILAS_Braunschweig_Baum.pdf, discussion of implicit Runge--Kutta positivity, including Lobatto IIIC.
