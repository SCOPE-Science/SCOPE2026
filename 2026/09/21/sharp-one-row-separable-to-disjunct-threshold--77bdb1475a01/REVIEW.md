# Same-model review

## Correctness

**PASS.** The construction has \(2d+1\) columns, so exact \((2d-1)\)-separability reduces to distinguishing the omitted pair. Private rows identify all omitted ordinary columns. The only remaining ambiguity, when exactly one ordinary column is omitted, is resolved by the corresponding row supported on \(\{C,A_i\}\) or \(\{C',D_j\}\). This proves exact \((2d-1)\)-separability for every \(d\ge2\).

The one-row obstruction is exact. The cover \(C\le A_1\lor\cdots\lor A_d\) can be broken by a new row only if the new entry at \(C\) is 1 and all new entries at \(A_i\) are 0. The cover \(C'\le C\lor D_1\lor\cdots\lor D_{d-1}\) can be broken only if the new entry at \(C'\) is 1 while the new entry at \(C\) and all \(D_j\) is 0. These requirements contradict each other at \(C\), so one added row cannot produce \(d\)-disjunctness. Two rows supported only on \(C\) and \(C'\), respectively, give every column a private row and therefore produce \(d\)-disjunctness. Hence the augmentation number is exactly two.

The global frontier follows from a separate elementary monotonicity fact: exact \(s\)-separability with more than \(s\) columns implies exact \(t\)-separability for every \(t<s\). Chen--Hwang therefore gives a one-row \(\lfloor s/2\rfloor\)-disjunct completion. For odd \(s=2d-1\), \(M_d\) rules out guaranteeing \(d\); for even \(s=2d\), \(M_{d+1}\) is already exact \(2d\)-separable and rules out guaranteeing \(d+1\). Thus \(G(s)=\lfloor s/2\rfloor\).

The accompanying verification program constructs the matrices and exhaustively checks every possible single appended binary row for \(d=2,\ldots,6\). These computations agree with the general proof.

## Originality

**PASS, to the best of our knowledge.** Chen and Hwang's 2007 theorem states that exact \(2d\)-separability permits conversion to \(d\)-disjunctness by adding at most one row, and the surrounding discussion explicitly leaves room for improving the quantitative link. Their 2009 follow-up treats an error-tolerant extension. Aldridge, Baldassini and Gunderson later restate the \(2k\)-to-\(k\) one-row theorem as the standard connection used in asymptotic work.

Searches covered exact separability, union-free families, disjunct matrices, cover-free families, superimposed codes, one-row and one-test augmentation, the phrases \(2d-1\) and \(2d\), the Chen--Hwang title and DOI, and later papers and surveys through 2026. No source located gives the present infinite family, states that exact \(2d\) is sharp for a one-row \(d\)-disjunct upgrade, or states the exact frontier \(G(s)=\lfloor s/2\rfloor\).

The primary 2007 theorem statement and its surrounding motivation were inspected in accessible indexed text; a direct repository rendering of that PDF was not available during this review. This leaves limited residual uncertainty about material elsewhere in the short paper, although later literature independently restates the same theorem. A broader residual originality risk remains because the elementary obstruction could have appeared under set-system or superimposed-code terminology without being indexed to the Chen--Hwang transformation. No concrete source suggesting such prior coverage was found.

## Value

**PASS.** The result determines the exact worst-case one-row conversion frontier between two standard nonadaptive group-testing design notions. It is an infinite-family impossibility result, not a single small parameter example, and it shows that the factor-two loss in the Chen--Hwang connection is unavoidable without extra hypotheses. The same obstruction also blocks the corresponding one-row upgrade to \(\overline{d+1}\)-separability.

## Scientific limitations

The theorem is specific to binary noiseless matrices and a one-row conversion guarantee. It does not optimize the number of rows in the witness matrices, classify extremal examples, or settle error-tolerant analogues. The conclusion is worst-case; additional hypotheses may permit stronger conversions.

Same-model review: passed. Independent audit: not yet performed.
