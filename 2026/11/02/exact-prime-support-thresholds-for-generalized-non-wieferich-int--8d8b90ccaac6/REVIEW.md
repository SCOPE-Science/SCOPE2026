# Review of exact prime-support thresholds for non-Wieferich integers

## Correctness — PASS
The calculation is an unconditional identity: odd-prime order lifting computes the order modulo each prime power, Chinese remaindering computes the global order, and another lifting step yields the exact quotient valuation. The proof explicitly excludes the exceptional prime \(2\) and noncoprime bases. Independent direct modular computations in `verify.py` check both the full criterion and its exponent boundaries. Numerical checks do not replace the proof.

## Originality — PASS, with remaining priority risk
The directly inspected 2026 paper of Siegel focuses on the global asymptotic and offers conditions for squarefree integers and bounds for nonsquarefree integers. The entire four-page 1995 Franco–Pomerance article gives the order-based definition, density one for Wieferich integers, and a one-prime obstruction; it does not give the complete threshold vector. OEIS A182297 and A237292 provide membership data and an order-ratio identity, but not the claimed classification of every exponent vector at fixed prime support. Targeted mathematical searches found no matching explicit theorem. The conclusion is subject to the risk that standard prime-power lifting has previously been assembled into the same all-support formula without being indexed or titled that way.

## Mathematical value — PASS
The exact exponent threshold \(t_p\) resolves natural membership for every integer with prescribed prime support, identifies a unique least admissible integer for each support, and computes the exact first non-Wieferich power of every odd integer. These qualitative structural statements are not direct restatements of the motivating density bound and require cross-prime order interactions. The generalized base parameter is natural. The proof is elementary; novelty and value should not be mistaken for a claim of technical depth, a new density asymptotic, or independent validation.

Self-review: passed. Independent audit: not yet performed.
