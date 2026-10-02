# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-b068c755f7ab`

## Final claim

For every visible alphabet size \(k\ge3\) and fixed hidden alphabet size \(h\ge2\), a bounded-arity hidden routing tree converts the Jirásková–Masopust finite-language projection witness to a fixed domain alphabet with the stated optimal routing overhead and an explicit exponential blow-up rate approaching the original rate as \(h\to\infty\).

## Correctness — PASS

The construction is correct. Replacing the direct hidden fan-out from the start state by an \(h\)-ary acyclic routing tree gives epsilon reachability to exactly the same original chain states after projection; fresh routing states have no visible transitions, so they do not change the projected language after the first visible symbol. A rooted deterministic router with \(J\) fresh internal vertices and \(L\) target leaves has \(J+L\) edges and at most \(h(J+1)\) outgoing hidden slots, proving \(J\ge\lceil(L-h)/(h-1)\rceil\); a partially filled \(h\)-ary tree attains it. Minimality of the input DFA follows from unique visible accepting continuations for chain states and distinct hidden path/visible continuation witnesses for routing states. Substituting \(m=\lfloor N/(\lceil\log_2 k\rceil+1)\rfloor\) and \(n=N+J\) gives the stated exponent and retained-fraction formula. The exact verifier independently checks minimality and projected transition systems on 63 parameter triples.

### Correctness sources

- assigned RESULT.md and verifier
- Jirásková–Masopust 2011 full primary paper
- finite-language NFA-to-DFA bounds

### Correctness risks

- The construction only approaches, rather than exactly attains, the old exponent for one fixed domain alphabet.
- The optimality statement is for the specified routing-only replacement model.

## Originality — PASS

The full primary projection paper explicitly says that its finite-language lower-bound construction needs a domain alphabet whose size grows linearly with the state count and leaves open whether that alphabet can be bounded by a constant. The audited routing-tree construction answers that limitation quantitatively: with a state-independent hidden alphabet it preserves the projected language exactly and retains an arbitrarily large fraction of the exponential exponent. Resultary and later projection-state-complexity searches did not locate this routing construction or its exact overhead/tradeoff.

### equivalent_formulations

Searches:
- Resultary semantic query for fixed hidden alphabet finite projection blow-up routing tree
- full-text comparison with Jirásková–Masopust Theorem 8 and its open constant-alphabet sentence

Evidence:
- The primary source states at the theorem transition that the domain alphabet is required to have linear size and that it remains open whether it can be limited by a constant.

Reasoning:
Equivalent formulations as replacing \(L\) erased fan-out letters by a fixed-arity epsilon-routing network and as constant domain-alphabet projection complexity were compared.

### broader_coverage

Searches:
- Jirásková–Masopust 2011/2012
- fixed-alphabet determinization literature
- later finite/block-language projection papers

Evidence:
- The source theorem gives the core exponential lower bound with \(L\) distinct hidden letters, but no fixed-alphabet compiler.

Reasoning:
General fixed-alphabet NFA determinization results do not mechanically preserve this particular projected finite language or its exponent.

### exact_database_or_table

Searches:
- current Resultary fixed-alphabet/projection records

Evidence:
- No exact database/table or stronger current theorem was located.

Reasoning:
The claim is constructive and asymptotic, not a table lookup.

### claim_vs_prior_implication

Searches:
- claim-versus-source implication comparison

Evidence:
- Source Theorem 8 explicitly spends one hidden symbol per fan-out target and notes constant domain size as open; an additional state-routing construction is necessary.

Reasoning:
The audited result solves a stated structural limitation rather than restating the source construction.

### source_inspections

- **State Complexity of Projected Languages** — https://users.math.cas.cz/~masopust/pubs/2011/dcfs2011.pdf. Trigger: Primary construction being compressed. Material read: Full primary paper around Sections 5–6, especially Theorems 7–8 and the statement that constant domain-alphabet size is open. Method: Primary full-text and figure/theorem inspection. Assessment: NOT COVERING the fixed-hidden-alphabet construction. Evidence: Theorem 8 uses a hidden letter \(a_\ell\) for each fan-out target and explicitly says the domain alphabet is linear in the state count and constant size remains open.
- **Assigned routing verifier** — artifacts/verify_fixed_hidden_projection.py. Trigger: Finite minimality and exact projected-language sanity checks. Material read: Complete source and deterministic output. Method: Line-by-line inspection plus reconstruction of routing counts. Assessment: Correct corroboration. Evidence: All 63 documented parameter triples reproduce the input-state count, minimality test, and projected visible transition structure.

### checked_sources

- Jirásková–Masopust 2011 full PDF
- current Resultary fixed-hidden-alphabet search
- assigned RESULT.md and verifier

### residual_risks

- A 2011 personal communication cited by the primary source is not publicly inspectable.
- Unindexed later alphabet-reduction folklore remains a residual risk.

## Scientific value — PASS

The result gives a quantitative partial solution to an explicit open limitation in a canonical state-complexity witness. The router overhead is exact in its natural model, and the construction shows that a truly fixed alphabet can retain an arbitrarily large fraction of the known exponential blow-up rate. This is a motivated structural tradeoff, not an arbitrary encoding exercise.

### Value sources

- primary source's explicit constant-alphabet question
- assigned optimal routing lemma and exponent tradeoff

### Value risks

- Exact equality with the original exponent for one fixed alphabet remains open.

## Limitations

- The fixed alphabet achieves an arbitrarily close exponent, not exact equality with the growing-alphabet witness.
- Routing optimality is asserted only in the stated root-to-target routing model.
- A cited private/personal communication remains inaccessible.

## Disposition

**PASSED**
