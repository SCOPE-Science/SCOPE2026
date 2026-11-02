# The eleven-state feasibility cutoff for Radau IIA on absorbing birth chains

## Finding
Let \(n\ge2\) be an integer. Let \(Q_n\) be the generator of the unit-rate, one-way absorbing birth chain \(1\to2\to\cdots\to n\): its entries are \((Q_n)_{i,i}=-1\) and \((Q_n)_{i,i+1}=1\) for \(1\le i<n\), with the final row zero. For the unmodified two-stage, third-order Radau IIA method, put
\[
R(z)=\frac{6+2z}{6-4z+z^2},\qquad M_n(h)=R(hQ_n),\quad h\ge0.
\]
The following statements hold, exactly:

1. A strictly positive timestep \(h>0\) with entrywise nonnegative \(M_n(h)\) exists **if and only if** \(n\le11\). For every \(n\ge12\), the complete entrywise-nonnegative timestep set is \(\{0\}\).
2. For \(2\le n\le5\), the complete set is \([0,3]\).
3. For \(n=6\), the complete set is
\[
\{0\}\cup[\gamma,3],\qquad
\gamma=0.253946561637298\ldots,
\]
where \(\gamma\) is the unique positive root of
\[
P(h)=h^5+30h^4+180h^3+360h^2+180h-72.
\]
4. For every \(7\le n\le11\), some interval \((3-\varepsilon_n,3]\), with \(\varepsilon_n>0\), is entrywise nonnegative; every \(h>3\) is unsafe. For every \(n\ge6\), all sufficiently small positive steps are unsafe.

The complete positive-timestep sets for \(7\le n\le11\) are **not** claimed here. No irreducibility, unequal-rate, internal-stage, or arbitrary-generator statement is asserted beyond the specified family.

## Assumptions and scope
All chains are finite, have the indicated absorbing final state, and have exactly unit jump rates. Matrices act on column vectors of state values while generators have row sums zero; entrywise nonnegativity of \(M_n(h)\) is equivalent to preserving the nonnegative cone of vectors and, together with \(M_n(h)\mathbf 1=\mathbf 1\), to being stochastic. The denominator matrix is invertible for all \(h\ge0\), as the only eigenvalues of \(Q_n\) are \(0\) and \(-1\), and \(6+4h+h^2>0\).

## Proof
Write
\[
A=h^2+4h+6,\qquad B=2h(h+2),\qquad C=h^2,
\]
and define \(f_h(z)=R(h(z-1))=(6-2h+2hz)/(A-Bz+Cz^2)\). For \(k\ge0\), set \(c_k=[z^k]f_h(z)\), \(b_k=1-\sum_{j=0}^{k}c_j\). The transient-to-transient entries of \(M_n(h)\), indexed \(0,\ldots,n-2\), are \(c_{j-i}\) for \(j\ge i\), and zero below the diagonal. The transition from transient state \(i\) to the absorbing state is \(b_{n-2-i}\), and the absorbing row is the unit row. These formulas follow either by the nilpotent upper-shift functional calculus on the transient block or by \(R(hQ_n)\mathbf1=\mathbf1\). Consequently, entrywise nonnegativity is precisely
\[
c_0,\ldots,c_{n-2}\ge0,\qquad b_0,\ldots,b_{n-2}\ge0.
\]
The generating-function identities give
\[
\begin{aligned}
c_0&=\frac{2(3-h)}A,\\
c_1&=\frac{2h(-h^2+6h+18)}{A^2},\\
c_2&=\frac{2h^2(h+3)(-h^2+12h+18)}{A^3},\\
c_3&=\frac{2h^3(-h^4+12h^3+108h^2+216h+108)}{A^4},\\
c_4&=\frac{2h^4(-h^5+15h^4+180h^3+540h^2+540h+108)}{A^5}.
\end{aligned}
\]
Every one of these is nonnegative for \(0\le h\le3\), and \(c_0<0\) whenever \(h>3\). Also
\[
\begin{aligned}
b_0&=\frac{h(h+6)}A,\\
b_1&=\frac{h^2(h^2+12h+18)}{A^2},\\
b_2&=\frac{h^3(h^3+18h^2+54h+36)}{A^3},\\
b_3&=\frac{h^4(h^4+24h^3+108h^2+144h+36)}{A^4},\\
b_4&=\frac{h^5P(h)}{A^5}.
\end{aligned}
\]
Thus the assertions for \(2\le n\le5\) follow. For \(n=6\), \(P'(h)=5h^4+120h^3+540h^2+720h+180>0\) on \(h\ge0\), while \(P(0)=-72<0<P(3)\); hence its unique positive zero \(\gamma\) determines the claimed complete interval. Direct rational substitution gives \(P(253946/10^6)<0<P(253947/10^6)\).

For the larger-size obstruction use the generating function
\[
\sum_{k\ge0}b_kz^k=\frac{1-f_h(z)}{1-z}
=\frac{h(h+6)-h^2z}{A-Bz+Cz^2}.
\]
For \(h>0\) define
\[
r=\frac h{\sqrt A},\quad
\phi=\arctan\frac{\sqrt2}{h+2},\quad
\psi=\arctan\frac{\sqrt2(h+6)}{4h+6}.
\]
The quadratic's conjugate poles, or the second-order coefficient recurrence, yield the exact identity
\[
b_k=r^{k+1}\frac{\sqrt{(4h+6)^2+2(h+6)^2}}{A\sin\phi}\sin(k\phi+\psi).
\]
The prefactor is positive. For \(0<h\le3\), both \(\phi\) and \(\psi\) decrease with \(h\). Moreover
\[
\phi\ge\phi(3)=\arctan(\sqrt2/5)>\pi/12,\qquad
\psi\ge\psi(3)=\arctan(1/\sqrt2)>\pi/6.
\]
(The first strict comparison follows from \(\sqrt2/5>2-\sqrt3=\tan(\pi/12)\); the second from \(1/\sqrt2>1/\sqrt3\).) Therefore \(\psi+10\phi>\pi\), while \(0<\psi<\pi/2\) and \(0<\phi<\pi/2\). At the first integer \(k\le10\) with \(k\phi+\psi>\pi\), this angle belongs to \((\pi,2\pi)\), whence \(b_k<0\). This is a forbidden entry whenever \(n\ge12\). For \(h>3\), the negative diagonal \(c_0\) is already a forbidden entry. The sole safe step for \(n\ge12\) is consequently \(h=0\).

It remains to show feasibility through eleven states. At \(h=3\), the coefficient recurrence is \(c_0=0\), \(c_1=2/9\), and
\[
c_k=(10c_{k-1}-3c_{k-2})/9\quad(k\ge2).
\]
Exact successive evaluation gives the following numerators after multiplying \(c_k\) and \(b_k\) by \(9^k\), respectively, for \(k=1,\ldots,9\):
\[
\begin{aligned}
9^kc_k:&\quad 2,20,146,920,5258,27740,135434,605360,2396882,\\
9^kb_k:&\quad 7,43,241,1249,5983,26107,99529,290401,216727.
\end{aligned}
\]
All these numerators are strictly positive, and \(b_0=1\). Thus \(M_{11}(3)\) is nonnegative. The coefficient conditions for every smaller \(n\) are a subset, so \(M_n(3)\) is nonnegative for every \(2\le n\le11\). Continuity and strict positivity of all applicable coefficients except \(c_0(3)=0\), which becomes positive just below \(3\), give a nondegenerate safe interval ending at \(3\). Finally, since the coefficient of \(z^5\) in the Taylor series of \(R(z)\) is \(-1/108\), the first-to-sixth transition in every chain with \(n\ge6\) is \(-h^5/108+O(h^6)<0\) for all sufficiently small positive \(h\). This completes the proof.

## Verification
The accompanying `verify.py` uses exact symbolic rational identities to verify the generating functions, coefficients, six-state full matrix, polynomial bracket, and positive endpoint numerators. It also compares recurrence-built matrices with independently inverted rational matrices in dimensions \(2,3,4,5,6,7,11,12\) at four positive rational steps. Execute `python3 verify.py` with SymPy installed. The replay completed **1701 exact assertions**. These computations corroborate the finitely stated identities; the all-dimensional obstruction is proved by the sine-phase argument, not by enumeration.

## Relationship to prior work
Lóczi and Ketcheson (2013) study absolute monotonicity of rational exponential approximations, supplying the general positivity/SSP context; they do not determine the present absorbing birth-chain cutoff. Higueras, Ketcheson and Kocsis (2015) optimize positivity-preserving *perturbations*, whereas this result fixes the unmodified Radau IIA method. A prior calculation for unit-rate directed cycles already demonstrated small-step negativity from six states onward and eventual large-step recovery; neither that small-step observation nor the general fifth Taylor coefficient is claimed as original. The new distinction is the absorbing-chain **eleven-state nonexistence frontier** and the exact bounded positive interval at six states. The known eight-state \([2/2]\) Padé/ Gauss–Legendre Markov barrier concerns a different rational time-stepping function and does not imply this frontier.

## Limitations
This is an exact result for *unit-rate absorbing pure-birth* generators only, not for arbitrary CTMCs, and it concerns endpoint matrices rather than intermediate implicit stages. The precise full safe sets for dimensions seven through eleven are left unresolved. Specialist historical overlap is not ruled out.

## References
1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (first public 26 March 2013). https://arxiv.org/html/1303.6651v1
2. I. Higueras, D. I. Ketcheson, and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, arXiv:1505.04024 (first public 15 May 2015). https://arxiv.org/abs/1505.04024
3. *Eight-state barrier for Markov positivity of the \([2/2]\) Padé map*, published published-finding corpus finding, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab (comparison restricted to the available description).
