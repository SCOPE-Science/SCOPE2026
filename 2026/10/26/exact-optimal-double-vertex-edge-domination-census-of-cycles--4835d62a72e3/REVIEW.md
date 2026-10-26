# Scientific review

## Correctness
PASS. The closed-edge-neighborhood condition is reduced exactly to every four consecutive cycle positions having at least two selected vertices (for lengths at least five). Counting incidences proves the cardinality lower bound and an alternating construction attains it. At equality, positive cyclic gaps obey adjacent-sum at most four. The resulting alphabet \(\{-1,0,1\}\), a local exclusion of negative neighbors, and total signed excess \(0\) or \(1\) rigorously force precisely the classified structures. Marked-vertex counting gives the closed formula; the small cycles are separately checked. Direct graph enumeration through length 18 and independent eight-state weighted-trace enumeration through length 80 agree, but are supplementary to the proof.

## Originality
PASS under accessible evidence, with residual priority risk. The parameter was introduced in 2017, and its general \(k\)-fold form was studied in 2023; the scalar cycle minimum is not claimed as novel. The theorem instead determines every minimum set, its gap pattern, exact labeled count, and rotation orbit. The 2023 source's actual introduction, theorem structure, tree algorithm, hardness sections and conclusion were inspected without finding such a result. Related publications on double edge-vertex domination reverse the selected-object type. Search of mathematical result records, cyclic four-window formulations and cycle-specific literature produced no equivalent complete census. The 2017 primary article's abstract and metadata were available, but the full text was inaccessible; that source remains a genuine priority risk rather than being declared not covering.

## Value
PASS. For a standard fault-tolerant vertex-to-edge covering constraint on a cycle, the count and complete structure of *all* cheapest protections matter independently of finding a single optimum. The exceptional six-versus-two even-cycle counts and the \(n\lfloor(n+3)/4\rfloor\) odd-cycle count are explained by a forced alternating defect run, producing a precise classification of the optimum landscape and its symmetries, not a normalization trick or a tiny numerical improvement.

## Literature and limitations
Closest sources: Krishnakumari--Chellali--Venkatakrishnan (2017), DOI `10.1142/S1793830917500458`; Bhattacharya--Paul (2023), arXiv:`2310.07452`; Miao et al. (2019), DOI `10.3390/math7111010`. The 2017 full-text access limitation is unresolved, and unindexed literature may overlap. The claim covers simple cycles and only the minimum layer; the full feasible-set polynomial is not determined.

Self-review: passed. Independent audit: not yet performed.
