# Scientific review

**Correctness — PASS.** Conditioning on the entire descendant label set leaves independent uniform parent choices within the branch and its complement. The resulting conditional leaf law is an independent sum, with a singleton-root correction. Leaf counts have an exact Eulerian distribution, and differentiation of its moment-generating function yields cumulants through order one less than tree size. A Laurent coefficient at the next even order gives the sharp defect \(-\beta_{2h}\). All steps are analytic. The included standard-library checker passed 6,586 exact rational assertions, including exhaustive trees up to nine vertices; these do not replace the unrestricted proof.

**Originality — PASS, with historical-priority risk.** Goldschmidt and Martin (arXiv:math/0502263, Sec. 2.2) establish the uniform recursive-tree/Chinese-restaurant connection. Bryc, Minda and Sethuraman (arXiv:0809.4741) study unconditioned leaves and their limits. The nearest published recursive-tree comparison concerns root degree versus leaves, not first-branch size or conditional cumulants. Their main accessible statements do not establish the exact moment-invisibility hierarchy or its sharp Bernoulli cutoff. A less accessible older split-tree treatment could still imply the result; no uniqueness guarantee is asserted.

**Mathematical value — PASS.** The result identifies a natural family of conditional statistics that provably cannot reveal the first root-branch size up to a sharp finite order. The general-order cutoff and explicit nonzero boundary defect go substantially beyond an isolated covariance identity. It may inform moment-based inference about split sizes and demonstrate the limits of low-order leaf statistics.

**Limitations.** Uniform independent-parent recursive trees only; finite-order equal moments do not imply conditional independence or equal full laws. The even-order cutoff is sharp; the optimal odd-order threshold is not claimed. Historical priority remains provisional. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
