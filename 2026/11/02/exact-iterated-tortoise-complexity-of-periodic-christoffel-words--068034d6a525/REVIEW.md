# Scientific review

## Correctness — PASS

A complete proof supplies three independent structural steps: preservation of binary prefix-count dominance under every tortoise iterate (proved from the ordered one-position lists), a complete rational rotation-phase cell description, and a necessary-and-sufficient criterion for each collision between neighboring cells. Monotonicity makes every image fiber a consecutive cell interval; the collision criterion reduces the deficit to positive nonmultiples of the period in one explicit bounded interval. A separate modular argument shows the cutoff parameter is never divisible by the period, establishing the sharp last collision. The proof covers arbitrarily large iteration counts, including those that sort every one. A standalone verifier checked 49,750 exact parameter cases and the published code reproduces the count.

## Originality — PASS, residual priority risk

Campbell–Rampersad (arXiv:2604.25811, Sections 3–4, 7) defines tortoise complexity and treats automatic sequences but does not present an all-iterate rational mechanical-word law. Carey–Clampitt (arXiv:1804.08724, Sections 1–2) establishes Christoffel adjacency and partition-variety results under a different equivalence relation; it does not count iterated tortoise fibers. The existing exact one-step Christoffel formula is *explicitly acknowledged* as already covered and is not the novelty claim. Likewise, the known all-iterate formula for irrational Sturmian words does not entail the rational-periodic modular exclusion or the sharp injectivity threshold because their length-n factor languages differ at the period. Earlier independent unindexed coverage remains possible.

## Value — PASS

The study of tortoise complexity explicitly motivates mechanical/Sturmian variations. The result completes the rational Christoffel problem for **all** iteration counts and lengths, giving an exact modular arithmetic law, a general order-preservation mechanism and a sharp final collision length. The oscillations depend on divisibility by the primitive period and cannot be inferred by merely extending a one-step linear branch. This supplies a meaningful rational-versus-irrational boundary and a reproducible benchmark for sorting equivalence on periodic words.

## Scope and risks

The theorem is confined to reduced rational mechanical periods and binary tortoise. It does not give an arbitrary-period theorem, nor an external novelty or correctness certificate. The one-step specialization and its known threshold are not asserted as newly discovered results.

Self-review: passed. Independent audit: not yet performed.
