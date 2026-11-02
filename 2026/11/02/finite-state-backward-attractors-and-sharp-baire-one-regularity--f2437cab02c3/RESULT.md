# Finite-state backward attractors and sharp Baire-one regularity for expanding Markov interval maps

## Finding

Let \(f:[0,1]\to[0,1]\) be a continuous surjective, uniformly expanding, piecewise-affine Markov map with a finite partition as specified below. The backward-attractor multifunction \(x\mapsto\beta_f(x)\), equipped with the Hausdorff metric on nonempty compact subsets of \([0,1]\), has finite range, is constant on every open Markov atom, and is of Baire class at most one. The bound is sharp: a four-branch slope-\(2\) map has a discontinuous backward-attractor multifunction.

More precisely, form the finite graph \(G\) whose vertices are all open Markov atoms and all singleton partition endpoints. Draw \(U\to V\) whenever \(V\subset f(U)\). A strongly connected component (SCC) is **cyclic** if it contains a directed cycle. For a cyclic SCC \(C\), let \(K_C\) be the closure of the union of all periodic orbits obtained by closing directed cycles within \(C\) and taking the unique fixed point of their contracting inverse compositions; singleton endpoint cycles give their actual finite periodic orbits. If \(V(x)\) is the unique graph cell containing \(x\), then the exact formula is

\[
\boxed{\displaystyle \beta_f(x)=\bigcup_{C\text{ cyclic SCC}:\ C\leadsto V(x)}K_C.}
\]

Here \(C\leadsto V\) means that some vertex of \(C\) has a directed path to \(V\), with paths of length zero permitted. This produces a finite graph algorithm for the set-valued dependence on \(x\), as well as a sharp partial answer to the Baire-class question for surjective interval maps.

## Assumptions and scope

Take \(0=c_0<c_1<\cdots<c_m=1\) such that \(f(c_i)\) is a partition point for each \(i\), and the restriction of \(f\) to every closed branch \([c_{i-1},c_i]\) is affine and strictly monotone, with \(|f'|\ge\lambda>1\). Continuity and surjectivity are assumed on the entire interval. Graph cells consist of \(J_i=(c_{i-1},c_i)\) and \(P_i=\{c_i\}\); hence each \(x\) belongs to exactly one cell. The Markov endpoint hypothesis ensures that for every source cell \(U\) and target cell \(V\), either \(V\subset f(U)\) or \(V\cap f(U)=\varnothing\). The endpoint vertices ensure that the claim includes **every** partition point, not merely almost every point.

For an infinite coherent backward orbit \(x_0=x\), \(f(x_{-n})=x_{-n+1}\), denote its accumulation set by \(\alpha((x_{-n})_{n\ge0})\). We use the backward-attractor convention

\[
\beta_f(x)=\overline{\bigcup\{\alpha((x_{-n})_{n\ge0}):x_0=x,\ f(x_{-n})=x_{-n+1}\}}.
\]

The hyperspace \(\mathcal K([0,1])\) comprises nonempty compact subsets with the Hausdorff metric. The conclusion is specific to finite expanding affine Markov partitions; it makes no general assertion for arbitrary continuous surjections, non-Markov critical maps, or non-expanding interval maps.

## Proof

**1. Exact graph coding.** Because each branch is strictly affine and all branch-image endpoints are partition points, an edge \(U\to V\) means every point of \(V\) has exactly one predecessor in \(U\). In particular this holds for singleton endpoint targets when the endpoint lies in the interior of the open image of \(U\). Thus every backward orbit gives a left-infinite walk \(\cdots\to V_2\to V_1\to V_0=V(x)\), and conversely every such walk admits a unique recursively lifted backward orbit starting at the specified \(x\).

**2. Eventual cyclic component.** In the finite SCC condensation graph, directed walks cannot visit distinct SCCs in a directed cycle. Reading the infinite backward walk backwards therefore shows that its far-past tail eventually remains within a single SCC \(C\). An infinite path within an SCC implies that \(C\) is cyclic. A cyclic SCC is entirely an interval-cell component or entirely a singleton-endpoint component: singleton endpoint cells map only to endpoint cells, so a directed path cannot return from a singleton to an open atom.

**3. Orbit upper bound.** Fix an orbit whose far-past cells lie in cyclic \(C\). If \(C\) consists of endpoints, all far-past points belong to the finite periodic orbit of that singleton SCC, contained in \(K_C\). Otherwise, for each positive integer \(k\), a sufficiently far-past point \(x_{-n}\) follows a directed \(k\)-step word in \(C\). Strong connectivity closes that word to a cycle inside \(C\); repeating the inverse affine branches around the cycle gives a unique periodic point \(p\) with the same initial \(k\)-step word. The corresponding closed \(k\)-cylinder has diameter at most \(\lambda^{-k}\), since each inverse branch contracts by at least \(\lambda^{-1}\). Hence \(\operatorname{dist}(x_{-n},K_C)\le\lambda^{-k}\) for all sufficiently large \(n\). As \(k\) is arbitrary, the orbit's accumulation set is contained in \(K_C\). Taking the union and closure over backward orbits gives

\[
\beta_f(x)\subseteq\bigcup_{C\leadsto V(x),\ C\text{ cyclic}}K_C.
\]

This is a finite union of closed sets.

**4. Orbit lower bound.** Fix a directed cycle within cyclic \(C\) and a path from \(C\) to \(V(x)\). By strong connectivity, extend the path to start at any chosen phase of the cycle. Lift its edges backwards from \(x\), then continue indefinitely by repeating the inverse branches around the chosen cycle. Uniform contraction forces its backward trajectory to converge along cycle phases to the unique periodic inverse-cycle point, so that whole periodic orbit is in the backward orbit's accumulation set. Every cycle in each reachable \(C\) thus contributes to \(\beta_f(x)\), and taking closures yields \(K_C\subseteq\beta_f(x)\). This proves the boxed equality, with endpoints handled by their exact singleton-state paths.

**5. Finite range and Baire-one regularity.** The formula depends on \(x\) only through its finite partition cell, so the multifunction is constant on every \(J_i\) and can only be discontinuous at the finitely many \(c_i\). It is Baire-one **in the Hausdorff hyperspace**, not merely as a scalar indicator. For compact nonempty \(A,B\subset[0,1]\), define the continuous Hausdorff-metric arc \(H_{A,B}(t)=(1-t)A+tB\), where the right side is a Minkowski sum. Interpolate the left atom value to the endpoint value and back to the right atom value inside windows of width \(1/n\) around each partition point, keeping each endpoint's prescribed value. The resulting hyperspace-valued maps are continuous and converge pointwise to \(\beta_f\). This proves Baire class at most one.

**6. Sharp example.** Let the partition be \(0,1/4,1/2,3/4,1\) and linearly interpolate

\[
(f(0),f(1/4),f(1/2),f(3/4),f(1))=(1/2,0,1/2,1,1/2).
\]

All four slopes have magnitude \(2\), and \(f\) is a continuous surjection. The two left open atoms form one full-branch cyclic SCC with \(K_{\rm L}=[0,1/2]\), and the two right open atoms form another with \(K_{\rm R}=[1/2,1]\). The midpoint singleton is a cyclic component with \(K_{\rm mid}=\{1/2\}\). The two open components each reach the midpoint, but neither reaches the other's open atoms. Consequently

\[
\beta_f(x)=[0,1/2]\quad(0<x<1/2),\qquad
\beta_f(1/2)=[0,1],\qquad
\beta_f(x)=[1/2,1]\quad(1/2<x<1).
\]

The Hausdorff jump at the midpoint is nonzero from either side; hence Baire class zero is impossible in general, and class one is optimal.

## Verification

The attached standalone `verify_example.py` checks the four exact rational affine branches, all nine endpoint/open-atom graph vertices, its three cyclic SCCs, all source-to-target reachability relations used above, and 80 exact-rational interior affine evaluations. Run `python3 verify_example.py`; a successful run prints a `VERIFY_OK` line. This finite check verifies the explicit example; it is **not** a substitute for the general infinite-path argument in steps 1–5.

## Relationship to prior work

Hantáková and Roth introduce backward attractors and explicitly ask in Problem 49 for the Baire class of the backward-attractor map of a surjective interval map (arXiv:2007.10883, v1, 2020-07-21). Their general theory provides structural results about backward limit sets, but the inspected definitions and Problem 49 do not yield the present finite-state SCC formula or the optimal hyperspace Baire-one classification for expanding affine Markov maps.

Foryś-Krawiec, Hantáková and Oprocha examine individual backward-trajectory alpha-limit sets for graph maps (arXiv:2106.05539, v1, 2021-06-10), including mixing restrictions. The relevant inspected statements do not give the pointwise backward-attractor **multifunction** formula or this Baire-class conclusion. The graph construction is an application of familiar Markov symbolic coding, so broader symbolic-dynamics literature might imply parts of the formula without using this terminology; a search for such coverage remains an important priority risk.

## Limitations

The claim is for finite uniformly expanding piecewise-affine Markov maps and the specified definition of \(\beta_f\). It does not resolve the unrestricted Baire-class problem for all continuous surjective interval maps. The effective graph expression uses closures of periodic-code orbit sets \(K_C\), which need not be finite or intervals for general Markov matrices. Only a self-review has been performed; no independent scientific audit or exhaustive priority certification has occurred.

## References

1. J. Hantáková and S. Roth, *On backward attractors of interval maps*, arXiv:2007.10883v1, first publicly posted 2020-07-21, especially the backward-attractor definition and Problem 49. https://arxiv.org/abs/2007.10883
2. A. Foryś-Krawiec, J. Hantáková and P. Oprocha, *On structure of alpha-limit sets of backward trajectories for graph maps*, arXiv:2106.05539v1, first publicly posted 2021-06-10. https://arxiv.org/abs/2106.05539
