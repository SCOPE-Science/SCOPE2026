# Logarithmic three-regime localized entropy for stretched-exponential dilation sequences

## Finding
Fix \(0<\kappa<1\). Let
\[
E_\kappa=\{1\}\cup\{1+e^{-n^\kappa}:n=1,2,\ldots\}\subset[1,2].
\]
Using the scale-resolved Legendre–Assouad entropy from [1], for each fixed real \(b\) and \(\delta\downarrow0\),
\[
\mathfrak N_{E_\kappa}^{\sharp}(b,\delta)\asymp_{\kappa,b}
\begin{cases}
(\log(1/\delta))^{1/\kappa},&b\le0,\\
\delta^{-b}(\log(1/\delta))^{(1-\kappa)(1-b)/\kappa},&0<b<1,\\
\delta^{-b},&b\ge1.
\end{cases}
\]
All three logarithmic exponents are sharp in the sense of two-sided estimates. In the middle region, the logarithmic factor is nonconstant and invisible to the usual power-law Legendre–Assouad exponent. In particular, \(\nu_{E_\kappa}^{\sharp}(b)=\max\{b,0\}\), while \(\mathfrak N_{E_\kappa}^{\sharp}(b,\delta)/\delta^{-b}\to\infty\) whenever \(0<b<1\).

## Assumptions and scope
For a bounded set \(A\subset\mathbb R\), \(N(A,\delta)\) denotes the least number of intervals of length \(\delta\) whose union covers \(A\), allowing closed interval endpoints. For \(R>0\), put \(E_R=R^{-1}(E_\kappa\cap[R,2R))\) and
\[
\mathfrak N_{E_\kappa}^{\sharp}(b,\delta)
=\sup_{R>0}\sup_{\substack{I\subset[1,2]\\\delta<|I|\le1}}
|I|^{-b}N(E_R\cap I,\delta).
\]
The set, outer normalization, and range of interval lengths coincide with equation (1.4) of [1]. The notation \(A\asymp_{\kappa,b}B\) means that their ratio is bounded above and away from zero for sufficiently small positive \(\delta\), with constants that may depend on the fixed parameters. Endpoints \(b=0,1\) belong to the outer regimes as displayed. These are metric-entropy statements, not maximal-operator norm estimates.

## Proof
Write \(u_n=e^{-n^\kappa}\) and \(g_n=u_n-u_{n+1}\). Since \(0<\kappa<1\), the continuous function \(u(t)=e^{-t^\kappa}\) is strictly decreasing and strictly convex for positive \(t\); thus \(g_n\) decreases to zero. Also, elementary differentiation and the mean-value theorem yield
\[
g_n\sim\kappa n^{\kappa-1}e^{-n^\kappa},\qquad g_{n-1}/g_n\longrightarrow1.
\]
For small \(\delta\), let \(m=m(\delta)\) be the smallest positive integer with \(g_m\le\delta\), set \(a=u_m\), and \(H=a/\delta\). The two inequalities \(g_m\le\delta<g_{m-1}\), together with the adjacent-gap ratio limit, imply \(g_m/\delta\to1\). Therefore
\[
H\sim \frac{m^{1-\kappa}}{\kappa},\quad
m\sim(\log(1/\delta))^{1/\kappa},\quad
H\asymp_\kappa(\log(1/\delta))^{(1-\kappa)/\kappa}.
\tag{1}
\]
Indeed \(-\log g_m=m^\kappa+(1-\kappa)\log m-\log\kappa+o(1)\), so \(m^\kappa\sim\log(1/\delta)\).

**Global entropy.** The \(m\) points \(u_1,\ldots,u_m\) have consecutive spacings at least \(\delta\) except possibly the final gap; an interval of length \(\delta\) contains at most two such points. Hence \(N(E_\kappa,\delta)\ge m/2\). Conversely use at most \(m\) intervals for the first \(m\) points and at most \(\lceil a/\delta\rceil+1\) for the tail in \([0,a]\). By (1), \(H=o(m)\). Thus
\[
N(E_\kappa,\delta)\asymp m\asymp(\log(1/\delta))^{1/\kappa}.
\tag{2}
\]
The translation by one has no effect on covering numbers.

**Local covering bound.** First work with \(F=\{0\}\cup\{u_n:n\ge1\}\), without the translation. Fix a real interval \(J\) of length \(r\ge\delta\). Its part in \([0,a]\) needs at most \(2+\min\{r,a\}/\delta\) length-\(\delta\) intervals. To bound the remaining part, note that the inverse counting variable is \(t(x)=(-\log x)^{1/\kappa}\) for \(0<x\le e^{-1}\), and on \(a\le x\le e^{-1}\) its derivative satisfies
\[
|t'(x)|=\frac{(-\log x)^{1/\kappa-1}}{\kappa x}
\le\frac{m^{1-\kappa}}{\kappa x}\le C_\kappa\frac Hx.
\]
Counting integers in any inverse-image interval gives
\[
\#\{n<m:u_n\in J\}\le 2+C_\kappa H\log(1+r/a).
\]
Consequently
\[
N(F\cap J,\delta)\le C_\kappa\bigl[1+\min\{r,a\}/\delta+H\log(1+r/a)\bigr].
\tag{3}
\]
For \(\delta\le r\le a\), the right side is at most \(C_\kappa(1+r/\delta)\); hence for fixed \(0<b<1\),
\[
r^{-b}N(F\cap J,\delta)\le C_{\kappa,b}\delta^{-b}H^{1-b}.
\]
For \(r\ge a\), put \(c=r/a\ge1\). The same follows from (3) and boundedness of \(c^{-b}[1+\log(1+c)]\) on \([1,\infty)\). This proves the middle-regime upper bound.

**Matching local lower bound.** Set \(J=[a,2a]\), of length \(a=\delta H\), for all sufficiently small \(\delta\). The inverse formula and the mean-value theorem give
\[
\#\{n:u_n\in[a,2a]\}
=m-(-\log(2a))^{1/\kappa}+O(1)
\sim\frac{m^{1-\kappa}}\kappa\log2\sim H\log2.
\]
The relevant spacings are at least \(\delta\) up to a harmless endpoint, so one length-\(\delta\) interval covers at most two of these points. Therefore
\[
a^{-b}N(F\cap[a,2a],\delta)\ge c_{\kappa,b}\delta^{-b}H^{1-b}.
\tag{4}
\]
This establishes the exact middle logarithmic exponent, without needing to optimize a leading constant.

For \(b\le0\), any admissible normalized interval has \(|I|^{-b}\le1\). The global upper bound (2) applies; choosing the entire interval \(I=[1,2]\) at \(R=1\) gives the matching lower bound. For \(b\ge1\), every interval of length \(r>\delta\) can be covered by at most \(2+r/\delta\) intervals of length \(\delta\), so \(r^{-b}N\le C\delta^{-b}\). Conversely choose at \(R=1\) an interval of length \(2\delta\) containing the point \(1\), which gives \(\gtrsim\delta^{-b}\).

Finally, the outer supremum over dilations \(R>0\) does not change these comparabilities. Whenever \(E_R\) is nonempty, \(1/2<R\le2\). Covering \(E_R\cap I\) at scale \(\delta\) is the same as covering \(E_\kappa\cap(RI)\) at scale \(R\delta\), with \(|RI|=R|I|\). All preceding estimates hold uniformly when the scale is multiplied by a factor between \(1/2\) and \(2\); these factors only affect constants in the two-sided bounds. The lower bounds already use \(R=1\). This completes the proof.

## Verification
The gap asymptotic follows by differentiating \(e^{-t^\kappa}\); the inverse derivative and integer counting establish (3) without an unproved localization lemma. Estimate (4) uses separated sparse points, not a continuum-density approximation. The regime comparison is an infinite argument valid for all sufficiently small scales; finite numerical tests are not substituted for proof. The constants implicit in comparability are not asserted to be sharp. In particular, the optimal *multiplicative* constant may be affected by the integer packing of near-critical gaps and is not identified here.

## Relationship to prior work
Reference [1], equations (1.1)–(1.5) and the example (1.12), introduces the exact entropy functional and analyzes polynomially convergent radii \(1+n^{-\mu}\) in its endpoint spherical-maximal study. Reference [2] establishes weighted spherical-maximal ranges in terms of the power-law Legendre–Assouad function. Those dimension exponents do not resolve the logarithmic growth factor established here for the distinct stretched-exponential family. Classical Assouad-spectrum references [3] concern dimension spectra, not this three-regime finite-scale two-sided logarithmic profile. The previous results remain prerequisites and context rather than being claimed as new. No conclusion about weighted endpoint boundedness of a maximal operator is drawn.

## Limitations
Only fixed \(0<\kappa<1\), fixed real \(b\), and the specified stretched-exponential family are treated. Constants are not uniform as \(b\) tends to \(0\) or \(1\), or as \(\kappa\) approaches either endpoint. The theorem determines exact exponents and two-sided orders, not a single optimal leading coefficient. Searches cannot exclude an unindexed equivalent result; this is a priority risk, not proof of uniqueness.

## References
[1] M. Fraccaroli, J. Lee, N. Lei, J. Roos, A. Seeger, *Endpoint power weight inequalities for spherical maximal functions*, arXiv:2610.18316 (first public 13 October 2026), especially equations (1.1)–(1.5), example (1.12), and Section 3.

[2] M. Fraccaroli, J. Roos, A. Seeger, *Power weight inequalities for spherical maximal functions*, arXiv:2602.17613 (first public 19 February 2026); Math. Z. 314, 4 (2026), especially Section 3.

[3] J. M. Fraser, *New dimension spectra: finer information on scaling and homogeneity*, Adv. Math. 329 (2018), 273–328; DOI:10.1016/j.aim.2017.12.019.
