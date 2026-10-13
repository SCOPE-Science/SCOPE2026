# Binary p-morphism rigidity for atomic Boolean compatibility frames

## Finding
For every nonempty set \(X\), let \(\mathcal C_X=(\mathcal P(X)^+,R)\), with \(\mathcal P(X)^+=\mathcal P(X)\setminus\{\varnothing\}\) and \(A\,R\,B\) precisely when \(A\cap B\ne\varnothing\). Let \(\mathbf F=\mathcal C_{\{0,1\}}\), the reflexive three-world frame with two mutually inaccessible leaves \(\{0\},\{1\}\) and the universal world \(\{0,1\}\).

**Theorem.** Every forth-and-back bounded morphism \(f:\mathcal C_X\to\mathbf F\) is uniquely induced by a surjective two-coloring \(q:X\to\{0,1\}\):
\[
f(A)=q[A]=\{q(x):x\in A\}\qquad (\varnothing\ne A\subseteq X).
\]
Conversely, each such coloring gives a bounded morphism. It follows that these maps exist exactly when \(X\) has at least two elements. If \(|X|=n\ge1\) is finite, their number is \(2^n-2\); if \(X\) is infinite, their cardinality is \(2^{|X|}\). For any complete atomic Boolean algebra, the same assertion holds after identifying its algebra with the powerset of its atoms. Moreover the induced \(f\), extended to the empty set by \(f(\varnothing)=\varnothing\), is left adjoint to the unique Boolean embedding \(e=q^{-1}:\mathcal P(\{0,1\})\hookrightarrow\mathcal P(X)\).

## Assumptions and scope
A **bounded morphism** here is a function between Kripke frames satisfying (forth) \(A R B\Rightarrow f(A)R f(B)\) and (back) \(f(A)R T\Rightarrow (\exists B)(A R B\land f(B)=T)\) for every source world \(A\) and every target world \(T\). No surjectivity is assumed in its definition. The target \(\mathbf F\) is the full nonzero compatibility frame of a four-element Boolean algebra, **not** a partial-function order and **not** an irreflexive fork. The domain is the **entire** nonzero powerset frame, not an arbitrary induced subframe. The set \(X\) is arbitrary, finite or infinite; no topology, probability measure, or choice of valuation is assumed.

## Proof
Write \(a=\{0\}\), \(b=\{1\}\), and \(c=\{0,1\}\). The only incompatible distinct target states are \(a\) and \(b\). First the back condition forces any map to be onto: a point mapped to \(c\) has required successors mapped to \(a\) and \(b\); a point mapped to \(a\) (respectively \(b\)) has a required successor mapped to \(c\), reducing to the preceding case. This uses that \(c\) is adjacent to both leaves.

**Singleton rigidity.** For any \(x\in X\), suppose \(f(\{x\})=c\). By the back condition at the singleton, there are nonempty sets \(U,V\subseteq X\) meeting \(\{x\}\) such that \(f(U)=a\) and \(f(V)=b\). Both contain \(x\), hence \(U\cap V\ne\varnothing\). Forth would give \(aRb\), a contradiction. Thus every singleton maps to exactly one leaf. Define \(q(x)=i\) when \(f(\{x\})=\{i\}\).

If \(f(A)=a\), then for every \(x\in A\), the edge \(\{x\}RA\) and forth show \(f(\{x\})\ne b\); hence \(q(x)=0\). Similarly \(f(A)=b\) implies \(q[A]=\{1\}\). Since \(f\) is onto and both leaves have nonempty preimages, both colors occur on singletons, so \(q\) is surjective.

If \(A\) contains both colors, its image must be adjacent to both \(a\) and \(b\), by forth applied to its singletons. Therefore \(f(A)=c=q[A]\). If \(A\) consists only of color \(0\), forth rules out \(f(A)=b\). Were \(f(A)=c\), the back condition would give a set \(V\) intersecting \(A\) with \(f(V)=b\); the preceding leaf-preimage observation would give \(q[V]=\{1\}\), contradicting \(A\cap V\ne\varnothing\). Thus \(f(A)=a=q[A]\), and symmetrically for monochromatic color \(1\). This proves the formula for all nonempty \(A\) and uniqueness from the singleton images.

Conversely let \(q:X\twoheadrightarrow\{0,1\}\) and put \(f(A)=q[A]\). If \(A\cap B\ne\varnothing\), then \(q[A]\cap q[B]\ne\varnothing\), proving forth. For back, suppose \(q[A]\cap T\ne\varnothing\) for a nonempty \(T\subseteq\{0,1\}\). Choose \(i\in q[A]\cap T\), \(x\in A\) with \(q(x)=i\), and for each (at most one) remaining \(j\in T\setminus\{i\}\), select \(y_j\in q^{-1}(\{j\})\). Then \(B=\{x\}\cup\{y_j:j\in T\setminus\{i\}\}\) is nonempty, meets \(A\), and satisfies \(q[B]=T\). This is the back condition; only finitely many selections are needed.

For \(S\subseteq\{0,1\}\) and \(A\subseteq X\), \(q[A]\subseteq S\) if and only if \(A\subseteq q^{-1}(S)\). Thus direct image is left adjoint to inverse image. Because \(q\) is onto, its inverse-image map is an injective Boolean homomorphism. Two-colorings of an \(n\)-element set number \(2^n\), with precisely two constant colorings excluded; for an infinite set removing those two does not change cardinality. Finally any complete atomic Boolean algebra is isomorphic to the powerset of its set of atoms by taking arbitrary joins. \(\square\)

## Verification
The symbolic proof works for all sets, including infinite sets; finite enumeration is not used to justify it. A separate finite-state reconstruction in `verify.cpp` enumerates **every** function from the \(2^n-1\) nonempty subsets of \([n]\) into the three target states for \(1\le n\le4\). For each, it directly tests all forth and back requirements against the incidence matrices. Compiling with `g++ -O3 -std=c++17 verify.cpp -o verify` and running `./verify` yields total and surjective bounded-morphism counts \((0,0)\), \((2,2)\), \((6,6)\), and \((14,14)\) respectively. In the largest census this checks all \(3^{15}=14,348,907\) functions. No finite experiment is claimed to prove the infinite case.

## Relationship to prior work
Jockwich, Tarafder, and Venturi introduce compatibility accessibility \(uRv\iff u\wedge v\ne0\) for Boolean values, identify the three-state nonzero frame of the four-element algebra, and use atom partitions to embed smaller finite powerset Boolean algebras into larger ones (Definition 3.5, Example 3.7, Lemma 6.13). Their results on the logics of induced subframes and the resulting hierarchy do not classify **all** bounded morphisms of the complete nonzero frame onto that three-state target. The present rigidity theorem provides the converse structural fact: no other relational forth-and-back maps occur, and this remains true with infinitely many atoms. These are frame-theoretic maps; the result is not asserted to preserve the restricted class of Boolean-value-induced propositional valuations under every pullback.

## Limitations
This theorem concerns complete atomic Boolean algebras (equivalently full powerset algebras) and one fixed target with two atoms. It does not classify morphisms from non-atomic Boolean compatibility frames, morphisms into targets with three or more atoms, or morphisms defined only on proper induced subframes. Counts use labeled target leaves; quotienting by the target's leaf swap would give a different orbit count. The result is a self-reviewed mathematical claim, not an independent verification or a claim of exhaustive literature coverage.

## References
S. Jockwich, S. Tarafder, and G. Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977v1 (first public 2026-07-28), especially Definition 3.5, Example 3.7, and Lemma 6.13. https://arxiv.org/abs/2607.25977
