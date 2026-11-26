# The first reducibility transition for commuting pairs in exterior algebras

## Finding

Let \(k\) be algebraically closed of characteristic different from two, and let \(E_n=\bigwedge_k k^n\) be the unital associative exterior algebra. The reduced variety of ordered pairs with ordinary commutator zero is irreducible for \(1\le n\le5\). It first becomes reducible at \(n=6\). The two rational components at this boundary have dimensions \(112\) and \(115\). They are the closure of the locus where the first member has nonzero degree-one part, and the closed locus where both degree-one parts vanish and the two degree-three parts have wedge product zero. The contribution here is the first-generator-number boundary, including the proof of irreducibility through five; the six-generator fiber calculation makes the boundary self-contained. Both finite-field counts below are included for comparison, not as novelty claims.

## Proof

Even elements are central. By graded commutativity, the ordinary commutator is twice the wedge product of the odd parts. Thus the even coordinates give a free affine factor of dimension \(2^n\). Write the two odd parts as \(u=u_1+u_3+u_5\) and \(v=v_1+v_3+v_5\), omitting nonexistent degrees. The conditions are
\[
u_1\wedge v_1=0,\qquad u_1\wedge v_3+u_3\wedge v_1=0,\qquad
u_1\wedge v_5+u_3\wedge v_3+u_5\wedge v_1=0,
\]
with equations beyond the top degree omitted.

On the open locus \(u_1\ne0\), one has \(v_1=c u_1\). Writing \(V=ku_1\oplus W\), the degree-four condition means \(v_3-c u_3\in u_1\wedge\bigwedge^2W\), where present (for \(n=3\) both sides of this kernel description equal \(\bigwedge^3 V\)). If \(n=6\), the last equation is one affine constraint on \(v_5\), since wedging by \(u_1\) maps \(\bigwedge^5 V\) onto \(\bigwedge^6 V\). These descriptions are affine-space bundles in local coordinates on the charts of \(V\setminus\{0\}\); they give an irreducible rational open locus for each \(n\). In odd coordinates its dimensions at \(n=5,6\) are respectively \(5+1+10+6+1+1=24\) and \(6+1+20+10+6+5=48\). At any commuting pair with \(u_1=0\), \(v_1\ne0\), the arc \((u+t v,v)\) is commuting since \(v\wedge v=0\) and has nonzero first linear part for \(t\ne0\).

To prove irreducibility through five, suppose now \(u_1=v_1=0\). Their higher odd parts commute because their wedge product has degree at least six. Choose \(w\in V\setminus\{0\}\) with \(w\wedge v_3=0\). For \(n\le4\) this is possible by comparing the dimensions of \(V\) and \(\bigwedge^4 V\), or taking any nonzero \(w\) when \(v_3\) is absent. For \(n=5\) identify \(\bigwedge^4 V\) with \(V^*\) using a volume form. Then \(w\mapsto w\wedge v_3\) corresponds, up to sign, to the alternating bilinear pairing with values given by \(w\wedge z\wedge v_3\). Every odd-dimensional alternating form has a nontrivial kernel. The arc \((u+t w,v)\) stays commuting, as the only new possibly nonzero product is \(t w\wedge v_3\). Thus every pair lies in the closure of the one irreducible open locus.

For \(n=6\), the closed locus \(u_1=v_1=0\) is instead the locus \(u_3\wedge v_3=0\), with \(u_5,v_5\) free. Complementary exterior basis monomials give a perfect alternating pairing on the 20-dimensional space of degree-three forms. Its bilinear equation in the 40 coordinates of \((u_3,v_3)\) has symmetric polar form of rank 40; a product of linear forms would have polar rank at most two. Hence its hypersurface is irreducible of dimension 39. It is rational by solving for one coordinate where its coefficient is nonzero. The two degree-five forms add twelve free coordinates, so this closed locus has odd-coordinate dimension 51. It is not contained in the 48-dimensional closure of the open locus, and the open locus is not contained in it. The previous arc for \(v_1\ne0\) shows the union of these two closed irreducible sets exhausts the variety. Adding the 64 even coordinates gives the claimed dimensions.

## Finite-field comparison

Let \(q\) be odd. For each fixed rank-one ordered pair \((u_1,v_1)\), a change of basis of the ordered pair reduces to a nonzero first linear part and zero second linear part. For each such fixed pair the number of choices of higher odd components is \(q^{18}\) for \(n=5\) and \(q^{41}\) for \(n=6\), by the open-locus equations above with the linear data fixed. There are \((q^n-1)(q+1)\) such ordered linear pairs. With both linear parts zero, the count is \(q^{22}\) for \(n=5\); for \(n=6\), separate \(u_3=0\) from \(u_3\ne0\), obtaining \(q^{12}[q^{20}+(q^{20}-1)q^{19}]\) by the perfect pairing. Multiplying by the number of choices of even coordinates and expanding gives
\[
\begin{aligned}
\#\mathcal C_5(\mathbb F_q)&=q^{56}+q^{55}+q^{54}-q^{51}-q^{50},\\
\#\mathcal C_6(\mathbb F_q)&=q^{115}+q^{112}+q^{111}-q^{106}-q^{105}+q^{96}-q^{95}.
\end{aligned}
\]
The five-generator expression is also obtained from its centralizer ranks [3]. The six-generator expression is exactly the commuting probability in [4] multiplied by \(q^{128}\). The counting proof here identifies the contribution of each linear-degree stratum but does not claim either polynomial is new.

## Relationship to prior work

Domokos–Zubor [1] and Bovdi–Leung [2] analyze commutative subalgebras; the former treats square-zero odd subspaces and the alternating top-degree pairing. These subalgebra results do not state the first reducibility boundary for the ordered-pair geometry. The related six-generator tuple study [5] is stated for tuple lengths at least three, expressly mentions the separately obtained two-component pair dimensions, and verifies the matching pair-count specialization. Its rank-one chart and isotropic-tuple argument specialize to length two and give the same six-generator geometry; no exclusive priority is claimed for that classification in isolation. It does not address irreducibility for pairs with fewer than six generators. The lower-generator arc argument and the two-component calculation together establish the sharp generator-number threshold without assuming a classification of maximal commutative subalgebras.

## Verification and scope

The accompanying `verify.py` checks exterior-multiplication ranks over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), the six-generator pairing, the forced five-generator kernel and the polynomial count identities. The all-characteristic-different-from-two geometry follows from the proof, not from those finite checks. No assertion concerns the original commuting scheme's reducedness, normality or embedded structure, characteristic two, or \(n\ge7\).

## References

1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916, https://arxiv.org/abs/1403.2916.
2. V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457, https://arxiv.org/abs/1803.03457.
3. Resultary record `2026/11/2/SCOPE-commuting-pair-threshold-in-fourth-order-grassmann-algebras-and--b94809d1e9e0`, five-generator centralizer table.
4. *Six centralizer dimensions and an exact commuting law for the six-generator exterior algebra*, Resultary record `2026/10/25/SCOPE-six-centralizer-dimensions-and-an-exact-commuting-law-for-the-si--1480b4c744ea`.
5. *Two rational components and exact finite-field counts for commuting tuples in the six-generator exterior algebra*, Resultary record `2026/10/26/SCOPE-two-rational-components-and-exact-finite-field-counts-for-commut--588618941429`, Proof §§2–5 and Relationship to prior work.
