# Scientific review

## Correctness — PASS

The listed family contains 34 distinct triples on the 16-point set. The checker verifies that all 102 unordered pairs are distinct, so the family is a partial Steiner triple system. It identifies four pairwise disjoint blocks and exhaustively checks all \(\binom{34}{5}=278256\) five-block subfamilies, finding none with 15 distinct vertices. Therefore its maximum partial parallel class is exactly four. The point-degree bound gives \(3B\le16\lfloor15/2\rfloor=112\), hence \(B\le37\) for any packing on 16 points.

## Originality — PASS, with residual risk

The closest direct record, `2026/9/9/SCOPE045`, establishes a 33-block lower bound and the 37-block ceiling, and explicitly leaves 34–37 unresolved. The new explicit 34-block family improves that lower bound. Stinson's general bounds do not imply this witness. The inspected enumeration paper on maximum partial triple systems on 16 points does not report maximum partial parallel class sizes. Searches used beta(4,16), PSTS(16), maximum partial parallel class four, five pairwise disjoint triples, and full-parallel-class-free packings; no prior 34-block witness or stronger exact value was returned. This is not a proof of bibliographic uniqueness.

## Mathematical value — PASS

The parameter \(\beta(4,16)\) is a natural finite extremal invariant of partial Steiner triple systems. Improving its best recorded constructive lower bound from 33 to 34 narrows the unresolved interval from \([33,37]\) to \([34,37]\) with a reproducible explicit witness. The result is intentionally limited to a lower-bound improvement; it does not claim the exact extremal value.

## Closest literature and limitations

The primary context is Stinson's general study of partial parallel classes. Demirkale–Donovan–Grannell enumerate maximum partial triple systems on 16 points, but their inspected tables concern structural counts rather than maximum partial parallel classes. The public 33-block record is the direct comparator. No independent audit or independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
