# Review of complete-prefix-coded positive critical periodic content

## Correctness — PASS

The proof defines the exact complete-code and strong-separation hypotheses. The Kraft identity fixes the Hausdorff exponent \(s=\log q/\log(1/r)\). A cyclic \(q\)-ary de Bruijn sequence of length \(q^n\) is parsed by the deterministic complete-prefix decoder on \(\mathbb Z/q^n\mathbb Z\); every directed decoder cycle consumes a positive multiple of \(q^n\) letters, so its number of codewords is at least \(q^n/L\). Distinct cycle starts have distinct source length-\(n\) factors, forcing total common-codeword-prefix length at most \(n-1\). Strong separation and exact similarity scaling give \(\eta_n\ge\delta r^{n-1}\). Thus \(p_n\eta_n^s\ge(\delta/r)^s/L\), with periods tending to infinity. This is an infinite analytic proof; the finite verifier independently exercises the symbolic mechanism and the displayed planar geometry uses exact rectangles. The weak-convergence statement is precisely covered by Kong–Wang–Yu Theorem 1.3 after its premises are established.

## Originality — PASS (provisional bibliographic assessment)

Kong–Wang–Yu introduce the invariant and explicitly ask the inhomogeneous critical-content question (Question 5.1); their homogeneous theorem and inhomogeneous dimension equality do not imply positivity here. The closest published two-map theorem treats ratios \(\rho,\rho^2\), whereas the present complete-prefix theorem includes the three-map ratios \(\rho,\rho^2,\rho^2\) and arbitrary complete finite prefix-code length profiles. The two-map critical exponent is smaller, so its lower-gap estimate does not imply positivity at the three-map exponent. The decoder-cycle argument supplies the new transfer of full-shift de Bruijn separation to variable-length IFS time. Moreno's 2005 abstract concerns de Bruijn cycles of restricted languages rather than critical Euclidean periodic content, but its full text was not available in this comparison. The known literature and semantic-record searches disclosed no dominating general prefix-code periodic-content theorem. Residual risks include unindexed variable-length suspension results and uninspected details of older combinatorial literature.

## Mathematical value — PASS

This is a structurally motivated positive answer for an infinite, naturally generated class of unequal-ratio systems to a recent explicit open question, not a finite table or parameter substitution. It yields a uniform explicit lower bound and a three-map strongly separated planar witness, and it gives concrete periodic-orbit measures converging to the canonical Hausdorff measure. Completeness is exactly the Kraft-critical balance, explaining why fixed-length universal cycles can be used after variable-length decoding. It does not resolve arbitrary inhomogeneous ratios and does not assert an optimal critical-content constant.

Self-review: passed. Independent audit: not yet performed.
