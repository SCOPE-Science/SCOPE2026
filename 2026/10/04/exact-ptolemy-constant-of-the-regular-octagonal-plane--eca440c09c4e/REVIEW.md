# Same-model review

## Claim
For the real regular octagonal plane \(X=(\mathbb R^2,N)\), where \(N(x,y)=\max\{|x|,|y|,(|x|+|y|)/\sqrt2\}\), the Ptolemy constant is exactly \(C_{\mathrm{Pt}}(X)=4-2\sqrt2\).

## Correctness
**PASS.** The proof first establishes the globally sharp comparison
\[
\cos\!\left(\frac\pi8\right)\|v\|_2\le N(v)\le\|v\|_2
\]
by reducing, through all sign and coordinate symmetries, to a one-variable minimization whose unique transition is \(t=\sqrt2-1\). Euclidean Ptolemy then gives \(C_{\mathrm{Pt}}\le\sec^2(\pi/8)=4-2\sqrt2\). The explicit triple \((-1,\sqrt2-1),(\sqrt2-1,-1),(-2,-2)\) is admissible and has exact ratio \(4-2\sqrt2\). No finite experiment substitutes for the infinite upper bound.

## Originality
**PASS, with an access residual.** Targeted semantic searches found no claim-level match for the regular octagonal Ptolemy constant. Zuo (2012) was inspected in full: its concrete examples do not contain an octagonal instance, and its relevant Euclidean midpoint-comparison hypothesis fails because \(\psi_2/\psi\) is maximized at the octagon's branch transition rather than at one half. Komuro--Saito--Tanaka (first published in 2015) was inspected in full and explicitly defines this regular-octagonal norm, but studies James constant \(\sqrt2\) and contains no Ptolemy result.

Zuo (2018) was inspected at theorem and example level. Its Example 1 treats \(\max\{\|\cdot\|_p,\lambda\|\cdot\|_q\}\); the regular octagon is the endpoint \((p,q,\lambda)=(\infty,1,1/\sqrt2)\), while the displayed mixed-regime exact formula is stated only above that endpoint. Its general symmetric theorem also does not imply the value under Euclidean comparison because the theorem's range condition requires a value larger than the regular octagon's James-function maximum.

The remaining risk is Zuo (2015), whose abstract announces additional sufficient conditions. Its readable full text could not be obtained through bounded lawful access routes, so it is recorded as an unresolved source rather than counted as noncoverage.

The current prior ledger contains a Banach--Mazur formula for an octagonal family whose regular member is this norm. That result determines the same Euclidean distortion factor and hence is related to the upper bound, but it neither states a Ptolemy constant nor provides the lower-bound configuration. The final equality is therefore not a duplicate or a formal corollary of the stored claim.

## Value
**PASS.** The regular octagonal plane is a standard benchmark in two-dimensional Banach-space geometry, explicitly used in the James-constant literature. The Ptolemy constant is a standard metric-geometric invariant. The exact value identifies when the sharp Euclidean comparison bound is attained and supplies an explicit extremal configuration. It also settles the natural endpoint omitted from the displayed mixed-regime max-norm formula in the inspected 2018 examples, rather than selecting an arbitrary parameter slice.

## Closest literature and limitations
The closest inspected sources are Zuo (2012), Komuro--Saito--Tanaka (2015/2016), and Zuo (2018). Zuo (2015) remains an access-limited comparison. The statement is deliberately restricted to the single regular-octagonal norm.

Same-model review: passed. Independent audit: not yet performed.
