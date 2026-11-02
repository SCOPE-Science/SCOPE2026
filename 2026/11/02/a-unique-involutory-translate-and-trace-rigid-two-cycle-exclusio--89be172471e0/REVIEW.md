# Self-review

**Correctness — PASS.** The proof constructs an explicit exponent-inverse power permutation and derives \(F_\delta(H(u))=H(u+1)+1+\delta\). This establishes the exceptional fixed-point-free involution and permutation property without relying on finite experiments. The characteristic-two linear map \(L(u)=u+u^{2^d}\) has kernel \(\{0,1\}\) and trace-zero image because \(\gcd(d,m)=1\); this gives the exact fixed-point counts. For every period-dividing-two point, the second-iterate calculation forces a fiber collision \(L(v)=L(u)\), allowing only a fixed point or the exceptional shift. The argument treats zero, \(m=3\), all \(\delta\), and quantifiers explicitly. Finite-field checks across six odd degrees agree but are not an infinite proof.

**Originality — PASS, with risk.** The motivating paper, Ding et al., arXiv:1402.5734v1, Theorem 1 and its concluding section, establishes that the unshifted trinomial is a permutation. Material inspected does not state its additive translates' least-two-period counts or the unique involution phenomenon. Related permutation-trinomial and involution work found by targeted searches has distinct maps or hypotheses; accessible research records found no equivalent statement. An as-yet-unlocated classical power-conjugacy identity could imply the claim, and the search cannot prove uniqueness in all literature.

**Mathematical value — PASS.** This is an exact complete local dynamical classification of a natural one-parameter family attached to a published finite-field permutation polynomial: among \(q\) translates there is one with \(q/2\) disjoint transpositions, while all other translates have no transpositions at all, and their fixed points obey a sharp trace law. The jump from no two-cycles to every point two-periodic is structurally meaningful and not merely a small sample or arbitrary parameter slice.

**Limits.** Longer periods, even extension degrees, and unrelated polynomial families are unclassified. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
