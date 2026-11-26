# Universal exceptional-set dimension for a chaotic planar invariant graph

## Finding

For \(2\le b\le4\), let \(F_b(x,y)=(|x|-y-1,x-|y|+b)\), and let \(\Gamma_b\) be the compact invariant graph of Cima, Gasull, Mañosa and Mañosas [1], including any associated isolated invariant points. Let \(\mathcal P_b\) be the union of the nondegenerate closed graph segments on which \(F_b\) is constant. Define the plateau-avoiding set
\[
E_b=\Gamma_b\setminus\bigcup_{n\ge0}(F_b|_{\Gamma_b})^{-n}(\mathcal P_b).
\]
Then
\[
\dim_{\mathrm H}E_b=\frac{\log(1+\sqrt2)}{\log4}\approx0.6358.
\]
This is an exact metric refinement of full arclength absorption, which is already covered by the broader theorem in [3].

On the edge \(C_b=\{(u,u+b+1):-b\le u\le0\}\), there are three noncollapsing full first-return branches on their interiors, of lengths \(3,4,7\). Their inverse maps, extended to the closed coordinate interval \([-b,0]\), are
\[
\psi_{3,b}(w)=\frac{w-b-4}{4},\qquad
\psi_{4,b}(w)=\frac{w+b-4}{4},\qquad
\psi_{7,b}(w)=-\frac{w+b+20}{16}.
\]
The corresponding separated Cantor set \(K_b\) in the coordinate \(u\) has the same Hausdorff dimension as \(E_b\). At depth \(k\), the union of the \(k\)-return cylinders has total coordinate length \(b(9/16)^k\) (arclength is \(\sqrt2\) times coordinate length). Return depth counts visits to \(C_b\), not iterates of \(F_b\).

## Assumptions and scope

The parameter range is the entire closed interval \([2,4]\). The graph is the finite union of compact straight segments in [1], rather than a numerical attractor. We use one-dimensional Hausdorff measure on the graph and include plateau endpoints in the hole. Finite graph boundary sets only cause countable exceptions when pulled back along noncollapsing itineraries. The statements address graph survivors, not planar Lebesgue measure.

## Proof

**1. Exhaustion of the noncollapsing itineraries.** Use the vertices of [1, §5.7 and Appendix Figs. 60–61], whose coordinates are
\[
\begin{array}{llll}
P_1=(-b-2,-1),&P_2=(b+2,-3),&P_3=(b+4,2b-1),&P_4=(4-b,5),\\
S=(0,b+1),&X_1=(0,-1),&X_2=(0,b-1),&X_3=(-b,1),\\
X_4=(b-2,-1),&Y_1=(b-1,0),&Y_2=(b-2,2b-1),&Z_1=(-b-1,0),\\
Z_2=(b,-1),&Z_3=(b,2b-1).& &
\end{array}
\]
Write \([U,V]\) for a closed segment joining vertices. The eight core edges and their images are
\[
\begin{array}{c|c|l}
  &\text{segment}&F_b(\text{segment})\\\hline
A &[Z_3,P_3]&C\cup[S,P_4]\\
B &[Y_2,Z_3]&D\cup[Z_1,X_3]\\
C &[X_3,S]&E\cup[X_1,X_4]\\
D &[P_1,Z_1]&G\\
E &[P_1,X_1]&H\cup I\cup G\\
G &[Z_2,P_2]&A\\
H &[X_2,Y_1]&C\cup[S,Y_2]\\
I &[Y_1,Z_2]&B
\end{array}
\]
These equalities follow by applying the quadrant-affine formula on each segment and mapping its endpoints. Each restriction in the table is affine and nonconstant. The remaining positive-length parts of the graph lie on the following four segments (sharing endpoints as necessary): \([Z_1,X_3]\), \([X_1,Z_2]\), \([X_2,Z_3]\), and the portion of the line \(y=x+b+1\) joining \(S\) to the farther of \(P_4,Y_2\). The first maps into the second, the second onto the third, and the third collapses to \(X_3\). The fourth collapses to \(P_1\). These facts also follow by endpoint substitution and the quadrant formulas. They apply both when \(X_1=X_4\) at \(b=2\) and when \(P_4=S\) at \(b=4\). Any associated isolated invariant points have dimension zero.

For an orbit avoiding plateaus and partition vertices, the only possible infinite paths are in the eight core edges. Every directed cycle among those edges passes through \(C\), so such an orbit reaches \(C\) and returns infinitely often. Conversely, an itinerary strictly on noncollapsing branches of this core avoids plateaus. For each fixed time, preimages of the finitely many vertices along noncollapsing branches are finite, because the affine restrictions can be subdivided into finitely many injective pieces at that time. Their union over all times is countable. This treatment of vertices does not require that preimages through a constant branch be countable: those histories already hit a plateau.

**2. Return geometry.** On \(C\), write the starting point as \((u,u+b+1)\). On the portion mapping into \(E\), the next point is \((-2u-b-2,-1)\), and the following point is \((t,b-1-t)\), where \(t=2u+b+2\). The only possible uninterrupted core paths back are \(C\to E\to H\to C\), \(C\to E\to G\to A\to C\), and \(C\to E\to I\to B\to D\to G\to A\to C\).

On the \(H\) path, \(t\) is between 0 and \(b-1\); applying \(F_b\) gives \((2t-b,2t+1)\). The part returning to \(C\) is exactly \(0\le t\le b/2\). On the \(G\) path, \(b\le t\le b+2\); the next two maps give \((2t-b,2b-1)\) and \((2t-3b,2t-2b+1)\). The part returning to \(C\) is \(b\le t\le 3b/2\), which lies within \([b,b+2]\) since \(b\le4\). On the \(I\) path, \(b-1\le t\le b\); the same first two formulas now give points on \(B\) and on \(D\) or its transient continuation. To stay on \(D\), require \(t\le b-1/2\). The next two points are \((5b-4t-2,4t-4b+1)\) on \(G\) and \((9b-8t-4,2b-1)\) on \(A\). The final first coordinate is \(7b-8t-4\); requiring that it belong to \([-b,0]\) gives \((7b-4)/8\le t\le b-1/2\). This interval lies within \([b-1,b]\) when \(b\le4\). At every endpoint of the parameter range the full branch interiors are nonempty, and endpoint orbit equalities are interpreted by continuity.

In the starting coordinate \(u\) the three return maps therefore have first coordinates \(4u+b+4\), \(4u-b+4\) and \(-16u-b-20\). Each covers \([-b,0]\) on its closed branch extension, giving precisely the displayed inverses. The inverse image intervals in increasing order are
\[
[-b/2-1,-b/4-1],\qquad [-(b+20)/16,-5/4],\qquad [-1,(b-4)/4].
\]
They lie in \([-b,0]\) throughout \([2,4]\), with two gaps of lengths \((3b-4)/16\) and \(1/4\). The similarity ratios are \(1/4,1/16,1/4\) in this order. Thus their total retained length fraction is \(9/16\) per return depth; disjointness and repeated similarity give the exact cylinder length formula.

**3. Dimension.** Up to the countable endpoint histories, the infinite-return subset of \(C\) is the compact self-similar set \(K_b\). By strong separation its Hausdorff dimension \(s\) solves \(2\cdot4^{-s}+16^{-s}=1\); solving the quadratic in \(4^{-s}\) gives \(s=\log(1+\sqrt2)/\log4>0\). Removing countably many points leaves this positive dimension unchanged. Every other plateau-avoiding point, apart from the isolated points and boundary histories, is a finite noncollapsing preimage of this set. On each finite itinerary the inverse is affine and injective in the edge coordinate, preserving its subset's dimension. The countable-union and monotonicity properties give \(\dim_{\mathrm H}E_b=s\). Since \(s<1\), this also recovers full arclength absorption on the graph.

## Verification

The supplied `verify_three_returns.py` checks 147 rational orbit identities across seven parameter values, including \(2\) and \(4\), and checks the interval ordering, widths, and selected intermediate signs. The uniform affine calculations and graph exhaustion above, not the finite checks, establish the result for all real parameters in the interval.

## Relationship to prior work

Cima et al. [1] construct the graph, give the Markov covering and return circuit lengths \(3,4,7\), and compute topological entropy. Their open-dense plateau-preimage theorem does not determine arclength or exact dimension. Their follow-up's full-measure ranges [2] do not include \([2,4]\), but the all-parameter arclength absorption theorem [3] implies the arclength corollary here: its hole contains the interiors of the plateau segments, hence is contained in the closed-plateau hole used here. That theorem does not give a Hausdorff-dimension formula. The quantitative result here is the explicit separated inverse-return construction, its exact return-depth length law, and the resulting metric dimension. A later catalogue entry [4] gives the same core-survivor dimension by graph-directed similarities and adds a finite-time arclength law in map iterates rather than in return depth.

## Limitations

This concerns the canonical invariant graph, not the ambient planar basin. No dimension or return construction outside \([2,4]\) is asserted. Time to plateau entry measured in iterates is different from the number of completed returns; the return-depth fraction \(9/16\) does not assert an escape factor per iterate.

## References

1. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052, §5.7, Proposition 38 and Appendix Figs. 60–61. https://arxiv.org/abs/2410.01052
2. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Further results for a family of continuous piecewise linear planar maps*, arXiv:2503.02411, Theorem 3 and Propositions 10–11. https://arxiv.org/abs/2503.02411
3. *Full arclength absorption by flat branches for every parameter in a planar absolute-value family*, Resultary, 2026-10-18. https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-full-arclength-absorption-by-flat-branches-for-every-parameter-i--335be622e78a/RESULT.md
4. *Universal survivor dimension and sharp arclength escape on a planar invariant graph*, Resultary, 2026-11-08. https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-universal-survivor-dimension-and-sharp-arclength-escape-on-a-pla--d62f7b3284a3/RESULT.md
5. J. E. Hutchinson, *Fractals and self-similarity*, Indiana University Mathematics Journal 30 (1981), 713–747.
