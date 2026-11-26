# The 48-point exceptional-curve deficit on the Fermat degree-two del Pezzo surface over \(\mathbb F_{25}\)

## Finding

Let \(k=\mathbb F_{25}\), let \(S\) be the degree-two del Pezzo surface \(w^2=x^4+y^4+z^4\) in \(\mathbb P_k(1,1,1,2)\), and write \(\pi:S\to\mathbb P^2_k\) for its anticanonical double cover. Let \(E\) be the union of the 56 exceptional curves. Then the rational points of \(S\) outside \(E\) are exactly the two lifts of each of the 24 points having one zero coordinate and nonzero coordinate ratio \(t\) with \(t^4\) a nonidentity cube root of unity. The criterion is independent of the order in which the two nonzero coordinates are taken. This whole complement is a single orbit under coordinate permutations, coordinatewise multiplication by fourth roots of unity, and the deck involution.

The numerical deficit \(826-778=48\) is an input to the exhaustion argument below: it follows from the existing Fermat-quartic incidence data and the degree-two del Pezzo boundary formula, not an independent novelty claim.

## Scope and arithmetic inputs

Everything concerns the indicated double cover in characteristic five, not a quadratic twist or a different split del Pezzo surface. The branch quartic \(C\) is smooth by the gradient criterion. The exceptional curves above a geometric bitangent are its two components in the double cover. The 28 Fermat bitangents are the sixteen lines \(x+ay+bz=0\), with \(a^4=b^4=1\), and the twelve coordinate-ratio lines \(x_i=\alpha x_j\) for \(i<j\) and \(\alpha^4=-1\). Over \(k\) all the latter scalars exist since \(8\mid 24\). On each ratio line the quartic restricts to the fourth power of the remaining coordinate. On each of the sixteen other lines the restriction equals \(2(a^2y^2+ab yz+b^2z^2)^2\), also a square over \(k\). Thus all 56 curves split, and a rational cover point belongs to \(E\) if and only if its image lies on a bitangent.

For completeness the known split-surface formula gives \(\#S(k)=25^2+8\cdot25+1=826\). The known Fermat incidence counts in characteristic five are \((n_2,n_3,n_4)=(240,16,15)\), with no fivefold point. These counts apply over \(k\) because all lines, hence all their pairwise intersections, are rational. The branch count is \(\#C(k)=44\): there are 12 one-zero-coordinate points with \(t^4=-1\), and for all coordinates nonzero the equation is \(a+b+1=0\) with \(a=(x/z)^4,b=(y/z)^4\) in \(\mu_6=\{\pm1,\pm\omega,\pm\omega^2\}\). Using \(\omega^2+\omega+1=0\), this equation gives only the two ordered pairs \((\omega,\omega^2),(\omega^2,\omega)\), with sixteen preimages each. In the Knecht–Reyes boundary formula the plane fourfold and threefold incidence counts are \(h=15,e=16\), respectively (not the doubled counts on \(S\)). Therefore
\[
\#E(k)=6h+2e+28(2\cdot25-25)-\#C(k)=778.
\]

## Identifying the complement

On \(z=0\) write an axis point with nonzero \(x,y\) as \([t:1:0]\). One of the sixteen ordinary bitangents contains it exactly when \(t^4=1\). A coordinate-ratio bitangent contains it exactly when \(t^4=-1\): the other two families of ratio lines cannot meet \([t:1:0]\) with both displayed coordinates nonzero. For \(t^4=\omega\) or \(\omega^2\) there is consequently no bitangent through the point, while the branch value is \(-\omega^2\) or \(-\omega\), respectively. Both values are nonzero squares: \(-1\) is a square in \(k\), and every cube root of unity is a square in its cyclic order-three subgroup. The fibre consists of exactly two rational points and avoids \(E\).

The fourth-power map has four preimages over each of the specified fourth powers, yielding eight such points on each of three axes. They are disjoint across the axes since each has exactly one zero coordinate. Their 48 lifts exhaust the deficit. Fourth-root scalings act transitively on the four ratios for a fixed fourth power, swapping the nonzero coordinates interchanges \(\omega\) and \(\omega^2\), and permutations move between axes. These base automorphisms lift by fixing \(w\); the deck involution exchanges the two points of each fibre. This proves transitivity on the complement.

## Verification and relationship to prior work

The standalone `verify.py` performs an exhaustive check of the bitangent and surface-point incidences over \(\mathbb F_5[\theta]/(\theta^2-2)\), independently checks the axis criterion by set equality, and checks the base symmetry orbit. The proof above uses the known incidence and boundary formulas and does not require that enumeration.

- Kresch and Tschinkel, *On the arithmetic of del Pezzo surfaces of degree 2*, §2, [full text](https://wrap.warwick.ac.uk/id/eprint/757/1/WRAP_Kresch_arithmetic_del_pezzo.pdf), supply the Fermat bitangent and exceptional-curve descriptions.
- Knecht and Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, [arXiv:1510.04621](https://arxiv.org/abs/1510.04621), §2 and Question 4.8, give the boundary count and discuss the existence question at field size 25. This particular example is not full; no conclusion follows about the existence of some other full surface at that field size.
- [*Exactly two exceptional characteristics for triple concurrence of Fermat-quartic bitangents*](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exactly-two-exceptional-characteristics-for-triple-concurrence-o--315db4bfe71c) gives the geometric incidence counts used here. [*Exceptional primes and Frobenius spectra for the Fermat quartic bitangent arrangement*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exceptional-primes-and-frobenius-spectra-for-the-fermat-quartic--1461ee4380ba) gives the rational incidence counts directly for characteristic five and \(q\equiv1\pmod 8\). Their aggregate incidence data give the size of the complement with the boundary formula, but not its location and single-orbit description. The exact complement, not the count alone, is the finding.
