# Bias reverses optimal zealot spacing on voter-model cycles while endpoint risks grow together

## Finding
Consider a continuous-time, two-opinion voter model on the cycle \(C_n\), for each integer \(n\geq4\), with one permanently positive vertex and one permanently negative vertex. If the two directed arcs between them have \(a\) and \(b=n-a\) edges, every nonfixed vertex adopts the opinion of each positive neighbor at rate \(\beta>0\), and that of each negative neighbor at rate \(\alpha>0\), independently across disagreeing neighbor incidences. Set \(r=\beta/\alpha\) and \(Z_m(r)=\sum_{j=0}^{m-1}r^j\) for integer \(m\geq1\). Let \(X\) be the number of positive voters in the unique stationary distribution.

**Exact law.** For all valid \(n,a,b,r\),
\[
\mathbb E[t^X]=t\frac{Z_a(rt)Z_b(rt)}{Z_a(r)Z_b(r)},\qquad
\Pr(X=1+s)=\frac{r^s}{Z_a(r)Z_b(r)}\max\{0,1+\min(a-1,s)-\max(0,s-b+1)\}
\]
for integer \(0\leq s\leq n-2\). Equivalently, \(X=1+I+J\) with independent truncated geometric interface positions \(\Pr(I=i)=r^i/Z_a(r)\), \(0\leq i<a\), and \(\Pr(J=j)=r^j/Z_b(r)\), \(0\leq j<b\).

**Strict spacing optimization.** For a fixed \(n\), call a placement more balanced if its smaller arc length is larger. Among all placements, when \(r>1\), the mean \(\mathbb E[X]\) strictly decreases with increasing balance, so the positive opinion's expected support is maximal for adjacent opposed zealots (arc lengths \(1,n-1\)) and minimal for the most evenly separated placement. For \(0<r<1\), every strict comparison reverses: maximizing positive support requires the most even separation. At \(r=1\), all placements have \(\mathbb E[X]=n/2\).

**Both extreme risks move together.** Regardless of whether \(r<1\), \(r=1\), or \(r>1\), both \(\Pr(X=1)\) (all free voters negative) and \(\Pr(X=n-1)\) (all free voters positive) strictly **increase** with increasing spacing imbalance. Thus an arrangement can raise the expected support of the favored opinion and simultaneously raise the probability that the same opinion attracts no free voter.

## Assumptions and scope
The graph is a simple undirected cycle with \(n\geq4\) vertices. Exactly two fixed opposing voters never update; all others update asynchronously according to the stated opinion-dependent imitation rates. Each disagreement incidence contributes its own transition rate; a site with two disagreeing neighbors has two independent contributions. There is no spontaneous mutation, spatial disorder, opinion-independent update clock followed by uniformly chosen neighbor (except when \(\alpha=\beta\)), or additional fixed voter. The arc lengths \(a,b\) count edges, not free vertices; consequently there are \(a-1\) and \(b-1\) free vertices on the respective arcs. Every claim applies to all initial spin configurations and the unique limiting stationary law. A placement is considered up to exchanging its two arcs.

## Proof
**(1) Closed irreducible recurrent configurations.** On either arc, order the free vertices from the positive endpoint to the negative endpoint. Configurations consisting of an initial block of \(i\) positive free vertices followed by negative free vertices, with \(i=0,\ldots,a-1\), form a closed class: every permitted flip changes \(i\) by exactly one. The positive block grows at rate \(\beta\) and shrinks at rate \(\alpha\), with reflected endpoint behavior. From any initial configuration, one can successively copy the negative endpoint along the arc, giving positive-probability paths into this class. Hence it is the unique recurrent class on that finite arc, and its birth-death chain is irreducible. The two arcs have disjoint sets of free vertices and independent update clocks, so their joint recurrent class is the Cartesian product and their stationary law is a product. This also establishes convergence from every initial state.

**(2) Detailed balance and distribution.** A one-step interface transition \(i\to i+1\) has rate \(\beta\), whereas \(i+1\to i\) has rate \(\alpha\). Therefore detailed balance requires \(\pi_{i+1}/\pi_i=r\), giving \(\pi_i=r^i/Z_a(r)\). Apply the identical argument to the other arc. Its independent contribution yields the generating function, and counting ordered solutions of \(i+j=s\), with \(0\leq i<a\) and \(0\leq j<b\), gives the coefficient formula. The endpoints correspond to unique interface pairs \((0,0)\) and \((a-1,b-1)\), proving
\[
\Pr(X=1)=\frac1{Z_a(r)Z_b(r)},\qquad
\Pr(X=n-1)=\frac{r^{n-2}}{Z_a(r)Z_b(r)}.
\]

**(3) Strict curvature of mean interface location.** Define \(f_m(r)=\sum_{j=0}^{m-1}jr^j/Z_m(r)\). Then \(\mathbb E[X]=1+f_a(r)+f_b(r)\). For \(r>1\) put \(\lambda=\log r>0\), extend the integer variable \(m\) to positive real \(x\), and write
\[
f_x(r)=\frac{x}{1-e^{-\lambda x}}-\frac{r}{r-1},\qquad g(z)=\frac{z}{1-e^{-z}}.
\]
The second derivative of the nonconstant part is \(\lambda g''(\lambda x)\), where
\[
g''(z)=\frac{e^{-z}\big((z-2)+(z+2)e^{-z}\big)}{(1-e^{-z})^3}>0\quad(z>0).
\]
Indeed for the parenthesis \(h(z)=(z-2)+(z+2)e^{-z}\), one has \(h(0)=0\), \(h'(z)=1-(z+1)e^{-z}>0\) for \(z>0\), using \(e^z>1+z\). Hence \(f_x(r)\) is strictly convex. For \(0<r<1\), the identity \(f_m(r)=(m-1)-f_m(1/r)\), from reversing the finite geometric weights, makes \(f_x(r)\) strictly concave. At \(r=1\), \(f_m(1)=(m-1)/2\). Consequently, for integer \(b\geq a+2\), transferring one unit of arc length from the longer arc to the shorter strictly decreases \(f_a(r)+f_b(r)\) when \(r>1\), strictly increases it when \(r<1\), and leaves it unchanged at \(r=1\). Every pair of placements with different imbalance is linked by such transfers; this proves the full ranking and extremizers.

**(4) Simultaneous extreme-probability ordering.** For \(b\geq a+2\), direct multiplication yields
\[
Z_{a+1}(r)Z_{b-1}(r)-Z_a(r)Z_b(r)
=\frac{r^{b-1}-r^a}{r-1}>0\qquad(r>0,\ r\ne1).
\]
The limit at \(r=1\) is \(b-a-1>0\). Hence balancing always increases the normalizing product, strictly lowering the two endpoint probabilities in step (2). This completes the proof for all parameter values, including adjacent zealots and equal or nearly equal arc lengths.

## Verification
The standalone `verify.py` uses only Python 3 standard libraries and exact rational arithmetic. Running `python3 verify.py` produces `certificate.json` (the enclosed expected output) as an exact, reproducible summary. It independently constructs the *full* continuous-time Markov generator on every permitted spin configuration for cycle sizes 3 through 9 and every pair of zealot positions, using five positive-rate pairs. It verifies global stationary flow balance, full-state reachability of the proposed recurrent support, normalization and all coefficient formulas. Separately it tests the exact inequalities and complete distributions for cycle sizes 4 through 40 and five rational bias values. The finite checks support implementation correctness but do not prove the universal assertions; the proof above supplies the argument for all finite \(n\) and all real \(r>0\).

## Relationship to prior work
Mobilia, Petersen and Redner (2007, arXiv:0706.2892), Section 4.1 and Appendix, already analyze two opposed zealots on a cycle with *equal* persuasion and obtain a continuum-scale magnetization distribution by two uniformly distributed domain walls. Therefore no novelty is claimed for the neutral-interface mechanism or its continuum limit. The present theorem instead treats distinct opinion-dependent microscopic persuasion rates for **every finite cycle**, and identifies a strict change in the optimal *fixed* placement as bias reverses, while showing simultaneous enhancement of both extreme stationary outcomes under clustering.

Yildiz, Ozdaglar, Acemoglu, Saberi and Scaglione (2011 manuscript, later published 2013) study discrete opinion dynamics with stubborn agents and optimal positions under uniform neighbor-copying. Vendeville, Guedj and Zhou (arXiv:2006.07265, 2022 version), Sections 3–4, establish average-opinion formulas under equal-rate imitation and uniformly randomized stubborn-node placement. Neither inspected formulation contains opinion-dependent rate asymmetry on a finite cycle and the joint strict placement comparison. Mobilia's nonlinear \(q\)-voter work (arXiv:1506.04911) treats a different \(q\geq2\) well-mixed model. The result is closely related to standard stationary birth-death calculations; the substantive conclusion is the quantified position-ranking reversal with simultaneous extreme-tail monotonicity, not the geometric stationary weights alone.

## Limitations
The model is deliberately simple: fixed opposed zealots, homogeneous opinion-dependent but location-independent rates, a one-dimensional cycle, and asynchronous linear imitation. No claim is made for arbitrary graphs, other zealot populations, homophilic clocks, endogenous persuasion or strategic actions. The location ranking compares expectation only; the exact endpoint conclusions should not be misread as full stochastic dominance of one placement over another. Neutral case geometric weights and the two-wall picture follow directly from prior work. While relevant source texts were examined, an unpublished or differently phrased weighted-voter theorem might imply the biased formulas or placement inequalities, so novelty awaits independent bibliography review. Verification does not certify claims beyond the analytical assumptions.

## References
1. M. Mobilia, A. Petersen and S. Redner, *On the Role of Zealotry in the Voter Model*, Journal of Statistical Mechanics P08029 (2007), first submitted 20 June 2007, arXiv:0706.2892, doi:10.1088/1742-5468/2007/08/P08029. https://arxiv.org/abs/0706.2892
2. E. Yildiz, A. Ozdaglar, D. Acemoglu, A. Saberi and A. Scaglione, *Discrete Opinion Dynamics with Stubborn Agents*, 2011 manuscript, later ACM Transactions on Economics and Computation (2013), doi:10.1145/2538508. https://web.mit.edu/Asuman/Desktop/asuman/www/documents/voter-submit.pdf
3. A. Vendeville, B. Guedj and S. Zhou, *Towards control of opinion diversity by introducing zealots into a polarised social group*, arXiv:2006.07265; proceedings (2022). https://arxiv.org/abs/2006.07265
4. M. Mobilia, *Nonlinear \(q\)-voter model with inflexible zealots*, Physical Review E **92**, 012803 (2015), arXiv:1506.04911. https://arxiv.org/abs/1506.04911
