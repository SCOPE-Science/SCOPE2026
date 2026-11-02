# A sharp interior-to-boundary optimizer transition for two-point compound-Poisson concentration

## Finding
Let \(X=\sum_{j=1}^N J_j-\lambda\mathbb EJ\), with independent \(N\sim\operatorname{Poisson}(\lambda)\), \(\lambda>0\), and \(\Pr(J=1)=1-p\), \(\Pr(J=5)=p\), \(0<p\le1\). Fix \(V=\operatorname{Var}(X)=\lambda(1+24p)\). The optimal right sub-gamma scale \(c_*(p)\) is the least \(c\ge0\) for which \(\log\mathbb Ee^{tX}\le Vt^2/(2(1-ct))\) for all \(0\le t<1/c\).

Define
\[
p_4=\frac{1927+575\sqrt{11}}{174752}\approx0.0219400021428,
\qquad p_c=\frac{17}{592}+\frac{25\sqrt{21}}{4144}\approx0.0563620637968.
\]
For every \(p_4\le p<p_c\), the exact scale is \(c_*(p)=\Psi_p(t_*(p))\), where \(t_*(p)>0\) is the **unique** maximizer of \(\Psi_p\) on positive arguments, and \(\Psi_p\) rises strictly before and falls strictly after \(t_*(p)\). For every \(p_c\le p\le1\), \(\Psi_p\) is strictly decreasing, and
\[
c_*(p)=m_p=\frac{1+124p}{3(1+24p)}.
\]
For \(p_4\le p<p_c\), \(c_*(p)>m_p\). The optimizer undergoes an explicit continuous transition:
\[
t_*(p)\sim\frac{\kappa}{-b_3(p_c)}(p_c-p),\qquad
c_*(p)-m_p\sim\frac{\kappa^2}{-2b_3(p_c)}(p_c-p)^2
\quad(p\uparrow p_c),
\]
where \(\kappa=-b_2'(p_c)>0\), with \(b_2,b_3\) as defined in the proof. Numerically the multipliers are \(11.751349368\ldots\) and \(27.024996394\ldots\).

## Assumptions and scope
The Poisson intensity is arbitrary positive, the jump values are exactly \(1,5\), and the mixing probability satisfies \(p_4\le p\le1\). The probability \(p_4\) is an explicit sufficient lower boundary of the proven phase classification, **not** asserted sharp. No claim is made for \(0<p<p_4\). The MGF is entire and all moments exist.

## Proof
Chen's canonical remainder representation (Theorem 3.1 and Proposition 6.1 of the first reference) gives
\[
M_p(t)=\sum_{n=0}^\infty a_n(p)t^n,
\quad a_n(p)=\frac{2[1+(5^{n+2}-1)p]}{(1+24p)(n+2)!},\quad
\Psi_p(t)=\frac{1-M_p(t)^{-1}}{t},\quad c_*(p)=\sup_{t>0}\Psi_p(t).
\]
In particular \(a_0=1\), \(a_1=m_p\), and the series converges for every real \(t\). Differentiate to obtain
\[
\Psi_p'(t)=\frac{H_p(t)}{t^2M_p(t)^2},\qquad
H_p(t)=tM_p'(t)-M_p(t)(M_p(t)-1)=\sum_{n\ge2}b_n(p)t^n,
\]
\[
b_n=(n-1)a_n-\sum_{i=1}^{n-1}a_i a_{n-i}.
\]
Direct exact arithmetic yields
\[
\begin{aligned}
b_2(p)&=-\frac{16576p^2-952p+1}{36(1+24p)^2},\\
b_3(p)&=-\frac{80976p^2-2852p+1}{45(1+24p)^2},\\
b_4(p)&=-\frac{2796032p^2-61664p+7}{720(1+24p)^2}.
\end{aligned}
\]
The larger roots of the numerator quadratics for \(b_4\) and \(b_2\) are respectively \(p_4\) and \(p_c\). The smaller root of the \(b_2\) numerator is below \(1/50<p_4\). Hence \(b_4(p)\le0\) for \(p\ge p_4\); \(b_2(p)>0\) for \(p_4\le p<p_c\) and \(b_2(p)\le0\) for \(p\ge p_c\). For \(p\ge p_c>1/20\), the numerator of \(-b_3\) is positive and increasing, giving \(b_3<0\).

It remains to establish \(b_n<0\) for **all** \(n\ge5\) uniformly over \(p\ge p_4\). Since every jump is at most five, for any integer \(i\) with \(1\le i\le n\),
\[
\frac{a_{n-i}}{a_n}=\frac{(n+2)!}{(n-i+2)!}\frac{\mathbb EJ^{n-i+2}}{\mathbb EJ^{n+2}}
\ge\frac{(n+2)!}{5^i(n-i+2)!}.
\]
For \(n\ge5\), the four convolution terms indexed by \(i=1,2,n-2,n-1\) are distinct; therefore
\[
\sum_{i=1}^{n-1}\frac{a_i a_{n-i}}{a_n}
\ge\frac{2a_1(n+2)}{5}+\frac{2a_2(n+2)(n+1)}{25}.
\]
Both \(a_1(p)\) and \(a_2(p)\) strictly increase with \(p\), and \(p\ge p_4>1/50\). At \(p=1/50\) they equal \(29/37\) and \(337/444\), so the right side minus \(n-1\) is at least
\[
\frac{337n^2-2799n+9704}{5550}>0\qquad(n\ge5),
\]
where positivity follows from its value \(689/925\) at \(n=5\) and positive first difference \((337n-1231)/2775\) thereafter. Hence \(b_n<0\) for all \(n\ge5\).

If \(p\ge p_c\), every coefficient of \(H_p\) is nonpositive, with \(b_3<0\); therefore \(\Psi_p'(t)<0\) for all \(t>0\). Its supremum is \(\lim_{t\downarrow0}\Psi_p(t)=a_1=m_p\). If \(p_4\le p<p_c\), then \(b_2>0\) and all \(b_n\le0\) for \(n\ge4\), with \(b_5<0\). The function
\[
\frac{H_p(t)}{t^3}=\frac{b_2(p)}{t}+b_3(p)+\sum_{n\ge4}b_n(p)t^{n-3}
\]
is strictly decreasing from \(+\infty\) to \(-\infty\) on positive \(t\). Thus it has exactly one zero, proving strict rise and fall and a unique positive global maximizer. Positivity of the initial derivative gives \(c_*(p)>m_p\).

For the transition, \(b_2(p)=\kappa(p_c-p)+O((p_c-p)^2)\), with \(\kappa=-b_2'(p_c)>0\), while \(b_3(p_c)<0\). The single positive root tends to zero: for \(p\) close to \(p_c\), \(b_3(p)\) is uniformly negative and all terms from degree four onward are nonpositive, forcing \(t_*\le b_2/(-b_3)\). Divide \(H_p(t_*)=0\) by \(t_*^2\) and use the analytic expansion to obtain \(t_*\sim\kappa(p_c-p)/[-b_3(p_c)]\). Finally \(\Psi_p'(t)=b_2(p)+b_3(p)t+O(t^2)\), uniformly near the critical point, so integrating from zero to \(t_*\) yields the asserted quadratic scale excess. All limits are for fixed jump support and \(\lambda>0\).

## Verification
`verify.py` recomputes all polynomial coefficients exactly with rational arithmetic, proves the required coefficient signs using exact formulas, validates the separation of the algebraic thresholds, and checks representative numerical optimizers. The infinite-family coefficient bound and uniqueness are analytic arguments above; finite numerical checks alone would not establish them.

## Relationship to prior work
Chen (2026) proves the general canonical variational formula and gives the particular two-point jump example \(p=1/40\), noting that the calculation gives existence but not uniqueness of its interior maximizer. Previously established analysis also gives uniqueness at that specific parameter and a distinct very-small-weight coexistence phenomenon. The present result instead proves a **uniform, complete global optimizer classification on the connected parameter interval** \([p_4,1]\), identifies its exact internal critical point, and gives a sharp critical scaling law. The algebraic two-point class is fixed by the motivating example; the source's general formula alone does not imply any of the global sign classifications.

## Limitations
No assertion of optimality for the lower cutoff \(p_4\), no classification for \(p<p_4\), and no result for different jump support, non-Poisson counts, or a variance proxy different from the true variance. This is a self-review; no independent verification has occurred. Historical-priority risk persists for general exponential-series variation-diminishing theorems that may imply this specialization.

## References
Chen, Y. (2026), *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first publicly submitted 2026-09-02), especially Theorems 3.1, 4.2 and Section 7.2. https://arxiv.org/html/2610.00032v1

Klar, B., and Müller, A. (2003), *On the M-class of life distributions*, as cited in Chen's bibliography (MGF-order context; no result from this paper is assumed in the new coefficient-sign argument).
