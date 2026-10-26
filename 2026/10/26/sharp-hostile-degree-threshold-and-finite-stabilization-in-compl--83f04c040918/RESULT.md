# Sharp hostile-degree threshold and finite stabilization in complete signed opinion networks

## Finding

Consider the synchronous repulsive bounded-confidence model defined below on a complete network of \(n\ge2\) agents with confidence radius \(c>0\). Every off-diagonal relationship is permanently designated friendly or hostile. Let \(H\) be the simple graph consisting of the hostile relationships, with vertex degrees \(d_i\) and descending degrees \(d_{(1)}\ge d_{(2)}\ge\cdots\); write \(m=|E(H)|\). Initially, every pair is receptive: \(\max_i x_i(0)-\min_i x_i(0)<c\).

**Theorem.** Every such initial profile remains fully receptive at every subsequent time, for every choice of initial real opinions, **if and only if**
\[
\boxed{d_{(1)}+d_{(2)}<n.}
\]
If this degree condition holds, each trajectory becomes **exactly stationary in finitely many synchronous steps**, rather than merely converging asymptotically. Writing \(\mu=n^{-1}\sum_i x_i(0)\), its terminal state has the quantized form
\[
 x_i(T)=\mu+\frac cn s_i,\qquad s_i\in\{-d_i,-d_i+2,\ldots,d_i\},\qquad \sum_i s_i=0.
\]
One can take the universal bound
\[
\boxed{T\le \min\!\left\{2^m,\prod_{i=1}^n(d_i+1)\right\}.}
\]
The bound is not asserted optimal. If \(d_{(1)}+d_{(2)}\ge n\), there are strictly ordered, initially fully receptive opinions for which at least one pair becomes nonreceptive immediately after the first update. Thus the network-level preservation condition is sharp.

## Assumptions and scope

The network is undirected and complete, with symmetric signs \(A_{ij}\in\{-1,+1\}\) for distinct agents, and self-inclusion \(A_{ii}=1\). At each integer time all agents update synchronously, using only pairs for which \(|x_i-x_j|<c\). Let \(N_i(t)=\{j\ne i:|x_j(t)-x_i(t)|<c\}\). An active friendly edge contributes \(x_j-x_i\) to agent \(i\)'s numerator; an active hostile edge contributes \((x_j-x_i)-c\sigma_{ji}\), where \(\sigma_{ji}\) is the sign of \(x_j-x_i\) if this difference is nonzero and is \(\operatorname{sgn}(j-i)\) at a tie. Hence the complete update is
\[
 x_i(t+1)=x_i(t)+\frac{\displaystyle\sum_{j\in N_i(t)}\left(x_j(t)-x_i(t)-c\,\mathbf1_{\{ij\in E(H)\}}\sigma_{ji}(t)\right)}{1+|N_i(t)|}.
\]
This is the self-inclusive Kann--Feng repulsive bounded-confidence rule, specialized only to a fixed complete relationship graph. It does **not** model attraction to hostile neighbors outside the confidence radius. The tie rule uses the fixed vertex labels \(1,\ldots,n\).

## Proof

For any opinion vector \(x\), define
\[
 g_i(x)=\sum_{j:ij\in E(H)}\sigma_{ij}(x),\qquad
 \sigma_{ij}(x)=\begin{cases}
 1,&x_i>x_j,\\ -1,&x_i<x_j,\\ \operatorname{sgn}(i-j),&x_i=x_j.
 \end{cases}
\]
Every hostile edge contributes opposite signs at its two endpoints. Thus \(\sum_i g_i(x)=0\), \(|g_i(x)|\le d_i\), and each \(g_i(x)\) is an integer congruent to \(d_i\) modulo \(2\).

**Full-reception reduction.** Whenever every pair is receptive, each denominator is exactly \(n\). The pairwise linear difference terms then sum to \(n(\mu-x_i)\), while the hostile corrections sum to \(cg_i(x)\). Therefore
\[
\boxed{x_i^+=\mu+\frac cn g_i(x).}\tag{1}
\]
Here \(\mu\) is preserved from one full-reception update to the next, by antisymmetry across every edge.

**Sharp reception criterion.** Equation (1) gives, for any distinct \(i,j\),
\[
 |x_i^+-x_j^+|=\frac cn|g_i(x)-g_j(x)|
 \le\frac cn(d_i+d_j)\le\frac cn(d_{(1)}+d_{(2)}).
\]
If the two highest hostile degrees sum to less than \(n\), this last quantity is strictly less than \(c\). Induction starting at time zero proves permanent full reception. Conversely, suppose the degree sum is at least \(n\). Choose distinct maximum- and second-maximum-degree vertices \(i,j\). Give \(i\) the unique largest initial opinion, \(j\) the unique smallest, and place all other opinions strictly between them in an interval shorter than \(c\). Then \(g_i(x)=d_i\), \(g_j(x)=-d_j\), so their first-update distance is exactly \(c(d_i+d_j)/n\ge c\). Strict bounded confidence excludes that pair at the next interaction. This proves both directions, including equality at the boundary.

**Strict potential and finite termination.** In the permanent full-reception regime put
\[
 Q(x)=\sum_{ij\in E(H)}|x_i-x_j|,\qquad
 \Phi(x)=Q(x)-\frac n{2c}\sum_i(x_i-\mu)^2.
\]
The vector \(g(x)\) is a valid subgradient of the convex function \(Q\); the prescribed tie orientation is a legitimate selection of the interval subgradient at zero. For \(y=x^+=\mu\mathbf1+(c/n)g(x)\), the convex subgradient inequality implies
\[
\begin{aligned}
 \Phi(y)-\Phi(x)
 &\ge g(x)\mathbin{\cdot}(y-x)
 -\frac n{2c}\big(\|y-\mu\mathbf1\|_2^2-\|x-\mu\mathbf1\|_2^2\big)\\
 &=\boxed{\frac n{2c}\|y-x\|_2^2}.
\end{aligned}
\]
Thus \(\Phi\) strictly increases at every nonstationary update. After the first update, equation (1) restricts every coordinate to one of \(d_i+1\) lattice values. Alternatively, each hostile edge has two possible orientations under the total order of pairs \((x_i,i)\), and the entire score vector \(g(x)\) is determined by that orientation, giving at most \(2^m\) possibilities. Because the subsequent evolution is deterministic, a nonstationary trajectory cannot revisit a lattice state: that would contradict strict potential increase. It must therefore reach a fixed point after at most the stated number of total time steps, including the first update. Its stationary opinion vector has the claimed quantized form.

## Verification

The standalone standard-library script `verify.py` directly compares the original signed averaging rule against equation (1) on \(2{,}800\) exact rational test cases, including opinion ties. It then enumerates every signing of the complete graph and every strict opinion ordering through \(n=5\). In this exhaustive *finite* range it checks the sharp degree condition, first-step reception, fixed-point termination, and the integer version of the potential inequality. These are \(231{,}388\) assertions for eligible configurations and boundary witnesses; \(33{,}314\) eligible starting-order instances reach fixed points. It additionally performs \(7{,}818\) exact checks on reproducibly sampled instances with \(6\le n\le8\). Run with `python3 verify.py`; it prints `DIRECT_UPDATE_OK` and `EXACT_OK`. This computational evidence is supplemental to the proof for arbitrary \(n\).

For a nontrivial eligible example, use \(n=7\) and hostile edges \(\{02,04,05,12,15,23,35,36\}\) with indices \(0,\ldots,6\). Its hostile degrees are \((3,2,3,3,1,3,1)\), so the top two sum to \(6<7\). Initial opinions proportional to \((4,0,6,3,5,2,1)\) with positive proportionality constant less than \(c/6\) produce four successive score vectors before reaching the fixed vector \((-3,-2,3,-3,1,3,1)\). At the sharp obstruction boundary, a five-agent hostile star has degree sum \(4+1=5\); placing its center highest and one leaf lowest yields a first-step pair gap exactly \(c\).

## Relationship to prior work

Kann and Feng (arXiv:2301.02210v1, January 5, 2023) introduce precisely this repulsive bounded-confidence update in their equations (3.1)--(3.2). Their Theorem 4.10 treats the opposite, all-hostile complete graph and its limiting span; their subsequent broader convergence/range claim is presented without a general proof. The present theorem instead identifies the exact degree-sum boundary for universal **permanent full reception** of signed complete networks, and proves finite-step termination and quantization on the preserving side. All-hostile complete graphs with at least three vertices lie outside that side, so the statements do not imply each other.

Earlier conventional Hegselmann--Krause finite-termination theorems concern attractive averaging without the present hostility correction. He, Liu, Hu, and Fang (2021) study another signed bounded-confidence mechanism, reported in their abstract as preserving opinion signs; its full text was unavailable for comparison. The 2024 Bernardo--Altafini--Proskurnikov--Vasca survey principally covers attractive synchronous bounded-confidence systems, while Li's 2021 mixed-HK analysis uses stochastic/stubborn averaging rather than the Kann--Feng repulsion term. These connections motivate caution about broader theorem equivalences, but none of the inspected statements establishes the stated sharp hostile-degree criterion in the specified update.

## Limitations

The universal threshold concerns *permanent full receptivity*, not general convergence after hostile or friendly interactions become inactive. The finite-time result assumes initially complete reception, symmetric complete signed relationships, synchronous updates, common strict confidence radius, and the specified self-inclusive normalization and tie rule. The step-count bound is not claimed sharp, and the finite computations do not prove any infinite family. Related full text by He and collaborators remained inaccessible, so publication priority is not established independently.

## References

1. C. Kann and M. Feng, *A Repulsive Bounded-Confidence Model of Opinion Dynamics in Polarized Communities*, arXiv:2301.02210v1 (first public January 5, 2023), https://arxiv.org/pdf/2301.02210.
2. G. He, J. Liu, H. Hu, and J.-A. Fang, *Discrete-time signed bounded confidence model for opinion dynamics*, Neurocomputing 425 (2021), 53--61, DOI:10.1016/j.neucom.2019.12.061.
3. C. Bernardo, C. Altafini, A. Proskurnikov, and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302, DOI:10.1016/j.automatica.2023.111302.
4. H.-L. Li, *Mixed Hegselmann-Krause Dynamics II*, arXiv:2112.13348v1 (2021), https://arxiv.org/html/2112.13348v1.
