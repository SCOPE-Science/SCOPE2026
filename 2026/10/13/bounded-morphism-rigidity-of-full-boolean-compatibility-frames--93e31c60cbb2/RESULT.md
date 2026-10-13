# Bounded-morphism rigidity of full Boolean compatibility frames
## Finding

Let \(X\) and \(Y\) be nonempty sets, and write \(\mathcal C_X=(\mathcal P(X)^+,R_X)\), with \(\mathcal P(X)^+=\mathcal P(X)\setminus\{\varnothing\}\) and \(A\,R_X\,B\) if and only if \(A\cap B\ne\varnothing\). The full co-consistency frames have the following exact morphism classification:

\[
\operatorname{BMor}(\mathcal C_X,\mathcal C_Y)
\cong \operatorname{Surj}(X,Y),\qquad
q\longmapsto (A\longmapsto q[A]).
\]

Every bounded morphism is necessarily surjective and is uniquely determined by the images of singleton worlds. In particular, full compatibility frames and their bounded morphisms form a category isomorphic to the category of nonempty sets and surjective functions. If \(|X|=n\) and \(|Y|=m\) are positive finite integers, the number of bounded morphisms is \(m!\,{n\brace m}\) for \(m\le n\) and zero for \(m>n\). The assertion includes arbitrary infinite \(X\) and \(Y\).

## Assumptions and scope

A bounded morphism of Kripke frames \(F:(W,R)\to (V,S)\) is a total map satisfying **forth**: \(wRw'\Rightarrow F(w)SF(w')\), and **back**: \(F(w)Sv\Rightarrow (\exists w'\in W)(wRw'\wedge F(w')=v)\). Neither surjectivity nor injectivity is included in its definition. All worlds in \(\mathcal C_X\) and \(\mathcal C_Y\) are *nonempty* subsets, and the relation is nonempty intersection, not inclusion or disjointness. No assumptions of finiteness, compactness, or choice are made.

## Proof

**1. A bounded morphism is onto.** Let \(F:\mathcal C_X\to\mathcal C_Y\) satisfy forth/back. The world \(F(X)\) is nonempty, so \(F(X)\,R_Y\,Y\). The back condition yields a nonempty \(B_0\subseteq X\) with \(F(B_0)=Y\). Consequently, for any nonempty \(C\subseteq Y\), since \(F(B_0)=Y\) meets \(C\), the back condition at \(B_0\) yields some source world \(B_C\) satisfying \(F(B_C)=C\). Thus \(F\) is surjective. Moreover, for every \(y\in Y\), choose a preimage world \(B_y\) of \(\{y\}\). Since \(X\cap B_y\ne\varnothing\), forth implies \(F(X)\cap\{y\}\ne\varnothing\); therefore \(F(X)=Y\). This last argument is pointwise in \(y\) and makes no simultaneous choice.

**2. Singletons have singleton images.** Fix \(x\in X\). Suppose that distinct \(y,z\) both belong to \(F(\{x\})\). The back condition at \(\{x\}\), first with the target world \(\{y\}\) and then with \(\{z\}\), produces nonempty source worlds \(B_y,B_z\) such that \(x\in B_y\cap B_z\), \(F(B_y)=\{y\}\), and \(F(B_z)=\{z\}\). Forth applied to \(B_y\,R_X\,B_z\) would make the disjoint target singletons intersect, a contradiction. Hence \(F(\{x\})=\{q(x)\}\) for a uniquely defined \(q(x)\in Y\). Since the values are unique, these assignments define a function \(q:X\to Y\) without a choice principle.

**3. All world images are direct images.** For any nonempty \(A\subseteq X\) and every \(x\in A\), singleton \(\{x\}\) meets \(A\). Forth implies \(\{q(x)\}\cap F(A)\ne\varnothing\), so \(q[A]\subseteq F(A)\). Conversely fix \(y\in F(A)\). By back at \(A\) with target \(\{y\}\), there exists a nonempty \(B\subseteq X\) meeting \(A\) and satisfying \(F(B)=\{y\}\). Any \(x\in A\cap B\) satisfies \(\{q(x)\}\cap\{y\}\ne\varnothing\) by forth, hence \(q(x)=y\). Thus \(F(A)\subseteq q[A]\), yielding \(F(A)=q[A]\). Applied to \(A=X\), step 1 gives \(q[X]=F(X)=Y\). Thus \(q\) is surjective and uniquely recovered from \(F\).

**4. Converse.** Suppose \(q:X\twoheadrightarrow Y\). For each nonempty \(A\subseteq X\), set \(F_q(A)=q[A]\). This is nonempty and preserves intersection-nonemptiness in the forward direction. For back, if \(q[A]\cap C\ne\varnothing\), where \(C\subseteq Y\) is nonempty, the set \(B=q^{-1}[C]\) is nonempty, meets \(A\), and satisfies \(q[B]=C\) by surjectivity of \(q\). Therefore \(F_q\) is a bounded morphism. Identities and composition satisfy \(F_{\mathrm{id}}=\mathrm{id}\) and \(F_{r\circ q}=F_r\circ F_q\), completing the categorical statement.

**5. Enumeration.** When \(X\) and \(Y\) have positive finite sizes \(n,m\), surjections exist exactly for \(m\le n\); their number is the classical count \(m!\,{n\brace m}\), obtained by partitioning the domain into \(m\) nonempty unlabeled fibers and then labeling them. The classification makes this count exact for bounded morphisms.

## Verification

The accompanying self-contained Python program exhaustively generates every map between the world sets for \((n,m)=(1,1),(1,2),(2,1),(2,2),(3,1),(3,2),(3,3)\). It directly checks forth and back and compares the surviving maps with independently generated direct-image maps of surjections. It checks \(825{,}763\) total candidate world maps across these pairs, and finds exactly the predicted morphisms. The finite computations are auxiliary sanity checks: the general finite/infinite theorem follows from the explicit proof above.

To reproduce, run `python3 verify.py` with Python 3 and no dependencies.

## Relationship to prior work

Jockwich, Tarafder and Venturi study internal modal forcing via Boolean co-consistency \(aRb\iff a\wedge b\ne0\), including the nonzero part of complete atomic Boolean algebras. Their Section 6, Lemma 6.13 embeds a smaller power-set algebra into a larger one by a partition of its atoms, and their Sections 5–6 analyze modal validities. That partition embedding is a relevant known construction, but does not itself classify **all** forth-and-back morphisms between the **full** corresponding nonzero frames. The two-atom target is a special case of the present statement and not an additional distinct contribution. Ordinary powerset inverse-image maps and surjection/partition counts are standard background; the asserted contribution is the necessity-and-sufficiency classification in the co-consistency Kripke category, for arbitrary source and target sets, with its categorical and finite enumerative consequences.

## Limitations

Only *full* nonzero power-set/complete atomic Boolean frames are covered. Arbitrary induced subframes, atomless Boolean algebras, and frames whose relation is reverse inclusion are different settings. The result does not identify modal logics, axiomatize forcing, or imply analogous rigidity for those broader objects. The count is for bounded morphisms as defined above and not arbitrary relation-preserving maps. All scientific checks here are non-independent; equivalent earlier formulations in categorical or Boolean duality literature remain a residual originality risk.

## References

1. Santiago Jockwich, Sourav Tarafder, Giorgio Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977v1 (first public posting 2026-07-28); especially Definition 5.1 and Lemma 6.13, and Sections 5–6. Full text also reproduced at https://www.scribd.com/document/1055209628/Modalities-and-Boolean-valued-Models.
2. Standard Kripke-frame theory: bounded (forth/back) morphisms. Standard combinatorics: the Stirling-number enumeration of surjections.
