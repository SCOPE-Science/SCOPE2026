# Sharp quotient complexity for a prescribed number of scattered \(01\) occurrences

## Finding
For every integer \(k\ge0\), let
\[
L_k=\{w\in\{0,1\}^{*}:c_{01}(w)=k\},\qquad
c_{01}(w)=\#\{(i,j):i<j,\ w_i=0,\ w_j=1\}.
\]
Here occurrences are *scattered* subsequences, not necessarily adjacent factors. If \(\kappa(X)\) denotes the number of states of the minimal **complete** DFA for a language \(X\) over exactly \(\{0,1\}\), then
\[
\boxed{\kappa(L_k)=3+\left\lfloor\frac{(k+1)^2}{4}\right\rfloor}
\quad\text{for every integer }k\ge0.
\]
In particular, the first values for \(k=0,1,\ldots,10\) are \(3,4,5,7,9,12,15,19,23,28,33\).

## Assumptions and scope
Words have arbitrary finite length, including the empty word. The zero-one pattern is an **ordered pair of positions**, so repeated embeddings of the same two-letter word count separately. The input alphabet is fixed to the two symbols \(0,1\), and the dead state counts toward the minimum. The theorem concerns each fixed finite nonnegative multiplicity \(k\), not a single finite-length sample. No minimality claim is made for larger patterns or nonbinary alphabets.

## Proof
**Exact right quotients.** Write \(z(u)\) for the number of zero symbols in a prefix \(u\), and \(b(u)=c_{01}(u)\). For arbitrary finite words \(u,v\), separating pairs entirely within either word from pairs crossing the join gives
\[
c_{01}(uv)=b(u)+z(u)\,\#_1(v)+c_{01}(v).
\]
Consequently, if \(b(u)\le k\), the right quotient \(u^{-1}L_k\) is
\[
R(a,t)=\{v:a\,\#_1(v)+c_{01}(v)=t\},\qquad
a=z(u),\ t=k-b(u).
\]
If \(b(u)>k\), the quotient is empty. When \(a=0\), necessarily \(b(u)=0\); all such prefixes give the single initial quotient \(R(0,k)=L_k\). Conversely, for any integers \(a\ge1\) and \(0\le t\le k\), the prefix \(u=0\,1^{k-t}\,0^{a-1}\) satisfies \(z(u)=a\) and \(b(u)=k-t\). Therefore **all** pairs in this range are reachable, and no unlisted kinds of quotients occur.

**Zero and impossible remainders.** For every \(a\ge1\), the equation defining \(R(a,0)\) permits no symbols \(1\), so \(R(a,0)=0^{*}\). For \(0<t<a\), each suffix containing \(1\) contributes at least \(a>t\), while a suffix without \(1\) contributes zero; hence \(R(a,t)=\varnothing\). The empty quotient is also reached after the count exceeds \(k\). Both languages are genuinely distinct, since one contains the empty word and the other does not.

**Single-one quotients.** Fix \(a\le t<2a\). Every accepted suffix has exactly one \(1\): two \(1\)'s alone contribute at least \(2a>t\). If that one \(1\) has \(d\) preceding zeroes, the total is \(a+d\), so
\[
R(a,t)=0^{d}10^{*},\qquad d=t-a.
\]
The constraint \(d<a\), together with \(a+d=t\le k\), is satisfiable precisely for integers \(0\le d\le\lfloor(k-1)/2\rfloor\). Thus there are exactly \(\lceil k/2\rceil\) distinct quotients of this kind (none when \(k=0\)). They are distinguished by their sole possible number \(d\) of initial zeroes before their unique one.

**Multi-one quotients and separation.** The remaining reachable nonempty cases have \(1\le a\le\lfloor t/2\rfloor\) and \(1\le t\le k\). They admit a suffix with two \(1\)'s, namely \(1\,0^{t-2a}1\), and hence are distinct from every single-one quotient, from \(0^{*}\), and from the empty quotient. More sharply, for any such \(R(a,t)\), the complete collections of test words of two forms satisfy
\[
0^j1\in R(a,t)\iff j=t-a,\qquad
1\,0^j1\in R(a,t)\iff j=t-2a\qquad(j\ge0).
\]
The two unique successful exponents determine \(a=(t-a)-(t-2a)\) and then \(t\). Thus **all these multi-one quotients are pairwise distinct**. Their number is
\[
\sum_{t=1}^{k}\left\lfloor\frac t2\right\rfloor
=\left\lfloor\frac{k^2}{4}\right\rfloor.
\]

**The initial quotient and the final count.** For \(k\ge1\), the suffix \(0^k1\) belongs to \(R(0,k)\), but to no \(R(a,t)\) with \(a\ge1\) and \(t\le k\), since in the latter its value is \(a+k>t\). The initial quotient also differs from the empty one. For \(k=0\), the initial quotient is \(1^{*}0^{*}\), separated from \(0^{*}\) and the empty quotient by the word \(1\); the single-one and multi-one lists are empty. Hence for \(k\ge1\) the number of distinct reachable right quotients is
\[
3+\left\lceil\frac k2\right\rceil
+\left\lfloor\frac{k^2}{4}\right\rfloor
=3+\left\lfloor\frac{(k+1)^2}{4}\right\rfloor,
\]
with the same formula valid at \(k=0\). By the Myhill–Nerode theorem, distinct reachable right quotients are exactly states of the minimal complete DFA. This proves both the lower and upper bounds for every \(k\).

## Verification
A standalone Python 3 standard-library program `verify_dfa.py` independently builds a saturated deterministic counting automaton, enumerates its reachable states, and performs partition refinement to compute its exact minimal-state count for all \(0\le k\le45\). The results agree with the formula. It also checks the join identity against a separate ordered-index-pair enumerator for all \(8191\) binary words of lengths \(0\) through \(12\). Run:

```text
python3 verify_dfa.py
```

Expected output begins `FINITE_CHECK_PASS`. The theorem for arbitrary \(k\) follows from the quotient proof above; bounded computer tests are corroboration, not an infinite certificate.

## Relationship to prior work
Brzozowski, Davies and Madan (2018), *State Complexity of Pattern Matching in Regular Languages*, Sections 6 and 7, determine worst-case state-complexity bounds for testing **existence** of a pattern as a subsequence within a regular text language. Existence does not impose exactly \(k\) distinct embeddings. Their single-word subsequence theorem consequently does not give this all-multiplicity formula.

Menon and Singh (2023), *Subsequence frequency in binary words*, introduces the quantities \(B_{n,p}(k)\) for counting binary words of prescribed *length* with exactly \(k\) embeddings of pattern \(p\), and determines enumeration formulas at small counts. Its sections on finite-length distributions do not state the state complexity of the unbounded-length language \(L_k\). The two projects share the scattered-embedding definition but address different natural invariants. No general result in the inspected literature was found that yields this exact quotient classification; this search outcome is not a proof of publication priority.

## Limitations
The formula is specific to the fixed binary pattern \(01\). It does not classify longer patterns, weighted occurrences, or variable \(k\) supplied as part of a separate input. The proof supplies an exact state-count formula and quotient structure, not a lower bound for every possible algorithm that computes subsequence statistics. The literature comparison is necessarily nonexhaustive and independent external validation has not occurred.

## References
1. J. A. Brzozowski, S. Davies, A. Madan, *State Complexity of Pattern Matching in Regular Languages*, arXiv:1806.04645, first publicly submitted 2018-06-12. https://arxiv.org/abs/1806.04645
2. K. Menon, A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, first publicly submitted 2023-06-13. https://arxiv.org/abs/2306.07870
