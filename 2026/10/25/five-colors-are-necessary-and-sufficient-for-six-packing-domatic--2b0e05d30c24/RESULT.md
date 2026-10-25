# Five colors are necessary and sufficient for six packing-domatic broadcasts on the two-way infinite path

## Finding

Let \(P_\infty\) be the two-way infinite path. For the packing \(k\)-domatic chromatic number introduced by Brešar, Ferme and Hu, the previously undetermined six-layer case has the exact value
\[
\boxed{\chi_{\rho,6}(P_\infty)=5.}
\]
Equivalently, a packing coloring of \(P_\infty\) with colours drawn from \(\{1,2,3,4\}\) can support at most five pairwise disjoint dominating broadcast layers. Five layers are attainable with four colours, as established in the cited paper.

The new contribution is the four-colour exclusion: an explicit finite-window counting obstruction to six disjoint covering layers. The five-colour construction below is taken from, and independently checked against, the cited paper.

## Assumptions and scope

The vertices of \(P_\infty\) are the integers, and two vertices are adjacent exactly when their difference has absolute value one. A packing coloring with palette \(\{1,\ldots,t\}\) is any map \(f:\mathbb Z\to\{1,\ldots,t\}\) such that, whenever distinct vertices \(u,v\) both have color \(j\), their distance satisfies \(|u-v|>j\).

A partition of the vertex set into \(k\) disjoint nonempty sets \(A_1,\ldots,A_k\) is broadcast dominating for \(f\) if, for every integer vertex \(x\) and each \(i\), there exists \(u\in A_i\) with \(|u-x|\le f(u)\). The least admissible palette maximum is \(\chi_{\rho,k}(P_\infty)\). We consider \(k=6\) and all possible infinite assignments and partitions; no periodicity is assumed for the lower bound.

## Proof

**Four colors cannot supply six layers.** Suppose a packing coloring \(f:\mathbb Z\to\{1,2,3,4\}\) admits six disjoint broadcast-dominating layers. Fix the consecutive target vertices \(I=\{1,2,\ldots,367\}\). Because every broadcast radius is at most four, every transmitter covering any target in \(I\) lies in the 375-vertex interval \(J=\{-3,-2,\ldots,371\}\).

For each target in \(I\) and for each of the six layers, choose a transmitter in that layer covering the target. Since the layers are disjoint, the six choices for a fixed target are distinct. Thus there are at least \(6\cdot367=2202\) pairs \((u,x)\) with \(u\in J\), \(x\in I\), and \(|u-x|\le f(u)\).

Let \(c_j\) be the number of vertices of color \(j\) in \(J\). A color-\(j\) transmitter covers at most \(2j+1\) targets. The packing constraint forces successive vertices of color \(j\) to be at least \(j+1\) units apart, whence
\[
c_2\le\left\lceil\frac{375}{3}\right\rceil=125,\quad
c_3\le\left\lceil\frac{375}{4}\right\rceil=94,\quad
c_4\le\left\lceil\frac{375}{5}\right\rceil=75.
\]
Since \(c_1+c_2+c_3+c_4=375\), the total number of covering pairs is at most
\[
3c_1+5c_2+7c_3+9c_4
=3\cdot375+2c_2+4c_3+6c_4
\le1125+250+376+450=2201.
\]
This contradicts the necessary \(2202\) pairs. Therefore \(\chi_{\rho,6}(P_\infty)\ge5\). The argument also excludes palettes with fewer than four colors, because they are contained in the four-color case.

The same method gives a reusable asymptotic capacity inequality: with colors at most four, the average possible number of broadcast incidences per path vertex is bounded above by
\[
3+\frac{2}{3}+\frac{4}{4}+\frac{6}{5}=\frac{88}{15}<6,
\]
where the color-\(j\) vertex density is at most \(1/(j+1)\) for \(j\ge2\). The finite window above removes any assumption about limiting color frequencies.

**Five colors supply six layers.** Use the six-periodic coloring, indexed from zero,
\[
(f(0),f(1),\ldots,f(5))=(5,1,2,4,1,3).
\]
The two consecutive occurrences of color one are three steps apart; every color from two through five recurs exactly six steps later. Thus the packing condition holds. Partition the integers into the following six classes using residues modulo thirty:

| Class | Residues modulo thirty |
| --- | --- |
| \(A_1\) | \(1,4,7,10,13,16,19,22,25,28\) |
| \(A_2\) | \(0,8,15,23\) |
| \(A_3\) | \(2,9,17,24\) |
| \(A_4\) | \(3,11,18,26\) |
| \(A_5\) | \(5,12,20,27\) |
| \(A_6\) | \(6,14,21,29\) |

Each integer occurs in exactly one residue class. Every consecutive pair in \(A_1\) is three steps apart, and radius-one broadcasts from \(A_1\) cover all integers. For each other class, successive transmitter distances around the thirty-period are alternately seven and eight, while transmitter colors occur cyclically as \((5,2,4,3)\) up to rotation. The consecutive radii have sums at least one less than the corresponding distance, so their integer-radius intervals leave no uncovered vertex. Hence each of the six classes is a dominating broadcast. This is the published upper-bound witness and proves \(\chi_{\rho,6}(P_\infty)\le5\).

Combining both inequalities yields the displayed equality.

## Verification

The standalone `verify.py` checks the six-period packing constraint, verifies that the six residue classes partition a full thirty-period, and checks coverage for every target residue and every class. These finite checks are exhaustive for this explicitly periodic witness. It also recomputes the exact \(2201<2202\) obstruction and the rational \(88/15<6\) capacity inequality. The corresponding output is in `verify_output.txt`. The unrestricted lower bound is the mathematical counting argument above, not an inference from finite experiments.

## Relationship to prior work

Brešar, Ferme and Hu introduced packing \(k\)-domatic colorings and proved \(\chi_{\rho,6}(P_\infty)\in\{4,5\}\). Their Theorem 3.6 exhibits the periodic five-color, six-layer witness reproduced above, while the text after that theorem leaves the distinction between four and five open. Theorem 3.6 also determines the corresponding values for three, four and five layers. The general lower bound in their Proposition 3.7 does not exclude four colors for six layers. The missing implication is supplied here by the finite broadcast-incidence obstruction, without assuming any periodicity of a putative four-coloring.

Classical packing coloring, studied before this combined invariant, imposes the same-color distance constraints but does not impose six disjoint broadcast-dominating layers; those older results do not immediately supply the stated obstruction. Searches for the new invariant under packing-domatic, broadcast-domatic, infinite-path and two-way-path terminology revealed no directly covering published result. This assessment is limited to the available scientific literature.

## Limitations

Only the six-layer parameter on the two-way infinite path is determined. No claim is made about other numbers of layers, finite-path thresholds, uniqueness of optimal patterns, or independent external validation. The original source supplies the upper bound, so only the new lower bound is claimed as an original step. An equivalent solution in inaccessible or unindexed work remains possible.

## References

1. Boštjan Brešar, Jasmina Ferme and Wenjie Hu, *Partitioning an S-packing coloring into broadcast dominating sets*, arXiv:2610.03477v1, publicly posted 2026-10-02, especially Definitions 1.1–1.2, Theorem 3.6, Proposition 3.7 and Section 5. https://arxiv.org/html/2610.03477v1
2. Wayne Goddard, Sandra M. Hedetniemi, Stephen T. Hedetniemi, John M. Harris and Douglas F. Rall, *Broadcast chromatic numbers of graphs*, Ars Combinatoria 86 (2008), 33–49; earlier packing-coloring framework, cited as Reference 7 by Brešar et al.
