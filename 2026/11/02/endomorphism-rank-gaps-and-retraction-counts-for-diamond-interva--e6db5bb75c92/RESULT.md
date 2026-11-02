# Endomorphism rank gaps and retraction counts for diamond interval semirings

## Finding

For every integer \(n\geq1\), let \(D_n\) be the finite bounded poset consisting of a minimum \(\bot\), a maximum \(\top\), and \(n\) pairwise incomparable elements \(p_1,\ldots,p_n\) satisfying \(\bot<p_i<\top\). Form its **flat interval semiring** \(S_n=I(D_n)\), with no distinguished constants in the signature: its elements are a multiplicative zero \(0\), the long interval \(w=(\bot,\top)\), and the \(2n\) short intervals
\[
 a_i=(\bot,p_i),\qquad b_i=(p_i,\top)\quad (1\leq i\leq n).
\]
Its addition is \(x+x=x\), \(x+y=0\) for distinct elements, and its only nonzero products are \(a_i b_i=w\). In particular \(|S_n|=2n+2\).

Write \(N_n(r)\) for the number of semiring endomorphisms with an image of cardinality \(r\), and write \((d)_{m}=d(d-1)\cdots(d-m+1)\), with \((d)_0=1\). Then the **entire endomorphism image-size distribution** is
\[
\boxed{N_n(m+1)=(2n)_{m}\,[z^m](1+z)(1+2z)^n\quad(0\leq m\leq n+1),}
\]
\[
\boxed{N_n(2n+2)=n!,\qquad N_n(r)=0\text{ for all other }r.}
\]
Thus all ranks \(1,2,\dots,n+2\) occur, and for \(n\geq2\) all ranks from \(n+3\) through \(2n+1\) are absent. The full endomorphism count is
\[
\boxed{|\operatorname{End}(S_n)|=n!+\sum_{m=0}^{n+1}(2n)_{m}[z^m](1+z)(1+2z)^n.}
\]
The unit group and the idempotent elements of the endomorphism monoid satisfy
\[
\boxed{\operatorname{Aut}(S_n)\cong\mathfrak S_n,\qquad
 |\{f\in\operatorname{End}(S_n):f^2=f\}|=3^n+1.}
\]
More precisely, an endomorphism is either a simultaneous permutation \(a_i\mapsto a_{\sigma(i)}\), \(b_i\mapsto b_{\sigma(i)}\), \(w\mapsto w\), or it sends \(w\) to zero and maps the \(2n\) short intervals injectively *on their nonzero images* into a set containing at most one member of every pair \(\{a_j,b_j\}\), with \(w\) additionally permitted among the images. Every such assignment defines an endomorphism. The idempotents apart from the identity are precisely the projections fixing a chosen zero-product subset of the short intervals and killing every other element.

For the canonical six-element case \(S_2\), the image sizes and multiplicities are \(N_2(1)=1\), \(N_2(2)=20\), \(N_2(3)=96\), \(N_2(4)=96\), and \(N_2(6)=2\); in particular \(|\operatorname{End}(S_2)|=215\), with ten idempotent endomorphisms and no endomorphisms of image size five.

## Assumptions and scope

All maps preserve both binary operations \(+\) and multiplication, with no prescribed images of constants (the signature has no constants). The semiring is the flat, noncommutative interval semiring of the explicitly specified \(n\)-diamond poset, *not* its incidence algebra, not the full relation semiring, and not a semiring of arbitrary subsets. The parameter \(n\) is an arbitrary positive integer; no assumption on an underlying coefficient field is relevant. Image cardinality counts the actual number of distinct values of an endomorphism, including zero.

The family \(S_n\) is also the flat **graph semiring** of the directed matching with arrows \(a_i\to b_i\), in the terminology of Gao--Ren: vertices are the short intervals, and every directed edge multiplies to the common annihilator \(w\). For \(n\ge2\), each \(S_n\) generates the bounded-height variety \(\mathcal B_2\) from Gao--Zhou, since \(S_2\) is their canonical generator \(I(Q_2)\), \(S_2\) is a subsemiring of \(S_n\), and \(S_n\in\mathcal B_2\).

## Proof

**Step 1: additive constraints.** Every element of \(S_n\), including \(0\), has square zero under multiplication. For a semiring endomorphism \(f\), multiplicativity of \(f\) and idempotence of \(0\) imply \(f(0)=f(0\cdot0)=f(0)^2=0\). Since the addition is flat, preservation of addition is then **equivalent** to the following rule: two distinct source elements may have the same image only when that image is zero. Indeed, for distinct \(x,y\), the equation \(f(x+y)=f(0)=0=f(x)+f(y)\) holds precisely if \(f(x)\ne f(y)\) or both are zero. When \(x=y\), the addition law is automatic.

**Step 2: the nonzero-product case.** In \(S_n\), all nonzero products have value \(w\) and arise only from the ordered pairs \((a_i,b_i)\). Therefore
\[
 f(w)=f(a_i)f(b_i)\in\{0,w\}\quad\text{for every }i.
\]
Suppose \(f(w)=w\). To obtain a nonzero product, there is a unique index \(j\) for which \(f(a_i)=a_j\) and \(f(b_i)=b_j\). Distinct nonzero source elements must have distinct nonzero images, by Step 1, so the indices \(j\) for different \(i\) are all distinct. They therefore form a permutation \(\sigma\in\mathfrak S_n\). Conversely, each such simultaneous permutation preserves both operations, giving exactly \(n!\) automorphisms. These are the only endomorphisms with \(f(w)\ne0\), and all have rank \(2n+2\).

**Step 3: the zero-product case.** Suppose \(f(w)=0\). For every ordered pair of short intervals \(s,t\), the source product lies in \(\{0,w\}\), so \(f(st)=0\). Consequently the images of **all** short intervals must multiply pairwise to zero. By the multiplication table this says exactly that their nonzero image set does not contain both \(a_j\) and \(b_j\) for any \(j\). There is no restriction on whether it contains \(w\), since \(w\) annihilates every element. In addition, by Step 1 the nonzero images must be distinct. Conversely, these two conditions ensure preservation of both operations on all source pairs, including those involving \(0\) or \(w\), so they are necessary and sufficient.

**Step 4: rank enumeration.** A zero-product subset \(T\subseteq\{a_1,b_1,\ldots,a_n,b_n,w\}\) can contain none or one of the two short intervals at index \(j\), and can independently contain \(w\). Thus its cardinality generating polynomial is \((1+2z)^n(1+z)\). For a fixed such subset of cardinality \(m\), each assignment of its members to \(m\) distinct source short intervals defines exactly one endomorphism of Step 3, with all remaining short intervals mapped to zero. There are \(\binom{2n}{m}m!=(2n)_m\) assignments. Its image consists of zero and precisely these \(m\) members, so its rank is \(m+1\). The target subset size satisfies \(0\le m\le n+1\), and each size occurs (as \(n+1\le2n\) for \(n\ge1\)). Adding the \(n!\) automorphisms from Step 2 gives the complete formula and the rank gap.

**Step 5: idempotent endomorphisms.** If \(f\) is an automorphism satisfying \(f^2=f\), it must be the identity. If instead \(f(w)=0\) and \(f^2=f\), no short interval can map to \(w\), since \(f(w)=0\). Every nonzero image of a short interval must be fixed by \(f\). The injectivity condition from Step 1 then forces all other short intervals to map to zero: a second source element cannot map to an already-fixed nonzero element. Thus an idempotent endomorphism of this type fixes exactly a subset \(F\) of the short intervals which contains at most one of \(a_j,b_j\) for each \(j\), kills all remaining elements, and fixes zero. Conversely every such projection preserves the multiplication and addition and is idempotent. There are \(3^n\) such subsets, and the identity is an additional idempotent, giving \(3^n+1\).

This proves all claims.

## Verification

Run `python3 verify.py` from the folder containing this file. The verifier builds the full semiring addition and multiplication tables from the definition. It exhaustively examines all functions on nonzero elements for \(n=1\) and \(n=2\), directly checks both homomorphism laws on every ordered pair, and compares the resulting rank distribution, idempotent count, and automorphism count against the formulas. A separate assignment enumeration for \(n=3\) checks all zero-product-case images and their rank counts. The expected output ends in `VERIFY_OK`.

The verified rank distributions are \((1,6,4,1)\) for \(n=1\), and \((1,20,96,96,0,2)\) for \(n=2\) (ordered by ranks starting at one). For \(n=3\), the collapsed-long-interval ranks one through five have counts \((1,42,540,2400,2880)\). These finite checks are consistency tests; the all-\(n\) result is proved in Steps 1--5.

## Relationship to prior work

Gao and Zhou introduced and developed flat interval semirings of posets and proved their variety-theoretic structural statements, including the finite generator \(I(Q_2)\) for \(\mathcal B_2\). Their construction yields the multiplication table used here but their stated theorems concern identity bases, subdirect irreducibility, and subvariety lattices, not the full endomorphism image-size distribution or retraction counts. The present theorem concerns a natural entire family including their canonical six-element generator.

Earlier, Gao and Ren defined graph semirings of directed paths, cycles, and disjoint unions. The graph semiring of \(n\) disjoint directed edges is isomorphic to \(S_n\); thus the underlying objects and their nilpotent multiplication are known and are not claimed as new. Their work analyzes varieties generated by these semirings. The specific complete endomorphism monoid description, rank spectrum with gap, and exact idempotent count were not found in the inspected portions of these primary sources or in targeted searches under both interval-semiring and graph-semiring terminology. This is a qualified comparison, not a claim of exhaustive historical priority.

## Limitations

The result does not classify endomorphisms of arbitrary interval semirings \(I(P)\), higher-height posets, or general directed-graph flat semirings. It counts and classifies maps preserving the two binary semiring operations, not arbitrary semigroup endomorphisms of the multiplicative reduct alone. The formulas are exact but do not determine the detailed Green relations or an abstract presentation of the endomorphism monoid. Earlier general results on transformations of three-nilpotent semigroups may indirectly imply the specialized enumeration; this remains a historical-priority risk.

## References

1. Zidong Gao and Yilin Zhou, *Equational Theories of Interval Semirings of Posets*, arXiv:2610.06351, first posted 2026-10-05; especially Section 3 and Proposition 5.2. https://arxiv.org/abs/2610.06351
2. Zidong Gao and Miaomiao Ren, *The flat semirings with nilpotent multiplicative reducts*, arXiv:2506.23047, first posted 2025-06-29; especially the graph-semiring definition in Section 2 and statements about varieties in Section 3. https://arxiv.org/abs/2506.23047
3. Miaomiao Ren, Marcel Jackson, Xianzhong Zhao, and Donglin Lei, *Flat extensions of groups and limit varieties of ai-semirings*, arXiv:2208.13973, first posted 2022-08-30. https://arxiv.org/abs/2208.13973
