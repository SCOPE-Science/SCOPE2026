# Parity-sharp Markov positivity and one-squaring repair for diagonal Padé exponentials

## Finding
For every integer \(n\ge2\), strictly positive probability vector \(\pi\in\mathbb R^n\), rate \(\lambda>0\), step \(h>0\), and Padé degree \(m\ge1\), consider the continuous-time **reset-chain** generator
\[
Q=\lambda(\mathbf1\pi^{\mathsf T}-I),\qquad \pi_i>0,\quad \sum_i\pi_i=1.
\]
Let \(R_m\) be the diagonal \([m/m]\) Padé approximant to the exponential, and let \(T_m(h)=R_m(hQ)\). All rows of \(T_m(h)\) sum to one, and all off-diagonal entries are strictly positive. Writing \(\pi_* =\min_i\pi_i\), \(z=\lambda h\), and \(r_m(z)=R_m(-z)\), the exact entrywise nonnegativity test is
\[
\boxed{T_m(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad
r_m(z)\ge-\frac{\pi_*}{1-\pi_*}.}
\]
For **every positive step size**, the Padé step is entrywise nonnegative if and only if either \(m\) is even or \(n=2\) and \(\pi=(1/2,1/2)^{\mathsf T}\). If \(m\) is odd and \(\pi_*<1/2\), it is nonnegative at sufficiently small positive steps but develops a negative diagonal entry at every sufficiently large step. The sharp signed-mass amplification formula is
\[
\boxed{\|T_m(h)\|_\infty=
1+2\max\!\left\{0,-\pi_*-(1-\pi_*)r_m(z)\right\}.}
\]
In particular, as \(h\to\infty\), this norm tends to \(1\) for even \(m\), whereas for odd \(m\) it tends to \(3-4\pi_*\). For a uniform reset distribution this latter value is \(3-4/n\), approaching \(3\) as \(n\to\infty\).

For **every** \(m,n,\pi,\lambda,h\) as above, a single scaling-and-squaring operation,
\[
\boxed{\bigl[R_m(hQ/2)\bigr]^2,}
\]
is a strictly positive row-stochastic matrix. Therefore the exact minimum number of binary squarings needed for entrywise nonnegativity is zero when the displayed scalar test holds and one otherwise. More generally, every positive number of binary squarings suffices.

For the three-stage Gauss–Legendre/\([3/3]\) case, the nonnegative-step region **is exactly one closed interval**: if \(\pi_*<1/2\), it is \(0\le z\le z_*(\pi_*)\), with a unique positive boundary solving \(R_3(-z)=-\pi_* /(1-\pi_*)\). For the uniform \(n\)-state chain, this boundary is the unique positive zero of
\[
\boxed{120n-60(n-2)z+12nz^2-(n-2)z^3=0.}
\]
It decreases strictly with \(n\ge3\), taking \(z_*(1/3)=34.5654766374196\ldots\) at \(n=3\) and tending to \(4.64437070925217\ldots\) as \(n\to\infty\). These numerical values are illustrative; the cubic and monotonicity characterize the exact boundary.

## Assumptions and scope
All matrix functions and squarings are evaluated in exact arithmetic. The row convention is used: probability row vectors propagate on the right, and \(Q\mathbf1=0\). The chain is irreducible because \(Q_{ij}=\lambda\pi_j>0\) for \(i\ne j\). Its exact exponential is \(e^{hQ}=\Pi+e^{-z}(I-\Pi)\), where \(\Pi=\mathbf1\pi^{\mathsf T}\). A *positive stochastic matrix* here means all entries strictly positive and every row sum one; *nonnegative stochastic* includes zero entries. The approximation is \(R_m(hQ)=P_m(hQ)P_m(-hQ)^{-1}\), where
\[
P_m(w)=\sum_{j=0}^m\frac{(2m-j)!m!}{(2m)!(m-j)!j!}\,w^j.
\]
The Padé denominator is invertible in this domain. An index \(m\) is a Padé polynomial degree, not a graph size; a single scaling-and-squaring operation means applying the approximant at half the step, then squaring it once, rather than squaring a previously computed full-step approximation.

## Proof
**1. Reduction to one scalar.** The idempotent \(\Pi^2=\Pi\) commutes with \(I-\Pi\), so \(Q\) acts by zero on \(\operatorname{range}\Pi\) and by \(-\lambda\) on \(\operatorname{range}(I-\Pi)\). Since \(P_m(0)=1\) and \(P_m(z)>0\) for \(z>0\), rational functional calculus yields
\[
T_m(h)=\Pi+r_m(z)(I-\Pi),\qquad r_m(z)=\frac{P_m(-z)}{P_m(z)}.
\]
Consequently \((T_m)_{ij}=(1-r_m)\pi_j\) when \(i\ne j\), and \((T_m)_{ii}=\pi_i+(1-\pi_i)r_m\). Every row sum is one.

**2. Scalar parity lemma.** All coefficients of \(P_m\) are strictly positive. Separating the even and odd powers gives \(P_m(z)=E_m(z)+O_m(z)\) and \(P_m(-z)=E_m(z)-O_m(z)\), with \(E_m(z),O_m(z)>0\) for \(z>0\). Thus \(-1<r_m(z)<1\). Moreover the *exact gamma-integral identity*
\[
P_m(w)=\frac1{(2m)!}\int_0^\infty e^{-t}t^m(t+w)^m\,dt
\]
follows by expanding \((t+w)^m\) and integrating each monomial. If \(m\) is even, its integrand at \(w=-z\) is nonnegative and not identically zero, so \(P_m(-z)>0\) for all \(z>0\). If \(m\) is odd, then
\[
\frac{d}{dz}P_m(-z)=-\frac{m}{(2m)!}\int_0^\infty e^{-t}t^m(t-z)^{m-1}\,dt<0,
\]
and \(P_m(-z)\) drops from \(1\) to negative infinity; it therefore has exactly one positive zero. Irrespective of this zero, comparison of leading polynomial coefficients gives \(r_m(z)\to(-1)^m\) as \(z\to\infty\).

**3. Exact positivity and mass amplification.** Since \(r_m(z)<1\), off-diagonals are positive and diagonals increase with \(\pi_i\). The smallest is \(d_* =\pi_*+(1-\pi_*)r_m(z)\), yielding the stated scalar criterion. Every row contains at most one negative entry, on the diagonal. Its absolute row sum is \(1+2\max\{0,-(T_m)_{ii}\}\); maximizing over rows proves the norm identity. For even \(m\), \(r_m>0\), so every finite step is positive. For odd \(m\), \(r_m\to-1\) and \(d_*\to2\pi_*-1\). Because \(n\ge2\) and the entries of \(\pi\) are positive, \(\pi_*\le1/2\), with equality only for the balanced two-state chain. If \(\pi_*=1/2\), the strict bound \(r_m>-1\) gives positive diagonals even for odd \(m\); otherwise the large-step diagonal is negative. Continuity near \(r_m(0)=1\) establishes small-step positivity. The norm limits follow by substitution.

**4. One squaring is sufficient and sharp.** Since \(\Pi\) and \(I-\Pi\) are complementary idempotents,
\[
\bigl[R_m(hQ/2^s)\bigr]^{2^s}=\Pi+\bigl[r_m(z/2^s)\bigr]^{2^s}(I-\Pi).
\]
For every integer \(s\ge1\), its scalar multiplier is in \([0,1)\), because \(-1<r_m<1\). Hence all off-diagonal entries are positive, all diagonal entries are positive, and each row sums to one. If an unsquared step violates the scalar inequality, zero squarings fail while one succeeds; otherwise zero are already enough.

**5. A sharp cubic boundary for degree three.** Direct expansion gives
\[
P_3(z)=1+\frac z2+\frac{z^2}{10}+\frac{z^3}{120},\qquad
r_3'(z)=-\frac{z^4-30z^2+600}{600P_3(z)^2}.
\]
The numerator of the negative derivative equals \((z^2-15)^2+375>0\), so \(r_3\) decreases strictly from \(1\) to \(-1\). This yields the claimed unique boundary for every \(\pi_*<1/2\). At uniform weights, clearing the positive denominator of \(r_3(z)=-1/(n-1)\) gives the displayed cubic. Because \(-1/(n-1)\) rises strictly with \(n\ge3\), the root decreases strictly; its limiting equation is \(P_3(-z)=0\), which has a unique positive zero by step 2.

## Verification
The standalone `verify.py` recomputes the Padé coefficients from factorial formulas, checks the integral's coefficient expansion, reconstructs exact rational matrix Padé maps and squarings on balanced, uniform, and unequal-probability reset chains, and validates the cubic coefficient and derivative identities. It completed **681 exact checks** under Python 3 and SymPy. To reproduce, run `python verify.py` with SymPy installed. These finite checks confirm instances and identities; the arbitrary-parameter conclusions rely on the integral and spectral proofs above.

## Relationship to prior work
Blanes, Kopylov and Seydaoğlu (arXiv:2404.12789v1, 19 April 2024), *Efficient scaling and squaring method for the matrix exponential*, provide the rational Padé formula, explain binary scaling and squaring, and emphasize preservation of algebraic matrix-group structure by diagonal approximants. Those statements do not alone ensure cone positivity. Driver and Temme (1999), *Zero and pole distribution of diagonal Padé approximants to the exponential function*, provide the classical polynomial integral representations and zero analysis; the scalar identities and parity consequences are not claimed as new. Horváth (1998, 2005) investigates general Runge–Kutta positivity thresholds. Related published results already describe Crank–Nicolson positivity on reversible chains and a different higher-order Padé positivity obstruction for pure-birth chains. The present result instead specifies the **exact arbitrary-order, arbitrary-stationary-distribution classification on reset chains**, the associated signed-mass norm, and the one-squaring repair. These comparisons do not establish global novelty; corresponding specialized statements may appear in broader positivity theory.

## Limitations
The classification concerns rank-one reset generators, not arbitrary continuous-time Markov generators. In particular, one squaring is **not** asserted to repair all generators. It studies entrywise positivity and row sums in exact arithmetic, not floating-point rounding, approximate inversion, backward error, tolerance selection, or global accuracy. For arbitrary odd \(m\), the exact pointwise scalar criterion is proved, but connectedness or uniqueness of the full positive-step interval is **not** claimed; the unique threshold is separately proved for \(m=3\). The two-state exception, the low-order scalar Padé facts, and general absolute-monotonicity restrictions have established antecedents. Literature-priority uncertainty remains for specialized consequences of older Runge–Kutta positivity theorems.

## References
1. S. Blanes, N. Kopylov, M. Seydaoğlu, *Efficient scaling and squaring method for the matrix exponential*, arXiv:2404.12789v1 (first public 2024-04-19), https://arxiv.org/abs/2404.12789.
2. K. A. Driver, N. M. Temme, *Zero and pole distribution of diagonal Padé approximants to the exponential function*, Quaestiones Mathematicae 22 (1999), 7–17, https://ir.cwi.nl/pub/1229.
3. Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6.
4. Z. Horváth, *On the positivity step size threshold of Runge-Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026.
