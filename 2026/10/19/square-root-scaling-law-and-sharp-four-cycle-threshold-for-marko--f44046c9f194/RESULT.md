# Square-root scaling law and sharp four-cycle threshold for Markov positivity of Padé squaring

## Finding
Let \(P_n\) be the cyclic permutation with \((P_n)_{i,i+1}=1\), indices modulo \(n\), and \(Q_n=P_n-I_n\). For \(h>0\) and every integer \(s\geq0\), set
\[
R(z)=(I+z/2)(I-z/2)^{-1},\qquad
T_{n,s}(h)=\big[R(hQ_n/2^s)\big]^{2^s}.
\]
This is the exact-arithmetic diagonal \([1/1]\) Padé / Crank–Nicolson scaling-and-squaring approximation to the transition matrix of the directed \(n\)-cycle. All its rows sum to one. Write \(s_n(h)\) for the smallest nonnegative integer \(s\) for which \(T_{n,s}(h)\) is entrywise nonnegative.

The complete small-cycle distinction is sharp:

* For \(n=2\), \(s_2(h)=0\) for all \(h>0\).
* For \(n=3\), \(s_3(h)=0\) precisely for \(0<h\leq 1+\sqrt5\), and \(s_3(h)=1\) otherwise. Indeed, **every positive number of dyadic squarings** gives a strictly positive matrix.
* For every fixed \(n\geq4\) and every fixed \(s\geq0\), the matrix \(T_{n,s}(h)\) has a negative entry for all sufficiently large \(h\). Nonetheless, for every finite \(h>0\), some finite squaring count makes it strictly positive. The required minimum satisfies
\[
\boxed{\displaystyle s_n(h)=\tfrac12\log_2 h+O_n(1)\quad(h\to\infty).}
\]
Thus four states are the first directed-cycle size for which **no fixed squaring budget** preserves Markov positivity at all step sizes.

The four-state frontier has an exact critical scaling. Suppose \(h\to\infty\), \(s\geq1\), \(m=2^s\to\infty\), and \(q=2m^2/h\to q_0\in(0,\infty)\). The first row of \(T_{4,s}(h)\) converges, entry by entry, to
\[
\frac14\big(1+e^{-q_0}+2e^{-q_0}\cos q_0,\ 
1-e^{-q_0}-2e^{-q_0}\sin q_0,\ 
1+e^{-q_0}-2e^{-q_0}\cos q_0,\ 
1-e^{-q_0}+2e^{-q_0}\sin q_0\big).
\]
It is entrywise nonnegative if and only if \(q_0\geq q_*\), where \(q_*\in(0,\pi)\) is the **unique positive solution** of
\[
\boxed{\displaystyle e^{q_*}=1+2\sin q_*,\qquad q_*=0.9777603734668504\ldots.}
\]
For \(0<q_0<q_*\) its one-step-forward transition entry is negative; for \(q_0>q_*\) all entries are strictly positive. The boundary limit has exactly one zero. This is an asymptotic threshold, not a claim of an identical finite-step criterion for every \(h\).

As a finite rational witness, for \(n=4\), \(h=50\) and one squaring (\(s=1\)), the exact first row is
\[
\frac1{309830404}(273799579,-9599175,13114375,32515625).
\]
The row sum is exactly one but an entry is strictly negative.

## Assumptions and scope
The statements concern real finite-dimensional continuous-time Markov chains with **unit-rate deterministic cyclic jumps** \(Q_n=P_n-I_n\), exact rational matrix arithmetic, the \([1/1]\) diagonal Padé map, and the specified order of scaling and squaring. The logarithm is base two. The asymptotic notation \(O_n(1)\) means bounded in magnitude by a constant depending on fixed \(n\), uniformly as \(h\to\infty\); no rate uniform in \(n\) is claimed. Positivity means entrywise nonnegativity, not positive definiteness. A strictly positive stochastic matrix has every entry greater than zero.

The exact transition matrix \(e^{hQ_n}\) is strictly positive for every \(h>0\), since the Poisson jump count assigns positive mass to every residue class modulo \(n\). Thus a negative computed entry is a genuine qualitative approximation error, not a property of the exact semigroup.

## Proof
**Resolvent and row sums.** Put \(m=2^s\), \(a=h/(2m)\), and \(A_a=(I+a(I-P_n))^{-1}\). The Padé factor is \(R(hQ_n/m)=2A_a-I\). Because \(a>0\),
\[
A_a=\frac1{1+a}\sum_{j=0}^{\infty}\left(\frac{a}{1+a}\right)^jP_n^j
\]
is strictly positive and row-stochastic. The factor \(2A_a-I\) and every power of it have row sums exactly one. Moreover \((A_a)_{ii}\geq (1+a)^{-1}\), so \(2A_a-I\) is strictly positive whenever \(a<1\). This proves that every finite step admits a positivity-restoring finite scaling count.

**Two and three states.** For \(n=2\), the factor is the positive stochastic matrix with diagonal \((1+2a)^{-1}\) and off-diagonal \(2a/(1+2a)\). For \(n=3\), the factor has positive off-diagonal entries and diagonal
\[
\frac{1+a-a^2}{1+3a+3a^2}.
\]
It is therefore nonnegative exactly when \(a\leq(1+\sqrt5)/2\). For one squaring, direct exact multiplication gives first row
\[
\frac1{(3a^2+3a+1)^2}
\big(9a^4+6a^3-a^2+2a+1,\ 4a(2a+1),\ 4a^2(3a+2)\big).
\]
All three numerators are strictly positive for \(a>0\); in the diagonal, \(6a^3-a^2+2a=a(6a^2-a+2)>0\). Every dyadic power \(m\geq2\) is a power of the strictly positive factor \([R(hQ_3/m)]^2\), proving the complete three-state classification.

**Why dimension four changes the large-step sign.** For fixed \(n\), define the uniform projection \(\Pi=n^{-1}\mathbf1\mathbf1^{\mathsf T}\) and
\[
K=\sum_{j=0}^{n-1}\frac{n-1-2j}{2n}P_n^j.
\]
The coefficients sum to zero, and direct coefficient comparison gives \((I-P_n)K=I-\Pi\) and \(K\Pi=0\). Fourier diagonalization of the cyclic permutation then proves
\[
A_a=\Pi+a^{-1}K+O_n(a^{-2})\quad(a\to\infty).
\]
For \(s=0\), \(T_{n,0}(h)\to2\Pi-I\). If \(n\geq3\), its diagonal tends to \(2/n-1<0\).

For any fixed \(s\geq1\), \(m=2^s\) is even and \(2\Pi-I\) acts as minus the identity on the zero-sum subspace, giving
\[
T_{n,s}(h)=I-\frac{2m}{a}K+O_{n,m}(a^{-2}).
\]
The coefficient of \(P_n\) in \(K\) is \((n-3)/(2n)\). Consequently the one-step-forward transition coefficient obeys
\[
[T_{n,s}(h)]_{i,i+1}
=-\frac{n-3}{n}\frac{m}{a}+O_{n,m}(a^{-2})
=-\frac{2(n-3)m^2}{nh}+O_{n,s}(h^{-2}).
\]
It is eventually negative for every \(n\geq4\) and every fixed \(s\geq1\). This also shows exactly why the three-cycle is exceptional: its corresponding first-order coefficient vanishes.

**Sharp logarithmic squaring exponent.** Let \(\lambda\ne1\) be an \(n\)-th root of unity. The nonconstant Fourier eigenvalue of the Padé factor is
\[
\rho_\lambda(a)=\frac{1+a(\lambda-1)}{1-a(\lambda-1)}
=-1+\frac2{1+a(1-\lambda)}.
\]
For large \(a\), the branch of \(\log(-\rho_\lambda(a))\) near zero satisfies
\[
\log(-\rho_\lambda(a))
=-\frac2{a(1-\lambda)}+O_n(a^{-2}).
\]
With \(q=m/a=2m^2/h\), for every even \(m\) and uniformly when \(a\to\infty\), \(q\to0\), Fourier inversion yields
\[
T_{n,s}(h)=I-2qK+O_n(q^2+q/a),
\qquad [T_{n,s}(h)]_{i,i+1}=-\frac{n-3}{n}q+O_n(q^2+q/a).
\]
Choose a small fixed \(q_0>0\). For all large \(h\), **all** dyadic \(m\geq2\) with \(2m^2/h\leq q_0\) give a negative forward-transition entry when \(n\geq4\). The unsquared case was already excluded for large \(h\). Therefore \(s_n(h)\geq\tfrac12\log_2 h-O_n(1)\).

Conversely, take \(m\) to be the smallest dyadic integer at least \(C\sqrt h\), with \(C>0\) fixed. Then \(q=2m^2/h\) stays in \([2C^2,8C^2)\), and \(a=h/(2m)\to\infty\). The same Fourier expansion gives the limit multiplier \(\exp[-2q/(1-\lambda)]\) on each nonconstant mode. Because
\[
\operatorname{Re}\frac1{1-\lambda}=\frac12
\]
for every nontrivial root of unity, the modulus of each limit multiplier is \(e^{-q}\). Choose \(C\) so that \(e^{-2C^2}<1/(2n)\). The resulting exact finite-step matrices are, for all sufficiently large \(h\), within spectral norm less than \(1/n\) of \(\Pi\), hence strictly positive entrywise. Thus \(s_n(h)\leq\tfrac12\log_2 h+O_n(1)\). Combining bounds proves the sharp exponent.

**Four-cycle critical constant.** Let \(n=4\), \(\lambda\in\{i,-1,-i\}\). If \(h\to\infty\), \(m\to\infty\), and \(q=m/a\to q_0>0\), then the three nontrivial Fourier multipliers of \(T_{4,s}(h)\) tend respectively to \(e^{-q_0(1+i)}\), \(e^{-q_0}\), and \(e^{-q_0(1-i)}\). Fourier inversion gives the four displayed limiting first-row entries. The first, third and fourth entries are strictly positive for every \(q_0>0\): after multiplication by \(4e^{q_0}\), their numerators are respectively \(e^{q_0}+1+2\cos q_0\), \(e^{q_0}+1-2\cos q_0\), and \(e^{q_0}-1+2\sin q_0\). For \(0<q_0\leq\pi/2\), the first is manifestly positive, and for larger \(q_0\) it exceeds \(e^{\pi/2}-1>0\); the third is at least \(e^{q_0}-1>0\); the fourth is positive up to \(\pi\) and thereafter exceeds \(e^\pi-3>0\).

The remaining entry has the sign of \(g(q)=e^q-1-2\sin q\). On \((0,\pi)\), \(g''(q)=e^q+2\sin q>0\), \(g(0)=0\), \(g'(0)=-1\), and \(g(\pi)>0\). Hence there is one positive root there, with negativity below and positivity above. For \(q\geq\pi\), \(g(q)\geq e^\pi-3>0\). This proves the unique critical constant, its exact sign classification, and the limiting single zero at the boundary.

## Verification
A standalone Python program, `verify_cycle.py`, implements exact rational inversion and powers of the directed-cycle Padé factors. On replay it passed 112 assertions, checking exact row sums over multiple dimensions, step sizes and squaring counts; the rational four-cycle witness; small-cycle positivity examples; fixed-budget negative entries; and numerical Fourier critical-scale comparisons. The numerical root was isolated by bisection. None of these finite checks is used as a proof of the universal or asymptotic statements above, which follow from the displayed algebraic and Fourier arguments.

## Relationship to prior work
Diagonal Padé approximation and scaling-and-squaring for general matrix exponentials are classical. Blanes, Kopylov and Seydaoğlu (2024, arXiv:2404.12789v1) analyze efficient Padé choices, error, and preservation of Lie-group structure, not positivity of scaled-and-squared directed Markov cycles; their full preprint was inspected in the relevant sections. Sherlock (2021) treats matrix exponential algorithms for finite Markov jump processes, recommending a nonnegative uniformization implementation of scaling-and-squaring; the relevant open-access algorithm section does not establish this fixed-Crank–Nicolson cycle threshold. Related positivity-preserving rational-map studies concern unsquared factors or other generators. The new mathematical distinction asserted here is **dimension-sharp failure under every fixed squaring count, the half-logarithmic minimum budget, and the explicit four-cycle critical Fourier constant**, not the Padé method or the general fact that a single Crank–Nicolson factor can have negative entries.

## Limitations
The classification is restricted to unit-rate directed pure cycles and the degree-one diagonal Padé method in exact arithmetic. The logarithmic budget is a qualitative entrywise-positivity guarantee, not an error-tolerance or cost-optimality statement for approximating \(e^{hQ_n}\). The sharp root governs the asymptotic coupled regime \(h,m\to\infty\), not a universal finite-step threshold. No conclusions are asserted for arbitrary finite Markov generators, other Padé degrees, floating-point rounding, or all entries of a general nonnormal matrix function. Priority against unindexed literature is not independently certified.

## References
1. S. Blanes, N. Kopylov and M. Seydaoğlu, *Efficient scaling and squaring method for the matrix exponential*, arXiv:2404.12789v1, first public 19 April 2024. https://arxiv.org/abs/2404.12789
2. C. Sherlock, *Direct statistical inference for finite Markov jump processes via the matrix exponential*, *Computational Statistics* 36 (2021), 2863–2887, DOI:10.1007/s00180-021-01102-6, first published 19 April 2021. https://doi.org/10.1007/s00180-021-01102-6
3. A. Itkin and R. Kazbek, *Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker–Planck equation*, arXiv:2608.22703 (2026). Its abstract discusses large-step sign behavior of **single rational factors**, without resolving the repeated-power directed-cycle limit above. https://arxiv.org/abs/2608.22703
