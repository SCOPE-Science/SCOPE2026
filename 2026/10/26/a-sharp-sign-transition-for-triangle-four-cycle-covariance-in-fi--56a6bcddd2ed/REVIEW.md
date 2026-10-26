# Scientific assessment

## Correctness — PASS

For \(G(n,m)\), a prescribed \(j\)-edge event has probability \((m)_j/(M)_j\). Among triangles relative to one fixed four-cycle, exactly four share two edges, \(4(n-4)\) share one, and the remainder share zero. This yields the displayed exact covariance identity for arbitrary \(n\) and \(m\). Algebraic factoring produces the claimed formula, and positivity of the remaining factors reduces the complete sign law to a one-dimensional affine comparison. The \(n=4\) cancellation is explicitly handled. An independent exhaustive graph-level enumerator and symbolic check pass. Finite tests supplement, rather than replace, the arbitrary-parameter proof.

## Originality — PASS, with residual priority risk

Queries for fixed-edge triangle/four-cycle covariance, its mixed factorial moments, threshold aliases, and relevant published findings did not identify this specific all-parameter signed formula. Stark–Wormald (arXiv:1608.05193v1) treat nonexistence probabilities for one prescribed subgraph in \(G(n,m)\); Sah–Sawhney (arXiv:2006.11369v1) treat local limit theorems for individual subgraph counts; Drmota–Ramos–Rué (arXiv:1512.08889v1) treat a different restricted graph class. The closest historical findings concern triangles versus graph-component statistics or versus isolated-edge components, not counts of four-cycles. Classical overlap counting could yield a precursor mixed moment, so an uninspected earlier formula remains the main historical-priority risk; searches do not certify uniqueness.

## Mathematical value — PASS

The sharply changing covariance sign concerns two fundamental motifs under the canonical fixed-edge random-graph null. The result resolves the sign for every graph order and every edge count, identifies an exact interior zero at \((n,m)=(5,8)\), and shows a universal four-to-five-edge sign reversal for all \(n\ge9\). Conditioning on the edge count makes the dependence genuinely different from the nonnegative motif covariance in independent-edge \(G(n,p)\). The classification is not a routine reparametrization of an existing all-density sign theorem in the sources checked.

## Evidence and limits

The checker enumerates all \(33{,}856\) graphs on four, five, or six vertices, makes 138 exact moment and symbolic-identity checks, and runs finite sign crosschecks up to 50 vertices. The mathematical proof covers all orders. The closest literature was compared by actual statement and graph model, and the older Kim–Vu paper was available only at abstract level; an unseen general mixed-moment identity might anticipate part of the finding. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
