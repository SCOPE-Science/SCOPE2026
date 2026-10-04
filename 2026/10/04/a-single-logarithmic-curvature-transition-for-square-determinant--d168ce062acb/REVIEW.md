# Same-model review

## Correctness
PASS. Starting from the published product for \(D_{n,r}\), the proof cancels adjacent-rank products explicitly and obtains
\[
\frac{D_{n,r-1}D_{n,r+1}}{D_{n,r}^{2}}
=
\frac{r(2n-r)}{4(2(n-r)-1)(2(n-r)+1)}.
\]
The sign comparison is then exactly equivalent to \(17(n-r)^2\gtreqless n^2+4\). The checker replays all product identities for \(2\le n\le40\) and the sign transition through \(n=1000\). No finite experiment is used as a substitute for the uniform proof.

## Originality
PASS. Friedland--Krattenthaler give the determinantal degree product, parity questions, and a boxed-plane-partition interpretation, but not the adjacent-rank curvature quotient or its one-switch threshold. Scientific searches for determinantal-degree log-concavity, rankwise degree curvature, boxed-plane-partition shape log-concavity, and the resulting negative Pell equality did not locate an equivalent or stronger statement. Harris--Tu is the foundational formula source, but the repository full text was inaccessible during this review; this remains a stated residual literature risk rather than being treated as evidence of novelty.

## Value
PASS. Rank is the defining stratification parameter for determinantal varieties, and projective degree is a basic enumerative invariant. The result gives a complete, exact second-order profile of that invariant across the whole square rank stratification, including a universal transition fraction and a Diophantine description of equality. This is substantially more informative than recomputing isolated degrees or giving a finite table.

## Closest literature and limitations
The closest inspected full text is Friedland--Krattenthaler, arXiv:math/0508498, whose formula (1.2) is the precise input. Their stated goals are parity of determinantal degrees and real rank consequences. The Harris--Tu article is foundational but was not available through the checked repository endpoint. Work on log-concavity of the ordinary plane-partition function concerns variation by volume, not variation of the containing box shape \((n-r)\times(n-r)\times r\).

Same-model review: passed. Independent audit: not yet performed.
