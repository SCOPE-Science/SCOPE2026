# Scientific review

**Correctness — PASS.** The conditional-window lemma has a direct intermediate-value argument valid uniformly for centers in \([-1,1]\), the conditional centered-block estimate follows from Hoeffding plus a Bernstein-controlled grid, and the double geometric summations yield respectively \(O(M)\) information cost and \(O(\sqrt{\log M/M})\) expected approximation error. Zero frequency and the independent tail are both included. The deterministic Fejér estimate and centered-tail maximal bound were checked against Section 4 of the source.

**Originality — PASS, with residual risk.** The closest full text is Kyselov (2026), Theorem 1.2 and its proof, which gives a squared logarithm and explicitly makes no optimality claim. The single-logarithm estimate cannot follow by weakening that lower bound. The 2017 qualitative support theorem does not provide the quantitative bound. Searches for equivalent small-ball bounds and for random-Fourier-series general theorems found no dominating statement. Implicit coverage by a general small-deviation result remains a real risk.

**Value — PASS.** A uniform quantitative estimate for a natural arithmetic random Fourier process is improved by an entire logarithmic factor in its exponential cost, using a transferable scale-dependent centered-conditioning technique. The improvement applies to the full target class rather than one constructed example.

**Limits.** No matching upper bound, general optimality, or endpoint-of-support statement is claimed. The original Kloosterman convergence theorem does not imply an effective finite-prime rate.

Self-review: passed. Independent audit: not yet performed.
