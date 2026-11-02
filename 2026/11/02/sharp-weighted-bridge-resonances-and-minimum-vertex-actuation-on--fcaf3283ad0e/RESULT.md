# Sharp weighted-bridge resonances and minimum vertex actuation on two-hub trees

## Finding

Let \(p,q\ge2\) and \(L\ge1\) be integers and let \(t>0\). Form a tree with a spine \(v_0,v_1,\ldots,v_L\), with every spine edge of conductance \(t\). Attach \(p\) new leaves \(a_1,\ldots,a_p\) to \(v_0\) and \(q\) new leaves \(b_1,\ldots,b_q\) to \(v_L\); every leaf edge has conductance one. Let \(\mathcal L\) be the ordinary weighted combinatorial Laplacian on its \(N=p+q+L+1\) vertices. An actuator set \(S\) means an independent scalar control at every vertex in \(S\):

\[\dot z=-\mathcal L z+B_Su,\qquad B_S=[e_s]_{s\in S}.\]

Define the finite exceptional set

\[\mathcal T_L=\left\{t_j=\frac{1}{2(1-\cos(j\pi/L))}:j=1,\ldots,L-1\right\}\]

for \(L\ge2\), and \(\mathcal T_1=\varnothing\). These numbers are all positive and pairwise distinct. The exact minimum number of vertex inputs that makes the entire state controllable is

\[\boxed{m(p,q,L,t)=p+q-2+\mathbf 1_{\{t\in\mathcal T_L\}}.}\]

All minimum actuator sets can also be described. If \(t\notin\mathcal T_L\), they are exactly the sets consisting of \(p-1\) left leaves and \(q-1\) right leaves. If \(t=t_j\), they are exactly the following sets, with arbitrary choices of omitted leaves:

1. All \(p\) left leaves and \(q-1\) right leaves, or \(p-1\) left leaves and all \(q\) right leaves.
2. Exactly \(p-1\) left leaves, \(q-1\) right leaves, and one internal spine vertex \(v_i\), where \(1\le i<L\) and \(L\nmid ji\).

In particular neither hub can replace the extra actuator at resonance. The number of eligible internal vertices is \(L-\gcd(j,L)\), as the nonzero entries of \(\sin(j\pi i/L)\) on \(1\le i<L\) occur exactly when \(L\nmid ji\).

For rational \(t>0\), the only exceptional choices are

\[\boxed{t=1,\ 1/3\quad\text{if }3\mid L;\qquad t=1/2\quad\text{if }2\mid L.}\]

The support tree has zero-forcing number \(p+q-2\) for \(L=1\) and \(p+q-1\) for \(L\ge2\). Therefore its fixed-weight Laplacian, for every \(L\ge2\) and every nonexceptional \(t>0\), can be controlled with exactly one fewer vertex input than the number needed for zero forcing.

## Assumptions and scope

The graph is a finite undirected tree, all spine conductances are the same positive real number \(t\), and all pendant conductances are exactly one. Both bundles contain at least two leaves. The system matrix is \(-\mathcal L\), not a normalized Laplacian or a generic matrix with the same sparsity pattern. Inputs are separate unit coordinate columns, not arbitrary linear combinations of state coordinates. Complete Kalman controllability is intended, including the consensus mode; no claim is made about energetic conditioning.

## Proof

**Leaf-twin lower bound.** For any two distinct leaves belonging to the same bundle, the vector which is \(+1\) at one, \(-1\) at the other, and zero elsewhere is a \(\mathcal L\)-eigenvector of eigenvalue \(1\). The left leaf-difference space has dimension \(p-1\), and the right one has dimension \(q-1\). By the Popov–Belevitch–Hautus (PBH) criterion, every controllable actuator set must include at least \(p-1\) left leaves and \(q-1\) right leaves: if two leaves of one bundle are unactuated, their difference vector is an unobserved eigenvector. Thus at least \(p+q-2\) actuators are required, regardless of other choices.

**Eigenvector reduction.** Let \(x\) be a \(\mathcal L\)-eigenvector of eigenvalue \(\lambda\), vanishing at \(p-1\) chosen left leaves and \(q-1\) chosen right leaves. Write \(x_i=x(v_i)\). The leaf equations are

\[(1-\lambda)x(a_r)=x_0,\qquad (1-\lambda)x(b_s)=x_L.\]

If \(\lambda\ne1\), the selected zero leaf values imply \(x_0=x_L=0\) and every leaf value zero. The equation at \(v_0\) then implies \(t x_1=0\). For \(L\ge2\) the ordinary spine recurrence forces all successive entries zero; for \(L=1\), the hub and leaf entries are already zero. Hence no nonzero eigenvector with \(\lambda\ne1\) is invisible to these inputs.

If \(\lambda=1\), the leaf equations require \(x_0=x_L=0\). For \(L\ge2\) the internal spine equations are

\[t(2x_i-x_{i-1}-x_{i+1})=x_i\quad (1\le i<L),\qquad x_0=x_L=0.\]

This is the Dirichlet Laplacian on a path with \(L-1\) interior vertices. Its eigenvalues are \(2t[1-\cos(j\pi/L)]\), with simple eigenvectors

\[x_i=c\sin(j\pi i/L),\qquad j=1,\ldots,L-1.\]

Consequently a nonzero internal spine mode at eigenvalue one occurs exactly when \(t=t_j\). If no such \(t_j\) exists, the spine is zero. The two hub equations then give \(\sum_r x(a_r)=\sum_s x(b_s)=0\). As all but one leaf of each bundle have zero value, the remaining two values must also vanish. This proves sufficiency of the \(p+q-2\) leaf inputs off resonance.

At a resonance \(t=t_j\), there is exactly one internal Dirichlet mode, up to scaling, with coordinates \(c\sin(j\pi i/L)\). The two hub equations give

\[\sum_r x(a_r)=-t x_1,\qquad\sum_s x(b_s)=-t x_{L-1}.\]

After forcing all but one leaf of each bundle to zero, these two identities uniquely determine the remaining leaf values for any prescribed nonzero mode amplitude \(c\). This constructs a nonzero eigenvector invisible to exactly \(p-1\) left and \(q-1\) right actuators. No set of \(p+q-2\) actuators can therefore control the resonant system, by the leaf-twin lower bound and the necessity of selecting those leaves.

**Complete minimum-set classification.** With \(p+q-1\) inputs, every controllable set must still have at least \(p-1\) and \(q-1\) selected leaves. If the additional input is the last leaf of either bundle, the corresponding hub identity forces \(x_1=0\) or \(x_{L-1}=0\); the first and last entries of the resonant sine mode are nonzero, so its amplitude vanishes. If instead the extra input is at \(v_i\) with \(1\le i<L\), it suppresses the remaining mode exactly if \(\sin(j\pi i/L)\ne0\), equivalently \(L\nmid ji\). At either hub the resonant eigenvector is identically zero and that input adds no information. No other distribution of \(p+q-1\) inputs can meet the necessary leaf counts. PBH therefore proves both sufficiency and exhaustion. The number of admissible internal positions is \(L-\gcd(L,j)\), because the forbidden internal positions are precisely the \(\gcd(L,j)-1\) positive multiples of \(L/\gcd(L,j)\) below \(L\).

**Rational resonance classification.** Suppose \(t\in\mathbb Q_{>0}\) and \(t=t_j\). Let \(\zeta=\exp(i\pi j/L)\), a root of unity. The number \(\zeta+\zeta^{-1}=2-1/t\) is both rational and an algebraic integer, hence an integer. As \(0<j<L\), it lies strictly between \(-2\) and \(2\); it is therefore \(-1\), \(0\) or \(1\). These cases give respectively \(t=1/3\), \(1/2\) and \(1\). They correspond to \(j/L=2/3\), \(1/2\) and \(1/3\), so precisely the stated divisibility conditions occur. Conversely each listed value gives a Dirichlet eigenvalue one.

**Zero-forcing comparison.** The two leaf bundles each require all but at most one leaf initially black: if two leaves of a bundle are white, neither can ever be the unique white neighbor of the hub. Thus \(Z\ge p+q-2\). When \(L=1\), taking all but one leaf on each side forces both hubs, then the two remaining leaves; hence equality. When \(L\ge2\), with only \(p+q-2\) black vertices one necessarily starts with exactly those leaves. The two hubs can be forced, but each has both its last white leaf and a white internal neighbor, so no next force is possible. Thus \(Z\ge p+q-1\). Selecting all left leaves and all but one right leaf lets the left hub force the entire spine, then the right hub forces its last leaf, so \(Z=p+q-1\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic and the full Kalman controllability matrix; it has no external dependencies. Run `python3 verify.py` in the directory containing this document. Its executed suite passed 1,003 assertions covering bundles of two or three leaves, path lengths one through seven, seven rational weights, exceptional and generic cases, admissible and forbidden extra actuators, and exhaustive minimum-cardinality sensor-set checks for eight small instances. It independently tests the Dirichlet determinant recurrence and its rational resonance conditions. The symbolic proof above, not those finite tests, establishes the theorem for all indicated integers and positive real weights.

As an explicit case, take \(p=q=3\), \(L=6\). The minimum is five at \(t\in\{1/3,1/2,1\}\) and four at any other positive rational weight (indeed at every nonresonant real weight). At \(t=1/2\), the resonant index is \(j=3\), so internal actuators at \(v_1,v_3,v_5\) work and those at \(v_2,v_4\) do not, when combined with two leaf actuators from each bundle.

## Relationship to prior work

The fixed-weight problem is different from strong structural controllability for an entire qualitative matrix class. Monshizadeh, Zhang and Camlibel (2014, Theorem IV.4) characterize robust controllability across the full qualitative class by zero forcing, and explicitly note that a particular graph Laplacian can be controllable from a non-zero-forcing set. The present theorem identifies exactly when that strict inequality occurs on a natural weighted tree family, and gives all minimum actuator positions.

Dai (2023, Theorem 3) proves that selecting all but one pendant vertex controls every undirected tree. This supplies a general upper bound matching the resonant cardinality, but not the lower off-resonance cardinality, the isolated conductance resonances, or their admissible vertex sets. Parlangeli (2025) gives graph-theoretic selection rules for starlike trees with only one major vertex, whereas the present trees have two major vertices. Gupta, Lather and Balaji (2025) characterize extremal multiplicity for unweighted tree Laplacians; their unweighted eigenvalue-one distance-modulo-three criterion *already implies the multiplicity jump at \(t=1\) when \(3\mid L\)*. That special unweighted multiplicity criterion is not presented as new here. The additional statements here concern all positive weighted bridge conductances and all minimum input placements, including the complete rational resonance classification.

## Limitations

The result requires equal weights along the spine and unit pendant edges, and separate vertex-coordinate inputs. It concerns exact Kalman controllability, not a guaranteed numerical conditioning margin: near a resonance the smallest nonzero controllability singular value may be very small. Allowing unequal spine weights, uneven pendant weights, directed arcs, input amplitude limits or control energy constraints requires separate analysis. Literature discovery does not guarantee absence of unindexed equivalent statements; no independent mathematical audit has been performed.

## References

1. N. Monshizadeh, S. Zhang and K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868, first public 2014-03-19. https://arxiv.org/abs/1403.4868
2. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications (2023), DOI 10.1049/cth2.12385. https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/cth2.12385
3. V. Gupta, G. Lather and R. Balaji, *Trees with extremal Laplacian eigenvalue multiplicity*, arXiv:2507.15472 (2025). https://arxiv.org/abs/2507.15472
4. G. Parlangeli, *Laplacian Controllability and Observability of Multi-Agent Systems: Recent Advances in Tree Graphs*, preprint posted 2025-03-19; journal version Algorithms 18(5), 239 (2025). https://www.preprints.org/manuscript/202503.1438
