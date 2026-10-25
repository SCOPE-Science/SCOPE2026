# Review

## Correctness — PASS

The graph is defined for every integer \(n\ge3\); its labelled binary transition matrix is exactly \(\left(\begin{smallmatrix}S+S^{-1}&I\\I&0\end{smallmatrix}\right)\). The proof establishes invertibility and computes both Smith factors of \(F_n^t-I\) in the Laurent-polynomial PID before quotienting. The only characteristic-two exception is the central root at \(s=1\) when \(n,t\) are both odd. The resulting kernel dimensions, finite-order bounds, Möbius inversion, and explicit parity-conserving affine involution yield one consistent complete claim. The standalone script constructs independently labelled adjacency matrices, tests rank and polynomial gcd formulas, exhaustively simulates 349,504 small states and checks the affine period pairing for all odd sampled sizes. Unbounded \(n\) is covered by the algebraic proof, not by extrapolating checks.

## Originality — PASS (bounded historical assessment)

The 1995 Kawahara–Lee technical report was inspected across its fifteen PDF pages, including its definitions and Theorem 4.2: its finite one-dimensional cellular automaton uses null boundary conditions and characterizes particular period-length phenomena rather than the complete sunlet cycle population and affine odd/even period correspondence. Martin–Odlyzko–Wolfram (1984) gives generic higher-order additive machinery and relevant period bounds; those are credited, not asserted to be new. Vlasov's open 2014 paper uses reversible memory dynamics on a different (infinite) domain. Checked published-result records concerning rule-90 sensors, asynchronous sweeps, rule-115 finite-support periods and parity on unrelated graph families do not imply the present arithmetic pairing. A materially relevant 1986 article by Guan and He claims general higher-order additive cycle multiplicity formulas; only its abstract was accessible. Accordingly this PASS concerns the unlocated *specific explicit arithmetic fixed-iterate formula together with the actual affine bijection*, not novelty of generic algorithms or period bounds. The opaque historical possibility of full-text broader coverage is a **material residual risk** rather than proof of uniqueness.

## Mathematical value — PASS

This is a natural graph dynamical system, equivalently a classic reversible memory variant of one-dimensional rule-90. The integer parity of the circumference causes a sharp qualitative change: even sizes have exactly the same orbit census as rotation of four-letter words, whereas odd sizes split every primitive-word population exactly in half between periods \(d\) and \(2d\). The split is explained by an explicit conserved binary parity and a statewise affine period-doubling involution, not just a numerical coincidence. These all-size structural laws give sharp period counts and a natural dynamical explanation of a central-frequency resonance.

## Sources and remaining limits

Primary dated source: Kawahara–Lee 1995, RIFIS 119 (full report inspected, not the boundary model studied here). Martin–Odlyzko–Wolfram 1984 (relevant accessible section excerpt); Guan–He 1986 (abstract only; full text unavailable), and Vlasov 2014 (open paper). published-finding corpus published-record similarity checks and accessible prior research claims found nearby but non-dominating topics. No exhaustive historical search or independent external assessment is claimed. A general unpublished or uninspected derivation may cover this result. The proof is specific to unweighted binary synchronous sunlets.

Self-review: passed. Independent audit: not yet performed.
