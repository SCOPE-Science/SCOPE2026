# A sharp adjacent-mass-one bound for discrete increasing-failure-rate tails

## Finding
Let \(X\) be an integer-valued random variable with \(\mathbb E|X|<\infty\), and suppose its survival sequence \(S_j=\Pr(X\ge j)\) is log-concave in \(j\in\mathbb Z\). For any integer \(m\) with \(\mathbb E X\ge m\) and
\[
0<\Pr(X=m)\le\Pr(X=m+1),
\]
we have the **sharp** inequality
\[
\Pr(X\ge m+1)\ge a^2=0.324717957244746\ldots,
\]
where \(a\in(1/2,1)\) is the unique root of \(a^3=(1-a)^2\), numerically \(a=0.569840290998053\ldots\).

Equality holds precisely for translations by \(m\) of the distribution
\[
\begin{aligned}
\Pr(X-m=-1)&=1-a,\\
\Pr(X-m=0)&=a(1-a),\\
\Pr(X-m=j)&=a^2(1-b)b^{j-1},\quad j\ge1,
\end{aligned}
\qquad b=2-1/a\in(0,a).
\]
It has mean exactly \(m\) and equal masses at \(m\) and \(m+1\). Thus the sharp extremizer has a two-rate, geometric-right-tail structure, rather than the three-point symmetric form attaining the weaker adjacent-ratio bounds. In particular, extending the three-point candidate \(\gamma/(1+2\gamma)\) to \(\gamma=1\) would incorrectly predict \(1/3\): a five-point IFR law with probabilities \((21,12,12,3,1)/49\) on \(\{-1,0,1,2,3\}\) has mean zero and upper-tail probability \(16/49<1/3\).

## Assumptions and scope
An integer distribution has increasing failure rate (IFR) here if its survival sequence is log-concave: \(S_j^2\ge S_{j-1}S_{j+1}\) for all integers \(j\). This is **not** the stronger requirement that the probability mass function itself be log-concave. For positive consecutive survivals, IFR is equivalent to nonincreasing successive ratios \(S_{j+1}/S_j\). No restriction is imposed on the support, except integrability and the stated positive adjacent masses. The threshold \(m\) need not equal the mean; equality forces it to do so. All probabilities refer to a single law; no asymptotic limit is needed.

## Proof
Translate so \(m=0\). Put \(s=S_1>0\), \(u=S_0>s\), and \(t=u/s=1+p_0/s>1\), where \(p_j=\Pr(X=j)\). Because \(p_1\ge p_0=(t-1)s\), and \(p_1\le s\), we have \(1<t\le2\). Furthermore
\[
\frac{S_2}{S_1}=1-\frac{p_1}{s}\le2-t.
\]
By IFR, for every integer \(j\ge1\), \(S_j\le s(2-t)^{j-1}\), also when the right support terminates (interpret \(0^0=1\)). Thus
\[
\mathbb E(X_+) =\sum_{j\ge1}S_j\le\frac{s}{t-1}.
\tag{1}
\]
For \(k\ge0\), monotonicity of the survival ratios in the other direction gives
\[
S_{-k}\le S_0t^k=st^{k+1},\qquad S_{-k}\le1.
\]
Consequently
\[
\mathbb E((-X)_+)=\sum_{k\ge0}(1-S_{-k})
\ge\sum_{j\ge1}(1-st^j)_+,
\tag{2}
\]
where \(v_+=\max(v,0)\). Combining (1) and (2) gives
\[
\mathbb E X\le F_s(t):=\frac{s}{t-1}-\sum_{j\ge1}(1-st^j)_+.
\tag{3}
\]
For each fixed \(t>1\), the sum has finitely many nonzero terms and \(F_s(t)\) is strictly increasing in \(s>0\).

Write \(s_*=a^2\), \(t_*=1/a=s_*^{-1/2}\), and \(L=-\log s_*\). The cubic equation for \(a\) gives the identity
\[
(1+s_*)(t_*-1)=1.\tag{4}
\]
We prove \(F_{s_*}(t)\le0\) for every \(1<t\le2\), with equality only at \(t=t_*\).

For \(t\in[t_*,2]\), exactly the \(j=1\) term in the sum (3) can be positive (the \(j=2\) term is zero at the left endpoint). Therefore
\[
F_{s_*}(t)=\frac{s_*}{t-1}-1+s_*t,
\quad F'_{s_*}(t)=\frac{s_*t(t-2)}{(t-1)^2}\le0.
\]
Its value at \(t_*\) is zero by (4).

For \(1<t<t_*\), split into intervals where exactly \(d\ge2\) terms of (3) are positive. On such an interval,
\[
F_{s_*}(t)=\frac{s_*}{t-1}-d+s_*\sum_{j=1}^dt^j,
\quad F'_{s_*}(t)=\frac{s_*t^d[d(t-1)-1]}{(t-1)^2}.
\]
The derivative changes from negative to positive at most once, so the maximum on each closed interval is attained at an endpoint. These endpoints are \(t_d=s_*^{-1/d}\) for integers \(d\ge2\), and direct summation there gives
\[
F_{s_*}(t_d)=\frac1{t_d-1}-(d-1+s_*).
\tag{5}
\]
We show (5) is nonpositive. Define for real \(y\ge2\)
\[
g(y)=(y-1+s_*)(e^{L/y}-1).
\]
Set \(c=1-s_*\) and \(v=L/y>0\). Differentiation yields
\[
g'(y)=e^v\bigl(1-e^{-v}-v+(c/L)v^2\bigr).
\]
Here \(1-e^{-v}\ge v-v^2/2\). Moreover \(L\le2c\): indeed \(s_*\in(1/4,1/2)\), and the function \(2(1-z)+\log z\) increases on \([1/4,1/2]\), where its value at \(1/4\) is \(3/2-\log4>0\). Thus \(g'(y)\ge0\). By (4), \(g(2)=1\), so \(g(d)\ge1\) for \(d\ge2\), strictly for \(d>2\). Equation (5) is nonpositive; its equality case is \(d=2\). This proves the asserted bound on all intervals and their endpoints.

If \(s<s_*\), strict monotonicity in (3) gives \(\mathbb E X\le F_s(t)<F_{s_*}(t)\le0\), contradicting \(\mathbb E X\ge0\). Therefore \(s\ge s_*\).

For equality, necessarily \(s=s_*\), \(t=t_*\), and both (1) and (2) are equalities. In (2) this forces \(S_{-1}=1\), and hence \(S_j=1\) for all \(j\le-1\). In (1) equality forces \(p_1=p_0\) and \(S_j=s_*b^{j-1}\) for every \(j\ge1\), with \(b=2-t_*\). These are precisely the stated masses. Conversely, their survival ratios are \(a,a,b,b,\ldots\), which are nonincreasing since \(0<b<a\), and their mean equals zero since \(a^3=(1-a)^2\). This proves both sharpness and uniqueness.

For the finite witness, the sequence of survivals at \(-1,0,1,2,3,4\) is \(1,4/7,16/49,4/49,1/49,0\); its successive ratios are \(4/7,4/7,1/4,1/4,0\). Hence the law is IFR, its mean is \(0\), its adjacent masses are equal, and its upper tail is \(16/49<1/3\).

## Verification
The standalone, dependency-free script `verification/check.py` checks the cubic equation, the equality-case normalization and mean, the derivative/endpoint inequalities on representative grids, and the exact-rational five-point witness. It passes more than 7,000 finite checks using standard Python. This does not establish the universal theorem: its proof is the analytic argument above, particularly the IFR survival-ratio bounds and the real-parameter monotonicity of \(g\).

## Relationship to prior work
Ai, Karagiannis, Kuželka and Pelekis (2026), Theorem 2, establish \(\Pr(X\ge m+1)\ge\gamma/(1+2\gamma)\) under \(p_{m+1}\ge\gamma p_m>0\) only for \(0<\gamma\le1/2\). Their method yields a general \(1/4\) bound in one of its cases; taking \(\gamma=1/2\) gives \(1/4\) under our stronger premise. The present exact constant at ratio one is not a special case of that stated theorem, and the explicit five-point witness explains why simply substituting \(\gamma=1\) into the three-point candidate is invalid.

Alqasem, Aravinda, Marsiglietti and Melbourne (2024) and Marsiglietti and Melbourne (2020/2024) study stronger log-concavity of the probability mass function. Our extremal mass sequence is not log-concave (the ratio from the mass at \(-1\) to that at \(0\) is \(a\), while the next mass ratio is \(1\)). Thus their probability-mass log-concave localization theorems do not directly cover the IFR extremal class. Classical bounds for increasing hazard rates motivate the comparison, but no matching exact adjacent-mass-one constant was identified in the material inspected.

## Limitations
Only the condition \(p_{m+1}\ge p_m>0\) is classified sharply here; this does not claim a complete optimal curve for arbitrary adjacent-mass ratios. The result assumes integrability and log-concavity of the *survival sequence* on the integers, not arbitrary distributions or continuous laws. The scientific literature check does not rule out an equivalent result in an inaccessible historical reliability report or an unindexed source. No independent audit has been performed.

## References
1. J. Ai, V. Karagiannis, O. Kuželka, C. Pelekis, *On the probability that a discrete IFR random variable exceeds its mean*, arXiv:2610.24726v1 (first posted 17 October 2026), Theorem 2 and Sections 2–4. https://arxiv.org/abs/2610.24726
2. A. Alqasem, H. Aravinda, A. Marsiglietti, J. Melbourne, *On a Conjecture of Feige for Discrete Log-Concave Distributions*, arXiv:2208.12702, SIAM J. Discrete Math. 38 (2024), 93–102. https://arxiv.org/abs/2208.12702
3. A. Marsiglietti, J. Melbourne, *Geometric and Functional Inequalities for Log-Concave Probability Sequences*, arXiv:2004.12005, Discrete Comput. Geom. 71 (2024), 556–586. https://arxiv.org/abs/2004.12005
4. G. P. Shah, *Bounds for Lattice Distributions Having Monotone Hazard Rate with Applications*, Berkeley Operations Research Center Report ORC 65-12 (1965), as cited by [1]. Full text not inspected.
