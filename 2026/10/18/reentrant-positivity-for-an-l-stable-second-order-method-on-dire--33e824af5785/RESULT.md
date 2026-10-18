# Reentrant positivity for an L-stable second-order method on directed cycles

## Finding
Let \(n\ge2\). Write \(P_n\) for the cyclic permutation matrix, with \(P_n^n=I\), and \(Q_n=P_n-I\) for the unit-rate continuous-time Markov generator of a one-way directed cycle. Consider the end-step rational map
\[
T_n(h)=R(hQ_n),\qquad R(z)=\frac{1+(\sqrt2-1)z}{[1-(1-1/\sqrt2)z]^2},\qquad h\ge0.
\]
It is the linear stability map of Alexander's second-order L-stable two-stage SDIRK method and also of L-stable TR-BDF2. Define
\[
\gamma=1-1/\sqrt2,\qquad a=1+\sqrt2,\qquad r=\frac{\gamma h}{1+\gamma h},\qquad
H_n(r)=1-\sqrt2\sum_{k=1}^{n-1}r^k+a(n-1)r^n.
\]
For \(h>0\), the \(j\)-th cyclic entry in every row is exactly
\[
(T_n(h))_{i,i+j\bmod n}=
\frac{(1-r)^2r^j}{(1-r^n)^2}
\bigl[H_n(r)+aj(1-r^n)\bigr],\qquad 0\le j<n.
\]
Therefore \(T_n(h)\) is entrywise nonnegative if and only if \(H_n(r)\ge0\); the entire obstruction is detected by its diagonal.

For \(2\le n\le4\), every positive timestep produces an entrywise strictly positive stochastic matrix. For every \(n\ge5\), the polynomial \(H_n\) has exactly two simple roots \(0<r_-(n)<r_+(n)<1\), and the exact nonnegativity set is the **disconnected** set
\[
\boxed{\;h\in[0,h_-(n)]\cup[h_+(n),\infty),\qquad
h_\pm(n)=\frac{r_\pm(n)}{\gamma[1-r_\pm(n)]}.\;}
\]
Inside \((h_-,h_+)\), every diagonal entry is negative. At either positive boundary every diagonal entry vanishes and every off-diagonal entry is positive. Thus a five-state uniform directed cycle is the smallest member of this family exhibiting loss followed by recovery of Markov positivity.

For \(n=5\), the boundaries are approximately \(h_-(5)=3.222709632051\) and \(h_+(5)=6.805854390690\). An exact common negativity witness for **every** \(n\ge5\) is
\[
\boxed{\;h=\frac{3}{2\gamma}=\frac32(2+\sqrt2),\qquad r=\frac35.\;}
\]
The large-cycle boundaries obey the asymptotic laws
\[
h_-(n)\longrightarrow1+\sqrt2,
\qquad \frac{h_+(n)}{n}\longrightarrow\frac1{\gamma c_*},
\]
where \(c_*>0\) is the unique positive solution of
\[
 e^{c_*}=1+(1+1/\sqrt2)c_*.
\]
Numerically \(c_*\approx0.98877987236\).

## Assumptions and scope
Matrices act on row probability vectors. The permutation \(P_n\) has one entry equal to one in each row and column; cyclic indices are modulo \(n\). A Markov-positive end step means that the complete matrix \(T_n(h)\) is entrywise nonnegative (equivalently, it sends every nonnegative row vector to a nonnegative row vector). The rate on each directed edge is one; any common positive rate rescales the dimensionless step \(h\). For \(h\ge0\), the denominator of \(R(hQ_n)\) is invertible because \(I-\gamma hQ_n\) is a nonsingular \(M\)-matrix. Also \(R(0)=1\), so all rows of \(T_n(h)\) sum to one for every \(h\ge0\). At \(h=0\), \(T_n(0)=I\).

All claims concern the exact end-step map for the stated uniform directed cycle; they are not general dimension bounds for arbitrary Markov generators or statements about internal stages.

## Proof
**1. Cyclic kernel.** Substitute \(x\) for the permutation variable and \(r=\gamma h/(1+\gamma h)\). Because \((\sqrt2-1)/\gamma=\sqrt2\), direct simplification gives the formal power-series identity
\[
R(h(x-1))=(1-r)\frac{1-ar+\sqrt2 rx}{(1-rx)^2}
=(1-r)\sum_{k\ge0}r^k[1+ak-a(k+1)r]x^k.
\]
For \(0<r<1\), this series converges absolutely. Reduce exponents modulo \(n\) using \(P_n^n=I\). The cyclic entry with displacement \(j\) is the sum over \(k=j+\ell n\), \(\ell\ge0\):
\[
(1-r)r^j\left[
\frac{1+aj-a(j+1)r}{1-r^n}
+\frac{an(1-r)r^n}{(1-r^n)^2}\right].
\]
Expanding \((1-ar)(1-r^n)/(1-r)+anr^n\) yields exactly \(H_n(r)\). The claimed closed kernel follows. Its prefactor is strictly positive for \(r>0\), and its bracket is \(H_n(r)+aj(1-r^n)\). Thus the diagonal \(j=0\) is nonnegative exactly when \(H_n(r)\ge0\); if that holds, every off-diagonal bracket is strictly positive. When it fails, the diagonal is negative. This proves the full-matrix reduction without a numerical sign inference.

**2. The short cycles.** For \(n=2,3,4\), strict positivity of \(H_n\) on \([0,1]\) has the following exact Bernstein-basis certificates. Reexpress each degree-\(n\) polynomial on each interval in the Bernstein basis of degree \(n\). Every Bernstein coefficient is at least the positive quantity shown:
\[
\begin{array}{c|c|c}
n&[0,\tfrac12]&[\tfrac12,1]\\\hline
2&1-\frac{\sqrt2}{4}&\frac54-\frac{\sqrt2}{4}\\
3&1-\frac{5\sqrt2}{12}&\frac54-\frac{\sqrt2}{2}\\
4&\frac{19-11\sqrt2}{16}&\frac{44-27\sqrt2}{32}
\end{array}
\]
Every displayed lower bound is strictly positive; a Bernstein polynomial with positive coefficients is positive throughout its interval. The accompanying exact checker reconstructs all \(3+3+4+4+5+5=24\) coefficients, verifying these precise minima rather than relying on sampling. Hence short-cycle nonnegativity holds for all finite \(h\ge0\).

**3. Exactly two thresholds for every larger cycle.** The coefficient sequence of \(H_n\) in ascending degree is \((1,-\sqrt2,\ldots,-\sqrt2,a(n-1))\), with exactly two sign changes. Descartes' rule of signs therefore gives at most two positive roots counted with multiplicity. At the endpoints,
\[
H_n(0)=1,\qquad H_n(1)=n>0.
\]
At \(r_0=3/5\), exact arithmetic yields
\[
H_5(r_0)=\frac{4097-3108\sqrt2}{3125}<0,
\]
since \(2\cdot3108^2-4097^2=2533919>0\). Moreover
\[
H_{n+1}(r_0)-H_n(r_0)=r_0^n[1-an(1-r_0)]<0
\quad(n\ge5).
\]
Thus \(H_n(r_0)<0\) for all \(n\ge5\). The intermediate-value theorem supplies one positive root on each side of \(r_0\), both within \((0,1)\). Descartes' upper bound implies that these are all positive roots and both have multiplicity one. The sign of \(H_n\) is consequently positive before the first and after the second root, negative between them. The strictly increasing bijection \(h\mapsto r\) completes the interval classification and its sharpness.

**4. Asymptotic endpoints.** For every fixed \(0\le r<1\), geometric summation gives
\[
H_n(r)\longrightarrow\frac{1-ar}{1-r}.
\]
Together with the unique-root classification, this gives \(r_-(n)\to1/a\) and \(r_+(n)\to1\), hence \(h_-(n)\to1+\sqrt2\). On the upper transition scale \(r=1-c/n\) with fixed \(c>0\),
\[
\frac1nH_n(1-c/n)\longrightarrow
F(c)=ae^{-c}-\sqrt2\frac{1-e^{-c}}{c}.
\]
The equation \(F(c)=0\) is equivalent to \(e^c=1+(a/\sqrt2)c\). Its right side has slope greater than one at zero; strict convexity of the exponential gives one and only one *positive* crossing \(c_*\). Furthermore \(F(c)>0\) for \(0<c<c_*\) and \(F(c)<0\) for \(c>c_*\). For fixed positive \(c<c_*<C\), the signs of \(H_n(1-c/n)\) and \(H_n(1-C/n)\) eventually differ, and the root between is necessarily the upper root, because \(r_-(n)\to1/a\). Bracketing shows \(n(1-r_+(n))\to c_*\). Substitution into \(h=r/[\gamma(1-r)]\) yields the stated linear growth of \(h_+(n)\).

## Verification
Run `python verification.py` with SymPy installed (see `requirements.txt`). The program symbolically verifies the rational uniformization formula; checks all the short-cycle Bernstein coefficients exactly; verifies the five-cycle negative algebraic witness and the monotone dimension step; and checks the cyclic rational resolvent equation and row sums at multiple exact rational \(r\) and dimensions from two through eleven. Its recorded execution was:

`VERIFY_OK 367 exact symbolic/algebraic assertions; Bernstein certificates, cyclic transfer identities, sharp five-cycle witness`

These finite checks support algebraic identities and the finite base cases. The arbitrary-dimension two-root and asymptotic conclusions are established by the preceding proof, not by a bounded numerical search. Numerical root approximations are illustrations only.

## Relationship to prior work
Alexander introduced the classical L-stable two-stage diagonally implicit method; its stability rational function is established background. Bonaventura and Della Rocca (2015, arXiv:1510.04303v1), Sections 3 and 6.2, directly analyze the same L-stable TR-BDF2 scalar stability function, prove a problem-class absolute-monotonicity step restriction, and experimentally study a **periodic upwind semi-discretization** (100 spatial grid points), which is precisely the type of uniform directed-cycle generator examined here. Those are material overlaps and are not claimed as new. Their complete inspected paper does not state or prove the exact all-cycle positivity iff-polynomial condition, the five-state cutoff, the disconnected timestep sets, or the large-cycle transition asymptotics. Their method-wide sufficient SSP bound neither establishes nor rules out large-step recovery for this particular spatial discretization.

Horváth's 1998 and 2005 positivity analyses likewise give the broad absolute-monotonicity and Runge–Kutta threshold framework. Their accessible metadata/abstracts do not establish the specific reentrant cyclic positivity classification; their complete texts were not inspected. Related results for the square of implicit midpoint, Crank–Nicolson resolvents, and diagonal fourth-order Padé end steps involve mathematically different rational functions and cannot imply the polynomial classification here merely by a choice of state dimension. These comparisons do not amount to a proof of global bibliographic uniqueness.

## Limitations
The classification is limited to **uniform one-way** cycles and the *endpoint matrix* of one specified L-stable rational method. It does not claim that five states are minimal over all continuous-time Markov generators, that internal stages preserve nonnegative states, that every nonlinear reaction–transport problem exhibits this phenomenon, or that positivity of the rational map guarantees solution accuracy. The asymptotic endpoint is in dimensionless unit-rate time; changing common jump rate rescales it. All exact signs assume exact arithmetic. The strongest bibliographic residual risk is a specialized derivation of the full cyclic transfer kernel or positivity windows in older Runge–Kutta and positive-systems literature that was not accessible in full.

## References
1. R. Alexander, *Diagonally implicit Runge–Kutta methods for stiff O.D.E.'s*, SIAM Journal on Numerical Analysis **14** (1977), 1006–1021. DOI: 10.1137/0714068. Original numerical method; accessible abstract.
2. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303v1 (first public posting 2015-10-14), especially Sections 3 and 6.2. Full preprint inspected. https://arxiv.org/abs/1510.04303
3. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics **28** (1998), 309–326. DOI: 10.1016/S0168-9274(98)00050-6. Abstract/metadata inspected.
4. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356. DOI: 10.1016/j.apnum.2004.08.026. Abstract/metadata inspected.
