# A median–midpoint law for welfare instability in heterogeneous triangle anti-coordination

## Finding
Consider the triangle \(K_3\) with binary actions \(a,b\). Player \(i\) has a type \(\gamma_i\in(0,1)\), earning \(\gamma_i\) per neighbor of the opposite action when playing \(a\), and \(1-\gamma_i\) per opposite-action neighbor when playing \(b\). Same-action edges pay zero to both endpoints. Write the three distinct types in increasing order \(\ell<m<h\), and exclude the two equality hypersurfaces \(m=\tfrac12\) and \(2m=\ell+h\).

There is exactly one welfare-maximizing action profile. If \(2m>\ell+h\), only the player of type \(\ell\) plays \(b\); if \(2m<\ell+h\), only the player of type \(h\) plays \(a\). The unique social optimum fails to be a Nash equilibrium **exactly when**
\[
\left(m-\tfrac12\right)\left(m-\tfrac{\ell+h}{2}\right)<0.
\]
If the three types are sampled independently and uniformly from \((0,1)\), the probability of this failure is **exactly \(\tfrac14\)**; in the complementary \(\tfrac34\) of instances, the unique welfare optimum is a strict Nash equilibrium (both statements almost surely).

## Assumptions and scope
The network is a fixed, unweighted, undirected triangle with three labeled players. All payoffs are additive over the two incident edges, types lie strictly between zero and one, and actions are chosen simultaneously. Social welfare is the sum of the three individual payoffs. Nash equilibrium means no individual strictly improves by changing only their own action. The deterministic classification holds for every strictly ordered triple avoiding \(m=\tfrac12\) and \(2m=\ell+h\); the exceptional equality sets have probability zero under independent continuous types. The probability calculation additionally assumes independent Uniform\((0,1)\) types. No distributional assumption is needed for the deterministic classification.

## Proof
Set \(S=\gamma_1+\gamma_2+\gamma_3\). If all three players make the same choice, social welfare is zero. If player \(i\) is the sole \(b\) player, that player earns \(2(1-\gamma_i)\), while the other two jointly earn \(S-\gamma_i\). Thus welfare is \(W_{b,i}=2+S-3\gamma_i\). If player \(i\) is the sole \(a\) player, welfare is \(W_{a,i}=2+3\gamma_i-S\). It follows that the best sole-\(b\) profile places \(b\) at \(\ell\), and the best sole-\(a\) profile places \(a\) at \(h\). Both have positive welfare, and their difference is
\[
(2+m+h-2\ell)-(2+2h-\ell-m)=2m-\ell-h.
\]
Since the types are strictly ordered and the difference is nonzero, the stated global welfare optimizer is unique.

In the \(b\)-minority optimum, the sole \(b\) player cannot benefit by flipping, as doing so produces a zero-payoff unanimous state. Either of the other two players, with type \(\gamma\), earns \(\gamma\) in the current configuration and would earn \(1-\gamma\) after flipping. Therefore that optimum is Nash if and only if \(m\ge\tfrac12\), and under the excluded ties is strict Nash if and only if \(m>\tfrac12\). In the \(a\)-minority optimum, the analogous condition is \(m\le\tfrac12\), with strictness when \(m<\tfrac12\). Combining this test with the welfare comparison proves the stated product-sign criterion.

For independent uniform types, the ordered triple \((\ell,m,h)\) has density six on \(0<\ell<m<h<1\). On the lower half \(m<\tfrac12\), failure occurs exactly when \(h<2m-\ell\); here \(2m-\ell<1\) automatically. Its ordered-simplex probability is
\[
6\int_0^{1/2}\!\int_0^m\!\int_m^{2m-\ell}dh\,d\ell\,dm
=6\int_0^{1/2}\frac{m^2}{2}\,dm=\frac18.
\]
Reflecting every type by \(\gamma\mapsto1-\gamma\) maps the other failure region bijectively to this one and preserves uniform measure. The failure probability is twice \(\tfrac18\), namely \(\tfrac14\). All remaining nondegenerate instances have a strict-Nash welfare optimum.

## Verification
The included `verify.py` enumerates all eight profiles and all one-agent deviations using exact rational arithmetic, comparing their unique optimum and Nash status to the formulas over a finite grid of distinct, nondegenerate types. It also checks an exact-rational witness and the integral's rational arithmetic. Execute `python3 verify.py` using only the Python standard library. Finite checks corroborate, rather than replace, the all-real-types proof above.

For a non-Nash optimum, take \((\gamma_1,\gamma_2,\gamma_3)=(\tfrac1{10},\tfrac25,\tfrac35)\). The unique optimal profile is \((b,a,a)\), with welfare \(\tfrac{14}{5}\). The type-\(\tfrac25\) player would increase payoff from \(\tfrac25\) to \(\tfrac35\) by switching to \(b\).

## Relationship to prior work
Deligkas, Eiben, Gutin, Neary and Yeo (2023) investigate welfare, Nash and potential objectives in binary-action polymatrix games, proving general computational-complexity classifications for anti-coordination and pure coordination. The present theorem specializes the anti-coordination side to a common natural vertex-type parameterization on the smallest nonbipartite network and establishes a *complete explicit preference-region condition* and *exact uniform-preference incidence*. These specific statements are not implied merely by hardness of computing general optima or by the existence of stable configurations. Their earlier May 2023 preprint is used as the earliest public source, rather than the November revision under a second identifier.

## Limitations
This theorem is for the specific per-vertex reward family on the unweighted triangle, not arbitrary edge-specific polymatrix payoffs or graphs of greater size. The strict classification excludes equal types, a median equal to \(\tfrac12\), and equality of the two candidate welfare values. The exact \(\tfrac14\) incidence uses independent uniform types and does not claim to hold for other distributions. The literature comparison cannot exclude all unindexed earlier equivalent results. No independent mathematical audit has been performed.

## References
1. A. Deligkas, E. Eiben, G. Gutin, P. R. Neary, A. Yeo, *Complexity of Efficient Outcomes in Binary-Action Polymatrix Games with Implications for Coordination Problems*, first public version 11 May 2023, arXiv:2305.07124, https://arxiv.org/abs/2305.07124.
2. A. Deligkas, E. Eiben, G. Gutin, P. R. Neary, A. Yeo, *Some coordination problems are harder than others*, first public version 6 November 2023, arXiv:2311.03195, https://arxiv.org/abs/2311.03195. This is a subsequent same-author treatment; the source date for this finding is the earlier 11 May 2023 posting.
3. A. Deligkas et al., *Complexity of Efficient Outcomes in Binary-Action Polymatrix Games and Implications for Coordination Problems*, IJCAI 2023, https://doi.org/10.24963/ijcai.2023/294.
