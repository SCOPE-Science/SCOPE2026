# Scientific review

## Correctness — PASS
The reversal-orbit graph recurrence is an exhaustive finite characterization: each admissible length-\(6\) window consumes exactly one of the \(28\) nonpalindromic reversal classes, and every admissible word corresponds uniquely to a legal path after fixing its initial five bits. The recurrence is justified by induction on the unused orbit count; both independent implementations enumerate the same \(22\) length-\(26\) words. A separate explicit six-orbit reduction and endpoint check establishes the remaining statements. The upper bound \(26\) is derived from the recurrence and is also independently published; the claim of new work excludes that known bound.

## Originality — PASS with residual risk
Burns–Mitchell's 1992 technical report, Section 5.2.2, Figure 7, supplies the *length* \(26\) and says an exhaustive search established it, not a full classification or symmetry census. Mitchell–Wild (2022), Section 5.3, construct *ideal* examples, but construction/existence does not imply that **every** longest admissible sequence is ideal. Gabric–Sawada (2024) study constructions and known length maxima rather than exhaustively classify linear order-\(6\) maxima. Distinct reversal-orbit paths are compared, not merely paper titles. The original 1993 printed expansion of the 1992 report was not available in full, so the possibility of an unindexed enumeration is a remaining literature risk. Search absence alone is not taken as novelty proof.

## Mathematical value — PASS
Complete extremal-object classification refines a longstanding, naturally motivated position-sensing bound: there are six genuinely different maximum designs, and every maximum design has a rigid endpoint form rather than merely admitting an ideal construction. This information is not implied by the previously tabulated optimal length and is relevant to exact finite design choice and testing. The value is deliberately finite, not claimed as a new asymptotic coding theorem.

## Limits
Binary, linear, order \(6\) only. The recurrence and code are the finite proof certificate; no external formal or independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
