# Scientific review: Arithmetic line spectrum of the octahedral sextic surface

## Correctness — PASS

The claim concerns the explicitly defined sextic \(f(x,y)+f(z,w)=0\), \(f=xy(x^4-y^4)\), in characteristic zero and primes at least five. Boissière--Sarti Proposition 4.1 classifies all lines on separated-variable smooth surfaces into joins and graphs. The exact included verifier exhausts \(6\cdot5\cdot4=120\) possible image triples of the six branch roots, proves exactly \(24\) normalized octahedral graph transformations, checks their degree-six identities, and gives a prime-support certificate \(\{2,5\}\) for all \(96\) excluded candidates. This excludes additional graph families for every \(p\ge7\). The scalar sixth-root parametrization identifies \(\mathbb Q(\zeta_{24})\) as both sufficient and necessary. The eight Frobenius counts follow from explicit congruences, not extrapolated finite data. The characteristic-five argument uses the exactly \(120\)-element projective group of the six \(\mathbb F_5\)-rational branch points, together with determinant square classes, to prove \(756\) geometric and \(156\) rational lines. Small-prime computations are checks, not substitutes for the all-prime argument.

Residual correctness risk: the cited general separated-variable line lemma is a mathematical input; its proof is sketched and specialized in the main result, but an independent formal proof has not been performed. No result is asserted at characteristic two or three.

## Originality — PASS, with residual bibliographic risk

The 180-line total is *not* original: Boissière--Sarti explicitly prove it. The 6912-element complex automorphism group and uniqueness are *not* original: Esser--Li and Yang--Yu--Zhu establish them. The arithmetic claims are different: the minimal common cyclotomic line field, precisely 20 rational lines, eight exact residue classes of rational-line counts for every prime at least seven, and the explicit arithmetic transition at characteristic five. Primary full-text sections on the same surface and exact geometric line parameterizations have been examined. The cited sources provide the needed broad parametrization but neither state nor immediately calculate the minimal field and Frobenius table. Focused mathematical record, alias, field-of-definition and prime-reduction searches supplied no matching result. An unindexed arithmetic calculation of this already classical surface remains possible, so this self-review is not a priority claim or independent originality certification.

## Value — PASS

The sextic is singled out both by its extremal 180 geometric lines and its maximal complex projective automorphism group. Its rational and finite-field line configurations are natural arithmetic invariants, not selected arbitrary numerical tests. Complete field-of-definition and Frobenius information makes the distinction between 180 geometric lines, 20 rational lines and exceptional arithmetic behavior explicit, and describes the entire good-prime distribution. Such information is not supplied by the geometric line total alone and provides a reusable exact reduction profile for this notable surface.

## Relationship and limitations

Sources: Boissière--Sarti, *Counting lines on surfaces*, Proposition 4.1 and §4.4 (2007); Esser--Li, *Hypersurfaces with large automorphism groups*, Example 2.9 (arXiv:2405.11666); Yang--Yu--Zhu, *On automorphism groups of smooth hypersurfaces*, Theorem 1.1 (arXiv:2405.09505). The results concern individual lines, not rational points on the surface or its Picard group, and exclude characteristic two and three. The characteristic-five geometric total is classical. Exact certificates and their limits are set out in `VERIFICATION.md`.

Self-review: passed. Independent audit: not yet performed.
