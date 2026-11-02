# Scientific review: denominator-mod-four resonance for alternating islands

## Correctness — PASS

The theorem has fixed exact assumptions: even reduced denominator \(q\ge4\), coprime \(p\) strictly below \(q/2\), the specified half-plane tie convention, and the **strictly alternating** regular-set components only. The two-cycle equation is explicitly solved. A branchwise induction proves necessary and sufficient half-plane constraints at every iterate; no sampling assumption enters that characterization. The supporting normals form two cyclic cosets whose equality versus disjointness is decided exactly by the parity of \(q/2\). Their common distance to the center proves regularity and inradius, whence the exact area. The point-period assertion follows from the order of \(\lambda^2\) and disjointness of the two cells. Strict signs establish a neighborhood separated from all critical-line preimages. The independent finite sample checker does not substitute for these universal arguments.

## Originality — PASS within inspected evidence

The originating work [1] proves that each rational regular-set component is a polygon with at most \(q\) sides for even \(q\), and derives a regular \(q\)-gon case only when its component period \(\ell\) is coprime to \(q\). Here \(\ell=2\), so that hypothesis fails for every even \(q\); the new formula gives **\(q/2\) rather than \(q\) sides** when \(q\equiv2\pmod4\). Goetz and Quas [2, Lemma 11] impose precisely the same coprimality restriction, so their general shape theorem likewise does not imply this statement. The low-angle square and triangle examples are already available in [3] and are expressly not claimed as new. The newly classified infinite family includes the \(q=10\) regular-pentagon case, all higher \(q\equiv2\pmod4\) cases, and exact area formulas. Searches for the explicit parity classification, for equivalent two-cycle polygon geometry, and for published or indexed dominating results did not reveal stronger coverage. A literature search cannot establish absolute priority, and equivalent unindexed geometric or recurrence formulations remain a real risk.

## Mathematical value — PASS

The number of sides is an intrinsic geometric invariant of the periodic component, and its exact dependence on \(q\bmod4\) resolves a specific natural gap in the published coprime-period shape theorems. The result provides a motivated infinite classification rather than a chosen numerical example. The side-count halving is a genuine resonance that appears **because** the orbit period shares a factor with the rotation denominator. The exact island area and period profile allow quantitative comparisons among rational parameters and give explicit test cases for the general geometry. No global classification, measure-theoretic density theorem, or new theorem for the already classified square/triangle examples is claimed.

## Closest sources and limits

[1] Cima, Gasull, Mañosa, Mañosas, *On some rational piecewise linear rotations*, arXiv:2306.17543; author postprint of DOI:10.1080/10236198.2023.2260898, Theorems A and B and Sections 2–4. The boundedness, periodicity and general polygon geometry are their results.

[2] Goetz and Quas, *Global properties of a family of piecewise isometries*, DOI:10.1017/S0143385708080280, especially Lemma 11 and its explicit condition \(\gcd(\ell,q)=1\).

[3] Cima, Gasull, Mañosa, Mañosas, *Pointwise periodic maps with quantized first integrals*, arXiv:2010.12901, for the specific rational angles and classical regular tiles.

Limitations: the proof addresses only the two strictly alternating components, not all periodic islands, odd denominators, or boundary dynamics. Publication-priority risk persists for unindexed sources or dual-billiards descriptions. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
