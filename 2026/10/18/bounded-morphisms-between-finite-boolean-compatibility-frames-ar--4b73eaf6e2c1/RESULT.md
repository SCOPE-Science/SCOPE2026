# Bounded morphisms between finite Boolean compatibility frames are precisely atom surjections

## Finding

For positive integers \(n,m\), define the finite frame
\[
G_n=(\mathcal P([n])\setminus\{\varnothing\},R_n),
\qquad A\,R_n\,B\iff A\cap B\ne\varnothing.
\]
Its worlds are the nonzero elements of the Boolean algebra on \(n\) atoms, with the compatibility (co-consistency) accessibility relation. A map \(F:G_n\to G_m\), not presumed surjective, is a bounded morphism if it preserves accessibility (**forth**) and satisfies the usual successor-lifting condition (**back**).

**Classification theorem.** For every \(n,m\ge1\), the bounded morphisms \(F:G_n\to G_m\) are exactly
\[
F_g(A)=g[A]\qquad(\varnothing\ne A\subseteq[n]),
\]
where \(g:[n]\twoheadrightarrow[m]\) is a surjection. The inducing map \(g\) is unique. In particular, the bounded-morphism conditions force \(F\) to be surjective without any such assumption.

The exact number of bounded morphisms is
\[
|\operatorname{BMor}(G_n,G_m)|
=|\operatorname{Surj}([n],[m])|
=m!\left\{\!\begin{matrix}n\\m\end{matrix}\!\right\}
=\sum_{j=0}^{m}(-1)^{m-j}\binom mj j^n,
\]
where the braces are Stirling numbers of the second kind and their value is zero when \(n<m\). Consequently the automorphism group of \(G_n\) is precisely the symmetric group \(S_n\), and every bounded endomorphism is an automorphism. Direct image gives a fully faithful functor from the category of nonempty finite sets and surjections to the category of Kripke frames and bounded morphisms, restricted to its essential image.

## Assumptions and scope

Throughout, \(n,m\) are positive integers and \([n]=\{1,\ldots,n\}\). All subsets used as worlds are **nonempty**. The accessibility relation contains loops (each nonempty subset meets itself). Frames are considered with ordinary classical Kripke semantics; no restriction from translated atomic valuations is imposed on morphisms.

A function \(F: G_n\to G_m\) obeys:

**Forth:** for all nonempty source subsets \(A,B\), \(A\cap B\ne\varnothing\) implies \(F(A)\cap F(B)\ne\varnothing\).

**Back:** for every nonempty source subset \(A\) and every nonempty target subset \(C\) with \(F(A)\cap C\ne\varnothing\), there exists a nonempty \(B\subseteq[n]\) with \(A\cap B\ne\varnothing\) and \(F(B)=C\).

No surjectivity hypothesis is included. These are exactly the standard bounded-morphism conditions for the two specified accessibility relations. The result does **not** classify maps between arbitrary induced subframes, nor morphisms preserving translated valuations.

## Proof

**1. Images of atoms are singletons.** Fix \(i\in[n]\). Suppose \(F(\{i\})\) contains two distinct points \(j,k\in[m]\). The singleton target worlds \(\{j\}\) and \(\{k\}\) each intersect \(F(\{i\})\). By back, there exist source worlds \(B_j,B_k\) meeting \(\{i\}\), with
\[
F(B_j)=\{j\},\qquad F(B_k)=\{k\}.
\]
Both contain \(i\), hence \(B_j\,R_n\,B_k\). Forth implies \(\{j\}\,R_m\,\{k\}\), contrary to \(j\ne k\). Thus \(F(\{i\})\) is a singleton. Write it as \(\{g(i)\}\). This defines a unique map \(g:[n]\to[m]\).

**2. Every image is a direct image.** Fix \(\varnothing\ne A\subseteq[n]\). If \(i\in A\), then \(\{i\}\,R_n\,A\), so forth gives \(g(i)\in F(A)\). Consequently \(g[A]\subseteq F(A)\).

For the reverse inclusion, choose \(j\in F(A)\). As \(F(A)\cap\{j\}\ne\varnothing\), back supplies \(B\subseteq[n]\), nonempty, with \(A\cap B\ne\varnothing\) and \(F(B)=\{j\}\). Pick \(i\in A\cap B\). Forth applied to \(\{i\}\,R_n\,B\) yields \(\{g(i)\}\cap\{j\}\ne\varnothing\), so \(j=g(i)\in g[A]\). Hence
\[
F(A)=g[A]
\]
for every nonempty \(A\).

**3. The atom map is surjective.** The full target world \([m]\) intersects \(F([n])\), since the latter is nonempty. Back at the source world \([n]\) and target world \([m]\) gives a source world \(B\) with \(F(B)=[m]\). By Step 2, \([m]=g[B]\subseteq g[[n]]\subseteq[m]\), hence \(g\) is onto. This proves the necessity direction, including automatic surjectivity of \(F\).

**4. Conversely, every atom surjection induces a bounded morphism.** Let \(g:[n]\twoheadrightarrow[m]\), and define \(F_g(A)=g[A]\). Images of nonempty worlds are nonempty. If \(A\cap B\) contains \(i\), then \(g(i)\in g[A]\cap g[B]\); so forth holds. If \(g[A]\cap C\ne\varnothing\), choose \(i\in A\) with \(g(i)\in C\). For each \(c\in C\) choose a preimage \(i_c\in[n]\) with \(g(i_c)=c\), and set
\[
B=\{i\}\cup\{i_c:c\in C\}.
\]
Then \(A\cap B\ne\varnothing\) and \(g[B]=C\), establishing back. Finiteness makes the representative choices elementary. Thus \(F_g\) is a bounded morphism.

**5. Enumeration, uniqueness, and composition.** The value of \(F_g\) on \(\{i\}\) is \(\{g(i)\}\), so distinct \(g\) give distinct \(F_g\). Surjections \([n]\to[m]\) are counted by \(m!\) times the number of partitions of \([n]\) into \(m\) nonempty blocks, or equivalently by the displayed inclusion-exclusion sum. If \(g:[n]\to[m]\) and \(h:[m]\to[\ell]\) are surjective, then
\[
F_h(F_g(A))=h[g[A]]=(h\circ g)[A]=F_{h\circ g}(A).
\]
The identity map is also preserved. A surjective \(g:[n]\to[n]\) is a permutation, giving exactly \(n!\) bounded endomorphisms, all invertible. A bounded frame automorphism must arise this way.

## Verification

The accompanying self-contained Python program `verify.py` tests the **unrestricted** forth/back definitions, rather than using the proof's claimed form as a filter. For each \(1\le n,m\le3\), it enumerates every function from the world set of \(G_n\) to that of \(G_m\), checks forth and back directly, and verifies that the accepted maps are exactly those independently generated from atom surjections. This comprises \(826{,}113\) candidate functions. The resulting bounded-morphism counts, row-by-row for \(n=1,2,3\) and \(m=1,2,3\), are \((1,0,0)\), \((1,2,0)\), and \((1,6,6)\). It also directly verifies both conditions on \(852\) induced maps with \(1\le n\le6\) and \(1\le m\le\min(n,3)\). All tests passed.

Reproduction requires only Python 3: run `python verify.py`. The proof of the theorem for arbitrary positive integers is Steps 1–5, **not** a conclusion inferred from these finite calculations.

## Relationship to prior work

Jockwich, Tarafder, and Venturi introduce the Boolean compatibility relation for an internal modal logic of forcing and discuss finite nonzero power-set frames. Their Lemma 6.13 uses a partition of atoms to construct a Boolean subalgebra embedding and derive inclusions between finite-stage logics. These embeddings correspond to inverse-image maps of atom surjections. The lemma neither identifies **all** bounded morphisms between the full nonzero frames nor proves that every bounded morphism is forced to arise from an atom surjection, and it does not count these morphisms.

A separate published study, *Every finite stage of the internal forcing logic hierarchy is strict*, establishes the largest complete-graph bounded-morphic quotient among induced subframes, using a sharp domatic number. That result concerns targets that are complete reflexive graphs and **does not** classify bounded morphisms with target another full compatibility frame \(G_m\). In particular, its quotient bound does not imply the present uniqueness or hom-set enumeration.

The familiar classification of Boolean subalgebra embeddings by partitions is **not** itself the present theorem: it describes algebra homomorphisms, while the current proof shows the modal forth/back axioms alone compel direct-image behavior on every nonempty subset. The structural implication from arbitrary bounded morphisms to such atom maps is the additional point.

## Limitations

The classification depends on having **every** nonempty subset as a world and on the intersection-based accessibility relation. Arbitrary induced subframes, non-Boolean underlying lattices, and valuation-preserving model morphisms are outside its scope. It makes no claim about infinite sets, where additional choice issues could arise. No optimal modal formulas or individual finite-stage axiomatizations are claimed. An equivalent formulation in the broader graph-homomorphism literature could exist under terminology not detected by the literature comparisons.

## References

[1] Santiago Jockwich, Sourav Tarafder, and Giorgio Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977, publicly posted 28 July 2026; especially Definition 3.5 and Lemma 6.13. https://arxiv.org/abs/2607.25977

[2] *Every finite stage of the internal forcing logic hierarchy is strict*, publicly available mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-every-finite-stage-of-the-internal-forcing-logic-hierarchy-is-st--069a2c03aeb3.

[3] Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge University Press, 2001; for standard bounded-morphism terminology.
