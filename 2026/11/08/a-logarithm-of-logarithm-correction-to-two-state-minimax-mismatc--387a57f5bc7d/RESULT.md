# A logarithm-of-logarithm correction to two-state minimax mismatch entropy

## Finding

Consider the irreducible two-state continuous-time Markov chain with transition rate \(a>0\) from state \(0\) to state \(1\), and rate \(b>0\) from state \(1\) to state \(0\). Write
\[
F(t)=\max_{\Pr(X_0=1)=\varepsilon\in[0,1]} H(X_0\mid X_t),
\]
where entropy is measured in nats, \(t>0\), and the dynamics are \(P_t=\exp(tQ)\). This conditional-entropy maximum is also the minimax mismatch entropy cost for the irreducible stochastic map \(P_t\) in the sense of [1].

**Theorem.** Suppose \(a>b>0\), put \(\Delta=a-b\), and define the dimensionless quantity \(L_t=\log(1/(\Delta t))\) for sufficiently small positive \(t\). The unique maximizing input distribution \((1-\varepsilon_t,\varepsilon_t)\) obeys
\[
\boxed{\lim_{t\downarrow0}\varepsilon_t L_t=\frac{a}{\Delta}},
\]
and the minimax cost has the sharp expansion
\[
\boxed{F(t)=at\{L_t-\log L_t\}+o(t).}
\]
Thus the first correction to the \(at\log(1/t)\) law is a negative \(at\log\log(1/t)\) term, and its constant-order term is fixed by the escape-rate contrast. The displayed \(o(t)\) holds for each fixed unequal positive pair of rates; uniformity as \(\Delta\downarrow0\) is not claimed. The case \(b>a\) follows on interchanging the state labels.

In sharp contrast, for equal rates \(a=b=c>0\) the maximizing prior is \((1/2,1/2)\) at every positive time, and
\[
\boxed{F(t)=h\!\left(\frac{1-e^{-2ct}}2\right)=ct\{\log(1/(ct))+1\}+o(t),}
\]
where \(h(s)=-s\log s-(1-s)\log(1-s)\). There is no logarithm-of-logarithm correction in the symmetric case.

## Assumptions and scope

The state space consists of exactly two states, the jump rates are fixed positive reals, there is no control or time dependence, and the observation is the endpoint state at time \(t\). The quantity \(F(t)\) is a minimax *mismatch* entropy cost, not the entire physical entropy production, which can have additional flow and implementation contributions. Entropy uses the natural logarithm. Only the small-positive-time regime is considered in the asymptotic assertions.

## Proof

**1. Exact transition and objective.** The off-diagonal transition probabilities are
\[
u_t=\frac{a}{a+b}(1-e^{-(a+b)t}),\qquad
v_t=\frac{b}{a+b}(1-e^{-(a+b)t}),\qquad
k_t=1-u_t-v_t=e^{-(a+b)t}.
\]
For an initial probability \(\varepsilon\) of state \(1\), the probability of observing state \(1\) at time \(t\) is \(w_t(\varepsilon)=u_t+k_t\varepsilon\). The entropy chain rule gives the exact objective
\[
\Phi_t(\varepsilon)=h(\varepsilon)+(1-\varepsilon)h(u_t)+\varepsilon h(v_t)-h(w_t(\varepsilon)).
\]
The exact stationarity equation in the open interval is
\[
\Phi_t'(\varepsilon)=
\log\frac{1-\varepsilon}{\varepsilon}
-k_t\log\frac{1-w_t(\varepsilon)}{w_t(\varepsilon)}+h(v_t)-h(u_t)=0.
\]
Further,
\[
\Phi_t''(\varepsilon)
=-\frac1{\varepsilon(1-\varepsilon)}+\frac{k_t^2}{w_t(\varepsilon)(1-w_t(\varepsilon))}<0.
\]
Indeed the strict inequality follows from
\[
w_t(1-w_t)-k_t^2\varepsilon(1-\varepsilon)
=(1-\varepsilon)u_t(1-u_t)+\varepsilon v_t(1-v_t)>0.
\]
The one-sided endpoint derivatives are \(+\infty\) and \(-\infty\), respectively, because \(0<u_t,v_t<1\). Therefore \(\Phi_t\) has exactly one maximizer \(\varepsilon_t\in(0,1)\) for each \(t>0\).

**2. Concentration on the faster-escaping state.** Assume \(a>b\) and write \(\Delta=a-b\). Uniformly for \(\varepsilon\in[0,1]\), estimating \(X_0\) by \(X_t\) gives error probability
\[
e_t(\varepsilon)=(1-\varepsilon)u_t+\varepsilon v_t
=t(a-\Delta\varepsilon)+O(t^2).
\]
The binary Fano inequality yields \(\Phi_t(\varepsilon)\le h(e_t(\varepsilon))\). For each *fixed interior* \(\varepsilon\), using the exact entropy formula also gives
\[
\Phi_t(\varepsilon)=(a-\Delta\varepsilon)t\log(1/t)+O_\varepsilon(t).
\]
Taking fixed \(\varepsilon\) arbitrarily small establishes
\[
\lim_{t\downarrow0}\frac{F(t)}{t\log(1/t)}=a.
\]
If the optimizing \(\varepsilon_t\) stayed bounded away from zero along a sequence, the uniform Fano bound would give a strictly smaller limiting coefficient. Thus \(\varepsilon_t\to0\).

**3. Boundary layer and precise prior scale.** For each fixed positive constant \(C\), insert \(\varepsilon=Ct\) into the derivative. Since \(u_t=at+O(t^2)\), \(v_t=bt+O(t^2)\), and \(k_t=1+O(t)\), one obtains
\[
\lim_{t\downarrow0}\Phi_t'(Ct)=\log\frac{C+a}{C}>0.
\]
Strict concavity forces \(\varepsilon_t>Ct\) eventually, for every fixed \(C\). Consequently \(t/\varepsilon_t\to0\). Apply the stationary derivative equation to \(\varepsilon_t\), split the derivative as
\[
[h'(\varepsilon_t)-h'(w_t(\varepsilon_t))]
+(1-k_t)h'(w_t(\varepsilon_t))
+h(v_t)-h(u_t)=0.
\]
In the regime \(\varepsilon_t\to0\) and \(t/\varepsilon_t\to0\), the three terms are, respectively,
\[
\frac{at}{\varepsilon_t}(1+o(1)),\qquad
O\!\left(t\{1+\log(1/\varepsilon_t)\}\right),\qquad
-\Delta t\log(1/t)+O(t).
\]
Therefore
\[
\frac{a}{\varepsilon_t}(1+o(1))
=\Delta\log(1/t)+O\!\left(1+\log(1/\varepsilon_t)\right).
\]
As \(\varepsilon_t/t\to\infty\), the last logarithm is at most \(\log(1/t)+O(1)\). This first implies \(1/\varepsilon_t=O(\log(1/t))\). It follows in turn that \(\log(1/\varepsilon_t)=O(\log\log(1/t))=o(\log(1/t))\), proving
\[
\varepsilon_t\log(1/t)\longrightarrow a/\Delta.
\]
Replacing \(\log(1/t)\) by \(L_t=\log(1/(\Delta t))\), a constant shift, gives the asserted prior limit.

**4. Cost through absolute order \(t\).** By the conclusion of step 3, \(\varepsilon_t\asymp1/\log(1/t)\). Taylor's theorem applied to \(h(w_t)-h(\varepsilon_t)\), with \(w_t-\varepsilon_t=at+O(\varepsilon_t t+t^2)\), gives
\[
h(w_t(\varepsilon_t))-h(\varepsilon_t)
=at\log(1/\varepsilon_t)+o(t).
\]
The Taylor remainder is \(O(t^2/\varepsilon_t)=o(t)\); the \(O(\varepsilon_t t)\) displacement has negligible contribution after multiplication by \(\log(1/\varepsilon_t)\). Similarly, the row entropies yield
\[
(1-\varepsilon_t)h(u_t)+\varepsilon_t h(v_t)
=at\{\log(1/t)+1-\log a\}-\Delta\varepsilon_t t\log(1/t)+o(t).
\]
Thus
\[
\frac{F(t)}{t}
=a\log(1/t)+a(1-\log a)
-\Delta\varepsilon_t\log(1/t)
-a\log(1/\varepsilon_t)+o(1).
\]
Since \(\Delta\varepsilon_t\log(1/t)\to a\) and
\(\log(1/\varepsilon_t)=\log\log(1/t)+\log(\Delta/a)+o(1)\), the constant terms simplify to
\[
F(t)/t=a\{\log(1/(\Delta t))-\log\log(1/(\Delta t))\}+o(1).
\]
This is the claimed expansion.

**5. Equal rates.** If \(a=b=c\), the binary channel has both crossover probabilities \(u_t=v_t=(1-e^{-2ct})/2\) and the strict-concavity objective is invariant under \(\varepsilon\mapsto1-\varepsilon\). Hence the unique maximum is at \(\varepsilon_t=1/2\). The exact entropy expression collapses to \(F(t)=h(u_t)\). Expanding \(u_t=ct+O(t^2)\) proves the equal-rate formula.

## Verification

The standalone `verify.py` checks the finite-time transition formula and conditional entropy against a direct four-cell joint distribution calculation, checks the strict-concavity variance identity and stationarity of the unique optimizer, and tests the asymptotic trends using 145-digit Decimal arithmetic. Run `python3 verify.py` with Python 3 and the standard library. It prints `PASS 135 deterministic exact-formula and high-precision checks`. All general-domain assertions above are analytical; finite checks do **not** certify limits, existence beyond the proved argument, or publication priority.

## Relationship to prior work

Yousef, Ansbacher and Wolpert [1], including their full accessible supplemental Section SX, establish the identity between minimax mismatch cost and maximum endpoint conditional entropy, the leading \(\lambda_{\max}t\log(1/t)\) law, and concentration of the optimal prior on states of maximum escape rate. Their statements do not give the concentration *rate* or the next \(t\log\log(1/t)\) and order-\(t\) terms. The present result supplies those terms for the irreducible two-state continuous-time chain and identifies the nonuniform symmetric boundary. Nedić and coauthors [2] develop the generic maximum-equivocation (commitment-capacity) optimization and uniqueness/algorithmic tools; their studied claims do not specialize to continuous-time Markov short-time asymptotics.

## Limitations

The expansion is for fixed positive rates and not uniform in the near-symmetric double-scaling limit. The sharp result is restricted to two states and does not classify higher-dimensional generators, partially observed endpoints, total entropy production, or thermodynamic realization costs. The minimax prior depends on the transition kernel; it is not generally the chain's stationary distribution. The original maximum-equivocation functional is known; the assessed extension is its singular next-order asymptotic not explicitly given in the sources inspected and optimizer rate in this precise setting. Publication-priority searches cannot establish exhaustive uniqueness, and independent mathematical audit has not been performed.

## References

[1] M. Yousef, B. Ansbacher and D. H. Wolpert, *Minimax entropy production for arbitrary processes*, arXiv:2610.03478, first publicly submitted 2026-10-02 (v3, 2026-10-06); full text and supplemental Section SX: https://arxiv.org/html/2610.03478v3 .

[2] N. Nedić, M. Kovačević, D. Čapko and S. Vukmirović, *Notes on conditional entropy and commitment capacity*, Probability and Mathematical Statistics **45** (2025), 115–126, doi:10.37190/0208-4147.00246; accessible full text: https://www.math.uni.wroc.pl/~pms/files_doi/g00246/g00246.pdf .
