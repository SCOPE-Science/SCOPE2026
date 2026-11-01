# Self-review

## Correctness — PASS

The proof directly reconstructs the steady states of the stated four-compartment equations. For \(\sigma=1\), the infected balance forces \(S+C=k\), while the susceptible balance yields the exact rational formula for \(C\) in terms of \(z=SI\). The physical interval is characterized by strictly increasing \(I(z)\). The remaining stationary equation becomes a scalar intersection between a strictly increasing function and a strictly decreasing function, proving existence and uniqueness without using numerical root counts. Ordering the scalar equations proves the two feedback monotonicities. The stationary recovered equation gives the strict-versus-zero infected response and the limiting quadratic. The packaged standalone tests check reduction identities with exact fractions and representative residuals, not universal quantifiers.

## Originality — PASS under inspected sources

The 2026 SIRCm source [1] proves general endemic existence and weak/strong-feedback uniqueness but does not state this unconditional maximal-reinfection result or strict feedback-interaction dichotomy for \(g=SI\). The closest published published-finding corpus theorem [3], read in full, treats \(g=I\); it gives an *opposite* zero-sensitivity result at \(\sigma=1\) and explicitly excludes transmission-driven feedback. The two systems cannot be substituted into one another at a fixed parameter choice because the additional factor \(S\) varies with the endemic state. The original zero-feedback SIRC model [2] is a special case and does not cover the positive-feedback comparative statics. Search coverage is not exhaustive; general monotonicity frameworks are a residual priority risk.

## Mathematical value — PASS

The endpoint \(\sigma=1\) is the natural limiting case of maximal susceptibility of the cross-immune compartment. At this boundary, the distinction between prevalence-driven and transmission-driven feedback is mathematically sharp: the second escape channel is neutral for prevalence-driven feedback but strictly increases endemic prevalence in the transmission-driven formulation precisely when the first escape channel is active. The theorem also classifies the equilibrium for arbitrarily large independent feedback parameters, beyond the source's weak/strong results and numerical observations, and provides a checkable limiting quadratic. This is a motivated structural benchmark, not an arbitrary numeric slice or a stability claim.

## Literature and limitations

[1] Ramírez-Gutiérrez et al., arXiv:2610.01111v1, Sections 2–4 and Appendix 7; inspected in full relevant HTML sections. [2] Casagrandi et al., Mathematical Biosciences 200 (2006), 152–169; only accessible abstract and citation data were inspected. [3] published-finding corpus 2026-10-11, *All-feedback endemic uniqueness and separate monotonicity in the prevalence-driven SIRCm system*; complete RESULT.md inspected. No claim is made about orbital stability, general \(\sigma\), or clinical causality. Independent review and comprehensive historical-priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
