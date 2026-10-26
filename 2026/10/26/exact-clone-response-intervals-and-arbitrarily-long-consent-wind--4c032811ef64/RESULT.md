# Exact clone-response intervals and arbitrarily long consent windows under the approval-weighted veto core

## Finding

**Theorem (single-alternative clone-response calculus and an unbounded acceptance window).** For a finite approval-and-ranking election, fix an alternative \(c\) approved by a strict majority and a distinct alternative \(d\). Repeatedly adding ordinally adjacent, approval-identical copies of \(d\) makes approval-weighted veto-core (AWVC) consent for \(c\) hold at *exactly* the integer points of one explicitly computable interval (possibly empty or unbounded). In particular, for every integer \(h\ge2\), there is an election with only five voters, three of whom approve \(c\), such that the number of initial alternatives is \(3h+2\), and after adding \(t\ge0\) perfect copies of the same alternative \(d\),

\[
 c\in\operatorname{AWVC}(t)\quad\Longleftrightarrow\quad 1\le t\le 3h-2.
\]

Thus the status of this **unchanged, majority-approved alternative** switches from exclusion to inclusion and then back to exclusion as one irrelevant-to-its-own-approval alternative is repeatedly cloned. The length \(3h-2\) of the consecutive acceptance window grows without bound while the electorate remains fixed at five voters.

## Assumptions and scope

There is a finite voter set \(N\) of size \(n\) and a finite alternative set \(C\) of size \(m\ge2\). Each voter reports a **strict** order over \(C\) and an approval set equal to a top segment (possibly empty) of that order. For any alternative \(x\), write \(s_x\) for the number of approving voters. For a nonempty coalition \(S\) of voters disapproving \(x\), define

\[
 B_S(x)=\{y\in C:\text{every voter in }S\text{ ranks }y\text{ strictly above }x\},
 \qquad b_S=|B_S(x)|.
\]

The AWVC criterion from Dong et al. is: for \(s_x>0\), \(x\) is **blocked** precisely when some such coalition \(S\) satisfies

\[
 \frac{|S|}{s_x}>1-\frac{|B_S(x)|}{m}.
\]

Alternatives with no approvers are excluded by convention. Equality does not block. This theorem concerns AWVC itself, not a subsequent rule that further filters its outcomes.

Fix a target \(c\) with \(s=s_c>n/2\), put \(D=\{i:c\notin A_i\}\), and fix \(d\ne c\). For each integer \(t\ge0\), adjoin distinct alternatives \(d_1,\ldots,d_t\), immediately adjacent to \(d\) in every ranking, without changing the relative order of old alternatives, and let voter \(i\) approve every copy precisely when they approve \(d\). In particular, \(c\)'s support \(s\), the electorate, and all original pairwise comparisons and approvals remain unchanged. For each nonempty \(S\subseteq D\), let

\[
 \chi_S=\begin{cases}1,&d\in B_S(c),\\0,&d\notin B_S(c),\end{cases}
 \qquad r_S=s(m-b_S)-|S|m.
\]

Here all quantities \(b_S,\chi_S,r_S\) refer to the un-cloned profile. Empty collections in maxima/minima below follow the stated conventions.

## Proof

**1. Complete affine characterization.** Each new copy of \(d\) is ranked above \(c\) by all members of \(S\) exactly when \(d\in B_S(c)\). Consequently the enlarged profile has \(m+t\) alternatives and \(b_S+t\chi_S\) unanimously better alternatives. The failure of the strict blocking inequality is therefore equivalent to

\[
 \frac{|S|}{s}\le1-\frac{b_S+t\chi_S}{m+t}
 \quad\Longleftrightarrow\quad
 r_S+t\bigl(s(1-\chi_S)-|S|\bigr)\ge0.
 \tag{1}
\]

Since \(c\) is supported by a strict majority, \(s>n-s=|D|\ge|S|\). Thus if \(\chi_S=0\), the coefficient of \(t\) in (1) is the positive integer \(s-|S|\), so \(S\)'s nonblocking condition is the lower bound \(t\ge\lceil-r_S/(s-|S|)\rceil\). If \(\chi_S=1\), the coefficient is \(-|S|\), and the nonblocking condition is the upper bound \(t\le\lfloor r_S/|S|\rfloor\).

Set

\[
 L=\max\left\{0,\max_{\substack{\varnothing\ne S\subseteq D\\\chi_S=0}}\left\lceil\frac{-r_S}{s-|S|}\right\rceil\right\},
 \qquad
 U=\min_{\substack{\varnothing\ne S\subseteq D\\\chi_S=1}}\left\lfloor\frac{r_S}{|S|}\right\rfloor.
 \tag{2}
\]

Use \(\max\varnothing=-\infty\) inside the definition of \(L\), and \(\min\varnothing=+\infty\) for \(U\). Then the exact set of admissible cloning counts is

\[
 \{t\in\mathbb Z_{\ge0}:c\in\operatorname{AWVC}(t)\}
 =\{t\in\mathbb Z:L\le t\le U\}.
 \tag{3}
\]

This also handles an empty disapprover set (every nonnegative \(t\) works), negative upper bound (empty interval), and equality at a blocking threshold (included).

**2. A five-voter family with a finite nontrivial interval.** Fix an integer \(h\ge2\). Take disjoint groups of original alternatives \(U,V,W\) of cardinalities

\[
 |U|=2h-1,\qquad |V|=h-1,\qquad |W|=3,
\]

along with target \(c\). Hence \(m=3h+2\). The first three voters rank \(c\) first and approve only \(c\). The fourth voter orders \(V\), then \(W\), then \(c\), then \(U\), approving exactly \(V\cup W\). The fifth voter orders \(U\), then \(W\), then \(c\), then \(V\), approving exactly \(U\cup W\). The order inside each group is any fixed strict order. Let \(d\in V\) and adjoin \(t\) copies of \(d\) as specified above. All approval sets are top segments, the target always has exactly three approvers, and the only potential blocking coalitions are \(\{4\},\{5\},\{4,5\}\).

Directly,

\[
 b_{\{4\}}(t)=h+2+t,\qquad
 b_{\{5\}}(t)=2h+2,\qquad
 b_{\{4,5\}}(t)=3,\qquad
 m(t)=3h+2+t.
\]

Using the weak **nonblocking** inequality \(3(m(t)-b_S(t))\ge|S|m(t)\), each coalition respectively gives

\[
 \begin{array}{c|c|c}
 S&\text{nonblocking condition}&\text{simplified}\\ 
 \hline
 \{4\}&6h\ge 3h+2+t&t\le3h-2\\
 \{5\}&3(h+t)\ge3h+2+t&t\ge1\\
 \{4,5\}&3(3h-1+t)\ge2(3h+2+t)&t\ge7-3h.
 \end{array}
\]

The first inequality in the table follows from \(m(t)-b_{\{4\}}(t)=2h\), as displayed. Since \(h\ge2\), the third condition is implied by \(t\ge1\). Hence the three constraints hold simultaneously exactly when \(1\le t\le3h-2\), proving the claim. At \(t=0\), voter 5 blocks; for \(t\ge3h-1\), voter 4 blocks. The target's approval share is exactly \(3/5\) throughout. As \(h\) increases, the acceptance window has unbounded cardinality \(3h-2\).

## Verification

The accompanying self-contained file `check.py` directly evaluates AWVC using **all** nonempty coalitions of disapprovers and independently evaluates the affine condition (1). It checks all integer cloning counts from zero through \(3h+3\) for each \(2\le h\le36\), and 100 seeded random profiles per pair of voter count \(3\le n\le8\) and alternative count \(3\le m\le9\), at five distinct copy counts each. It completed 25,270 exact-integer comparisons, all agreeing. These are finite regression tests; the proof above, rather than the experiments, establishes the quantified result for all \(h\ge2\) and all finite strict-majority profiles.

To reproduce, save the accompanying `check.py` in the same directory and run `python3 check.py` with Python 3's standard library. No external data or solvers are required.

## Relationship to prior work

Dong, Kraiczy, Vasishta, Brill, Holliday, and Boehmer (2026, Definition 8) introduced the finite-candidate AWVC criterion used here, including the approval-weighted denominator and the exact strict blocking threshold. Their Theorem 4 establishes its majority approval threshold, and their Proposition 4 concerns the effect of **adding disapproving voters**, not copying alternatives. Neither implies monotonicity under additions of candidate clones. The present contribution is the candidate-clone interval formula (1)–(3) and the arbitrarily long exclusion–inclusion–exclusion phenomenon for five fixed voters.

The general proportional veto core is **already known not to satisfy independence of clones**: Ianovski and Kondratev (2023, Proposition 15) give a finite ordinal counterexample. Neither that qualitative counterexample nor the customary clone-independence axiom is asserted here as new. The distinction here is the *approval-weighted* consent criterion, a complete numerical response to arbitrary repeated adjacent cloning under fixed majority support, and an unbounded explicit finite acceptance window.

## Limitations

The argument is restricted to finite candidate sets with normalized counting measure, strict preferences, approval sets consistent with rankings, and copies that exactly inherit their original's approval pattern for every voter. The interval formula (2) uses strict-majority support to identify coefficient signs; other support levels may require a different partition of constraints. It characterizes one candidate's membership in AWVC, not the full set-valued outcome nor a final winner of a downstream social choice rule. The five-voter profile is deliberately constructed; there is no claim about typical elections or empirical frequency. The theorem is reviewed against the identified literature but has not undergone independent scientific audit. Related general mechanisms of clone sensitivity were known earlier.

## References

1. C. Dong, S. Kraiczy, R. Vasishta, M. Brill, W. H. Holliday, and N. Boehmer, *Where Should Society Draw the Line? A Social Choice Approach to Collective Consent*, arXiv:2609.10759v1 (first posted 2026-09-09). Definition 8, Theorem 4, Proposition 4, Section 3.2. https://arxiv.org/abs/2609.10759
2. E. Ianovski and A. Y. Kondratev, *Computing the Proportional Veto Core*, arXiv:2003.09153 (first posted 2020-03-20; consulted version v4, 2023). Proposition 15 on pre-existing clone-independence failures. https://arxiv.org/abs/2003.09153
