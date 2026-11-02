# A two-front phase transition for random approval-weighted veto consent

## Finding

Fix an integer \(m\ge 2\) and a distinguished candidate \(c\) among \(m\) candidates. Each of \(n\) independent voters approves \(c\) with probability \(p\in(0,1)\), and independently approves each of the other \(m-1\) candidates with a common probability \(q\in(0,1)\). All voter–candidate approval bits are mutually independent. Give each voter binary utility \(1\) for approved candidates and \(0\) for disapproved candidates, with approval threshold \(1/2\). Let \(P_{n,m}(p,q)\) denote the probability that \(c\) belongs to the approval-weighted veto core (AWVC) of Dong et al.

Put
\[
q_c(m)=m^{-1/(m-1)},\qquad
p_*(m,q)=\max\left\{\frac12,\frac{m q^{m-1}}{1+m q^{m-1}}\right\}.
\]

**Phase diagram.** For every fixed \(m\ge2\), \(p\in(0,1)\), and \(q\in(0,1)\),
\[
\lim_{n\to\infty}P_{n,m}(p,q)=
\begin{cases}
0,&p<p_*(m,q),\\
1,&p>p_*(m,q),\\
\frac12,&p=p_*(m,q),\ q\ne q_c(m),\\
\frac14+\frac{1}{2\pi}\arcsin\sqrt{\frac{2}{m+1}},&p=\frac12,\ q=q_c(m).
\end{cases}
\]
In particular, with three candidates the simultaneous critical point \((p,q)=(1/2,1/\sqrt3)\) has limiting consent probability exactly \(3/8\), rather than \(1/2\). The exceptional value results from two distinct classes of blocking coalition being simultaneously marginal. Away from the phase boundary, error probabilities decay exponentially in \(n\) for fixed \((m,p,q)\).

A useful **exact finite-electorate reduction** accompanies this asymptotic statement. Write \(a\) for the number of approvers of \(c\), and for each subset \(T\) of the other candidates let \(h_T\) be the number of voters who disapprove \(c\) and approve every member of \(T\). If \(a=0\), AWVC excludes \(c\) by convention. If \(a>0\), then
\[
 c\notin\mathrm{AWVC}\quad\Longleftrightarrow\quad
 \exists T\subseteq C\setminus\{c\}:\quad m h_T>a(m-|T|).
\]
This reduction is exact for arbitrary finite binary approval profiles, without independence assumptions.

## Assumptions and scope

The candidate set is finite with exactly \(m\) labeled options, and the electorate size \(n\) tends to infinity while \(m,p,q\) remain fixed. The utility and approval threshold are as above, so a voter strictly prefers \(d\) over a disapproved \(c\) precisely when she approves \(d\). The AWVC is the *uncomposed* approval-weighted veto core, not the disapproval-Smith-set composition. All probabilities concern the status of one specified candidate; no independence between the acceptance outcomes of different candidates is asserted. We use the strict AWVC blocking inequality and its prescribed zero-approval convention.

## Proof

**1. Exact blocking reduction.** The definition of AWVC says that when \(a>0\), a nonempty coalition \(S\) of disapprovers of \(c\) blocks it exactly when
\[
\frac{|S|}{a}>1-\frac{|B_S(c)|}{m},\qquad
B_S(c)=\{d:\text{every }i\in S\text{ strictly prefers }d\text{ to }c\}.
\]
With binary utilities and \(c\) disapproved by all members of \(S\), \(B_S(c)\) is their common approval intersection. Set \(T=B_S(c)\). Since \(S\) is contained in the set \(H_T\) of disapprovers approving all of \(T\), its size obeys \(h_T\ge |S|\), giving \(m h_T>a(m-|T|)\). Conversely, if a subset \(T\) satisfies that inequality, then \(H_T\) is nonempty (because \(m-|T|\ge1\) and \(a>0\)), its common approval intersection contains \(T\), and the defining AWVC inequality holds for the coalition \(H_T\). Thus the finite characterization follows, including \(T=\varnothing\).

**2. Law of large numbers.** For fixed \(T\) of cardinality \(k\), the strong law yields
\[
\frac{a}{n}\longrightarrow p,\qquad
\frac{h_T}{n}\longrightarrow (1-p)q^k
\quad\text{almost surely}.
\]
The deterministic limiting blocking inequality is
\[
m(1-p)q^k>p(m-k)
\quad\Longleftrightarrow\quad
p<\theta_k:=\frac{m q^k}{m-k+m q^k}.
\]
Only finitely many subsets occur at fixed \(m\). Therefore, away from the largest of the \(\theta_k\), the candidate is eventually blocked or unblocked with probability tending to one. Indeed, the bounded independent summands defining each finite inequality give exponentially small opposite-tail probabilities by Hoeffding's inequality; a union bound over at most \(2^{m-1}\) subsets proves the claimed exponential convergence.

**3. The two extreme coalition types.** Because \(u\mapsto u/(1+u)\) is strictly increasing, maximizing \(\theta_k\) is equivalent to maximizing \(q^k/(m-k)\). On the real interval \([0,m-1]\),
\[
f(x)=x\log q-\log(m-x),\qquad f''(x)=\frac{1}{(m-x)^2}>0.
\]
Strict convexity forces the maximum over the integer grid to occur at \(k=0\) or \(k=m-1\), and every interior value is strictly smaller than the greater endpoint value. The endpoint values are \(1/m\) and \(q^{m-1}\), equal precisely when \(q=m^{-1/(m-1)}\). This proves the asserted \(p_*\), identifies the two possibly active coalitions, and proves that away from \(q_c\) only one subset size is asymptotically tight on the boundary.

**4. Single-front boundary.** If \(p=p_*\) and \(q\ne q_c\), the sole active subset has either size \(0\) or size \(m-1\). Its centered finite inequality is a sum of independent bounded, nondegenerate, mean-zero variables, while all other subset tests have strictly negative normalized means. The one-dimensional central limit theorem and continuity of the limiting normal distribution give survival probability \(1/2\), including either equality convention.

**5. Double-front boundary.** Let \(p=1/2\) and \(q=q_c\). For each voter define \(Y=1\) if she approves \(c\), and \(Z=1\) if she disapproves \(c\) and approves all the other \(m-1\) candidates. Then
\[
\Pr(Y=1)=\frac12,\quad \Pr(Z=1)=\frac{1}{2m},\quad YZ=0.
\]
The two asymptotically active nonblocking inequalities become
\[
\sum_{i=1}^n\left(Y_i-\frac12\right)\ge0,
\qquad
\sum_{i=1}^n(Y_i-mZ_i)\ge0.
\]
Set \(U=Y-1/2\) and \(V=Y-mZ\). Directly,
\[
\operatorname{Var}(U)=\frac14,\quad
\operatorname{Var}(V)=\frac{m+1}{2},\quad
\operatorname{Cov}(U,V)=\frac12,
\quad\rho=\sqrt{\frac{2}{m+1}}.
\]
The multivariate central limit theorem gives a centered bivariate normal with correlation \(\rho\). For such a normal, the first-quadrant probability equals \(1/4+\arcsin(\rho)/(2\pi)\), as seen by expressing independent standard normals in polar coordinates and measuring the angular intersection of two half-planes. The remaining \(k=1,\dots,m-2\) blocking tests have strictly negative limiting margins by step 3, hence vanish in probability; for \(m=2\) there are no intermediate tests. This completes the formula. For \(m=3\), \(\rho=1/\sqrt2\) and \(\arcsin(\rho)=\pi/4\), giving \(3/8\).

## Verification

The accompanying standalone `PROOF_CHECK.py` independently implements (a) the literal coalition definition and (b) the subset reduction. Their results agree on all \(40,960\) approval profiles in the tested ranges \((m,n)=(3,4),(3,5),(4,3)\). A separate grid of \(5,771\) \((m,q)\) pairs checks the endpoint maximization identity. A seeded multinomial check of the double-critical bivariate limit at \(m=3,4,6\), with \(30,000\) trials each and \(n=4,000\), reproduces the predicted values to finite-sample accuracy. The analytic arguments above, rather than these finite tests, establish the theorem for all stated \(n\)-limits and parameter values.

Reproduce with `python3 PROOF_CHECK.py`; NumPy is optional and used only for the Monte Carlo supplement. The exact profile and convexity-grid checks require only the standard library.

## Relationship to prior work

Dong, Kraiczy, Vasishta, Brill, Holliday and Boehmer introduce AWVC in arXiv:2609.10759 (Definition 8), prove its deterministic approval threshold and minority-veto envelope (Theorem 4), and conduct empirical analyses. The present result keeps their exact solution concept but studies a specified independent approval culture, deriving a sharp probabilistic survival boundary and a nontrivial simultaneous-critical Gaussian quadrant law. These probabilistic statements do not follow from the deterministic approval threshold alone, since coherent disapprovers can veto candidates with majority support.

Ianovski and Kondratev study the *proportional veto core without an approval gate* and derive its expected size under independent uniform strict rankings (arXiv:2003.09153, Proposition 7); the rule and stochastic input differ, so that proposition does not imply this AWVC phase diagram. Lackner and Maly study approval-only shortlisting rules, including threshold and gap procedures, but not this approval-weighted coalition-veto definition. A general law of large numbers and a bivariate Gaussian quadrant identity are established tools; the new content is their exact application to the AWVC blocking geometry and its two-front critical coincidence.

## Limitations

This is an asymptotic fixed-number-of-candidates theorem under independent, exchangeable rival approval bits and binary utilities; correlated approvals, heterogeneous rival probabilities, continuously varying utilities, growing candidate sets and the disapproval-Smith composition are not covered. The exact finite reduction remains valid for all binary profiles. The normal-limit statements do not give exact finite-electorate probabilities, and numerical checks do not replace the analytic proof. A specialized equivalent in unindexed or incompletely inspected literature cannot be excluded. Independent mathematical evaluation remains outstanding.

## References

1. C. Dong, S. Kraiczy, R. Vasishta, M. Brill, W. H. Holliday, and N. Boehmer, *Where Should Society Draw the Line? A Social Choice Approach to Collective Consent*, arXiv:2609.10759, first submitted September 9, 2026, https://arxiv.org/abs/2609.10759.
2. E. Ianovski and A. Y. Kondratev, *Computing the proportional veto core*, arXiv:2003.09153 (first submitted March 20, 2020), https://arxiv.org/html/2003.09153v4.
3. M. Lackner and J. Maly, *Approval-based shortlisting*, Social Choice and Welfare 64 (2025), 97–142, first published August 11, 2023, https://doi.org/10.1007/s00355-023-01482-2.
