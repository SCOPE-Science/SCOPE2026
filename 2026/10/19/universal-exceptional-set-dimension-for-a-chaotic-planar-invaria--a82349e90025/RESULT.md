# Universal exceptional-set dimension for a chaotic planar invariant graph

## Finding

For every real parameter \(2\le b\le4\), consider the continuous planar map
\[
F_b(x,y)=(|x|-y-1,\ x-|y|+b).
\]
Let \(\Gamma_b\) be its compact invariant graph of Cima, Gasull, Mañosa and Mañosas (2024), described in their Section 5.7 and Appendix, with any isolated invariant points included. Let \(\mathcal P_b\) be the union of all nondegenerate closed graph segments on which \(F_b\) is constant (its plateaus). Define the exceptional set
\[
E_b=\Gamma_b\setminus\bigcup_{n\ge0}(F_b|_{\Gamma_b})^{-n}(\mathcal P_b).
\]
Then
\[
\boxed{\dim_{\mathrm H} E_b=\frac{\log(1+\sqrt2)}{\log4}\approx0.6358.}
\]
In particular, the union of all plateau preimages has **full one-dimensional Hausdorff (arclength) measure on \(\Gamma_b\)** for every \(b\in[2,4]\). This establishes the full-measure plateau-attraction assertion for an entire parameter interval not covered by the previously published sufficient ranges.

There is an explicit dynamically defined Cantor set realizing the dimension. On the graph edge
\[
C_b=\{(u,u+b+1):-b\le u\le0\},
\]
write the three inverse first-return contractions, in the coordinate \(u\), as
\[
\psi_{3,b}(w)=\frac{w-b-4}{4},\qquad
\psi_{4,b}(w)=\frac{w+b-4}{4},\qquad
\psi_{7,b}(w)=-\frac{w+b+20}{16}.
\]
They have mutually disjoint image intervals, with contraction ratios \(1/4,1/4,1/16\). The attractor \(K_b\) of these three contractions satisfies \(\dim_{\mathrm H}K_b=\dim_{\mathrm H}E_b\). Its \(k\)-th stage has total coordinate length exactly \(b(9/16)^k\).

## Assumptions and scope

All parameters are real and include both endpoints \(b=2\) and \(b=4\). The invariant graph and plateaus are those of the exact planar map displayed above, not a numerically reconstructed attractor. The graph is a finite union of compact straight segments (and possibly isolated points), so arclength means one-dimensional Hausdorff measure. A plateau is a positive-length interval contained in the graph where \(F_b\) is constant; it includes its endpoints by convention. Different endpoint conventions change only countably many forward/backward boundary orbits and never the dimension or full-measure conclusions. The theorem concerns graph arclength, **not** an assertion of full two-dimensional Lebesgue measure on the ambient plane.

## Proof

**Step 1: the noncollapsing graph.** For \(2\le b\le4\), the invariant graph and its absorbing flat edges are explicitly listed in Cima et al., Section 5.7 and Appendix Figures 60–61. Removing those flat edges and their finite-time predecessors leaves eight relevant Markov segments, denoted \(A,B,C,D,E,I,G,H\) in that paper. Their nonconstant covering relations are
\[
A\to C,\quad B\to D,\quad C\to E,\quad D\to G,\quad
E\to H,I,G,\quad I\to B,\quad G\to A,\quad H\to C.
\]
Images may additionally enter the already removed flat part. Every directed circuit in these eight segments passes through \(C\), and the remaining edges of the original finite graph have only transient paths to this eight-edge system or to plateaus. Consequently, except for a countable set of boundary preimages and isolated periodic points, any orbit avoiding the plateaus forever reaches \(C\) and then revisits it infinitely often. Conversely, a point with a strict infinite itinerary through the system avoids every plateau. The exceptional set is therefore, modulo a countable set, a countable union of affine finite-itinerary inverse images of the infinite-return subset of \(C\).

**Step 2: exact return branches.** Parameterize \(C\) by \((u,u+b+1)\) for \(-b\le u\le0\). On the noncollapsing part, its first image belongs to the horizontal edge \(E\) and has first coordinate \(-2u-b-2\). After the next iterate the orbit is \((t,b-1-t)\), where \(t=2u+b+2\). There are precisely three possible noncollapsing paths back to \(C\):
\[
C\to E\to H\to C,\qquad
C\to E\to G\to A\to C,\qquad
C\to E\to I\to B\to D\to G\to A\to C.
\]
Their lengths are respectively \(3,4,7\). Direct substitution into the four quadrant-wise affine formulas gives the return coordinate
\[
R_b(u)=
\begin{cases}
4u+b+4,&\text{on the length-3 path},\\
4u-b+4,&\text{on the length-4 path},\\
-16u-b-20,&\text{on the length-7 path}.
\end{cases}
\]
All three branches cover the full coordinate interval \([-b,0]\). Their inverse branches are exactly \(\psi_{3,b},\psi_{4,b},\psi_{7,b}\) as stated.

To verify the quadrant restrictions for all parameters, the intermediate coordinate \(t\) on the length-3 inverse branch ranges through \([0,b/2]\), contained in the edge \(H\) for \(b\ge2\). On the length-4 inverse branch it ranges through \([b,3b/2]\), contained in the edge \(G\) because \(b\le4\). On the length-7 inverse branch it ranges through \([(7b-4)/8,b-1/2]\), contained in \(I\), and its subsequent image traverses \(B,D,G,A\) in that order. Thus these are genuine full branches, not merely formal affine compositions.

Their ordered coordinate image intervals are
\[
\begin{aligned}
\psi_{3,b}([-b,0])&=[-b/2-1,-b/4-1],\\
\psi_{7,b}([-b,0])&=[-(b+20)/16,-5/4],\\
\psi_{4,b}([-b,0])&=[-1,(b-4)/4].
\end{aligned}
\]
For every \(2\le b\le4\), these intervals lie inside \([-b,0]\) and have positive gaps: the first gap is \((3b-4)/16\ge1/8\), and the second gap is \(1/4\). The inverse system therefore satisfies strong separation uniformly on the entire closed parameter interval.

**Step 3: dimension and full measure.** The infinite-return subset is the invariant Cantor set of this three-map iterated function system, except possibly for finite-itinerary boundary points. At stage \(k\), its basic intervals are disjoint and have total length
\[
b\bigl(1/4+1/4+1/16\bigr)^k=b(9/16)^k.
\]
Hence the Cantor set has zero arclength. The strong-separation form of the self-similar dimension theorem (or the standard covering upper bound together with the separated-cylinder mass-distribution lower bound) gives the unique \(s>0\) satisfying
\[
2\cdot4^{-s}+16^{-s}=1.
\]
Putting \(v=4^{-s}\), we obtain \(v^2+2v=1\), so \(v=\sqrt2-1\) and
\[
s=\log(1+\sqrt2)/\log4.
\]
Affinely nonconstant inverse branches preserve Hausdorff dimension. Because every noncollapsing infinite itinerary is, apart from countably many exceptional endpoints or isolated periodic points, a finite inverse image of this Cantor set, the exceptional set \(E_b\) has the same dimension. It is therefore arclength-null, and its complement—the union of plateau preimages—has full arclength in \(\Gamma_b\).

## Verification

The standalone \`verify_three_returns.py\` uses exact rational arithmetic and verifies the three return identities for 147 rational endpoint/interior cases spanning seven parameters including \(b=2\) and \(b=4\). It also verifies the disjoint inverse images and their exact lengths in each case, and checks intermediate quadrant branches. The symbolic formulas, uniform interval inequalities, the finite graph covering relations and the separated-cylinder argument—not the finite tests—prove the theorem for the entire real parameter interval.

## Relationship to prior work

Cima, Gasull, Mañosa and Mañosas first constructed the invariant graph, identified its Markov covering graph for \(2\le b\le4\), and calculated topological entropy from the return circuit lengths \(3,4,7\). Their original Theorem C established only an **open dense** family of plateau preimages. Their follow-up theorem proved full arclength measure for certain other parameter regions (\(b<-2\) and two small intervals near entropy onsets), not for \([2,4]\). The present result supplies the explicit geometric inverse-return contractions and an exact Hausdorff-dimension computation, which are not determined by a topological-entropy computation alone, and settles full arclength measure in the stated remaining band. The underlying separated self-similar-set dimension theorem is classical; the graph geometry, parameter-uniform return contractions and application to the outstanding full-measure question are the contribution.

## Limitations

The theorem makes no full-area assertion for planar initial conditions outside the invariant graph, and it does not treat parameters outside \([2,4]\). It does not determine the distribution of physical attraction times, the precise planar basin geometry, or the dimension of exceptional sets for other parameter regimes. The novelty assessment cannot exclude an unindexed equivalent treatment of the same graph-directed repeller. The stated dimension applies to the exceptional set for all graph plateaus, not to an arbitrary subset selected by a different dynamical hole.

## References

1. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052 (first public version 2024-10-01), especially Section 5.7, Proposition 38 and Appendix Figures 60–61; *Qualitative Theory of Dynamical Systems* 24 (2025), article 70. https://arxiv.org/abs/2410.01052.
2. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Further results for a family of continuous piecewise linear planar maps*, arXiv:2503.02411 (first public version 2025-03-04), Theorem 3, Propositions 10–11. https://arxiv.org/abs/2503.02411.
3. J. E. Hutchinson, *Fractals and self-similarity*, Indiana University Mathematics Journal 30 (1981), 713–747, the separated self-similar dimension theorem.
