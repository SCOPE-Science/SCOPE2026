# Independent mathematical audit

## correctness

PASS

The frozen proof uses the correct closure value H, but RESULT.md:6 incorrectly gives G and K on the generated sets without specifying closure; read literally for G(w) the former is false since the frame-valid top is not in the empty raw generator. The frozen limitations likewise incorrectly exclude monotonicity and idempotence. The replacements in repairs/3 correct these issues, preserving the witness, the original scope of the claim, and the verification front matter. Re-audit: Nishimura's Definitions 2.2–2.3 require nonempty W, finite raw generators for finiteness, and evaluate box by membership in cl(G(w)). Definition 2.5/Figure 1 require frame-valid formulas to belong to cl(G(w)) and modus ponens within cl(G(w)). On the repaired singleton frame G(w)=∅ and cl(G(w))=H=b⁻¹(1). Under the all-false valuation truth is b by Boolean induction and the box-membership clause; every frame-valid formula is thus in H. Boolean modus ponens keeps H closed. Switching to the valuation where p is true falsifies ¬p in H at the only world; the truth-set intersection in Definition 4.22 is empty, while p is not in H. Thus its implication from the subset relation to membership fails. The same calculation excludes a separation world for p. Nonemptiness makes the world bound sharp. The constant map is monotone and idempotent and fails extensivity on {p}; the repaired scope states this correctly without asserting a result under identity or extensivity. No numerical or formal certificate is needed.

## originality

PASS

Credit the finite singleton boundary and the empty raw generator, not the already-known unrestricted non-implication. The repair does not claim a new distinct theorem about monotonicity or idempotence; it accurately describes the existing witness.

## value

PASS

The witness shows that restricting to the source's finite models cannot rescue the representability implication, and sharpens the cardinality bound down to the minimum. It identifies a distinct finite obstruction: checking frame validity can use a different valuation from the one whose truth sets must represent H. This is a motivated structural boundary, even though the constant-map construction is short; it neither replaces the identity-closure example nor claims a finite H.

The dated certificate retains the supplied scientific assessment, sources and limitations.
