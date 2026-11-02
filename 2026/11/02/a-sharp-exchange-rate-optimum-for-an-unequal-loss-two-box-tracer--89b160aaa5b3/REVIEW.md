# Scientific review

## Correctness

**PASS.** The two-box matrix exponential produces the exact receiver impulse response; its logarithmic exchange-rate derivative has precisely one zero because every zero has the proved strictly negative derivative. The positive hyperbolic power series proves the key parameter monotonicity without approximations. The separate zero-contrast case is monotone rather than unimodal. The boundary values and observation normalization are explicitly included. A standalone script tests the exact critical-point algebra, the hyperbolic coefficients, numerical location and ordering of maxima, and the original matrix exponential (1,444 checks). Computation corroborates the analytic proof and is not used to infer infinite uniqueness.

## Originality

**PASS within the inspected evidence, with historical-priority risk.** The archived full source for the two-box exchange-with-reaction model explicitly contains the same passive exchange and local reaction equations, so the ODE is prior art. Its complete four-page instructional guide and the complete two-page exchange-only guide were inspected in full alongside both source-code files; none gives the fixed-horizon global tuning law. The 1984 lake-model article and the 2000 tracer-study abstract concern model calibration and late-time transfer; their accessible descriptions do not imply the theorem. Search comparisons with other published mathematical claims found no same-formulation or stronger covering claim. The original 1984 journal article and full 2000 report were not fully inspected; independent historical priority remains unresolved.

## Value

**PASS.** A single finite observation time is a natural endpoint for tracer measurements. The result proves that increasing transfer indefinitely can *reduce* downstream snapshot concentration when decay differs, classifies the exact equality boundary, and gives a unique optimally tuned rate with a universal dimensionless lower bound and monotone sensitivity to loss contrast. These properties directly characterize a meaningful design/interpretation feature of even the simplest reactive two-zone water-quality model, without claiming field validity or an optimal integrated exposure.

## Closest literature and limitations

The full archived model sources `Comp2Exchange_0.mod` and `Comp2ExchangeReaction_0.mod`, and their complete two- and four-page instructional guides, contain the governing transport/reaction systems but no finite-horizon parameter optimizer. Shanahan–Harleman (1984), DOI `10.1061/(ASCE)0733-9372(1984)110:1(42)`, and Haggerty–McKenna–Meigs (2000), Sandia SAND99-3120J, establish environmental multiple-box or rate-limited mass-transfer motivations. Detailed historical coverage of inaccessible parts is unverified. The mathematics is restricted to two equal volumes, constant linear exchange and losses, and a receiver snapshot.

Self-review: passed. Independent audit: not yet performed.
