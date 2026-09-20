# Review

## Scientific assessment

The proposed finding gives an explicit four-color interval construction with asymptotic rainbow-Schur density \(553/1000\), improving the \(k=4\) specialization \(10/21\) of the general lower bound in Hegde--Kumar--Pratibha.

### Correctness: PASS

The construction and proof were checked against the following points.

- The normalization agrees with the primary source: ordered pairs \((x,y)\) with \(x+y\le n\) are counted, and the total number of ordered Schur pairs is \(\binom n2\).
- The rectangle-under-a-diagonal formula
  \[
  \Phi_t([a,b),[c,d))
  =
  \frac12[(t-a-c)_+^2-(t-b-c)_+^2-(t-a-d)_+^2+(t-b-d)_+^2]
  \]
  follows by inclusion-exclusion and exactly measures the required area.
- Summing over interval triples whose three assigned colors are distinct gives \(2A=553/1000\) in exact integer arithmetic. The ten scaled contributions are \(0,0,280,648,648,220,1086,922,1272,454\), which sum to \(5530\).
- The passage from area to finite colorings is a standard Riemann-sum argument. The only discontinuities lie on finitely many vertical, horizontal, and diagonal lines, so boundary conventions contribute only \(o(n^2)\).
- Independent finite enumeration of the stated coloring gives normalized densities \(0.5584924623\) at \(n=200\), \(0.5552384770\) at \(n=500\), \(0.5541261261\) at \(n=1000\), and \(0.5535647824\) at \(n=2000\), consistent with convergence to \(0.553\).
- The source lower bound at \(k=4\) is \((k-2)(k+1)/((k-1)(k+3))=10/21\); the claimed improvement is therefore exact.

The computational checks are not used in place of the proof.

### Originality: PASS, to the best of our knowledge

The current full text of Hegde--Kumar--Pratibha, arXiv:2609.18474v1, was inspected. It states that its general bounds are, to the best of the authors' knowledge, the first nontrivial bounds for \(k\ge4\), gives \(10/21\) as the \(k=4\) lower bound by specialization, says the general bounds are likely not optimal, and explicitly identifies the \(k=4\) case as worth further investigation. It does not state the present interval construction or a four-color lower bound of \(553/1000\).

Parczyk--Spiegel's earlier multiplicity paper treats the three-color problem. Older rainbow-Schur literature located in the search primarily concerns existence/rainbow-number questions rather than maximizing the asymptotic fraction of rainbow Schur triples.

Searches using four-color/4-color rainbow Schur triples, anti-Ramsey Schur multiplicity, maximum rainbow-Schur fraction, \(k=4\), \(553/1000\), \(0.553\), and the construction's breakpoint data did not identify prior coverage or a stronger four-color lower bound.

No inaccessible paper was identified whose title or available metadata specifically suggests the same four-color multiplicity bound. The principal residual risk is instead the recency of arXiv:2609.18474v1: contemporaneous work may not yet be indexed.

### Value: PASS

The improvement is substantial rather than a rounding change:
\[
\frac{553}{1000}-\frac{10}{21}
=
\frac{1613}{21000}
\approx0.07681.
\]
It addresses exactly the \(k=4\) case singled out by the recent primary source and supplies a deterministic, elementary construction whose limiting density is certified by a compact exact calculation.

## Limitations

The result does not determine the optimum, improve the \(3/4\) upper bound, prove existence of \(\lim_n\Lambda_{n,4}\), establish uniqueness or local optimality of the interval pattern, or improve the known lower bounds for \(k\ge5\). The originality assessment is to the best of our knowledge and retains the possibility of unindexed contemporaneous work.

Same-model review: passed. Independent audit: not yet performed.
