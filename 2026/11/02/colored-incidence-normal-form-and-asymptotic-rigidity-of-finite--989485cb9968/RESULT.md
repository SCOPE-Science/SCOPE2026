# Colored incidence normal form and asymptotic rigidity of finite BALFIs

## Finding

Let \(m\ge 1\), let \(U=\{1,\ldots,m\}\), and put \(B=\mathcal P(U)\), equipped with its Boolean operations and its Boolean implication. A **BALFI expansion** of \(B\) consists of two (not necessarily monotone) unary functions \(\neg,\circ:B\to B\) satisfying, for every \(A\subseteq U\),
\[
A\cup\neg A=U,\qquad A\cap\neg A\cap\circ A=\varnothing.
\]
These are exactly the two defining equations for Boolean algebras with LFI operators, introduced in the cited literature. The classification and counts below concern the full variety, not a particular restricted presentation or a free algebra.

**Colored incidence classification.** Every expansion is uniquely encoded by independent choices at the \(m2^m\) input-atom incidences \((A,j)\). For \(j\in A\), its two bits \((1_{j\in\neg A},1_{j\in\circ A})\) are any of
\[
(0,0),\ (0,1),\ (1,0),
\]
and for \(j\notin A\) they are any of \((1,0),(1,1)\). Conversely, every such assignment determines a BALFI. Two expansions are isomorphic precisely when their colored incidence tables differ by a simultaneous permutation of the Boolean atoms \(U\).

Put \(L_m=m2^{m-1}\). The labelled expansions number \(6^{L_m}\). The expansions satisfying the **consistency-recovery identity** \(\circ A=U\setminus(A\cap\neg A)\) (the standard \(\mathrm{ciw}\) condition) number \(2^{L_m}\). The expansions with \(\neg A=U\setminus A\) (classical negation) number \(4^{L_m}\). The latter two collections intersect in exactly one expansion.

For a permutation \(\sigma\in S_m\), let \(r\) be its order, let \(f(\tau)\) and \(c(\tau)\) denote the numbers of fixed points and cycles of a permutation \(\tau\) on \(U\), and define
\[
o_m(\sigma)=\frac1r\sum_{t=0}^{r-1}f(\sigma^t)2^{c(\sigma^t)-1}.
\]
Then the numbers of *isomorphism classes* in the three families (all BALFIs, \(\mathrm{ciw}\) BALFIs, classical-negation BALFIs) are exactly
\[
N_m(q)=\frac1{m!}\sum_{\sigma\in S_m}q^{o_m(\sigma)},
\qquad q=6,2,4\ \text{respectively}.
\]
For \(m=1,2,3,4\), respectively, \(N_m(6)\) equals \(6,666,362937456,331610880495493011617856\). At \(m=2\), the corresponding \(\mathrm{ciw}\) and classical-negation class counts are \(10\) and \(136\).

**Asymptotic rigidity.** For every \(m\ge2\) and each \(q\in\{2,4,6\}\), a uniformly chosen labelled expansion from the corresponding family obeys
\[
\Pr(\operatorname{Aut}\ne1)\le(m!-1)q^{-(m+2)2^{m-3}}.
\]
Thus the probability of a nontrivial automorphism tends to zero, and
\[
N_m(q)\sim\frac{q^{L_m}}{m!}\qquad(m\to\infty).
\]
Finally, in a uniformly chosen BALFI, the number \(C_m\) of inconsistent input-atom incidences \((A,j)\) with \(j\in A\cap\neg A\) is exactly distributed as
\[
C_m\sim\operatorname{Binomial}(L_m,1/3).
\]
In particular, the fraction of labelled BALFIs admitting an inconsistent Boolean value is \(1-(2/3)^{L_m}\). This is an algebraic witness statement, not a theorem about the frequency of contradictions in arbitrary externally generated knowledge bases.

## Assumptions and scope

The Boolean reduct \(\mathcal P(U)\) is **finite, nontrivial, and fixed up to atom labelling**. Implication is the Boolean residual \(A\to B=(U\setminus A)\cup B\). The operations \(\neg\) and \(\circ\) are unrestricted unary functions except for the two BALFI equations above; in particular neither is assumed monotone, additive, involutive, or compatible with a topology. The \(\mathrm{ciw}\) subclass imposes exactly one further identity. The classical-negation subclass constrains only \(\neg\), not \(\circ\).

The symbol \(\operatorname{Aut}\) means automorphisms of the *entire expanded algebra*. The probability measures are uniform over labelled expansions on the fixed reduct. The asymptotic parameter is the number \(m\) of Boolean atoms, so the algebra has \(2^m\) elements.

## Proof

**1. Independent incidence choices.** Fix \(A\subseteq U\) and \(j\in U\). If \(j\notin A\), the equality \(A\cup\neg A=U\) forces \(j\in\neg A\); the gentle-explosion equation imposes no restriction on membership in \(\circ A\). This gives precisely two local states. If \(j\in A\), excluded middle imposes no further condition, while gentle explosion forbids simultaneous membership in \(\neg A\) and \(\circ A\). This gives the other three states. Because the defining equations are pointwise, there are no constraints coupling distinct incidences. Conversely the allowed states satisfy both equations at every atom. This proves the stated normal form and its completeness.

There are exactly \(L_m\) incidences of each kind: each fixed atom belongs to exactly half the subsets \(A\). Thus the unrestricted labelled count is \(3^{L_m}2^{L_m}=6^{L_m}\). Under \(\mathrm{ciw}\), every outside incidence is fixed to \((1,1)\), and each inside incidence has one of two complementary bit pairs \((0,1),(1,0)\), giving \(2^{L_m}\). Under classical negation, every inside incidence has first bit zero, and every outside incidence has first bit one; the second bits are free independently, giving \(2^{2L_m}=4^{L_m}\). Both constraints together force \(\neg A=U\setminus A\) and \(\circ A=U\) for every \(A\), a unique expansion.

**2. The isomorphism action.** Every Boolean-algebra automorphism of \(\mathcal P(U)\) is uniquely induced by a permutation of its atoms. An isomorphism between two expansions must preserve the Boolean reduct and hence is such a permutation. It intertwines both unary maps exactly when it preserves their colored incidence tables under \((A,j)\mapsto(\sigma A,\sigma j)\). Therefore the isomorphism classes are precisely the \(S_m\)-orbits of the allowed incidence colorings.

Let \(I=\{(A,j):j\in A\}\) and \(O=\{(A,j):j\notin A\}\). Complementation in the first coordinate gives an \(S_m\)-equivariant bijection \(I\to O\). The action of \(\sigma\) therefore has the same number \(o\) of cycles on each. A coloring of \(I\) by three colors and of \(O\) by two colors is \(\sigma\)-invariant exactly when it is constant on each cycle, yielding \(3^o2^o=6^o\) fixed BALFIs. In the recovery and classical-negation subclasses, the corresponding fixed counts are \(2^o\) and \(4^o\).

To compute \(o\), apply the orbit-counting lemma to the cyclic group generated by \(\sigma\). If \(\tau\) fixes exactly \(f(\tau)\) atoms and has \(c(\tau)\) atom cycles, a fixed incidence \((A,j)\in I\) requires a fixed atom \(j\) and a union of cycles \(A\) containing its singleton cycle. Hence there are exactly \(f(\tau)2^{c(\tau)-1}\) fixed incidences. Averaging over the powers of \(\sigma\) proves the displayed formula for \(o_m(\sigma)\). Applying Burnside's lemma to \(S_m\) gives all three exact isomorphism-class counts.

**3. Rigidity and asymptotics.** A nonidentity atom permutation \(\sigma\) fixes at most \(m-2\) atoms and has at most \(m-1\) cycles. Consequently it fixes at most \((m-2)2^{m-2}\) elements of \(I\). Every other incidence lies on a \(\sigma\)-cycle of size at least two. Therefore
\[
o_m(\sigma)\le\frac{L_m+(m-2)2^{m-2}}2
=L_m-(m+2)2^{m-3}.
\]
In any of the three families, the probability that this particular nonidentity permutation is an automorphism is \(q^{o_m(\sigma)-L_m}\). The union bound over all nonidentity permutations yields the stated estimate. Since \((m+2)2^{m-3}\) eventually grows faster than \(\log_q(m!)\), the right-hand side tends to zero. Dividing the Burnside sum into its identity and nonidentity terms gives the asymptotic formula for \(N_m(q)\).

**4. Incidence contradiction distribution.** For each incidence \((A,j)\in I\), one of the three equiprobable allowed local states has \(j\in\neg A\). These local choices are independent under the uniform product measure. Thus \(C_m\) is binomial with parameters \(L_m,1/3\), and it vanishes with probability \((2/3)^{L_m}\). Vanishing means \(A\cap\neg A=\varnothing\) for all \(A\), which together with excluded middle is equivalent to classical negation. Otherwise a Boolean element \(A\) witnesses an allowed contradiction, and a valuation may assign that element to a propositional variable.

## Verification

The included standalone `checker.py` is ordinary finite arithmetic and Boolean-table code, not an infinite proof or independent certification. It reconstructs all \(6\) labelled expansions for \(m=1\) and all \(1296\) for \(m=2\), checks both BALFI identities on every Boolean element, verifies the two subclass counts and their unique intersection, directly computes permutation-fixed expansions, and checks their orbit count. Separately it computes incidence cycles and the permutation-power formula for every atom permutation through \(m=5\), confirming equality of the three calculations of \(o_m\) and reproducing the class-count table. It prints `ALL_CHECKS_OK` on success. The general results rest on the preceding proofs, not on exhaustive checks of unbounded \(m\).

## Relationship to prior work

Carnielli, Coniglio and Fuenmayor introduced the BALFI semantics for self-extensional paraconsistent logic. Their Definition 2.10 gives the equations used here; Proposition 3.4 identifies the \(\mathrm{ciw}\) recovery identity. Coniglio and Mallea's 2026 work extends the theory with finite-model filtration, decidability, and algebraic distinctions among consistency axioms. Both sources establish the semantic setting; neither of the inspected relevant passages states this incidence-coordinate classification, the three finite isomorphism enumerators, or the almost-sure automorphism rigidity bound.

The orbit-counting lemma and Burnside's lemma are established general-purpose results used in the proof, not themselves new claims. A general orbit-counting identity alone does not supply the BALFI-specific correspondence or the explicit cycle-count formula. Nearby Boolean-algebra operator enumerations concern different unary equations and thus do not directly imply this classification. Exact absolute priority across all terminology is not claimed.

## Limitations

The theorem does not enumerate BALFIs satisfying arbitrary additional propagation axioms, nor does it classify infinite Boolean reducts. The probability law refers to uniformly sampled *finite labelled expansions*, not to a probability distribution on formulas or observed inconsistent databases. Finite tests corroborate examples and formulas but do not certify the general proof. Relevant older algebraic-enumeration literature may contain a terminology-translated equivalence that was not located.

## References

1. W. Carnielli, M. E. Coniglio, and D. Fuenmayor, *Logics of Formal Inconsistency enriched with replacement: an algebraic and modal account*, arXiv:2003.09522, first public version March 20, 2020. Definitions 2.10 and Proposition 3.4; accessible full-text HTML at https://arxiv.org/abs/2003.09522 .
2. M. E. Coniglio and H. F. Mallea, *Self-extensional logics of formal inconsistency: Decidability and limits for paraconsistency*, arXiv:2608.28443, first public version August 28, 2026. Sections 2.3, 3, 4, and 5; accessible full-text HTML at https://arxiv.org/abs/2608.28443 .
3. Burnside's orbit-counting lemma and the elementary finite Boolean-algebra automorphism theorem (standard tools; used with complete derivations of their specialized inputs above).
