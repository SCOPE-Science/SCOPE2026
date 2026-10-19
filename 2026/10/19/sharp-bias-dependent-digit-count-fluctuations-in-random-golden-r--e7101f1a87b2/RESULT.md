# Sharp bias-dependent digit-count fluctuations in random golden-ratio expansions

## Finding
Let \(\beta=(1+\sqrt5)/2\), \(p=\beta^{-2}\), and \(r=\beta^{-1}=1-p\). In the random golden-ratio expansion, make an independent digit-\(1\) choice with probability \(q\in(0,1)\) whenever the orbit visits the switch interval; elsewhere the digit is forced. Start the interval coordinate in the explicitly specified absolutely continuous invariant law below. If \(D_j\in\{0,1\}\) is the digit emitted at time \(j\) and \(S_n=\sum_{j=0}^{n-1}D_j\), then
\[
\frac{S_n}{n}\longrightarrow \rho(q)=\frac{1-qr}{1+p}\quad\text{almost surely},
\qquad
\frac{S_n-n\rho(q)}{\sqrt n}\Longrightarrow \mathcal N(0,V(q)).
\]
The asymptotic variance is exactly
\[
V(q)=\lim_{n\to\infty}\frac{\operatorname{Var}(S_n)}{n}
=\underbrace{\frac{pr}{(1+p)^3}}_{V_{\min}}
+\underbrace{\frac{r^2(p^2+5p+2)}{p(1+p)^3}}_{C>0}\,q(1-q).
\]
Consequently the **unique maximal-variance bias** is \(q=1/2\), whereas the sharp infimum over \(q\in(0,1)\) is attained only in the limits \(q\downarrow0\) or \(q\uparrow1\). Numerically,
\[
V_{\min}=0.0894427190999916\ldots,
\qquad V(1/2)=0.473606797749979\ldots,
\qquad \frac{V(1/2)}{V_{\min}}=5.295084971874738\ldots .
\]
At the balanced bias, the limiting digit density is exactly \(1/2\), but its variance rate exceeds \(1/4\), the benchmark for independent fair digits. At all biases, the intervals between successive switch-region visits have the *same* independent shifted-geometric law; the variation in digit variance comes from the rewards accumulated during those excursions.

## Assumptions and scope
The interval coordinate lies in \(J=[0,\beta]\). Up to endpoints, partition it into
\[
A=[0,r),\qquad B=[r,1],\qquad C=(1,\beta].
\]
On \(A\) the digit is \(0\) and the next coordinate is \(\beta x\); on \(C\) the digit is \(1\) and the next coordinate is \(\beta x-1\). On \(B\), independently at each visit, choose digit \(1\) and map \(x\mapsto\beta x-1\) with probability \(q\); otherwise choose digit \(0\) and map \(x\mapsto\beta x\). The fresh choices are independent of the coordinate and of past choices.

For this model, use the invariant interval-coordinate probability whose density is constant on each atom, with respective values
\[
h_A=\frac{q}{r(1+p)},\qquad h_B=\frac{1}{1+p},\qquad h_C=\frac{1-q}{r(1+p)}.
\]
This is the absolutely continuous invariant branch law; endpoints have probability zero. The result concerns this stationary random dynamical system; no convergence theorem for arbitrary singular initial distributions is asserted.

## Proof
**1. Finite-state coding and invariant law.** Every branch of the map between atoms \(A,B,C\) is affine with slope \(\beta\) and maps its source subinterval *onto the entire target atom*. Consequently a coordinate conditionally uniform on one atom remains conditionally uniform on the next atom, even after specifying a finite atom itinerary. The atom process is therefore the stationary three-state Markov chain with transition matrix, ordered \(A,B,C\),
\[
P_q=\begin{pmatrix}
r&p&0\\ q&0&1-q\\0&p&r
\end{pmatrix}.
\]
Its invariant distribution is
\[
\pi=\frac{1}{1+p}(q,p,1-q).
\]
The Markov chain is irreducible and aperiodic for \(0<q<1\); the above density on \(J\) follows by dividing each atom's stationary mass by its length \((r,p,r)\). This also verifies the claimed invariance directly.

**2. Exact excursion law.** Write \(\tau_i\) for consecutive times when the atom is \(B\). Immediately after a visit to \(B\), the chain jumps to \(A\) with probability \(q\), or to \(C\) with probability \(1-q\). From *either* outer atom it returns to \(B\) with probability \(p\) on each step, otherwise remains in that outer atom with probability \(r\). Thus successive excursion lengths \(L_i=\tau_{i+1}-\tau_i\) are independent and identically distributed with
\[
\Pr(L_i=\ell)=p\,r^{\ell-2},\qquad \ell=2,3,\ldots,
\]
regardless of \(q\). Denote by \(Z_i\) the choice of the digit \(1\) at \(B\), so \(Z_i\) is an independent Bernoulli-\(q\) mark, independent of all the lengths. The total number of digit ones emitted during excursion \(i\), including its first \(B\) time and excluding the next, is
\[
R_i=\begin{cases}1,&Z_i=1,\\ L_i-1,&Z_i=0.\end{cases}
\]
The pairs \((L_i,R_i)\) are i.i.d. Their exponential moments exist around the origin. A stationary initial segment that precedes the first switch visit has an exponentially decaying length, so it does not change the linear mean, asymptotic variance, or central limit law.

**3. Renewal-reward limits.** Let \(J_i=L_i-1\); then \(\Pr(J_i=j)=p\,r^{j-1}\) for \(j\ge1\). In particular
\[
\mathbb E J_i=\frac1p,\quad \operatorname{Var}(J_i)=\frac r{p^2},\quad
m:=\mathbb E L_i=\frac{1+p}{p},\quad \mathbb E R_i=q+\frac{1-q}{p}.
\]
The regenerative strong law gives the asserted \(\rho(q)=\mathbb E R_i/m\). The regenerative central limit theorem (or the i.i.d. two-dimensional CLT followed by random-time inversion) gives
\[
\frac{S_n-n\rho(q)}{\sqrt n}\Longrightarrow\mathcal N\left(0,\frac{\operatorname{Var}(R_i-\rho(q)L_i)}{m}\right).
\]
The same formula is the limit of \(\operatorname{Var}(S_n)/n\), since excursion lengths have exponential tails; for example, truncate the last excursion at length \(O(\log n)\) and bound its complement exponentially, then apply standard second-moment renewal arguments.

For completeness, condition on \(Z_i\). Since \(Z_i\) is independent of \(J_i\), the total-variance identity yields
\[
\begin{aligned}
\operatorname{Var}(R_i-\rho L_i)
={}&\frac r{p^2}\left[q\rho^2+(1-q)(1-\rho)^2\right]
+q(1-q)\left(1-\frac1p\right)^2.
\end{aligned}
\]
Substituting \(\rho=(1-qr)/(1+p)\), multiplying by \(1/m=p/(1+p)\), and simplifying gives the displayed identity for \(V(q)\). Since \(p,r>0\), its coefficient \(C\) is strictly positive. The unique maximizer of \(q(1-q)\) on \((0,1)\) is \(1/2\); its infimum is zero, approached at either endpoint. The corresponding numerical values are direct evaluations of the exact expressions.

**4. Independent spectral cross-check.** The emitted digit labels belong to transitions of the Markov chain: \(A\to A,B\) emits \(0\), \(B\to A\) emits \(1\), \(B\to C\) emits \(0\), and \(C\to B,C\) emits \(1\). Its tilted transition matrix is
\[
M_q(t)=\begin{pmatrix}
r&p&0\\qe^t&0&1-q\\0&pe^t&re^t
\end{pmatrix}.
\]
With \(z=e^t\), the characteristic equation of the Perron eigenvalue \(\lambda_q(t)\) is
\[
\lambda^3-r(1+z)\lambda^2+(r^2z-pz)\lambda+prz(1-q+qz)=0.
\]
The stationary scaled cumulant generating function is \(\log\lambda_q(t)\); its first and second derivatives at \(t=0\) are \(\rho(q)\) and \(V(q)\), respectively. This supplies an algebraically independent route to the mean and variance formulas.

## Verification
The accompanying `verify.py` uses only the Python standard library. It represents \(p=(3-\sqrt5)/2\) exactly as an element of \(\mathbb Q(\sqrt5)\). It checks the invariant distribution, row normalization, the geometric excursion decomposition, and the closed variance formula for five rational biases. Separately, it computes the dominant root of the tilted characteristic polynomial and checks the equivalent renewal equation and numerical derivatives for several values of \(t\). Run `python3 verify.py` from the extracted package directory. The checks establish exact algebraic identities and numerical consistency, not the regenerative central limit theorem by finite enumeration.

## Relationship to prior work
Dajani and Kraaikamp introduced random \(\beta\)-expansions and finite-state descriptions for algebraic bases in *Random \(\beta\)-expansions* (2003). Dajani and de Vries established Bernoulli-choice absolutely continuous invariant laws in *Invariant densities for random \(\beta\)-expansions* (preprint 2006; journal 2007). Their earlier work on measures of maximal entropy gives *independent fair digits under a different invariant measure*; this distinction is essential here. Baker and Dajani's *Induced Random \(\beta\)-transformation* (2015 preprint) analyzes switch-region first-return maps and explicitly identifies the golden-ratio case as a full-branch generalized Lüroth transformation. Thus the finite-state and geometric-return ingredients are prior mathematics, not asserted as new.

The evaluated result here is the **exact sharp asymptotic variance envelope for the emitted digit count across all Bernoulli switch biases**, including its unique maximizing bias and its contrast with the fair independent-digit maximal-entropy measure. The published Markov/inducing machinery makes this evaluation possible; it does not in the inspected passages state the variance expression or its bias optimization. An unlocated earlier finite-Markov-chain variance calculation may imply the result; the originality assessment is not an independent priority determination.

## Limitations
The theorem uses the golden ratio, Bernoulli choices independent at successive switch visits, and the specified stationary absolutely continuous law. It does not claim independence of the emitted digit process, a general formula for all noninteger bases, or a mixing-time rate. The two endpoint biases are limiting infimizers; the theorem's stationary irreducibility claim is for open-interval biases. The derivation of central limit and variance limits is analytical; finite tests alone cannot establish infinite-time convergence. A general spectral Markov-process theorem plus the finite-state matrix may imply the exact formula after additional calculation, so historical priority remains uncertain.

## References
1. K. Dajani and C. Kraaikamp, *Random β-expansions*, Ergodic Theory Dynam. Systems 23 (2003), 461–479, DOI: 10.1017/S0143385702001141.
2. K. Dajani and M. de Vries, *Measures of maximal entropy for random β-expansions*, J. Eur. Math. Soc. 7 (2005), 51–68, DOI: 10.4171/JEMS/21.
3. K. Dajani and M. de Vries, *Invariant densities for random β-expansions*, arXiv:math/0612602 (first posted 2006-12-20); J. Eur. Math. Soc. 9 (2007), 157–176.
4. S. Baker and K. Dajani, *Induced Random β-transformation*, arXiv:1509.06194 (first posted 2015-09-21); Acta Arith. 178 (2017), 1–14.
