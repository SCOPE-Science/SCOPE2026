# Exact normal form and census of modal expansions of finite diamond lattices

## Finding

Let \(n\ge 3\), and let \(M_n=\{0,1,a_1,\ldots,a_n\}\) be the bounded lattice with \(n\) pairwise incomparable atoms, so distinct atoms have meet \(0\) and join \(1\). A **modal expansion** is an ordered pair of maps \(\Box,\Diamond:M_n\to M_n\) satisfying Definition 4.10 of Bezhanishvili–Dmitrieva–de Groot–Moraschini [1]:
\[
\Box1=\Diamond1=1,\qquad
\Box(x\wedge y)=\Box x\wedge\Box y,\qquad
x\le y\Longrightarrow\Diamond x\le\Diamond y,\qquad
\Diamond x\wedge\Box y\le\Diamond(x\wedge y).
\]
There is no additional assumption that \(\Diamond\) preserves joins or bottom. Put
\[
P_n=\sum_{r=0}^{n}\binom nr^2r!,\qquad
Q_n=\sum_{r=2}^{n}\binom nr^2r!\,(n-r+1)^{n-r}.
\]
The exact number of expansions on the **fixed labelled lattice** \(M_n\) is
\[
\boxed{N_n=1+P_n+(n+2)^n+2n^{n+1}+Q_n
          +n(n+2)2^n+n^3(n-1)+3n^2+3n.}
\]
In particular \(N_3=574\), \(N_4=5054\), \(N_5=70834\), and \(N_6=1332432\). Under simultaneous conjugation of both maps by the automorphism group \(S_n\) of the underlying diamond lattice, the counts of **isomorphism classes** are exactly \(126\) for \(n=3\) and \(325\) for \(n=4\).

A complete normal form is given by the five disjoint cases in the proof. Thus the displayed formula counts every such modal expansion, not merely a subclass.

## Assumptions and scope

The carrier is \(M_n\) for arbitrary integer \(n\ge3\), with atoms distinctly labelled only for the first count. All modal axioms are exactly those specified above. For the orbit count, an isomorphism of modal expansions is a lattice automorphism commuting with both modal maps. The first genuinely nondistributive member of this family is \(M_3\), with five lattice elements; \(M_2\) is the four-element Boolean lattice. Nothing is asserted about other varieties of modal lattices, arbitrary finite lattices, or isomorphism counts for \(n\ge5\).

## Proof

**1. Local axiom reduction.** Write \(B=\Box\), \(D=\Diamond\), \(z=B0\), and \(t=D0\). Meet preservation and top preservation make \(B\) monotone; \(D\) is monotone by assumption. The Dunn inequality at \(x=1\) gives \(B u\le D u\) for every \(u\), including \(z\le t\). Every other pair \((x,y)\in M_n^2\) in the Dunn inequality is then automatic except the pairs of distinct atoms. Hence the necessary and sufficient remaining tests are
\[
 z\le t,\qquad B a_i\le D a_i\ (1\le i\le n),\qquad
 B a_i\wedge D a_j\le t\ (i\ne j).
\]
Indeed, the cases \(x=0\) are bounded by \(t\), cases \(y=0\) follow from \(B0\le t\), cases involving \(1\) are the displayed diagonal inequality or tautologies, and the equal-atom case is tautological. Distinct-atom meets are \(0\). In addition, \(B a_i\wedge B a_j=z\) for \(i\ne j\).

**2. Shape of the meet map.** When \(z=1\), all \(B a_i=1\). When \(z=c\) is an atom, each \(B a_i\in\{c,1\}\), and at most one image can be \(1\), yielding \(n+1\) possible meet maps for each \(c\). When \(z=0\), either (i) the nonzero atom-images define an injective partial map from the \(n\) source atoms to the \(n\) target atoms, with all other atom-images zero, or (ii) exactly one source atom maps to \(1\) and all others to \(0\). In alternative (i), rank \(r\) has precisely \(\binom nr^2r!\) maps. Hence there are \(P_n+n\) meet maps when \(z=0\).

**3. Case \(z=1\).** Since \(z\le t\), all values of both maps are \(1\), contributing \(1\).

**4. Case \(z=c\) for an atom \(c\).** Necessarily \(t=c\) or \(t=1\). If \(t=1\), all \(D a_i=1\) and any of the \(n+1\) meet maps is permitted. If \(t=c\), a meet map sending every source atom to \(c\) permits independent \(D a_i\in\{c,1\}\), contributing \(2^n\). A meet map with its unique \(B a_i=1\) forces \(D a_i=1\) and \(D a_j=c\) at all other atoms, contributing \(n\). Thus summing over all \(n\) choices of \(c\) gives \(n(2n+1+2^n)\).

**5. Case \(z=0,t=1\).** Monotonicity forces \(D\) to be constantly \(1\), while any of the \(P_n+n\) meet maps is allowed. Contribution: \(P_n+n\).

**6. Case \(z=0,t=c\) for an atom \(c\).** Each \(D a_i\) equals either \(c\) or \(1\). There are three and only three possibilities for \(B\):

(a) All images are zero except for at most one image \(c\). There are \(n+1\) such maps, each allowing all \(2^n\) choices of the diamond atom-values.

(b) There is exactly one source with an atom-image other than \(c\); optionally a different source maps to \(c\). There are \(n(n-1)[1+(n-1)]=n^2(n-1)\) such maps. At the exceptional source \(D=1\), and elsewhere \(D=c\), uniquely.

(c) Exactly one source has \(B=1\), all others have \(B=0\). There are \(n\) such meet maps, each forcing the diamond map uniquely as in (b).

Two different non-\(c\) atom-images are impossible because each would force its diamond value to \(1\), contradicting the distinct-atom Dunn test at the other image. The contribution for all atoms \(c\) is
\[n\bigl((n+1)2^n+n^2(n-1)+n\bigr).\]

**7. Case \(z=t=0\).** If every atom-image of \(B\) is zero, the diamond atom-values are arbitrary and contribute \((n+2)^n\). If \(B\) is a rank-one partial injection, there are \(n^2\) choices of its source and target; the diamond value at that source is either its target atom or \(1\), and each of the remaining \(n-1\) diamond atom-values has \(n\) choices (zero or one of the \(n-1\) other atoms). This gives \(2n^{n+1}\). If \(B\) has partial-injection rank \(r\ge2\), the diamond value at each active atom is forced to be its corresponding target atom: choosing \(1\) would violate the cross-atom test at another active source. At each of the \(n-r\) inactive sources, the diamond may take \(0\) or an atom not used in the injection, giving \(n-r+1\) choices independently. This contributes \(Q_n\). Finally, if exactly one atom maps to \(1\) under \(B\), all remaining diamond atom-values are forced to zero, contributing \(n\). Total:
\[
(n+2)^n+2n^{n+1}+Q_n+n.
\]

**8. Summation.** Add the disjoint contributions from Steps 3–7 and rearrange. The sum is exactly the boxed \(N_n\). The argument uses only the defining equations and holds for every \(n\ge3\).

**9. Isomorphism counts.** Every lattice automorphism of \(M_n\) fixes \(0,1\) and permutes its atoms, giving precisely \(S_n\). It acts on a pair of maps by simultaneous conjugation. Complete enumeration of valid pairs for \(n=3\) yields \(574\) fixed by the identity, \(52\) by each transposition, and \(13\) by each three-cycle. Burnside's lemma gives \((574+3\cdot52+2\cdot13)/6=126\). At \(n=4\), the corresponding fixed counts by cycle type are \(5054\) (identity), \(316\) (one transposition), \(86\) (two transpositions), \(62\) (three-cycle), and \(16\) (four-cycle). Thus
\[
(5054+6\cdot316+3\cdot86+8\cdot62+6\cdot16)/24=325.
\]
The supplied exhaustive verifier independently implements the modal equations and automorphism action directly, rather than simply grouping the cases of the proof.

## Verification

Execute `python3 verify.py` using Python 3 standard library. For \(n=3,4\), it constructs every top-preserving meet map and every top-preserving monotone diamond map, tests the Dunn inequality for *all ordered pairs* of lattice elements, compares the exact result against the closed formula, and obtains the fixed-point data by explicit atom-permutation conjugation. The independently checked totals are \(574,5054\), with \(126,325\) orbits, respectively. The formula is also evaluated exactly at \(n=5,6\), where no exhaustive assertion is made. The combinatorial argument above, not finite testing, proves the general formula.

## Relationship to prior work

Bezhanishvili, Dmitrieva, de Groot, and Moraschini [1, Definition 4.10] define these non-distributive modal lattices and prove a broad representation and duality theory, not an exact enumeration of expansions of the fixed diamond family. Dmitrieva's earlier thesis [2, Definition 5.1.1] studies an algebraically different, more restrictive signature: its diamond is join-preserving and bottom-preserving, while the present diamond need only be monotone and top-preserving. Consequently its general representation results do not supply this exact formula. The earlier positive modal algebra literature [3] assumes distributivity and does not cover \(M_n\) for \(n\ge3\). The finite-chain modal and Heyting examples identified in database searches concern different carrier lattices and different axioms. The new claim is only the normal-form *census* on diamond lattices, not the underlying modal-lattice axioms or known duality.

## Limitations

These are counts of the specified modal lattice axioms without extra equations such as \(\Diamond0=0\) or additivity of \(\Diamond\). Counts for those strengthened classes need separate proofs. Only the cases \(n=3,4\) have been exhaustively checked and classified up to isomorphism. For larger \(n\), the formulas give exact labelled counts, but no formula for orbit counts is asserted. Literature equivalence under an unrecognized alternative presentation remains possible; computational verification is not a proof of external novelty.

## References

[1] N. Bezhanishvili, A. Dmitrieva, J. de Groot, and T. Moraschini, *Positive Modal Logic Beyond Distributivity*, arXiv:2204.13401, first public version 2022-04-28, Definition 4.10; *Annals of Pure and Applied Logic* **175** (2024), 103374. https://arxiv.org/abs/2204.13401 ; https://doi.org/10.1016/j.apal.2023.103374

[2] A. Dmitrieva, *Positive Modal Logic Beyond Distributivity: Duality, Preservation and Completeness*, MSc thesis, University of Amsterdam, 2021, particularly Definition 5.1.1 and Chapter 5. https://eprints.illc.uva.nl/id/eprint/1811/

[3] T. Moraschini, *Varieties of Positive Modal Algebras and Structural Completeness*, arXiv:1908.01659 (2019). https://arxiv.org/abs/1908.01659
