# Scientific review: sharp decreasing-tail threshold

## Correctness

PASS. The assertion quantifies over all integers \(k\ge2\), all real \(\lambda>0\), and every integer \(n\ge k\). From the two exponential generating functions, the exact first-block differences are \(\lambda^2(S_{k+t}-T_t)\). Vandermonde convolution and the factorial denominator inequality establish \(S_{k+t}\le S_kT_t\), excluding later first-block reversals before the unique crossing \(S_k=1\). The first comparison \(p_k>p_{k+1}\) is separately verified, with a necessary special treatment for \(k=2\). The coefficient recurrence then propagates strict descent to the infinite tail. At and above the root the crossing itself disproves strict descent. The independent exact-rational finite checks support, but do not replace, these analytic steps.

## Originality

PASS with bibliographic risk. The closest directly inspected source, Mane (arXiv:2310.05671v1, §4), states precisely this boundary as Conjecture 4.3 and presents numerical rather than general proof. The earlier Mane manuscript (arXiv:2310.00827v1, §4) proves propagation from a decreasing block but not that the proposed sharp root gives the required block for all orders. Kwon–Philippou (Entropy 25 (2023), 699) concerns small-order global modes and is not a full all-order tail criterion. Equivalent unpublished or differently titled work cannot be excluded by the searches performed.

## Value

PASS. The result closes a specifically formulated, natural probability-theoretic conjecture for **every** integer order, converting a local crossing polynomial into an if-and-only-if infinite-tail criterion. It identifies the exact sharp transition and its endpoint obstruction, not merely an improved numeric bound or a small-order example. Such a threshold matters when verifying monotonicity and tail shape of uniform-jump compound Poisson distributions.

## Limitations and closest literature

The conclusion assumes independent, equal-rate component Poisson counts. It is distinct from a global-mode classification and does not extend to arbitrary compound Poisson jump intensities. The detailed bibliography is in RESULT.md. Priority beyond the inspected literature has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
