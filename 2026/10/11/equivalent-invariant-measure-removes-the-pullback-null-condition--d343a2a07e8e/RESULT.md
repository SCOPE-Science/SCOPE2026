# Equivalent invariant measure removes the pullback-null condition for decreasing Lorenz entropy staircases
## Finding
Let \(f\in\mathrm{{EDLM}}\) be a topologically expansive decreasing Lorenz map on \([0,1]\) with critical point \(c\). Assume that \(f\) preserves an ergodic probability measure \(\mu\) equivalent to Lebesgue measure. For every fixed \(a\) with \(0<a<c\), the pullback-null condition
\[
\operatorname{{Leb}}\!\left(\Phi_f^{{-1}}(E_{{-2}}(m))\right)=0
\]
from Proposition 5.2 of Ding--Steiner--Sun follows automatically. Therefore their Corollary 3 applies: the function
\[
b\longmapsto h_{{\mathrm{{top}}}}(S_f(a,b)),\qquad c\le b<1,
\]
is a devil's staircase in their sense, including the possible constant case.

## Assumptions and scope
The map \(f\) is in the class \(\mathrm{{EDLM}}\) defined by Ding--Steiner--Sun: it has two strictly decreasing branches, an upward discontinuity at \(c\), the endpoint normalization used there, and dense precritical set. The invariant probability \(\mu\) is assumed ergodic and equivalent to Lebesgue measure, meaning that \(\mu\) and Lebesgue measure have exactly the same null sets. The fixed left endpoint is restricted to \(0<a<c\). No assertion is made that every map in \(\mathrm{{EDLM}}\) possesses such a measure.

## Proof
For \(N\ge1\), define
\[
d_N=c+\frac{{1-c}}{{N+1}},\qquad H_N=(a,d_N).
\]
Every \(H_N\) is a nonempty open interval, hence has positive Lebesgue measure and therefore positive \(\mu\)-measure. By the ergodic theorem applied to the indicator of \(H_N\), \(\mu\)-almost every point visits \(H_N\) infinitely often. Thus the survivor set
\[
S_f(a,d_N)=\{{x:f^n(x)\notin(a,d_N)\text{{ for every }}n\ge0\}}
\]
has \(\mu\)-measure zero. Equivalence of \(\mu\) and Lebesgue measure then gives
\[
\operatorname{{Leb}}(S_f(a,d_N))=0
\]
for every \(N\ge1\).

It remains to connect these fixed-hole null sets to the parameter pullback. Write
\[
\Phi_f(b)=\pi_{{-2}}(\tau_f(b+)),\qquad m=\pi_{{-2}}(\tau_f(a-)).
\]
Take \(b\in\Phi_f^{{-1}}(E_{{-2}}(m))\) with \(b>c\), and set \(\epsilon=\Phi_f(b)\) and \(\mathbf b=\tau_f(b+)\). The self-survival characterization in Proposition 5.2, applied to the negative doubling map, gives \(\epsilon\in S_{{-2}}(m,\epsilon)\). Since \(a<c<b\), the corresponding address orbit avoids the critical point \(1/2\), so its itinerary is unique and equals \(\mathbf b\). Proposition 5.1 then places \(\mathbf b\) in the symbolic survivor space and realizes it by a point \(x\in S_f(a,b)\). Strict order preservation of one-sided itineraries at distinct points forces \(x=b\). Hence \(b\in S_f(a,b)\).

Choose \(N\) with \(d_N<b\). Since \((a,d_N)\subset(a,b)\), survival of \(b\) for the larger hole implies \(b\in S_f(a,d_N)\). Therefore
\[
\Phi_f^{{-1}}(E_{{-2}}(m))
\subseteq \{{c\}\cup\bigcup_{{N\ge1}}S_f(a,d_N).
\]
The right-hand side is a countable union of Lebesgue-null sets, so condition \((P)\) holds. Corollary 3 of Ding--Steiner--Sun then yields the stated devil's-staircase conclusion.

## Verification
The proof uses only three ingredients: the ergodic theorem for the equivalent invariant probability, the source's self-survival characterization and symbolic realization in Propositions 5.1--5.2, and countable subadditivity. The direction of absolute continuity was checked explicitly: equivalence is needed because \(\mu(S)=0\) must imply \(\operatorname{{Leb}}(S)=0\). Mere absolute continuity \(\mu\ll\operatorname{{Leb}}\) would not suffice for that step.

## Relationship to prior work
Ding--Steiner--Sun prove the entropy staircase for general \(\mathrm{{EDLM}}\) only under the pullback-null condition \((P)\), and verify \((P)\) directly for a two-slope piecewise-linear family. Their argument also contains the parameter-to-fixed-survivor inclusion used above. Sun--Li--Ding previously proved an analogous ergodic absolutely continuous invariant-measure criterion for increasing expansive Lorenz maps; that theorem concerns increasing branches and does not imply the decreasing result. The present finding identifies a standard measure-theoretic hypothesis under which the new decreasing-map pullback condition is automatic.

## Limitations
The result is conditional on the existence of an ergodic invariant probability equivalent to Lebesgue measure. It does not prove such a measure exists for arbitrary \(\mathrm{{EDLM}}\), does not replace equivalence by one-sided absolute continuity, and does not address Hausdorff-dimension transfer for general decreasing Lorenz maps. The proof is stated for \(0<a<c\); endpoint variants may require separate bookkeeping for the completed critical orbit.

## References
1. Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1 (2026), especially Proposition 5.1, Proposition 5.2, Corollary 3, and Example 5.1.
2. Y. Sun, B. Li, Y. Ding, *Topological expansive Lorenz maps with a hole at critical point*, arXiv:2311.02465v1; Journal of Statistical Physics 191, Article 50 (2024).
3. P. Glendinning, C. Hege, *The boundary of chaos for piecewise smooth maps and the boundary of positive Hausdorff dimension for survivor sets of open maps*, arXiv:2508.21429v1; Nonlinearity 39, 075022 (2026).
