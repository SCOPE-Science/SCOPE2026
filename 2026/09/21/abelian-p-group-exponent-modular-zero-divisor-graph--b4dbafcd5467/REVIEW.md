# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The key algebraic step is valid specifically because \(G\) is
abelian. If \(e=\exp(G)=p^a\) and \(x\) lies in the augmentation ideal, the
Frobenius identity gives \(x^e=0\). Thus multiplication by \(x\) is a
nilpotent operator on the \(N=|G|\)-dimensional group algebra with all Jordan
blocks of length at most \(e\), so its kernel, which is
\(\operatorname{Ann}(x)\), has dimension at least \(N/e\).

The lower bound is sharp for \(x=g-1\) with \(o(g)=e\): multiplication by
\(g\) has \(N/e\) cycles on the group basis, and the fixed space has one
dimension per cycle. The passage from annihilator size to graph degree
correctly treats the loopless convention: a square-zero vertex has degree
\(|\operatorname{Ann}(x)|-2\), while any other vertex has degree
\(|\operatorname{Ann}(x)|-1\). When \(e>2\), the sharp element \(g-1\) is not
square-zero, and every square-zero element has annihilator dimension strictly
larger than \(N/e\). This yields the stated minimum-degree formula, including
the exceptional exponent-two case.

The graph-isomorphism consequence uses the published theorem that the finite
coefficient field, group order, and abelianness are preserved in this
setting. Equality of minimum degrees then forces equality of exponents. Over
the prime field, the published rank invariant combines with order and
exponent to identify every rank-two abelian \(p\)-group.

Small exact checks over \(\mathbf F_2\) and \(\mathbf F_3\) were consistent
with the formula for \(C_2\), \(C_4\), \(C_2^2\), \(C_4\times C_2\), and
\(C_3\); the proof does not depend on these checks.

## Originality

**PASS, to the best of our knowledge.** The 2014 paper of Aliniaeifard and Li
was inspected at its Section 3 theorem statements. It proves preservation of
the finite field and group order, preservation of abelianness, the cyclic
case, and, over the prime field, preservation of the rank of a finite
abelian \(p\)-group. It also explicitly presents the modular \(p\)-group case
as the remaining core of the isomorphism problem. No exponent invariant or
minimum-degree formula of the form proved here was found there.

Searches used exact and synonymous combinations of "zero-divisor graph",
"group ring/group algebra", "modular", "abelian p-group", "exponent",
"minimum degree", "annihilator", "rank two", and "two-generated". They did
not locate a theorem recovering \(\exp(G)\) from \(\Gamma(KG)\), nor a
rank-two modular isomorphism result obtained from order, rank, and exponent.

Later literature located in the search includes work on the annihilator graph
of group rings (a different adjacency relation) and on zero-divisor graphs of
semisimple group rings (the nonmodular setting). Neither gives the present
claim. The author's earlier thesis *Rings, Group Rings, and Their Graphs* was
also checked through its searchable text for "exponent", "minimum degree",
and "maximal order"; no matching statement was found. The thesis was not
manually inspected page by page, so it remains a minor residual source risk.

No overlapping SCOPE record was located under searches for zero-divisor
graphs, modular group algebras, abelian \(p\)-groups, exponent, or equivalent
claim language.

The main residual originality risk is that the proof is short and depends
only on standard modular-group-algebra and linear-algebra facts. An implicit
observation in a thesis, textbook, or unindexed paper may therefore exist
without using the same terminology.

## Value

**PASS.** The result adds a new group-theoretic invariant, the exponent, to
the order and rank already known to be visible in modular zero-divisor
graphs. It also turns those invariants into a complete isomorphism criterion
for all two-generated finite abelian \(p\)-groups over the prime field,
covering an infinite class beyond the previously settled cyclic case.

## Limitations

The exponent formula uses commutativity of \(KG\) and is not asserted for
nonabelian \(p\)-groups. The rank-two isomorphism corollary is stated over
\(\mathbf F_p\), matching the hypothesis of the published rank theorem.
Order, rank, and exponent do not classify finite abelian \(p\)-groups of
arbitrary rank, so the general modular isomorphism problem remains open.
