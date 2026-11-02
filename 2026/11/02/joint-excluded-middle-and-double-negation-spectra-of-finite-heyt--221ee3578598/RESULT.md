# Joint excluded-middle and double-negation spectra of finite Heyting algebras

## Finding

Let \(H\) be a finite nontrivial Heyting algebra, with an element chosen uniformly at random. Define
\[
p(H)=\Pr_{x\in H}[x\vee\neg x=\top],\qquad
q(H)=\Pr_{x\in H}[\neg\neg x=x].
\]
The **joint spectrum** of \((p(H),q(H))\), over all such algebras, is exactly the set of finite coordinatewise products of pairs from
\[
\mathcal S_{\mathrm{conn}}=
\left\{\left(\frac2N,\frac2N\right):N\in\mathbb Z,\ N\ge2\right\}
\cup
\bigcup_{t=2}^{\infty}
\left\{\left(\frac2N,\frac{2^t}N\right):N\in\mathbb Z,\ N\ge2^t+1\right\}.
\]
The empty coordinatewise product is \((1,1)\), already present as the term \(N=2\). Every listed pair is realized, without limiting processes. Moreover, if \(P\) is the finite nonempty poset of join-irreducibles of \(H\), \(c\) the number of connected components in its undirected comparability graph, and \(m\) its number of minimal points, then
\[
\boxed{p(H)=\frac{2^c}{|J(P)|},\quad q(H)=\frac{2^m}{|J(P)|},\quad \frac{q(H)}{p(H)}=2^{m-c}.}
\]
In particular the ratio is always a nonnegative integral power of two. At **every prescribed positive defect** \(k=m-c\ge1\), the two sharp, simultaneous envelopes are
\[
\boxed{p(H)\le\frac{2}{2^{k+1}+1},\qquad q(H)\le\frac{2^{k+1}}{2^{k+1}+1}.}
\]
Equality in either envelope holds if and only if \(P\) is a disjoint union of one component consisting of \(k+1\) incomparable minimal points below a single maximum, together with any number of isolated points. Thus, for instance, the first three positive-defect endpoints are \((2/5,4/5)\), \((2/9,8/9)\), and \((2/17,16/17)\). For defect zero, \(p(H)=q(H)\); if \(H\) is not Boolean this common value is at most \(2/3\), with equality exactly for a three-element chain Heyting algebra times a finite Boolean factor.

## Assumptions and scope

A finite **nontrivial** Heyting algebra has \(\bot\ne\top\). Its pseudocomplement is \(\neg x=(x\to\bot)\). The probabilities count elements, not valuations of two independent variables: both tests are applied to the **same** uniformly chosen element. The term *defect* means the integer \(k=\log_2(q/p)\); it is an invariant of the poset decomposition, not a limiting parameter.

By the finite Birkhoff representation, every such \(H\) is isomorphic, as a Heyting algebra, to the order ideals \(J(P)\) of a finite nonempty poset \(P\). We use **downsets**: \(I\subseteq P\) is an ideal if \(x\in I\) and \(y\le x\) imply \(y\in I\). For such ideals,
\[
\neg I=\{x\in P:\downarrow x\cap I=\varnothing\}.
\]
The comparability graph has an undirected edge whenever two distinct poset points are comparable. Its connected components may include singletons.

## Proof

**1. Counting the Boolean center.** For an ideal \(I\), the equality \(I\cup\neg I=P\) holds exactly when membership in \(I\) is constant on each connected component of the comparability graph. To prove necessity, take \(y\le x\). Downset closure gives \(x\in I\Rightarrow y\in I\). Conversely, if \(y\in I\) while \(x\notin I\), then \(\downarrow x\cap I\ne\varnothing\), so \(x\notin\neg I\), contradicting the equality. Hence membership is also upward closed and constant along all comparability edges. The converse follows because a union of connected components is both upward and downward closed; its complement is exactly its pseudocomplement. There are therefore exactly \(2^c\) excluded-middle solutions.

**2. Counting regular elements.** Write \(M=\min P\), with \(|M|=m\). Every nonempty downset contains a minimal point, so \(\downarrow x\cap I\ne\varnothing\) precisely when some point of \(M\cap I\) lies below \(x\). Hence \(\neg I\) depends only on \(I\cap M\). All \(2^m\) subsets \(S\subseteq M\) occur as ideals; their pseudocomplements are distinct, because at a minimal point \(a\in M\) we have \(a\in\neg S\) exactly when \(a\notin S\). Consequently the negation map has exactly \(2^m\) distinct values. The Heyting identity \(\neg\neg\neg I=\neg I\) implies that the image of negation is precisely the set of double-negation fixed points. Hence there are \(2^m\) such points, establishing the boxed formulas. Each connected component has at least one minimum, so \(k=m-c\ge0\).

**3. All directly indecomposable pairs.** The factorization \(J(P_1\sqcup\cdots\sqcup P_c)\cong\prod_iJ(P_i)\) corresponds to comparability components. Thus a directly indecomposable nontrivial algebra is represented by a connected \(P\), for which \(c=1\). If \(P\) has only one minimum, it has \(N=|J(P)|\ge2\) ideals. Conversely, a chain with \(N-1\) points gives \(N\) ideals and pair \((2/N,2/N)\) for every integer \(N\ge2\).

If connected \(P\) has \(t\ge2\) minima, all \(2^t\) subsets of the minima are distinct ideals, and \(P\) itself is a further ideal, so \(N\ge2^t+1\). Every integer \(N\ge2^t+1\) occurs: take \(t\) incomparable minimal points, place a nonempty chain of \(r=N-2^t\) points above all of them, and order the chain linearly. Its ideals are precisely the \(2^t\) subsets of minima and the \(r\) prefixes reaching the chain, giving \(N=2^t+r\). The paired probabilities are \((2/N,2^t/N)\). This proves exactly \(\mathcal S_{\mathrm{conn}}\).

By decomposition into comparability components, both equations are satisfied in a direct product exactly when they hold in every factor. Their uniform degrees therefore multiply componentwise. Conversely the disjoint union of the explicit connected posets realizes any finite coordinatewise product. The displayed spectrum is complete.

**4. Sharp positive-defect envelopes and rigidity.** For a connected poset component having \(t\) minimal points, put
\[
g(1)=2,\qquad g(t)=2^t+1\quad(t\ge2).
\]
Step 3 shows that the number \(N_i\) of ideals of each component satisfies \(N_i\ge g(t_i)\). For all integers \(a,b\ge1\),
\[
g(a)g(b)\ge 2g(a+b-1).
\]
Equality holds exactly when at least one of \(a,b\) is one. Indeed if \(a=1\) or \(b=1\) it is equality; otherwise the left-minus-right difference is \(2^a+2^b-1>0\). Inducting over the \(c\) components and observing \(\sum_i(t_i-1)=k\) gives, for every \(k\ge1\),
\[
|J(P)|=\prod_iN_i\ge \prod_i g(t_i)
\ge2^{c-1}g(k+1)=2^{c-1}(2^{k+1}+1).
\]
Division of the exact center and regular counts by this lower bound yields the claimed two envelopes.

For equality, each of the componentwise lower bounds and each nontrivial merge must be an equality. Thus exactly one component has more than one minimum; it has \(k+1\) minima, and all other components are singleton points. In the distinguished component, equality means precisely \(2^{k+1}+1\) ideals. Its only ideal not contained in the minimal set must be the entire poset. If the component had two distinct nonminimal points, the principal downset of at least one of them would be a second nonminimal ideal (possibly by taking a point other than a putative greatest one). Hence there is exactly one nonminimal point, which lies above every minimal point by connectedness. Conversely this single-top star has exactly \(2^{k+1}+1\) ideals; adding isolated points multiplies its count and both solution counts by two, so equality remains sharp.

For \(k=0\), every component has one minimum. In each connected component, the ideal count is at least two, with equality only for a singleton. If \(H\) is non-Boolean, at least one component has two or more elements, hence at least three ideals; the product count is at least \(3\cdot2^{c-1}\), giving \(p=q\le2/3\). Equality requires exactly one two-point chain component and all other components isolated, which represents the stated algebra. If every component is isolated, the algebra is Boolean and both probabilities equal one.

**5. Joint law.** Excluded middle implies double-negation elimination, so the four events for a single element have probabilities \(p\), \(0\), \(q-p\), and \(1-q\), respectively, in the order (both), (excluded middle only), (double-negation only), (neither). The spectrum therefore also classifies the full two-bit joint distribution, not just its marginals.

## Verification

The included standalone program `verify_joint.py` independently enumerates all \(5{,}231\) naturally labeled finite posets of sizes one through six, computes every downset and its pseudocomplement directly, and checks the formulas, ratio, sharp bound, and equality characterization. It also tests all connected star-plus-chain constructions for \(2\le t\le5\) minima and \(1\le r\le4\) additional points. Run `python3 verify_joint.py`; the final marker is `JOINT_HEYTING_ALL_CHECKS_PASS enumerated=5231`. These finite calculations support the constructions and detect implementation mistakes; the universal spectrum and inequalities follow from the proofs above, not finite extrapolation.

## Relationship to prior work

Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras* (first public preprint 2021-10-21, arXiv:2110.11515), prove the non-Boolean excluded-middle upper bound \(2/3\) (Theorem 2.4), describe the Boolean center and regular elements (Propositions 1.18–1.21 and 2.12), note the \(2/5\) threshold for unequal center and regular sets (paragraph 1.22), and explicitly raise the classification of relative degrees of one-variable equations (paragraph 6.6). These antecedents and endpoints are prior knowledge. The present result is the exact **simultaneous attainable-pair spectrum**, the integer-power ratio tied to minimal-poset points, the sharp bound at every prescribed defect \(k\), and the equality-case classification. The known results do not themselves state that complete classification. Evans' *Satisfiability degrees for BCK-algebras* (arXiv:2209.13704) studies similar equations on a different class of algebras and does not settle the specified finite Heyting-pair spectrum. The poset representation used here is the classical finite Birkhoff theorem.

## Limitations

The theorem applies to finite nontrivial Heyting algebras with uniform sampling of a **single** element. It does not classify arbitrary pairs of one-variable equations, infinite algebras, or nonuniform sampling. All-size claims have proofs but have not received independent scientific audit. Literature comparisons establish no directly covering statement among inspected sources, not absolute historical priority; equivalent descriptions via finite distributive lattices, Kripke frames, or regular-open nuclei remain a residual priority risk.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (initial public submission 2021-10-21), especially §§1.14–1.22, 2.4, 2.12, 6.4, and 6.6. https://arxiv.org/html/2110.11515v3 ; DOI:10.1017/jsl.2024.2.
2. C. M. Evans, *Satisfiability degrees for BCK-algebras*, arXiv:2209.13704 (2022). https://arxiv.org/abs/2209.13704.
3. G. Birkhoff, finite representation of distributive lattices by order ideals (classical theorem; invoked only in its standard finite form).
