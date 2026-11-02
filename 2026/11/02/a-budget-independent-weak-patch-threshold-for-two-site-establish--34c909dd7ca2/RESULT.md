# A budget-independent weak-patch threshold for two-site establishment

## Finding

Let three independently colonizable habitats receive nonnegative expected introduction efforts \(x_1,x_2,x_3\) with fixed total \(E>0\). The first two habitats have the same positive successful-founder intensity per unit effort \(a\), and the third has intensity \(b\), where \(0<b\le a\). Successful-founder counts are independent Poisson variables with means \(a x_1,a x_2,b x_3\). A habitat is established when its successful-founder count is positive. The objective is the probability that **at least two distinct habitats are established**; it is not the expected number of founders or established habitats.

Set \(B=aE\), \(h=b/a\), and \(z=a x_3\). There is a **unique** maximizing allocation. It always has \(x_1=x_2=(E-x_3)/2\), and its third-site effort is characterized exactly by

\[
\begin{cases}
 z=0,&0<h\le \tfrac12,\\
 \displaystyle\frac{e^{hz}-1}{e^{(B-z)/2}-1}=2h-1,\quad 0<z<B,&\tfrac12<h\le1.
\end{cases}
\]

For \(h>1/2\), the equation has exactly one solution. Thus **the weak site receives strictly positive effort if and only if its successful-founder efficiency exceeds half that of either strong site, independent of the available budget**. The minimum two-site establishment failure probability is

\[
F_*(B,h)=u^2+2u(1-u)v,
\qquad u=e^{-(B-z)/2},\quad v=e^{-hz},
\]

with \(z\) as specified; the optimal success probability is \(1-F_*(B,h)\). For \(h\le1/2\), the optimum simplifies to \((1-e^{-B/2})^2\). For \(h=1\), the three efforts are each \(E/3\).

When \(1/2<h\le1\) is fixed, the optimal third-site *fraction of total normalized effort* satisfies

\[
\frac{z_*(B,h)}B\longrightarrow\frac{2h-1}{4h-1}\quad(B\downarrow0),
\qquad
\frac{z_*(B,h)}B\longrightarrow\frac{1}{2h+1}\quad(B\to\infty).
\]

More precisely, for fixed \(h>1/2\),
\[
z_*(B,h)=\frac{B+2\log(2h-1)}{2h+1}+o(1)\qquad(B\to\infty).
\]

These are statements about the stated independent, one-shot establishment model, not long-term persistence after establishment.

## Assumptions and scope

The Poisson counts are independent across habitats, with means proportional to introduction efforts. Each site needs at least one successful founder, the target is at least two *different* established sites, and effort is divisible continuously. There is no post-establishment dispersal, density dependence, Allee threshold above one successful founder, shared environmental shock, or time-dependent resource effect. The efficiencies \(a,b\) are fixed and known; the two strong sites are exchangeable. The result holds for all real \(E,a>0\) and \(0<b\le a\), including the boundary \(b=a/2\).

Under Poisson thinning, the per-site establishment probabilities are \(1-e^{-a x_1}\), \(1-e^{-a x_2}\), and \(1-e^{-b x_3}\). These are model premises, not empirical estimates.

## Proof

**1. Symmetry of optimal efforts at the strong sites.** For fixed \(x_3\), put \(r=1-e^{-b x_3}\), \(u_1=e^{-a x_1}\), and \(u_2=e^{-a x_2}\). The probability of at least two establishments is
\[
P=1-(1-r)(u_1+u_2)+(1-2r)u_1u_2.
\]
The product \(u_1u_2=e^{-a(E-x_3)}\) is fixed. Since \(1-r=e^{-b x_3}>0\), maximizing \(P\) requires minimizing \(u_1+u_2\). The arithmetic-geometric mean inequality gives \(u_1+u_2\ge2\sqrt{u_1u_2}\), with equality if and only if \(x_1=x_2\). Thus *every* global maximizer has equally funded strong sites, even if the weak site receives all effort.

**2. Failure probability after equalization.** With \(z=a x_3\), the failure probabilities at strong and weak sites are \(u=e^{-(B-z)/2}\) and \(v=e^{-hz}\). The system fails when no site or exactly one site establishes, whence
\[
F(z)=u^2+2u(1-u)v,\qquad 0\le z\le B.
\]
Direct differentiation, using \(u'=u/2\) and \(v'=-hv\), yields the exact factorization
\[
F'(z)=u\bigl[u(1-v)+(1-2h)v(1-u)\bigr].
\]

**3. Sharp regime and equality.** If \(0<h\le1/2\), both bracket terms are nonnegative and the first is strictly positive at every \(z>0\), so \(F\) is strictly increasing on \((0,B]\); its unique minimum is \(z=0\). If \(h>1/2\), for \(0<z<B\) the sign of \(F'(z)\) is the sign of
\[
R(z)-(2h-1),\qquad R(z)=\frac{e^{hz}-1}{e^{(B-z)/2}-1}.
\]
The numerator of \(R\) strictly increases, the denominator strictly decreases, and \(R\) increases continuously from \(0\) to \(+\infty\) as \(z\) runs from \(0\) to \(B\). There is a unique stationary point \(z_*\in(0,B)\). The derivative is negative before it and positive afterward; it is the unique global minimum of \(F\). Combining with Step 1 proves uniqueness of the original three-effort optimum for all allowed parameters.

**4. Small and large budget boundaries.** For fixed \(h>1/2\), write \(z_*=B s_B\). At small \(B\), the root equation, divided by \(B\), gives \(h s_B/[(1-s_B)/2]\to2h-1\), and the interior root and monotonicity ensure \(s_B\to(2h-1)/(4h-1)\). At large \(B\), monotonicity of the same ratio shows that its root lies at positive fractions of \(B\) bounded away from \(0\) and \(1\). Therefore both exponential arguments tend to infinity; taking logarithms of the root equation gives \((h+1/2)z_*-B/2=\log(2h-1)+o(1)\). This proves the stated expansion and large-budget fraction. The case \(h=1\) follows directly by equality of the two exponential terms at \(z=B/3\).

## Verification

The standalone standard-library program `check.py` recomputes the exact three-Bernoulli success probability from the Poisson model, compares it with the reduced expression, checks the root condition, tests strict equalization against nonsymmetric allocations, samples the full budget simplex, and checks the two asymptotic fractions. It reports `VERIFY_OK assertions= 18898`. These numerical samples do not certify the continuum result: Steps 1–4 are the proof. The statement concerns only the defined independent one-shot model.

For illustration, with \(B=3\) and \(h=3/4\), the unique optimum allocates \(z\approx0.8838605327\) normalized units to the weaker site and reaches success probability about \(0.6459140960\). Excluding that site instead gives about \(0.6035267481\).

## Relationship to prior work

Independent Poisson arrivals and immigration effects are central to stochastic metapopulation models, including Eriksson et al. (2014); Leung et al. (2004) concern propagule pressure and establishment in an empirical invasion model. These works motivate the assumptions but do not, in the materially inspected sections, optimize the probability of establishing at least two sites under an unequal-efficiency seeding budget.

Derman, Lieberman and Ross (1974) study budget allocation to a general \(k\)-out-of-\(n\) reliability system with the same cost-to-success function for each component. The current heterogeneous three-site threshold is **not** a claim to originate the \(k\)-out-of-\(n\) framework or the independence formula; the contribution assessed here is its exact heterogeneous-efficiency activation threshold, unique optimizer, and budget-limit laws. The 1974 complete text and a related 1975 allocation chapter could not be materially compared, so independent priority remains unresolved.

## Limitations

The narrow two-equal/one-weaker class and the requirement of at least two sites are essential; no assertion is made for three arbitrary efficiencies, larger numbers of habitats, multiple-founder Allee barriers, dependent environmental outcomes, integer release constraints, or long-run population persistence. The model excludes transport mortality variation with intensity and post-release migration. Biological significance is a transparent mathematical benchmark rather than field validation. The related 1974 and 1975 reliability literature leaves a historical-overlap risk.

## References

- Derman, C., Lieberman, G. J., and Ross, S. M. (1974). *Optimal Allocations in the Construction of k-Out-of-n Reliability Systems*. Management Science 21(3), 241–250. DOI: 10.1287/mnsc.21.3.241. Public journal date: 1974-11-01. Abstract and 1973 Stanford technical-report catalog inspected; complete text unavailable.
- Leung, B., Drake, J. M., and Lodge, D. M. (2004). *Predicting Invasions: Propagule Pressure and the Gravity of Allee Effects*. Ecology 85(6), 1651–1660. DOI: 10.1890/02-0571. First published 2004-06-01. Public abstract and first PDF page inspected.
- Eriksson, A., Elías-Wolff, F., Mehlig, B., and Manica, A. (2014). *The emergence of the rescue effect from explicit within- and between-patch dynamics in a metapopulation*. Proceedings of the Royal Society B 281, 20133127. DOI: 10.1098/rspb.2013.3127. Public online date 2014-02-12. Full PMC article read.
- Derman, C., Lieberman, G. J., and Ross, S. M. (1975). *Optimal allocation of resources in systems*. Reliability and Fault Tree Analysis, SIAM, pp. 307–324. Bibliographic evidence inspected, full chapter unavailable.
