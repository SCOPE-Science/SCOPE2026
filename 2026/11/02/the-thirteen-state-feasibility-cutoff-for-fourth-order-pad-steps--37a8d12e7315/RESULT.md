# The thirteen-state feasibility cutoff for fourth-order Padé steps on absorbing birth chains

## Finding

Let \(n\ge2\) be an integer. Let \(Q_n\) be the row-generator of the continuous-time, unit-rate pure-birth chain \(1\to2\to\cdots\to n\), with \(n\) absorbing. Define the two-stage Gauss–Legendre/fourth-order diagonal Padé endpoint map
\[
R(z)=\frac{1+z/2+z^2/12}{1-z/2+z^2/12},\qquad M_n(h)=R(hQ_n),\quad h\ge0.
\]
Here nonnegative means **every matrix entry is nonnegative**, hence (because every row sum is one) that the endpoint is a stochastic transition matrix.

**Theorem (complete timestep classification).** Define
\[
H=2\sqrt3,\qquad h_n=\sqrt3\cot\left(\frac{\pi}{n-1}\right)-3\quad(n\ge8).
\]
Then, with closed intervals including their endpoints,
\[
\{h\ge0:M_n(h)\ge0\text{ entrywise}\}=\begin{cases}
[0,\infty),&n=2,\\
[0,H],&3\le n\le7,\\
\{0\}\cup[h_n,H],&8\le n\le13,\\
\{0\},&n\ge14.
\end{cases}
\]
In particular, a **positive** admissible timestep exists if and only if \(n\le13\). At \(n=13\), the only positive admissible timestep is \(H\). The lower thresholds at \(n=8,9,10,11,12,13\) are, respectively, approximately \(0.596640561867168\), \(1.181540550352056\), \(1.758770483143634\), \(2.330704256005837\), \(2.898823332445145\), and \(3.464101615137755\).

The lower-bound failure for \(8\le n\le13\) is a *negative absorption-column entry*, whereas the upper-bound failure for every \(n\ge3\) is a *negative nearest-neighbor transient entry*. This separates the two mechanisms responsible for the sharp window.

## Assumptions and scope

The generator is the \(n\times n\) matrix with \((Q_n)_{ii}=-1\) and \((Q_n)_{i,i+1}=1\) for \(1\le i<n\), all other entries zero, and \((Q_n)_{nn}=0\). The state-space order is fixed and the birth rate on each transient edge is one. Matrices act on row distributions; the endpoint is assessed only for finite \(n\), real \(h\ge0\), and exact arithmetic. The endpoint map is *unmodified* Gauss–Legendre, with no projection or coefficient adaptation. Other birth rates \(\lambda>0\) common to all transient states follow by replacing \(h\) by \(\lambda h\).

The rational denominator \(1-z/2+z^2/12\) vanishes only at \(3\pm i\sqrt3\), whereas the spectrum of \(hQ_n\) is contained in \(\{-h,0\}\). Thus \(M_n(h)\) is defined for every \(h\ge0\). Since \(Q_n\mathbf 1=0\) and \(R(0)=1\), \(M_n(h)\mathbf1=\mathbf1\).

## Proof

**Step 1: transient and absorbing coefficients.** For positive \(h\), let \(x\) be a formal variable and set
\[
F_h(x)=R(h(x-1))=1+\frac{h(x-1)}{D_h(x)},\qquad D_h(x)=1+\frac h2(1-x)+\frac{h^2}{12}(1-x)^2.
\]
Write \(D_0=h^2+6h+12\), and define
\[
\rho=\frac{h}{\sqrt{D_0}},\qquad
\theta=\arctan\frac{\sqrt3}{h+3},\qquad
0<\theta<\frac\pi6.
\]
Then \(\cos\theta=(h+3)/\sqrt{D_0}\), \(\sin\theta=\sqrt3/\sqrt{D_0}\), and
\[
D_h(x)=\frac{D_0}{12}\bigl(1-2\rho\cos\theta\,x+\rho^2x^2\bigr).
\]
The standard generating-function identity for the sine/Chebyshev sequence gives, as an absolutely convergent series for \(|x|\le1\),
\[
\frac1{D_h(x)}=\sum_{j\ge0}a_jx^j,
\qquad
 a_j=\frac{12}{D_0}\rho^j\frac{\sin((j+1)\theta)}{\sin\theta}.
\]
(The denominator zeros lie outside the closed unit disk, since \(0<\rho<1\).) Consequently the coefficient of \(x^j\) in \(F_h\) is
\[
c_0=1-ha_0=\frac{h^2-6h+12}{D_0}>0,\qquad
c_j=h(a_{j-1}-a_j)\quad(j\ge1).
\]
The first \(n-1\) states have the transient upper-bidiagonal generator \(-I+N\), with \(N\) the nilpotent superdiagonal shift. Hence \((M_n(h))_{i,i+j}=c_j\) whenever \(1\le i\le i+j\le n-1\). Mass conservation gives its absorbing entry exactly as the complementary partial sum
\[
(M_n(h))_{i,n}=1-\sum_{j=0}^{n-i-1}c_j=h a_{n-i-1}.
\]
Thus, with \(r=n-i-1\), every structurally permitted absorbing entry is
\[
q_r=h a_r=\frac{12h}{D_0}\rho^r\frac{\sin((r+1)\theta)}{\sin\theta},
\qquad 0\le r\le n-2.
\]
In particular there are *no additional entries* beyond these coefficients, absorbing tails and the final identity row.

**Step 2: a closed formula for signs of transient transitions.** The definitions imply
\[
\rho=\cos\theta-\sqrt3\sin\theta,\qquad
 h=\sqrt3\cot\theta-3.
\]
Using the addition identity for sine,
\[
\sin(j\theta)-\rho\sin((j+1)\theta)
=2\sin\theta\sin\left((j+1)\theta-\frac\pi6\right).
\]
Therefore
\[
\boxed{c_j=\frac{24h}{D_0}\rho^{j-1}
\sin\left((j+1)\theta-\frac\pi6\right)}
\quad(j\ge1).
\]
For \(n\ge3\), the entry \(c_1\) exists, so the necessary condition \(c_1\ge0\) is equivalent, using \(0<\theta<\pi/6\), to \(2\theta-\pi/6\ge0\), i.e.
\[
\theta\ge\frac\pi{12}\quad\Longleftrightarrow\quad h\le2\sqrt3.
\]

**Step 3: all absorbing entries, simultaneously.** For \(0<\theta<\pi/6\), and any integer \(N\ge1\), the inequalities \(\sin(k\theta)\ge0\) for **every** \(1\le k\le N\) are equivalent to \(N\theta\le\pi\). For necessity, if \(N\theta>\pi\), let \(k\) be the smallest index with \(k\theta>\pi\); then \(\pi<k\theta\le\pi+\theta<2\pi\), so its sine is strictly negative. The case of an exact earlier crossing \(j\theta=\pi\) does not help, because the next value is negative. Sufficiency is immediate. Applied to the \(q_r\), this is precisely
\[
q_r\ge0\ (0\le r\le n-2)\quad\Longleftrightarrow\quad
(n-1)\theta\le\pi.
\]

**Step 4: sufficiency and all dimensions.** Suppose \(n\ge3\) and both inequalities \(\theta\ge\pi/12\) and \((n-1)\theta\le\pi\) hold. Then, for every \(1\le j\le n-2\),
\[
0\le2\theta-\frac\pi6\le (j+1)\theta-\frac\pi6
\le\pi-\frac\pi6<\pi.
\]
Hence every \(c_j\ge0\). Step 3 gives every \(q_r\ge0\), and Step 1 gives \(c_0>0\); therefore the conditions are jointly **sufficient**. Conversely, any nonnegative endpoint must satisfy both inequalities by Steps 2–3. Thus positive-step feasibility for \(n\ge3\) is *equivalent* to
\[
\frac\pi{12}\le\theta\le
\min\left\{\frac\pi6,\frac\pi{n-1}\right\},
\qquad \theta=\arctan\frac{\sqrt3}{h+3}.
\]
The function \(\theta(h)\) decreases strictly from \(\pi/6\) (as \(h\downarrow0\)) to zero (as \(h\to\infty\)). If \(3\le n\le7\), the absorbing inequality is automatic and \(0<h\le2\sqrt3\) is the full positive range. If \(8\le n\le13\), the sharp lower step is \(h_n=\sqrt3\cot(\pi/(n-1))-3\), and the window ends at \(2\sqrt3\). At \(n=13\) the two boundaries coincide. At \(n\ge14\), \(\pi/(n-1)<\pi/12\), so no positive step is feasible. When \(n=2\), the only nontrivial entries are \(c_0>0\) and \(q_0=12h/D_0>0\) for every \(h>0\). Finally \(M_n(0)=I\) is nonnegative for every \(n\). This proves the theorem.

## Verification

The accompanying standalone standard-library Python program `verify_gauss_birth.py` computes \(M_n(h)\) by **independent exact-rational Gaussian elimination** on the denominator matrix and compares every entry with a separate generating-function coefficient recurrence. It tests all \(2\le n\le18\), twelve rational timesteps including zero, normalizes every row, and checks the predicted positivity classification. A fresh execution produced `VERIFY_OK 27584 exact assertions`. It additionally checks exact formulas for the transient diagonal and nearest-neighbor entries.

The verifier checks finite instances only. The statements for all integers \(n\ge2\), the boundary at the irrational step \(2\sqrt3\), and the exact trigonometric threshold follow from the analytic proof above, **not** from numerical or finite enumeration. The verifier requires no third-party library.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten [1] establish that diagonal Padé discretization can destroy positivity even for arbitrarily small steps; their Section 4 studies an eight-dimensional nilpotent/Metzler chain and sufficient general positivity criteria. They do not give a complete all-length classification of the stochastic absorbing pure-birth chain here. Lóczi and Ketcheson [2] establish the vanishing unrestricted absolute-monotonicity radius of the \([2/2]\) rational approximant; a global radius of zero neither implies nor supplies this graph-specific exact timestep domain.

The published *eight-state barrier for Markov positivity of the [2/2] Padé map* [3] already gives the full stochasticity window at \(n=8\), including the same lower endpoint \(h_8\) (expressed there as an algebraic root), and proves the general seven-state small-step guarantee. Neither fact is claimed as new. The new conclusion here is the **simultaneous exact classification for every chain length**, including the sharp feasible maximum \(n=13\), an isolated positive feasible step at that maximum, and impossibility for every \(n\ge14\). The finite-dimensional window for eight states is an explicit included special case, not separate novelty.

The later Fokker–Planck rational-map discussion [4] studies eventually exponentially positive generators and other Padé maps; its accessible abstract does not establish the above pure-birth classification, but the full comparison to all results in that work is not claimed complete.

## Limitations

Only a *unit-rate*, *absorbing*, *one-directional* birth chain and the unmodified two-stage Gauss–Legendre **endpoint** are classified. There is no claim for arbitrary unequal birth rates, branching or reversible generators, nonlinear time stepping, intermediate Runge–Kutta stages, finite-precision sign robustness, or numerical accuracy at the positive recovery timesteps. An entrywise-positive endpoint can still be a poor approximation to the exact semigroup for a large step. Literature comparisons are bounded to the inspected material and searches; independent validation of this theorem has not been conducted.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, “Essentially Negative News About Positive Systems,” *Linear Algebra and its Applications* **436** (2012), 3425–3442, DOI: https://doi.org/10.1016/j.laa.2011.12.021. Open author manuscript: https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf. Public repository deposit recorded 2012-06-19: https://mural.maynoothuniversity.ie/id/eprint/3761/.
2. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS J. Comput. Math.* **17** (2014), 159–205; preprint https://arxiv.org/abs/1303.6651 (first public 2013-03-26).
3. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” published-finding corpus (published 2026-09-20), https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
4. A. Itkin and R. Kazbek, “Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker–Planck equation,” https://arxiv.org/abs/2608.22703 (2026-08-24).
