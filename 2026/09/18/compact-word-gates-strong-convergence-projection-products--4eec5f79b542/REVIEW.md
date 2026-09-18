# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The proof reduces the problem to the orthogonal complement of the common
intersection. Since \(M\subseteq\mathcal R(P_j)\), one has
\(P_jP=P=PP_j\), so \(M^\perp\) is invariant under every factor and
\(PT_n=P=T_nP\). Hence for \(y=(I-P)x\), the assumed weak convergence is
\(T_ny\rightharpoonup0\), while \(\|T_ny\|\) is nonincreasing.

At an endpoint of a recurrent word \(\omega\),
\[
T_{b_k}y=WT_{a_k}y=(W-P)T_{a_k}y.
\]
The vectors \(T_{a_k}y\) are bounded and weakly null. Compactness of
\(W-P\) therefore forces \(T_{b_k}y\to0\) in norm. Monotonicity then forces
the whole norm sequence to tend to zero. This establishes strong
convergence without an unproved compactness inheritance step.

For the finite-excess corollary,
\(P_j-P\) is exactly the orthogonal projection onto
\(\mathcal M_j\cap M^\perp\), so finite-dimensional excess is equivalent to
finite rank of that reduced projection. The 2026 definition of an
infinite-periodic selection requires each index to occur infinitely often,
so the one-letter compact gate recurs.

The two-letter example was checked blockwise. With
\(F_n=\operatorname{span}(c_ne_n+s_nf_n)\), the operator \(Q_EQ_F\) on the
\(n\)-th two-dimensional block has singular values \(c_n,0\). Thus
\(Q_EQ_F\) is compact when \(c_n\to0\), while both \(Q_E\) and \(Q_F\) are
infinite-rank projections and are noncompact. Also \(E\cap F=\{0\}\), so
the stated common intersection is correct.

## Originality

The claim is qualified **to the best of our knowledge**.

Eskandari--Moslehian arXiv:2609.13957v1 was inspected at theorem level.
Theorem 2.12 proves weak convergence for infinite-periodic selections.
Corollary 3.3 obtains strong convergence from positivity of a subsequence of
partial products. Searches of the full text found no occurrence of
"compact", "finite-dimensional", or "Calkin".

Their earlier arXiv:2405.04848v2 was inspected around the strong-convergence
section. Lemma 2.14 states that weak convergence plus an already strongly
convergent subsequence implies full strong convergence; Theorem 2.16 uses a
finite-family angle condition and a monotonically decreasing tail. The
present contribution is the compact recurrent-word mechanism that
produces such a strong subsequence and, via the new infinite-periodic weak
theorem, gives a countably infinite strong-convergence criterion.

The closest classical compactness precedent found is Dye--Khamsi--Reich
(1991): for a finite number of suitable contractions, one compact
contraction yields uniform convergence. Dye (1989) likewise concerns a
finite set of compact contractions. The accessible statements do not give
the present condition that a recurrent *word*, rather than a generator,
equals the common-intersection projection modulo compacts, nor its
application to the countably infinite infinite-periodic setting.

Pustylnik--Reich--Zaslavski (2011--2012) give noncyclic/nonperiodic
strong-convergence criteria based on angles and inclination of finite
tuples. Their 2012 abstract and the way the result is used in
arXiv:2405.04848 were inspected, but the complete theorem-level contents of
all older papers in that line were not exhaustively checked. Dye's 1989
paper was also not fully inspected beyond its accessible abstract and
bibliographic description. These are the main residual originality risks:
a differently phrased compact-semigroup special case in the older
finite-family literature could overlap a finite-family restriction of the
theorem. No inspected source supplied the countably infinite recurrent-word
criterion or the strict two-letter compact-modulo-\(P\) example.

Repository searches by random projection products, infinite-periodic
strong convergence, compact gates, finite excess, recurrent words, Calkin
projection products, and the source identifier found no prior SCOPE record
covering this claim.

## Value

The result converts a newly available weak-convergence theorem for
countably many projections into strong convergence under an operator-ideal
condition that is easy to verify geometrically: one recurrent subspace may
have finite-dimensional excess over the common intersection.

The multi-letter formulation is more reusable than that corollary. A
finite product can collapse to the common-intersection projection modulo
compacts even when every individual reduced projection is noncompact. The
explicit two-subspace block construction demonstrates that this is a
genuine phenomenon rather than a reformulation of "one compact
projection".

The Calkin-algebra formulation isolates the mechanism succinctly:
recurrence supplies repeated compact gates, while weak convergence supplies
weakly null inputs to those gates.

## Scope and limitations

This is a sufficient criterion, not a necessary one. It does not classify
all infinite-periodic controls with strong convergence, does not give a
rate, and does not assert operator-norm convergence. For multi-letter
gates the ordered word must actually recur consecutively. The result is
stated for orthogonal projections; no extension to arbitrary oblique or
nonlinear projections is claimed.
