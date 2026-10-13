# Scientific review: sharp cold-collective ergotropy asymptotics

## Correctness — PASS
The spin-sector stationary populations follow from the explicitly stated collective Lindbladian and a maximally mixed input; the lowest-weight vector in spin sector \(j=n/2-k\) has excitation count \(k\). The exact nonzero eigenvalue and multiplicity are \((2j+1)/2^n\) and \(\binom nk-\binom n{k-1}\). Passive sorting uses ordered spectral ranks, not a thermal-equilibrium assumption. The logarithmic moderate-deviation formulas put occupied ranks at energy distance \(\tfrac12\sqrt{n\log n}\) below the spectral center. A total-spin Casimir moment bounds the fluctuating spin by \(O(\sqrt n)\); a uniform Hoeffding tail bound upgrades rank-quantile convergence in probability to convergence of its expectation. The resulting coefficient is exactly \(1/2\). An independent computational-basis check returned `VERIFY_OK` for \(n\le7\), while exact spectral sorting was checked for \(n<40\). Finite tests are not treated as proof of the limit.

## Originality — PASS, subject to specified residual risk
The closest source [1] gives the same zero-temperature spin-sector stationary populations (its Eq. (88)) and general ergotropy analysis. This removes stationary-state derivation and finite passive sorting as standalone novelty. However, its asymptotic activation argument concerns interior bath/input parameters and establishes positivity, not the boundary limit \(\mathcal W_n/(\omega\sqrt{n\log n})\to1/2\) with an explicit constant. In [2], the full-text scaling sections address ground or random inputs, not this fixed maximally mixed input with cold bath. The abstract of [3] concerns a separate charging construction, and the full text was inaccessible, leaving a disclosed indexing risk. Targeted published-literature, semantic-database, and existing-result comparisons did not identify a stronger theorem that entails the sharp boundary asymptotic. This is not an independence or exhaustive novelty certification.

## Value — PASS
A known many-body dissipative protocol had nonzero work and numerical size dependence but lacked a sharp quantitative scale at the simultaneous thermal endpoint. A \(\sqrt{n\log n}\) law is neither extensive nor ordinary \(\sqrt n\) spin fluctuation scaling; its constant arises from spectral-rank constraints in exponentially degenerate energy levels. The result identifies the exact degree of extraction possible under unrestricted global control and explains the otherwise surprising logarithmic enhancement. The claim is restricted to its idealized model and does not imply device-level feasibility or finite-time performance.

## Closest literature and limitations
[1] B. Ahmadi et al., *Harnessing Environmental Noise for Quantum Energy Storage*, arXiv:2510.06384v1, Sec. II, Eq. (27)/(88), Sec. III–IV; full text inspected at https://arxiv.org/html/2510.06384v1 .

[2] B. Çakmak, *Ergotropy from coherences in an open quantum system*, arXiv:2005.08489v3, Sec. IV.B; primary PDF inspected at https://arxiv.org/pdf/2005.08489 .

[3] G. Watanabe et al., *Scaling law of asymptotic freedom in collective charging of quantum batteries*, arXiv:2606.10054v1; abstract inspected at https://arxiv.org/abs/2606.10054 ; complete source was not retrieved and remains a residual risk.

The Markovian, exactly collective, strictly cold-bath, infinite-input-temperature, ideal-global-extraction scope is essential. A differently indexed scaling result or more general transfer theorem could reduce originality.

Self-review: passed. Independent audit: not yet performed.
