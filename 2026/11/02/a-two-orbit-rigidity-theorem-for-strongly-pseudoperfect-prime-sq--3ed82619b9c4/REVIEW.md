# Self-review

## Correctness — PASS

For \(n=2^a p^2\), the divisor sum \((2^{a+1}-1)(p^2+p+1)\) and the three odd-weight complement orbits give the exhaustive parity split. The proof excludes all one-orbit possibilities and classifies two-orbit possibilities by four pair-type cases. The sole exceptional middle singleton forces \(a=2\), \(p=3\). The two outer cases are eliminated with exact integer quadratics and consecutive-root barriers. All exponent boundaries, particularly \(a=1,2,3\) and square-root orbits, are handled separately. The exact-integer verifier checks 5,010 parameter pairs, but does not establish the infinite statement by enumeration.

## Originality — PASS, subject to residual literature risk

Wang–Zelinsky (arXiv:2609.36068, full HTML examined through the sparse-omission restrictions and computational examples) study one- and two-pair omissions in \(3\cdot2^a p\) and list \(36\), but do not state a low-orbit classification for \(2^a p^2\). Aryan et al. (arXiv:2310.01305, abstract reviewed) classify two omitted **individual divisors** in \(2^a p^2\); that condition does not control two entire complement orbits, which can comprise three or four individual divisors. The accessible published characterization of \(2^a p\) concerns exponent one on the odd prime, not the present prime-square family. OEIS A334405 gives the example \(36\), not the uniform uniqueness theorem. Targeted semantic and literature searches identified no equal or stronger implication. A hidden specialization of work on sparse divisor omissions or four-near-perfect numbers remains possible. No independent priority certification is claimed.

## Mathematical value — PASS

The number of omitted complementary-divisor orbits is the natural sparsity parameter for strongly pseudoperfect representations. This theorem determines its entire zero-to-two range in a full two-prime-support family, with a unique exceptional square-root-orbit phenomenon at \(36\). It strengthens the ordinary two-omitted-divisor viewpoint without presuming higher-rank representability and gives a sharp lower bound of three omitted orbits everywhere else. It does not claim a complete classification of all strongly pseudoperfect numbers \(2^a p^2\).

## Closest sources and limitations

- A. Wang and J. Zelinsky, *Strongly Pseudoperfect Numbers*, https://arxiv.org/html/2609.36068 (full text, Sections 1–3, and example table).
- V. Aryan et al., *On 2-Near Perfect Numbers*, https://arxiv.org/abs/2310.01305 (abstract and theorem scope; accessible HTML unavailable).
- OEIS A334405, https://oeis.org/A334405 (example at \(36\)).
- Published bit-mask description of complement omissions for \(2^a p\), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-first-multi-pair-strongly-pseudoperfect-number-of-the-form-2--067a5b7cff02 (different odd-prime exponent).

Self-review: passed. Independent audit: not yet performed.
