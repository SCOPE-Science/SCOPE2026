# Scientific review

## Correctness — PASS
The defining inequality for an ordinary defensive alliance on the balanced complete multipartite graph is \(s-s_i\ge\lfloor(r-1)n/2
floor\) in each occupied part. The proof separately shows why **every** nonempty proper defensive subset is impossible under the two-tight-parts criterion; this is essential because local minimality and global minimality differ for general graphs. It then constructs maximum-size examples and proves the full coefficient formula by a disjoint counting weight identity. The pure-Python graph verifier agrees with weighted profile enumeration and independently constructed alternating coefficients for 145,206 direct candidate vertex subsets in ten finite graphs; ten larger occupancy comparisons also passed. The infinite claim rests on proof, not sample checks.

## Originality — PASS with literature risk
The closest primary literature establishes the ordinary upper alliance parameter, general algorithms for globally minimal alliances, and enumerating algorithms. The closest publicly accessible complete-multipartite result treats **strong** alliances and uses a similar two-tight-parts criterion. That technique and the difference between ordinary and strong support are explicitly acknowledged. For **even** common degree the predicates coincide, so the two-tight-parts classification is already implicit in the earlier result; the new ordinary predicate arises for **odd** common degree. This finding counts **globally minimal ordinary** alliances and their exact maximum, whereas the earlier strong polynomial counts **all strong** alliances. Equivalent work indexed under critical alliances or related terms may have been missed; similarity to the strong proof is a material residual risk.

## Value — PASS
The maximum cardinality among globally inclusion-minimal defensive alliances is a studied invariant distinct from the minimum alliance number. The theorem solves it exactly on a natural infinite graph family, proves that global and local minimality coincide there, and determines every cardinality multiplicity and the number of maximum examples. These are complete structural and counting results, not just isolated numerical entries. The theorem has no claim outside equal part sizes, and no computational experiment certifies the infinite statement.

### Sources and limits
- Bazgan–Fernau–Tuza, *Aspects of upper defensive alliances* (online 2018-06-30), DOI 10.1016/j.dam.2018.05.061.
- Gaikwad–Maity, *Globally Minimal Defensive Alliances: A Parameterized Perspective*, arXiv:2202.02010.
- Feng–Fernau–Mann, *Enumerating Minimal Defensive Alliances*, arXiv:2312.11963.
- *Strong alliance polynomial of complete multipartite graphs*, public result (2026), cited fully in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
