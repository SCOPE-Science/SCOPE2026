# Distinct optimal innovation rates for Shannon and Simpson diversity under a permanent cultural fitness advantage

## Finding

In the precisely defined novelty-influx copying model below, for every incumbent fitness factor \(a>1\) the limiting Hill effective diversities of orders one and two have **different unique global maximizing innovation fractions** \(\varepsilon_1\) and \(\varepsilon_2\). They satisfy

\[
0<\varepsilon_2=\frac{a^2-1}{2a^2}<\varepsilon_1=\frac{1}{a/(a-1)+a^{-1/(a-1)}}<\varepsilon_c=1-\frac1a<1.
\]

Their respective maxima are

\[
\max_{0<\varepsilon<1} N_1=1+\frac{a}{a-1}a^{1/(a-1)},\qquad
\max_{0<\varepsilon<1} N_2=\frac{2a}{a-1}.
\]

For \(a=2\), the exact maximizing rates are \(\varepsilon_2=3/8\) and \(\varepsilon_1=2/5\), with maximal effective diversities four and five respectively, while the incumbent disappears at the larger threshold \(\varepsilon_c=1/2\). Thus an innovation increase in the interval \((3/8,2/5)\) *raises Shannon effective diversity but lowers Simpson effective diversity* even though each step creates a previously absent type. Both effective diversities decline strictly above the incumbent's persistence threshold.

## Assumptions and scope

The state at integer time \(t\geq0\) is a probability vector on one permanent incumbent type \(0\) and previously introduced types \(1,\ldots,t\). Initially \(p_{0,0}=1\). The incumbent has fixed fitness \(a>1\), all newcomer types have fitness one, and a fixed \(\varepsilon\in(0,1)\) fraction of the next population is assigned to **one brand-new uniquely labeled type**. All remaining mass undergoes deterministic, normalized fitness-weighted copying:

\[
Z_t=1+(a-1)p_{t,0},\quad p_{t+1,0}=\frac{(1-\varepsilon)a p_{t,0}}{Z_t},\quad
p_{t+1,j}=\frac{(1-\varepsilon)p_{t,j}}{Z_t}\ (1\le j\le t),\quad p_{t+1,t+1}=\varepsilon.
\]

There is no finite-population sampling noise, forgetting other than relative frequency change, returning mutations, variable fitness, interaction network or demographic feedback. The original labels change with time; the limiting law below is expressed in **age coordinates**: incumbent plus immigrant introduced \(k\) steps previously, with \(k=0,1,\ldots\). Define Shannon entropy using natural logarithms, \(H=-\sum_j p_j\log p_j\) with \(0\log0:=0\), Hill order-one diversity \(N_1=e^H\), and Hill order-two diversity \(N_2=(\sum_jp_j^2)^{-1}\). Limits \(t\to\infty\) are taken with \(a,\varepsilon\) fixed, before optimizing over \(\varepsilon\).

## Proof

**1. Incumbent persistence.** Put \(x_t=p_{t,0}\) and \(c=a(1-\varepsilon)\). Then

\[
x_{t+1}=\frac{cx_t}{1+(a-1)x_t},\qquad
x_{t+1}^{-1}=c^{-1}\left(x_t^{-1}+a-1\right).
\]

This exact affine reciprocal recurrence gives

\[
\lim_{t\to\infty}x_t=x_*=
\begin{cases}1-\dfrac{a\varepsilon}{a-1},&0<\varepsilon<\varepsilon_c,\\0,&\varepsilon_c\le\varepsilon<1,\end{cases}
\qquad\varepsilon_c=1-\frac1a.
\]

At equality \(\varepsilon=\varepsilon_c\), \(x_t=1/[1+(a-1)t]\), so the boundary is included. Above it, \(x_t\) decays geometrically.

**2. Newcomer age law.** A type introduced \(k\) steps before time \(t\) has mass

\[
\varepsilon\prod_{s=t-k}^{t-1}\frac{1-\varepsilon}{1+(a-1)x_s}.
\]

The factor converges to \(r_*=1/a\) if \(\varepsilon<\varepsilon_c\), or \(r_*=1-\varepsilon\) otherwise. Each finite-age mass converges to \(u_k=\varepsilon r_*^k\). Every copying factor is at most \(1-\varepsilon\), hence \(0\le u_{t,k}\le\varepsilon(1-\varepsilon)^k\). Dominated convergence for the summable age envelope establishes convergence in \(\ell^1\), together with incumbent mass, and permits passage to squared-mass sums and entropy, the latter by the summable geometric bound on \(-u\log u\) for small \(u\). Indeed \(x_*+\sum_{k\ge0}u_k=1\).

**3. Exact limiting diversity.** Write \(\kappa=a/(a-1)\), \(d=\log(a)/(a-1)\), \(C=1/N_2\). Summing the geometric-age series gives, for \(0<\varepsilon<\varepsilon_c\),

\[
H=-x_*\log x_*-\kappa\varepsilon\log\varepsilon+\kappa\varepsilon d,
\qquad
C=x_*^2+\frac{\varepsilon^2}{1-a^{-2}},\qquad x_*=1-\kappa\varepsilon.
\]

For \(\varepsilon_c\le\varepsilon<1\), the formulas become

\[
H=-\log\varepsilon-\frac{1-\varepsilon}{\varepsilon}\log(1-\varepsilon),
\qquad C=\frac{\varepsilon}{2-\varepsilon}.
\]

The two pieces agree continuously at the critical value. For the first piece,

\[
H'=\kappa\left(\log\frac{x_*}{\varepsilon}+d\right),\qquad
H''=-\kappa\left(\frac{\kappa}{x_*}+\frac1\varepsilon\right)<0.
\]

Consequently the sole Shannon maximizer occurs where \(x_*/\varepsilon=a^{-1/(a-1)}\), giving \(\varepsilon_1\) and \(e^{H(\varepsilon_1)}=1+\kappa e^d\). Moreover \(C\) is a strictly convex quadratic on this region, with its sole minimum at \(\varepsilon_2=(a^2-1)/(2a^2)\), where \(C=(a-1)/(2a)\). Both candidates lie strictly below \(\varepsilon_c\).

For the second piece, \(H'=\log(1-\varepsilon)/\varepsilon^2<0\) and \(C'=2/(2-\varepsilon)^2>0\). Hence the earlier critical points are global. Finally, at \(\varepsilon_2\), \(x_*/\varepsilon_2=a/(a+1)\), and

\[
H'(\varepsilon_2)=\kappa\left[\frac{\log a}{a-1}-\log\left(1+\frac1a\right)\right]>0
\]

because \(\log a>(a-1)/a\) and \(\log(1+1/a)<1/a\) for \(a>1\). Since \(H\) is strictly concave before its unique maximum, \(\varepsilon_2<\varepsilon_1\). This proves the complete strict ordering and all maximum formulas.

## Verification

Run `python verify.py` using the Python standard library. It performs 128 exact-fraction, analytic-formula, and finite-time checks, including independent dynamical iterations over seven fitness factors and five innovation multipliers. In particular it certifies the rational \(a=2\) values without floating-point error. The unrestricted parameter and infinite-age conclusions above are proved analytically; finite-time tests alone would not establish them.

## Relationship to prior work

McBride and Leroi (2026) report that new cultural variants sustain and increase musical repertoire entropy despite selection, and use frequency-weighted per-tune copying, but their published birth-process model does not explicitly model novelty inception or derive infinite-age effective-diversity optima [1, particularly Results/Discussion and Methods]. The novelty-influx step here is a separate simplified mathematical assumption, not a fitted version of their empirical model. Kandler and Laland (2009) examine cultural innovation and several diversity indices in an ecological model; they numerically find that higher innovation generally raises ensemble diversity over their investigated innovation range rather than analyzing this permanent-fitness, one-new-variant-per-step mechanism [2, Sections 3 and Appendix B]. Standard single-peak quasispecies/error-threshold work explains the incumbent persistence boundary in related models but does not establish the separate Hill-order optimizing innovation rates for this age-labeled copying model [3]. The claim is confined to the explicit combination proved above, not the geometric-series identities, general Hill indices, or single-peak error threshold in isolation.

## Limitations

This is an idealized deterministic infinite-population benchmark. In particular, a fixed share of population devoted to one new type **every** period differs from a probability of independent invention or a fitted empirical arrival process. Newly created types are assumed permanently less fit than the incumbent; there are no multiple favored variants, type interactions, finite sample correction or finite horizon optimality statements. Fixed labels do not converge coordinatewise to the moving age law: convergence is only in incumbent-plus-relative-age coordinates. The theorem does not assert monotonic diversity growth over time, empirical predictive accuracy, or applicability to arbitrary mutation-selection models. Distinct metric optima may have broader analogues in existing literature.

## References

[1] J. M. McBride and A. M. Leroi, *Population Ecology of Tunes*, arXiv:2609.09501, first posted 2026-09-08. https://arxiv.org/pdf/2609.09501

[2] A. Kandler and K. N. Laland, *An investigation of the relationship between innovation and cultural diversity*, Theoretical Population Biology **76** (2009), 59–67, doi:10.1016/j.tpb.2009.04.004. https://lalandlab.wp.st-andrews.ac.uk/files/2015/08/Publication140.pdf

[3] C. O. Wilke, *Quasispecies theory in the context of population genetics*, BMC Evolutionary Biology **5** (2005), 44, doi:10.1186/1471-2148-5-44. https://link.springer.com/article/10.1186/1471-2148-5-44
