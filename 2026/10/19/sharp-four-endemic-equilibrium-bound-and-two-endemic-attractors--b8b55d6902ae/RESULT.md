# Sharp four-endemic-equilibrium bound and two endemic attractors in a purely triadic SIS model

## Finding
In a two-susceptibility deterministic SIS population with **only collective three-person contagion** and no pairwise infection, the number of distinct positive endemic equilibria is at most four. This sharp bound is attained by an explicit rational-parameter model with **two locally attracting endemic states**, two saddle endemic states, and the attracting disease-free state. The five-equilibrium configuration persists under sufficiently small parameter perturbations. The result is a concrete separation between a homogeneous pure-triadic population, which has at most two endemic states, and a heterogeneous one.

## Assumptions and scope
Let \(p\in(0,1)\), \(a,b>0\), and let \(x_1(t),x_2(t)\in[0,1]\) denote infected fractions in two classes. Set \(M=p x_1+(1-p)x_2\) and consider
\[
\dot x_1=-x_1+a(1-x_1)M^2,\qquad
\dot x_2=-x_2+b(1-x_2)M^2.
\]
Each infectious contact term requires two infected interaction partners. The recovery rates are normalized to one. The square \([0,1]^2\) is forward invariant: at \(x_i=0\) the outward derivative is nonnegative, and at \(x_i=1\) the derivative equals \(-1\). Thus every initial state in this square has a unique global forward solution. The model is a deterministic mean-field construction; the particular very unequal susceptibilities are mathematical witness parameters, not empirical estimates.

An endemic equilibrium means \(M>0\). A sink means both Jacobian eigenvalues have negative real part; a saddle means one eigenvalue is positive and the other negative.

## Proof
**Reduction and sharp upper bound.** At every endemic equilibrium,
\[
x_1=\frac{aM^2}{1+aM^2},\qquad x_2=\frac{bM^2}{1+bM^2}.
\]
Substituting into the definition of \(M\) and clearing strictly positive denominators gives \(M P(M)=0\), with
\[
P(M)=abM^4-abM^3+(a+b)M^2-[pa+(1-p)b]M+1.
\]
Every positive root of \(P\) with \(0<M<1\) determines exactly one equilibrium by the displayed formulas. Conversely, the scalar fixed-point equation for such a root forces the constructed fractions to have weighted mean \(M\); hence it is sufficient. There are at most four distinct such roots. The disease-free state \((0,0)\) is always a sink since its Jacobian is \(-I\).

**Four certified roots.** Choose \(p=1/1000\), \(a=100000000\), \(b=100\). Exact rational substitution into \(P\) gives the alternating signs
\[
\begin{array}{c|ccccc}
M&0&1/50000&1/500&1/50&1\\\hline
\operatorname{sgn}P(M)&+&-&+&-&+
\end{array}.
\]
Each of the four disjoint intervening open intervals therefore contains a root. Because \(P\) has degree four, each interval contains exactly one root, these are all roots counted with multiplicity, and all four roots are simple. All are in \((0,1)\), so they are all biological endemic equilibria. Approximate prevalence values, for orientation only, are \(0.00001009165731\), \(0.001116577197\), \(0.008965072452\), and \(0.9899082587\).

**Stability.** Write \(D_1=1+aM^2\), \(D_2=1+bM^2\), \(w=(p,1-p)^T\), and \(u=(2aM/D_1,2bM/D_2)^T\), evaluated at an endemic equilibrium. The Jacobian is the Metzler rank-one matrix
\[
J=-\operatorname{diag}(D_1,D_2)+u w^T.
\]
Let \(F(s)=p a s/(1+a s)+(1-p)b s/(1+b s)\) and \(G(M)=F(M^2)-M\). The matrix determinant lemma yields
\[
\det J=D_1D_2\left(1-2M\left[\frac{pa}{D_1^2}+\frac{(1-p)b}{D_2^2}\right]\right)=-D_1D_2 G'(M).
\]
Moreover, multiplying the equilibrium equation by the common denominator shows
\[
G(M)=-\frac{M P(M)}{(1+aM^2)(1+bM^2)}.
\]
At a simple positive root of \(P\), the derivative \(G'\) has sign opposite to \(P'\). The sign pattern \(+,-,+,-,+\) of \(P\) implies that the four successive roots have \(G'\) of signs \(+,-,+,-\). At roots with \(G'>0\), \(\det J<0\), hence the equilibria are hyperbolic saddles.

At roots with \(G'<0\), let \(s_i=w_i u_i/D_i\) (with \(w_1=p\), \(w_2=1-p\)). Then \(s_i\ge0\) and
\[
s_1+s_2=2M\left(\frac{pa}{D_1^2}+\frac{(1-p)b}{D_2^2}\right)=1+G'(M)<1.
\]
Thus \(\operatorname{tr}J=-D_1(1-s_1)-D_2(1-s_2)<0\), while \(\det J>0\). The corresponding roots are hyperbolic sinks. Together with the disease-free sink, there are exactly three locally attracting equilibria. Because the four roots are simple and lie strictly inside \((0,1)\), implicit-function continuity preserves four distinct roots and their hyperbolic stability types under all sufficiently small perturbations of the positive parameters.

## Verification
The accompanying dependency-free `verify.py` evaluates the five polynomial sign witnesses using exact rational arithmetic, verifies their alternating signs, independently checks the equilibrium-to-polynomial algebra at rational sample inputs, and constructs rational root brackets by bisection. The existence and exhaustiveness conclusions come from the intermediate-value theorem and degree-four bound, not numerical root finding. The Jacobian stability proof above is analytic.

## Relationship to prior work
Landry and Restrepo (2020) derive a general heterogeneous hypergraph mean-field SIS model with collective contagion, and discuss bistability driven by higher-order interactions. Their general formulation includes specializations of the present triadic form, but their inspected analysis does not give this sharp **four endemic equilibrium** count or the two-endemic-sink witness; model-class containment is not a prior theorem of the claimed classification. Cisneros-Velarde and Bullo (2020) establish general higher-order SIS threshold and stability conditions without this complete multiplicity classification. Kiss, Bick, and Simon (2025) analyze two-group higher-order contagion with within-group triadic contacts and cross-group pairwise contacts; that interaction architecture differs from the pure rank-one pooled triadic term \(M^2\). Samadi and colleagues' 2026 SIS–opinion higher-order study motivates a contemporary re-examination of multi-group effects, but their additional opinion coupling is not assumed here. The general existence of bistability is prior knowledge; the precise sharp four-root construction and resulting **two endemic sinks with no pairwise infection** are the proposed contribution.

## Limitations
The proof establishes an upper bound and one open parameter region exhibiting all four endemic states, not the global parameter-space phase diagram. It does not prove that every trajectory converges to an equilibrium, characterize global attraction basins, or transfer the statement to a finite stochastic hypergraph epidemic. The witness features extreme parameter separation; its empirical realism is not claimed. Although relevant literature was inspected, equivalent unindexed special-case calculations cannot be ruled out, and the full text of one relevant 2026 preprint was not inspected.

## References
1. Samadi, Caiza, Gracy and Paré, *A Networked SIS Epidemic–Opinion Model with Higher-Order Interactions*, arXiv:2608.31032v1 (first public August 31, 2026), https://arxiv.org/abs/2608.31032.
2. Kiss, Bick and Simon, *Decoding how higher-order network interactions shape contagion dynamics*, Journal of Mathematical Biology (2025), DOI:10.1007/s00285-025-02247-4, https://link.springer.com/article/10.1007/s00285-025-02247-4.
3. Cisneros-Velarde and Bullo, *Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions*, arXiv:2005.11404 (2020), https://arxiv.org/abs/2005.11404.
4. Landry and Restrepo, *The effect of heterogeneity on hypergraph contagion models*, Chaos **30**, 103117 (2020), DOI:10.1063/5.0020034, https://www.researchgate.net/publication/346108698_The_effect_of_heterogeneity_on_hypergraph_contagion_models.
