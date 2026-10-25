# Golden-mean entropy without periodic-orbit bifurcation in symmetric negative-doubling holes

## Finding

For the circle map \(T(x)=-2x\pmod 1\), remove the open symmetric hole \(H_a=(a,1-a)\), where \(0<a<1/2\), and let \(S_a=\{x\in\mathbb T:T^j x\notin H_a\text{ for all }j\geq0\}\). Put \(a_-=3/7\), \(a_+=4/9\), and \(\varphi=(1+\sqrt5)/2\). Then, **for every** \(a\in[a_-,a_+]\),
\[
h_{\mathrm{top}}(T|S_a)=\log\varphi,
\qquad
\dim_H S_a=\frac{\log\varphi}{\log2}.
\]
For every \(a\in[a_-,a_+)\), the set of *all periodic points* of \(T|S_a\) is independent of \(a\), and its Artin–Mazur zeta function is
\[
\zeta_a(z)=\frac{1}{(1-z)(1-z-z^2)(1-z+z^2)}.
\]
At \(a=a_+\), exactly two additional primitive period-three orbits enter, namely \(\{4/9,1/9,7/9\}\) and \(\{5/9,8/9,2/9\}\), and no other periodic points appear. Consequently
\[
\zeta_{a_+}(z)=\frac{1}{(1-z)(1-z-z^2)(1-z+z^2)(1-z^3)^2}.
\]
Equivalently, writing \(P_n(a)=\#\operatorname{Fix}(T^n|S_a)\), \(L_n=\varphi^n+(-\varphi^{-1})^n\), one has
\[
P_n(a)=1+L_n+2\cos(n\pi/3)+6\,\mathbf1_{\{a=a_+,\;3\mid n\}}
\qquad(n\geq1,\ a\in[a_-,a_+]).
\]
The extra orbits change the zeta function at the endpoint while the topological entropy remains constant and positive.

## Assumptions and scope

The circle \(\mathbb T\) identifies real endpoints \(0\) and \(1\); hence \(0\) is one fixed point, not a pair of interval endpoints. The map \(T\) is a continuous, degree-two, orientation-reversing expanding circle covering. Every survivor includes hole boundary points whenever their forward orbits avoid the *open* hole. Zeta functions are interpreted as formal power series (also convergent near \(z=0\)); they count distinct geometric periodic points, not one-sided Markov addresses. The distinction is essential at the rational hole boundaries. No assertion concerns other hole locations or the maximum entropy plateau.

## Proof

**1. Two exact Markov descriptions.** Let \(k\in\{3,4\}\), \(m=2k+1\), and \(a=k/m\). Partition the two retained closed arcs by the grid \(\{j/m:0\leq j\leq m\}\). Denote by \(I_j=[j/m,(j+1)/m]\) the intervals with \(j\in J_k=\{0,1,\ldots,2k\}\setminus\{k\}\); the omitted interval is the hole. The image of the interior of each retained interval spans exactly two grid intervals. Define
\[
b_j=\begin{cases}m-2j-2,&j<k,\\2m-2j-2,&j>k,\end{cases}
\qquad
(A_k)_{j\ell}=\mathbf1_{\{\ell\in\{b_j,b_j+1\}\cap J_k\}}.
\]
The transition lists are, with cell indices shown literally,

- \(k=3\): `0:5,6; 1:4; 2:1,2; 4:4,5; 5:2; 6:0,1`.
- \(k=4\): `0:7,8; 1:5,6; 2:3; 3:1,2; 5:6,7; 6:5; 7:2,3; 8:0,1`.

Direct characteristic-polynomial computation gives
\[
\det(\lambda I-A_3)=(\lambda-1)(\lambda+1)(\lambda^2-\lambda-1)(\lambda^2-\lambda+1),
\]
\[
\det(\lambda I-A_4)=(\lambda-1)(\lambda+1)^3(\lambda^2-\lambda-1)(\lambda^2-\lambda+1).
\]
Every admissible infinite path determines a point by nested inverse-image intervals, and only partition-grid boundary points admit multiple one-sided addresses; their multiplicity is at most two. Conversely every survivor point has an address. The finite-to-one coding therefore has the same topological entropy as the corresponding finite-state edge shift, namely \(\log\rho(A_3)=\log\rho(A_4)=\log\varphi\). Since \(S_{a_-}\subseteq S_a\subseteq S_{a_+}\), monotonicity gives the displayed entropy equality for all intermediate \(a\).

The slope modulus is uniformly \(2\). Admissible cylinder intervals have lengths bounded above and below by positive grid-dependent constants times \(2^{-n}\); finite endpoint duplication does not affect exponential cylinder growth. The upper Hausdorff bound follows by covering the survivor with \(O((\varphi+\epsilon)^n)\) cylinders. For the lower bound, a maximal strongly connected component of \(A_k\) with Perron root \(\varphi\) supports its usual Perron cylinder probability, yielding a Frostman estimate of exponent arbitrarily close to \(\log\varphi/\log2\). Thus the dimension formula holds at both endpoints. Inclusion and monotonicity of Hausdorff dimension yield the formula throughout the interval.

**2. No intermediate periodic points enter.** Refine the \(a_+\) Markov partition by both grids of denominators seven and nine. The resulting consecutive endpoints, in increasing order, are
\[
0,\ 1/9,\ 1/7,\ 2/9,\ 2/7,\ 3/7,\ 4/9,\ 5/9,\ 4/7,\ 5/7,\ 7/9,\ 6/7,\ 8/9,\ 1.
\]
Let the resulting open cells be indexed `0,1,...,12`, omitting cell `6`, the open hole \((4/9,5/9)\). Their positive-length image transitions are

`0:10,11,12; 1:9; 2:7,8; 3:5; 4:2,3,4; 5:1; 7:11; 8:8,9,10; 9:7; 10:4,5; 11:3; 12:0,1,2`.

The strongly connected components are exactly \(\{0,12\}\), \(\{2,4,8,10\}\), and \(\{1,3,5,7,9,11\}\). The last component is a single directed six-cycle `5→1→9→7→11→3→5`. Every periodic orbit that enters either *new annulus* \((3/7,4/9)\) (cell `5`) or \((5/9,4/7)\) (cell `7`) in its interior must follow this cycle. Its six-step branch on the cycle is respectively \(T^6(x)=64x-27\) or \(T^6(x)=64x-36\). These have unique fixed points \(3/7\) and \(4/7\), both outside the annulus interiors. Consequently no periodic orbit enters the open annuli. Any periodic point in \(S_{a_+}\setminus S_{a_-}\) must therefore belong to the newly admitted boundary orbits through \(4/9\) or \(5/9\). Iterating yields precisely the two claimed primitive three-cycles. They are excluded for \(a<a_+\) because they meet a point in the larger open hole. All other periodic points are already in \(S_{a_-}\).

The refined partition endpoints themselves produce no exceptions to this argument: every refined-grid point strictly inside the old forbidden arc is among the two newly admitted boundary three-cycles, or lies in the open hole; the old endpoints \(3/7,4/7\) already survive.

**3. Correct the periodic-boundary addresses.** For an interval Markov presentation of an expanding piecewise-affine covering, \(\operatorname{tr}(A_k^n)\) counts cyclic \(n\)-step one-sided *addresses*. Such addresses correspond bijectively to actual periodic points away from partition boundaries. The boundary orbits must be counted separately.

For \(k=3\), the grid boundary orbits are: the fixed circle point \(0\), which has two addresses exchanged by the orientation-reversing map; and one six-cycle on \(\{1/7,\ldots,6/7\}\), which has exactly one admissible cyclic side address. Therefore the fixed point \(0\) contributes two addresses when \(n\) is even and none when \(n\) is odd, although it always contributes one geometric point. The exact correction is
\[
\operatorname{tr}(A_3^n)-P_n(a_-)=(-1)^n.
\]
For \(k=4\), the grid boundary orbits are the three fixed points \(0,1/3,2/3\), each with two opposite exchanged side addresses, together with the two primitive three-cycles through \(4/9\) and \(5/9\). Each of these three-cycles has a hole boundary with just one permissible side, but its odd return reverses sides. It consequently has no admissible bi-infinite cyclic side address, although all six points are geometrically periodic. Thus
\[
\operatorname{tr}(A_4^n)-P_n(a_+)=3(-1)^n-6\mathbf1_{\{3\mid n\}}.
\]
The matrix factorizations in Step 1 and the identity
\[
\exp\left(\sum_{n\ge1}\frac{\operatorname{tr}(A^n)}{n}z^n\right)=\det(I-zA)^{-1}
\]
produce the two stated rational zeta functions by the elementary expansions of \(\log(1+z)\) and \(\log(1-z^3)\). In particular, the correction removes the spurious \((1+z)\) factors from both determinants, while the two newly admitted three-cycles give \((1-z^3)^{-2}\). Taking logarithmic derivatives gives the formula for every \(P_n\), completing the proof.

## Verification

The accompanying standalone `checks/verify.py` computes both characteristic polynomials exactly, enumerates all actual circle fixed points by integer arithmetic through period fourteen, compares all Markov traces with their precise boundary corrections, verifies the refined transition graph and its strongly connected components, and checks both entering three-cycles. Additional exact enumerations at representative interior parameters check their common periodic-point counts through period twelve. The complete recorded execution is in `checks/verify-output.txt`. These finite checks are not used as substitutes for the all-period argument, the entropy/dimension proof, or the symbolic boundary accounting.

## Relationship to prior work

Ding, Steiner, and Sun (arXiv:2610.03327v1, publicly submitted 2026-10-02) establish the general negative-doubling survivor framework, its entropy–dimension identity, and the value \(\log\varphi\) for the periodic kneading boundary pair \((112)^\infty,(221)^\infty\), corresponding to \((4/9,5/9)\) (their Example 4.4). The entropy value *at that endpoint* is therefore known; it is **not** asserted as new here. The additional assertions concern the one-parameter symmetric interval starting at \(3/7\), equality of *every individual periodic point set* before its final endpoint, and the exact Artin–Mazur zeta jump at that endpoint. The source treats symbolic survivor/entropy plateaux and does not supply these particular periodic counting formulas or the boundary-address correction. Related published work on symmetric negative-doubling holes covers the different region \(a\le2/5\) with zero entropy. General zeta/Markov determinant methods are used as known tools, not claimed as inventions.

## Limitations

The result is for the **circle** negative-doubling map and **open** symmetric holes; treating \(0\) and \(1\) as distinct interval endpoints changes periodic counts and must not be conflated with the circle formula. The proof says nothing about all other entropy plateaux, the maximum period-fiber size, or behavior beyond \(a_+\). The historical-priority assessment has not excluded every general past theorem about zeta functions of open Markov maps. No independent audit has been performed.

## References

1. Yiming Ding, Wolfgang Steiner, Yun Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1 (first public 2026-10-02), especially Sections 2–4 and Example 4.4. https://arxiv.org/html/2610.03327v1
2. Michael Artin and Barry Mazur, *On periodic points*, Annals of Mathematics 81 (1965), 82–99. DOI: 10.2307/1970384. The zeta-function definition and the periodic-point framework are classical.
3. Nikita Sidorov, *Supercritical holes for the doubling map*, Acta Mathematica Hungarica 143 (2014), 298–312. DOI: 10.1007/s10474-014-0403-7. Context on holes in expanding circle dynamics; the doubling-map orientation and exact hole geometry differ.
