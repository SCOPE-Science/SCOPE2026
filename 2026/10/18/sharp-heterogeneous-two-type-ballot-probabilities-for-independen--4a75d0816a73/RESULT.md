# Sharp heterogeneous two-type ballot probabilities for independent first-arrival clocks

## Finding

For each of two types \(j\in\{1,2\}\), two competing collectors independently receive the type at identically distributed, atomless, almost-surely finite times, with cumulative distribution function \(F_j\). All four times are independent. The eventual winner is the collector first receiving both types. Let \(B\) be the event that this winner never has fewer distinct types than the loser at any time before completion.

For independent \(X\sim F_1\) and \(Y\sim F_2\), the exact ballot probability is
\[
\boxed{\Pr(B)=\frac12+\operatorname{Var}(F_2(X))+\operatorname{Var}(F_1(Y)).}
\]
The possible values over all such clock laws form the **entire sharp interval** \([1/2,3/4]\), including both endpoints.

If clocks are first arrivals of independent Poisson processes, with rates \(r>0\) for type one and \(s>0\) for type two for **each** collector, put \(u=r/s\). Then
\[
\boxed{\Pr(B)=\frac12+\frac{u(u^2+4u+1)}{(u+1)^2(u+2)(2u+1)}.}
\]
In the exponential subclass \(1/2<\Pr(B)\le 2/3\), with the upper endpoint attained exactly when \(r=s\); \(1/2\) is approached as \(r/s\) tends to zero or infinity, but is not attained for positive finite rates. Thus heterogeneous first-arrival distributions can achieve ballot probabilities exceeding the largest exponential-clock value.

## Assumptions and scope

The four independent nonnegative almost-surely finite clocks are \(T_{A1},T_{B1}\sim F_1\) and \(T_{A2},T_{B2}\sim F_2\), independent across every index, each \(F_j\) atomless. A collector's count at \(t\ge0\) is \(C_P(t)=\sum_{j=1}^2\mathbf 1\{T_{Pj}\le t\}\). The completion time is \(\tau_P=\max_jT_{Pj}\). With probability one no clocks tie; hence exactly one collector has the smaller completion time. The event \(B\) is
\[
 B=\{\tau_A<\tau_B,\ C_A(t)\ge C_B(t)\ \forall 0\le t\le\tau_A\}\ \cup\ \{\tau_B<\tau_A,\ C_B(t)\ge C_A(t)\ \forall 0\le t\le\tau_B\}.
\]
The theorem is finite-sample and has no large-number-of-types limit. Only its exponential-clock specialization assumes memorylessness.

## Proof

**Step 1: conditional orientations.** For each type \(j\), write the unordered interval \(I_j=[L_j,U_j]\), where \(L_j=\min(T_{Aj},T_{Bj})\) and \(U_j=\max(T_{Aj},T_{Bj})\). Conditional on both intervals, the identity of the collector receiving the type at \(L_j\) is an independent fair coin for each \(j\), since the two clocks for that type are iid, atomless, and independent of the other type. There are almost surely four distinct endpoints.

Order the four endpoints. Up to swapping types, their pairing is one of: disjoint \((1,2),(3,4)\), crossing \((1,3),(2,4)\), or nested \((1,4),(2,3)\). In each case the four orientation pairs are equally likely. The number for which collector \(A\) never trails is respectively one, one, and two (checked directly by recording the four increments of \(C_A-C_B\)). Exchanging collector labels yields the same counts for collector \(B\); the two successful events are disjoint because the first increment cannot have both signs. Consequently,
\[
 \Pr(B)=\frac12+\frac12\Pr(I_1\text{ and }I_2\text{ are nested}).
\]
The event that the winner never trails until completion agrees with a sign-consistent four-increment path: after the earlier completion the winner has count two while the opponent has count at most two, so no later trailing can occur.

**Step 2: nested interval probability.** Let \(X_1,X_2\) be iid with CDF \(F_1\). Conditional on these endpoints, both type-two clocks lie strictly inside \((\min(X_1,X_2),\max(X_1,X_2))\) with probability
\[
 [F_2(\max(X_1,X_2))-F_2(\min(X_1,X_2))]^2
 =[F_2(X_1)-F_2(X_2)]^2.
\]
Taking expectations gives \(2\operatorname{Var}(F_2(X))\), the probability that \(I_1\) contains \(I_2\). Reversing types gives \(2\operatorname{Var}(F_1(Y))\) for \(I_2\) containing \(I_1\). These events are disjoint except for an event of probability zero. Substitution proves the distribution-free identity.

**Step 3: sharp upper bound.** With independent \(X\sim F_1\) and \(Y\sim F_2\), set \(Z=\mathbf1\{X<Y\}\) and \(p=\mathbb EZ\). Because the laws are atomless, \(\mathbb E[Z\mid X]=1-F_2(X)\) and \(\mathbb E[Z\mid Y]=F_1(Y)\). The centered conditional means are orthogonal in \(L^2\) by independence, and their residual is orthogonal to both. Therefore
\[
 \operatorname{Var}(F_2(X))+\operatorname{Var}(F_1(Y))\le \operatorname{Var}(Z)=p(1-p)\le\frac14.
\]
Both variances are nonnegative; hence \(1/2\le\Pr(B)\le3/4\).

To attain every intermediate value, let \(X\) be uniform on \((2,3)\), and let \(Y\) be uniform on \((0,1)\) with probability \(w\) and on \((4,5)\) with probability \(1-w\), for any \(w\in[0,1/2]\). These are atomless finite positive clocks. Then \(F_2(X)=w\) surely, while \(F_1(Y)\) is Bernoulli with probability \(1-w\). Thus
\[
 \Pr(B)=\frac12+w(1-w),\qquad 0\le w\le\frac12,
\]
which continuously and strictly increases from \(1/2\) to \(3/4\). This also proves endpoint attainability.

**Step 4: exponential subclass.** For \(X\sim\operatorname{Exp}(r)\), \(Y\sim\operatorname{Exp}(s)\),
\[
 \operatorname{Var}(F_2(X))=\frac{r}{r+2s}-\left(\frac r{r+s}\right)^2,
 \qquad
 \operatorname{Var}(F_1(Y))=\frac{s}{s+2r}-\left(\frac s{r+s}\right)^2.
\]
Adding and simplifying gives the boxed rational formula. Moreover, elementary polynomial factorization yields
\[
 \frac23-\Pr(B)=\frac{(u-1)^2(2u^2+7u+2)}{6(u+1)^2(u+2)(2u+1)}.
\]
All denominator factors and \(2u^2+7u+2\) are strictly positive for \(u>0\). Equality with \(2/3\) occurs precisely at \(u=1\). The probability exceeds \(1/2\) for every \(u>0\), while the rational positive correction approaches zero at either end of the rate-ratio axis.

## Verification

The included, standard-library-only program `ballot_first_arrival_check.py` checks the three endpoint pairings by full enumeration of their four orientations, and independently enumerates all \(4!=24\) exponential race orders at each of 324 integer rate pairs. Race-order probabilities are calculated using exact rational arithmetic, not Monte Carlo. It compares all cases with the separate closed-form expression, checks sharp inequalities, and tests rational points of the attaining two-component example. The program executed with **352 exact rational assertions passed**. Finite checks support but do not replace the complete argument above.

To replay, run `python ballot_first_arrival_check.py` in a directory containing that file. No third-party packages are required.

## Relationship to prior work

Long's 2026 theorem analyzes the ballot event for **simultaneous discrete rounds**, with each collector drawing one uniform coupon per round, and obtains a large-type asymptotic. Myers and Wilf (2003) develop the earlier two-player discrete-round framework and a more restrictive never-lose-the-lead event. These formulations differ from independent type-specific first-arrival clocks and neither evaluated an arbitrary-law two-type clock formula or its sharp \([1/2,3/4]\) range in the material inspected. The alternating-label and conditional-expectation methods are elementary; the classical equal-law \(2/3\) Catalan case and orthogonal conditional-mean decomposition are not asserted to be novel. The contribution claimed here is their combination into the exact heterogeneous-clock classification and exponential specialization.

## Limitations

The result treats exactly two coupon types and two exchangeable collectors; it does not cover three or more types, dependencies between type clocks, atoms/tied arrival times, or simultaneous-round draws. The fully general upper endpoint can require nonexponential, separated-support clocks. Although primary relevant literature was compared, an unlocated general two-sample ordering theorem might imply some or all of the identity; independent priority assessment has not been performed. No independent validation is asserted.

## References

1. Christopher D. Long, *The Ballot Event for Two-Player Coupon Collection: A Renewal–Catalan Asymptotic*, arXiv:2605.09641, first version posted May 10, 2026. https://arxiv.org/abs/2605.09641
2. Amy N. Myers and Herbert S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229, first version posted April 16, 2003. https://arxiv.org/html/math/0304229v1
3. Wassily Hoeffding, *A Class of Statistics with Asymptotically Normal Distribution*, Annals of Mathematical Statistics 19 (1948), 293–325, doi:10.1214/aoms/1177730196. The conditional projection device in the proof is standard.
