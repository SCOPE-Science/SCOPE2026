# A sharp source–sink establishment reversal under symmetric dispersal

## Finding
Consider a two-patch, discrete-generation, density-independent Poisson branching population with source mean \(r>1\), sink mean \(0<s<1\), and symmetric offspring dispersal probability \(d\in[0,1]\). If a single founder starts in either patch with probability \(1/2\), its permanent lineage-establishment probability is \(S(d)\). Let \(q\in(0,1)\) be the unique nonunit solution of \(q=e^{r(q-1)}\).

The exact first-order response at zero dispersal is
\[
S'(0+)=\frac{(1-q)(s-rq)}{2(1-s)(1-rq)}.
\]
Thus low dispersal improves uniformly averaged founding success exactly when \(s>rq\), despite the fact that the Perron population-growth factor strictly decreases for every increment of dispersal. Moreover, whenever
\[
 rq<s<\frac1r,
\]
there exists a unique critical dispersal \(d_c=(r-1)(1-s)/(r+s-2rs)\in(0,1)\); establishment is possible for \(0\le d<d_c\), but extinction is certain for \(d_c\le d\le1\). Hence \(S\) attains its maximum at an interior dispersal probability. This paradoxical parameter interval is nonempty for **every** \(r>1\).

As an exact illustrative case, take \(r=4\log(4)/3\) and \(s=1/2\). Then \(q=1/4\), \(S(0)=3/8\),
\[
S'(0+)=\frac38\frac{3-2\log4}{3-\log4}>0,
\qquad d_c=\frac43\log4-1.
\]

## Assumptions and scope
Each parent in habitat 1 (respectively habitat 2) independently produces a Poisson number of offspring with mean \(r\) (respectively \(s\)); each newborn independently emigrates to the opposite patch with probability \(d\), after reproduction and without dispersal mortality. The parents then die. No density regulation, environmental randomness, evolution, or demographic feedback is present. A founder is selected uniformly from the *two patches*, not proportionally to existing patch abundance. Permanent establishment means nonextinction of the founder's branching lineage; it is not a claim about positive carrying-capacity equilibria.

Write \(Q_i(d)\) for the probability of eventual extinction conditional on a single patch-\(i\) founder; \(S(d)=1-(Q_1(d)+Q_2(d))/2\). At \(d=0\), only the source can persist and \((Q_1,Q_2)=(q,1)\). The result concerns the least nonnegative solution to the extinction fixed-point equations, not the always-existing trivial solution \((1,1)\).

## Proof
**Step 1: extinction equations.** Poisson thinning gives independent Poisson offspring counts sent from patch \(i\) to each destination. Their bivariate probability-generating functions imply
\[
Q_1=e^{r((1-d)Q_1+dQ_2-1)},\qquad
Q_2=e^{s(dQ_1+(1-d)Q_2-1)}.
\]
For \(r>1\), scalar Poisson branching has a unique smaller extinction root \(q\in(0,1)\), and \(rq<1\). The latter follows because \(e^{r(t-1)}-t\) crosses zero with negative derivative at its smaller root (equivalently, the nontrivial extinction fixed point is attracting).

**Step 2: exact first-order establishment criterion.** Define residuals by moving each generating-function expression to the left. At \(d=0\), their Jacobian with respect to \((Q_1,Q_2)\) is diagonal with entries \(1-rq>0\) and \(1-s>0\). The implicit-function theorem therefore supplies the local extinction branch, and differentiation yields
\[
Q_1'(0+)=\frac{rq(1-q)}{1-rq},\qquad
Q_2'(0+)=-\frac{s(1-q)}{1-s}.
\]
The nearby branch is the *physical* extinction solution: for every sufficiently small positive \(d\), the descendants remaining in the source alone form a supercritical Poisson process of mean \(r(1-d)>1\). Therefore \(Q_1(d)\) is uniformly bounded away from one as \(d\downarrow0\). Any accumulation point of the minimal extinction solution solves the zero-dispersal equations, and the only such solution with first component below one is \((q,1)\). Continuity and local uniqueness of the implicit branch therefore identify it with the actual extinction probabilities. Consequently
\[
S'(0+)=-\tfrac12(Q_1'(0+)+Q_2'(0+))
=\frac{(1-q)(s-rq)}{2(1-s)(1-rq)}.
\]
Its denominator is positive, giving the necessary-and-sufficient sign test, including the zero-derivative boundary \(s=rq\).

**Step 3: growth decreases at every dispersal intensity.** The mean progeny matrix and its spectral radius are
\[
M(d)=\begin{pmatrix}r(1-d)&rd\\sd&s(1-d)\end{pmatrix},
\qquad
\rho(d)=\frac{(r+s)(1-d)+\sqrt{(r-s)^2(1-d)^2+4rsd^2}}2.
\]
Let \(v(d)=((r-s)(1-d),2\sqrt{rs}\,d)\). Then \(2\rho'(d)=-(r+s)+\langle v(d),v'(d)\rangle/\|v(d)\|\). By strict Cauchy–Schwarz,
\[
\langle v,v'\rangle/\|v\|<\|v'\|=\sqrt{(r-s)^2+4rs}=r+s
\]
for all \(d\in[0,1]\): because \(r>s>0\), the vectors \(v(d)\) and \(v'(d)\) are never positively collinear. Hence \(\rho'(d)<0\), with \(\rho(0)=r\) and \(\rho(1)=\sqrt{rs}\).

**Step 4: sharp global extinction cutoff.** If \(rs<1\), strict monotonicity yields a unique \(d_c\in(0,1)\) with \(\rho(d_c)=1\). The characteristic equation \(\det(I-M(d_c))=0\) reduces to
\[
(1-r)(1-s)+d_c(r+s-2rs)=0,
\qquad d_c=\frac{(r-1)(1-s)}{r+s-2rs}.
\]
For \(0<d<1\), the two-type branching process is irreducible and has positive probability of zero offspring, so its total lineage survives with positive probability exactly when \(\rho(d)>1\). At the critical value it dies out almost surely. At \(d=1\), two-generation progeny expectations have factor \(rs<1\), giving almost-sure extinction. At \(d=0\), source founders survive with probability \(1-q\). Continuity at the critical threshold follows by passing limits through the generating-function equations and using uniqueness of the critical fixed point \((1,1)\). Thus \(S(d)>0\) for \(0\le d<d_c\) and \(S(d)=0\) for \(d\ge d_c\). If \(S'(0+)>0\), compactness and continuity force at least one maximizer strictly between zero and \(d_c\).

**Step 5: the beneficial-then-fatal band always exists.** For any \(r>1\), define \(h(r)=r-r^{-1}-2\log r\). We have \(h(1)=0\) and \(h'(r)=(r-1)^2/r^2>0\). Consequently
\[
e^{r(r^{-2}-1)}=e^{r^{-1}-r}<r^{-2}.
\]
The convex function \(e^{r(t-1)}-t\) is negative precisely between its two zeros \(q\) and \(1\). Because \(r^{-2}<1\), the inequality implies \(q<r^{-2}\), hence \(rq<1/r\). Any \(s\) in the nonempty interval \((rq,1/r)\) satisfies simultaneously the initial establishment-benefit condition and the global-collapse condition \(rs<1\).

For the displayed exact example, \(q=1/4\) follows by substitution in \(q=e^{r(q-1)}\). The inequalities \(rq<s\) and \(rs<1\) both follow from \(\log4<3/2\), so all conclusions apply without rounding.

## Verification
The accompanying standalone `verify.py` implements least-fixed-point iteration for extinction probabilities, computes the eigenvalue directly, checks the exact example, and samples seven source strengths with sink strengths inside the proved parameter band. On execution it reports \(r\approx1.84839248149\), \(S(0)=0.375\), \(S(0.01)\approx0.375415222956\), \(S'(0+)\approx0.0528468309866\), and \(d_c\approx0.848392481493\). These computations test the formulas; all universal assertions and the nonempty interval are established algebraically above.

## Relationship to prior work
Bansaye and Lambert, *Past, growth and persistence of source-sink metapopulations* (arXiv:1111.2535v1, 2011), study precisely the reproduction-then-dispersal source–sink lifecycle and derive persistence and growth criteria in broader branching models, including two patches. Their analysis supplies the population framework and general persistence principles. The contribution here is the exact **uniform-founder extinction-probability derivative**, its sharp sign condition \(s>rq\), and the explicit nonempty region where founder success initially increases while growth strictly decreases and eventual high-dispersal extinction follows; their displayed results do not present that combined comparison.

Tomasini and Peischl, *Establishment of Locally Adapted Mutations Under Divergent Selection* (2018), and Czuppon et al., *The Effect of Habitat Choice on Evolutionary Rescue in Subdivided Populations* (2021), study two-type branching establishment and already report nonmonotone effects of migration on establishment probabilities. These **qualitative effects and the general Poisson fixed-point approach are not claimed as new**. Their migration/selection life cycles and establishment objectives differ from the present patch-reproduction-then-offspring-dispersal model. The new statement is the exact all-strength sign threshold and nonempty rescue-then-collapse interval for uniformly located founders, alongside globally decreasing expected growth. Unnoticed equivalent specializations of branching theory remain a literature risk.

## Limitations
This is a two-patch density-independent Poisson model; the claims do not transfer without proof to other offspring laws, biased founder distributions, asymmetric dispersal, pre-reproduction migration, density regulation, or stochastic environmental forcing. The theorem proves existence of an interior maximizer, not uniqueness or an explicit maximizing dispersal rate. The full shape of \(S(d)\) between its endpoints is not classified. Persistence means a positive probability of unlimited lineage growth, not deterministic establishment in every realization. General branching-process fixed-point equations are classical; the originality assessment specifically concerns the joint sharp criterion and global contrast, and a completely exhaustive literature survey is not asserted.

## References
1. Vincent Bansaye and Amaury Lambert, *Past, growth and persistence of source-sink metapopulations*, arXiv:1111.2535v1 (public 2011-11-10), https://arxiv.org/abs/1111.2535 .
2. Matteo Tomasini and Stephan Peischl, *Establishment of Locally Adapted Mutations Under Divergent Selection*, Genetics 209 (2018), 885–895, https://doi.org/10.1534/genetics.118.301104 .
3. Peter Czuppon, François Blanquart, Hildegard Uecker, and Florence Débarre, *The Effect of Habitat Choice on Evolutionary Rescue in Subdivided Populations*, American Naturalist 197 (2021), 625–643, https://doi.org/10.1086/714034 .
