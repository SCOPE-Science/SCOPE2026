# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The argument was checked along three separate mathematical interfaces.

First, for boundary landmarks \(\{0,a,L\}\) on \(C_{2L}\), the three sorted distance functions were written explicitly on each order interval of the two semicircles. Comparing the resulting affine normalized codes gives a complete classification of all collisions. The parity split is essential: even \(a\) produces translation separation \(a/2\), while odd \(a\) produces \(\min(a,(L-a)/2)\). The formulas agree at the transition \(3a=L\).

Second, the passage from cycle codes to cylinder codes is exact: moving from layer zero to layer \(i\) adds \(i\) to all three sorted distances. Hence two normalized cycle codes can collide in an \(m\)-layer cylinder exactly when their minimum-distance offsets differ by at most \(m-1\). This proves the vertical-lift criterion without an approximation or probabilistic step.

Third, optimizing the exact separation formula over \(a\) gives \(\lfloor L/3\rfloor\); the explicit choices according to \(L\bmod6\) attain that value. Since \(n=2L\ge6m\), this separation is at least \(m\). The standard lower bound \(\operatorname{md}(G)\ge3\) for connected non-path graphs then makes the result exact.

A standalone checker was also executed as supporting evidence. It verified the collision classification for every odd \(7\le L\le301\) and all admissible \(a\), and checked the constructed resolving sets for \(3\le m\le40\) over a finite band of admissible circumferences beginning at \(6m\). These computations are not used in place of the proof.

## Originality

The closest primary source is Marcelo–Tolentino–Garciano–Buot (2025), DOI 10.61091/jcmcc126-15. Its Theorem 3.5 proves multiset dimension three for \(P_m\square C_n\) when \(n\ge8m+1\), and its conclusion explicitly states that determining the remaining cylindrical cases is open. The present result gives an infinite family in that open region, including all \(n\equiv2\pmod4\) with \(6m\le n\le8m\), and supplies a distinct structural mechanism via antipodal normalized-code collisions.

Searches covered the exact product notation, “cylindrical graph”, “multiset dimension”, “m-resolving set”, the equivalent ID-coloring terminology, mod-four/congruence formulations, and the direct reference chain. The 2026 survey by Farhan–Klavžar–Kuziak–Yero was also checked for current context. No prior statement matching either the \(n\ge6m,\ n\equiv2\pmod4\) theorem or the exact antipodal-capacity formula was found.

Originality is therefore assessed only to the best of our knowledge. No specific inaccessible paper was identified as especially likely to contain the same result; the directly relevant cylinder paper and foundational statements were accessible. Residual risk remains from differently indexed terminology or unindexed parallel work.

## Value

The result resolves an infinite, linearly wide portion of an explicitly open parameter region rather than a finite list of small cases. It improves the known sufficient circumference coefficient from 8 to 6 on a full congruence class and provides an exact mechanism—translation separation of normalized three-distance codes—that can be reused when searching for the other congruence classes.

## Limitations

The theorem only treats \(n\equiv2\pmod4\) and \(n\ge6m\). It does not determine multiset dimension for the other congruence classes in the remaining region, nor for \(n<6m\). The threshold \(6m\) is sharp for the particular antipodal boundary family in the sense proved here, but no global optimality claim is made for arbitrary three-landmark sets. No independent validation or cross-model review has been performed.
