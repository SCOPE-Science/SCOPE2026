# Review

## Correctness

PASS. A separating family of \(m\) unary formulas assigns each valuation an \(m\)-bit truth vector, and the induced coequivalence is exactly equality of those vectors. Hence a quotient with \(k\) classes requires \(k\le2^m\). Conversely, because every subset of the finite Boolean cube is definable in \(\mathsf{CPC}\), any injection of the \(k\) quotient classes into \(\{0,1\}^m\) can be implemented coordinate-by-coordinate by formulas. This gives the matching upper bound \(m=\lceil\log_2k\rceil\).

The bijection between CPC coequivalences and partitions of the \(2^n\) valuations yields the Bell and Stirling counts directly. The bundled finite checker independently enumerates all partitions for \(n\le3\) and reproduces the stated rank profiles.

## Originality

PASS. The closest primary result is Example 3.10 of Almeida and De Berardinis (2026), which proves that every CPC coequivalence is separating by using one indicator formula for each equivalence class. It does not optimize the number of separating formulas or count coequivalences by separation complexity.

Targeted searches for coequivalence separation rank, logarithmic quotient coding, minimal separating predicates, and Bell-number enumerations did not locate the exact \(\lceil\log_2k\rceil\) theorem or its rank distribution.

## Value

PASS. Coequivalence separation is introduced as a way of turning implicit quotients into explicit definitions. The minimum number of unary formulas is therefore a natural quantitative invariant of that explicitization. The theorem gives the exact invariant, a sharp universal \(n\)-formula bound for \(n\) propositional variables, and a complete census of quotient complexity. It improves the source construction from \(k\) class indicators to the information-theoretically optimal number of Boolean coordinates.

## Closest literature and limitations

Almeida and De Berardinis provide the qualitative CPC separation theorem and connect the notion to effective equivalence relations and uniform elimination of imaginaries. Ghilardi and Zawadowski provide the broader categorical setting.

The result does not optimize formula length and does not automatically extend beyond classical propositional logic, where arbitrary unions of quotient classes may cease to be definable.

Same-model review: passed. Independent audit: not yet performed.
