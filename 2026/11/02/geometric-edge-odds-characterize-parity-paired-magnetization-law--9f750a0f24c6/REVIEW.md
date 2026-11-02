# Review of geometric-odds parity pairing

## Correctness — PASS

The change-set distribution conditional on the total number of changes is a Gaussian subset-sum measure. Positive run-compositions yield explicit odd/even magnetization masses; a Gaussian-binomial quotient proves their pointwise proportionality, with all normalization factors accounted for. Consecutive paired laws differ by a kernel that is strictly decreasing in absolute magnetization, establishing strict likelihood-ratio order. For a four-spin window equality of the central magnetization masses is equivalent to \(v^2=uw\); applying this to overlapping windows yields geometric odds. Limits at \(q=1\), endpoint counts, and strictly positive support are handled. `verify.py` passed 986 exact assertions on the packaged formulas; finite computations support rather than replace the algebraic proof.

## Originality — PASS (qualified best-knowledge comparison)

Antal–Droz–Rácz (arXiv:cond-mat/0308442), particularly its finite free-boundary magnetization/domain-wall section, covers the homogeneous special case. Denisov–Hänggi (arXiv:cond-mat/0603417) investigates finite-chain domain statistics with homogeneous coupling. Neither inspected primary text supplies the characterization of spatially varying edge odds by equality on every four-spin window, nor the strict absolute-magnetization likelihood-ratio ordering for the geometric-odds family. Related fixed-composition transition statistics concern a distinct conditioning. Gaussian-binomial coefficients and weighted subset laws are classical ingredients and not claimed original. Remaining risk: more general historical weighted-run, spatially inhomogeneous Ising, or q-enumeration literature might imply one or more parts; independent priority examination has not occurred.

## Mathematical value — PASS

The locally checkable four-site criterion completely classifies a nonconstant family of inhomogeneous binary Markov chains by a strong global conditional-distribution degeneracy; the same structure forces ordered magnetization concentration at all lengths and a universal strictly negative covariance for all increasing absolute-magnetization scores. This is more than a restatement of homogeneous Ising counts or a numerical enumeration: it isolates precisely which spatial variation preserves the parity plateau and supplies a quantitative stochastic ordering of the full family of distributions.

## Closest work and limits

The strongest relevant comparison is the classical homogeneous Ising chain. The contribution does not claim the \(q=1\) joint law, Gaussian-binomial algebra, or independent certification. It assumes a fair initial spin, independent changes and finite positive odds, and is limited to contiguous paths. An uninspected source treating general spatially graded runs could affect originality.

Self-review: passed. Independent audit: not yet performed.
