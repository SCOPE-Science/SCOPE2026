# Third-moment ordering of volunteer equilibria across four group sizes, with a five-size obstruction

## Finding

In the random-group, one-volunteer public-good game, the mean and variance of the group size need not determine the equilibrium volunteering fraction. Nevertheless, **on any prescribed set of at most four possible group sizes, with all sizes at least two, the third raw group-size moment completely orders every interior volunteering equilibrium among laws with identical first two moments**. Specifically, if two distinct laws \(P,Q\) on four prescribed sizes have the same mean and variance and \(\mathbb E_Q[N^3]>\mathbb E_P[N^3]\), then their unique interior replicator equilibria satisfy \(x_Q^*<x_P^*\) for every benefit \(B>0\) and volunteering cost \(0<C<B\). Their payoff advantages are strictly ordered in the same direction at every frequency \(0<x<1\).

The support threshold is sharp in two distinct senses. On at most three prescribed group sizes, the first two moments already determine the law. On five prescribed sizes, even the first three raw moments can coincide for two strictly positive probability laws whose volunteering equilibria differ; thus the third moment no longer determines the equilibrium. The four-class ordering is an exact, all-parameter statement rather than a small-variation approximation.

## Assumptions and scope

Let \(N\) be a random integer with an exogenously fixed *focal-player* group-size law \(p_n=\Pr(N=n)\), supported on a finite set of integers \(n\ge2\). The focal law, rather than the distribution of physical group counts, is specified so that no size-bias convention is left implicit. In each interaction, each of the other \(N-1\) players independently volunteers with probability \(x\in[0,1]\), independent of \(N\). A single volunteer suffices to deliver benefit \(B>0\) to every group member, and volunteering costs its actor \(C\), where \(0<C<B\). Volunteering and non-volunteering frequencies evolve by standard two-strategy replicator dynamics, without assortment or mutation.

Write
\[
G_p(q)=\sum_n p_n q^{n-1},\quad q\in[0,1],\qquad
\dot x=x(1-x)\bigl(BG_p(1-x)-C\bigr).
\]
The *raw* third moment is \(m_3(p)=\sum_n p_n n^3\). Under a common mean, ordering raw third moments is equivalent to ordering third central moments (skewness numerators). Comparisons use two laws supported on one common set of at most four prescribed integer sizes, allowing zero mass at some of those sizes.

## Proof

**1. Selection gradient and unique equilibrium.** A non-volunteer gets the public good unless at least one other member volunteers. A volunteer gets that benefit in either case and pays \(C\). Thus the payoff difference (volunteer minus non-volunteer), conditional on \(N=n\), is \(B(1-x)^{n-1}-C\), giving the stated replicator equation after averaging over \(p\). Because \(n\ge2\), \(G_p\) is continuous and strictly increasing on \([0,1]\), with \(G_p(0)=0\) and \(G_p(1)=1\). Therefore there is exactly one \(q_p^*\in(0,1)\) solving \(G_p(q_p^*)=C/B\); its associated \(x_p^*=1-q_p^*\) attracts all initial \(x\in(0,1)\).

**2. The four-support moment fiber.** Fix four distinct integers \(2\le n_1<n_2<n_3<n_4\). Put
\[
w_i=\left(\prod_{j\ne i}(n_i-n_j)\right)^{-1}.
\]
The coefficient of the cubic term in the Lagrange interpolation polynomial for \(t^k\), \(k=0,1,2,3\), yields
\[
\sum_{i=1}^4w_i n_i^k=0\ (k=0,1,2),\qquad
\sum_{i=1}^4w_i n_i^3=1.
\]
If \(P,Q\) have equal zeroth, first and second moments on these nodes, the difference of their weight vectors belongs to the one-dimensional nullspace of the rank-three Vandermonde matrix. Consequently,
\[
Q(n_i)-P(n_i)=\bigl(m_3(Q)-m_3(P)\bigr)w_i.
\]
For \(0<q<1\), define \(f_q(t)=q^{t-1}\). The quantity
\[
\sum_{i=1}^4 w_i f_q(n_i)
\]
is the leading cubic coefficient of the Lagrange polynomial interpolating \(f_q\) at the four nodes. The difference between this polynomial and \(f_q\) vanishes at four points. Three applications of Rolle's theorem produce some \(\xi\in(n_1,n_4)\) for which this coefficient is \(f_q'''(\xi)/6\). Since
\[
f_q'''(\xi)=(\log q)^3q^{\xi-1}<0,
\]
we have the *strict all-frequency sign identity*
\[
\operatorname{sgn}(G_Q(q)-G_P(q))
=-\operatorname{sgn}\bigl(m_3(Q)-m_3(P)\bigr)
\quad(0<q<1).
\]
If \(m_3(Q)>m_3(P)\), then \(G_Q<G_P\) throughout the interior, so the unique crossing of the horizontal line \(C/B\) occurs at \(q_Q^*>q_P^*\), giving \(x_Q^*<x_P^*\). The strict selection-gradient comparison follows by multiplying the generating-function inequality by \(B>0\). For at most three support nodes, the zeroth-to-second Vandermonde matrix has full column rank, proving identical moments imply identical laws.

**3. Exact four-size example.** On sizes \((2,3,4,5)\), let
\[
P=(7,3,9,5)/24,\qquad Q=(5,9,3,7)/24.
\]
Both have mean \(7/2\) and variance \(5/4\), while \(m_3(P)=223/4<m_3(Q)=225/4\). Directly,
\[
G_P(1/2)=91/384>15/64>89/384=G_Q(1/2).
\]
For \(C/B=15/64\), therefore, \(x_P^*>1/2>x_Q^*\), although the laws have the same mean and variance. All eight displayed masses are strictly positive.

**4. Sharp five-size obstruction.** On sizes \((2,3,4,5,6)\), let
\[
U=(9,4,14,4,9)/40,\qquad V=(7,12,2,12,7)/40.
\]
Both are strictly positive probability vectors, with exactly equal zeroth through third raw moments, respectively \(1,4,18,88\). Their generating functions satisfy
\[
G_U(q)-G_V(q)=\frac1{20}q(1-q)^4>0\qquad(0<q<1).
\]
At \(q=1/2\), these values are \(249/1280\) and \(247/1280\), respectively. Taking \(C/B=31/160\) gives \(x_U^*>1/2>x_V^*\), despite matching the first three raw moments. Four or fewer possible sizes cannot exhibit this obstruction because equality of the zeroth through third moments uniquely determines their weights by Vandermonde invertibility.

## Verification

The standalone `check.py` uses exact rational arithmetic. It checks the interpolation identities and strict generating-function comparison on all \(210\) four-element subsets of sizes \(2,\ldots,11\), at four rational arguments apiece with strictly positive constructed moment-matched laws, as well as every moment and generating-function identity in both examples. Execution completed with `PASS: 2330 exact-rational assertions; 210 ordered four-size support choices; two explicit sharp examples.` These finite checks are corroborative only; the universal statement is established analytically by the interpolation/Rolle argument.

To reproduce, run `python check.py` from the directory containing this document and the script. Python's standard library is the only dependency.

## Relationship to prior work

Diekmann's original volunteer's dilemma analyzes the fixed-size collective-action model. Peña (first online 2011) develops replicator dynamics with random group sizes and identifies mean/variance effects by Jensen's inequality, including the one-volunteer case and a generating-function formulation. Brännström, Gross, Blasius and Dieckmann (first preprint 2010) establish general effects of group-size fluctuations for evolutionary cooperation games with continuous investments. These models, selection equations and Jensen comparisons are not claimed as new. The result here isolates a different, exact **moment-matched** comparison: an all-cost-ratio third-moment ordering for four arbitrarily spaced allowed group sizes and a five-size failure even after matching the third moment. Jensen comparison against a deterministic law with the same mean alone does not provide this strict comparison of laws having identical mean and variance.

## Limitations

The theorem is conditional on a fixed focal-player group-size distribution with at most four prescribed sizes; it does not say that larger arbitrary supports are ordered by skewness. The five-class obstruction is a rigorous counterexample to sufficiency, not a classification of all five-class distributions. The equilibrium is an idealized deterministic well-mixed replicator prediction; sampling uncertainty, group-size bias, variable benefits and costs, assortment, finite-population fixation and real-world behavioral effects are not addressed. The divided-difference ingredient is classical, and unlocated specialized literature could contain this application; historical priority has not been independently established.

## References

1. Diekmann, A. (1985), “Volunteer's Dilemma”, *Journal of Conflict Resolution* 29(4), 605–610. https://doi.org/10.1177/0022002785029004003
2. Peña, J. (first online November 4, 2011; issue 2012), “Group-size diversity in public goods games”, *Evolution* 66(3), 623–636. https://doi.org/10.1111/j.1558-5646.2011.01504.x
3. Brännström, Å., Gross, T., Blasius, B., Dieckmann, U. (preprint October 26, 2010), “Consequences of fluctuating group size for the evolution of cooperation”. https://arxiv.org/abs/1010.5478
