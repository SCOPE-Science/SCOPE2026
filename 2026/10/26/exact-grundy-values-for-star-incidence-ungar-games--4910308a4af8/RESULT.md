# Exact Grundy values for star-incidence Ungar games

## Finding

Let \(K_{1,n}\) be the labelled star with one centre and \(n\geq1\) leaves. Form its incidence poset \(P_n\): the elements are its vertices and edges, with each edge element strictly below its two endpoint vertices and no other comparabilities. Start the normal-play Ungar game at the full ideal \(P_n\), where a legal move removes any nonempty subset of the currently maximal elements. If \(g(P_n)\) is its Sprague–Grundy number, then

\[
g(P_n)=2n+1-\kappa(n),\qquad
\kappa(n)=\max\{k\in\mathbb Z_{\geq0}: k(k+1)/2\leq n\}.
\]

The theorem is supported by an exact formula for all auxiliary residual positions. Write \(F(a,b)\) for a disjoint union of \(a\) two-element chains and \(b\) singleton elements under the same Ungar rules, and put \(T_b=b(b+1)/2\). For every \(a,b\geq0\),

\[
F(a,b)=\begin{cases}
2a+b,&a\leq T_b,\\
T_b+\bigl((a-T_b-1)\bmod(b+1)\bigr),&a>T_b.
\end{cases}
\]

Write \(H(a,b)\) for the poset containing one central maximal element, \(a\) leaves above distinct edge-elements also below the centre, and \(b\) further edge-elements below only the centre. Then \(H(a,b)=a\) whenever \(b\geq1\), and \(H(n,0)=2n+1-\kappa(n)\) for \(n\geq1\).

## Assumptions and scope

All posets are finite. The normal-play convention assigns nimber zero to the empty poset and the mex of option nimbers to every other position; a move removes at least one currently maximal element. Vertices and edges are *poset elements*, not moves of an ordinary edge-deletion game. The statement concerns the entire nimber, not merely the identity of the winner. The incidence-poset construction and its full initial ideal are fixed. No assertion is made for arbitrary incidence graphs.

## Proof

**Step 1: the independent-chain positions.** From a position counted by \(F(a,b)\), remove \(i\) of its \(a\) chain tops and \(j\) of its \(b\) singleton tops, where \(0\leq i\leq a\), \(0\leq j\leq b\), and \(i+j>0\). The resulting position has \(a-i\) two-element chains and \(b+i-j\) singletons. Thus

\[
F(a,b)=\operatorname{mex}\{F(a-i,b+i-j):0\leq i\leq a,\ 0\leq j\leq b,\ i+j>0\}.
\]

We prove the displayed formula for \(F\) by induction on \(2a+b\). When \(a=0\), any nonempty set of singleton elements may be removed, giving \(F(0,b)=b\). Put \(s=T_b\) and \(W=2a+b\). Suppose first \(a\leq s\). Every successor has fewer than \(W\) elements and, by the induction formula, nimber at most its element count, so no option has value \(W\). For \(b\geq1\), the set of options from \((a,b)\) includes the position \((a,b-1)\) and, by removing that particular singleton together with any extra chosen maximal elements, also every option *of* \((a,b-1)\). Hence option nimbers realize \(0,\ldots,F(a,b-1)\). If \(a\leq T_{b-1}\), this already gives \(0,\ldots,W-1\). Otherwise \(T_{b-1}<a\leq T_b\), so the induction formula gives \(F(a,b-1)=a-1\). Removing all \(a\) chain tops and any number of original singletons gives values \(a,a+1,\ldots,a+b\). Removing \(i\) chain tops and no singletons, for \(1\leq i\leq a\), leaves a high-region position \((a-i,b+i)\) with value \(W-i\), covering \(a+b,\ldots,W-1\). Thus every smaller nonnegative integer occurs and \(F(a,b)=W\).

Now suppose \(a>s\). Write \(a=s+1+r+(b+1)u\), uniquely with \(0\leq r\leq b\) and \(u\geq0\). The proposed value is \(s+r\). Consider an arbitrary move to \((a',b')=(a-i,b+i-j)\). If the successor is in its high region, its nimber is its remaining element count \(W-i-j\geq a>s+r\). If it is in its low region and \(b'>b\), its nimber is at least \(T_{b+1}=s+b+1>s+r\). If it is low with \(b'=b\), necessarily \(i=j\geq1\), and its low residue differs from \(r\) modulo \(b+1\). Finally, a low successor with \(b'<b\) has value at most \(T_b-1=s-1\). Thus no option has value \(s+r\).

Every integer below \(s\) is nonetheless reachable. For each \(b'\in\{0,\ldots,b-1\}\), choose \(i\) freely from \(0,\ldots,b'\) and set \(j=i+b-b'\). These are legal moves, keep the successor in its low region, and sweep its residue through \(0,\ldots,b'\). Hence they realize exactly the consecutive band \([T_{b'},T_{b'+1}-1]\); the bands cover \(0,\ldots,s-1\). For the remaining integers \(s,\ldots,s+r-1\), take \(i=j\in\{1,\ldots,r\}\), giving value \(s+r-i\). Consequently \(F(a,b)=s+r\), completing the induction.

**Step 2: the central residual positions.** In \(H(a,b)\), a move omitting the centre removes \(i\geq1\) leaf tops and gives \(H(a-i,b+i)\). A move removing the centre also removes any \(i\geq0\) leaf tops; the resulting independent chains and singleton elements give \(F(a-i,b+i)\). Therefore

\[
H(a,b)=\operatorname{mex}\left(
\{H(a-i,b+i):1\leq i\leq a\}\cup
\{F(a-i,b+i):0\leq i\leq a\}
\right).
\]

For \(b\geq1\), induction on \(a\) proves \(H(a,b)=a\): the first class of moves has values \(0,\ldots,a-1\). In the second class, the high branch of the \(F\)-formula gives \(2a+b-i>a\), while the low branch gives at most \(a-i-1<a\). Thus the value \(a\) is absent. This argument includes \(a=0\), for which only the centre can be removed and \(F(0,b)=b\ne0\).

For \(H(n,0)\), the first class of options realizes \(0,\ldots,n-1\) because \(H(n-i,i)=n-i\) for \(1\leq i\leq n\). The second class has values \(F(n-i,i)\), for \(0\leq i\leq n\). In its low branch this is at most \(n-i-1<n\); in its high branch it is \(2n-i\). The high branch occurs precisely when \(n-i\leq T_i\), equivalently \(n<T_{i+1}\), or \(i\geq\kappa(n)\). Therefore high-branch moves realize each of \(n,n+1,\ldots,2n-\kappa(n)\). The lowest missing option value is \(2n-\kappa(n)+1\). This equals the asserted \(2n+1-\kappa(n)\). Finally, \(P_n=H(n,0)\) by construction.

## Verification

The accompanying self-contained `verify.py` independently recomputes the mex recurrences for every \(0\leq a,b\leq30\), tests central residual positions across \(a<30\) and \(1\leq b\leq14\), tests the initial star formula for \(1\leq n\leq27\), and separately computes game nimbers directly on the labelled incidence posets for \(1\leq n\leq8\), without using the compressed recurrences for this final check. Run `python3 verify.py`; success prints `VERIFY_OK`. These finite checks are corroboration; the induction above establishes the unbounded result.

## Relationship to prior work

Defant, Kravitz and Williams introduced Ungar games. Paltrowitz classified second-player wins in graded-poset cases; Hashimoto studied computational complexity on distributive lattices. Those results concern outcome or complexity rather than the complete Sprague–Grundy number on star-incidence posets. The independent-chain auxiliary game is a special case of slow Moore Nim with arbitrarily many piles of heights at most two. Gurvich and Ho's studied Sprague–Grundy cases impose small fixed pile-count constraints; their full-text theorem does not provide the present arbitrary-\(a,b\) expression. No historical uniqueness assertion is made.

## Limitations

The closed formula applies to incidence posets of stars, together with the explicitly described residual positions, not to arbitrary height-two posets or all graph-incidence posets. Similar formulas might occur under alternative names in selective-compound impartial game literature; an undiscovered equivalent is a residual priority risk. Verification is not independent mathematical review.

## References

- K. Hashimoto, *The Computational Complexity of the Ungar Games on Distributive Lattices*, arXiv:2610.11017 (first posted 2026-10-07), https://arxiv.org/abs/2610.11017.
- C. Defant, N. Kravitz and N. Williams, *The Ungar Games*, arXiv:2302.06552, https://arxiv.org/abs/2302.06552.
- J. Paltrowitz, *The Ungar Games on Graded Posets*, arXiv:2509.02959, https://arxiv.org/abs/2509.02959.
- V. Gurvich and N. B. Ho, *Slow k-Nim*, arXiv:1508.05777, https://arxiv.org/abs/1508.05777.
