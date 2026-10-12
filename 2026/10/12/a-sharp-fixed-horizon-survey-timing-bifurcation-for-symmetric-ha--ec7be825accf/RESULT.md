# A sharp fixed-horizon survey-timing bifurcation for symmetric habitat occupancy

## Finding

Consider a single habitat with occupied/unoccupied state \(X(t)\in\{0,1\}\), changing from either state to the other at common rate \(\lambda/2\), where \(\lambda>0\). Start the process in its stationary distribution. Observe the true state without measurement error at three predetermined times \(0,u,H\), with \(0<u<H\). The design objective is the Fisher information about \(\theta=\log\lambda\) in the full three-observation likelihood, with \(H\) fixed.

Define \(f(x)=x^2/(e^{2x}-1)\) for \(x>0\), continuously extended by \(f(0)=0\). Let \(a\) denote the unique positive zero of \(f''\), numerically \(a=1.5430468848087244617\ldots\), and write \(T=\lambda H\).

**Theorem.** The complete set of information-maximizing interior survey times has the following phase diagram.

1. If \(0<T\le 2a\), the unique optimum is \(u=H/2\).
2. If \(T>2a\), there are exactly two optima, \(u=x_T/\lambda\) and \(u=H-x_T/\lambda\), where \(x_T\in(0,T/2)\) is the unique solution of \(f'(x_T)=f'(T-x_T)\). The midpoint is then a strict local minimum of Fisher information, not an optimum.
3. As \(T\to\infty\), \(x_T\to c=0.7968121300200200461\ldots\), where \(c\) is the unique positive maximizer of \(f\).

Consequently the sharp symmetry-breaking horizon is \(\lambda H=3.0860937696174489235\ldots\). This transition concerns information for the *turnover timescale* under a finite endpoint-constrained three-visit design; it is not the classical freely chosen equal-spacing problem.

## Assumptions and scope

Each habitat follows the stationary continuous-time two-state Markov model with known equal colonization and local-extinction rates \(\lambda/2\), unknown common timescale \(\lambda\), no false positives or negatives, instantaneous noninvasive observations, and a fixed compulsory first/last observation pair separated by \(H>0\). One middle observation time is freely chosen in \((0,H)\). Independent replicate habitats multiply Fisher information by their number without affecting the optimizer. If the occupancy equilibrium, the two transition rates separately, or detection probabilities are unknown, the objective and conclusions need not apply.

## Proof

**Step 1 (likelihood and information).** The two-state transition matrix over lag \(h\) has diagonal entries \((1+e^{-\lambda h})/2\) and off-diagonal entries \((1-e^{-\lambda h})/2\). Conditional on each preceding state, the next observation reports *same* with a Bernoulli probability depending only on \(\lambda h\), not on the value of the preceding state. Thus the two same/different indicators from lags \(u\) and \(H-u\) are independent. The stationary initial observation contributes no information about \(\theta\). Direct differentiation of their Bernoulli likelihoods gives
\[
\mathcal I_\theta(u,H)=f(\lambda u)+f(\lambda(H-u)).
\]
Writing \(x=\lambda u\) reduces the problem to maximizing \(F_T(x)=f(x)+f(T-x)\) over \(0\le x\le T\). The endpoints are not maxima: \(f'(0)=1/2\) and \(f'(x)<1/2\) for all \(x>0\), so \(F_T'(0)>0\); symmetry gives \(F_T'(T)<0\).

**Step 2 (an exact one-inflection lemma).** Write \(y=e^{2x}\). Repeated differentiation yields \(f^{(k)}(x)=P_k(x,y)/(y-1)^{k+1}\), where \(P_0=x^2\) and
\[
P_{k+1}=(y-1)(\partial_xP_k+2y\partial_yP_k)-2(k+1)yP_k.
\]
In particular
\[
P_2=y^2(4x^2-8x+2)+y(4x^2+8x-4)+2.
\]
Its Taylor series in \(x\) has no terms below degree three, strictly negative coefficients in degrees \(3,4,5,6,7\), and strictly positive coefficients in every degree \(n\ge8\). Indeed, the two exponential contributions to \(n![x^n]P_2\) are
\[
(4n(n-1)-32n+32)4^{n-2}
\quad\text{and}\quad
(4n(n-1)+16n-16)2^{n-2},
\]
for \(n\ge2\), and they are nonnegative and positive respectively for \(n\ge8\). A power series with finite negative lower-order coefficients and positive higher-order coefficients has exactly one positive zero: divide by the largest negative monomial power, making its negative-power part and positive-power part jointly strictly increasing from a negative to a positive limit. This also shows the root is simple. Hence \(f''<0\) before its unique root \(a\), and \(f''>0\) afterwards.

**Step 3 (shape of the third derivative).** The fourth-derivative numerator is
\[
\begin{aligned}
P_4={}&y^4(16x^2-64x+48)+y^3(176x^2-192x-48)\\
&+y^2(176x^2+192x-48)+y(16x^2+64x+48).
\end{aligned}
\]
Expanding the exponentials gives zero coefficients through degree five, strictly negative coefficients in degrees \(6,\ldots,25\) and positive coefficients in all degrees \(n\ge26\). The twenty negative coefficients are verified by the exact integer formula
\[
\begin{aligned}
n![x^n]P_4={}&(16n(n-1)8^{n-2}-64n8^{n-1}+48\cdot8^n)\\
&+(176n(n-1)6^{n-2}-192n6^{n-1}-48\cdot6^n)\\
&+(176n(n-1)4^{n-2}+192n4^{n-1}-48\cdot4^n)\\
&+(16n(n-1)2^{n-2}+64n2^{n-1}+48\cdot2^n).
\end{aligned}
\]
For \(n\ge26\), each of the four bracketed contributions is strictly positive (check their quadratic factors), so the positive tail follows without truncation. The same one-sign-change power-series argument therefore gives exactly one positive zero \(b\) of \(f^{(4)}\), negative before and positive after it. Since \(f'''(a)>0\) by the simple upward crossing of \(f''\), whereas \(f'''\) increases to zero from below beyond \(b\), we have \(b>a\). Moreover \(f'''\) strictly decreases on \((0,b)\), is negative on \([b,\infty)\), and therefore
\[
 f'''(x)>f'''(z)\quad\text{whenever }0<x<a<z.
\]
These are global sign statements, not conclusions from a finite numerical grid.

**Step 4 (global optimization).** For \(0<x<T/2\),
\[
F_T'=f'(x)-f'(T-x),\quad F_T''=f''(x)+f''(T-x),\quad F_T'''=f'''(x)-f'''(T-x).
\]
If \(T\le2a\), then wherever \(T-x\le a\), both second-derivative terms are negative. On any remaining region \(x<a<T-x\), the inequality in Step 3 makes \(F_T''\) strictly increasing, and its value at the right endpoint of that region is nonpositive. Thus \(F_T''<0\) for \(0<x<T/2\). As \(F_T'(T/2)=0\), one has \(F_T'(x)>0\) throughout \((0,T/2)\). Symmetry proves the midpoint is the unique global maximum.

If \(T>2a\), then \(F_T''>0\) on \([a,T/2)\), while \(F_T''\) is strictly increasing on \((0,a)\) by Step 3. The function \(F_T'\) is positive at zero, zero at \(T/2\), and negative immediately to the left of \(T/2\) because \(F_T''(T/2)>0\). Therefore \(F_T''\) has one zero in \((0,a)\), and \(F_T'\) has exactly one zero \(x_T\) in \((0,T/2)\), changing there from positive to negative. This yields exactly the two reflected global maxima, and the midpoint is a strict local minimum.

**Step 5 (large horizon).** One has \(f(x)>0\) for \(x>0\) and \(f(x)\to0\) at both zero and infinity. The equation \(f'(x)=0\), equivalent to \(1-x=e^{-2x}\), has exactly one positive solution \(c\), the unique maximum. The optimum for large \(T\) has at least the value \(f(c)+f(T-c)\to f(c)\). As the shorter of its two gaps lies in \([0,T/2]\), any subsequence of such gaps escaping to infinity would make both information terms tend to zero, a contradiction; bounded subsequential limits must maximize \(f\), hence equal \(c\). Thus \(x_T\to c\).

## Verification

Run `python verify.py` using Python 3 with SymPy and mpmath. The checker reconstructs the derivative-numerator recurrence symbolically, verifies all finite exceptional Taylor-coefficient signs exactly as integers, proves the infinite positive coefficient ranges by their explicit quadratic factors, checks high-precision brackets for \(a,b,c\), and illustrates the optimizer phase diagram numerically. The proof above, not a sampled grid, establishes global optimization and uniqueness.

## Relationship to prior work

Royle and Kéry (2007) model dynamic species occupancy and its turnover parameters. Mehtälä, Auranen and Kulathinal (2011/2015) study observation spacing for binary longitudinal Markov processes, while their 2014/2015 multistate sequel extends interval design. Michel (2018 preprint; 2020 publication) establishes the free uniform-spacing optimum and adaptive rate estimation for a symmetric two-state chain. The latter source's information formula supplies an equivalent single-interval objective, but its stated asymptotic freely spaced or adaptive results do not impose fixed *first and last* observation times with exactly one intermediate visit. The contribution here is the sharp finite-horizon equal-to-unequal design bifurcation and its complete global classification. An inaccessible specialized fixed-horizon result could cover it; novelty is therefore qualified rather than asserted solely from failed searches.

## Limitations

This is a locally optimal design depending on the unknown turnover scale \(\lambda\); it is a benchmark, not a directly implementable parameter-free schedule. It assumes exactly observed stationary binary states, equal two-way transition rates, equal information value per observation, fixed endpoints, and one middle visit. The model is not a general ecological detection model with imperfect observation, varying transitions, correlated habitats, or cost constraints. Scientific review is same-model only; no independent audit or empirical validation is claimed.

## References

- Royle, J. A., and M. Kéry (2007), *A Bayesian state-space formulation of dynamic occupancy models*, Ecology 88, 1813–1823, DOI `10.1890/06-0669.1` (public July 1, 2007).
- Mehtälä, J., K. Auranen and S. Kulathinal (2011 online), *Optimal designs for epidemiologic longitudinal studies with binary outcomes*, Statistical Methods in Medical Research 24 (2015), 803–818, DOI `10.1177/0962280211430663`.
- Mehtälä, J., K. Auranen and S. Kulathinal (2014 online), *Optimal Observation Times for Multistate Markov Models—Applications to Pneumococcal Colonization Studies*, JRSS C 64 (2015), 451–468, DOI `10.1111/rssc.12084`.
- Michel, J. (2018), *Optimal adaptive sampling for a symmetric two-state continuous time Markov chain*, public manuscript `https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/6/56774/files/2017/12/optimal_sampling_design_ctmc9-1nt190d.pdf`; published Econometric Reviews 39 (2020), 602–611, DOI `10.1080/07474938.2019.1701808`.
- Brown, M., H. Solomon and M. A. Stephens (1977), *Estimation of Parameters of Zero-One Processes by Interval Sampling*, Operations Research 25, 493–505, DOI `10.1287/opre.25.3.493`.
