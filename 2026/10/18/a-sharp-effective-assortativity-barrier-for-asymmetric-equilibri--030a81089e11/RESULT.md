# A sharp effective-assortativity barrier for asymmetric equilibria in two-community hypergraph contagion

## Finding

Consider the equal-sized two-community, pair-and-triangle mean-field social-contagion model of Landry and Restrepo [1], with unit recovery, positive pairwise and triangle strengths \(b,c>0\), and assortativities \(e,f\in[0,1]\). Write the *effective within-community reinforcement strengths* as \(u=be\) and \(v=cf\).

For \(0\le u<1\), let \(t(u)\) be the unique number in \((1,3/2]\) satisfying
\[
 t(u)^2(3-2t(u))=u,
\]
and put \(V(u)=t(u)^3\). In particular, \(V(0)=27/8\), while \(V(u)\) decreases to \(1\) as \(u\) increases to \(1\).

**Sharp universal exclusion and attainability theorem.** Every equilibrium with both community densities strictly between zero and one has equal densities if either \(u\ge1\), or \(0\le u<1\) and \(v\le V(u)\). In the latter case, the inequality is inclusive at equality. If some cross-community infection is present, *every* equilibrium in the closed physical square has equal densities under these conditions. Conversely, for every \(0\le u<1\) and every \(v>V(u)\), there exist admissible parameters with these same effective strengths and a genuinely asymmetric interior equilibrium.

This is a sharp boundary for the **possibility**, over parameters sharing \((u,v)\), of asymmetric stationary states, **not** a stability threshold and **not** a sufficient condition for asymmetric equilibria at each fixed choice of \((b,c,e,f)\). In particular, existence of an asymmetric stationary state is not the same as stable opinion disparity.

An exact asymmetric witness is
\[
 (b,c,e,f)=\left(\frac{19}{54},\frac{154}{45},\frac{27}{95},1\right),
 \qquad (x_1,x_2)=\left(\frac14,\frac12\right).
\]
Here \(u=1/10\), \(v=154/45\), and both derivatives vanish exactly. This witness is a saddle, not a claimed stable polarized state.

## Assumptions and scope

The state \((x_1,x_2)\in[0,1]^2\) evolves according to Eqs. (15)–(16) of [1], with time rescaled to unit recovery. Writing \(j=3-i\), these equations are
\[
 \dot x_i=-x_i+(1-x_i)\left\{\frac b2[(1+e)x_i+(1-e)x_j]+\frac c4[(1+3f)x_i^2+2(1-f)x_ix_j+(1-f)x_j^2]\right\}.
\]
The theorem applies to **equal-sized communities**, nonnegative assortativity in the source's admissible range, and the deterministic mean-field approximation. It does not assert anything for unequal community sizes, finite-network stochastic simulations, or arbitrary negative assortativity.

An equilibrium is *interior* when \(0<x_i<1\) for both \(i\). It is *asymmetric* when \(x_1\ne x_2\). Cross-community infection is present when \(e<1\) or \(f<1\).

## Proof

**1. Shared-pressure reduction.** Put \(S=x_1+x_2\) and
\[
 L(S)=\frac{b(1-e)}2 S+\frac{c(1-f)}4 S^2.
\]
Direct expansion of the infection pressure in each equation gives exactly \(L(S)+u x_i+v x_i^2\). At an interior equilibrium, division by \(1-x_i\) yields
\[
 h_{u,v}(x_1)=h_{u,v}(x_2)=L(S),\qquad
 h_{u,v}(z)=\frac{z}{1-z}-uz-vz^2.
\]
Notice \(L(S)\ge0\), strictly positive whenever \(S>0\) and cross-community infection is present. No assumptions about linear stability have been used.

**2. Necessary exclusion for \(u<1\).** On \((0,1)\),
\[
 h_{u,v}'(z)=\frac1{(1-z)^2}-u-2vz,\quad
 h_{u,v}''(z)=\frac2{(1-z)^3}-2v.
\]
When \(0\le v\le1\), the first derivative is strictly positive for \(u<1\). When \(v>1\), it has a unique global minimum at \(z_*=1-v^{-1/3}\), with value
\[
 h_{u,v}'(z_*)=3v^{2/3}-2v-u.
\]
For \(v>1\), this minimum is nonnegative exactly when \(v\le V(u)\). Indeed \(t=v^{1/3}>1\), and \(t^2(3-2t)\) decreases continuously and strictly from \(1\) at \(t=1\) to \(0\) at \(t=3/2\). If the derivative has a single zero at the equality boundary, \(h_{u,v}\) is nonetheless strictly increasing: it is increasing on every nonempty interval. Thus \(h(x_1)=h(x_2)\) implies \(x_1=x_2\).

**3. Necessary exclusion for \(u\ge1\).** Define
\[
 Q_{u,v}(z)=\frac1{1-z}-u-vz,
 \qquad h_{u,v}(z)=zQ_{u,v}(z).
\]
Here \(Q_{u,v}(0)=1-u\le0\), \(Q_{u,v}''(z)=2/(1-z)^3>0\), and \(Q_{u,v}(z)\) tends to positive infinity as \(z\uparrow1\). Strict convexity implies that the portion of \((0,1)\) where \(Q_{u,v}\) is positive is a right-hand interval on which \(Q_{u,v}\) is strictly increasing. There \(h=zQ\) is strictly increasing; outside it \(h\le0\). Therefore **every positive level** of \(h\) is met at most once. Since an interior asymmetric equilibrium with cross-community infection has the common level \(L(S)>0\), such equilibria cannot occur. If cross-community infection vanishes (\(e=f=1\)), then \(L=0\); in that case \(Q\) has at most one positive zero, so again \(h(z)=0\) has at most one interior root. This completes the interior exclusion for all \(u\ge1\).

**4. Sharp attainability for \(u<1\), \(v>V(u)\).** Now \(h'(0)=1-u>0\) but its interior minimum is negative; as \(z\uparrow1\), \(h'(z)\) becomes positive without bound. Hence \(h\) has a strict positive local maximum and a later strict local minimum. Select a common level \(C>0\) strictly between the two extrema, and choose distinct \(x,y\in(0,1)\) with \(h(x)=h(y)=C\). For any such pair set
\[
 c=v,\quad f=1,\quad b=u+\frac{2C}{x+y},\quad e=\frac{u}{b}.
\]
Then \(b,c>0\), \(0\le e<1\), \(f=1\), \(be=u\), \(cf=v\), and \(L(x+y)=b(1-e)(x+y)/2=C\). The shared-pressure equations imply that \((x,y)\) is an interior asymmetric equilibrium of the original system. Thus the strict boundary cannot be strengthened when only \((u,v)\) are specified.

**5. Boundary states.** At \(x_i=1\), the vector-field component is \(-1\), so no equilibrium lies on a top or right edge. At \(x_i=0<x_j\), if either \(e<1\) or \(f<1\), its infection pressure is \(L(x_j)>0\); thus this cannot be an equilibrium. The remaining boundary equilibrium is the symmetric origin. The preceding interior exclusion therefore extends to the entire physical square when cross-community infection is present. At \(e=f=1\), asymmetric boundary equilibria may occur even when all interior equilibria are symmetric; the full-square assertion correctly excludes that disconnected case.

## Verification

For the exact witness, a rational-arithmetic calculation gives
\[
 h_{1/10,154/45}(1/4)=h_{1/10,154/45}(1/2)=\frac{17}{180}
 =\frac{19}{54}\left(1-\frac{27}{95}\right)\frac{(1/4+1/2)}2.
\]
Thus the two original vector-field components vanish. Moreover
\[
 h_{1/10,154/45}'(2/5)=-\frac3{50}<0,
\]
showing this point lies beyond the sharp monotonicity barrier without approximating a cubic root. The Jacobian of the original vector field at this witness has negative determinant \(-1747/64800\), so the witness is a saddle.

Run `python3 checks/verify_fold.py` with Python 3 and no third-party packages. It checks 324 exact rational identities between the original and reduced equations, the exact asymmetric equilibrium, the derivative sign, and additional monotone-parameter samples. These tests do **not** constitute a proof of the all-parameter theorem: the proof is the monotonicity/convexity argument above.

For the numerical regime in Fig. 3 of [1], \(b=0.2\), \(e=0.5\), giving \(u=0.1\). The universal bound is \(V(0.1)\approx3.22266\); with \(c=4\) this excludes asymmetric equilibria for \(f\lesssim0.805665\). That is a necessary threshold, not a claim that asymmetric stationary states appear immediately for this particular parameter slice.

## Relationship to prior work

Landry and Restrepo [1, Eqs. (15)–(16), Figs. 3–5, Appendix C] develop precisely the equal-sized-community model, exhibit numerical asymmetry and stability regimes, and state that they use interval root finding to determine stationary states on parameter grids. Their fixed-parameter figures do not state or imply the analytical universal \((u,v)\) exclusion boundary or its existential sharpness. The accompanying reproduction repository [2] contains numerical mean-field parameter scans, rather than this monotonicity theorem. The supplementary related 2026 collective-decision study [3] investigates a different competing-opinions model; its model and state variables are not those of the two-community SIS equations, so its bifurcation analyses do not directly imply the present barrier. This comparison is about the **actual statements and equations**, not merely matching terminology. General convexity and fold theory motivate the proof but, without specializing the shared-pressure reduction, do not themselves specify the exact threshold for Eqs. (15)–(16).

## Limitations

The condition is a *universal nonexistence barrier for asymmetric fixed points*, not a complete bifurcation diagram for each parameter quadruple. The constructive converse varies the pairwise rate and assortativity while holding their product fixed. The exact witness is dynamically unstable. The inequality gives no global convergence result, no bound on transient community differences, and no guarantee of stable disparity above the boundary. Population-noise effects and unequal-sized communities are outside the claim. A mathematically equivalent theorem could exist in other nonlinear or social-contagion literature not located in the cited comparison; independent audit is not claimed.

## References

[1] N. W. Landry and J. G. Restrepo, *Opinion disparity in hypergraphs with community structure*, arXiv:2302.13967 (first posted 2023-02-27); *Physical Review E* **108**, 034311 (2023), doi:10.1103/PhysRevE.108.034311. Full preprint: https://arxiv.org/pdf/2302.13967.

[2] N. W. Landry, *Opinion disparity in hypergraphs with community structure* accompanying reproduction code: https://github.com/nwlandry/opinion-disparity-in-hypergraphs (README and mean-field numerical scripts).

[3] *Symmetry breaking in collective decision-making through higher-order interactions*, *npj Complexity* (2026). The comparison concerns the freely accessible article's different collective-decision dynamics, not a claimed exact match to [1].
