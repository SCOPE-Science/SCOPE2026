# Same-model review

## Claim
For the real plane \(X=(\mathbb R^2,\|\cdot\|_{2,1})\), where \(\|(u,v)\|_{2,1}=\sqrt{u^2+v^2}\) when \(uv\ge 0\) and \(\|(u,v)\|_{2,1}=|u|+|v|\) when \(uv\le 0\), the Ptolemy constant is exactly \(C_{\mathrm{Pt}}(X)=\sqrt 2\).

## Correctness
**PASS.** The identity
\[
\|(u,v)\|_{2,1}=\max\left\{\sqrt{u^2+v^2},|u-v|\right\}
\]
is exact on both sign regions. The Ptolemy upper bound treats every possible pair of active numerator branches. The Euclidean and one-dimensional same-branch cases have constant \(1\); each mixed case costs at most the sharp comparison factor \(\sqrt2\). The explicit triple \((a,0),(0,a),(a,a)\) attains \(\sqrt2\), so the upper bound is sharp.

## Originality
**PASS, with an access residual.** Targeted searches found no direct statement for the \(\ell_2-\ell_1\) plane. Yang--Li (2015) treats the exact family but different constants. Zuo (2012) does not imply the value through its midpoint-extremum theorem: after converting to an absolute normalized norm, the Euclidean comparison ratio is larger at \(t=2-\sqrt2\) than at \(t=1/2\). Zuo (2018) was inspected through its comparison theorems and concrete examples; the relevant exact theorems require midpoint extremality or symmetry not present here.

The main residual risk is Zuo (2015), DOI 10.12386/A2015sxxb0033. Its abstract was available, but readable full text was not obtained in bounded access attempts. This source is recorded as unresolved rather than treated as evidence of noncoverage.

## Value
**PASS.** The Ptolemy constant is a standard quantitative invariant of Banach-space geometry. The \(\ell_p-\ell_1\) family already has exact James-type and von Neumann--Jordan-type calculations in the literature, so determining \(C_{\mathrm{Pt}}\) for its \(p=2\) member is a natural complementary exact fact. The proof also identifies a reusable structural mechanism: a maximum of two Ptolemaic gauges with a sharp \(\sqrt2\) comparison.

## Closest literature and limitations
The closest inspected sources are Yang--Li (2015), Zuo (2012), and Zuo (2018), with Zuo (2015) remaining an access-limited comparison. The claim is only for the real two-dimensional \(p=2\) member; no statement is made here for general \(p\).

Same-model review: passed. Independent audit: not yet performed.
