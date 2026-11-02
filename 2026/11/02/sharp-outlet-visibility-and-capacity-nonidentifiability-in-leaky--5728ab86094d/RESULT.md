# Sharp outlet visibility and capacity nonidentifiability in leaky fill-and-spill trees

## Finding

For every finite rooted drainage tree with at least two stores, positive local recharge at every store, positive linear leakage, and a positive linear spill coefficient above each store's threshold, the steady outlet discharge as a function of a common nonnegative recharge multiplier is continuous, nondecreasing, convex, and piecewise affine. Each store has one positive activation intensity. When these intensities are distinct, a store contributes a *visible* positive slope jump at the outlet **if and only if it activates after every store on its downstream path to the outlet**. An explicit product formula gives that jump. Thus the number of visible outlet thresholds is between one and the number of stores, and every integer in that interval is realized on every fixed rooted-tree topology by positive storage capacities.

More strongly, when the outlet store activates after all others, the *entire* observed outlet curve is a single hinge, and an open family of storage capacities of dimension one less than the number of stores generates precisely the same curve. The result concerns an exact steady-state forcing-response curve; it is not a claim about transient hydrographs or about arbitrary nonlinear or cyclic catchment models.

## Assumptions and scope

Let \(G\) be a finite rooted directed tree with \(n\ge2\) vertices, oriented from the upstream children \(C(i)\) toward the unique outlet root \(r\). Each vertex has strictly positive local recharge coefficient \(w_i\), linear leakage coefficient \(\ell_i\), spill coefficient \(k_i\), and storage threshold \(V_i\). A spatially uniform nonnegative forcing multiplier \(I\) supplies local water at rate \(w_i I\); all spill from a child reaches its parent. The equilibrium storage \(S_i(I)\ge0\) and spill \(q_i(I)\ge0\) obey

\[
 w_i I+\sum_{j\in C(i)}q_j(I)
 =\ell_iS_i(I)+q_i(I),
 \qquad q_i(I)=k_i(S_i(I)-V_i)_+,
\]

where \((z)_+=\max\{z,0\}\). The observable is \(Q(I)=q_r(I)\) for all \(I\ge0\). No lateral recirculation, negative routing fractions, storage-dependent recharge or measurement error is assumed. Rates \(w_i,\ell_i,k_i\) are regarded as known in the capacity-identifiability assertion.

Set \(\beta_i=k_i/(k_i+\ell_i)\in(0,1)\) and let

\[
F_i(I)=w_iI+\sum_{j\in C(i)}q_j(I),\qquad
q_i(I)=\beta_i\big(F_i(I)-\ell_iV_i\big)_+.
\]

Each \(F_i\) is strictly increasing and has a unique crossing \(t_i>0\) of \(\ell_iV_i\), called the activation intensity of vertex \(i\). The *ancestors* \(A(i)\) are its strict downstream vertices on the unique path to \(r\). For pairwise distinct activation intensities, the exact visibility and slope-jump formula are

\[
\Delta Q'(t_i)=
\begin{cases}
 \displaystyle \beta_iF_i'(t_i^-)\prod_{a\in A(i)}\beta_a,
 & t_a<t_i\quad\text{for all }a\in A(i),\\
 0,&\text{otherwise.}
\end{cases}
\]

Here \(F_i'(t_i^-)\ge w_i>0\), an empty product is one, and \(\Delta Q'(t_i)=Q'_+(t_i)-Q'_-(t_i)\). Thus an activation is visible exactly when the displayed quantity is positive. Even without the distinctness assumption, \(Q\) has no more than \(n\) positive slope jumps.

## Proof

**1. Exact equilibrium elimination.** For any prescribed input \(F_i\ge0\), the right-hand side of the balance equation is strictly increasing in storage. If \(F_i\le\ell_iV_i\), then \(S_i=F_i/\ell_i\) and \(q_i=0\). Otherwise \(S_i=(F_i+k_iV_i)/(\ell_i+k_i)\) and \(q_i=k_i(F_i-\ell_iV_i)/(\ell_i+k_i)\). Hence the displayed hinge recursion follows, is unique, and determines every vertex by induction from leaves to root. Positivity of the coefficients and a positive input give nonnegative storage throughout.

**2. Shape and activation.** At a leaf, \(F_i(I)=w_iI\), so its spill is continuous, nondecreasing, convex, piecewise affine, and nonnegative. If every child's spill has these properties, their sum plus \(w_iI\) is continuous, convex, nondecreasing, and strictly increasing. The positive-part operation preserves all those properties and piecewise affinity. Moreover \(F_i(0)=0<\ell_iV_i\), while \(F_i(I)\ge w_iI\to\infty\), so a unique \(t_i>0\) exists. The only possible derivative discontinuities of \(q_i\) occur at its own activation or at those of its descendants. The assertion follows at the root, including the upper bound of \(n\) total distinct hinge locations. In particular, at its own activation \(t_i\), if all activation intensities are distinct, \(F_i\) is affine near \(t_i\), and \(q_i\) changes derivative from zero to \(\beta_iF_i'(t_i^-)\).

**3. Exact visibility.** Fix one activation \(t_i\) and suppose no other vertex activates at the same intensity. Its local positive derivative jump must propagate along the unique directed path to the outlet. At a strict downstream ancestor \(a\) that is already active (\(t_a<t_i\)), the recursion is locally linear in its incoming spill, multiplying the arriving jump by \(\beta_a\). At an ancestor not yet active (\(t_a>t_i\)), its spill is identically zero in a neighborhood of \(t_i\), so the jump is blocked and cannot reappear at that same intensity. There are no cancellations, because all coefficients are positive. Multiplication along the path proves the stated exact formula and its necessary-and-sufficient positivity condition.

**4. Every number of visible kinks is attainable.** Fix any positive values of the rates and any set of distinct desired positive activation intensities \((t_i)\). Choose capacities upward from the leaves, setting

\[
 V_i=F_i(t_i)/\ell_i
\]

once its children's spill functions have been defined. Every capacity is strictly positive because \(F_i(t_i)\ge w_it_i>0\). The unique crossing of each store is then exactly the prescribed \(t_i\); thus any distinct positive activation ordering is realizable. For an integer \(m\in\{1,\ldots,n\}\), choose any \(m-1\) nonroot vertices as a set \(H\). Assign every vertex outside \(H\cup\{r\}\) distinct intensities below one, assign the root intensity two, and assign members of \(H\) distinct intensities above two, ordered so that every selected downstream ancestor precedes its selected upstream descendants. By step 3 exactly the root and the \(m-1\) selected vertices are visible. This proves sharpness on every tree.

**5. A full-dimensional hidden-capacity family.** Fix a target outlet activation \(T>0\), fix the tree and all \(w_i,\ell_i,k_i\), and freely choose each nonroot capacity in the open interval

\[
0<V_i<\frac{w_iT}{\ell_i}\qquad(i\ne r).
\]

Because \(F_i(T)\ge w_iT>\ell_iV_i\), every nonroot vertex activates strictly before \(T\), regardless of the other freely chosen capacities. Set the root capacity to \(V_r=F_r(T)/\ell_r>0\). Then the root activates exactly at \(T\), and the observable is zero on \([0,T]\). For \(I>T\) all stores are active; differentiating the affine recursions upward gives constant slopes

\[
L_i=\beta_i\left(w_i+\sum_{j\in C(i)}L_j\right)>0.
\]

These slopes depend on the fixed rates and topology but **not** on any capacity. Since \(Q(T)=0\), continuity gives

\[
\boxed{Q(I)=L_r(I-T)_+\qquad\text{for every }I\ge0.}
\]

The \(n-1\) freely varying nonroot capacities form an open box, and the root capacity is a uniquely determined positive continuous function of them; hence this is an \((n-1)\)-dimensional graph of observationally indistinguishable positive capacities. For \(n=2\), take unit coefficients \(w_i=\ell_i=k_i=1\). Capacities \((V_r,V_{\mathrm{leaf}})=(4,1)\) and \((7/2,2)\) both give exactly \(Q(I)=\tfrac34(I-3)_+\) for all \(I\ge0\), despite different local activation intensities.

## Verification

The standalone \(\texttt{ffspill_check.py}\) uses rational arithmetic only. It derives capacities from specified activation intensities, replays equilibrium discharge values immediately to either side of each vertex activation, checks the exact derivative-jump formula and the visible-path equivalence, tests arbitrary counts of visible kinks, and verifies identical full output curves for distinct capacity vectors. The deterministic campaign counted 10,720 exact-rational network/vertex comparisons, with multiple assertion checks within many comparisons. Execute using \(\texttt{python ffspill_check.py}\) in the same folder. The proof above is the infinite-family justification; finite tests are consistency checks, not substitutes for its induction and construction.

## Relationship to prior work

Tromp-van Meerveld and McDonnell (2006) established fill-and-spill connectivity as a physical explanation for hillslope runoff thresholds. Graham and McDonnell (2010) explicitly modeled thresholded subsurface reservoirs and bedrock leakage in a numerical catchment framework. Chu et al. (2015) documented stepwise connectivity in microrelief-driven experiments; McDonnell et al. (2021) emphasized that macroscopic runoff requires locally filled stores to become connected. Those physical concepts are the motivation, not claimed discoveries. The statement here is an exact theorem for a *distinct, restricted, steady linear-leakage tree model*: strict convexity of the slope changes, a necessary-and-sufficient visibility test, a sharp realizability classification for every number of observed breaks, and a constructive \((n-1)\)-dimensional nonidentifiability set. It does not purport to reproduce the transient quantitative predictions of those papers.

The mathematical recurrence is a nonnegative feed-forward positive-part network. Rolnick and Kording (2019) treat reverse engineering of general ReLU networks when sufficiently intersecting activation boundaries are visible. Their reconstruction hypotheses are not satisfied by distinct activation thresholds along one scalar forcing axis in the hidden-capacity case, and their conclusions do not imply identification of those capacities. The overlapping piecewise-linearity observation is acknowledged. The 2013 dynamic puddle-network article of Chu and collaborators was identified but its complete text was not inspected; the precise scope of any earlier exact steady-state identifiability result therefore remains a priority risk.

## Limitations

The forcing is held constant until steady state and is not an individual storm or a real-time discharge trace. Every local recharge is strictly positive, the routing tree is acyclic with one outlet, leakage and above-threshold spill are linear, routing is lossless along each edge, and all coefficients except capacities are fixed in the indistinguishability construction. The strict visibility formula assumes pairwise distinct activation intensities; coincident activations merge changes and remain within the general \(n\)-kink upper bound. The theorem does not establish noisy finite-sample inference, identify a real catchment, predict a flood hydrograph, or handle multiple outlets or nonlinear flow laws. Historical priority has not been independently established.

## References

1. H. J. Tromp-van Meerveld and J. J. McDonnell, “Threshold relations in subsurface stormflow: 2. The fill and spill hypothesis,” *Water Resources Research* 42 (2006), DOI: 10.1029/2004WR003800; first published 21 February 2006. https://doi.org/10.1029/2004WR003800
2. C. B. Graham and J. J. McDonnell, “Hillslope threshold response to rainfall: (2) Development and use of a macroscale model,” *Journal of Hydrology* 393 (2010), 77–93, DOI: 10.1016/j.jhydrol.2010.03.008. https://research.fs.usda.gov/download/treesearch/39620.pdf
3. X. Chu, J. Yang, Y. Chi, and J. Zhang, “Dynamic puddle delineation and modeling of puddle-to-puddle filling-spilling-merging-splitting overland flow processes,” *Water Resources Research* 49 (2013), 3825–3829, DOI: 10.1002/wrcr.20286. https://doi.org/10.1002/wrcr.20286
4. X. Chu, G. Padmanabhan, and D. Bogart, “Microrelief-Controlled Overland Flow Generation: Laboratory and Field Experiments,” *Applied and Environmental Soil Science* (2015), DOI: 10.1155/2015/642952. https://doi.org/10.1155/2015/642952
5. J. J. McDonnell et al., “Fill-and-Spill: A Process Description of Runoff Generation at the Scale of the Beholder,” *Water Resources Research* 57 (2021), DOI: 10.1029/2020WR027514. https://doi.org/10.1029/2020WR027514
6. D. Rolnick and K. P. Kording, “Reverse-Engineering Deep ReLU Networks” (2019), arXiv:1910.00744. https://arxiv.org/abs/1910.00744
