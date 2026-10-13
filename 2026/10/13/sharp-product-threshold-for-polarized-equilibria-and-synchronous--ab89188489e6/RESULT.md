# Sharp product threshold for polarized equilibria and synchronous reversals in two contrarian communities

## Finding

**Theorem.** Consider two well-mixed communities, A and B, each consisting of a continuum-scale population choosing between binary opinions 0 and 1. At each synchronous round, an agent in community A draws three independent opinions from community B, determines their local majority, and adopts its opposite with probability \(u_A\) if the sample is unanimous and \(v_A\) if the sample is split two to one; otherwise the agent adopts the majority. Agents in B obey the corresponding rule with \(u_B,v_B\), drawing only from A. Let \(p_A,p_B\in[0,1]\) denote the fractions choosing opinion 1. This is a deterministic mean-field update, not a statement about finite-population sample trajectories.

Assume, for each \(i\in\{A,B\}\),
\[
0\le v_i\le u_i\le1,\qquad 3v_i>1+u_i.
\]
Write
\[
a_i=\frac32(u_i+v_i-1)>0,\quad b_i=\frac{3v_i-1-u_i}{2}>0,
\quad \Theta=a_Aa_B=\frac94(u_A+v_A-1)(u_B+v_B-1).
\]
Then **\(\Theta=1\) is the exact global transition surface**:

1. If \(\Theta\le1\), every trajectory converges to the balanced state \((p_A,p_B)=(1/2,1/2)\). For \(\Theta<1\), convergence is exponential. At \(\Theta=1\), nonzero centered coordinates decay at the explicit universal power \(n^{-1/2}\) described below.
2. If \(\Theta>1\), there is a unique pair \(r,s\in(0,1]\) satisfying \(r=a_As-b_As^3\) and \(s=a_Br-b_Br^3\). In centered coordinates \(x=2p_A-1\) and \(y=2p_B-1\), the dynamics has **exactly two attracting polarized fixed points** \((r,-s),(-r,s)\) and **one attracting synchronous opinion-reversal two-cycle** \((r,s)\longleftrightarrow(-r,-s)\). Every initial condition with \(xy<0\) approaches its corresponding polarized fixed point; every initial condition with \(xy>0\) approaches the indicated two-cycle. Initial conditions on an axis converge to one of two non-attracting axial two-cycles, while the origin is a repelling fixed point. There are no other recurrent periodic orbits.

At \(\Theta=1\) put \(K_A=a_Ab_B+b_Aa_B^3\) and \(K_B=a_Bb_A+b_Ba_A^3\). Both are strictly positive. For \(x_0\ne0\), respectively \(y_0\ne0\), the exact critical asymptotics are
\[
|x_{2n}|\sim(2K_A n)^{-1/2},\qquad |y_{2n}|\sim(2K_B n)^{-1/2}.
\]
Thus the critical surface is included in global balancing, but not exponential balancing for generic initial states.

## Assumptions and scope

Sampling is with replacement in each community, both communities update simultaneously, and the fractions are deterministic probabilities in the infinite well-mixed limit. The response parameters are fixed by receiving community (A or B) and by the sample composition, and do not depend on the majority opinion's identity. The strict inequality \(3v_i>1+u_i\) selects the genuine, concave high-contrarian response regime; the weak inequality \(u_i\ge v_i\) ensures the response has no fold on the physical interval. We do not claim a classification outside this explicitly specified four-parameter region.

## Proof

**1. Exact mean-field operator and normalization.** A receiver with parameters \((u,v)\) sees a majority of opinion 1 in a three-person sample with probability \(p^3+3p^2(1-p)\), and the opposite majority with probability \(3p(1-p)^2+(1-p)^3\). Separating unanimous and split samples gives
\[
f_{u,v}(p)=(1-u)p^3+3(1-v)p^2(1-p)+3vp(1-p)^2+u(1-p)^3.
\]
Direct polynomial expansion yields, for \(z=2p-1\),
\[
2f_{u,v}\!\left(\frac{1+z}{2}\right)-1
=-az+bz^3=-P(z),\quad P(z)=az-bz^3.
\]
Hence the exact two-community map is \(T(x,y)=(-P_A(y),-P_B(x))\) on \([-1,1]^2\). Our assumptions imply \(a_i>0,b_i>0\), \(a_i-3b_i=3(u_i-v_i)\ge0\), and \(P_i(1)=2u_i-1\in(0,1]\). Thus each \(P_i\) is odd, strictly increasing on \((-1,1)\), maps \([-1,1]\) into itself, and is strictly concave on \((0,1)\).

**2. Two-step decoupling.** Write \(G_A=P_A\circ P_B\) and \(G_B=P_B\circ P_A\). Oddness implies \(T^2(x,y)=(G_A(x),G_B(y))\). Each \(G_i\) is odd, strictly increasing, and strictly concave on \((0,1)\), maps \([-1,1]\) into itself, and has derivative \(G_i'(0)=a_Aa_B=\Theta\). Strict concavity and \(G_i(0)=0\) show that \(G_i(z)/z\) is strictly decreasing on \((0,1]\). Because \(G_i(1)\le1\), this gives precisely one of two possibilities: if \(\Theta\le1\), zero is the sole fixed point and \(0<G_i(z)<z\) for \(0<z\le1\); if \(\Theta>1\), there is exactly one positive fixed point (possibly at \(z=1\)), it attracts all positive iterates, and its negative attracts all negative iterates. In the strict latter case, the attracting fixed points are simple, as strict concavity implies \(0\le G_i'(r_i)<1\). The positive solutions are linked by \(s=P_B(r)\) and \(r=P_A(s)\), so the pair is unique.

**3. Full coupled limit sets and exact basins.** The signs of the two nonzero centered coordinates are preserved by \(T^2\). In the \(\Theta>1\) regime, \(T^2\) therefore sends every point off the axes to one of four corners \((\pm r,\pm s)\). One application of \(T\) fixes each opposite-sign corner and exchanges the two same-sign corners. On an axis, \(T^2\) converges to one of \((\pm r,0)\), \((0,\pm s)\), which \(T\) pairs into two axial two-cycles. The origin is fixed. These nine points exhaust the fixed points of \(T^2\), hence all periodic states of \(T\): each increasing coordinate map \(G_i\) admits no nontrivial periodic orbit. Attracting corners have both two-step multipliers strictly less than one. Each axial cycle has one unstable two-step multiplier \(\Theta>1\); the origin has two unstable two-step multipliers \(\Theta>1\). This establishes the asserted exhaustive attraction and non-attraction classification.

**4. The critical surface and convergence rates.** If \(\Theta<1\), concavity gives \(|G_i(z)|\le\Theta|z|\), so the two-step iteration decays geometrically. If \(\Theta=1\), direct composition gives
\[
G_A(z)=z-K_Az^3+O(z^5),\qquad
G_B(z)=z-K_Bz^3+O(z^5),
\]
where \(K_A=a_Ab_B+b_Aa_B^3>0\) and \(K_B=a_Bb_A+b_Ba_A^3>0\). The preceding global argument guarantees decay toward zero for every coordinate. For nonzero initial values, applying \(z_{n+1}=z_n-Kz_n^3+O(z_n^5)\) to the positive magnitudes yields \(z_{n+1}^{-2}-z_n^{-2}=2K+o(1)\); summation and Cesàro averaging give \(z_n\sim(2Kn)^{-1/2}\). The theorem follows.

## Verification

A standalone Python 3 script, `verify.py`, checks the majority-sampling polynomial reduction with exact rational arithmetic, the coefficient identity \(a_i-3b_i=3(u_i-v_i)\), the cubic critical coefficient, several exact subcritical/critical/supercritical parameter witnesses, and representative finite-step basin behavior. Run `python3 verify.py` in a directory containing that file. The finite checks corroborate exact algebra and illustrative orbits; the general quantifiers follow from the proof above.

An exact heterogeneous supercritical witness is \((u_A,v_A)=(19/20,9/10)\) and \((u_B,v_B)=(9/10,9/10)\). Here \(a_A=51/40\), \(a_B=6/5\), and \(\Theta=153/100>1\): the two communities have different contrarian profiles and exhibit all three attracting outcomes depending on their initial majority signs. [Numerical verification code uses these exact parameters.] A critical witness is \((u_A,v_A)=(5/6,5/6)\) and \((u_B,v_B)=(5/6,5/6)\), yielding \(a_Aa_B=1\).

## Relationship to prior work

Galam, *Ratio-Dependent Contrarian Activation in Opinion Dynamics* (2026), derives the one-population three-person majority/contrarian update and its two-dimensional **parameter** landscape, including scalar alternating regimes; it does not construct two interacting populations with potentially distinct response parameters, derive the four-parameter product threshold, or classify coexisting polarized fixed points and synchronous reversing two-cycles. In particular, Galam's uniform single-population flip value \(c=5/6\) reappears as the diagonal intersection of the present threshold when both communities share \(u_i=v_i=c\), which is a consistency check, not the main new claim.

Nettasinghe, Percus, and Lerman (2025) study affective polarization across two parties, but use asynchronous individual binary threshold updates with in-/out-group weights and a limiting continuous-time description, not coupled synchronous Galam triad polynomials. Lambiotte, Ausloos, and Hołyst (2007) analyze two partially overlapping networks under an ordinary (noncontrarian) majority rule with local asynchronous triplet updates and an interconnectivity threshold. Their equations are not a two-population cross-only synchronous complementary-majority map and do not imply the alternating-cycle classification or its contrarian product boundary. The classical Galam (2004) uniform-contrarian construction likewise concerns a single population. The composition and concavity observations in the proof are classical dynamical arguments; originality is claimed only for their specific social-dynamics classification and its sharp heterogeneous product boundary.

## Limitations

This theorem describes deterministic synchronous mean-field fractions with cross-community sampling. It is not a theorem for the finite-population random partition process, network correlations, within-community sampling, delayed or asynchronous updates, or parameter values violating the stated concavity and monotonicity constraints. Attracting fixed states represent opposing *population-level majority fractions*, not guaranteed frozen individual opinions. The originality comparison cannot exhaust unindexed conference proceedings, works describing equivalent compositions with alternative terminology, or unpublished results; independent audit has not been performed.

## References

1. S. Galam, *Ratio-Dependent Contrarian Activation in Opinion Dynamics*, Entropy **28** (2026), 443, doi:10.3390/e28040443; lawful open preprint arXiv:2604.27226v1. First public journal date: 2026-04-14.
2. B. Nettasinghe, A. G. Percus, and K. Lerman, *How out-group animosity can shape partisan divisions: A model of affective polarization*, PNAS Nexus **4** (2025), pgaf082, doi:10.1093/pnasnexus/pgaf082.
3. R. Lambiotte, M. Ausloos, and J. A. Hołyst, *Majority model on a network with communities*, Physical Review E **75** (2007), 030101, doi:10.1103/PhysRevE.75.030101; arXiv:physics/0612146v3.
4. S. Galam, *Contrarian deterministic effects on opinion dynamics: the hung elections scenario*, Physica A **333** (2004), 453–460, doi:10.1016/j.physa.2003.10.041.
