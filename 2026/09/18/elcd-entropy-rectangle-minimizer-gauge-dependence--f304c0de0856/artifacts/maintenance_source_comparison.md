# Primary-source comparison and scope of the correction

The primary ELCD paper, arXiv:2609.19838v1, equation (2.2) and Section 3, was compared to the complete theorem in this record. Section 3 motivates entropy minimization on a density-pressure rectangle and explicitly infers from convexity that one need only consider its corners. Algorithm 1 subsequently implements a **discrete four-candidate** choice. These are distinct assertions: the record corrects the continuous-rectangle inference, not the fact that a minimum over four explicitly prescribed candidates is at one of those four candidates.

For \(\gamma>1\), the mathematical entropy is strictly decreasing in pressure. On the upper-pressure edge its unique unconstrained density minimizer is
\[
\rho_C=\exp(-1+C/\gamma)p_+^{1/\gamma}.
\]
Clamping this density to the permitted interval gives the rectangle minimum. It can be an edge-interior point; convexity alone therefore does not justify the parent inference. Adding a conserved-mass multiple to an entropy remains a valid entropy gauge but can alter minimization over different candidate densities. The exact identric-mean switching formula and excess identity quantify this separate selection issue.

The later arXiv:2609.24479v1 discusses physical entropy in empirical LLF/ELCD comparisons. Its complete Appendix B reproduces the same corner algorithm; it does not derive the continuous minimizer or the gauge-switching formulas. This record does not claim to refute its numerical experiments, prove that a different flux performs better, or supply a general entropy-stability theorem.

A fresh five-hit Resultary query for ELCD entropy, rectangle, identric mean and gauge returned this record and four mathematically different topics. This finite semantic search is supplementary, not an exhaustive originality certificate. Original exact web searches are retained at their recorded scope.
