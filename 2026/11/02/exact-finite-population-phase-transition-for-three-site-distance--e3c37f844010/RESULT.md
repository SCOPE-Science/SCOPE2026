# Exact finite-population phase transition for three-site distance-weighted two-facility location

## Finding

Consider the **Global Pair** (also called **Pairwise-Distance**) randomized two-facility rule. Among \(n\ge3\) agents on the real line occupying **exactly three distinct sites**, it selects an unordered pair of agent indices with probability proportional to their distance, then opens facilities at the selected reports. Let \(D_n\) be the supremum, over these profiles, of expected total nearest-facility distance divided by the unrestricted optimal total distance using at most two facilities.

Put \(N=n-1\) and
\[
Q_N=\max_{1\le a\le N-1}\frac{4}{1+1/a+2/(N-a)}.
\]
Then the exact finite-population law is
\[
\boxed{D_n=\max\left\{\frac{3(n-2)}{n-1},\;Q_{n-1}\right\}}
\]
and exhibits a sharp transition:
\[
\boxed{D_n=\begin{cases}
\dfrac{3(n-2)}{n-1},&3\le n\le14,\\[3pt]
\displaystyle\max_{1\le a\le n-2}\frac{4}{1+1/a+2/(n-1-a)},&n\ge15.
\end{cases}}
\]
For \(3\le n\le14\), the supremum is **not attained** at any profile with three distinct occupied sites. It is approached by counts \((1,n-2,1)\) as one consecutive gap becomes arbitrarily larger than the other. For \(n\ge15\), the maximum **is attained** by three equally spaced sites with counts \((a,n-1-a,1)\), where \(a\) minimizes \(1/a+2/(n-1-a)\). It suffices to test the two integers nearest \((n-1)/(1+\sqrt2)\). For example, \(D_{14}=36/13\), while \(D_{15}=48/17\), attained by multiplicities \((6,8,1)\).

As \(n\to\infty\), the sharp three-site factor tends to \(4\), the previously established population-uniform bound for the rule. The new assertion is the **exact factor at each finite population size under the minimal nontrivial three-site support restriction**, together with the change in extremizer geometry at \(n=15\); the general factor \(4\) and the rule itself are not claimed as new.

## Assumptions and scope

All \(n\) agents are labeled and located at positions \(0,u,u+v\), where \(u,v>0\), with positive integer multiplicities \(A,B,C\) satisfying \(A+B+C=n\). Translation and scaling leave the approximation ratio unchanged. Coincident agent reports at one occupied site are allowed, but the three sites themselves must be distinct.

Each unordered pair of indices at different locations has probability equal to its distance divided by the sum of all pairwise distances. Pairs of indices at a common location have zero weight. Every agent pays the distance to their nearer opened facility, and the expected social cost averages over this lottery. The optimum places at most two facilities **anywhere on the real line**, not merely at two previously selected reports. The optimum is strictly positive for the stipulated three-site profiles.

The conclusion is about the cost ratio of this particular mechanism, not the best possible mechanism, equilibrium behavior, or non-line metrics. The rule's strategyproofness on Ptolemaic metric spaces comes from prior literature and is not reproved here.

## Proof

**1. An exact three-site formula.** Let \(a=u\), \(b=v\), and \(Z=ABa+BCb+AC(a+b)\), the sum of all pair weights. The lottery chooses a pair of occupied sites \((0,a)\), \((a,a+b)\), or \((0,a+b)\) with aggregate weights \(ABa\), \(BCb\), or \(AC(a+b)\). In these outcomes the social costs are respectively \(Cb\), \(Aa\), and \(B\min(a,b)\). Consequently
\[
\mathbb E\mathrm{SC}=\frac{ABC\bigl(2ab+(a+b)\min(a,b)\bigr)}{ABa+BCb+AC(a+b)}.
\]
The unrestricted optimal cost is
\[
\mathrm{OPT}=\min\{Aa,\,B\min(a,b),\,Cb\}.
\]
Indeed, an optimal two-median solution on the line can choose sites among the distinct reported locations: in an optimal assignment, each center can be moved to a median of its assigned agents without increasing total cost. Checking the three two-site selections yields the stated minimum.

**2. Extremal gap reduction.** By reflection it is sufficient first to take \(a\le b\), set \(a=1\), and put \(t=b/a\ge1\). Define \(d=\min(A,B)\), \(U=A(B+C)\), and \(V=C(A+B)\). The ratio becomes
\[
R(t)=\frac{ABC(1+3t)}{(U+Vt)\min(d,Ct)}.
\]
In the branch \(Ct\le d\), differentiation gives
\[
\frac{dR}{dt}=-\frac{AB(U+2Vt+3Vt^2)}{t^2(U+Vt)^2}<0.
\]
In the branch \(Ct\ge d\), differentiation gives
\[
\frac{dR}{dt}=\frac{ABC(3U-V)}{d(U+Vt)^2},
\]
which has constant sign. Thus the supremum for fixed multiplicities and \(t\ge1\) occurs either at \(t=1\) or in the limit \(t\to\infty\). The latter equals \(3\max(A,B)/(A+B)\). Reflecting exchanges \(A\) and \(C\). Therefore, for every fixed triple of counts, the supremum over all positive gaps is exactly the maximum of
\[
E(A,B,C)=\frac{4ABC}{(AB+BC+2AC)\min(A,B,C)},\quad
\frac{3\max(A,B)}{A+B},\quad
\frac{3\max(B,C)}{B+C}.
\]
No other gap ratio needs to be optimized.

**3. Optimize integer multiplicities.** The two degenerate-gap terms are at most \(3(n-2)/(n-1)\), because their smaller displayed count is at least one, while the sum of the displayed counts is at most \(n-1\). Equality of the limiting value is possible for counts \((1,n-2,1)\).

For the equal-gap term \(E\), if \(B\) is a smallest count then
\[
E\le\frac{4AC}{A+C+2AC}<2.
\]
For \(n\ge4\) this is at most the degenerate-gap bound, and \(n=3\) is immediate. If \(C\) is a smallest count, then
\[
E\le\frac{4AB}{AB+B+2A}=\frac{4}{1+1/A+2/B}.
\]
Increasing \(A\) or \(B\) until \(A+B=n-1\) can only increase the right-hand side. If instead \(A\) is smallest, the analogous estimate is \(4/(1+1/C+2/B)\), with the same optimization. Equality is achieved by placing a single agent at the relevant end site and using equal consecutive gaps. Hence maximizing \(E\) over all counts yields no value exceeding the larger of the degenerate-gap bound and \(Q_{n-1}\), and the \(Q_{n-1}\) value is realizable. This establishes the exact maximum-of-two formula.

**4. The sharp transition.** Write \(N=n-1\). The function
\[
g_N(s)=\frac1s+\frac2{N-s},\qquad 0<s<N,
\]
is strictly convex and uniquely minimized over the reals at \(s=N/(1+\sqrt2)\). Cauchy--Schwarz gives \(g_N(s)\ge(3+2\sqrt2)/N\). Thus
\[
Q_N\le\frac{4N}{N+3+2\sqrt2}.
\]
For \(2\le N\le13\), this is strictly below \(3(N-1)/N\), since
\[
p(N)=N^2-(6+6\sqrt2)N+9+6\sqrt2<0
\]
throughout that interval: \(p\) is convex and both endpoint values \(p(2)=1-6\sqrt2\) and \(p(13)=100-72\sqrt2\) are negative. Consequently the collapsing-gap term wins strictly for \(3\le n\le14\).

For even \(N=2k\ge14\), the equal-gap choice of counts \((k,k,1)\) has factor \(4k/(k+3)\), which exceeds \(3(2k-1)/(2k)\) precisely when \(2k^2-15k+9>0\), true for \(k\ge7\). For odd \(N=2k+1\ge15\), counts \((k,k+1,1)\) give \(4k(k+1)/(k^2+4k+1)\), exceeding \(6k/(2k+1)\) precisely when \(k^2-6k-1>0\), again true for \(k\ge7\). Therefore the equal-gap branch wins strictly for all \(n\ge15\). Strict convexity of \(g_N\) restricts its integer minimizers to the floor and ceiling of \(N/(1+\sqrt2)\).

Finally, in the small-population branch the sole possible equality with the limiting upper term requires the two displayed group counts to be \(1\) and \(n-2\), with the remaining group count one. For these counts the ratio increases strictly toward its limit in the relevant gap branch and is smaller at equal gaps; hence no finite positive gap ratio attains the supremum. In the large-population branch equal-gap profiles explicitly attain \(Q_N\). The proof is complete.

## Verification

`verification/check_three_sites.py` independently enumerates all labeled site-pair selections and compares the exact-rational ratio against the closed formula and sharp finite-population bound. It includes exhaustive multiplicity/gap checks for population sizes \(3\) through \(18\), larger structured cases through size \(40\), and seeded profiles through size \(65\). `verification/check_algebra.py` symbolically checks both derivative identities, the equal-gap singleton formula, and strict convexity. Run from the package root using:

```sh
python verification/check_three_sites.py
python verification/check_algebra.py
```

These finite tests check implementations and representative cases; the all-size and all-real-gap statements are established by the preceding analytical proof, not inferred from finite enumeration. Rational arithmetic avoids floating-point tolerance decisions in the finite tests.

## Relationship to prior work

Ma and Peng introduced the Global Pair mechanism and proved its population-uniform approximation factor \(4\), as well as an instance-dependent bound; Chan, Lin, and Wang independently analyzed the same Pairwise-Distance rule and its combinations with another mechanism. Their asymptotic tightness examples include three occupied sites and unbalanced blocks. Those papers establish neither the exact fixed-\(n\) supremum across **all** three-site multiplicities and spacings nor its finite-population change of extremizer type at \(n=15\). Prior finite-size calculations for small numbers of agents are compatible with the relevant branch but do not imply the all-\(n\) transition.

The rule itself, the universal factor \(4\), and the fact that large unbalanced three-site instances approach factor \(4\) are all prior results. The present contribution is the exact integer-parameter optimization and its sharp geometric phase boundary.

## Limitations

This is a restriction to profiles on the real line with exactly three occupied sites. It does not assert the same finite-population approximation factor among profiles with four or more distinct sites, on general metric spaces, for other facility mechanisms, or for truthful report deviations. For \(n\le14\), sharpness requires a limiting gap ratio rather than an admissible maximizing profile. Independent review and independent validation have not been performed; an unindexed equivalent exact three-site optimization remains a priority risk.

## References

1. M. Ma and B. Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, arXiv:2608.09061, first posted 2026-08-10, https://arxiv.org/abs/2608.09061 .
2. H. Chan, J. Lin and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, first posted 2026-08-23, https://arxiv.org/abs/2608.22484 .
