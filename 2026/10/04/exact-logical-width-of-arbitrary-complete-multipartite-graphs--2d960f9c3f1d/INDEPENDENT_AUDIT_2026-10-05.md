# Independent mathematical audit

## correctness

PASS

The upper bound is valid with one reusable pool of \(M+1\) variable names: same-part equivalence is first-order definable from adjacency, transitivity needs three names, exact class size \(s\) needs \(s+1\), and exact multiplicity \(m_s\) needs \(m_s+1\) representatives while inner class-size quantifiers may shadow and release representative names lexically. For the lower bound at \(k=M\), if a part of size \(M\) exists, enlarge one such part by one vertex; otherwise add one extra part of a size already occurring in exactly \(M\) copies. In either case Duplicator's invariant in the infinite \(M\)-pebble game is sound: after a moved pebble is lifted, at most \(M-1\) vertices or relevant parts remain occupied, leaving a fresh match on the smaller side. Thus the nonisomorphic witness is \(M\)-variable equivalent. The repository checker independently verifies capped type profiles for all integer partitions through order 12 and solves representative small pebble games by greatest fixed point.

## originality

PASS

The finite-variable graph literature supplies the invariant, pebble-game characterization, and benchmark \(W(K_n)=n+1\), but the checked full survey does not state the arbitrary complete-multipartite width formula. Targeted Resultary and web searches for complete multipartite/equivalence-class size-multiplicity width found no implication-equivalent theorem. The proof uses standard finite-variable methods, so folklore equivalence-structure classifications remain a residual risk, but no checked broader result supplied this exact two-bottleneck graph invariant.

## value

PASS

Logical width is a standard finite-model-theoretic invariant, and complete multipartite graphs form a canonical graph class whose isomorphism type is exactly a multiset of equivalence-class sizes. The theorem gives a complete all-parameter evaluation and reveals two independent obstructions—largest class size and largest multiplicity—rather than a one-off small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
