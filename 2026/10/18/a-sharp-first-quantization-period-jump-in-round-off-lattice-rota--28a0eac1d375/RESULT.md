# A sharp first-quantization period jump in round-off lattice rotations

## Finding

Consider the invertible round-off rotation on the integer lattice
\[
 F_\lambda(x,y)=(\lfloor\lambda x\rfloor-y,x),\qquad (x,y)\in\mathbb Z^2,\quad 0<\lambda<2.
\]
For each integer \(r\geq 0\), define
\[
 h(x,y)=|x|+|y|-\mathbf 1_{\{x<0,\ y<0\}},\qquad C_r=\{(x,y)\in\mathbb Z^2:h(x,y)=r\}.
\]
**Protected shells.** For every integer \(r\geq1\), throughout the sharp parameter interval \(0<\lambda<1/r\), the set \(C_r\) is an invariant single periodic orbit of exact length \(4r+1\). Moreover \(C_0=\{(0,0)\}\) is fixed for all parameters. Consequently, for every positive integer \(R\) with \(\lambda<1/R\), the complete set \(\{h\leq R\}\) is partitioned into exactly \(R+1\) periodic orbits and contains precisely \((R+1)(2R+1)\) lattice points.

**Sharp first resonance.** For every integer \(q\geq2\), at the first floor-activation threshold \(\lambda=1/q\), the least period of \((q,0)\) jumps from \(4q+1\) to exactly \(8q-2\):
\[
 \operatorname{per}_{F_\lambda}(q,0)=4q+1\quad(0<\lambda<1/q),\qquad
 \operatorname{per}_{F_{1/q}}(q,0)=8q-2.
\]
At resonance the new orbit contains **all** \(4q+1\) points of \(C_q\) and exactly \(4q-3\) points of \(C_{q+1}\), with no other lattice points. All inner shells \(C_0,\ldots,C_{q-1}\) retain their original exact periods. The parameter threshold is sharp even at the level of set invariance: whenever \(\lambda\geq1/q\), \(C_q\) is not invariant.

## Assumptions and scope

All quantifiers above range over integer initial states in \(\mathbb Z^2\), positive integers \(r,R\) and \(q\ge2\), and real parameters in the explicitly stated intervals. \(\lfloor t\rfloor\) means the largest integer not exceeding \(t\); in particular negative multiples and exact integer boundary values are handled without rounding conventions. The period is the **least positive return time** of the named point, not a numerically observed approximate period. No general global-periodicity assertion is made for other lattice points. The special case \(q=1\) also satisfies the displayed resonance formula, giving the known order-six map at \(\lambda=1\); it is not used as the new contribution.

## Proof

**Step 1: an exactly solvable lattice limit.** Introduce
\[
 G(x,y)=(-y-\mathbf1_{\{x<0\}},x).
\]
Fix \(r\ge1\) and let \(m=4r+1\). The four quadrant sectors of \(C_r\) are parameterized, without overlap, as follows:

| Sector | Lattice points, parameter range | Phase \(\tau_r\) modulo \(m\) |
|---|---|---|
| \(x\ge0,y\ge0\) | \((r-b,b)\), \(0\le b\le r\) | \(-4b\) |
| \(x<0,y\ge0\) | \((b-r,b)\), \(0\le b<r\) | \(2+4b\) |
| \(x<0,y<0\) | \((-a,-(r+1-a))\), \(1\le a\le r\) | \(3+4(a-1)\) |
| \(x\ge0,y<0\) | \((r-b,-b)\), \(1\le b\le r\) | \(4b\) |

Their cardinalities add to \((r+1)+r+r+r=4r+1\). Their phases cover every residue modulo \(m\) exactly once: the first sector contributes residue zero and all positive residues congruent to one modulo four; the remaining sectors contribute respectively all residues congruent to two, three and zero modulo four.

Check the four transitions directly. From the first sector with \(b=0\), \(G(r,0)=(0,r)\) has phase one; for \(b>0\), the image \((-b,r-b)\) has phase \(2+4(r-b)\equiv-4b+1\pmod m\). From the second sector, \((b-r,b)\mapsto(-b-1,b-r)\), which has phase \(3+4b\). From the third sector, \((-a,-(r+1-a))\mapsto(r-a,-a)\), with phase \(4a\). From the fourth sector, \((r-b,-b)\mapsto(b,r-b)\), with phase \(-4(r-b)\equiv4b+1\pmod m\). Thus in every case the image belongs to the same shell and its phase increases by exactly one. As the phase is bijective, \(G|_{C_r}\) is one cycle of length \(4r+1\).

**Step 2: maximal protected radius.** If \(0<\lambda<1/r\), then for every \((x,y)\in C_r\), we have \(-r\le x\le r\), whence \(\lfloor\lambda x\rfloor=-\mathbf1_{\{x<0\}}\). Thus \(F_\lambda\) agrees **pointwise** with \(G\) on \(C_r\). This proves the protected orbit statement and, by summing \(1+\sum_{j=1}^{R}(4j+1)\), the point count. Conversely \(F_\lambda(r,0)=(\lfloor\lambda r\rfloor,r)\) has shell height strictly greater than \(r\) for \(\lambda\ge1/r\). The threshold is therefore sharp.

**Step 3: the two-shell first-resonance itinerary.** Fix \(q\ge2\), put \(\lambda=1/q\), and observe that for \(-q\le x\le q\), the map agrees with \(G\) except at \(x=q\), where \(F_{1/q}(q,y)=(1-y,q)\) and \(G(q,y)=(-y,q)\). Starting at \((q,0)\), the first step is
\[
 (q,0)\xrightarrow{F_{1/q}}(1,q)\in C_{q+1}.
\]
The phase of \((1,q)\) on \(C_{q+1}\) is \(5\) modulo \(4q+5\), while that of \((q,1)\) is \(4q+1\). Their forward \(G\)-arc has exactly \(4q-4\) steps and consists of the successive phases \(5,6,\ldots,4q+1\). Every point on that arc has \(-q\le x\le q\), and its only point with \(x=q\) is the terminal point \((q,1)\). Indeed the points of \(C_{q+1}\) with \(x=-q-1\) have phases \(2\) and \(4q+3\); those with \(x=q\) have phases \(4\) and \(4q+1\); the sole point with \(x=q+1\) has phase zero. These possibilities exhaust all excluded \(x\)-values. Hence all \(4q-4\) intervening steps are exactly the \(G\)-steps, and no earlier exceptional step occurs.

The next exceptional step is
\[
 (q,1)\xrightarrow{F_{1/q}}(0,q)\in C_q.
\]
On \(C_q\), \((0,q)\) has phase \(1\) modulo \(4q+1\), and the sole point with \(x=q\) is \((q,0)\), of phase zero. Thus \(F_{1/q}\) agrees with \(G\) along the following \(4q\) steps, traversing every remaining point of \(C_q\) and first returning to \((q,0)\) at the last step. Therefore the first return has length
\[
 1+(4q-4)+1+4q=8q-2.
\]
No earlier return is possible: the traversed points on each shell have distinct phases and the two shells are disjoint. The segment on \(C_{q+1}\) has \(4q-3\) points; the segment on \(C_q\), including its returned starting point, has \(4q+1\) distinct points. This also proves the exact composition of the resonant cycle. Finally, all shells \(C_r\) with \(r<q\) are protected at \(\lambda=1/q\) by Step 2.

## Verification

The self-contained `verify.py` uses only Python integer arithmetic. It checks the shell partition, phase bijection and phase increment on shells through radius 40, the exact protected periods for rational parameters strictly below threshold, and the first-resonance least return time plus two-shell point counts for all integers \(2\le q\le120\). It also checks the first two resonances by explicit hand-scale state lists. Execution returns `VERIFY_OK`. These finite checks are **not** the proof of the universal statements: the argument above covers every positive integer shell and every real parameter in the stated interval.

## Relationship to prior work

The map and its arithmetic-periodicity conjecture are established historical objects. Akiyama and Pethő (arXiv:1206.3868) proved infinitely many periodic orbits for each admissible parameter, but did not give the exact first floor-activation period of the specified central orbit. Reeve-Black and Vivaldi (arXiv:1208.1132) developed the near-integrable limit, polygonal Hamiltonian description, density estimates, and return-strip framework; their general statements do not determine the sharp parameter boundary and the specific \(8q-2\) period jump. The later linked-strip analysis (arXiv:1405.7918) studies different large-scale asymptotics. Akiyama and Mance (arXiv:2507.12654) prove periodicity for bounded starting coordinates and describe conditional period partitions, without asserting the uniform all-integer \(q\) resonance formula or the complete shell-merger itinerary. The different sign and ordering conventions for discretized rotations must be compared at the level of their exact implications; no unproved pointwise conjugacy at rational boundaries is assumed.

## Limitations

This theorem identifies a sharp **first** quantization event for one natural family of initial points; it does not resolve the general periodicity conjecture, higher resonances, or the cycles supported entirely outside the protected diamond. It does not assert that other initial conditions behave identically at the same parameter. The scope is the floor convention shown, including exact rational endpoints. Historical novelty is a best-knowledge statement rather than an independent certification: an earlier derivation could exist in unindexed lattice-dynamics literature.

## References

1. S. Akiyama and A. Pethő, *Discretized rotation has infinitely many periodic orbits*, first public 18 June 2012, arXiv:1206.3868v1, https://arxiv.org/abs/1206.3868 .
2. H. Reeve-Black and F. Vivaldi, *Near-integrable behaviour in a family of discretised rotations*, first public 6 August 2012, arXiv:1208.1132v1, https://arxiv.org/abs/1208.1132 .
3. H. Reeve-Black and F. Vivaldi, *Asymptotics in a family of linked strip maps*, first public 30 May 2014, arXiv:1405.7918v1, https://arxiv.org/abs/1405.7918 .
4. S. Akiyama and B. Mance, *Discretized Rotation with fixed initial points*, first public 16 July 2025, arXiv:2507.12654v1, https://arxiv.org/abs/2507.12654 .
