# Exact stochasticity reentry for fourth-order Gauss stepping on the directed eight-cycle

## Finding

Let \(P\) be the cyclic permutation matrix on eight states, \(P^8=I\), and set \(Q=P-I\). The matrix \(Q\) is an irreducible continuous-time Markov generator with a uniform stationary distribution. For \(h\ge0\), the completed two-stage, order-four Gauss--Legendre step is
\[
 T(h)=r(hQ),\qquad r(z)=\frac{12+6z+z^2}{12-6z+z^2}.
\]
There exist two uniquely specified numbers \(h_-\) and \(h_+\) such that
\[
\boxed{T(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad h=0\ \text{or}\ h_-\le h\le h_+.}
\]
Here \(h_-=0.51225154437271\ldots\) is the unique positive root of
\[
 G(h)=7h^6+84h^5+420h^4+1008h^3+1008h^2-432,
\]
and \(h_+=3.52719746626943\ldots\) is the unique positive root of
\[
\begin{aligned}
F(h)={}&5h^{12}+96h^{11}+792h^{10}+3672h^9+9288h^8\\
 &-111024h^6-528768h^5-1446336h^4-2612736h^3\\
 &-3110400h^2-2239488h-746496.
\end{aligned}
\]
For every \(h\), all row sums and column sums of \(T(h)\) equal one. For \(0<h<h_-\), the coefficient on the seven-step cyclic transition is negative; for \(h>h_+\), the coefficient on the one-step transition is negative. Every matrix entry is strictly positive when \(h_-<h<h_+\).

Thus fourth-order Gauss stepping on an irreducible, doubly stochastic Markov generator can *lose* positivity for arbitrarily small steps, *regain* it on one bounded interval, and lose it again for larger steps.

## Assumptions and scope

The directed cycle has states indexed by residues modulo eight and unit clockwise jump rate. The matrix \(P\) sends state \(i\) to state \(i+1\) modulo eight, so \(P^8=I\), \(Q\mathbf1=0\), and \(\mathbf1^TQ=0\). The claim concerns the completed end-step matrix, not the internal stage values, and exact real arithmetic. For a uniform jump rate \(\lambda>0\), the criterion applies to the dimensionless product \(\lambda h\).

## Proof

**Rational matrix reduction.** Put \(X=P\) and work in the commutative algebra \(\mathbb Q[h,X]/(X^8-1)\). Define
\[
M=12-6h(X-1)+h^2(X-1)^2,
\quad N=12+6h(X-1)+h^2(X-1)^2.
\]
The denominator of \(r(hQ)\) is invertible for all \(h\ge0\): its scalar roots are \(3\pm i\sqrt3\), whereas every eigenvalue of \(hQ\) has nonpositive real part. Therefore \(T(h)=NM^{-1}\), and \(r(0)=1\) implies both stochastic sum identities, independently of signs.

**Exact coefficient certificate.** Direct multiplication in the cyclic algebra gives
\[
M\sum_{j=0}^7 A_j(h)X^j=\Delta(h)N,
\]
with \(\Delta(h)>0\) for \(h\ge0\), because its ascending-power coefficient vector is
\[
(2239488,8957952,17169408,20901888,18071424,11757312,5951232,2389824,769392,199584,41832,7056,924,84,4).
\]
Thus \(T(h)=\sum_{j=0}^7[A_j(h)/\Delta(h)]P^j\). The eight cyclic permutation matrices have pairwise disjoint entry supports; accordingly, entrywise nonnegativity is **equivalent** to \(A_j(h)\ge0\) for every \(j\).

Four coefficient polynomials, \(A_0,A_4,A_5,A_6\), have exclusively nonnegative coefficients and are positive at positive \(h\). For completeness, the ascending coefficient vector of \(A_0\) is
\[
(2239488,6718464,9331200,7838208,4354560,1632960,399168,58320,7344,4536,3276,1512,420,63,4).
\]
The other three factor as
\[
\begin{aligned}
A_4={}&3h^4(h^9+48h^8+624h^7+4284h^6+18648h^5+54432h^4\\
&\hspace{7mm}+106704h^3+134784h^2+98496h+31104),\\
A_5={}&9h^5(h+2)(h^7+22h^6+180h^5+816h^4+2232h^3\\
&\hspace{7mm}+3600h^2+3024h+864),\\
A_6={}&3h^7(5h^6+84h^5+588h^4+2268h^3+5040h^2+6048h+3024).
\end{aligned}
\]
The four sign-sensitive coefficients are
\[
A_1=-3hF(h),\quad A_2=-9h^2(h+2)F_2(h),\quad A_3=-3h^3F_3(h),\quad A_7=3h^7G(h),
\]
where
\[
\begin{aligned}
F_2(h)={}&h^{10}+10h^9-516h^7-4248h^6-19728h^5-60912h^4\\
 &-128736h^3-181440h^2-155520h-62208,\\
F_3(h)={}&h^{10}-12h^9-396h^8-3888h^7-22176h^6-84672h^5\\
 &-225072h^4-414720h^3-508032h^2-373248h-124416.
\end{aligned}
\]
All four polynomials \(F,F_2,F_3,G\) have negative constant coefficients, positive leading coefficients, and **exactly one sign change** in descending coefficients. Descartes' rule together with continuity gives each exactly one positive root. Exact substitution shows
\[
 G(0)<0<G(1),\quad F(3)<0<F(4),\quad F_2(4)<0,\quad F_3(4)<0.
\]
Hence the positive roots occur in the order
\[
0<h_-<1<3<h_+<4<\min\{\rho(F_2),\rho(F_3)\},
\]
where \(\rho\) denotes the unique positive root. Therefore \(A_7(h)\ge0\) exactly for \(h\ge h_-\), while \(A_1,A_2,A_3\ge0\) simultaneously for positive \(h\) exactly on \(0<h\le h_+\). The four other coefficients are positive for \(h>0\). At \(h=0\), the rational map is the identity. This proves the stated complete positivity set and strict positivity on its open nonzero interval.

The multiplication identity, all polynomial coefficients, the four one-sign-change tests and the interval comparisons are independently replayable with integer-only polynomial arithmetic in the bundled program `artifacts/verify_cycle.py`; no floating-point comparisons enter the proof.

## Verification

Run `python3 artifacts/verify_cycle.py` using Python 3 and no third-party packages. It checks the cyclic rational-matrix identity coefficient by coefficient, verifies the four sign-sensitive factorizations and the two positive root intervals, and reports the decimal endpoints by exact rational bisection. Separate exact \(8\times8\) rational-matrix comparisons at \(h=1/4,1,3,4,10\) agreed with the polynomial formula and yielded the predicted signs. Finite spot checks are supplemental; the global assertion follows from the polynomial identity and sign arguments.

## Relationship to prior work

The cited work on implicit Runge--Kutta boundedness explains why rational stability and positivity are distinct. Zappavigna, Colaneri, Kirkland and Shorten study small-step positivity loss for the same \([2/2]\) rational map, including a nonconservative nilpotent/Metzler construction. A prior exact Markov classification establishes the eight-state minimum and an intermediate positivity window for an **absorbing pure-birth chain**. Neither its upper-triangular generator nor its numerical window is equivalent under relabeling to the present irreducible cyclic generator, which has uniform stationary distribution and a different exact window. The present result proves the full interval specifically for this canonical strongly connected, balanced Markov network. General absolute-monotonicity results do not determine the entry signs of this particular eight-state circulant.

## Limitations

This is an exact classification for one uniform eight-state oriented cycle, not a characterization of all irreducible eight-state generators or all directed cycles. It does not assert internal-stage positivity or preservation for nonlinear ODEs, and does not provide a universal safe step size for other chains. Earlier work gives the general minimal state count; that claim is not asserted as new. Related broader rational monotonicity literature may contain indirect consequences not detected by the comparisons, so originality should be checked independently before publication.

## References

1. W. Hundsdorfer, B. Mozartova, M. N. Spijker, “Stepsize Conditions for Boundedness in Numerical Initial Value Problems,” *SIAM Journal on Numerical Analysis* 47 (2009), https://doi.org/10.1137/090745842 (online publication December 4, 2009).
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), https://doi.org/10.1016/j.laa.2011.12.021 ; lawful author manuscript: https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf .
3. L. Lóczi, D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* 17 (2014), https://doi.org/10.1112/S1461157013000326 .
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” published mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
