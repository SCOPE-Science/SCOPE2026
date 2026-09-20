# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

For binary cube vertices, the identity
\[
(x-y)\cdot(z-y)=\#\{i:x_i=z_i\ne y_i\}
\]
shows that a right angle at \(y\) is exactly the Hamming-geodesic condition \(y\in I(x,z)\). The verifier implements this coordinate condition directly and first confirms that all \(\binom{24}{3}\) triples of the displayed Kamenetsky configuration are valid.

For each deletion number \(0\le r\le7\), every \(r\)-subset of the 24-point configuration is enumerated. After retaining \(T\), the candidate filter is exact for triples containing one new vertex and two retained vertices. Pair compatibility is exact for triples containing two new vertices and one retained vertex. The backtracking step then checks all triples among the selected new vertices. These three classes exhaust all triples in a proposed extension. Removed original vertices are not artificially forbidden from reappearing, so the nonexistence conclusion is valid for every 25-point set containing the retained subset, not merely for completions having a prescribed exact intersection.

The full run reports no completion after deleting \(r\le7\) vertices and requesting \(r+1\) additions. Therefore any 25-point general-position set has intersection at most 16 with the displayed 24-point set, equivalently at least 17 vertices in symmetric difference. Hypercube automorphisms preserve geodesic intervals, so the corollary for equivalent images follows immediately.

The explicit 24-word input was checked against the current OEIS attachment. The verification source and its complete output are included as compact artifacts.

## Originality

**PASS, to the best of our knowledge.**

The current OEIS A089676 entry records the 11-dimensional lower bound 24 and links the Kamenetsky witness used here. Korže--Vesel (2023) treat the equivalent hypercube general-position problem with SAT methods and report partial results beyond the dimensions where they establish exact values. Randriambololona (2013) treats the equivalent asymptotic \((2,1)\)-separating-system problem.

Searches covered the exact and synonymous formulations “cubic acute set”, “general position hypercube”, “(2,1)-separating system”, and “binary 2-frameproof code”, together with “exchange”, “local”, “maximal”, “overlap”, the parameter 11, and the known size 24. No matching statement was located for the edit-distance or seven-exchange isolation of this explicit configuration. Existing SCOPE records were also searched by the same mathematical objects and claim family, with no collision found.

Some frameproof-code literature is not fully open in the searched interfaces. In particular, the full text of Kathuria--Batra--Arora, *A Class of 2-FP Codes* (2017), was not inspected; its accessible abstract describes a parametric construction rather than the explicit length-11 configuration, so it is not presently strong evidence of coverage. This leaves a residual terminology/indexing risk, and the originality claim remains qualified rather than absolute.

## Value

**PASS.**

The best currently recorded 11-dimensional witness has 24 points, while the global optimum is not established by the sources checked. A natural route to 25 is therefore to perturb the known witness. The theorem excludes the complete neighborhood obtained by replacing at most seven of its points: a hypothetical 25-set must instead discard at least eight vertices and introduce at least nine new ones. This is a concrete structural obstruction that materially changes how a future computational search around the record construction must be organized.

The result is deliberately not presented as a new lower or upper bound. Its value is the exact local rigidity information around the strongest current explicit witness.

## Limitations

- No global upper bound for \(gp(Q_{11})\) is obtained.
- A structurally distant 25-point configuration is not excluded.
- The certified exchange radius stops at seven deletions.
- The certificate is computational, not proof-assistant formalized.
- Residual originality risk remains from differently indexed frameproof/separating-code literature.
- Independent audit has not been performed.
