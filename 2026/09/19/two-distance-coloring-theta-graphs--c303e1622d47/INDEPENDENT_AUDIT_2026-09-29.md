# Independent audit — Exact two-distance chromatic number of three-path theta graphs

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/two-distance-coloring-theta-graphs--c303e1622d47`  
**Audited tree:** `977996a2498531cdaf988e1bc51610ff303190af`

## Disposition

**PASSED.**

## Correctness

**PASS.** The classification is correct. Independently iterating the 12-state four-color path transfer from state 01 gives reachable-state counts 2,4,7,10,11,12 for lengths 2 through 7, exactly matching the transfer table and saturation claim. A separate exact graph-square coloring computation over the tested theta instances reproduces the stated 4/5/6 trichotomy; the repository's deterministic verifier checks all 210 triples 1≤a≤b≤c≤10 (b≥2), finding 189 four-color, 20 five-color, and one six-color case, with Θ(2,2,3)^2=K6. The endpoint compatibility arguments in the proof align with those finite-state constraints and extend the classification to the infinite families.

## Originality

**PASS.** PASS for the complete three-path classification and transfer proof, but not for the general K4-minor-free upper bound or isolated sharpness examples. Lih–Wang–Zhu (2003) proves the general χ(G²)≤Δ+3 bound for subcubic K4-minor-free graphs and gives sharp examples; Hetherington–Woodall (2008) proves the corresponding list-coloring bounds. Their abstracts do not state an exact path-length classification for theta graphs, and targeted searches under theta/generalized-theta, graph-square, and two-distance terminology did not locate one. Lawful open-access full text for both older papers was unavailable; Oxford institutional retrieval was attempted after OA/arXiv checks but both jobs stopped at publisher human verification, so those papers were not claimed as read. This leaves a documented residual overlap risk, especially for an isolated sharp example, but it is not decisive for the record's complete infinite classification.

## Scientific value

**PASS.** Three-path theta graphs are the first basic 2-connected non-cactus series-parallel blocks. An exact classification showing infinite five-color obstruction families and the unique six-color triple gives a useful structural benchmark beyond general upper bounds, and the small transfer automaton is reusable for related series-parallel square-coloring problems.

## Independent checks

- Recomputed the four-color transfer relation from the path-square constraint; all 12 ordered unequal states are reached from length seven onward.
- Confirmed Θ(2,2,3)^2 is K6.
- Compared an exact square-coloring enumeration through path lengths ten with the theorem; all 210 repository-verified instances agree.
- Checked the abstracts and bibliographic records of the two main older K4-minor-free square-coloring papers.
- Attempted authorized Oxford retrieval of both older full texts after OA/arXiv failure; both required human publisher verification and therefore were not read.

## Evidence and literature

- https://doi.org/10.1016/S0012-365X(03)00059-1 — Lih–Wang–Zhu (2003), general K4-minor-free square-coloring bounds and sharpness examples; abstract inspected, full text inaccessible in this run.
- https://doi.org/10.1016/j.disc.2007.07.102 — Hetherington–Woodall (2008), list-coloring analogue and sharp general bounds; abstract inspected, full text inaccessible in this run.
- https://doi.org/10.1016/j.disc.2009.07.004 — Kostochka–Özkahya–Woodall (2009), later Brooks-type refinement; contextual evidence that the older results are general K4-minor-free bounds rather than a theta path-length classification.

## Limitations

- Ordinary two-distance chromatic number only; list two-distance coloring is not classified.
- Exactly three internally disjoint paths are treated, not generalized theta graphs with more branches.
- The full texts of Lih–Wang–Zhu (2003) and Hetherington–Woodall (2008) could not be accessed without human publisher verification; hidden special-case overlap remains a residual originality risk.

## Repository identity

The assigned source-tree SHA `977996a2498531cdaf988e1bc51610ff303190af` exactly matched the current tree at the audited path on `main`; GitHub was read only during this audit.
