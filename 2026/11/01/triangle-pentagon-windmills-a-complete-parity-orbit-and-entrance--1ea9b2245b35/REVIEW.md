# Scientific review

## Correctness — PASS

The statement specifies undirected petal gluing, the open-neighborhood binary XOR update, synchronous timing, and all nonnegative parameter pairs except the empty graph. The proof reconstructs the \(\mathbb F_2\) kernel directly, identifies the even-parity image as the exact recurrent state space, proves a six-step return on that space by an order-three forcing decomposition, and solves the fixed-space equations for iterates one, two, and three. Möbius inversion then gives every primitive orbit count; the exact \(2d\)-state basin size for each length-\(d\) orbit and the sharp six-cycle criterion follow with no numerical extrapolation. Standalone tests independently establish finite agreement: 827,208 directly enumerated states across 24 graphs and 168 larger bit-vector matrix checks. The tests support, but are not substitutes for, the symbolic argument.

## Originality — PASS, qualified

The closest primary literature is Noual–Regnault–Sené (2012, arXiv:1208.2767), addressing XOR circulant networks, and Alcolei–Perrot–Sené (2015, arXiv:1510.05452), addressing asynchronous XOR flowers. Neither inspected full text supplies the two-parameter synchronous, undirected recurrence census. Aledo–Martínez–Valverde (2015) is a broader survey. Li–Zhang–Wang (2026) treats characteristic polynomials of the same graph family, but real spectral data alone do not determine characteristic-two Jordan chains or their dynamical cycle counts. Public research-record searches for petal-length aliases, period spectra, exact counts, and broader adjacency automata returned no equivalent claim; the closest records concern different graph families or local rules. Unindexed historical equivalence and incomplete full-text access to the recent spectral paper remain risks. No uniqueness or independence is inferred from database partitioning or negative searches.

## Mathematical value — PASS

The family is the natural two-petal-length extension of XOR flower networks already studied under asynchronous updates. The result gives the complete recurrent state-space structure, every possible primitive period and its exact orbit count, and a sharp minimal six-cycle motif: a single triangle plus a pentagon does not suffice, whereas two pentagons or two triangles with a pentagon do. It also establishes the full one-step entrance-time distribution and a uniform, exact orbitwise basin law for all labelled states. These are natural dynamical invariants, not arbitrary parameter slices or a recomputation of a known spectral table.

## Scope and remaining risks

The proof does not apply to directed flowers, asynchronous updates, other cycle lengths, or other coefficient fields. The 2026 characteristic-polynomial study was accessible as abstract and bibliographic information only; its uninspected sections are a named residual originality risk. No claim of first-ever appearance is made.

Self-review: passed. Independent audit: not yet performed.
