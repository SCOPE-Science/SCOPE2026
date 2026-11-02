# Scientific review: exponential rigidity for random perfect evolution algebras

## Correctness — PASS

All quantifiers are explicit: any fixed prime power \(q\ge2\), any dimension \(n\ge1\), and uniform \(M\in\operatorname{GL}_n(\mathbb F_q)\). Perfectness forces monomial automorphisms; the fixed-map equations split into permutations moving \(s\ge2\) indices and nontrivial diagonal scalings. The first family loses at least \(\lceil s(2n-s)/2\rceil\) independent matrix entries, and the second loses at least \(sn/(q-2)\) when \(q>2\). Their independent upper bounds sum to the stated \(\Delta_{n,q}\); conditioning and Burnside yield both inequalities. The exponential limit follows for every fixed \(q\). Exact tests reproduce automorphism and orbit counts in four small parameter instances, without standing in for the infinite proof.

## Originality — PASS, qualified

Wei and Zou (arXiv:2310.12368) already provide the monomial group action and a full finite-dimensional Burnside formula. They are credited and those facts are expressly excluded from the novelty claim. The new statement is the explicit exponentially small expected excess stabilizer and asymptotic class count as dimension increases with \(q\) fixed. Costoya, Mayorga, and Viruel (doi:10.1007/s00009-025-02924-0) study realizability of automorphism permutation representations; the 2026 survey (arXiv:2610.22248, Questions 21–22) identifies the random-automorphism and class-count themes. Searches under asymptotic rigidity, stabilizers, equivalent idempotent/perfect terminology, and exact orbit counting revealed no dominating published estimate. An earlier fixed-dimensional exact formula could in principle be reanalyzed to yield the same limit. Historical priority is not independently certified.

## Mathematical value — PASS

This result supplies a quantitative almost-sure rigidity theorem and explains why the established orbit-count sum has an asymptotically free leading term. It resolves a natural fixed-field specialization of a recently posed statistical automorphism problem; it is not an arbitrary small-value computation. It does not address singular structure matrices, varying \(q\), group schemes, or sharper error constants.

## Closest literature and limitations

Primary background: arXiv:2310.12368 (exact Burnside framework); arXiv:2610.22248v1 (research questions); doi:10.1007/s00009-025-02924-0 (automorphism realizations); arXiv:1312.4685 (graph framework). The first two differ from this claim by lacking the growing-dimension mean-stabilizer estimate, the key step enabling the probability and class-count asymptotics. Tests cover only prime fields and dimensions two and three, while the proof handles all prime powers and dimensions. Results remain subject to independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
