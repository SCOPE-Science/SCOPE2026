# Scientific assessment

## Correctness — PASS
A focal cooperator's marginal shared return conditioned on \(K\) other cooperators in an \(\ell\)-person group is \(b_\ell\delta_\ell^K/\ell\). Binomial averaging proves the exact pay-off difference, rather than assuming its polynomial form. The second derivative of each term is nonnegative for all positive \(\delta_\ell\); its coefficient and base are strictly positive for every nontrivial size \(\ell\ge3\). This proves convexity and the uniform at-most-two *isolated* zero bound. The degenerate constant and affine cases are separately handled. The sharp example has rational coefficients and strict inequality witnesses, and its exact symbolic checks are reproduced in `verify.py`.

Correctness risks: The result does not extend to arbitrary marginal-benefit functions, negative weights or correlations across game partners. The claim is not an empirical statement or an enumeration-based proof.

## Originality — PASS, with residual risk
The motivating paper (Llabrés et al., arXiv:2604.07228) derives the geometric mixed-order payoff and proves the two-order equilibrium bound using a ratio argument in Appendix A; its actual equations and Appendix were inspected. The present theorem replaces the two-order restriction by an arbitrary finite support with independently chosen nonlinearities and benefit intensities; the proof of the extension invokes positivity of the whole second derivative. Peña (2012) studies general size distributions, but its geometric-payoff example has a *common* multiplier across sizes, precluding the decreasing/increasing competition in this example. Hauert and McAvoy (2024) address another family of frequency-dependent returns rather than the arbitrary-order geometric law. Semantic literature searches and research-record searches did not yield an identical generalization. The closest mathematical tools—convexity and the scalar phase-line test—are elementary existing methods; their novelty is not claimed.

Originality risks: Specialized unpublished or unindexed heterogeneous-synergy analyses could contain this same general no-go. A sufficiently broad existing general convex-payoff result may subsume the model-specific theorem even if its title is unrelated. Search absence alone is not proof of priority. Independent literature audit is still needed.

## Mathematical value — PASS
Adding interaction types to public-goods models is a natural route to richer coexistence landscapes; the source paper exhibits richer behavior for mixing two orders but does not resolve whether additional orders permit further isolated interior states. The theorem provides a complete universal obstruction: no number of geometric-return orders can create a third isolated interior equilibrium or a second attracting mixed equilibrium. It characterizes the two-root region exactly using derivatives, endpoint levels and a unique minimum, and supplies a three-distinct-order parameter example showing that the bound can be reached while discount and synergy coexist. This is a meaningful structural constraint on a natural evolutionary model class, beyond merely recomputing an existing two-order numerical figure.

Value limitations: The argument is elementary once convexity is recognized; it is not a general theorem for arbitrary nonlinear public goods or structured finite networks. The result's usefulness is to delimit one specific model class.

Self-review: passed. Independent audit: not yet performed.
