# Prefix-surjective bounded morphisms of finite weak-Pierce frames: rank and idempotent spectra

## Finding
For finite weak-order Kripke frames whose antichain levels each have at least two worlds, every bounded morphism has a unique **surjective prefix followed either by one constant terminal tail or by an arbitrary last-level map**. This is an exact normal form for all bounded morphisms between any two such frames, regardless of their heights. It yields a closed formula for their cardinalities and complete image-rank and idempotent spectra for endomorphisms.

Write \(P(\mathbf a)=A_1\oplus\cdots\oplus A_h\), with higher levels first and \(|A_i|=a_i\ge2\), and \(Q(\mathbf b)=B_1\oplus\cdots\oplus B_k\), with \(|B_i|=b_i\ge2\). An ordinal sum here means every point of an earlier level is above every point of a later level; distinct points within a level are incomparable. Define
\[
s(m,n)=\sum_{u=0}^{n}(-1)^u\binom nu(n-u)^m,
\]
the number of surjections from a labelled set of size \(m\) onto a labelled set of size \(n\). Empty products are one. Then
\[
\left|\operatorname{PM}(P(\mathbf a),Q(\mathbf b))\right|
=\sum_{j=1}^{\min(h-1,k)}b_j\prod_{i<j}s(a_i,b_i)
+\mathbf 1_{h\le k}\,b_h^{a_h}\prod_{i<h}s(a_i,b_i).
\]
The formula includes the one-level source case \(h=1\).

For \(P=P(\mathbf a)\), let \(R_{\mathbf a}(z)=\sum_f z^{|f(P)|}\) sum over bounded endomorphisms. Then
\[
R_{\mathbf a}(z)=
\sum_{j=1}^{h-1}a_j\left(\prod_{i<j}a_i!\right)z^{1+\sum_{i<j}a_i}
+\left(\prod_{i<h}a_i!\right)
\sum_{t=1}^{a_h}\binom{a_h}{t}s(a_h,t)z^{t+\sum_{i<h}a_i}.
\]
In addition, the numbers of idempotent bounded endomorphisms and automorphisms are, respectively,
\[
I(P)=\sum_{j=1}^{h-1}a_j+\sum_{t=1}^{a_h}\binom{a_h}{t}t^{a_h-t},\qquad
|\operatorname{Aut}(P)|=\prod_{i=1}^h a_i!.
\]
For example, when \(\mathbf a=(2,2,2)\), \(R_{\mathbf a}(z)=2z+4z^3+8z^5+8z^6\), with \(22\) endomorphisms, \(7\) idempotents and \(8\) automorphisms.

## Assumptions and scope
All frames are finite, nonempty, and have at least two incomparable points in **every** level, including the top and bottom. The source and target heights \(h,k\) are positive integers and may differ. Levels are labelled sets. The map \(f:P\to Q\) is a bounded morphism precisely when \(f(\uparrow x)=\uparrow f(x)\) for every \(x\in P\); isotonicity follows from this equality. Image rank in the polynomial is **cardinality of the image set of the dual frame map**, not linear-algebra rank or the size of the image Heyting algebra. The corresponding Heyting-algebraic endomorphisms are obtained by inverse image on upsets under finite Esakia duality.

## Proof
**Step 1: A permitted-image lemma.** For \(x\in A_i\), put \(S_i=\bigcup_{r<i}f(A_r)\). Since \(\uparrow x=\{x\}\cup\bigcup_{r<i}A_r\), the bounded-morphism condition is exactly
\[
S_i\cup\{f(x)\}=\uparrow f(x).
\]
For \(y\in B_j\), \(\uparrow y=(B_1\cup\cdots\cup B_{j-1})\cup\{y\}\). In particular \(S_1=\varnothing\) forces \(f(A_1)\subseteq B_1\).

**Step 2: Exhaustive prefix/tail alternatives.** Suppose the preceding \(i-1\) source levels have each mapped onto the corresponding distinct target levels \(B_1,\ldots,B_{i-1}\). Then \(S_i=B_1\cup\cdots\cup B_{i-1}\). Since each \(B_r\) contains at least two points, the permitted-image lemma forces \(f(A_i)\subseteq B_i\), and this is impossible if \(i>k\). If \(i<h\), three cases exhaust the possibilities. When \(f(A_i)=B_i\), the prefix continues. When \(f(A_i)=\{y\}\subseteq B_i\), the next and every subsequent source level must map entirely to \(y\), since \(S_{i+1}=B_1\cup\cdots\cup B_{i-1}\cup\{y\}\) and all target levels have size at least two. A proper image of \(A_i\) containing at least two but fewer than \(b_i\) points cannot admit a value for any point of \(A_{i+1}\): a value in \(B_i\) would require the preceding image there to be a singleton, while a value in \(B_{i+1}\) would require it to be all of \(B_i\); other target levels contradict the form of an upper cone. Thus this case is impossible. Induction gives either a terminal index \(j<h\) with bijection-free surjective maps on every earlier level followed by one constant tail, or \(h\le k\) and a surjection on levels \(1,\ldots,h-1\) followed by any map \(A_h\to B_h\). Conversely, every listed map satisfies the displayed upper-cone equality, so the normal form is necessary and sufficient and its parameters are unique.

**Step 3: Exact hom-set count.** For a terminal index \(j<h\), each earlier level contributes \(s(a_i,b_i)\) surjections, and the terminal world has \(b_j\) choices. Such a terminal index must satisfy \(j\le k\). The unrestricted final-level case exists only when \(h\le k\) and has \(b_h^{a_h}\) choices after the prefix surjections. The displayed cardinality formula follows by disjointness of the normal forms.

**Step 4: Endomorphism image ranks.** Specialize to \(P=Q\). Every surjection \(A_i\to A_i\) is a permutation, contributing \(a_i!\) choices. A terminal tail at level \(j<h\) has image \(A_1\cup\cdots\cup A_{j-1}\cup\{y\}\), hence size \(1+\sum_{i<j}a_i\). In the unrestricted last-level case the image has size \(\sum_{i<h}a_i+t\) exactly when the last-level map has image size \(t\). There are \(\binom{a_h}{t}s(a_h,t)\) such last-level maps. Summing yields \(R_{\mathbf a}(z)\).

**Step 5: Idempotents and units.** An idempotent surjective self-map of a finite set is the identity. Thus any idempotent terminal-tail map is the identity on its earlier levels and constant on its tail, giving exactly \(a_j\) options at each \(j<h\). In the final-level case earlier permutations must be identities, while an idempotent self-map of \(A_h\) with exactly \(t\) fixed image points is obtained by choosing the image and sending each remaining point into it, giving \(\binom{a_h}{t}t^{a_h-t}\) choices. A bounded self-map is bijective only in the unrestricted last-level case with permutations on every level, yielding the product of factorials.

## Verification
Two standalone Python programs accompany this statement. `verify_weakorder.py` enumerates all functions between selected small source and target frames and independently tests the actual upper-cone equality; it compares counts, image-rank distributions and idempotent counts to the stated formulas. `verify_algebra.py` checks the corresponding equality between the bounded-morphism criterion and preservation of finite Heyting implication on all upsets of selected small frames. Both programs terminate with explicit `VERIFY_OK`/`ALGEBRA_OK` indicators and were executed from their packaged text.

## Relationship to prior work
Bezhanishvili, Bezhanishvili, Moraschini and Stronkowski (2021), especially Section 2.1 and Section 3, establishes the finite Esakia duality and identifies Boolean cascades as the finite weak-order spectra relevant to weak Pierce logic. Those results establish the setting and the correspondence between bounded morphisms and Heyting homomorphisms; they do **not** state the specialized prefix/tail normal form or its joint hom-set, image-rank and idempotent enumerators in the inspected text. Ordinary monotone-map enumeration on finite weak orders is a weaker categorical condition: monotone maps need not be bounded morphisms and their total count does not determine these enumerators. General literature on endomorphism monoids of complete Heyting algebras addresses broader representation questions, not necessarily these precise finite profiles.

## Limitations
The non-singleton-level hypothesis is essential to this normal form. If a target level is a singleton, a bounded morphism can mix images in that singleton level and the next one, so the formula is not claimed in that case. The exact counting identities are proved for all finite parameters, while finite exhaustive tests only check explicitly listed small instances. No uniqueness within the entire mathematical literature or independent external certification is claimed. Earlier equivalent formulations in the literature on Esakia equivalences, finite bounded morphisms and transformation semigroups cannot be ruled out absolutely.

## References
1. G. Bezhanishvili, N. Bezhanishvili, T. Moraschini and M. Stronkowski, *Profiniteness and representability of spectra of Heyting algebras*, arXiv:2103.02530 (first publicly available 3 March 2021), §§2.1, 3. https://arxiv.org/abs/2103.02530
2. A. Pultr and J. Sichler, *Endomorphisms of complete Heyting algebras*, Semigroup Forum 54 (1997), 364–374, DOI:10.1007/BF02676617. General background and an incompletely inspected potential overlap, not used in the proof.
