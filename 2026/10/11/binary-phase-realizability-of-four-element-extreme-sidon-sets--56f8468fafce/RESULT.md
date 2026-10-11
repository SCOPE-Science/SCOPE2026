# Binary-phase realizability of four-element extreme Sidon sets
## Finding
Let \(G\) be a discrete abelian group and let \(E\subset G\) be a four-element extreme Sidon set. Call \(E\) binary-phase realizable when there is a measure \(\mu=\sum_{x\in E}\varepsilon_x\delta_x\), with every \(\varepsilon_x\in\{+1,-1\}\), such that \(\mu*\widetilde\mu=4\delta_0\). Under the Graham--Ramsey classification of four-element extreme sets, binary-phase realizability occurs exactly for the rectangle family \(E=\{0,x,y,x+y\}\) with \(2x=0\) (which includes the four-element subgroup case) and for the \(\mathbb Z_7\) prototype \(\{0,1,2,4\}\). It fails for the \(\mathbb Z_5\) prototype \(\{0,1,2,3\}\) and for the exceptional \(\mathbb Z_4\times\mathbb Z_2\) prototype \(\{(0,0),(1,0),(3,1),(0,1)\}\). Hence, up to the support operations in that classification, these are precisely the four-point Sidon-extreme geometries that admit an extremal measure with a common phase times real signs.

## Assumptions and scope
An extreme measure on a finite support \(E\) is normalized here by the standard equality condition \(\mu*\widetilde\mu=|E|\delta_0\), equivalently constant Fourier modulus \(\sqrt{|E|}\) when all point masses have modulus one. The new assertion concerns the additional restriction that, after multiplication by one common unimodular scalar, all four masses lie in \(\{+1,-1\}\).

The support classification used in the proof is Graham and Ramsey's Proposition 3.2: every four-element extreme set reduces, under their support operations, to the four-element subgroup, the \(\mathbb Z_5\) prototype \(\{0,1,2,3\}\), the \(\mathbb Z_7\) prototype \(\{0,1,2,4\}\), a rectangle \(\{0,x,y,x+y\}\) with \(2x=0\), or the exceptional \(\mathbb Z_4\times\mathbb Z_2\) prototype. The subgroup case is itself a rectangle, by taking the order-two element as \(x\).

## Proof
For a rectangle \(E=\{0,x,y,x+y\}\) with \(2x=0\), take
\[
\mu=\delta_0+\delta_x+\delta_y-\delta_{x+y}.
\]
For every character \(\chi\), the value \(\chi(x)\) is \(1\) or \(-1\), and
\[
\widehat\mu(\chi)=1+\chi(x)+\chi(y)-\chi(x)\chi(y).
\]
If \(\chi(x)=1\), this equals \(2\); if \(\chi(x)=-1\), it equals \(2\chi(y)\). Thus \( |\widehat\mu(\chi)|=2\) identically, proving binary-phase realizability.

For \(E=\{0,1,2,4\}\subset\mathbb Z_7\), take signs \((1,-1,-1,-1)\). Its cyclic autocorrelation at the six nonzero differences cancels in pairs. For example, the positive differences \(1,2,3\) have contributions \((-1)+1\), \((-1)+1\), and \((-1)+1\), respectively; the remaining three are their conjugate/reversed counterparts. Hence \(\mu*\widetilde\mu=4\delta_0\).

For \(E=\{0,1,2,3\}\subset\mathbb Z_5\), every nonzero difference has exactly three ordered representations by pairs from \(E\). With binary coefficients, the corresponding autocorrelation coefficient is therefore a sum of three numbers from \(\{+1,-1\}\), which can never vanish. No binary-phase extremal measure exists.

For the exceptional support \(F=\{(0,0),(1,0),(3,1),(0,1)\}\subset\mathbb Z_4\times\mathbb Z_2\), consider \(h=(0,1)\). Exactly two ordered pairs in \(F^2\) have difference \(h\), namely \(((0,1),(0,0))\) and \(((0,0),(0,1))\). For real signs their autocorrelation contribution is
\[
2\varepsilon_{(0,0)}\varepsilon_{(0,1)}\in\{-2,2\},
\]
so it cannot vanish. Thus this prototype is not binary-phase realizable.

The defining autocorrelation identity is invariant under translation and group automorphisms, and it is unchanged when the same support and measure are regarded inside an ambient abelian group through the support operations used in the classification. Graham--Ramsey's exhaustive four-point classification therefore yields the stated if-and-only-if result.

## Verification
The accompanying `verify.py` independently checks the two finite prototype assertions by exact integer autocorrelation over all \(2^4\) sign patterns, verifies the displayed \(\mathbb Z_7\) witness exactly, and tests the rectangle formula on \(1560\) cyclic rectangle instances. Its replay output is:

`VERIFY_OK rectangle_cases=1560 z7=1 z5_binary_solutions=0 exceptional_binary_solutions=0 max_rectangle_err=7.994e-14`

The finite checks are corroborative. The universal rectangle statement and the exhaustive reduction to prototype families are proved symbolically above; the latter uses the published support classification.

## Relationship to prior work
Graham and Ramsey classify the supports of all four-element extreme Sidon sets and explicitly include the five prototype forms used here. Their paper also establishes the unit-mass/flat-transform criterion for extremal measures. It does not state which four-element support families admit a \(\{+1,-1\}\)-valued extremal measure.

Graham's later survey gives explicit measures for several of these supports. In particular, it records the real-sign witness \(\delta_0-\delta_1-\delta_2-\delta_4\) for the \(\mathbb Z_7\) prototype, while its treatment of the \(\mathbb Z_5\) and exceptional examples uses nonreal phases. It also poses a different question about extreme measures with real Fourier transforms. The present statement is instead a complete classification of supports admitting real binary point-mass phases.

The later survey supplies an explicit nonreal witness for the \(\mathbb Z_5\) prototype but does not classify binary realizability. Other searched literature concerns Fourier-zero counts or fourth moments of four-point supports rather than the binary flat-spectrum property. No inspected statement implied the global two-family if-and-only-if classification.

## Limitations
The theorem is specific to supports of cardinality four and to the two-phase alphabet \(\{+1,-1\}\) up to a common scalar. It does not classify all complex extremal measures on the rectangle, \(\mathbb Z_7\), or exceptional families, nor does it address larger supports or the distinct property that the Fourier transform itself be real.

The 1981 article predates the exact day-level public-source record used in the machine metadata. The inspected journal metadata gives its 1981 issue but not a verified first-public day. The earliest day-resolved public availability verified for that exact full text is the author-uploaded copy dated 2016-06-28; no day in 1981 is inferred.

A residual literature risk remains that the same binary-phase classification may have been encoded in older perfect-sequence, weighing-matrix, or periodic-autocorrelation terminology. Targeted searches under those aliases did not locate an equivalent theorem.

## References
1. C. C. Graham and L. T. Ramsey, *Sidon sets with extremal Sidon constants*, Proceedings of the American Mathematical Society 83 (1981), 522--526, DOI: 10.1090/S0002-9939-1981-0627683-3.
2. C. C. Graham, *A beastiary of sets having extremal Sidon constant, or, there must be more than one theorem somewhere here*, arXiv:1910.00924v1, 2019-10-01.
