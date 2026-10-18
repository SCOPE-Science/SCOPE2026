# Sharp Markov positivity barriers for even reciprocal-Taylor Padé approximants

## Finding

Let \(m\ge4\) be even and let
\[
R_m(z)=\left(\sum_{k=0}^{m}\frac{(-z)^k}{k!}\right)^{-1}.
\]
For every finite conservative continuous-time Markov generator \(Q\) of order \(n\le m+2\), there is \(\varepsilon_Q>0\) for which \(R_m(hQ)\) is entrywise nonnegative for every \(0\le h\le\varepsilon_Q\). The bound on the state count is sharp: on the unit-rate pure-birth chain with \(m+3\) states and an absorbing terminal state, the entry from the initial state to the terminal state is negative for every sufficiently small positive \(h\), with the expansion
\[
(R_m(hQ))_{1,m+3}=-\frac{2(m+1)}{(m+2)!}h^{m+2}+O(h^{m+3}).
\]

At order \(m=4\), the seven-state unit pure-birth chain has a particularly exact recovery phenomenon. Its rational update is entrywise nonnegative **if and only if** \(h=0\) or \(h\ge\tau\), where \(\tau\) is the unique positive root of the explicit polynomial \(P\) below, and
\[
0.32606<\tau<0.32607.
\]
For all \(h>0\), its sole potentially negative entry is the initial-to-absorbing transition.

## Assumptions and scope

A conservative \(n\times n\) Markov generator means a real matrix \(Q\) with \(Q_{ij}\ge0\) for \(i\ne j\) and \(\sum_j Q_{ij}=0\). The update \(R_m(hQ)\) is defined by the inverse of \(\sum_{k=0}^{m}(-hQ)^k/k!\). This inverse exists for all sufficiently small \(h\), since its value at \(h=0\) is the identity. It is always row-stochastic whenever it exists: multiplication by the constant-one vector gives the constant-one vector. Entrywise nonnegativity is a separate property.

The sharp dimension statement concerns *sufficiently small positive steps* for arbitrary conservative generators, not a universal step bound independent of \(Q\), nor unconditional positivity for all positive steps. The exact all-step result concerns the specified seven-state unit-rate pure-birth generator, with \(Q_{i,i}=-1\), \(Q_{i,i+1}=1\) for \(1\le i\le6\), and terminal row zero. This is a rational matrix-exponential approximation, not the diagonal Padé or Gauss–Legendre rule.

## Proof

**1. Coefficients and path-length obstruction.** Put \(R_m(z)=\sum_{k\ge0}a_kz^k\). For even \(m\), the denominator differs from \(e^{-z}\) first in degree \(m+1\). Expanding the reciprocal, or multiplying formal series, gives the exact identities
\[
a_k=\frac1{k!}\quad(0\le k\le m),\qquad
a_{m+1}=0,\qquad
a_{m+2}=-\frac{2(m+1)}{(m+2)!}.
\]
Indeed, with \(E_m(z)=\sum_{k=m+1}^{\infty}(-z)^k/k!\), one has \(R_m(z)=e^z(1-e^zE_m(z))^{-1}\), and the preceding coefficients follow through degree \(m+2\). This identity holds as a formal power series and as an analytic expansion around zero.

Write \(Q=U-D\), where \(U\) has nonnegative off-diagonal entries and zero diagonal, and \(D\) is the nonnegative diagonal of exit rates. For distinct vertices \(i,j\), let \(d\) denote the directed shortest-path length from \(i\) to \(j\) in the positive-rate graph, or \(\infty\) if no such path exists. If \(d<\infty\), then \((Q^k)_{ij}=0\) for \(k<d\) and \((Q^d)_{ij}=(U^d)_{ij}>0\). If \(d\le m\), the leading term of the update entry is \(h^d(U^d)_{ij}/d!>0\). If no path exists, the entry is identically zero near zero, since every power \((Q^k)_{ij}\) vanishes.

For \(n\le m+2\), only \(d=m+1\) remains. This forces \(n=m+2\), and every shortest path traverses every vertex once. An all-off-diagonal walk of length \(d+1\) from \(i\) to \(j\) cannot exist: it would repeat a vertex and removing the directed cycle (whose length is at least two) would yield a walk shorter than \(d\). In the expansion of \((U-D)^{d+1}\), terms with two or more diagonal factors likewise have fewer than \(d\) off-diagonal moves and vanish. Consequently
\[
(Q^{d+1})_{ij}=-\sum_{r=0}^{d}(U^rDU^{d-r})_{ij}<0.
\]
Strict negativity follows because at least one exit rate along a positive directed shortest path is positive. Since \(a_d=a_{m+1}=0\) and \(a_{d+1}=a_{m+2}<0\), the first nonzero term in \((R_m(hQ))_{ij}\) is strictly positive. Diagonal entries equal \(1+O(h)\). Finitely many entries then admit a common positive \(\varepsilon_Q\), proving the universal dimension bound.

For the \(m+3\)-state pure-birth generator, the initial-to-terminal shortest path has length \(d=m+2\) and \((Q^d)_{1,m+3}=1\). The coefficient \(a_{m+2}<0\) supplies the asserted negative leading term and proves sharpness for every even \(m\ge4\).

**2. Seven-state exact positivity.** Fix \(m=4\) and write
\[
D(h)=h^4+4h^3+12h^2+24h+24.
\]
On the six transient states the generator is \(-I+N\), with \(N\) the strict upper shift. Therefore its entry at displacement \(j\), for \(0\le j\le5\), equals
\[
c_j(h)=\frac{h^j}{j!}R_4^{(j)}(-h).
\]
Row sums equal one. Hence the probability of absorption from a state \(d\) steps before the absorbing vertex is
\[
g_d(h)=1-\sum_{j=0}^{d-1}c_j(h),\qquad1\le d\le6.
\]
An exact differentiation-and-common-denominator computation shows that each of the six \(c_j\) and each \(g_d\) for \(1\le d\le5\) has a rational expression with strictly positive denominator and a numerator polynomial having nonnegative coefficients and at least one positive coefficient. The standalone symbolic certificate `verification.py` constructs and checks these eleven polynomials exactly; the computation is a finite polynomial identity, independent of any floating-point sign test.

For the remaining absorption entry, direct simplification gives
\[
g_6(h)=\frac{h^6P(h)}{D(h)^6},
\]
where
\[
\begin{aligned}
P(h)={}&h^{18}+24h^{17}+312h^{16}+2864h^{15}+17520h^{14}\\
&+72960h^{13}+201664h^{12}+319104h^{11}+41472h^{10}\\
&-1113600h^9-2488320h^8-1078272h^7+6552576h^6\\
&+19243008h^5+28200960h^4+25436160h^3\\
&+12939264h^2-2654208.
\end{aligned}
\]
To prove the **unique positive zero** assertion without numerical root-counting, split \(h>0\) into \(0<h<1\) and \(h\ge1\). For \(0<h<1\), substitute \(h=t/(1+t)\), \(t>0\). The 19 coefficients, ordered from highest to lowest degree, of
\[
(1+t)^{18}P\!\left(\frac{t}{1+t}\right)
\]
have exactly one sign change: twelve positive coefficients followed by seven negative coefficients. Descartes' rule gives at most one positive root on this interval. For \(h\ge1\), every coefficient of \(P(1+t)\) is strictly positive, so there are no roots. Finally \(P(0)<0<P(1)\) gives one root by continuity, and the strict rational sign tests \(P(32606/100000)<0<P(32607/100000)\) enclose it. Thus \(g_6(h)<0\) for \(0<h<\tau\), equals zero at \(\tau\), and is positive thereafter. All other entries are nonnegative; this proves the exact recovery interval.

## Verification

The self-contained exact-arithmetic Python/SymPy script `verification.py` (requirements in `requirements.txt`) expands the rational functions, checks all eleven coefficientwise positivity certificates, verifies the polynomial identity for \(g_6\), checks both Descartes coefficient sign tests and the rational root bracket, and compares to independently inverted seven-by-seven rational matrices at \(h=1/10\) and \(h=1/2\). It also checks the formal Taylor-coefficient identities for nine even orders as corroboration. Successful replay prints `VERIFY_OK`. None of these finite computational tests substitutes for the analytical arbitrary-order path-length argument in part 1.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten study stability and positivity issues for Padé discretizations of positive systems, mainly diagonal approximants. Xue and Ye analyze entrywise matrix-exponential computation for essentially nonnegative matrices. Those establish the setting but do not state the present even-denominator-degree sharp state count or exact seven-state reciprocal-quartic interval in the inspected full texts. Published discussions of the fourth-order diagonal \([2/2]\) approximation establish a distinct eight-state obstruction: its rational function, first sign-defect coefficient and state dimension differ. The previously known second-order reciprocal-Taylor examples, including \([0/2]\) positive/negative path effects, are covered cases and are not claimed as a new discovery here; this theorem's new family starts at even order four.

Rossi, Colaneri and Shorten study the preservation of polyhedral Lyapunov functions under Padé discretization; preserving such a function does not imply entrywise positivity of a transition matrix. Work on eventual positivity of subdiagonal rational maps concerns a different range or choice of rational approximants. Possible unindexed equivalent formulations remain a limitation.

## Limitations

The universal statement concerns sufficiently small steps, with a generator-dependent bound, and does not classify all-step positivity for arbitrary generators or for even degrees beyond the seven-state fourth-order example. The degree-18 polynomial identity and the eleven positivity checks can be reproduced using exact arithmetic, but independent external validation has not been performed. A related 1996 paper by Arioli, Codenotti and Fassino on Padé matrix exponentials could not be inspected in full; its accessible bibliographic material concerns numerical Padé exponential evaluation. An equivalent specialized result in unindexed literature cannot be excluded.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems* (MTNS, 2010); lawful full text: https://mural.maynoothuniversity.ie/id/eprint/2195/ .
2. J. Xue and Q. Ye, *Computing Exponentials of Essentially Non-negative Matrices Entrywise to High Relative Accuracy*; accessible full text: https://www.ms.uky.edu/~qye/reports/expenm.pdf .
3. M. Arioli, B. Codenotti and C. Fassino, *The Padé method for computing the matrix exponential*, Linear Algebra and its Applications (1996); DOI: https://doi.org/10.1016/0024-3795(94)00190-1 (full text not inspected).
4. F. Rossi, P. Colaneri and R. Shorten, *Padé discretization for linear systems with polyhedral Lyapunov functions*, IEEE Transactions on Automatic Control 56 (2011), 2717–2722; https://mural.maynoothuniversity.ie/id/eprint/2822/ .
5. Published result on the distinct \([2/2]\) Padé Markov positivity barrier: https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
