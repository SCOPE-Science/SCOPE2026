# Review of gain-uniform two-leader placement on clique windmills

## Correctness (PASS)

The claim explicitly fixes \(r,m\ge2\), identical positive finite feedback gains \(\kappa\), two distinct leaders, and the trace-of-inverse objective. The connected windmill Laplacian has the three mutually orthogonal nonconstant eigenspaces described in RESULT.md with eigenvalues \(1\), \(m+1\), and \(rm+1\). A constant-mode Schur complement plus the rank-one inverse identity provides an exact expression for the trace with two pinned vertices; projector evaluation produces all three candidate values. The difference \(J_B-J_A\) is strictly positive. The second difference has a polynomial numerator negative for \(r=2\) and strictly positive for \(r\ge3\), including the potentially delicate \((r,m)=(3,2)\) case, where it becomes \(4\kappa^2-3\kappa+9>0\). The accompanying `verify.py` independently passed 1,566 exact-rational checks, including full pair enumeration on smaller graphs. The infinite theorem relies on the proof, not the finite checks.

## Originality (PASS, residual risk noted)

The 2013 finite-gain leader paper of Lin--Fardad--Jovanović gives the objective and general algorithms but no inspected windmill placement theorem. Fitch--Leonard's 2014/2015 joint-centrality work gives a general two-leader formula and explicit solutions for cycles and paths but does not state the windmill branch transition. Thus the exact gain-independent switch at three clique blades requires an additional nontrivial comparison, established here by a strict parameter-polynomial analysis. Related indexed windmill and clique-sum results concern different invariants. Sun--Li--Liu (2020), *Noisy consensus dynamics in windmill-type graphs*, is an important closely related source: its publicly available abstract states exact leader-follower coherence results on windmill networks, but full-text comparison was not possible. A theorem there on the exact same **finite positive gain**, equal-gain two-leader objective could supersede the present claim. This is a concrete residual originality risk, not a statement that the source was fully checked or found noncovering.

## Value (PASS)

The precise two-leader placement problem is a natural combinatorial control-design question, and locating optimal sensor/leader positions on hub-and-community networks matters independently of the numerical objective value. The classification is not a renaming of an existing invariant: it shows that the maximum-degree hub is *never* included when there are exactly two blades, while it is *always* included once there are at least three, for arbitrary clique size and all positive gains. It proves strict uniqueness up to automorphisms and closed performance formulas on a two-parameter infinite graph family. No extension to unequal gains, altered edge weights, or other leader counts is claimed.

## Closest literature and scientific limitations

Primary sources read: Lin--Fardad--Jovanović, arXiv:1302.0450 (2013), especially problem statement and selection methods; Fitch--Leonard, arXiv:1407.1569 (2014), model, two-noisy-leader formulas, and explicit path/cycle results. A later highly relevant windmill coherence article, Sun--Li--Liu, Chaos 30 (2020), 123131, was accessible only by abstract; its unavailable full text is a substantial residual risk. The theorem concerns exactly two equal finite-gain leaders and unit graph edges. Verification is same-model only.

Self-review: passed. Independent audit: not yet performed.
