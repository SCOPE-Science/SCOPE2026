# A collision-lineage identity and equilibrium-Weibull law for repeated birthdays

## Finding

For each integer \(m\ge1\), sample an infinite sequence independently and uniformly from \(m\) labeled categories. For an integer \(s\ge2\), let \(T_s\) be the first sample index at which a category has been sampled \(s\) times. Let \(J_s\) be that unique category, and for \(r\ge2\) let \(B_r=\{J_r=J_{r+1}\}\). Set \(S_s(k)=\Pr(T_s\ge k)\) for integers \(k\ge1\).

**Exact winner-lineage kernel.** For all integers \(m\ge1\), \(r\ge2\), and \(k\ge1\),
\[
\Pr(B_r,T_{r+1}=k)=\frac{S_{r+1}(k)-S_r(k)}m.
\]
Thus
\[
\Pr(B_r)=\frac{\mathbb ET_{r+1}-\mathbb ET_r}{m}
=\int_0^\infty \left[Q_{r+1}(x)^m-Q_r(x)^m\right] \,dx,
\qquad Q_s(x)=e^{-x}\sum_{j=0}^{s-1}\frac{x^j}{j!}.
\]
The integral is absolutely convergent. In particular, \(\Pr(B_r)=1\) when \(m=1\).

**Sharp rare-lineage asymptotics.** For fixed \(r\ge2\), define \(c_s=(s!)^{1/s}\Gamma(1+1/s)\). As \(m\to\infty\),
\[
\Pr(B_r)=c_{r+1}m^{-1/(r+1)}-c_rm^{-1/r}
+O_r\bigl(m^{-2/(r+1)}\bigr).
\]
For the first double and triple collisions this becomes
\[
\Pr(J_2=J_3)=6^{1/3}\Gamma(4/3)m^{-1/3}
-\sqrt{\pi/2}\,m^{-1/2}+O(m^{-2/3}).
\]

**Conditional time law.** Put \(a_m=m^{r/(r+1)}\). Conditional on \(B_r\),
\[
\frac{T_{r+1}}{a_m}\ \Rightarrow\ H_{r+1},\qquad
f_{H_{r+1}}(t)=\frac{\exp[-t^{r+1}/(r+1)!]}{c_{r+1}}\mathbf1_{\{t\ge0\}}.
\]
This is the equilibrium (integrated-tail) distribution associated with the usual limiting Weibull waiting time for the first \((r+1)\)-fold repeat. The unconditioned limit instead has survival function \(\exp[-t^{r+1}/(r+1)!]\) and density \(t^r\exp[-t^{r+1}/(r+1)!]/r!\) for \(t\ge0\). In particular the rare event that the same category wins both thresholds selects a different limiting time distribution.

## Assumptions and scope

Draws are independent and uniform from exactly \(m\) distinguishable categories; \(m\) ranges through positive integers. All hitting times are finite almost surely because a category must reach count \(s\) no later than sample \(m(s-1)+1\). Thresholds \(r\ge2\) are integers; the limits hold with \(r\) fixed while \(m\to\infty\). An arriving observation raises the count of exactly one category, so no ties occur in first threshold crossings. The theorem does not assert a comparable formula for nonuniform probabilities, growing thresholds, or several jointly tagged winners.

## Proof

**1. Exact discrete kernel.** Immediately before the draw at time \(k\), on the event \(T_r<k\le T_{r+1}\), exactly one category was first to reach occupancy \(r\). That winning category currently has occupancy exactly \(r\): had it acquired another observation, a category would already have reached \(r+1\), contradicting \(T_{r+1}\ge k\). By independent uniform sampling, the conditional chance that observation \(k\) hits that category is \(1/m\). That hit occurs at \(T_{r+1}=k\) and establishes \(J_{r+1}=J_r\). Conversely, every outcome in \(\{B_r,T_{r+1}=k\}\) arises in this way. Since \(T_r\le T_{r+1}\),
\[
\Pr(T_r<k\le T_{r+1})
=\Pr(T_{r+1}\ge k)-\Pr(T_r\ge k)
=S_{r+1}(k)-S_r(k).
\]
This proves the exact first identity, including endpoint values at which either tail is zero.

**2. Expected-waiting-time identity.** Every \(T_s\) is an integer-valued bounded waiting time, so \(\mathbb ET_s=\sum_{k\ge1}S_s(k)\). Summing the kernel gives \(\Pr(B_r)=(\mathbb ET_{r+1}-\mathbb ET_r)/m\).

Embed the draws as marks of a rate-\(m\) homogeneous Poisson process, assigning each arrival a uniformly random category. The category processes are independent rate-one Poisson processes. Write \(Z_s\) for the calendar time of the first category's \(s\)-th arrival. The Poisson arrival gaps are independent exponential random variables of mean \(1/m\), independent of the category marks. Hence \(\mathbb EZ_s=\mathbb ET_s/m\). For one rate-one category, the probability of fewer than \(s\) arrivals by time \(x\) is \(Q_s(x)\). Consequently \(\Pr(Z_s>x)=Q_s(x)^m\), and integrating the tails proves the displayed integral.

**3. Asymptotic expected waiting times.** Fix an integer \(s\ge2\). Taylor expansion at zero gives
\[
Q_s(x)=1-\frac{x^s}{s!}+O_s(x^{s+1}),
\qquad x\downarrow0.
\]
Upon setting \(x=u m^{-1/s}\), this implies \(Q_s(u m^{-1/s})^m\to\exp(-u^s/s!)\) for each \(u\ge0\). To justify integration and the error term, choose a small positive \(\delta_s\) so that for \(0\le x\le\delta_s\), the logarithm satisfies
\[
\log Q_s(x)=-\frac{x^s}{s!}+O_s(x^{s+1})
\quad\text{and}\quad \log Q_s(x)\le-\frac{x^s}{2s!}.
\]
After rescaling, split the integral into \(u\le m^{1/(2s(s+1))}\), its remaining part below \(\delta_s m^{1/s}\), and the region above \(\delta_s m^{1/s}\). In the first region, the mean-value inequality for exponentials controls the difference by \(C_s m^{-1/s}u^{s+1}e^{-u^s/(2s!)}\); in the second region the exponential envelope makes the integral negligible; in the third region \(Q_s(x)^m\) has an exponentially small integral because \(Q_s\) is decreasing and its tail is bounded by a polynomial times \(e^{-x}\). Therefore,
\[
\mathbb EZ_s
=m^{-1/s}\int_0^\infty e^{-u^s/s!}\,du
+O_s(m^{-2/s})
=c_s m^{-1/s}+O_s(m^{-2/s}).
\]
Subtract this expansion for \(s=r\) and \(s=r+1\). Since \(2/r\ge2/(r+1)\) for fixed \(r\), the error is \(O_r(m^{-2/(r+1)})\), proving the two-scale probability expansion.

**4. Conditional limit.** Poisson embedding also proves that the first \(s\)-fold time has the ordinary Weibull limit on scale \(b_{m,s}=m^{1-1/s}\): for each \(t\ge0\), \(\Pr(Z_s>t m^{-1/s})\to e^{-t^s/s!}\), and the total rate-\(m\) arrival process concentrates around its mean. More precisely, the Poisson arrival count in the interval \([0,t m^{-1/s}]\) has mean \(t b_{m,s}\) and relative fluctuations tending to zero; monotone sandwiches at \((t\pm\epsilon)m^{-1/s}\) transfer the continuous-time limit to \(\Pr(T_s>\lfloor t b_{m,s}\rfloor)\). Hence
\[
\Pr(T_s/b_{m,s}>t)\longrightarrow e^{-t^s/s!},\qquad t\ge0.
\]
Taking \(s=r+1\), the scale is exactly \(a_m\). Moreover \(\mathbb ET_r=O(m^{1-1/r})=o(a_m)\), since \((r-1)/r<r/(r+1)\).

Let \(g\) be continuous with compact support in \([0,\infty)\). By the exact kernel,
\[
\mathbb E\left[g(T_{r+1}/a_m)\mathbf1_{B_r}\right]
=\frac1m\sum_{k\ge1}g(k/a_m)[S_{r+1}(k)-S_r(k)].
\]
The first tail sum, multiplied by \(1/a_m\), is a Riemann sum converging to \(\int_0^\infty g(t)e^{-t^{r+1}/(r+1)!}\,dt\), using monotonicity of survival functions and convergence at continuity points. The second sum has absolute value at most \(\|g\|_\infty\mathbb ET_r/a_m=o(1)\). Thus the numerator multiplied by \(m/a_m\) converges to the stated integral. The probability of the conditioning event obeys \(\Pr(B_r)\sim c_{r+1}a_m/m\) by step 3. Dividing proves weak convergence on compactly supported test functions. The limiting density integrates to one by the defining gamma integral; hence vague convergence of these probability distributions upgrades to weak convergence, proving the assertion for all bounded continuous test functions.

## Verification

The standalone file `verification/birthday_lineage_verification.py` has no external data dependencies; Python and SciPy are used for exact rational finite-state enumeration and independent numerical quadrature. Running `python verification/birthday_lineage_verification.py` produces:

```
PASS exact finite-state identities: 165
PASS independent gamma-integral comparisons: 12
PASS sharp two-scale asymptotic checks: 6
```

The rational checks independently enumerate the first threshold winner and its successor, verifying the kernel and expectation identity for \(1\le m\le5\) and \(2\le r\le4\). The integral and asymptotic numerical comparisons are not proofs of the asymptotic assertions. The unrestricted results follow from steps 1–4 above.

## Relationship to prior work

Holst (1995) analyzes general birthday quota hitting times and uses Poisson embedding to derive waiting-time moments. Camarri (1998), Section 2, Theorems 1, 2 and 4, and Lemma 3, analyzes \(k\)-fold repeat times and the relation among repeat processes across multiplicities. Camarri and Pitman (2000) supply related repeat-time laws, including Poisson embeddings. These sources establish the classical marginal waiting-time and Weibull background. The result here concerns a different *joint label event*: whether the specific category that was first to reach multiplicity \(r\) is also the first to reach multiplicity \(r+1\). The survival-difference kernel is an exact finite-sample link between that marked event and the two marginal tails. Its conditional time law is an equilibrium Weibull, distinct from the unconditioned Weibull limit.

The expected waiting-time asymptotics alone, or the Poisson embedding itself, are not claimed to be new. The proposed contribution is the exact marked-lineage kernel together with its rare-event probability and conditional selection limit. Earlier general marked-process or quota identities might imply this special case; priority is not independently certified.

## Limitations

All sampling probabilities must be equal and the threshold \(r\) fixed for the limit. The leading and second-order probability terms are asymptotic; the stated remainder does not provide a uniform numerical bound across thresholds. Some historical work on general birthday quotas is not available in full text for comparison, so the novelty assessment carries residual risk. Computational checks cover finite cases only and do not substitute for the analytic proof. 
## References

1. Michael Camarri, *Asymptotics for k-fold repeats in the birthday problem with unequal probabilities*, University of California, Berkeley, Technical Report 524, dated July 10, 1998. https://statistics.berkeley.edu/sites/default/files/tech-reports/524_0.pdf .
2. Michael Camarri and Jim Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, Electronic Journal of Probability **5** (2000), 1–18. https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/58/58-115-1-PB.pdf .
3. Lars Holst, *The general birthday problem*, Random Structures & Algorithms **6** (1995), 201–208. https://doi.org/10.1002/rsa.3240060207 .
