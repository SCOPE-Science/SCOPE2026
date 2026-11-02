# Five cyclic rotated odometers: exact quarter-return laws and a half-measure five-cycle island

## Finding

Consider all five cyclic permutations of five equal interval sectors in the rotated-odometer construction of Bruin and Lukina. The first-return time to the first quarter has the following **complete pointwise laws** on the indicated half-open intervals. Throughout, \(B=[0,1/4)\), \(s\in\{0,1,2,3,4\}\), and \(\tau_s(x)=\min\{n\geq1:F_s^n(x)\in B\}\). All endpoints are exact rationals.

| \(s\) | Subintervals of \(B\) and corresponding \(\tau_s\) | \(\mathbb E_B\tau_s\) | \(\operatorname{Var}_B(\tau_s)\) |
|---|---|---:|---:|
| \(0\) | \([0,1/4):4\) | \(4\) | \(0\) |
| \(1\) | \([0,1/10):2\), \([1/10,3/20):10\), \([3/20,1/4):3\) | \(4\) | \(46/5\) |
| \(2\) | \([0,1/10):6\), \([1/10,1/5):3\), \([1/5,1/4):2\) | \(4\) | \(14/5\) |
| \(3\) | \([0,1/20):2\), \([1/20,3/20):8\), \([3/20,1/4):1\) | \(4\) | \(54/5\) |
| \(4\) | \([0,1/5):1\), \([1/5,1/4):6\) | \(2\) | \(4\) |

The mean drops from \(4\) to \(2\) **only for the backward cyclic rotation** \(s=4\). The resulting non-full return sweep is accompanied by a positive-measure invariant periodic island. More precisely, for \(s=4\) the five half-open intervals
\[
J_0=[1/4,7/20),\ J_1=[11/20,13/20),\ J_2=[17/20,19/20),\ J_3=[2/5,1/2),\ J_4=[7/10,4/5)
\]
are cyclically permuted \(J_0\to J_1\to J_2\to J_3\to J_4\to J_0\), with \(F_4^5\) the identity on their union \(C\). Every point of \(C\) has *least* period five, and \(\lambda(C)=1/2\). The complement \([0,1)\setminus C\) is exactly the saturation of \(B\) under \(F_4\), of measure \(1/2\). This statement does not exclude additional isolated or interval-periodic orbits within that complementary invariant set.

## Assumptions and scope

Work on the half-open unit interval \(I=[0,1)\), with Lebesgue length \(\lambda\). Define the dyadic odometer \(A\) by
\[
I_n=[1-2^{1-n},1-2^{-n}),\qquad
A(y)=y-1+3\cdot2^{-n}\quad(y\in I_n,\ n\ge1).
\]
The countable half-open intervals \(I_n\) partition \(I\). For each \(s\in\{0,1,2,3,4\}\) let \(R_s(x)=x+s/5\pmod1\), and put \(F_s=A\circ R_s\). These maps are bijective, measure-preserving interval exchanges, with every boundary assigned to its right-hand interval. Probabilities and moments labeled \(\mathbb E_B\) or \(\operatorname{Var}_B\) refer to normalized Lebesgue measure \(4\lambda|_B\), not a stationary probability confined to an ergodic component.

The result is a finite rational-algebraic theorem for five specific canonical cyclic sector permutations. No assertion is made for arbitrary five-symbol permutations, higher sector counts, or any other target section.

## Proof

**Return-detection reduction.** The first two dyadic branches of \(A\) send \([0,1/2)\) to \([1/2,1)\) by translation \(+1/2\), and \([1/2,3/4)\) to \([1/4,1/2)\) by translation \(-1/4\). The remaining dyadic branches partition \([3/4,1)\), and their images partition \([0,1/4)\). Hence
\[
A(y)\in B\quad\Longleftrightarrow\quad y\in[3/4,1).
\]
At each time strictly before first return to \(B\), only the following two affine transforms are possible after the rotation: if \(z=R_s(x)\in[0,1/2)\), replace \(z\) by \(z+1/2\); if \(z\in[1/2,3/4)\), replace it by \(z-1/4\). The third case \(z\in[3/4,1)\) is an immediate return.

**Exhaustive rational partition.** Begin with the single interval \(B\), labeled by the current affine translation \(0\). At each step, intersect each surviving initial-condition interval with the preimages of the fifths \([j/5,(j+1)/5)\), apply the rotation translation \(((j+s)\bmod5-j)/5\), and then intersect with the two nonreturn bands and the return band above. A nonreturn branch carries the updated affine translation; a return branch records its exact time. Every cut is a rational endpoint and all intervals are half-open. After at most ten steps there are no surviving branches for any \(s\), and the merged return intervals are precisely the five rows in the finding table. This gives a proof for **every** initial \(x\in B\): there is no truncation of an infinite orbit search. `verify_fifths.py` implements these interval intersections using integer-rational arithmetic and independently checks each entire row against explicit expected intervals.

Normalized moments follow by exact interval lengths:
\[
\mathbb E_B\tau_s=4\sum_{J\text{ in row }s}|J|\tau_s(J),\qquad
\operatorname{Var}_B\tau_s
=4\sum_{J\text{ in row }s}|J|\tau_s(J)^2-(\mathbb E_B\tau_s)^2.
\]
In particular, the values of the second moment are respectively \(16\), \(126/5\), \(94/5\), \(134/5\), and \(8\), producing the displayed variances.

**Exact five-cycle island and complement.** For the backward rotation \(s=4\), direct substitution into the finitely many dyadic branches met by each \(J_i\) gives a single affine translation on the *entire* half-open interval, with images \(F_4(J_i)=J_{i+1\bmod5}\). Their respective translations are \(+3/10\), \(+3/10\), \(-9/20\), \(+3/10\), and \(-9/20\). The five shifts sum to zero, so \(F_4^5\) is the identity. The five intervals are pairwise disjoint, establishing least period five for every point of their union. Their total length is \(5/10=1/2\).

For a direct complementary partition, the first-return row for \(s=4\) gives \(F_4([0,1/5))=[0,1/5)\), and the height-six base \([1/5,1/4)\) passes through the six disjoint half-open intervals
\[
[1/5,1/4),\ [1/2,11/20),\ [4/5,17/20),\
[7/20,2/5),\ [13/20,7/10),\ [19/20,1)
\]
before returning to the base. These six pieces contribute \(6/20=3/10\), and the self-returning base piece contributes \(1/5\). Their union is disjoint from \(C\), and together with \(C\) they partition \([0,1)\). Thus the \(B\)-saturation has measure \(1/5+3/10=1/2\) and the complement is exactly \(C\). This also explains the mean return \(2\) via the elementary return-tower identity \(\lambda(\operatorname{Sat}(B))=\lambda(B)\mathbb E_B\tau_4\). For \(s\le3\) the same identity and mean \(4\) imply full-measure return saturation, without asserting that those maps are globally ergodic.

## Verification

Run `python verify_fifths.py` with Python 3 and no external dependencies. The program performs exact \(\mathbb Q\)-arithmetic subdivision, checks all stated return intervals and their cover of \(B\), checks all ten rational moments, and checks all five translations in the periodic island together with full-interval coverage by the island and return tower. Its final success output is `PASS: five complete first-return partitions, means, variances, 5-cycle, full partition`. This is an exhaustive finite affine-branch certificate for the specified theorem, not sampling or numerical extrapolation.

## Relationship to prior work

Bruin and Lukina introduced rotated odometers, developed their Bratteli–Vershik models and general structure of periodic intervals, and studied specific five-sector permutations. The definition, measure preservation, general existence of periodic intervals, and return-map framework are their prior results. The present statement is a fully explicit **five-member cyclic-translation census** and a precise half-measure periodic decomposition for the reverse cycle, rather than a claim to have invented the model or the induction procedure. In particular, the original article's examples for other five-sector permutations do not state the five return tables above. A published three-sector cyclic/permutation return analysis gives a different set of return laws and does not imply these five-sector quantities without additional computation and boundary analysis.

## Limitations

The result concerns the first quarter and five cyclic rotations only. Full return saturation does not establish unique ergodicity. The exact return-time calculation alone does not characterize the spectrum, mixing, or all invariant probabilities of any of the maps. General earlier induction algorithms can reproduce these formulas after the additional case-specific arithmetic, and an unindexed computation or thesis table could predate them. The publication-priority comparison is therefore not a proof of global novelty. Independent mathematical audit has not been performed.

## References

- H. Bruin and O. Lukina, *Rotated Odometers*, arXiv:2101.00868, first posted 4 January 2021; *Journal of the London Mathematical Society* **107** (2023), 1983–2024, DOI:10.1112/jlms.12731.
- H. Bruin and O. Lukina, *Rotated Odometers and Actions on Rooted Trees*, arXiv:2104.05420 (2021), covering a distinct dyadic-sector setting.
