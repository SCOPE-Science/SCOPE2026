# Scientific review: exact cyclic majority stabilization-time distribution

## Correctness — PASS

The wall-bit identity \(d'_i=d_i(1\oplus d_{i-1}\oplus d_{i+1})\) is derived directly from the three-input majority truth table and is valid even for the small cyclic rings with repeated neighbors. With at least one zero wall, one-runs erode from both ends, with odd-length central walls becoming stationary. This proves the first-fixed-time formula without an unproved global convergence assumption. Parity of a cyclic XOR derivative is exactly even, and every admissible wall word has exactly two preimages. The transfer matrix recognizes exactly circular wall words with bounded one-runs; the determinant lemma and formal matrix trace identity rigorously yield the generating function. The upper bound is attained by an even-length wall run of maximal allowable length. All quantifiers cover \(n\ge1\), \(t\ge0\). A stdlib standalone verifier exhausts all words through length 16 and independently checks the transfer/determinant coefficients. Computation supports, but is not substituted for, the mathematical proof.

## Originality — PASS, with historical-priority risk

The fixed-point and two-cycle classification of synchronous majority was already known: Tosic–Agha (2004), Lemmas 3–4, explicitly give the attractor partition. Inokuchi–Sato (2000) analyze threshold-rule transients with **fixed boundaries**, not the indexed periodic-ring time distribution. Tosic (2016) computes the stable-configuration counts, which correspond to the time-zero specialization. Nakar–Ron (2022) analyze spatial structure of eventual majority configurations, not a simultaneous all-ring/time-indexed exact cumulative count. The Fuks–Gomez Soto preimage-density study concerns marginal density dynamics under product initial measures, not these circular first-fixed-time counts. None of the material actually inspected supplies the present exact family of logarithmic-derivative rational generating functions, nor does the qualitative 2004 classification imply those numerical identities without the additional wall-run and even-parity counting arguments.

A strong residual priority risk remains: Goles–Martínez (1990), *Neural and Automata Networks*, contains a highly relevant chapter, but its full text could not be inspected. Only its publisher preview and bibliographic material were available. The originality verdict is therefore a best-knowledge, qualified comparison rather than certified historical precedence; no absence assertion is made for the inaccessible chapter. Unindexed variants of the same wall-run method could also exist.

## Value — PASS

The exact first-fixed-time distribution is a natural dynamical invariant: it refines the older partition into transient/fixed/cycle states, resolves **all transient depths at every ring size**, and supplies a compact integer recurrence for its coefficients. The bound \(\lfloor(n-1)/2\rfloor\) is sharp; the parity projection retains the nontrivial cyclic constraint and excludes the alternating orbit correctly. The result is mathematically motivated independent of any numerical novelty or implementation and gives an exact finite-size relaxation law, not just a finite table or an arbitrary special case.

## Scope and limitations

This result is restricted to synchronous radius-one binary majority on labeled finite cyclic rings. It does not extend automatically to fixed boundaries, higher majority radius, multistate alphabets, or stochastic dynamics. All-length correctness follows from the proof, not from bounded enumeration. Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
