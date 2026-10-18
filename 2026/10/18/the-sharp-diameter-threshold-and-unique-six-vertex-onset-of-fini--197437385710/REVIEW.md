# Review of the sharp multiset-partition diameter threshold

## Correctness — PASS

For diameter at most two, every \(k\)-part partition yields at most \(k\) possible codes; the only possible resolving partition would have all vertices singleton, but then its codes are determined by positive vertex degree, which cannot be distinct at all vertices. The finite uniqueness is proved by the actual exact labelled graph-and-partition enumeration: \(12,300,12540\) diameter-three connected masks at orders four to six, and \(0,0,720\) labelled masks admitting resolving partitions. All \(720\) are explicitly checked to be isomorphic to the seven-edge witness. Its full partition enumeration gives exactly two five-part solutions and none of other sizes. Code, proof and produced output are included.

## Originality — PASS with identified risks

The 2026 original paper supplies the definition, a general bound and named infinitude cases, but its materially inspected Sections 1–4 do not give the universal diameter-two theorem or sharp unique six-vertex onset. The 2026 survey introduces the parameter without this classification. published-finding corpus and broader-source alias searches found other multiset parameters but no implication covering both clauses. Absence from inspected work is not proof of bibliographic priority; older unordered-distance-code or partition terminology is a residual risk.

## Value — PASS

The theorem gives a structural impossibility criterion across **all** connected diameter-two graphs instead of listing particular families. Its sharpness is nontrivial: the first possible finite case at diameter three occurs in just one isomorphism class at order six, and all optimal partitions are classified. The fact that the discrete refinement fails shows why unordered block-distance codes behave differently from standard ordered partition resolving codes. This is a natural boundary theorem for a new graph invariant; the finite census is a complete cutoff rather than an arbitrary isolated numeric answer.

## Scope and limits

The classification at diameter three concerns at most six vertices, not all orders. The universal impossibility proof is unrestricted for diameter one and two. The finite claim depends on a transparent complete enumeration, independently checkable from the attached standalone Python source. Definitive priority and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
