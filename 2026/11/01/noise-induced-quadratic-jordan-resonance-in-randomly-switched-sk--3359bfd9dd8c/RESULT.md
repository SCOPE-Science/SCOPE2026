# Noise-induced quadratic Jordan resonance in randomly switched skew tent maps

## Finding
For any probability law \(\eta\) on \((0,1)\), let independent parameters \(A_0,A_1,\ldots\sim\eta\) select full-branch skew tent maps
\[
T_a(x)=\begin{cases}x/a,&0\le x\le a,\\(1-x)/(1-a),&a<x\le1.\end{cases}
\]
Start \(X_0\) uniformly on \([0,1]\) and set \(X_{j+1}=T_{A_j}(X_j)\). This is a stationary annealed process. Define \(m=\mathbb E_\eta A\), \(q=\mathbb E_\eta[A(1-A)]\), \(r=2m-1\), \(s=1-3q\), and \(h(x)=x^2-1/3\). For each integer \(n\ge0\), its autocovariance is exactly
\[
C_n:=\mathbb E[h(X_0)h(X_n)]
=\frac{r^n}{12}+\frac{s^n}{180}
-\frac q{12}\sum_{j=0}^{n-1}r^{n-1-j}s^j.
\]
The empty sum is zero. Thus for \(r\ne s\) the sum is \((r^n-s^n)/(r-s)\).

The annealed transfer operator on the centered polynomial space of degrees at most two is non-diagonalizable **if and only if**
\[
3\mathbb E_\eta[A^2]-5m+2=0,
\quad\text{equivalently}\quad q=\frac{2(1-m)}3.
\]
This resonance forces \(2/3\le m<1\), with \(m=2/3\) only for the deterministic parameter \(A=2/3\). Set \(\lambda=2m-1\), so \(1/3\le\lambda<1\). On the resonance locus,
\[
C_n=\frac4{45}\lambda^n-\frac{1-m}{18}\,n\lambda^{n-1},
\qquad
\operatorname{Corr}(X_0^2,X_n^2)
=\lambda^n\left(1-\frac{5(1-m)n}{8\lambda}\right).
\]
Consequently, every resonant law has eventually strictly negative square-coordinate correlations with exact polynomial-times-exponential decay. The coincident positive polynomial eigenvalue is strictly larger than each diagonal eigenvalue on polynomial degrees \(k\ge3\), so this collision is isolated from all higher polynomial degrees; no assertion about the complete spectrum on an infinite-dimensional function space is made.

A fully random example uses \(A=1/2\) with probability \(1/4\) and \(A=5/6\) with probability \(3/4\). Both individual centered quadratic transfer restrictions are diagonalizable, but their mixture has a size-two Jordan block at \(\lambda=1/2\). In this case
\[
\boxed{\operatorname{Corr}(X_0^2,X_n^2)=2^{-n}(1-5n/16),\quad n\ge0.}
\]
The correlation is positive at lags \(0,1,2,3\), negative at every lag \(n\ge4\), and tends to zero from below at rate \(n2^{-n}\).

## Assumptions and scope
The switching parameters are independent and identically distributed, independent of the uniform initial coordinate, and almost surely strictly between zero and one. All expectations are annealed over both initial coordinate and switching. Each branch covers the full unit interval and has inverse slope magnitude smaller than one. This theorem concerns finite-dimensional polynomial transfer restrictions, explicit scalar observables, and no general assertion of isolated Ruelle resonances on \(BV\) or another function space.

## Proof
Each \(T_a\) preserves Lebesgue measure, since its inverse branches are \(ax\) and \(1-(1-a)x\), whose absolute derivatives sum to \(a+(1-a)=1\). Thus the uniform law is stationary, and the annealed Perron--Frobenius operator acts as
\[
(Pf)(x)=\mathbb E_\eta\bigl[A f(Ax)+(1-A)f(1-(1-A)x)\bigr].
\]
For \(u(x)=x-1/2\) and \(v(x)=x^2-x+1/6\), direct polynomial expansion for each \(a\in(0,1)\) gives
\[
P_a u=(2a-1)u,\qquad
P_a v=(1-3a(1-a))v-a(1-a)u.
\]
Therefore \(Pu=ru\) and \(Pv=sv-qu\). Since \(h=u+v\), induction in the invariant space \(\operatorname{span}\{u,v\}\) yields
\[
P^nh=r^n u+s^n v-q\sum_{j=0}^{n-1}r^{n-1-j}s^j u.
\]
Lebesgue integration gives \(\int_0^1u^2dx=1/12\), \(\int_0^1v^2dx=1/180\), and \(\int_0^1uv\,dx=0\). Using transfer duality \(C_n=\int_0^1 h(P^nh)dx\) proves the covariance formula for all \(n\ge0\), including the endpoints and degeneracy case.

The restricted operator has matrix \(\begin{pmatrix}r&-q\\0&s\end{pmatrix}\) in the basis \((u,v)\). Because \(q>0\), a nontrivial Jordan block occurs precisely for \(r=s\), which is the stated moment equation. Since \(q\le m(1-m)\) by Jensen, resonance implies \(m\ge2/3\). Equality holds only when \(A\) is constant; support in \((0,1)\) implies \(m<1\). At resonance the geometric sum becomes \(n\lambda^{n-1}\); substitution and division by \(\operatorname{Var}(X^2)=4/45\) yield the two displayed formulas. The negative term dominates for \(n>8\lambda/[5(1-m)]\).

For every polynomial degree \(k\ge3\), the highest-degree coefficient under \(P\) is \(d_k=\mathbb E[A^{k+1}+(-1)^k(1-A)^{k+1}]\). Pointwise \(a^{k+1}+(-1)^k(1-a)^{k+1}<a^3+(1-a)^3\) for \(0<a<1\) and \(k\ge3\). Hence \(d_k<s=\lambda\) on resonance; no higher-degree polynomial diagonal coefficient shares \(\lambda\). For the two-atom example, \((m,q,r,s)=(3/4,1/6,1/2,1/2)\). The individual parameters are not \(2/3\), hence their degree-one and degree-two eigenvalues differ, while their averaged restriction is defective. The explicit correlation and sign classification follow exactly.

## Verification
`CHECK.py` independently splits the initial interval into every affine branch cylinder for each tested random switching sequence, integrates the polynomial product using exact rational arithmetic, and compares it with the transfer-operator formula. It checks twenty-three finite-lag integral identities across a resonant two-map mixture, the resonant deterministic boundary, and a nonresonant control law; it also checks twenty-five explicit-lag specializations and exact sign inequalities. Run with `python CHECK.py` using Python's standard library only. This finite test corroborates the algebra but does not replace the general proof above.

## Relationship to prior work
Kalle and Maggioni (2018) construct invariant densities for random piecewise-linear interval systems, including random tent-map examples. Their invariant-density results motivate the annealed setting but do not provide this moment-collision locus or the square-observable correlation law. Driebe (1997) and Butterley--Kiamari--Liverani (2020/2022) demonstrate nonsemisimple transfer dynamics in other deterministic expanding Markov maps; consequently Jordan blocks and polynomial-times-exponential decay are **not** claimed as new phenomena in themselves. The new assertion is the exact locus, coefficient, universal eventual sign reversal, and noise-induced defect from two diagonalizable skew tent components. Older tent-map spectral work (Subbiah--Driebe 1998) treats height variations and band-splitting rather than this i.i.d. random full-height parameter mixture. Closest indexed records were compared by implication, not only by titles.

## Limitations
The formulas concern annealed time correlations, not correlations conditional on a fixed switching realization. The strict sign pattern \(n\ge4\) pertains only to the displayed two-atom law, whereas every resonant law has its own exact sign threshold. The Jordan statement is for the finite polynomial restriction and is not a claim of spectral isolation on a Banach space. Generic spectral work already establishes similar mechanisms for other maps. Full text of Driebe (1997) and Daems (1996) was not accessible during comparison, so exhaustive priority over all spectral constructions is not claimed. No independent scientific audit has been performed.

## References
1. C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430v1 (publicly posted 2018-05-29), https://arxiv.org/abs/1805.11430.
2. O. Butterley, N. Kiamari and C. Liverani, *Locating Ruelle--Pollicott resonances*, arXiv:2012.13145, section 2.1, https://arxiv.org/pdf/2012.13145.
3. D. J. Driebe, *Jordan blocks in a one-dimensional Markov map*, Computers & Mathematics with Applications 34 (1997), 103--109, https://doi.org/10.1016/S0898-1221(97)00120-X.
4. D. Daems, *Non-diagonalizability of the Frobenius--Perron operator and transition between decay modes of the time autocorrelation function*, Chaos, Solitons & Fractals 7 (1996), 1753--1760, https://doi.org/10.1016/S0960-0779(96)00107-5.
5. S. Subbiah and D. J. Driebe, *Spectral decomposition of the tent map with varying height*, arXiv:chao-dyn/9804022, https://arxiv.org/abs/chao-dyn/9804022.
