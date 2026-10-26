# Scientific review of the critical radial-confinement quantile theorem

## Correctness — PASS

The conclusion is a theorem for fixed \(a>0\), \(\beta\in[1/2,1]\), and \(q\in(0,1)\). The independent radial normalization, the explicit derivative \(-F'_\beta(t)\), and the Poisson-age formula establish strict monotonicity. The stationary complementary fraction is the modified-Bessel integral of the inverse-gamma variable, so the unique critical rate and its strict dependence on the shape are rigorous. The exact relaxation excess has a positive integrand. Uniform endpoint Laplace asymptotics near the critical rate establish its \(e^{-rt}t^{-\beta-1}\) scale; a Taylor expansion of the stationary mass and fixed-window sign brackets yield the full \(-\log\log\) coefficient and explicit constant. The accompanying `verify.py` passed 75 independent finite numerical assertions. Numerical cases corroborate but do not establish the theorem.

## Originality — PASS, subject to independent priority review

The main antecedent (Sandev et al., arXiv:2609.24427v1) gives the free radial laws, resetting renewal equations, the median threshold and qualitative logarithmic divergence. Its Sections 2.4 and 3.4, including equations (47)--(51) and (91)--(94), do not state the sharp finite-time transition window or its coefficient \(\beta+1\), its explicit Bessel intercept, or a full quantile-and-interpretation crossing classification. The classical renewal mechanism in Evans and Majumdar (2011) is not new; standard Laplace asymptotics and Bessel identities are not claimed to be new. Searches of relevant literature and available mathematical research records did not locate stronger coverage of this combined finite-window statement. This is best-knowledge assessment, not a literature-wide priority certificate. Residual risk: a broad general renewal/quantile theorem could imply the same asymptotics without citing the heterogeneous diffusion setting.

## Value — PASS

Near the confinement transition, a merely logarithmic approximation leaves an unbounded error of order \(\log\log(1/\epsilon)\). The theorem supplies a universal corrected observation clock, finite-window crossing profile and exact parameter threshold. The correction distinguishes the Itô, Stratonovich and Hänggi--Klimontovich conventions by \(2\), \(7/4\) and \(3/2\), respectively, which can be used when interpreting threshold-time data. The result is specific to a physically motivated disk-occupancy observable, not an arbitrary parameter slice. It separates instantaneous occupation from first passage, a distinction essential for correct application.

## Literature and limits

The full relevant HTML sections of arXiv:2609.24427v1 were read and compared to the theorem's mathematical implications. Background comparisons used Evans and Majumdar (2011, arXiv:1102.2704) and Cherstvy, Chechkin and Metzler (2014, doi:10.1039/C3SM52846D), with only their accessible abstract-level material read; neither was treated as a full-text absence certificate. No claim is made for non-Poisson resetting, first-passage survival, operational-time memory, or joint parameter limits. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
