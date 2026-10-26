# A two-switch dependence window for isolated occupancy boxes

## Finding
Let \(n\ge2\) distinguishable balls be assigned independently and uniformly to \(m\ge2\) labeled boxes. For distinct boxes \(i,j\), let \(I_i\) indicate that box \(i\) contains exactly one ball and let \(C_m(n)=\operatorname{Cov}(I_i,I_j)\).

For every \(m\ge4\), there are exactly two real numbers \(2<\alpha_m<m<\beta_m<\infty\) such that, for integer \(n\ge2\),
\[
C_m(n)>0\quad\Longleftrightarrow\quad \alpha_m<n<\beta_m,
\]
and \(C_m(n)<0\) outside the closed interval. At an integer endpoint equality holds. The continuous thresholds are the two zeros on \(x>1\) of
\[
F_m(x)=\log(1-1/x)-2\log(1-1/m)+(x-2)\log\!\left(1-\frac1{(m-1)^2}\right).
\]
Their sharp asymptotics, as \(m\to\infty\), are
\[
\alpha_m=m-\sqrt{m/2}-1/4+O(m^{-1/2}),\qquad
\beta_m=m+\sqrt{m/2}-1/4+O(m^{-1/2}).
\]
More finely, for each fixed real \(s\), with \(n_m=m+\lfloor s\sqrt m\rfloor\),
\[
\lim_{m\to\infty}m^2C_m(n_m)=e^{-2}(1/2-s^2).
\]
For \(m=2\), covariance is positive only at \(n=2\); for \(m=3\), it is positive exactly at \(n=2,3\). It is negative at all other integer \(n\ge2\) in those cases.

## Assumptions and scope
The number of boxes \(m\) and number of balls \(n\) are finite integers, both at least two; independent allocation probabilities are all exactly \(1/m\). Correlations concern *two fixed distinct* singleton-box indicators, not the total occupancy count or conditioned/Poissonized allocations. Strict signs exclude possible integer solutions of \(F_m(n)=0\) without assuming such solutions do not exist. The asymptotic uses natural logarithms and any fixed \(s\); floor rounding does not change its limit.

## Proof
Write \(b=1-1/m\) and \(a=1-2/m\). The multinomial probabilities of one singleton and of two distinct singleton boxes are respectively
\[
P_1=\frac nm b^{n-1},\qquad P_{11}=\frac{n(n-1)}{m^2}a^{n-2}.
\]
Therefore \(C_m(n)=P_{11}-P_1^2\). For \(m\ge3\) we may divide by \(P_1^2>0\) and obtain
\[
\frac{P_{11}}{P_1^2}=\frac{n-1}{n}\,b^{-2}\,q^{n-2},\qquad
q=\frac{a}{b^2}=1-\frac1{(m-1)^2}.
\]
Thus its logarithm is \(F_m(n)\), and the covariance has the same sign as \(F_m(n)\). For real \(x>1\),
\[
F_m''(x)=-\frac{2x-1}{x^2(x-1)^2}<0.
\]
Also \(F_m(x)\to-\infty\) as \(x\to\infty\), because \(\log q<0\). At \(x=2\), \(\exp F_m(2)=m^2/[2(m-1)^2]<1\) for integers \(m\ge4\). At \(x=m\), put \(k=m-1\). Bernoulli's inequality gives, for \(k\ge2\),
\[
\exp F_m(m)=(1+1/k)(1-1/k^2)^{k-1}
\ge (1+1/k)\left(1-\frac{k-1}{k^2}\right)=1+\frac1{k^3}>1.
\]
Strict concavity (and thus strict decrease of \(F_m'\)) gives a single positive interval between exactly two zeros, located as stated by the intermediate value theorem. The signs outside follow without further hypotheses.

For \(m=2\), when \(n=2\) both boxes are singletons with probability \(1/2\) and \(C_2(2)=1/4\); for \(n>2\) the two singleton events cannot co-occur but each has positive probability, hence \(C_2(n)<0\). For \(m=3\), the ratio at \(n=2\) is \(9/8\), at \(n=3\) is strictly above one by the preceding Bernoulli bound, and at \(n=4\) it is \(243/256<1\). Since \(F_3'(4)=1/12+\log(3/4)<0\) and \(F_3'\) decreases, all later integer values are strictly negative.

For asymptotics, set \(t=m^{-1/2}\) and \(x=m+s\sqrt m\). Taylor expansions of the three logarithms uniformly for bounded \(s\) give
\[
F_m(m+s\sqrt m)=m^{-2}(1/2-s^2)+m^{-5/2}(s^3-s)+O(m^{-3}).
\]
The two roots approach \(s=\pm1/\sqrt2\) on this scale, as follows from strict concavity and the displayed expansion with fixed \(s\) on either side of those two values. To determine the constant terms, insert \(s=s_0+c m^{-1/2}\) with \(s_0=\pm1/\sqrt2\). The coefficient of \(m^{-5/2}\) becomes \(-2s_0c+s_0^3-s_0\), so \(c=(s_0^2-1)/2=-1/4\). Uniform Taylor remainder near the two simple roots yields \(O(m^{-1/2})\) in \(x\). Finally, for \(n=m+\lfloor s\sqrt m\rfloor\), \(P_1\to e^{-1}\), and \(C_m(n)=P_1^2(e^{F_m(n)}-1)\), giving the stated scaled covariance limit.

## Verification
`verify.py` checks the multinomial probability formula against independent exact enumeration of every allocation for \(2\le m\le5\), \(2\le n\le6\); checks the sign-window structure with exact rational arithmetic for \(2\le m\le80\) and \(2\le n\le3m+10\); and checks the displayed second-order asymptotic numerically for several larger box counts. These finite checks support but do not replace the analytic proof, which applies to every finite \(m,n\).

## Relationship to prior work
The classical isolated-ball model and its variance and normal approximation are studied by Penrose (arXiv:0901.3493, first posted January 22, 2009). Barbour and Gnedin (arXiv:0809.4387, first posted September 25, 2008) study occupancy frequency counts and limiting covariance structures for infinite boxes. Their investigated regimes concern count fluctuations and distributional limits, rather than the fixed-pair singleton-indicator covariance's two finite-sample switches and square-root critical window. The exact two-box joint probability itself is an elementary multinomial identity and is **not** claimed as novel; the claimed contribution is the global two-switch classification and precise critical-width asymptotics. These results do not follow merely from the published leading-order normal approximations.

## Limitations
The result requires equal independent box probabilities; unequal frequencies need not have the same sign diagram. The fixed-box covariance is of order \(m^{-2}\) in the critical window, even though summing over box pairs produces an order-one contribution to the singleton-count variance; no full normal or Edgeworth approximation is established here. Only identified relevant sections of the historical literature were examined, and a complete historical priority audit is outstanding. The sign-classification theorem does not assert a closed form for the finite roots.

## References
1. M. D. Penrose, *Normal approximation for isolated balls in an urn allocation model*, arXiv:0901.3493, version 1 posted 2009-01-22, https://arxiv.org/abs/0901.3493.
2. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387, version 1 posted 2008-09-25, https://arxiv.org/abs/0809.4387.
3. V. F. Kolchin, B. A. Sevast'yanov, and V. P. Chistyakov, *Random Allocations*, 1978 (background monograph; full text not examined here).
