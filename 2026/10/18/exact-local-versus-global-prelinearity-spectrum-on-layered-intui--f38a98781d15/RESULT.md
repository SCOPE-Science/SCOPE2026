# Exact local-versus-global prelinearity spectrum on layered intuitionistic frames

## Finding
Let \(P=A_1\oplus\cdots\oplus A_h\) be an ordinal sum of nonempty antichains, with \(n_i=|A_i|\ge1\). Consider the finite Heyting algebra \(H=\operatorname{Up}(P)\) of upper sets of this Kripke frame, and choose an ordered pair \((U,V)\) uniformly from \(H^2\). Write \(C\) if the upsets are globally comparable by inclusion, and \(D\) if the Gödel–Dummett prelinearity instance \((U\to V)\vee(V\to U)=P\) holds. Define
\[
N=1+\sum_{i=1}^{h}(2^{n_i}-1),\qquad q_i=4^{n_i}-2\cdot3^{n_i}+2^{n_i}.
\]
The exact and disjoint three-cell distribution is
\[
\boxed{|C|=N^2-\sum_{i=1}^{h}q_i,\qquad |D\setminus C|=q_1,\qquad |\neg D|=\sum_{i=2}^{h}q_i.}
\]
These are counts of ordered pairs, not probabilities; divide by \(N^2\) to obtain exact uniform probabilities. In particular,
\[
\Pr(D)=1-\frac{\sum_{i=2}^{h}q_i}{N^2},\qquad
\Pr(C)=1-\frac{\sum_{i=1}^{h}q_i}{N^2}.
\]
Consequently, universal prelinearity holds if and only if each upper level is a singleton, that is, \(n_2=\cdots=n_h=1\); this condition is vacuous for one level. Moreover, for every fixed \(h\ge2\) and fixed upper-level sizes \(n_2,\ldots,n_h\), as \(n_1\to\infty\),
\[
\boxed{\Pr(D)\longrightarrow1\quad\text{but}\quad\Pr(C)\longrightarrow0.}
\]
Thus a single frame family exhibits near-certain local prelinearity while almost every pair of truth sets is globally incomparable. At the opposite extreme, with earlier levels fixed and a single upper level of size growing to infinity, \(\Pr(D)\to0\). For fixed \(h\ge2\) and all \(n_i=m\to\infty\), \(\Pr(D)\to1-(h-1)/h^2\).

## Assumptions and scope
Here \(A_i\) is an antichain and every point of \(A_i\) lies strictly below every point of \(A_j\) for \(i<j\). All levels are finite and nonempty. The order is the intuitionistic information order, so a truth set is an upset. Heyting implication is the Kripke implication
\[
U\to V=\{x\in P:\uparrow x\cap U\subseteq V\}.
\]
Prelinearity at a pair requires that every world satisfy at least one of the two implications; it need not require that the same implication holds everywhere. This is **different** from global comparability, which forces one of the implications to be universally true. The probabilities sample \(U,V\) independently and uniformly from the **distinct upsets**, not by independent Bernoulli assignments to every world. The theorem also covers \(h=1\), all singleton levels, and empty upsets.

## Proof
**Upset normal form.** The empty upset is one possibility. Each nonempty upset has a unique first level \(i\) at which it appears: it is specified by a nonempty subset \(S\subseteq A_i\), contains all of \(A_{i+1},\ldots,A_h\), and contains none of the preceding levels. This gives exactly \(N=1+\sum_i(2^{n_i}-1)\) upsets.

**Global incomparability.** If two nonempty upsets have different first occupied levels, one includes the other. If their first level is the same, say \(i\), write their chosen nonempty boundary subsets as \(S,T\subseteq A_i\). The upsets are incomparable if and only if both \(S\setminus T\) and \(T\setminus S\) are nonempty. There are \(4^{n_i}\) ordered subset pairs in total; \(3^{n_i}\) satisfy \(S\subseteq T\), another \(3^{n_i}\) satisfy \(T\subseteq S\), and \(2^{n_i}\) satisfy both. Inclusion–exclusion yields exactly \(q_i=4^{n_i}-2\cdot3^{n_i}+2^{n_i}\) incomparable pairs. Both boundary subsets are necessarily nonempty in such a pair. Summing gives \(|\neg C|=\sum_iq_i\).

**The local implication test.** Let \(B=U\setminus V\) and \(E=V\setminus U\). At a world \(x\), implication \(U\to V\) fails exactly when \(\uparrow x\cap B\ne\varnothing\), while \(V\to U\) fails exactly when \(\uparrow x\cap E\ne\varnothing\). Therefore prelinearity fails somewhere exactly when \(B\) and \(E\) contain points with a common lower bound \(x\). For an incomparable pair whose earliest occupied level is \(i\), both difference sets are nonempty subsets of the antichain \(A_i\), with no differences in any other level. If \(i=1\), no point can lie below two distinct points of \(A_1\), so the pair satisfies local prelinearity even though it is not globally comparable. If \(i\ge2\), every point of \(A_{i-1}\) is below both difference sets and witnesses failure of the prelinearity identity. Globally comparable pairs always satisfy it. Hence precisely the \(q_1\) incomparable first-level pairs belong to \(D\setminus C\), and exactly \(\sum_{i\ge2}q_i\) pairs fail \(D\). This proves all three cells and their completeness.

**Validity and limits.** Since \(q_i=0\) precisely when \(n_i=1\) (for positive integer level size), universal prelinearity is equivalent to all upper levels being singleton. For fixed upper-level sizes and growing \(n_1\), we have \(N\sim2^{n_1}\), \(q_1\sim4^{n_1}\), and \(\sum_{i\ge2}q_i=O(1)\). Hence \(\Pr(D)\to1\) while \(\Pr(C)=1-(q_1+O(1))/N^2\to0\). With the highest level growing and all lower sizes fixed, its \(q_h\) asymptotically equals \(N^2\), giving \(\Pr(D)\to0\). If all level sizes equal \(m\), then \(N\sim h2^m\) and each \(q_i\sim4^m\), giving the stated balanced limit.

## Verification
The standalone standard-library Python program `verify_prelinearity.py` constructs each labelled weak-order frame and all of its upsets by independent bitset tests. It directly evaluates each of the two Heyting implications at every world in each ordered pair; it does not invoke the closed formulas to decide logical satisfaction. It separately counts global comparability, local prelinearity without global comparability, and local failure. It then checks all three exact formulas and the universal-prelinearity criterion for **all 511 level-size compositions of total size from one through nine worlds**. Fourteen additional larger symbolic-parameter consistency checks test counting bounds. The reproducible command is `python verify_prelinearity.py` and its observed completion line is:

`VERIFY_OK exact joint spectrum on all 511 compositions of 1..9 worlds; 14 large-parameter algebraic consistency tests`

These finite tests support, but do not replace, the proof for arbitrary finite level sizes.

## Relationship to prior work
Flaminio, Godo, Menchón, and Rodriguez (2021) study Gödel modal logic via finite-frame and prelinearity semantics. Their central requirement is **universal** validity, not the exact fraction of valuation pairs satisfying prelinearity in a fixed non-Gödel Heyting algebra. Bumpus and Kocsis (2021) develop degrees of satisfiability for finite Heyting algebras, including several classical principles; the pertinent treatment does not provide the three-cell local-versus-global prelinearity spectrum for weak-order frames. Lyon (2023) studies Gödel–Dummett logic and its proof-theoretic/local frame conditions; the inspected semantic treatment does not enumerate random valuation pairs. The present theorem combines natural Heyting degree-of-satisfiability sampling with exact weak-order level combinatorics and identifies a strong local/global probability separation. It does not claim to originate the Gödel–Dummett axiom, the Kripke truth clause, weak-order decompositions, or the principle of measuring satisfiability degrees.

## Limitations
The exact formulas depend on complete cross-level comparability and are not asserted for arbitrary finite posets, forests, or nonuniform valuation measures. The result counts truth assignments as uniformly chosen distinct upsets; sampling independent bits at all worlds would not have the same measure. Independent external validation has not been performed. Relevant primary literature and mathematical research records were examined, but an equivalent formula in older order-theoretic or probabilistic-logic literature cannot be conclusively excluded; search silence is not a proof of priority.

## References
1. T. Flaminio, L. Godo, P. Menchón, and R. O. Rodriguez, “Algebras and relational frames for Gödel modal logic and some of its extensions,” arXiv:2110.02528, first publicly submitted 2021-10-06. https://arxiv.org/abs/2110.02528
2. B. M. Bumpus and Z. A. Kocsis, “Degree of Satisfiability in Heyting Algebras,” arXiv:2110.11515, first publicly submitted 2021-10-21. https://arxiv.org/abs/2110.11515
3. T. S. Lyon, “Nested Sequents for Intermediate Logics: The Case of Gödel-Dummett Logics,” arXiv:2306.07550, first publicly submitted 2023-06-13. https://arxiv.org/abs/2306.07550
