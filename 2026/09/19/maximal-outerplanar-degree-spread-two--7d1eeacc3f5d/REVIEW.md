# Review

## Correctness

**PASS.** The lower bound
\[
\operatorname{MOP}(n,2)\ge\left\lceil\frac{4n+10}{9}\right\rceil
\]
for maximal outerplanar graphs is Theorem 17 of Caro–Škrekovski–Zarb, arXiv:2609.19762v1, and holds for every \(n\ge5\). Their Theorem 20 supplies a maximal outerplanar graph \(H_k\) on \(18k+2\) vertices with degree counts \(n_2=8k,n_3=2,n_5=8k,n_6=2,n_8=2k-2\).

The new upper-bound construction is explicit. Inserting an ear on a boundary edge of a polygon triangulation preserves maximal outerplanarity and changes the two endpoint degrees by \(+1\) while adding one degree-two vertex. The seventeen nonzero residue templates in RESULT.md consist only of such insertions. Their local degree changes give the displayed window table; its maximum is exactly \(8k+\lceil(18+4r)/9\rceil=\lceil(4n+10)/9\rceil\) for \(n=18k+2+r\). No resulting degree exceeds 8, and every remaining three-degree window has size at most \(2k+2\), so no omitted window can dominate. This proves equality for every \(n\ge20\). Explicit triangulations settle \(14\le n\le19\).

For \(5\le n\le13\), the verifier performs an exhaustive polygon-triangulation recursion: the unique triangle incident to a fixed boundary edge determines a split into two smaller triangulated polygons. The enumeration sizes agree with the Catalan numbers \(C_{n-2}\), and direct evaluation of every degree sequence gives minima \(5,5,6,6,6,6,7,7,8\). Explicit witnesses are independently checked. Thus the finite computer-assisted part is exhaustive rather than heuristic.

The standalone verifier also reconstructs the published \(H_k\) chord construction and checks all residue templates for \(1\le k\le50\); these checks support, but do not replace, the general boundary-ear proof.

## Originality

**PASS, to the best of our knowledge, with a specific residual risk.** The current accessible main text of arXiv:2609.19762v1 was inspected. It proves the lower bound, proves equality only for \(n\equiv2\pmod{18}\), and gives the universal upper bound \(\lceil(4n+10)/9\rceil+43\). It also states that seventeen further caps were found and computer-verified over a covered range, and says that *presumably* \(\operatorname{MOP}(n,2)=\lceil(4n+10)/9\rceil\) for every \(n\ge14\). Thus the formula for \(n\ge14\) is explicitly anticipated by the source, but it is not proved there. The originality claim here is therefore the uniform proof for all residue classes and the complete exact determination for \(5\le n\le13\), not the conjectural formula or the idea of residue-dependent caps.

The supplementary material referred to in arXiv:2609.19762v1 was not inspected. It is the most plausible source capable of overlapping the residue constructions, because the paper says it contains seventeen caps and finite verification. The main paper explicitly characterizes the evidence as verification over a finite range and retains the all-order statement as a presumption. Nevertheless, if the supplementary material contains an unadvertised symbolic or uniform argument valid for every ladder length, the originality of the \(n\ge14\) proof would be weakened or lost. No originality is claimed for the mere existence of seventeen caps.

The accessible 2019 Caro–Lauri–Zarb paper was also inspected in the relevant maximal-outerplanar section. It proves the earlier lower bound \(4n/9\), gives a construction asymptotic to \(5n/11\), and explicitly asks for the correct order of magnitude of \(\operatorname{MOP}(n,2)\); it does not contain the exact formula here. Targeted searches for the exact notation, the \((4n+10)/9\) expression, degree spread, and maximal outerplanar graphs located no additional source stating the universal exact theorem.

## Value

**PASS.** The result removes the additive-constant gap left in the newest paper and proves its explicitly anticipated exact formula for every \(n\ge14\). It also completes the parameter for all \(n\ge5\), identifying exactly six small exceptional orders. The construction is reusable: a finite list of boundary-ear templates converts the source's single congruence-class extremal ladder into optimal graphs in every congruence class without changing the periodic core.

## Limitations

- The supplementary material associated with arXiv:2609.19762v1 was not inspected; it is the principal residual originality risk for the residue constructions.
- The orders \(5\le n\le13\) are settled by exhaustive computation over polygon triangulations, with a standalone verifier, rather than by a separate hand classification.
- The result concerns only spread parameter \(k=2\) for maximal outerplanar graphs; it does not address other graph classes or other spread widths.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
