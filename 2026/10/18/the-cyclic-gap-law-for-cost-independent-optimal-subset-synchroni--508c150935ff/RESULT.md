# The cyclic-gap law for cost-independent optimal subset synchronization

## Finding

For every integer \(n\ge 2\), consider the standard binary Černý automaton with states \(Q=\{0,\ldots,n-1\}\), rotation \(a(i)=i+1\pmod n\), and contraction \(b(n-1)=0\), \(b(i)=i\) for \(i<n-1\). Give the two letters arbitrary **strictly positive** costs \(\alpha\) and \(\beta\), respectively.

Take any nonempty initial state set \(S\). If \(|S|=1\), the unique minimum-cost synchronizing word is empty, at cost zero. If \(|S|\ge2\), list its states as \(s_1<\cdots<s_k\) and put \(s_{k+1}=s_1\). The cyclic gap ending at \(s_{j+1}\) is \(g_j=(s_{j+1}-s_j)\bmod n\), with \(1\le g_j<n\). Define

\[
G=\max_{1\le j\le k}g_j,\qquad
 t=\max\{s_{j+1}:g_j=G\},\qquad r=n-G.
\]

Then the **unique** minimum-cost word that maps \(S\) to a singleton is

\[
w_S=a^{\,n-1-t}b\bigl(a^{\,n-1}b\bigr)^{r-1}.
\]

It contains exactly \(r\) contractions and \((n-1)r-t\) rotations. Its cost, therefore, is

\[
V_{\alpha,\beta}(S)=\alpha\bigl((n-1)(n-G)-t\bigr)+\beta(n-G).
\]

In particular, **the word itself is independent of the relative positive letter costs**. Computing the word and its cost from the ordered set takes \(O(|S|)\) arithmetic operations, apart from writing down the output word. For \(S=Q\), the formula recovers the classical \((n-1)^2\) shortest reset length when both costs equal one.

## Assumptions and scope

The automaton is exactly the two-letter Černý family with the displayed state labeling, rather than an arbitrary synchronizing automaton or an arbitrary relabeling of its letters. The objective is to merge all states of the **given** nonempty subset into any one state, not to reach a prescribed terminal state. Input costs are fixed per letter and strictly positive real numbers. Quantification is over all \(n\ge2\), every nonempty \(S\subseteq Q\), and all such \(\alpha,\beta\). Cyclic gaps are directed in the positive \(a\)-orientation; the maximum endpoint \(t\) resolves a tie between largest gaps.

## Proof

For \(|S|\ge2\), associate to every directed cyclic gap of size \(g\) ending at state \(u\) its *potential contribution*

\[
 c(g,u)=\bigl((n-1)\alpha+\beta\bigr)(n-g)-\alpha u.
\]

Let \(F(S)\) be the minimum of these contributions, and let \(F\) vanish on singletons. If \(g'<g\), then

\[
c(g',u')-c(g,u)\ge ((n-1)\alpha+\beta)-\alpha(n-1)=\beta>0.
\]

For equal gap sizes, the contribution is strictly smallest at the largest endpoint. Hence the minimizing gap is unique: it is exactly \((G,t)\), and \(F(S)=V_{\alpha,\beta}(S)>0\).

We establish **strict Bellman inequalities**. Under \(a\), every gap length is unchanged, and each endpoint increases by one modulo \(n\). A contribution with endpoint below \(n-1\) decreases by \(\alpha\); a contribution with endpoint \(n-1\) increases by \((n-1)\alpha\). Consequently

\[
 F(S)\le\alpha+F(Sa),
\]

with equality precisely when \(t<n-1\). Indeed, in that case the unique minimum contribution decreases by exactly \(\alpha\); if \(t=n-1\), that contribution rises, while every other contribution starts strictly larger and can decrease by at most \(\alpha\).

If \(n-1\notin S\), then \(Sb=S\) and \(F(S)<\beta+F(Sb)\). Otherwise, the gap immediately preceding \(n-1\) in cyclic order is extended by one and changes its endpoint to zero when \(b\) sends \(n-1\) to zero. Its contribution therefore decreases by exactly

\[
 ((n-1)\alpha+\beta)-\alpha(n-1)=\beta.
\]

The outgoing gap of \(n-1\) either disappears (if zero was already in \(S\)) or becomes one shorter and therefore has a **larger** contribution; all other gaps are unchanged. This gives

\[
 F(S)\le\beta+F(Sb),
\]

with equality precisely when the minimizing gap ends at \(t=n-1\). If the contraction produces a singleton, necessarily \(S=\{0,n-1\}\), and the same identity follows directly from \(F(S)=\beta\). For every other case, a contraction of a nonminimizing gap cannot give equality, because its contribution was strictly larger than \(F(S)\) beforehand. Thus **exactly one** of \(a,b\) makes its Bellman inequality an equality at each nonsingleton \(S\).

For any synchronizing word, repeated use of the inequalities gives \(\operatorname{cost}(w)\ge F(S)\). To attain equality, repeatedly apply the uniquely equality-achieving letter. Initially the winning gap ends at \(t\), so \(n-1-t\) rotations bring its endpoint to \(n-1\); the next letter is \(b\). The winning gap grows by one and now ends at zero. Because it has become strictly longer than every other gap, the next equality-achieving letters are \(a^{n-1}b\), repeatedly. Exactly \(r=n-G\) contractions grow the gap to full length, at which point the state set is a singleton. This produces \(w_S\), whose cost equals \(F(S)\), proving optimality. Since all other first letters at every nonsingleton state cause a strict loss and letter costs are positive, induction proves uniqueness of the entire minimum-cost word.

## Verification

The standalone `verify.py` reconstructs transitions from bit masks, checks all strict Bellman equalities/inequalities for every nonsingleton subset through \(n=16\) under four distinct positive cost assignments, and independently calculates shortest costs by reverse Dijkstra search for all subsets through \(n=12\) under three cost assignments. It further replays the displayed word for all subsets through \(n=9\) and sampled subsets through \(n=128\). The accompanying `verification_output.txt` records the successful execution. These finite tests are **not** substituted for the all-\(n\) proof above.

## Relationship to prior work

Eppstein (1990, Theorem 1) proved a shortest-sequence algorithm for *all starting subsets* of monotonic cyclic automata by passing to an interval automaton. This is an especially relevant predecessor, but its published statement gives an algorithm, not the explicit Černý cyclic-gap cost formula or a unique policy simultaneously optimal under **every positive pair of letter costs**. Gusev (2014) studied the Černý *pair* automaton and expected synchronization under random inputs, not deterministic weighted shortest words from arbitrary subsets. Behague and Johnson (2020/2022) studied \(k\)-set rendezvous thresholds over classes of automata and cited lower bounds based on the Černý family; those bounds do not assert a pointwise optimal-word formula. Ruszil (2021) studied approximation algorithms for generally weighted automata, rather than this exact cost-invariant Černý result.

The formula includes familiar shortest words for the entire state set and for two-element sets as special cases. The new structural content is the same **closed-form, uniquely optimal, letter-cost-independent synchronization law for every cardinality and every initial subset**.

## Limitations

The theorem does not cover zero or negative letter costs, state-dependent weights, prescribed terminal singletons, other synchronizing automata, or arbitrary letter extensions. Positivity is essential to the asserted uniqueness. The closest literature contains interval algorithms and subset-synchronization bounds that substantially anticipate parts of the structure; priority over every unpublished or unindexed derivation has not been established. A relevant 2014 dissertation by A. F. P. Cardoso was identified bibliographically but its full text was not accessible for comparison; the possibility of an earlier related closed form is a residual literature risk. No independent audit has been performed.

## References

1. D. Eppstein, *Reset Sequences for Monotonic Automata*, SIAM Journal on Computing 19 (1990), 500–510; accessible author manuscript: https://www.ics.uci.edu/~eppstein/pubs/Epp-SJC-90.pdf . In particular Theorem 1 and Theorem 3.
2. V. V. Gusev, *Synchronizing Automata with Random Inputs*, arXiv:1404.6731v1 (2014-04-27), https://arxiv.org/pdf/1404.6731 . In particular the pair automaton and Theorem 3.
3. N. C. Behague and J. R. Johnson, *Synchronizing Times for \(k\)-sets in Automata*, arXiv:2008.12166v1 (2020-08-27), https://arxiv.org/pdf/2008.12166 . In particular the definitions of rendezvous times and discussion of the Černý family.
4. J. Ruszil, *Approximation algorithm for finding short synchronizing words in weighted automata*, arXiv:2103.16185v1 (2021-03-30), https://arxiv.org/pdf/2103.16185 . In particular the weighted model and algorithms.
5. A. F. P. Cardoso, *The Černý Conjecture and Other Synchronization Problems*, doctoral dissertation, Universidade do Porto (2014), DOI: 10.34626/607f-t921. Full text inaccessible for the present comparison.
