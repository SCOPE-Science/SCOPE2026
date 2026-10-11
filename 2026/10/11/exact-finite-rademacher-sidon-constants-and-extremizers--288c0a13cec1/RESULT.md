# Exact finite Rademacher Sidon constants and extremizers
## Finding
Let \(E=\{-1,+1\}\), and for an integer \(n\ge5\) let \(r_j:E^n\to\mathbb T\) be the coordinate character \(r_j(\varepsilon)=\varepsilon_j\). Define the Sidon constant of these \(n\) coordinate characters by
\[
S_n=\sup_{a\in\mathbb C^n\setminus\{0\}}\frac{\sum_{j=1}^n|a_j|}{\max_{\varepsilon\in E^n}\left|\sum_{j=1}^n\varepsilon_j a_j\right|}.
\]
Then
\[
S_n=n\sin\!\left(\frac{\pi}{2n}\right).
\]
Moreover, equality holds for a nonzero coefficient vector \(a\) if and only if there are \(r>0\), \(\theta\in\mathbb R\), a permutation \(\sigma\) of \(\{1,\ldots,n\}\), and signs \(\eta_j\in\{-1,+1\}\) such that
\[
a_{\sigma(j)}=\eta_j r\exp\!\left(i\left(\theta+\frac{(j-1)\pi}{n}\right)\right),\qquad 1\le j\le n.
\]
Equivalently, the coefficient moduli are equal and their directions modulo sign are equally spaced by \(\pi/n\).

## Assumptions and scope
The scalar field is \(\mathbb C\). The norm on \(\sum_j a_jr_j\) is the supremum over the finite group \(E^n\). The theorem is stated for every integer \(n\ge5\); no assertion about smaller dimensions is included in this result. The result concerns the exact finite-dimensional constant and all equality cases, not merely the limiting Sidon constant of the infinite Rademacher system.

## Proof
Put
\[
L=\sum_{j=1}^n|a_j|,
\qquad
M=\max_{\varepsilon\in E^n}\left|\sum_{j=1}^n\varepsilon_j a_j\right|.
\]
Identify \(\mathbb C\) with the Euclidean plane and form the zonogon
\[
Z=\sum_{j=1}^n[-a_j,a_j].
\]
It is the convex hull of the signed sums \(\sum_j\varepsilon_j a_j\). Hence every point of \(Z\) lies in the closed disk of radius \(M\) centered at the origin, and \(M\) is the maximum Euclidean norm on \(Z\).

Group nonzero generators that are parallel modulo sign. If there are \(d\) distinct generator directions, then \(Z\) has at most \(2d\le2n\) sides. For each generator direction, the two opposite boundary edges together have length four times the sum of the generator lengths in that direction. Therefore
\[
\operatorname{per}(Z)=4L.
\]
If all generators are parallel, then \(M=L\), so the desired inequality is immediate. Assume henceforth that \(Z\) is two-dimensional and write \(m\) for its number of sides.

We use the following elementary polygon lemma. If a convex \(m\)-gon is contained in a disk of radius \(R\), then its perimeter is at most
\[
2mR\sin\!\left(\frac{\pi}{m}\right).
\]
To prove the lemma, maximize perimeter over all convex \(m\)-gons in the disk. A genuine vertex of a maximizing polygon cannot lie strictly inside the disk: with its two neighbors fixed, the sum of its two incident edge lengths is a convex function of that vertex, and an interior maximum can occur only when the two incident unit directions cancel, which makes the vertex collinear with its neighbors and hence nongenuine. Thus all genuine maximizing vertices lie on the boundary circle. If their successive central-angle gaps are \(\delta_1,\ldots,\delta_m>0\), then \(\sum_k\delta_k=2\pi\) and the perimeter is
\[
2R\sum_{k=1}^m\sin(\delta_k/2)
\le 2mR\sin\!\left(\frac{\pi}{m}\right)
\]
by concavity of \(\sin\) on \([0,\pi]\). Degenerate vertices only decrease the effective number of sides. Equality requires all vertices on the circle and all \(\delta_k=2\pi/m\), so the polygon is regular.

Apply the lemma to \(Z\) with \(R=M\). Since \(m\le2n\), and \(x\mapsto x\sin(\pi/x)\) is strictly increasing for \(x\ge2\),
\[
4L=\operatorname{per}(Z)
\le2mM\sin\!\left(\frac{\pi}{m}\right)
\le4nM\sin\!\left(\frac{\pi}{2n}\right).
\]
Thus
\[
\frac{L}{M}\le n\sin\!\left(\frac{\pi}{2n}\right).
\]

For sharpness, take coefficients of one common modulus \(r>0\) whose directions modulo sign are \(\theta,\theta+\pi/n,\ldots,\theta+(n-1)\pi/n\). Their zonogon is a regular \(2n\)-gon with side length \(2r\), hence circumradius
\[
M=\frac{r}{\sin(\pi/(2n))}.
\]
Because \(L=nr\), this gives \(L/M=n\sin(\pi/(2n))\).

Finally suppose equality holds. Equality in the side-count step forces \(m=2n\), so no coefficient vanishes and no two generator directions coincide modulo sign. Equality in the polygon lemma forces \(Z\) to be a regular \(2n\)-gon. The two edges contributed by generator \(a_j\) have length \(2|a_j|\); regularity therefore forces all \(|a_j|\) to be equal, and its edge directions are equally spaced modulo \(\pi\). This is exactly the displayed extremizer form. The converse was already proved by the regular-zonogon construction.

## Verification
The proof is symbolic for every \(n\ge5\). The accompanying script `verify.py` independently enumerates all signs for the regular-zonogon extremizers for \(5\le n\le12\), checks the displayed sharp constant numerically to floating-point tolerance, and performs deterministic random stress tests of the universal inequality for \(5\le n\le9\). These finite checks are corroborative only; the all-dimensional theorem follows from the perimeter argument above.

## Relationship to prior work
Seigner proved that the Sidon constant of the infinite Rademacher system is \(\pi/2\), and his sharpness argument exhibits finite root-of-unity coefficient vectors before passing to the limit. The inspected proof establishes the universal \(\pi/2\) bound and then takes \(n\to\infty\); it does not state an exact value for every finite \(S_n\) or classify its equality cases. The present theorem supplies the finite sharp constant and rigidity. In particular,
\[
n\sin\!\left(\frac{\pi}{2n}\right)
=\frac{\pi}{2}-\frac{\pi^3}{48n^2}+O(n^{-4}),
\]
so it quantifies the approach to Seigner's limiting constant.

Bourgain and Lewko place Sidonicity and Rademacher-Sidonicity in the modern character-system framework and list MSC 43A46 as the first classification of their paper. Their work supplies the literature anchor and terminology but does not address this finite coordinate-character extremal problem. Cartwright, Howlett, and McMullen study extreme Sidon constants for finite subsets in a broader compact-group setting; only bibliographic and abstract-level material was inspected here, so older equivalent formulations remain a residual originality risk rather than being asserted absent.

## Limitations
The theorem concerns complex scalar coefficients and the coordinate Rademacher characters on \(E^n\). It does not claim an analogous formula for arbitrary Sidon subsets, vector-valued coefficients, or other norms. The computational checks cover only the stated finite test ranges and are not used as proof. A residual literature risk remains that the finite formula or its regular-zonogon equality classification appears in older work under planar vector-balancing or convex-polygon terminology.

## References
1. Jean Bourgain and Mark Lewko, *Sidonicity and variants of Kaczmarz's problem*, arXiv:1504.05290, first submitted 2015-04-21; 2010 MSC 43A46, 42C05.
2. J. A. Seigner, *Rademacher variables in connection with complex scalars*, Acta Math. Univ. Comenianae 66 (1997), 329--336.
3. D. I. Cartwright, R. B. Howlett, and J. R. McMullen, *Extreme values for the Sidon constant*, Proc. Amer. Math. Soc. 81 (1981), 531--537, DOI 10.1090/S0002-9939-1981-0601723-X.
