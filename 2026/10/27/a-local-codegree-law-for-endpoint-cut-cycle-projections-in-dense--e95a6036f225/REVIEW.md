# Scientific review: local-codegree law for dense regular complements

## Correctness — PASS

The theorem fixes the graph class, projection normalization, and every finite parameter. The key identity \(L_{\overline H}|_{\mathbf1^\perp}=NI-L_H\) leads to an absolutely convergent Neumann expansion because \(2r/N\le1/2\). Its remainder has \(\ell_1\) norm at most \(16r^2/N^3\). The first two terms have exactly three non-source potential levels, counted by \(A=r-c_e\); the proof evaluates their total variation in the complete graph and subtracts every deleted edge, including the explicitly controlled non-source contribution \(T\). The resulting \(32r^2/N^2\) error is then converted to the \(44r^2/N^2\) complementary-projection error using the exact diagonal resistance identity. Distinct integer codegrees differ at first order by at least \(2/N\), establishing the stated sufficient threshold. Independent finite matrix reconstruction of 606 columns is supplementary rather than the basis of the infinite proof.

## Originality — PASS, with residual bibliographic risk

Schild–Rao–Srivastava, *Localization of Electrical Flows* (arXiv:1708.01632), gives a universal average localization result and an expander Neumann expansion, but not a local codegree coefficient for arbitrary regular complements. Dilworth–Kutzarova–Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582), treats invariant projections and explicitly computes ordinary Hamming-cube norms, not regular deleted-subgraph perturbations. Gurel-Gurevich–Nachmias–Sachdeva, *A Tight Bound on Localization of Electrical Flows* (arXiv:2605.24130), gives a universal logarithmic localization estimate, again not the edgewise density expansion. Relevant indexed results about sparse-graph and graph-subspace projections were checked by mathematical implication, and do not directly establish the result. No search result proves novelty; equivalent unpublished or poorly indexed perturbation results remain a risk.

## Value — PASS

The theorem supplies the first-order response of canonical real Banach endpoint projection norms to a general regular pattern of edge deletions. Its coefficient reveals an otherwise hidden **local-neighborhood overlap** effect despite identical graph degrees, and yields a uniform strict rule excluding larger-codegree edges from both global maximizer sets for sufficiently dense complements. The conclusions apply to nontransitive regular deleted graphs and give concrete structural consequences for complements of cycles and hypercubes. This goes beyond merely restating spectral or resistance bounds; it resolves which local graph statistic selects maximizing currents to first order. The constants and density cutoff are only sufficient, not asserted optimal.

## Remaining limits

No assertion is made about exact global values for every graph, ranking within the minimum-codegree class, weighted or irregular deletions, intermediate \(\ell_p\), or minimum norms over nonorthogonal projections. Bibliographic completeness is not independently certified.

Self-review: passed. Independent audit: not yet performed.
