# Exact exceptional-prime reductions of a rational weak Ziegler pair

## Finding

Let \(C=V(X^2+Y^2-25Z^2)\subset\mathbb P^2_{\mathbb Z}\). Form two conic-line arrangements \(\mathcal A_1\) and \(\mathcal A_2\) using this conic and the six integral lines in the table below, where an entry \((a,b,c)\) denotes \(aX+bY+cZ=0\). These are the explicit rational weak Ziegler pair of Lampa-Baczyńska and Wójcik [1].

| Line | \(\mathcal A_1\): \((a,b,c)\) | \(\mathcal A_2\): \((a,b,c)\) |
| --- | --- | --- |
| 1 | \((1,0,-4)\) | \((1,0,4)\) |
| 2 | \((1,0,4)\) | \((1,0,0)\) |
| 3 | \((3,4,0)\) | \((1,0,-4)\) |
| 4 | \((1,0,3)\) | \((0,1,-3)\) |
| 5 | \((6,1,21)\) | \((0,1,3)\) |
| 6 | \((0,1,3)\) | \((3,-4,0)\) |

For **every prime \(p\ge7\)**, the reductions satisfy the following complete alternatives.

1. \(\mathcal A_{2,p}\) has six distinct lines and a smooth conic, with all component intersections transverse. Its singular locus consists of exactly six ordinary double points, three ordinary triple points, and two ordinary quadruple points. All eleven points are \(\mathbb F_p\)-rational. Its complete labeled incidence structure agrees with the characteristic-zero structure.
2. \(\mathcal A_{1,p}\) has exactly the same ordinary singularity counts, with all eleven points rational and the same labeled incidences, for every \(p\notin\{7,11\}\).
3. At \(p=7\), the first and fourth lines coincide, as do the third and fifth. The *reduced support* of \(\mathcal A_{1,7}\) is a smooth conic together with four distinct lines, with precisely **two ordinary double points, two ordinary triple points and one ordinary quadruple point**. Its five singular points are all \(\mathbb F_7\)-rational.
4. At \(p=11\), all six lines of \(\mathcal A_{1,11}\) remain distinct, but line 5 is tangent to the conic at the point \([1:2:8]\), where lines 2 and 3 also meet. This is a nonordinary four-branch point (one contact-two branch pair). There are exactly **ten** distinct geometric singular points: five double, three triple, and two quadruple as counts by the number of local branches, with the indicated quadruple point nonordinary. All ten are \(\mathbb F_{11}\)-rational.

Consequently, the exact exceptional-prime set \(p\ge7\) for preservation of the *published labeled smooth-component incidence arrangement* is \(\{7,11\}\) for \(\mathcal A_1\) and the empty set for \(\mathcal A_2\).

## Assumptions and scope

We reduce the **specified integral equations**, with no coordinate changes, modulo prime \(p\ge7\), and work over an algebraic closure when testing geometric singularity and intersection types. Ordinary \(r\)-fold means \(r\) smooth local branches with mutually distinct tangent directions. Multiplicities at the characteristic-\(11\) nonordinary point are counted by local branches, not by pairwise intersection numbers. We do not claim that this exceptional-prime set is intrinsic under changes of integral model, nor that Jacobian syzygies or near-freeness are preserved modulo \(p\). The source's complex weak Ziegler pair and its common counts are background, not claimed as new.

## Proof

**Completeness of the rational intersection census.** Parametrize the conic by
\[
[5(1-t^2):10t:1+t^2],\qquad t\in\mathbb P^1.
\]
For any line \(aX+bY+cZ=0\), its intersections with \(C\), counted with multiplicity, correspond to the roots in \(\mathbb P^1\) of
\[
(c-5a)t^2+10bt+(5a+c)=0.
\]
The discriminant is \(4(25(a^2+b^2)-c^2)\). For all twelve displayed lines it is a nonzero integer square, so **both distinct conic intersections are rational**. Each intersection of two distinct rational lines is rational. Taking the union of the fifteen line-pair intersections and twelve conic-line intersections, with repetitions removed, gives exactly eleven projective points for each arrangement. The complete coordinates and their incidences are enumerated from the input equations by `verify.py`, with no supplied output point list needed. In characteristic zero, for each arrangement the profile is \((t_2,t_3,t_4)=(6,3,2)\), and all intersections are ordinary: each conic-line discriminant is nonzero and every line is smooth. This is consistent with the original paper [1].

**A finite certificate for the all-prime assertion.** Represent each rational singular point by a primitive integral triple. Two distinct such projective points collide after reduction modulo \(p\) exactly if \(p\) divides the gcd of the three coordinates of their cross product. Computing those gcd prime supports over every unordered pair of the eleven rational points gives
\[
S_{\mathrm{points}}(\mathcal A_1)=\{2,3,5,7,11\},\qquad
S_{\mathrm{points}}(\mathcal A_2)=\{2,3,5\}.
\]
Applying the same test to the six line coefficient triples gives
\[
S_{\mathrm{lines}}(\mathcal A_1)=\{2,3,7\},\qquad
S_{\mathrm{lines}}(\mathcal A_2)=\{2,3\}.
\]
The executable certificate in `verify.py` recomputes these four supports by exact integer arithmetic. For \(p\ge7\), the common conic is smooth. Outside the supports, the six lines are distinct, the eleven complete intersection points stay pairwise distinct, and both roots of each conic-line intersection stay distinct. Hence there are no new coincidences or tangencies: every intersection of two components is already a specialization of one of the eleven rational points. The source incidences and their transverse local types therefore survive for every such prime, not just sampled primes.

**Characteristic seven.** Direct coefficient reduction yields \(L_1=L_4\) and \(L_3=L_5\) as projective lines, with no other coincidences. The reduced support thus has only four line components. Exhausting the \(7^2+7+1=57\) rational projective points gives the complete singular locus
\[
\begin{array}{c|c}
[1:1:2]&4\\
[1:1:5]&3\\
[1:6:5]&3\\
[1:6:2]&2\\
[0:1:0]&2
\end{array}
\]
where the right-hand column gives the number of smooth branches. All conic intersections with the distinct reduced lines remain transverse. Every intersection is rational, so this finite-field census is exhaustive over the algebraic closure as well: all pairwise line intersections and both conic intersections with each line are rational. The pairwise Bézout count is \(\binom{4}{2}+2\cdot4=14=2\binom{2}{2}+2\binom{3}{2}+\binom{4}{2}\) when the right side is read as \(6+6+2\) from one quadruple, two triples and two doubles.

**Characteristic eleven.** The unique collision of distinct rational singular points occurs between \([4:-3:-1]\) and \([104:153:-37]\); both reduce to \(P=[1:2:8]\). Point \(P\) lies on lines 2, 3, 5 and the conic. In particular, the gradient of the conic at \(P\), namely \((2X,2Y,-50Z)\), is proportional over \(\mathbb F_{11}\) to the coefficients \((6,1,21)\) of line 5. Thus line 5 is tangent to \(C\) there. Its two previously distinct conic intersections merge; the other five lines each retain two distinct conic intersections. An independent census of the \(11^2+11+1=133\) rational projective points gives ten singular points, with branch-count profile \((5,3,2)\). The classical pairwise Bézout total \(15+12=27\) agrees with \(5+3\cdot3+2\cdot6+1=27\), where the last unit accounts for the unique contact-two pair. Again all geometric intersection points are rational because the line-line and line-conic parameter equations split over \(\mathbb F_{11}\).

The remaining assertions follow from the gcd support exclusion and the independent modular profiles at the two exceptional primes. \(\square\)

## Verification

Run `python3 verify.py` using Python 3.9 or newer. The program uses only the standard library. It constructs the conic-line intersections via rational root formulas, computes all rational singular points and their incidences, factors all projective collision contents, then enumerates finite projective planes in characteristics 7 and 11 (and spot-checks 13, 17, 19, 23, 29). Its expected opening output is `VERIFY_OK`. The all-prime claim rests on the symbolic finite support certificate plus the proof that these lists exhaust the intersections, not on the finite prime spot checks.

## Relationship to prior work

Lampa-Baczyńska and Wójcik [1] construct the explicit pair over \(\mathbb Q\), prove common weak combinatorics and different minimal degrees of Jacobian relations. That complex-geometry result does not determine behavior of these *integral models* in positive characteristic. The later conic-arrangement work [2] distinguishes weak and strong Ziegler configurations through combinatorics and Milnor algebra data, not the exceptional-prime incidence behavior here. The general theorem that finite arrangements admit good reductions away from finitely many primes [3] supplies context, but does not imply the exact sets or the special-fiber geometry for this line-conic pair. No new freeness or syzygy classification is claimed.

## Limitations

The result concerns the two fixed integral polynomial presentations, prime characteristics at least seven and geometric component incidence, not other arithmetic models, primes 2, 3, 5, Jacobian syzygies in positive characteristic, étale specialization data, or homological properties of the reduced schemes. At \(p=7\) the original product is nonreduced; the stated geometric profile is for its reduced support. At \(p=11\), the branch-count profile alone does not encode tangency, which is explicitly recorded above.

## References

[1] M. Lampa-Baczyńska and D. Wójcik, *Weak Ziegler pairs of conic-line arrangements with ordinary singularities*, arXiv:2403.16870v1 (first public 2024-03-25), especially the Main Theorem and displayed equations in its proof. DOI: 10.4064/ba240508-29-8.

[2] A. Bromboszcz, B. Jarosławski and P. Pokora, *On plus–one generated arrangements of plane conics*, DOI: 10.1007/s10711-025-01063-w, Section 5 (weak/strong Ziegler framework).

[3] R. P. Stanley, *An Introduction to Hyperplane Arrangements*, Section 5, proposition on the good reduction of integral arrangements; background on general finiteness of bad primes, not a theorem specifically about conic-line arrangements.
