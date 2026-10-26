# Exact sign-reversal boundary for correlations in a locally reset voter chain

## Finding

A one-dimensional nearest-neighbor voter chain copies a uniformly chosen neighbor at rate one per site. Independently, every site resets at rate \(r>0\) to its own frozen initial opinion. Suppose the frozen opinions form a stationary, symmetric two-state Markov chain with correlation parameter \(-1\le c\le1\). Thus the initial opinions \(\sigma_j\in\{-1,1\}\) satisfy \(\mathbb E\sigma_j=0\) and \(\mathbb E[\sigma_0\sigma_n]=c^{|n|}\); the endpoint values represent symmetric mixtures of the two checkerboards (\(c=-1\)) and the two constant configurations (\(c=1\)).

Let \(G_1(r,c)=\lim_{t\to\infty}\mathbb E[s_0(t)s_1(t)]\), where the expectation includes the initial opinion field and all copying and resetting clocks. Set
\[
q=1+r-\sqrt{r(r+2)}\in(0,1),\qquad r=\frac{(1-q)^2}{2q}.
\]
Then the stationary nearest-neighbor correlation is exactly
\[
\boxed{G_1(r,c)=\frac{4c^2q^4-c(3q^4+2q^3+2q^2+2q-1)+2q^3+2q}{(1+q)^2(1-cq)^2}.}
\]
The following classification is sharp:

* If \(0\le c\le1\), then \(G_1(r,c)>0\) for every finite \(r>0\).
* For every \(-1\le c<0\), there is exactly one \(r_c(c)>0\) such that \(G_1(r,c)>0\) for \(0<r<r_c(c)\), \(G_1(r_c(c),c)=0\), and \(G_1(r,c)<0\) for \(r>r_c(c)\). It is the unique positive rate obtained from the unique \(q\in(0,1)\) solving the displayed numerator equation. The map \(c\mapsto r_c(c)\) is strictly increasing and \(r_c(c)\sim1/|c|\) as \(c\uparrow0\).
* Across every Markov template in this family, the smallest possible sign-reversal rate occurs for the perfectly alternating template, \(c=-1\). It is
\[
\boxed{r_* = \frac{(1-q_*)^2}{2q_*}=1.446156936667017\ldots,\quad
7q_*^3-3q_*^2+5q_*-1=0,\quad q_*\in(0,1).}
\]
For \(r\le r_*\), neighboring stationary opinions are never negatively correlated for any \(c\in[-1,1]\). For \(r>r_*\), negatively correlated examples exist, and the exact boundary within the Markov-template family is the unique negative solution \(c\) of the displayed numerator equation.

Equivalently, the stationary domain-wall density \(\rho=(1-G_1)/2\) can exceed the independent-spin benchmark \(1/2\) only beyond the stated correlation-sign boundary. This crossing of a local correlation is not asserted to be a thermodynamic phase transition.

## Assumptions and scope

The sites are \(\mathbb Z\). Each site has a rate-one copying clock; on a ring of its clock it takes the current spin of either neighbor with probability \(1/2\). Each site has a separate independent rate-\(r\) Poisson clock whose mark replaces its current spin by the *same frozen* spin \(\sigma_i\), not a freshly sampled spin. The template is sampled once from the stationary symmetric nearest-neighbor Markov law with transition probabilities \(\mathbb P(\sigma_{i+1}=\sigma_i)=(1+c)/2\). All driving clocks are independent of one another and of the template.

The formula concerns the infinite lattice and the stationary annealed (template-averaged) expectation. Time is normalized so that total copying rate is one; if that rate is \(\tau^{-1}\), replace \(r\) throughout by the dimensionless \(r\tau\). It includes the two nonergodic endpoint template laws by their natural shift-invariant symmetric mixtures. It does not concern global simultaneous resets, spontaneous memoryless opinion flips, or a non-Markov reset template outside this family.

## Proof

**1. Stationary construction and correlations with the frozen field.** Use the usual graphical representation of the voter model. Following a single spin backward in time gives a continuous-time nearest-neighbor random walk with jumps left and right each at rate \(1/2\), until the first encountered local resetting mark; that mark sets its ancestor to the frozen template opinion at the mark's site. The killing rate along every backward path is \(r\). Thus the ancestral search is almost surely finite, and the dependence of a fixed finite set of spins on states before elapsed time \(t\) is at most its cardinality times \(e^{-rt}\). This constructs a unique stationary conditional law given the template and shows convergence from any starting spin configuration.

Write \(C_n=c^{|n|}\) and \(H_n=\mathbb E[s_0\sigma_n]\) in stationarity. The generator of one spin gives
\[
(r-\tfrac12\Delta)H=rC,\qquad (\Delta f)_n=f_{n-1}+f_{n+1}-2f_n.
\]
Let \(P\) be the unique bounded Green kernel satisfying \((r-\Delta/2)P=r\delta_0\). Solving its recurrence and normalization gives
\[
P_n=\frac{1-q}{1+q}q^{|n|},\qquad \sum_{n\in\mathbb Z}P_n=1,
\]
where \(q\) is as defined above. Hence \(H=P*C\).

**2. The two-spin boundary constraint.** For \(n\ne0\), copying either of the two distinct spins and resetting either spin produces
\[
(2r-\Delta)G_n=2rH_n,\qquad G_0=1.
\]
The even convolution \(B=P*P*C\) satisfies the same inhomogeneous equation on the full lattice, since \((2r-\Delta)P=2r\delta_0\). The bounded even solutions of the corresponding homogeneous recurrence away from \(n=0\) are multiples of \(q^{|n|}\). Enforcing \(G_0=1\) therefore yields the exact complete stationary two-point formula
\[
G_n=B_n+(1-B_0)q^{|n|}\qquad(n\in\mathbb Z).
\]
Uniqueness also follows from the backward graphical construction. This step retains the diagonal identity \(G_0=1\), which an unconstrained independent-walker convolution alone would violate.

**3. Evaluation at adjacent sites.** Put \(a=(1-q)/(1+q)\). Direct convolution of the two geometric Green kernels gives
\[
(P*P)_n=a^2q^{|n|}\left(|n|+1+\frac{2q^2}{1-q^2}\right).
\]
Absolute convergence holds for \(|c|\le1\), since \(0<q<1\). Splitting the convolution \(B_1-qB_0\) at template index \(m=0\), then summing the geometric series and its first moment, gives
\[
B_1-qB_0
=a^2\left[\frac{q+c}{1-cq}+\frac{(1-q^2)c^2q}{(1-cq)^2}\right]
=a^2\frac{q+c(1-q^2)-c^2q^3}{(1-cq)^2}.
\]
Since \(G_1=q+B_1-qB_0\), bringing these terms over the common positive denominator \((1+q)^2(1-cq)^2\) proves the displayed rational formula.

**4. Exact sign and uniqueness.** Differentiation of that rational expression yields
\[
\frac{\partial G_1}{\partial q}
=\frac{2(c-1)P(q,c)}{(q+1)^3(cq-1)^3},
\]
where
\[
P(q,c)=4c^2q^4-2cq^4-7cq^3+3cq^2-cq-c+q^3+3q^2-q+1.
\]
For \(-1\le c\le0\), write \(u=-c\). Then
\[
P=4u^2q^4+u\bigl(2q^4+q(7q^2-3q+1)+1\bigr)
+\bigl(q^3+3q^2+1-q\bigr)>0.
\]
Indeed \(7q^2-3q+1>0\) for real \(q\), and \(1-q>0\) on \((0,1)\). Since \(c-1<0\) and \((cq-1)^3<0\), \(\partial_qG_1>0\). Moreover \(\lim_{q\downarrow0}G_1(q,c)=c\) and \(\lim_{q\uparrow1}G_1(q,c)=1\). This proves one and only one zero for each \(c<0\), and the direction of the crossing follows because \(r=(1-q)^2/(2q)\) decreases strictly in \(q\). For \(c\ge0\), the backward coalescing-walk representation gives \(G_1=\mathbb E[C_{A-B}]\ge0\), where the random ancestral sites \(A,B\) can coincide with strictly positive probability for any finite \(r>0\); hence strict positivity. Equivalently, the closed expression has this sign.

To order the thresholds in \(c\), differentiate again:
\[
\frac{\partial G_1}{\partial c}
=\frac{(q-1)^2\,[3cq^3-cq-q^2-1]}{(q+1)^2(cq-1)^3}>0
\qquad(-1\le c\le1,\ 0<q<1).
\]
The square bracket is strictly negative: for \(q\ge1/\sqrt3\), it is at most \((q-1)(3q^2+2q+1)<0\); for \(q<1/\sqrt3\), it is at most \(-1+q-q^2-3q^3<0\). The denominator is negative. The zero therefore moves to smaller \(q\), hence larger \(r\), when \(c\) increases through the negative interval.

At \(c=-1\), the correlation simplifies to
\[
G_1(q,-1)=\frac{7q^3-3q^2+5q-1}{(1+q)^3}.
\]
The numerator is strictly increasing, since its derivative \(21q^2-6q+5\) is positive for all real \(q\), and it changes sign between \(q=0\) and \(q=1\). Thus the unique root \(q_*\) gives the universal minimal rate \(r_*\) in this template family. Finally the numerator of the general rational expression, expanded around \((q,c)=(0,0)\), gives \(q_c=-c/2+O(c^2)\) as \(c\uparrow0\). Substituting into \(r=(1-q)^2/(2q)\) yields \(r_c(c)\sim1/|c|\). All inequalities are strict where claimed.

## Verification

The accompanying standalone `check.py` uses SymPy to reconstruct the rational formula from the Green kernels, differentiate and factor it symbolically, check the \(c=-1,0,1\) specializations, locate the unique cubic root, and compare with independently truncated absolutely convergent convolution sums. In one replay it produced 1,335 individual numeric/rational kernel and positivity comparisons, alongside exact symbolic identity checks; all passed. Those finite checks are secondary to the analytic monotonicity and endpoint arguments above.

For a simple exact sign witness, the alternating template has \(G_1(1,-1)=5/3-8\sqrt3/9>0\) and \(G_1(2,-1)=2-3\sqrt2/2<0\). The critical rate is strictly between one and two. All calculations are reproducible with Python 3 and SymPy by running `python check.py` in the extracted package directory.

## Relationship to prior work

Pascal Grange, *Voter model under stochastic resetting*, arXiv:2207.08590, first released 18 July 2022, introduced the local resetting rule and derived the exact one- and two-point kinetic equations. The paper's explicit stationary density of domain walls takes independent unbiased initial spins, corresponding to \(c=0\). Its general moment equations are used here with full credit; they do not state the Markov-correlated template law or the sharp correlation-sign inversion boundary. The special case \(c=0\) of the present expression is consistent with the paper's stationary result and its small-reset asymptotic. The proof's *new content* is the correlated-template evaluation and strict sign-threshold classification, not the generator identities, Green-kernel method, or standard voter graphical duality.

Mario J. de Oliveira, *Linear Glauber model*, Physical Review E 67, 066101 (2003), concerns a linear voter/noise model and Green-function correlations, but its memoryless noise is not the reset-to-own-frozen-template protocol used here. Other general noisy-voter and global-Ising-resetting studies likewise address different noise/reset protocols. The possibility of an equivalent specialization in broader quenched-disorder or noisy-voter literature remains a priority limitation requiring independent literature review.

## Limitations

The result is an annealed stationary pair-correlation theorem for a particular one-dimensional Markov family of initial memories, not an assertion about samplewise correlation signs for every frozen configuration. Only the sign of the nearest-neighbor correlation is completely classified; no full joint stationary spin law, all-distance sign diagram, higher-dimensional analogue, finite-size crossover, or thermodynamic phase transition is claimed. The novelty assessment is a literature comparison, not proof of worldwide priority; no independent audit was performed.

## References

1. P. Grange, *Voter model under stochastic resetting*, arXiv:2207.08590 (first public 18 July 2022), https://arxiv.org/abs/2207.08590 ; complete mathematical treatment at https://arxiv.org/html/2207.08590v6 .
2. M. J. de Oliveira, *Linear Glauber model*, Physical Review E **67**, 066101 (2003), https://doi.org/10.1103/PhysRevE.67.066101 .
3. M. Magoni, S. N. Majumdar, and G. Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867 (2020), https://arxiv.org/abs/2002.04867 .
