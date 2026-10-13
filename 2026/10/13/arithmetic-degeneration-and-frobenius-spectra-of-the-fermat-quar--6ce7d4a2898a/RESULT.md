# Arithmetic degeneration and Frobenius spectra of the Fermat quartic bitangents

## Finding
Let \(C\) be the smooth Fermat plane quartic \(X^4+Y^4+Z^4=0\) over \(\mathbb Q\). For every odd prime \(p\), write \(\mathcal B_p\) for the reduced union of its \(28\) geometric bitangent lines after reduction modulo \(p\). These lines are taken over \(\overline{\mathbb F}_p\), even when individual lines are not defined over \(\mathbb F_p\). For \(j\ge2\), let \(t_j(p)\) be the number of geometric intersections lying on exactly \(j\) of these lines, and let \(r_j(p)\) count those same points that belong to \(\mathbb P^2(\mathbb F_p)\).

The **complete geometric incidence spectrum** at all odd primes is:

| Prime condition | \(t_2(p)\) | \(t_3(p)\) | \(t_4(p)\) | All geometric intersection points |
|---|---:|---:|---:|---:|
| \(p\notin\{2,3,5,17\}\) | 288 | 0 | 15 | 303 |
| \(p=3\) | 0 | 0 | 63 | 63 |
| \(p=5\) | 240 | 16 | 15 | 271 |
| \(p=17\) | 144 | 48 | 15 | 207 |

All \(28\) lines remain distinct, and there are no points of multiplicity above \(4\). Thus **the odd exceptional primes are exactly \(3,5,17\)**.

The **complete rational intersection spectrum** is:

| Prime condition | \(r_2(p)\) | \(r_3(p)\) | \(r_4(p)\) | Rational intersection points |
|---|---:|---:|---:|---:|
| \(p\notin\{2,3,5,17\}\), \(p\equiv1\pmod8\) | 288 | 0 | 15 | 303 |
| \(p\notin\{2,3,5,17\}\), \(p\equiv5\pmod8\) | 48 | 0 | 15 | 63 |
| \(p\notin\{2,3,5,17\}\), \(p\equiv3,7\pmod8\) | 0 | 0 | 9 | 9 |
| \(p=3\) | 0 | 0 | 9 | 9 |
| \(p=5\) | 0 | 16 | 15 | 31 |
| \(p=17\) | 144 | 48 | 15 | 207 |

In particular, **every one of the \(31\) points of \(\mathbb P^2(\mathbb F_5)\) is a triple or quadruple intersection of the geometric bitangents**. The natural prime densities for \(303\), \(63\), and \(9\) rational intersection points are respectively \(1/4\), \(1/4\), and \(1/2\), since the three exceptional primes do not affect densities.

## Assumptions and scope
The base is the explicit rational Fermat plane quartic, not the Fermat quartic **surface** in \(\mathbb P^3\). Its reduction is smooth for odd \(p\) since the three partial derivatives cannot vanish simultaneously at a projective point when \(4\ne0\). A geometric bitangent is a line whose intersection divisor with this quartic has even multiplicity at every contact point. The \(28\) lines are counted individually over the algebraic closure, and a rational intersection point is counted irrespective of whether its incident lines are individually rational. All singularities of a reduced union of distinct projective lines occur at their transverse intersections, so point multiplicities determine the ordinary singularity types.

## Proof
**1. Exact bitangent list.** In any algebraically closed field of odd characteristic, put \(\mu_4=\{r:r^4=1\}\). There are \(16\) lines
\[
L_{r,s}: Z-rX-sY=0,\qquad (r,s)\in\mu_4^2,
\]
and \(12\) additional lines
\[
X-aY=0,\qquad Y-aZ=0,\qquad Z-aX=0,\qquad a^4=-1.
\]
The restriction of the quartic equation to \(L_{r,s}\) is \(2(r^2X^2+rsXY+s^2Y^2)^2\). On the other three types of lines it restricts to a fourth power, up to scaling. Therefore all the listed lines are bitangents, and they are distinct in odd characteristic: the eight roots of unity are separable, the first \(16\) lines have three nonzero coefficients, and each of the last \(12\) has exactly one zero coefficient. A smooth plane quartic over an algebraically closed field of characteristic different from \(2\) has exactly \(28\) bitangents, counted through its odd theta characteristics. Thus the list is exhaustive, including characteristic \(3\).

**2. An exact integral discriminant of triple concurrence.** Put \(\zeta=\zeta_8\), \(\zeta^4=-1\), \(R=\mathbb Z[\zeta]\), and write every line above by a coefficient triple in \(R^3\), with \(\mu_4=\{\zeta^0,\zeta^2,\zeta^4,\zeta^6\}\) and \(a\in\{\zeta,\zeta^3,\zeta^5,\zeta^7\}\). For the \(\binom{28}{3}=3276\) triples of lines, compute the coefficient determinant \(\Delta\in R\). Exactly \(60\) determinants vanish identically, namely the four choices of three lines through each of \(15\) quadruple points. For the other \(3216\) determinants, the absolute algebraic norms \(|N_{\mathbb Q(\zeta)/\mathbb Q}(\Delta)|\) have the exhaustive distribution:

| Norm | 1 | 2 | 4 | 8 | 9 | 16 | 17 | 32 | 36 | 64 | 256 | 400 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 384 | 64 | 864 | 384 | 192 | 560 | 192 | 96 | 192 | 192 | 64 | 32 |

All norms are products of primes in \(\{2,3,5,17\}\). For odd \(p\) outside \(\{3,5,17\}\), no previously nonzero determinant can vanish under reduction modulo a prime of \(R\) above \(p\), and distinct lines remain distinct. Consequently **no new three-line concurrence occurs**. Since every change in the multiplicity partition of line intersections would create a new triple concurrence, the characteristic-zero distribution \((288,0,15)\) remains valid at every such prime. Its pair-count check is \(288\binom22+15\binom42=378=\binom{28}{2}\).

**3. Exact exceptional reductions.** Work in \(\mathbb F_{p^2}\), which contains all eighth roots of unity for the three exceptional primes and indeed for every odd \(p\). Enumerate all \(378\) pairs of distinct lines; take the cross product of their coefficient triples; normalize each nonzero point projectively; group equal points and count their incident lines. This finite exhaustive computation gives at \(p=3\), \((t_2,t_3,t_4)=(0,0,63)\); at \(p=5\), \((240,16,15)\); and at \(p=17\), \((144,48,15)\). The respective pair-count identities are \(63\binom42=378\), \(240+16\binom32+15\binom42=378\), and \(144+48\binom32+15\binom42=378\). The code does not infer these infinite-prime statements from samples: the norm argument proves generic stability, while the three exceptional field computations are exhaustive finite certificates.

At \(p=5\), the \(16\) lines \(Z-rX-sY=0\) are defined over \(\mathbb F_5\), since \(\mu_4=\mathbb F_5^\times\). Every point \([X:Y:Z]\) with all coordinates nonzero lies on **exactly three** of these \(16\) lines: after scaling \(Z=1\), each choice of \(r\in\mathbb F_5^\times\) determines \(s=(1-rX)/Y\), with precisely one choice making \(s=0\). There are exactly \(16\) such points. All other \(15\) rational projective points have at least one zero coordinate and are the \(15\) quadruple points (for the three coordinate vertices the four incident lines come from the \(a^4=-1\) family; for the other twelve points they come from the \(16\) rational lines). Since the complete \(\mathbb F_{25}\) calculation found exactly \(16\) geometric triple points and \(15\) geometric quadruple points, these exhaust the rational points, and all \(240\) double intersections are non-rational. Notice that \(C(\mathbb F_5)=\varnothing\), because every nonzero fourth power in \(\mathbb F_5\) equals \(1\) and a sum of one, two, or three such ones is never zero.

**4. Frobenius for every generic prime.** Every characteristic-zero intersection is the cross product of a pair of coefficient triples in \(\mathbb Q(\zeta_8)^3\), hence defined over \(\mathbb Q(\zeta_8)\). When \(p\notin\{2,3,5,17\}\), the determinant calculation assures no collision between distinct point classes, so the geometric Frobenius action is the reduction of the cyclotomic Galois automorphism \(\zeta_8\mapsto\zeta_8^p\). Exact permutation of the line pairs yields the following numbers of fixed geometric points, subdivided by their multiplicity:

| Exponent \(p\bmod8\) | Fixed double points | Fixed quadruple points |
|---|---:|---:|
| 1 | 288 | 15 |
| 3 | 0 | 9 |
| 5 | 48 | 15 |
| 7 | 0 | 9 |

This proves the generic rationality table. At each of the three exceptional primes, the same projective-point enumeration in \(\mathbb F_{p^2}\), followed by the field-Frobenius fixed-point test, produces \((r_2,r_3,r_4)=(0,0,9)\), \((0,16,15)\), and \((144,48,15)\), respectively. Dirichlet's theorem on primes in each of the four reduced residue classes modulo \(8\) yields the stated densities.

## Verification
Run the accompanying standard-library-only script with \(\texttt{python3 verify.py}\). It constructs \(\mathbb Z[\zeta_8]\) as \(\mathbb Z[T]/(T^4+1)\), verifies all \(3276\) exact determinants and the displayed norm histogram, constructs the \(378\) generic pair-intersection classes, and computes the four cyclotomic fixed-point spectra. Separately it performs exact projective incidence and Frobenius computations in \(\mathbb F_{p^2}\) for \(p=3,5,7,11,13,17,19,23,29,31,41\). The generic assertion for all remaining primes follows from the integral norm argument in the proof, not from the finite list of test primes. Successful execution prints \(\texttt{VERIFY\_OK}\).

## Relationship to prior work
Janasz–Pokora–Zieliński [1, Proposition 3.2 and Tables 5–7] give the \(28\) lines and the complex geometric distribution \(288\) double and \(15\) quadruple points. Knecht–Reyes [2, Theorem 4.1] give the \(\mathbb F_9\) Fermat curve with \(28\) hyperflexes and \(9\) quadruple intersections on each line; their Theorem 4.5 lists the bitangent intersection profiles at \(p=17\). Thus the \(p=3\) and \(p=17\) individual spectra are **previously implied**, and are used here as external cross-checks, not offered as discoveries. Bethea–Brazelton [3, Section 4.2] study complex automorphism orbits on the same \(28\) bitangents. The novel claim is the exhaustive **odd-prime exceptional-prime classification**, the full **rational-point Frobenius spectrum across all primes**, and particularly the **characteristic-five decomposition of every rational projective point into triple or quadruple intersections**. The general line-definition field itself is not claimed to be new.

## Limitations
Characteristic \(2\) is excluded because the quartic reduction is not smooth and the \(28\)-bitangent description no longer applies. The result counts intersections of the geometric line arrangement, not quartic rational points, tangency contact points, freeness, or lines on a quartic surface. The proof and verifier give an exact finite arithmetic certificate for the asserted family; they do not purport to establish that no unpublished or unindexed earlier calculation exists. The characteristic-three and characteristic-seventeen individual intersection counts are explicitly acknowledged as pre-existing consequences of [2]. No independent mathematical audit has been performed.

## References
[1] M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, originally publicly posted 2023-08-31; Proposition 3.2, Section 3.2, Tables 5–7. https://arxiv.org/abs/2308.16514

[2] A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv:1510.04621 (2015), especially Theorems 4.1 and 4.5. https://arxiv.org/abs/1510.04621

[3] C. Bethea and T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242 (2024), Section 4.2. https://arxiv.org/abs/2410.09242
