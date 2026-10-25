# Scientific review

## Correctness — PASS

The graph-to-fixed-root-forest bijection and the \(\mathcal F(q,k)\) count yield the joint mixed factorial moments by deleting specified leaves and reattaching them to the correct parent classes. The calculation explicitly handles the empty noncycle set and the terminal case \(q=k\). The covariance follows from the three smallest moments, with an elementary strict inequality for every \(m\ge2\); the asymptotic coefficient follows from a first-order logarithmic expansion. Independent rooted-forest and simple-graph enumerations gave 273 passing exact comparisons, not an infinite proof.

## Originality — PASS, qualified

Pitman's 1996 forest enumeration is used as a premise, not claimed as new. Existing exact total-leaf/cycle-length enumeration covers the marginal distribution of \(J+H\); that marginal is excluded from the originality claim. Neither this marginal nor a vector of uncolored offspring degrees encodes whether individual terminal vertices attach to a cycle root, so they do not imply the two-color joint law. The inspected Ben-Naim–Krapivsky text treats evolving component counts rather than the conditional joint leaf classes. Janson's abstract concerns cycle and component-size distributions; its full text was unavailable and remains a source of historical-priority risk. No match was identified in the searches performed, which is not proof of uniqueness.

## Mathematical value — PASS

Direct-cycle pendant vertices measure one-step attachments to the two-core, while deeper leaves reflect the nontrivial attached trees. The theorem supplies the full finite joint distribution and proves that the shallow and deep counts compete, including an exact strictly negative covariance and a nonzero linear asymptotic scale. This is finer structural information than the already-known total number of leaves and applies to every admissible conditional cycle length.

## Scope and limitations

Only the conditional simple-graph model is treated; no unconditional covariance, multigraph extension, or joint central limit theorem is established. Full-text historical coverage remains incomplete for one relevant random-graph article. Finite verification does not replace the analytic proof.

Self-review: passed. Independent audit: not yet performed.
