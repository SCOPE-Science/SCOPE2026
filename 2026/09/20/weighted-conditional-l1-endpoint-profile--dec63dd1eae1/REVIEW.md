# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The starting identity is exact:
\[
\|M_wEM_uf\|_1
=\int E(|w|)|E(uf)|\,d\mu
=\|E(E(|w|)uf)\|_1.
\]
With \(q=E(|w|)\), the conditioning sigma-algebra decomposes into its
non-atomic part \(B\) and its atoms \(A_n\).  On \(A_n\), the operator is
rank one and its norm is exactly
\[
q_n\|u\chi_{A_n}\|_\infty.
\]
This is the key endpoint quantity: the dual of \(L^1(A_n)\) is
\(L^\infty(A_n)\), so the norm of
\(f\mapsto\int_{A_n}uf\) is the essential supremum of \(u\), not its
conditional average.

The approximation-number upper bound is obtained by deleting all but fewer
than \(k\) atomic blocks.  The remainder is an \(\ell_1\)-direct sum, hence
has norm equal to the largest remaining block norm or the non-atomic block
norm.

For the Bernstein lower bound, the atomic case uses \(k\) disjoint
near-norming vectors.  In the non-atomic case, for any
\(t<\|qu\chi_B\|_\infty\), the measure
\[
\nu(C)=\mu(C\cap\{|qu|>t\}),\qquad C\in\mathcal A|_B,
\]
is absolutely continuous with respect to a non-atomic measure and is itself
non-atomic.  It can therefore be split into \(k\) disjoint positive pieces.
Phase-adjusted \(L^1\) unit vectors on those pieces have disjoint images and
give a uniform lower bound \(t\).  This verifies the exact
\(a_k=b_k\) formula without a hidden complementability assumption.

The infinite version of the same construction produces disjoint normalized
vectors spanning an isometric \(\ell_1\).  The projection
\[
Ph=\sum_j\left(\int hg_j\,d\mu\right)f_j
\]
has norm at most one when \(g_j\) are norm-one biorthogonal functions on the
disjoint supports.  Thus the claimed complementability is explicit, rather
than inferred from an unconditional basis.

The nuclear upper bound is the explicit atomic rank-one expansion.  For the
lower bound, compress to finitely many atomic blocks using an isometric
embedding \(J:\ell_1^F\to L^1\) and a contraction
\(Q:L^1\to\ell_1^F\).  The finite-dimensional compression is diagonal with
entries arbitrarily close to the \(c_n\).  The ideal property of the nuclear
norm and the trace pairing with the norm-one identity give
\[
\|T\|_{\mathcal N}\ge\sum_{n\in F}c_n.
\]
Exhaustion by finite \(F\) gives the exact nuclear norm.

The two explicit stress tests were checked directly:
(1) conditional expectation onto the trivial sigma-algebra on a non-atomic
probability space is rank one; (2) in the block-counting example with
\(|A_n|=2^n\), \(u(a_n)=2^n\) and \(w|_{A_n}=2^{-n}\), the operator is an
isometry on the distinguished coordinate copy of \(\ell_1\).

## Originality

**PASS, to the best of our knowledge.**  Estaremi--Jabbarzadeh (2013),
Theorem 2.7, states an \(L^1\) compactness criterion in terms of finitely
many \(\Sigma\)-atoms.  The trivial-conditioning rank-one example contradicts
that statement as written.  Estaremi (2014) presents the same endpoint
criterion by a different proof.

Al Ghafri--Shamsigamchi--Estaremi, arXiv:2602.19105v1 (2026), Proposition
2.6 and Theorem 2.9, use the average-based series
\[
\sum_n E(|w|)(A_n)E(|u|)(A_n)
\]
for \(L^1\) nuclearity.  In the displayed proof of Proposition 2.6 the
functional
\[
\phi_n(f)=\int_{A_n}uf\,d\mu
\]
is estimated by \(E(|u|)(A_n)\); its exact \(L^1\)-dual norm is instead
\(\|u\chi_{A_n}\|_\infty\).  The finite-block counting example in RESULT.md
satisfies the average criterion while the operator fixes a complemented
copy of \(\ell_1\), so the criterion cannot hold as written.  The same
example also contradicts the compactness statement of Theorem 2.5.

Searches around weighted conditional expectations, Lambert-type operators,
compactness, essential norms, strict singularity, approximation numbers and
nuclearity did not locate the corrected all-\(k\) profile or exact nuclear
norm.  The principal residual risk is older general Banach-lattice work on
multiplication--conditional-expectation operators: it may encode parts of
the direct-sum mechanism under different terminology, even though an
equivalent endpoint theorem was not located.

## Value

**PASS.**  This is not only a correction of one threshold.  A single
endpoint invariant determines the complete approximation/Bernstein profile,
the exact distance to three operator ideals, the sharp compact/FSS/SS
boundary, a complemented-\(\ell_1\) obstruction, and the exact nuclear norm.
The counterexamples are elementary and reusable, making the source of the
endpoint failure transparent.

## Scientific limitations

The theorem is specific to \(L^1(\Sigma)\to L^1(\Sigma)\).  It does not
replace the distinct \(1<p<\infty\) theory, where conditional \(L^{p'}\)
moments rather than \(L^\infty\) block norms naturally occur.

Originality remains to the best of our knowledge.  The general papers on
operators representable as multiplication--conditional-expectation
operators and older Banach-lattice treatments were identified as the most
plausible source of an equivalent abstract reformulation; no such
formulation was located in the inspected statements and literature trail.
