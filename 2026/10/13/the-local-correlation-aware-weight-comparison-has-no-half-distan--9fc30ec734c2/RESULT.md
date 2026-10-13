# The local correlation-aware weight comparison has no half-distance ceiling

## Finding
For the local two-class comparison used in Section III of arXiv:2607.01342v2, the advertised correlation-aware ceiling at \(\lceil d/2\rceil\) does not follow from the displayed weights. Let \(d\ge3\) be odd and let a contiguous packet error \(E\) occupy \(n\) sites of a minimum-weight logical \(\bar X\) chain, with \(1\le n<d\). Its logical complement is
\[
E'=E\bar X,
\]
and occupies exactly \(d-n\) sites. The two errors have the same syndrome because \(EE'=\bar X\) commutes with every stabilizer.

The source assigns the packet event the single-edge cost
\[
w_{\mathrm{net}}=-\log p_{\mathrm{net}},
\]
and assigns each independent local edge the cost
\[
w_{\mathrm{gate}}=-\log p_{\mathrm{gate}}.
\]
Therefore its complement has the displayed-model cost
\[
w(E')=(d-n)w_{\mathrm{gate}}.
\]
Whenever \(0<p_{\mathrm{gate}}\le p_{\mathrm{net}}<1\), monotonicity of \(-\log\) gives
\[
w_{\mathrm{net}}\le w_{\mathrm{gate}}\le(d-n)w_{\mathrm{gate}}.
\]
Thus the packet edge is never more expensive than its logical complement for any \(n<d\). It is strictly cheaper for every \(n\le d-2\), even when \(p_{\mathrm{net}}=p_{\mathrm{gate}}\), and is also strictly cheaper at \(n=d-1\) whenever \(p_{\mathrm{net}}>p_{\mathrm{gate}}\). The sole boundary tie is \(n=d-1\) with equal probabilities.

Consequently, the local packet-versus-complement argument itself has no half-distance ceiling. Within that reduced comparison, all packet sizes \(n<d\) are locally favored by a correlation-aware edge under the paper's condition \(p_{\mathrm{net}}\ge p_{\mathrm{gate}}\); the genuinely different obstruction is \(n=d\), where the packet is the full logical operator and has zero syndrome. Any rigorous upper bound below \(d\) must therefore come from other matching classes, combinations of faults, or additional geometric/noise assumptions rather than from the displayed two-class comparison.

## Assumptions and scope
The statement concerns exactly the source's reduced on-chain comparison: a contiguous packet support contained in one minimum-weight logical \(\bar X\) chain, its complement on that same chain, the source's costs \(-\log p_{\mathrm{net}}\) and \(-\log p_{\mathrm{gate}}\), and \(0<p_{\mathrm{gate}}\le p_{\mathrm{net}}<1\). It does not replace the full detector-error model by this one-dimensional reduction and it does not assert that full MWPM decoding is fault tolerant for every \(n<d\).

The source explicitly notes that a third error class could be cheaper than the packet edge. That caveat remains. The present result isolates a different point: the logical complement cited in the paper cannot by itself create the claimed correlation-aware cutoff at \(\lceil d/2\rceil\).

## Proof
Because \(EE'=\bar X\), the errors \(E\) and \(E'\) differ by a logical operator and therefore yield the same stabilizer syndrome. The source's packet model represents \(E\) by one correlated edge of weight \(w_{\mathrm{net}}=-\log p_{\mathrm{net}}\). Its local comparison represents \(E'\), which contains \(d-n\) sites, by \(d-n\) local edges, giving \(w(E')=(d-n)w_{\mathrm{gate}}\).

Since \(p_{\mathrm{net}}\ge p_{\mathrm{gate}}>0\),
\[
-\log p_{\mathrm{net}}\le-\log p_{\mathrm{gate}}.
\]
Since \(n<d\), one has \(d-n\ge1\), and because \(p_{\mathrm{gate}}<1\), one has \(w_{\mathrm{gate}}>0\). Hence
\[
w_{\mathrm{net}}\le w_{\mathrm{gate}}\le(d-n)w_{\mathrm{gate}}=w(E').
\]
If \(d-n\ge2\), the second inequality is strict. If \(d-n=1\), the comparison is strict precisely when \(p_{\mathrm{net}}>p_{\mathrm{gate}}\); equality occurs only for equal probabilities. At \(n=d\), the complement is the identity and the packet is the complete logical operator, so the syndrome vanishes and this two-defect comparison no longer applies. This proves the claim.

## Verification
No finite experiment is needed for the all-\(d\), all-\(n\) statement. The proof uses only the source's own formulas for the two compared matching costs, the exact identity \(EE'=\bar X\), and monotonicity of \(-\log\). Boundary cases were checked explicitly: \(n=\lceil d/2\rceil\) is not special in the inequality; \(n=d-2\) leaves a two-edge complement and is strictly more expensive; \(n=d-1\) leaves a one-edge complement and gives the unique possible tie; \(n=d\) has zero syndrome.

## Relationship to prior work
Rennela's paper derives a decoder-independent floor \(n\le\lfloor d/2\rfloor\), then proposes the correlation-aware design rule \(n_{\max}^{\mathrm{corr}}=\lceil d/2\rceil\). Its Section III explicitly compares one packet edge of cost \(-\log p_{\mathrm{net}}\) with a logical complement and labels that comparison heuristic because a third matching class may be cheaper. The same section states the complement has \(\lfloor d/2\rfloor\) local edges at \(n=\lceil d/2\rceil\).

The observation above applies the identical comparison at arbitrary \(n<d\), where the complement has \(d-n\) local edges. It shows that the pairwise rationale actually continues to favor the packet edge past \(\lceil d/2\rceil\). The public source-specific review of the paper independently flags that the correlation-aware ceiling is not proved and that third error classes remain unresolved, but it does not identify this all-\(n\) consequence of the displayed local weights. Fowler's earlier correlated-decoding work establishes the importance of using correlated error probabilities in surface-code decoding; it does not analyze this multi-gate-teleportation packet/complement comparison.

## Limitations
The result is deliberately not a theorem about the full two-dimensional detector-error model. A different matching with the same syndrome can have lower total weight, correlated and local faults can occur together, and effective DEM edge probabilities need not equal one bare gate-fault probability. Those issues can impose a practical cutoff below \(d\). The claim is only that the paper's stated two-class local argument cannot establish \(\lceil d/2\rceil\) as that cutoff and, in fact, favors the packet edge for every \(n<d\) under its own probability ordering.

No claim is made about arbitrary target placement, other Pauli sectors, other codes, or the packet-versus-sequential logical-error-rate crossover.

## References
1. M. Rennela, *Design rules for fault-tolerant multi-gate teleportation*, arXiv:2607.01342v2 (2026).
2. A. G. Fowler, *Optimal complexity correction of correlated errors in the surface code*, arXiv:1310.0863v1 (2013).
