# Fixed-composition concept lattices: optimal one-pass bases and all-interval Möbius values

## Finding

**Theorem.** Fix an integer \(q\ge3\) and positive integers \(m_1,\ldots,m_q\), and set \(n=\sum_{a=1}^q m_a\). Let \(\mathcal W_{\mathbf m}\) be the set of words \(f:[n]\to[q]\) in which color \(a\) occurs exactly \(m_a\) times. Form the formal context with objects \(\mathcal W_{\mathbf m}\), attributes \(E=[n]\times[q]\), and incidence \(f\,I\,(i,a)\) iff \(f(i)=a\). Write \(c(S)\) for the intersection of the literal sets of all objects containing \(S\), interpreting the empty intersection as \(E\).

The family has the following complete classification, sharp basis formula, and Möbius formulas.

**Closure.** A feasible partial word \(S\subseteq E\) has no two labels at the same position and contains at most \(m_a\) occurrences of each color \(a\). Put \(s_a=|S\cap([n]\times\{a\})|\) and \(r_a=m_a-s_a\). When at least two \(r_a\) are positive, \(c(S)=S\). When exactly one is positive, \(c(S)\) is the unique complete word extending \(S\). When all are zero, \(S\) is complete and closed. For any infeasible \(S\), \(c(S)=E\). Thus the closed sets are \(E\), all complete words, and feasible partial words leaving at least two colors unfinished.

**Sharp implications.** The inclusion-minimal nonclosed sets, which are also precisely the Duquenne–Guigues pseudo-intents, are exactly:

1. \(\{(i,a),(i,b)\}\) for a position \(i\) and distinct colors \(a,b\).
2. \(\{(i,a):i\in J\}\), where \(|J|=m_a+1\).
3. Partial words with exactly \(m_b\) occurrences of every color \(b\ne a\) and no occurrence of color \(a\), for one omitted color \(a\).

For each such premise \(P\), use the multi-conclusion implication \(P\to c(P)\setminus P\). These rules compute \(c(S)\) from every initial \(S\) in one simultaneous pass; among **all** sound and complete implication bases with multi-attribute conclusions, including unrestricted iterative bases, their number is minimum and equals

\[
 b(\mathbf m)=n\binom q2+\sum_{a=1}^q\binom n{m_a+1}+q\frac{n!}{\prod_{a=1}^q m_a!}.
\]

**Exact lattice size.** Put \(M=n!/\prod_a m_a!\). The number of closed sets is

\[
 |\mathcal L_{\mathbf m}|=1+
 \sum_{0\le s_a\le m_a}\frac{n!}{(n-\sum_as_a)!\prod_as_a!}
 -M\sum_{a=1}^q(2^{m_a}-1).
\]

More precisely, their literal-cardinality enumerator is

\[
 t^{nq}+\sum_{0\le s_a\le m_a}
 \frac{n!\,t^{\sum_as_a}}{(n-\sum_as_a)!\prod_as_a!}
 -M\sum_{a=1}^q\sum_{j=0}^{m_a-1}\binom{m_a}{j}t^{n-m_a+j}.
\]

**Every Möbius value.** Let \(S\subseteq T\) be closed sets, and suppose first that \(S\ne E\). If \(T\ne E\) is a noncomplete feasible partial word, then

\[
 \mu(S,T)=(-1)^{|T|-|S|}.
\]

If \(T\ne E\) is a complete word, define the residual quotas \(r_a=m_a-s_a\), \(r=\sum_ar_a\), and \(s=|\{a:r_a>0\}|\). For \(S\ne T\),

\[
 \mu(S,T)=(-1)^r(1-s),
\]

and \(\mu(T,T)=1\). Finally, for every feasible closed \(S\), with residual quotas \(r_a\) as above,

\[
 \mu(S,E)=-\sum_{0\le t_a\le r_a}(-1)^{\sum_at_a}
 \frac{r!}{(r-\sum_at_a)!\prod_at_a!}.
\]

In particular, the last formula remains valid for a complete word, where it gives \(-1\). Also \(\mu(E,E)=1\).

## Assumptions and scope

All colors have positive prescribed multiplicity, and \(q\ge3\) is essential for the displayed minimal-premise classification. Positions and colors are labeled. A literal is a positive assertion of one color at one position; no negated literals occur. Multi-conclusion implication count means one rule per distinct premise, without counting individual output literals. A simultaneous pass fires only rules whose antecedents are already present in the **initial** set, not conclusions generated during that pass. The Möbius function is that of the closed-set lattice ordered by inclusion, with top \(E\). A feasible partial word need not be closed.

## Proof

**1. Feasibility and closure.** Two labels at one position contradict functionality; more than \(m_a\) appearances of color \(a\) contradict its quota. Conversely, a partial word avoiding both violations extends to a complete word: distribute the remaining multiset of exactly \(r_a\) copies of each color over its unassigned positions. At any given unassigned position, every color with \(r_a>0\) can be placed there in some completion. Thus with at least two unfinished colors no new literal is shared by all completions; with one unfinished color all remaining positions are forced, and with none the word is complete. Contradictory premises have no model and closure \(E\).

**2. Minimal nonclosed premises.** A minimal contradiction consists either of two different literals at the same position or of one color appearing \(m_a+1\) times at distinct positions. Since \(q\ge3\), every proper subset of either form is closed: a proper subset of an over-quota set can leave at least two other colors with positive residual quotas, and a singleton leaves at least two unfinished colors. A compatible partial word is nonclosed precisely when only one color \(a\) has positive residual quota. If it is minimal nonclosed, it must contain no \(a\)-literals and must saturate every other color: deleting one of the already-assigned literals makes a second color unfinished. Conversely, every such full-other-colors stem is minimal nonclosed. These are all cases.

A pseudo-intent is a nonclosed \(P\) such that every strictly smaller pseudo-intent \(Q\) has \(c(Q)\subseteq P\). Every minimal nonclosed set is a pseudo-intent. Conversely, any other inconsistent nonclosed set contains a proper minimal inconsistent premise \(Q\), with \(c(Q)=E\not\subseteq P\); any other compatible nonclosed set contains a proper omitted-color stem \(Q\) with \(c(Q)=c(P)\not\subseteq P\). Hence no other pseudo-intents occur.

**3. Optimality and directness.** For any inclusion-minimal nonclosed \(P\), no nontrivial sound implication whose premise is properly contained in \(P\) can add an attribute when started from \(P\): all those smaller premises are closed. Consequently, any complete implication base must contain a useful implication with antecedent exactly \(P\); distinct minimal nonclosed sets require distinct rules. The three families contain respectively \(n\binom q2\), \(\sum_a\binom n{m_a+1}\), and \(qM\) members. For directness, an inconsistent set contains a minimal inconsistent premise and one pass adds \(E\); a compatible nonclosed set contains the omitted-color stem whose closure is the same unique complete word. Closed sets trigger no nontrivial additions. So the displayed base attains its universal lower bound and works in one pass.

**4. Closed-set counting.** For feasible partial words with exactly \(s_a\) occurrences of color \(a\), choose disjoint labeled position sets: their number is \(n!/(n-\sum_as_a)!\prod_as_a!\). For each omitted color \(a\), feasible but nonclosed partial words saturate every other color and assign \(j\) positions to \(a\), for \(0\le j<m_a\). Their number is \(M\binom{m_a}{j}\). The omitted color is unique, so the families are disjoint. Subtract them, and add the infeasible top \(E\). Recording the number of assigned literals proves the polynomial as well.

**5. Möbius intervals.** We use an elementary closure-inversion identity. For closed \(S\subseteq T\),

\[
 \mu(S,T)=\sum_{U\subseteq T\setminus S:\;c(S\cup U)=T}(-1)^{|U|}.
\]

Indeed, summing its right side over all closed \(T\) below a fixed closed \(W\) gives \(\sum_{U\subseteq W\setminus S}(-1)^{|U|}\), which is one for \(W=S\) and zero otherwise; this is the defining Möbius recurrence. If \(T\) is incomplete and closed, every intermediate subset between \(S\) and \(T\) is still closed, so the interval is Boolean.

Suppose \(T\) is a complete word. The residual positions \(T\setminus S\) split into \(s\ge2\) positive-size color groups. An intermediate subset closes to \(T\) exactly if all but at most one of these groups have been completely included. For each group \(a\), the signed sum over subsets that contain every other group is zero, because the group itself is nonempty. Intersections of any two such conditions contain only all residual positions. Inclusion-exclusion therefore gives \((-1)^r(1-s)\). When \(S=T\), the interval is a singleton.

For the top interval, let \(F(\mathbf r)\) be the signed sum over all feasible extensions of \(S\) within its residual positions. Choosing \(t_a\) extra occurrences of color \(a\) gives the explicit truncated-multinomial expression in the theorem. There are \(M_{\mathbf r}=r!/\prod_ar_a!\) complete extensions. The signed sum over nonclosed feasible extensions with only one unfinished color is \(s(-1)^{r+1}M_{\mathbf r}\), whereas the sum of their closed full-completion interval Möbius values is \((1-s)(-1)^rM_{\mathbf r}\). These cancel in the Möbius recurrence after removing the complete extensions from \(F(\mathbf r)\), leaving \(\mu(S,E)=-F(\mathbf r)\). For \(S\) already complete, this is simply the two-point interval. For \(S=E\), \(\mu(E,E)=1\).

## Verification

The standalone `verify.py` independently constructs all fixed-content words and their literal incidence, computes closure by intersecting every compatible complete model, enumerates all literal subsets, and compares their minimal nonclosed premises, one-round implications, closed-set counts, and every interval Möbius value with the formulas. It exhaustively checks multiplicity vectors \((1,1,1)\), \((2,1,1)\), \((1,1,1,1)\), \((3,1,1)\), and \((2,2,1)\). The all-parameter result comes from the proof, not the finite experiments.

## Relationship to prior work

Baixeries and Napoli (2024 preprint; revised 2025) develop the general distinction between minimum and direct implication bases and compare closure algorithms. Adaricheva, Nation, and Rand (2011) analyze ordered direct bases of arbitrary finite closure systems. Those general definitions and algorithms are prior work; the present theorem gives a family-specific simultaneous optimum, pseudo-intent classification, exact cardinality enumerator, and full Möbius formulas not stated in the inspected materials.

The previously studied permutation-assignment context corresponds to the special vector \((1,\ldots,1)\): the basis formula reduces to \(n^2(n-1)+n\,n!\). Fixed content with unequal positive multiplicities is not an instance of that special case. Conversely, permitting arbitrary surjective words combines different contents and changes the closure relation; the present fixed-content closure is not a corollary of its implication counts. These comparisons do not constitute proof that the current formulas were never published under another name.

## Limitations

The theorem excludes \(q=1,2\); in particular, some minimum-premise descriptions change for \(q=2\). It does not treat forbidden-position boards or unrestricted assignments with only lower bounds on color multiplicities. No independent external correctness or publication-priority audit has been performed. The specific content-class lattice may have equivalents in the literature of contingency tables, constrained assignments, or multiset permutations that were not indexed by the searches made.

## References

1. J. Baixeries and A. Napoli, *A minimal base or a direct base? That is the question!*, arXiv:2404.12229 (first public preprint 18 April 2024), especially Sections 2, 4, 6–8.
2. K. Adaricheva, J. B. Nation, and R. Rand, *Ordered direct implicational basis of a finite closure system*, arXiv:1110.5805 (2011), especially Sections 1–2.
3. The definition of the Duquenne–Guigues pseudo-intent and canonical implication base is used in the standard finite formal concept analysis sense, as discussed in Reference 1.
