# A sharp mean-square stability boundary for randomized Runge–Kutta integration of a pure-delay equation

## Finding

Consider the real delay equation
\[
y'(t)=-b\,y(t-1),\qquad b>0,
\]
with a continuous initial history on \([-1,0]\). Apply the two-stage randomized Runge–Kutta construction of Difonzo, Przybyłowicz, Wu and Xie [1] using **one step per unit delay**, hence step length \(h=1\), with a newly sampled independent uniform stage \(\gamma_j\in(0,1)\) in each successive delay interval. Write \(s=b\). After the initial interval, the grid values obey the exact recursion
\[
Y_{j+1}=Y_j-sY_{j-1}+s^2\gamma_jY_{j-2},\qquad j\ge1.
\]
For the three-coordinate state \(V_j=(Y_j,Y_{j-1},Y_{j-2})^{\mathsf T}\), mean-square stability means \(\mathbb E\|V_j\|_2^2\to0\) for every nonzero deterministic initial state. There is a unique number \(s_*\in(9/8,7/6)\), characterized by
\[
Q(s_*)=0,\quad
Q(s)=s^7-s^5-4s^4-4s^3+12s^2-24s+24,
\]
for which the sharp classification is
\[
\boxed{\text{mean-square stable exactly for }0<s<s_*},\qquad
s_*=1.1444760473540796515\ldots.
\]
At the boundary, every nonzero initial state has nonvanishing mean-square state norm, and above it that norm grows exponentially. By contrast, at the exact rational parameter \(s=7/6\), the expected iterate converges to zero exponentially for every deterministic initial state, and the **deterministic central-stage method**, obtained by replacing \(\gamma_j\) by \(1/2\), is Schur stable. The randomized method is nevertheless mean-square unstable because
\[
\det(I-M(7/6))=-\frac{1270787}{20155392}<0,
\]
where \(M\) is its six-dimensional second-moment operator. In particular, this separation applies to every nonzero constant starting history.

More generally, for any independent stage law with mean \(1/2\) and variance \(v\), the second-moment growth factor is **nondecreasing with \(v\)** for fixed \(s>0\), and strictly increasing between positive variances. This gives a structural explanation for why independently randomized stages can lose long-time mean-square stability even when their deterministic central-stage counterpart is stable.

## Assumptions and scope

The delay and step are both fixed at one. Arithmetic is exact; there is no exogenous forcing or observation noise. The stage variables used in distinct delay intervals are independent. The source method uses the *current interval's* sampled stage also to reconstruct the delayed intermediate value, rather than reusing a sampled stage from the preceding interval. The state definition includes two preceding grid values, and exponential growth/decay refers to this three-dimensional state in expectation, not to an almost-sure Lyapunov exponent. At \(s=0\) the recurrence is not asymptotically stable. All other parameter values \(s>0\) are covered by the theorem.

The starting history may be arbitrary and continuous. After the first interval the method is a homogeneous random recurrence. For a nonzero constant history \(\varphi\equiv c\), its initial three-vector at the beginning of this recurrence is \(((1-s)c,c,c)^{\mathsf T}\), which is nonzero. Thus the sharp classification is applicable to genuine histories, not just artificially initialized linear recurrences.

## Proof

**1. Exact source-method specialization.** Equations (2.3)–(2.4) of [1] set the delayed intermediate value, when there is one step in each delay interval, to
\[
\widetilde Y_{j-1}=Y_{j-1}+\gamma_j f(Y_{j-1},Y_{j-2})
                  =Y_{j-1}-s\gamma_jY_{j-2}.
\]
Because \(f(t,x,z)=-sz\) is independent of \(t,x\), the current-state predictor cancels from the update. Hence the stated three-lag recurrence follows, with companion matrix
\[
B_s(g)=\begin{pmatrix}1&-s&s^2g\\1&0&0\\0&1&0\end{pmatrix},\quad
V_{j+1}=B_s(\gamma_j)V_j.
\]

**2. Exact second-moment transfer.** If \(X_j=\mathbb E[V_jV_j^{\mathsf T}]\), then
\[
X_{j+1}=\Phi_s(X_j),\quad
\Phi_s(X)=\mathbb E[B_s(\gamma)XB_s(\gamma)^{\mathsf T}].
\]
In coordinate order \((X_{11},X_{12},X_{13},X_{22},X_{23},X_{33})\), integration using \(\mathbb E\gamma=1/2\) and \(\mathbb E\gamma^2=1/3\) yields
\[
M(s)=\begin{pmatrix}
1&-2s&s^2&s^2&-s^3&s^4/3\\
1&-s&s^2/2&0&0&0\\
0&1&0&-s&s^2/2&0\\
1&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&0&1&0&0
\end{pmatrix}.
\]
Direct symbolic elimination gives the exact identity
\[
\det(I-M(s))=\frac{s}{12}Q(s).
\]

**3. Why the Perron root is the actual all-initial-state growth factor.** The map \(\Phi_s\) preserves the cone of positive-semidefinite symmetric matrices. Its adjoint therefore has a nonzero positive-semidefinite eigenmatrix \(P\) with eigenvalue \(r(s)=\rho(M(s))\). In fact, \(P\) is positive definite. To see this, any vector in \(\ker P\) is mapped by \(B_s(g)\) back into \(\ker P\) for almost every \(g\), by the nonnegativity of the terms in \(\mathbb E[B_s(g)^{\mathsf T}PB_s(g)]=r(s)P\). The entries are polynomial in \(g\), so the invariance holds for all \(g\). For \(s>0\), the family \(\{B_s(g):0<g<1\}\) has no common nontrivial proper invariant subspace: a subspace containing a vector with nonzero third coordinate contains the first basis vector by taking differences of two stage matrices, then the second and third basis vectors by applying the companions; a subspace whose vectors all have third coordinate zero must itself be zero by the last two rows of the companion. Thus \(\ker P=\{0\}\).

Consequently, for every deterministic nonzero state \(V_0\),
\[
\mathbb E[V_j^{\mathsf T}PV_j]=r(s)^jV_0^{\mathsf T}PV_0.
\]
Positive definiteness of \(P\) makes \(\mathbb E\|V_j\|_2^2\) comparable to \(r(s)^j\) with fixed positive constants. Stability, nondecay, and growth therefore correspond exactly to \(r(s)<1\), \(r(s)=1\), and \(r(s)>1\), respectively.

**4. One crossing, and no reentrant stability.** At \(s=0\), \(M(0)\) has one simple eigenvalue one and five eigenvalues zero. Its left and right eigenvectors at one may be taken as the first coordinate row and the all-ones column. Direct differentiation gives \(r'(0)=-2\), so \(r(s)<1\) for all sufficiently small positive \(s\). An exact Sturm sequence for \(Q\) has eight members of degrees \(7,6,5,4,3,2,1,0\), with sign-variation counts \(4\) at \(s=0\) and \(3\) at \(s=3/2\). Therefore \(Q\) has exactly one distinct root in \((0,3/2)\). The rational evaluations \(Q(9/8)>0\) and \(Q(7/6)=-181541/279936<0\) isolate it as \(s_*\). If \(r\) crossed one before \(s_*\), the positive cone's Perron eigenvalue would force an additional zero of \(\det(I-M)\), which is impossible. Hence \(r<1\) throughout \((0,s_*)\), and continuity gives \(r(s_*)=1\).

On \((s_*,\sqrt2)\) the polynomial \(Q\) is negative (there is no second root below \(3/2\)), so \(\det(I-M)<0\); since \(\det(\lambda I-M)\to+\infty\) as \(\lambda\to+\infty\), \(M\) has a real eigenvalue greater than one. For \(s\ge\sqrt2\), the mean companion \(A_s=\mathbb E B_s\) has determinant \(s^2/2\), so its spectral radius is at least \((s^2/2)^{1/3}\ge1\). Jensen's inequality implies \(r(s)\ge\rho(A_s)^2\); thus there is no mean-square stability in this range either. This proves the complete all-positive-parameter classification.

**5. Exact mean-versus-second-moment separation.** At \(s=7/6\), the characteristic polynomial of \(A_s\) is \(z^3-z^2+sz-s^2/2\). Under the disk-to-left-half-plane map \(z=(1+w)/(1-w)\), its numerator becomes
\[
\frac{277w^3+57w^2+207w+35}{72}.
\]
All coefficients are positive and \(57\cdot207>277\cdot35\), so the cubic Routh–Hurwitz criterion places all roots in the open left half-plane, proving that \(A_s\) is Schur stable. But the exact negative determinant displayed above forces \(r(7/6)>1\). Indeed numerical diagonalization, used only to illustrate the proved inequality, gives \(r(7/6)\approx1.02645717\).

**6. Stage variance law.** For an independent law of stage \(g\) with \(\mathbb E g=1/2\) and variance \(v\), writing \(E=e_1e_3^{\mathsf T}\) gives
\[
\Phi_{s,v}(X)=A_sXA_s^{\mathsf T}+s^4vX_{33}e_1e_1^{\mathsf T}.
\]
Thus increasing \(v\) increases the positive map in the cone order, so its spectral radius cannot decrease. Strictness between two positive variances follows by pairing a nonzero positive eigenmatrix of the smaller map with the positive-definite adjoint eigenmatrix of the larger one: the added term has strictly positive pairing, since the smaller eigenmatrix has a positive third diagonal entry by the companion's irreducibility. This establishes the stated monotonicity.

## Verification

The standalone `verify.py` reconstructs the covariance map by integrating the original random companion exactly, checks the displayed matrix and determinant symbolically, computes the complete Sturm sequence and its two endpoint variation counts, checks the exact rational comparison value and the strict Routh–Hurwitz inequalities, and verifies the stage-variance decomposition. It also computes a high-precision approximation to the unique root, which is not used as proof of root uniqueness. Execute `python verify.py` with `sympy>=1.12` and `mpmath>=1.3`; the recorded execution is in `verification_output.txt`.

## Relationship to prior work

Difonzo–Przybyłowicz–Wu–Xie [1] define the exact randomized delayed-stage update and prove fixed-horizon \(L^p\) convergence; their Sections 2, 4 and 5 do not determine this infinite-horizon pure-delay second-moment boundary. Bochacik–Goćwin–Morkisz–Przybyłowicz [2, Section 5] derive the mean-square stability region of randomized Runge–Kutta applied to the **nondelayed scalar ODE test equation**, establishing the relevant distinction between random and central-stage stability but not the three-lag stochastic delay recurrence or its degree-seven threshold. Engelborghs–Roose [3] consider characteristic roots and stability of **deterministic linear multistep delay methods**, not independent random stages. The general finite-dimensional positive-map spectral criterion and Sturm theorem are standard proof tools; the result here is the exact method-specific delay threshold and its mean/mean-square separation.

## Limitations

The theorem is for one step per delay, a linear scalar pure-delay test equation, independently resampled stages and exact arithmetic. It does not classify the almost-sure Lyapunov exponent, higher moments, arbitrary ratios of delay to step, nonlinear equations or the influence of accumulated floating-point errors. The source article's fixed-horizon convergence theorem is not contradicted: infinite-horizon stability at fixed step is a distinct question. Other random difference-equation formulations could potentially contain an equivalent result; the cited comparisons do not establish exhaustive bibliographic uniqueness.

## References

1. F. V. Difonzo, P. Przybyłowicz, Y. Wu and X. Xie, *A Randomized Runge-Kutta Method for time-irregular delay differential equations*, arXiv:2401.11658v1, first posted 2024-01-22, specifically Eqs. (2.3)–(2.4), Theorem 4.3 and Section 5. https://arxiv.org/html/2401.11658v1
2. T. Bochacik, M. Goćwin, P. M. Morkisz and P. Przybyłowicz, *Randomized Runge-Kutta method—stability and convergence under inexact information*, arXiv:2006.12131v1 (2020), specifically Section 5. https://arxiv.org/abs/2006.12131
3. K. Engelborghs and D. Roose, *On Stability of LMS Methods and Characteristic Roots of Delay Differential Equations*, SIAM Journal on Numerical Analysis 40 (2002), 629–650. https://doi.org/10.1137/S003614290037472X
4. MSC2020, code 65L03: *Numerical methods for functional-differential equations*. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=65L03
