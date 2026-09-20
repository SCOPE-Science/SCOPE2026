# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The upper bound separates the universal-vertex case
\(\gamma=1\) from \(\gamma\ge2\). For \(\gamma\ge2\), the proof uses the
order bound \(\gamma_{t2}\le n/2\) and supplies a direct auxiliary-graph
proof of \(\gamma_{t2}\le2\gamma-1\). Their intersection gives
\[
\gamma_{t2}-\gamma\le\left\lfloor\frac{n-2}{4}\right\rfloor.
\]
The construction \(B_{d,s}\) has order \(4d+s+2\), domination number
\(d+1\), and semitotal domination number \(2d+1\). The lower bound on the
latter is arm-local: every length-four arm contributes at least two
selected vertices to any semitotal dominating set, while a direct leaf of
the center forces one additional selected vertex outside the arm
interiors.

A standalone exhaustive verifier agrees with the theorem on every
connected Graph Atlas graph through order seven and every nonisomorphic
tree through order ten, and checks the explicit extremal family through
order twenty.

## Originality

**PASS, to the best of our knowledge.** The foundational 2014 paper was
checked for the order bound and domination comparisons. The 2018 tree
paper, the 2024 paper comparing semitotal and ordinary/total domination in
trees, and the 2025 characterization of graphs with
\(\gamma_{t2}=n/2\) were also checked. Exact and synonymous searches for a
fixed-order maximum of \(\gamma_{t2}-\gamma\), maximum differences between
semitotal and ordinary domination, and equivalent tree formulations did
not locate the stated formula or the explicit all-order extremal family.

The originality risk is nonzero because the upper bound is a short
optimization of known inequalities. A differently indexed domination
paper may have stated the same fixed-order corollary without using
"difference" or "gap" terminology. No such statement was found in the
checked sources.

## Value

**PASS.** The result converts two established one-parameter bounds into an
exact two-parameter extremal comparison at fixed order and supplies a
sharp tree construction for every order. It also shows that allowing
cycles or denser connected graphs cannot enlarge the extremal gap.

## Scientific limitations

- No characterization of all extremal connected graphs or all extremal
  trees is given.
- The theorem is specific to finite simple connected graphs.
- The proof of the upper bound is short and relies on the established
  half-order bound for semitotal domination; the contribution is the exact
  fixed-order optimization and sharpness construction rather than a new
  standalone half-order estimate.
- Originality remains subject to unindexed or differently phrased
  semitotal-domination literature.

## Sources checked

- W. Goddard, M. A. Henning, C. A. McPillan, *Semitotal Domination in
  Graphs*, Utilitas Mathematica 94 (2014), 67--81.
- Z. Wei, G. Hao, *Semitotal domination in trees*, DMTCS 20(2) (2018).
- W. Zhuang, *Semitotal domination versus domination and total domination
  in trees*, RAIRO Operations Research 58 (2024), 1249--1256.
- Q. Chen, Y. Xu, *Graphs with semitotal domination number half their
  order*, Bulletin of the Australian Mathematical Society 111 (2025),
  197--204.
