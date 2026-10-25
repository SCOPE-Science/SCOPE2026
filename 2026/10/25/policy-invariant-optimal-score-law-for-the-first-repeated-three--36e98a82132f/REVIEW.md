# Scientific review

## Correctness — PASS
The claim is a finite, fully specified 90-word model. Conditioning on any feedback history produces a uniform posterior on the surviving words. The proof independently maximizes the unnormalized first moment, then minimizes/maximizes each future-score coefficient across *every* such expectation-optimal decision. The two polynomial extremal vectors agree componentwise at the root. The exact 11,867-state recurrence and a separate forward enumeration over 90 complete decks both pass; this proves all-policy invariance, not merely one example. Its only boundary is this exact finite composition.

## Originality — PASS on compared sources
The value \(271/90\) of the optimal mean is **known** to four decimal places (Diaconis–Graham–Spiro, Table 2) and is not the asserted new component. Their published table, the Diaconis–Graham–He–Spiro paper, and the 1981 foundational paper give mean or structural results but not the coefficientwise comparison proving that all mean-optimal policies have the same six-point score law. The published-finding corpus comparison found no matching claim. Earlier dissertations, unpublished numerical tables, and software remain residual priority risks. An algorithm capable of computing the mean is not itself a published assertion of distributional invariance.

## Value — PASS
This is the smallest balanced repeated deck in which three types cause a genuinely ambiguous incorrect guess, unlike binary decks. The complete optimal score law answers a natural risk-sensitive question left by the mean-only tables: all optimal controls have the same tail probabilities and variance, and each attains at least two hits on *every* six-card word. The result is an exact natural finite classification, not an incremental correction to the known expectation or an arbitrary parameter slice.

## Limits
No larger-composition statement; no independent expert audit or certification. Historiographic priority remains partly uncertain.

Self-review: passed. Independent audit: not yet performed.
