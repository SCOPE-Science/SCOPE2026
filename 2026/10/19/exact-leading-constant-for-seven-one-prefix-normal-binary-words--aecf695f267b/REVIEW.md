# Scientific review: seven-one prefix-normal asymptotic

**Correctness — PASS.** For a length-\(n\) word with seven ones, the fifteen consecutive-gap inequalities exactly characterize 1-prefix-normality. Nonnegative internal zero gaps with sum at most \(n-7\) are in bijection with all such words. Consequently their count is an Ehrhart lattice-point function of a full-dimensional six-polytope. An exact integer/rational certificate exhausts twenty-one constraint rows, fourteen extreme rays, 155 polytope faces and 2184 simplex flags, producing volume \(289/2488320\). Direct word enumeration and independent gap enumeration agree through length seventeen. No finite sample is used to infer the all-length theorem.

**Originality — PASS, with literature risk.** Burcsi et al. [1] prove the gap criterion and general rationality and give explicit generating functions only for weights zero through six; their Section 4.2 says the cases above six resisted direct calculation. The exact seven-one volume and limiting conditional probability are not present in that source. The all-density result of Balister and Gerke [2] and later generation work [3] do not determine this exact coefficient. Searches of equivalent probability, gap-volume, Ehrhart, and fixed-density language, together with general sequence records [4], identified no broader or equivalent explicit coefficient. Unindexed equivalent prior work remains possible.

**Mathematical value — PASS.** The result addresses the first weight beyond a published exact table and produces a reproducible, exact rational asymptotic constant for a natural enumerative class. It also identifies the exact limiting fraction among words whose first symbol is one. It is not a full density-seven rational generating function or a result uniform in growing density; those remain limitations.

**References.** [1] Burcsi–Fici–Lipták–Ruskey–Sawada, arXiv:1611.09017v1, Lemma 8 and Proposition 16. [2] Balister–Gerke, arXiv:1903.07957. [3] *Generating a Gray code for prefix normal words in amortized polylogarithmic time per word*, arXiv:2003.03222. [4] OEIS A194850.

Self-review: passed. Independent audit: not yet performed.
