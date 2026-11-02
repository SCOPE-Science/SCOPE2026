# State-resolved stationary reconstruction and a unique beta–binomial sector in a three-state active oscillator

## Finding

For a one-dimensional harmonically confined run-and-tumble particle with a nonzero-duration resting state, **the complete stationary joint law of position and internal motor state is determined by one integral of the known total-position marginal**. For every pair of positive dimensionless rates \(a,t\), let \(p\) be the stationary density of normalized position \(X\in(-1,1)\), and \(p_s(x)\) the joint density of \(X=x\) and motor state \(S=s\in\{-1,0,1\}\). Then, for almost every \(x\in(-1,1)\),

\[
\begin{aligned}
p_0(x)&=(1-x^2)p(x)-a\int_{|x|}^1 y\,p(y)\,dy,\\
p_{\pm1}(x)&=\tfrac12\bigl[(1\pm x)p(x)-p_0(x)\bigr].
\end{aligned}
\tag{1}
\]

This reconstruction applies **without an exception** at \(a+t=1\), at integral rates, and at the singularity or regularity transitions of the total density. Consequently all state-resolved polynomial moments are explicitly determined: with \(M_{2k}=\mathbb E[X^{2k}]\), \(M_0=1\),

\[
\begin{aligned}
\mathbb E[X^{2k}\mathbf1_{\{S=0\}}]
 &=M_{2k}-\left(1+\frac{a}{2k+1}\right)M_{2k+2},\\
\mathbb E[X^{2k}\mathbf1_{\{S=\pm1\}}]
 &=\tfrac12\left(1+\frac{a}{2k+1}\right)M_{2k+2},\\
\mathbb E[X^{2k+1}\mathbf1_{\{S=0\}}]&=0,\\
\mathbb E[X^{2k+1}\mathbf1_{\{S=\pm1\}}]&=\pm\tfrac12M_{2k+2},
\end{aligned}\tag{2}
\]

where \(k\ge0\) and

\[
M_{2k}=\frac{(2k)!}{4^k k!}
\frac{(t/2)_k}{((a+t)/2)_k((a+1)/2)_k}.
\tag{3}
\]

There is exactly one positive-rate curve on which the conditional motor state has the **binomial law with its success probability determined solely by position**:

\[
\boxed{\quad
\mathbb P(S=s\mid X=x)
 =\binom{2}{s+1}\left(\frac{1+x}{2}\right)^{s+1}
 \left(\frac{1-x}{2}\right)^{1-s}
\quad\text{for }s=-1,0,1\quad
\Longleftrightarrow\quad t=a+1.
}\tag{4}
\]

Along this entire curve the full joint densities factor explicitly:

\[
\boxed{\quad
p_{\pm1}(x)=\frac{C_a}{4}(1-x^2)^{a-1}(1\pm x)^2,
\qquad p_0(x)=\frac{C_a}{2}(1-x^2)^a,
\quad C_a=\frac{\Gamma(a+\frac12)}{\sqrt\pi\Gamma(a)}.
}\tag{5}
\]

Equivalently, \(Q=(1+X)/2\) is exactly \(\operatorname{Beta}(a,a)\) distributed, and \(S+1\mid Q\sim\operatorname{Binomial}(2,Q)\). Thus the posterior motor-state law is independent of \(a\), although the position marginal and unconditional motor-state probabilities depend on \(a\). In particular, \(\mathbb E[S\mid X=x]=x\), \(\operatorname{Var}(S\mid X=x)=(1-x^2)/2\), and \(\operatorname{Corr}(X,S)=1/\sqrt{a+1}\) on this curve.

## Assumptions and scope

The normalized process solves \(\dot X=-X+S\), where \(S\) is a continuous-time irreducible Markov chain on \(\{-1,0,1\}\): a running state \(+1\) or \(-1\) jumps to resting state \(0\) at rate \(a>0\), and a rest jumps independently to either running sign at rate \(t/2\), with \(t>0\). No direct \(+1\leftrightarrow-1\) switches or additional spatial Brownian noise are present. The unique stationary position distribution is supported on \([-1,1]\); its total marginal \(p\) is even and locally integrable, with no stationary atoms. In physical units, \(\dot Y=-bY+V S\), \(b,V>0\), use \(X=bY/V\), \(a=\gamma_R/b\), and \(t=\gamma_T/b\); the unique binomial condition becomes \(\gamma_T=\gamma_R+b\). Formulas (1)–(5) are identities of density representatives away from singular points and almost everywhere on the full interval.

## Proof

**Stationarity and regularity.** The finite-state chain \(S\) has a unique stationary law, and the stationary position is the bounded functional \(X_u=\int_{-\infty}^u e^{-(u-v)}S_v\,dv\). This realizes the unique invariant law: two solutions driven by the same stationary internal path contract in position at rate \(e^{-u}\), while the finite-state irreducible chain couples exponentially. Its stationary state-resolved densities satisfy the forward transport equations in the open interval. The endpoint behavior \(p(x)=O((1-|x|)^{a-1})\), known from the exact stationary marginal and independently consistent with the rate of uninterrupted runs, gives \((1-x^2)p(x)\to0\). The resting-state density vanishes at the endpoints: to rest at a position within \(\varepsilon\) of either endpoint, the preceding run must approach that endpoint and the ensuing resting trajectory only moves inward. The transport equations can also be interpreted weakly across any integrable center singularity.

**Flux reconstruction.** Write \(u=p_{+1}+p_{-1}\) and \(q=p_{+1}-p_{-1}\). Adding the three stationary forward equations gives zero net flux \(-xp+q=0\), since the flux is constant and must vanish at the compact support endpoints. Thus \(q=xp\). Subtracting the two running-state equations cancels their equal replenishment terms, giving

\[
\frac{d}{dx}(u-xq)=-a q.
\]

Since \(u=p-p_0\), this becomes \(\frac{d}{dx}[(1-x^2)p-p_0]=-axp\). Integrating from \(x\) to the right endpoint for \(x>0\), and using evenness for \(x<0\), gives (1). Nonnegativity follows because these are the densities of the unique invariant process, not because a difference of arbitrary positive functions must be nonnegative. The same identity remains valid at \(a+t=1\), where a different algebraic elimination formula would divide by zero.

**All mixed moments.** Integrating (1), using Fubini and evenness, yields

\[
2\int_0^1x^{2k}\left(\int_x^1y p(y)\,dy\right)dx
=\frac{M_{2k+2}}{2k+1}.
\]

This proves (2). Formula (3) follows from the established exact hypergeometric characteristic function of the total marginal, or directly from the finite-state stationary generator moment recurrence \((mI-Q^\top)m_m=m\operatorname{diag}(-1,0,1)m_{m-1}\). Its \(k=0\) case gives \(\mathbb P(S=0)=a/(a+t)\), as required.

**Existence of the binomial sector.** Set \(t=a+1\) and define the three nonnegative functions in (5). They sum to the normalized beta density \(p(x)=C_a(1-x^2)^{a-1}\). Substitute them into the three stationary transport equations

\[
\begin{aligned}
0&=-\partial_x[(-x-1)p_{-1}]-a p_{-1}+\tfrac t2 p_0,\\
0&=\partial_x(xp_0)+a(p_{-1}+p_{+1})-t p_0,\\
0&=-\partial_x[(1-x)p_{+1}]-a p_{+1}+\tfrac t2 p_0.
\end{aligned}
\]

Each left-hand side vanishes identically for \(|x|<1\); the endpoint probability currents vanish, and the densities have the required integrable behavior because \(a>0\). Uniqueness of the stationary law therefore proves (5), and division by their sum gives (4) in the forward direction.

**Uniqueness of the binomial sector.** Conversely assume the conditional binomial formula in (4) holds for the stationary law at arbitrary \(a,t>0\). Its conditional moments give \(\mathbb E[S\mid X]=X\) and \(\mathbb E[S^2\mid X]=(1+X^2)/2\). Stationarity applied to the test functions \(X^2\) and \(XS\), noting that the internal generator sends \(S\mapsto-aS\), gives the two exact identities

\[
\mathbb E[XS]=\mathbb E[X^2],\qquad
\mathbb E[S^2]=(a+1)\mathbb E[X^2].
\]

Hence \(\mathbb E[X^2]=1/(2a+1)\), and \(\mathbb E[S^2]=(a+1)/(2a+1)\). But the stationary internal chain has \(\mathbb E[S^2]=t/(a+t)\). Comparing these positive quantities and canceling \(a>0\) forces \(t=a+1\). The correlation statement follows from the stated second moments, symmetry and \(\mathbb E[XS]=\mathbb E[X^2]\).

## Verification

The supplied `state_checker.py` implements exact rational arithmetic with no third-party packages. It independently solves the three-state generator's stationary moment equations for 21 successive degrees across 56 positive-rate pairs and compares every state moment with (2)–(3), then verifies the beta-binomial stationary generator equations through degree 26 for eight further parameter choices. All **4,200** comparisons passed when run on the actual code file before packaging. These are finite checks; the proof above establishes the arbitrary-rate and all-degree assertions.

Reproduce using `python3 state_checker.py`. The code tests moments and stationarity rather than approximating or asserting the uniqueness of an infinite-dimensional invariant measure.

## Relationship to prior work

Sun, Ye and Podgornik, arXiv:2409.00578v1 (first public 2024-09-01), derive the **total** one-dimensional stationary position density and its moment sequence for arbitrary independent run and tumble rates; their later v2, Section III, explicitly notes that resolving the **separate internal-state densities** from their total distribution was left for further investigation. The present theorem uses their total characteristic function for (3), but supplies the missing state-resolved reconstruction, exact mixed moments, and a uniquely characterized beta–binomial joint-law sector.

Basu, Majumdar, Rosso, Sabhapandit and Schehr, arXiv:1910.10083, solve the related three-state confined model when the outgoing running and resting rates coincide. Their source-model constraint \(a=t\) does not include the binomial curve \(t=a+1\), and their state-resolved equations do not provide the all-rate reconstruction formula (1). The current result is not a new total-density formula and does not claim that the known special equal-rate solutions were unknown.

## Limitations

The conditional binomial identity is limited to the exact no-translational-noise, unbiased, three-internal-state model. Other velocity distributions, state-dependent trap forces, direct sign reversals, nonexponential switching, and thermal diffusion are not covered. The all-rate state reconstruction requires the *known total density*; (1) is not a closed elementary expression for that density itself. The source's finite-tumble total hypergeometric density and the earlier equal-rate state-resolved case must be credited. Publication priority remains provisional pending comparison with any broader, presently unidentified state-resolved stationary PDMP identities. No independent audit is claimed.

## References

1. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v1 (2024-09-01), Section III, Eqs. (37)–(42); revised v2 (2025-04-16), Eqs. (38)–(43). https://arxiv.org/html/2409.00578v2
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083v1 (2019-10-22), Sections 2–3. https://arxiv.org/pdf/1910.10083
3. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap*, *Physical Review E* **111**, 044136 (2025), DOI:10.1103/PhysRevE.111.044136.
