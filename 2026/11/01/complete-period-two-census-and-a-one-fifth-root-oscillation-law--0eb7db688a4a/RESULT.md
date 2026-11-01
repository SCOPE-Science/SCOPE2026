# Complete period-two census and a one-fifth root-oscillation law for majority dynamics on perfect binary trees

## Finding
Let \(T_h\) be the labelled perfect rooted binary tree of height \(h\ge1\), with \(2^{h+1}-1\) vertices. Under synchronous binary **neighbor-majority** dynamics, ties retain the vertex's old state. Define integer sequences
\[
u_0=1,\quad v_0=0,\qquad
u_{h+1}=u_h(u_h+2v_h),\quad v_{h+1}=u_h^2.
\]
The exact numbers of fixed configurations, two-step returning configurations, and distinct primitive period-two temporal orbits are respectively
\[
F_h=2u_h,\qquad Q_h=2(u_h^2+v_h^2),\qquad
N_h=u_h^2+v_h^2-u_h.
\]
These formulas count all two-cycles, including **mixed** cycles with both fixed and flipping vertices; no spatial or temporal symmetry is factored out except the two temporal phases of each primitive orbit.

Exactly \(2v_h^2\) of the two-step returning configurations have a flipping root. Consequently, if a primitive period-two configuration is chosen uniformly, the probability that its root flips is
\[
\frac{v_h^2}{u_h^2+v_h^2-u_h}\longrightarrow\frac15
\quad(h\to\infty).
\]
The proportion of primitive period-two configurations with a *fixed* root therefore tends to \(4/5\). The number of primitive period-two orbits grows exponentially in the number of vertices, with the exact per-vertex growth constant
\[
\lim_{h\to\infty}N_h^{1/(2^{h+1}-1)}
=\rho=\exp\!\left(\sum_{j=1}^{\infty}2^{-j-1}
\log\frac{P_{j+1}}{P_j}\right)
=1.53717671718234\ldots,
\]
where \(P_0=P_1=1\) and \(P_{j+1}=P_j+2P_{j-1}\) for \(j\ge1\). This concerns the invariant periodic-state set, not the probability of arriving at a particular orbit from a uniformly random arbitrary initial state.

For heights \(1,2,3,4\), the exact triples \((F_h,Q_h,N_h)\) are
\[
(2,4,1),\quad(6,20,7),\quad(30,612,291),\quad(990,591300,295155).
\]

## Assumptions and scope
Every vertex of \(T_h\) carries one binary state, either \(0\) or \(1\). The root has two neighbors, non-root internal vertices have three neighbors, and leaves have one neighbor. All vertices update simultaneously: a vertex takes the strict majority of its neighbors and, only on an exact tie, retains its own current color. Thus only the root can face a tie. Vertices and tree positions are distinguished (labelled). The claim holds for every integer \(h\ge1\), including the smallest three-vertex tree. An orbit of least period two is one unordered pair of distinct states \(\{x,F(x)\}\); configurations, rather than orbits, are sampled in the root-flip probability.

A configuration \(x\) is fixed when \(F(x)=x\), is two-step returning when \(F^2(x)=x\), and is primitive period two when \(F^2(x)=x\ne F(x)\). The general theorem that finite symmetric majority systems eventually have period at most two is prior work, not needed to count their periodic states here.

## Proof
**1. A temporal two-layer factorization.** Let a rooted planted full binary subtree of height \(k\) be attached to one external parent. Prescribe the parent's states at two successive times as \(p=(p_0,p_1)\) and the subtree root's states as \(s=(s_0,s_1)\). Let \(H_k(p,s)\) count assignments to all subtree vertices at the two times satisfying both local equations \(F(x)=y\) and \(F(y)=x\), with the parent's two values held fixed. One assignment is specified by its binary values at time zero and its prescribed time-one values; it is not weighted by automorphisms.

Put \(A_k(a,b)=u_k\) when \(a=b\), and \(A_k(a,b)=v_k\) otherwise. We prove
\[
H_k(p,s)=A_k(p_0,s_1)A_k(p_1,s_0).
\]
At height zero the subtree is a leaf: it follows the parent at the following update, so \(s_1=p_0\) and \(s_0=p_1\). Hence the formula holds with \(u_0=1,v_0=0\).

Suppose it holds for height \(k\). At a nonleaf planted root there are two child subtrees. Each of its update equations is a strict majority of three values: the parent and the two child roots, at one of the two times. In the sum over the children's temporal states, the two time layers factor independently, since each child contributes \(A_k(s_0,c_1)A_k(s_1,c_0)\). For prescribed parent time-zero color \(a\) and root time-one color \(b\), the weighted sum over two child time-zero colors equals \(u_k^2+2u_kv_k\) when \(a=b\), because at least one child must match \(b\); it equals \(u_k^2\) when \(a\ne b\), because both children must match \(b\). The other time layer is identical. This proves the factorization at height \(k+1\) and the displayed recurrence.

**2. Closing the tree at its root.** For \(T_h\), the two children of the root carry planted subtrees of height \(h-1\). If the root retains the same color in both phases, then at each update it must have at least one child with that color; a tie retains the root's state. Each time layer contributes \(u_{h-1}^2+2u_{h-1}v_{h-1}=u_h\). There are two choices of stable root color, contributing \(2u_h^2\) two-step returning configurations.

If instead the root flips between the phases, its two children must both have the opposite color at each update. Each time layer contributes \(u_{h-1}^2=v_h\). There are two orientations of the root's alternating colors, contributing exactly \(2v_h^2\) returning configurations. Hence \(Q_h=2(u_h^2+v_h^2)\) and the root-flip count is \(2v_h^2\).

**3. Subtracting fixed states without overcounting.** For time-independent colorings, the same planted-subtree computation uses just one time layer. Its weighted two-color boundary matrix is \(A_k\), with identical initial values and recurrence. At the complete root, the one-layer stable condition has weight \(u_{h-1}^2+2u_{h-1}v_{h-1}=u_h\) for each of its two possible colors. Thus \(F_h=2u_h\). Every nonfixed two-step returning configuration belongs to a unique two-element temporal orbit. Therefore \(N_h=(Q_h-F_h)/2=u_h^2+v_h^2-u_h\).

**4. Limiting root law.** For \(h\ge1\), \(v_h>0\). The ratios \(r_h=u_h/v_h\) satisfy \(r_1=1\) and \(r_{h+1}=1+2/r_h\). Defining \(P_0=P_1=1\), \(P_{j+1}=P_j+2P_{j-1}\), gives \(r_h=P_h/P_{h-1}\) and \(P_j=(2^{j+1}+(-1)^j)/3\). Consequently \(r_h\to2\). Furthermore \(u_h\to\infty\): \(u_2=3\), and from then onward \(u_{h+1}\ge u_h^2\). A flipping root rules out a fixed configuration, so among the \(Q_h-F_h\) primitive-period-two configurations the flipping-root fraction is
\[
\frac{2v_h^2}{2(u_h^2+v_h^2-u_h)}
=\frac{1}{r_h^2+1-u_h/v_h^2}\longrightarrow\frac15.
\]
The fixed fraction among *all* two-step returning configurations tends to zero by \(F_h/Q_h=u_h/(u_h^2+v_h^2)\to0\).

**5. Orbit-growth constant.** From \(u_{h+1}=u_h^2r_{h+1}\), with \(u_1=1\), one obtains
\[
\frac{\log u_h}{2^h}
=\sum_{j=1}^{h-1}2^{-j-1}\log r_{j+1}.
\]
Since \(1\le r_j\le3\), the series converges absolutely, with the tail starting at \(j=m\) bounded by \(2^{-m}\log3\). As \(N_h=u_h^2(1+r_h^{-2}-u_h^{-1})\) and the number of vertices is \(2^{h+1}-1\), the stated limit \(N_h^{1/(2^{h+1}-1)}=\rho\) follows. Substituting \(r_j=P_j/P_{j-1}\) gives the displayed series and rigorous numerical convergence.

## Verification
The standalone standard-library script `verify_majority_tree.py` independently computes rooted boundary-pair counts with a sixteen-entry dynamic program that does **not** use the two-layer factorization, and separately counts fixed states with a two-color stationary dynamic program, for heights one through eight. It also simulates every one of the \(2^3+2^7+2^{15}=32904\) labelled binary configurations at heights one, two, and three, testing both one-step fixedness and exact two-step return, and checks the root-flipping count. Run `python3 verify_majority_tree.py` in the directory containing that script; the recorded standard output is in `verify_majority_tree.output.txt`. All checks pass and end with `BINARY_TREE_MAJORITY_VERIFY_OK 8 independent_DP_heights_and_3_exhaustive_heights`.

The unbounded-height theorem is proved by the induction above; the finite checks are corroboration and do not establish it by extrapolation. The computed entropy constant is justified by the explicit geometric tail bound, not merely by floating-point fitting.

## Relationship to prior work
Goles and Olivos established eventual period at most two for symmetric finite threshold dynamics; this is background, not a contribution here. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486, first public 2014-05-11) analyze convergence, unanimity and disagreement, primarily on infinite/unimodular and random graphs; their results do not enumerate labelled periodic configurations on perfect binary trees.

Královič (2001) already counted fixed configurations of complete binary trees asymptotically; the fixed-point recurrence and its exponential rate are **not** claimed as independent discoveries. Turau (arXiv:2202.01580, 2022) characterizes fixed points, pure cycles and the block decomposition of mixed two-cycles on general finite trees, but does not state this all-cycle numerical census or the root one-fifth law, and identifies limitations to a complete enumeration. Turau (arXiv:2312.13769, 2023) explicitly computes fixed-point and **pure**-cycle counts, leaving mixed two-cycles outside that counting theorem. Benjamini, Zakharov and Zhukovskii (2026) give stabilization-time results for finite trees, a different statistic. The present claim is the exact all-periodic-state count, the mixed-cycle prevalence and its local root statistic, not the known general period bound or fixed-point enumeration.

## Limitations
The sample space consists of already periodic configurations; it is not a basin-size or random-initial-condition convergence-time law. The tree is perfect, rooted, binary, and uses tie retention at its degree-two root; the expressions need not hold for irregular trees, different root degrees, or other tie rules. The known fixed-point recurrence underlies the new two-time enumeration. A historically equivalent all-cycle enumeration may exist outside the inspected literature, especially because Královič's 2001 full text was not accessible. Independent external validation has not been performed.

## References
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI 10.1016/0012-365X(80)90121-1.
- R. Královič, *On majority voting games in trees*, SOFSEM 2001, LNCS 2234, 282–291, DOI 10.1007/3-540-45627-9_25 (abstract and subsequent literature inspected).
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (2014-05-11), https://arxiv.org/pdf/1405.2486.
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1 (2022), https://arxiv.org/pdf/2202.01580.
- V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769v1 (2023), https://arxiv.org/pdf/2312.13769.
- I. Benjamini, G. Zakharov and M. Zhukovskii, *Majority Dynamics on Finite Trees*, Random Structures & Algorithms 69 (2026), e70092, DOI 10.1002/rsa.70092.
