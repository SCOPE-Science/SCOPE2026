# Six is the sharp group-size threshold for two stable interior states in a two-project volunteer game

## Finding
In a well-mixed, one-shot, two-strategy volunteer game, suppose one volunteer pays a constant cost \(c>0\) and her contribution simultaneously counts toward two shared public goods. The goods have strictly interior distinct thresholds \(2\le k_1<k_2\le N-1\) and positive rewards \(b_1,b_2\) for *every* group member once their thresholds are met. With random groups of size \(N\), no assortment, and infinite-population replicator dynamics, the following group-size bound is sharp:

**Theorem.** If \(N\le5\), every such game has at most two distinct interior equilibrium frequencies and at most one asymptotically stable interior equilibrium. At \(N=6\), the two projects with thresholds \(k_1=2\), \(k_2=5\), and equal positive reward \(b_1=b_2=b\) have **exactly four distinct interior equilibria, exactly two locally asymptotically stable**, if and only if
\[
\frac{5b}{16}<c<\frac{5b}{12}.
\]
At the explicit cost \(c=b/3\), the four distinct roots are
\[
x=\frac12\pm\sqrt{\frac{5-2\sqrt5}{60}},\qquad
x=\frac12\pm\sqrt{\frac{5+2\sqrt5}{60}}.
\]
When arranged in increasing order, the second and fourth roots are stable and the first and third are unstable. This is the first group size at which *two stable interior volunteer frequencies* can coexist under these two strictly interior positive threshold rewards and a shared constant contribution cost.

## Assumptions and scope
An infinitely large population mixes randomly into temporary groups of integer size \(N\ge2\), with two heritable pure types, volunteer (V) and nonvolunteer (D), and no relatedness, repeated play, mutation, or demographic stochasticity. The population frequency of V is \(x\in[0,1]\). The two nonexcludable goods pay \(b_1,b_2>0\) per individual whenever the total number of V players meets thresholds \(k_1,k_2\), respectively. A V player always pays \(c>0\), independently of whether any threshold is met; a D player does not. The same contribution counts for both goods. Throughout, thresholds are distinct and strictly interior, \(2\le k_1<k_2\le N-1\); there are no admissible pairs for \(N\le3\). The payoff-difference function is \(G(x)=\pi_V(x)-\pi_D(x)\), and the standard replicator equation is \(\dot x=x(1-x)G(x)\). Stability is relative to the scalar dynamics on \([0,1]\), and "interior" means \(0<x<1\).

## Proof
**1. Exact gain from volunteering.** Let \(J\sim\operatorname{Bin}(N-1,x)\) be the number of other volunteers. The focal volunteer rather than nonvolunteer crosses threshold \(k_i\) precisely when \(J=k_i-1\). Thus, with \(F=G+c\),
\[
F(x)=\sum_{i=1}^2b_i\binom{N-1}{k_i-1}x^{k_i-1}(1-x)^{N-k_i},\quad G(x)=F(x)-c.
\]
Because neither threshold is one or unanimity, \(F(0)=F(1)=0\), and hence \(G(0)=G(1)=-c<0\). This fact also determines the signs on both sides of any simple interior root.

**2. Group sizes through four.** For \(N\le4\), the degree of \(G\) is at most three. A real polynomial of degree at most three that is strictly negative at both ends of \([0,1]\) cannot have three distinct roots in \((0,1)\): three distinct roots of a cubic must all be simple and would reverse the endpoint sign. Hence at most two distinct interior rest points occur, and at most one can be attracting (the scalar vector field starts and ends negative).

**3. The five-member obstruction.** Write \(t=x/(1-x)>0\). Multiplying \(G(x)\) by \((1+t)^4\) yields a real polynomial in \(t\) whose degree-four coefficients (in ascending order) are \(\binom4j(b_1\mathbf1_{j=k_1-1}+b_2\mathbf1_{j=k_2-1}-c)\), \(j=0,\ldots,4\). The endpoints \(j=0,4\) are negative. There are at most two positive coefficient locations. Unless they are exactly \(j=1,3\), the nonzero coefficient sequence has at most two sign changes. Descartes' rule, counting multiplicities, then permits at most two positive roots \(t\), hence two interior frequencies \(x\).

The only potentially four-change pattern is \((k_1,k_2)=(2,4)\). Here set \(A=4b_1>0\), \(B=4b_2>0\). An exact substitution gives
\[
F=\frac{At+Bt^3}{(1+t)^4},\qquad
\frac{dF}{dt}=\frac{Q(t)}{(1+t)^5},\quad
Q(t)=A-3At+3Bt^2-Bt^3.
\]
The cubic has discriminant
\[
\operatorname{disc}(Q)=-108AB(A-B)^2\le0.
\]
If \(A\ne B\), it has precisely one real zero, which is positive because \(Q(0)=A>0\) and \(Q(t)\to-\infty\). If \(A=B\), then \(Q=A(1-t)^3\), also with one positive zero. Consequently \(F\) strictly increases and then strictly decreases on the positive \(t\)-axis and can meet the level \(c>0\) at most twice. This disposes of the exceptional sign pattern, completing the \(N\le5\) bound.

**4. A six-member two-project witness.** Put \(k_1=2\), \(k_2=5\), and \(b_1=b_2=b>0\). The pivotal expression simplifies to
\[
F(x)=5b[x(1-x)^4+x^4(1-x)]
=b\left(\frac5{16}+\frac52y^2-15y^4\right),\quad y=x-\frac12.
\]
Its derivative is \(F'(x)=5b y(1-12y^2)\). On the open unit interval, it has two strict local maxima at \(x=1/2\pm1/(2\sqrt3)\), both at height \(5b/12\), and a strict local minimum at \(x=1/2\) of height \(5b/16\). Also \(F(0)=F(1)=0\). Therefore a horizontal line \(F=c\) crosses each of the four monotonic arcs exactly once if and only if \(5b/16<c<5b/12\). Outside this strict window there are fewer than four distinct interior intersections. The sign pattern of \(G\) from left to right is negative, positive, negative, positive, negative, making roots one and three repelling, roots two and four attracting under \(\dot x=x(1-x)G(x)\). At \(c=b/3\), solving \(-15y^4+(5/2)y^2-1/48=0\) gives exactly the four stated radicals. This proves sharpness. \(\square\)

## Verification
Run `python verification/verify.py` after installing the isolated optional dependency from `verification/requirements.txt` (SymPy 1.13–1.x). The standalone checker performs 145 exact symbolic/rational assertions, including direct independent enumeration of focal-player pivotal events at rational frequencies, polynomial and derivative identities, all four radical roots and their vector-field signs, the exceptional five-player cubic discriminant, and the admissible short-group coefficient sign patterns. The finite checks verify algebraic intermediates; the all-parameter statements follow from the analytic arguments in the proof, not from numerical sampling.

## Relationship to prior work
Archetti and Scheuring (first public 10 November 2010) study volunteer production of a *single* public good with one threshold and show how a stable mixed equilibrium can occur. Peña, Lehmann, and Nöldeke (public arXiv version 1 October 2013) prove general Bernstein-polynomial sign-variation tools, including their application to single-threshold public goods, but those upper bounds alone do not exclude four roots in the exceptional five-player two-threshold case. The present finding specializes to *two independently awarded, monotone threshold goods triggered by the same volunteer contribution* and proves both the all-parameter five-player obstruction and a six-player sharp example with two stable interior states. Archetti (2018) surveys Bernstein methods and complex benefit functions, including a nonmonotone double sigmoid, but this is not the present monotone two-step benefit model or its minimum group size. Zhang and collaborators (2013) consider divisible versus indivisible investment in nonlinear public-goods games, with different strategy dynamics. This is a claim of a specific mathematical refinement, not of novelty of the underlying replicator method.

## Limitations
The conclusion depends on two positive shared threshold rewards, one shared fixed volunteering cost, exactly two strictly interior thresholds, and well-mixed infinite-population replicator dynamics. A single good, threshold one or unanimity, nonpositive rewards, dynamic costs, random group-size mixtures, finite-population stochastic stability, and spatial assortment are not classified. This is a statement about exact equilibria and local deterministic stability; global stochastic persistence, basin volumes, and empirical behavioral calibration are not proved. Earlier equivalent presentations of the sharp six-player boundary could remain undiscovered, and independent validation has not been conducted.

## References
1. M. Archetti and I. Scheuring, *Coexistence of Cooperation and Defection in Public Goods Games*, Evolution 65 (2011), 1140–1148; first published online 10 November 2010. DOI: https://doi.org/10.1111/j.1558-5646.2010.01185.x .
2. J. Peña, L. Lehmann, and G. Nöldeke, *Gains from Switching and Evolutionary Stability in Multi-player Matrix Games*, Journal of Theoretical Biology 346 (2014), 23–33; first arXiv version 1 October 2013. https://arxiv.org/abs/1310.0498 .
3. M. Archetti, *How to Analyze Models of Nonlinear Public Goods*, Games 9 (2018), 17. https://doi.org/10.3390/g9020017 .
4. Y. Zhang, F. Fu, T. Wu, G. Xie, and L. Wang, *A Tale of Two Contribution Mechanisms for Nonlinear Public Goods*, Scientific Reports 3 (2013), 2021. https://doi.org/10.1038/srep02021 .
