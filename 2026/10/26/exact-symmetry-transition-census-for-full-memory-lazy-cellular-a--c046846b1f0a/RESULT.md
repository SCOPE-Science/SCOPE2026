# Exact symmetry-transition census for full-memory lazy cellular automata

## Finding
Let \(G\) be a finite abelian group, \(A\) an alphabet of size \(q\ge2\), and \(H\le K\le G\). For a pattern \(p\in A^G\) and a writing symbol \(a\ne p(e)\), let \(\tau_p^a\) be the cellular automaton with active neighborhood all of \(G\), changing the current symbol to \(a\) exactly when the entire observed configuration equals the active pattern. Write \(G_x=\{g\in G:g\cdot x=x\}\) for the translation stabilizer, where \((g\cdot x)(h)=x(hg)\).

Put \(M_q(K)=|\{x\in A^G:G_x=K\}|\). The number \(N_q(H,K)\) of **distinct full-memory lazy rules** \((p,a)\) satisfying \(G_p=H\) and \(G_{\tau_p^a(p)}=K\) is exactly

\[
N_q(H,K)=\begin{cases}
(q-1)M_q(K),&H<K,\\
(q-1)\bigl(2M_q(H)-q^{[G:H]}\bigr),&H=K,\\
0,&H\not\le K.
\end{cases}
\]

Here the counts \(M_q(K)\) are explicit through the subgroup-lattice Möbius function:

\[
M_q(K)=\sum_{L\ge K}\mu(K,L)q^{[G:L]}.
\]

In particular, for every subgroup \(H\le G\),
\[
M_q(H)\ge\tfrac12q^{[G:H]},
\]
with equality **if and only if** \(q=2\) and \(G/H\) is isomorphic to \(C_2\) or \(C_2\times C_2\). Equivalently, a stabilizer-preserving full-memory lazy rule sourced at \(H\) exists in every other case.

## Assumptions and scope
Throughout, \(G\) is finite and abelian (not necessarily cyclic), \(e\) is its identity, \(A\) is a finite discrete alphabet of size \(q\ge2\), and all source patterns use the **entire** active neighborhood \(G\). We count labeled rules, not conjugacy classes or compositions. Since the local map differs from the identity exactly on its active pattern, different pairs \((p,a)\) define different full-memory lazy maps. The output used in the classification is the specific image \(\tau_p^a(p)\), not an arbitrary point in its image orbit. For \(H=G\), the quotient \(G/H\) is trivial and the inequality is strict.

## Proof
**1. Local action and monotonicity.** The full-memory rule fires on \(p\) precisely at positions \(h\in G_p\). Consequently, if \(G_p=H\), its image \(y=\tau_p^a(p)\) is obtained by replacing \(p(h)=p(e)\) with \(a\) at every \(h\in H\), leaving other coordinates unchanged. Equivariance gives \(H\le G_y\). There are exactly \((q-1)M_q(H)\) rules sourced at \(H\).

**2. Exact fibres over a strictly larger stabilizer.** Fix \(H<K\) and any \(y\) with \(G_y=K\). Set \(a=y(e)\). For each \(b\in A\setminus\{a\}\), define \(p_b(h)=b\) on \(H\), and \(p_b(g)=y(g)\) outside \(H\). We claim \(G_{p_b}=H\).

Embed the \(q\) symbols injectively into distinct real numbers. In the complex Fourier transform on the finite abelian group, \(p_b=y+(b-a)\mathbf1_H\). Write \(H^\perp\) and \(K^\perp\) for the character annihilators. For every character \(\chi\in H^\perp\setminus K^\perp\), the transform of \(y\) vanishes because \(y\) is \(K\)-invariant, whereas that of \(\mathbf1_H\) equals \(|H|\). Thus \(\widehat p_b(\chi)=(b-a)|H|\ne0\). Any translating stabilizer of \(p_b\) lies in the kernel of every such character.

The characters in \(H^\perp\setminus K^\perp\) generate \(H^\perp\): choose \(\chi_0\) outside \(K^\perp\), and express each \(\eta\in K^\perp\) as \((\chi_0\eta)\chi_0^{-1}\), with both outside \(K^\perp\). Duality then forces \(G_{p_b}\le H\). Conversely \(H\) stabilizes both \(y\) and \(\mathbf1_H\), so \(H\le G_{p_b}\). The claim follows. The lazy action on \(p_b\) replaces its \(H\)-coordinates with \(a\), giving \(y\). Conversely any rule with input stabilizer \(H\), output \(y\), and changed symbol has exactly this form, with \(b=p(e)\). There are exactly \(q-1\) possibilities, so \(N_q(H,K)=(q-1)M_q(K)\).

**3. Diagonal count and Möbius formula.** Exactly \(q^{[G:H]}\) configurations have stabilizer containing \(H\): they are the functions on the coset space \(G/H\). Partitioning them according to their exact stabilizer yields
\[
\sum_{K\ge H}M_q(K)=q^{[G:H]}.
\]
The displayed Möbius inversion follows. Subtract all strict-transition counts from the \((q-1)M_q(H)\) rules sourced at \(H\); the remainder is \((q-1)(2M_q(H)-q^{[G:H]})\). Nonnegativity gives the half bound.

**4. Exact equality cases.** Stabilizers of \(H\)-invariant configurations correspond to stabilizers for the quotient \(B=G/H\). If \(q=2\) and \(B=C_2\), each aperiodic two-coloring has one exceptional site; changing the identity symbol makes it constant. If \(q=2\) and \(B=C_2\times C_2\), each aperiodic coloring has support of size one or three; changing the identity creates support of even size, hence a coloring with a nontrivial period (including the constant cases). Thus the diagonal count vanishes in both groups, giving equality.

To prove strictness in every other case, construct one aperiodic coloring whose identity-symbol change is also aperiodic. For the trivial quotient any two different constant configurations suffice. If \(q\ge3\) and \(B\ne\{e\}\), take \(p\) equal to symbol 1 at some \(g\ne e\) and symbol 0 elsewhere; rewrite the identity to a third symbol 2. Both colorings are aperiodic: the first has a unique 1 and the second a unique 2. If \(q=2\) and \(B\) contains \(g\) of order greater than two, take the indicator of \(\{g\}\), and rewrite the identity to 1. The resulting two-point support \(\{e,g\}\) has no nonzero translational period because \(2g\ne e\). Finally, if \(q=2\), \(B\) has exponent two, and \(|B|\ge8\), choose three independent \(u,v,w\). The indicator of \(\{u,v,w\}\) is aperiodic because a nonzero order-two translation cannot preserve a set of odd size. After rewriting the identity its support is \(\{e,u,v,w\}\); any four-set invariant under a nonzero order-two translation has group sum zero, whereas here the sum is \(u+v+w\ne e\). Thus its stabilizer is trivial. These cases exhaust finite abelian quotients. Hence the stated equality criterion is exact.

## Verification
The standalone `verify.py` exhaustively computes stabilizers and actual lazy rule outputs on 17 finite abelian group/alphabet systems (orders two through nine, with binary and ternary alphabets), and checks both transition and diagonal formulas directly. It also separately checks the sum of exact stabilizer counts against the number of quotient colorings. The run reports 349 verified counting identities. This is independent finite corroboration of the proof, not a claim that finitely many cases establish the general theorem. Run `python verify.py` with Python 3 and the standard library.

## Relationship to prior work
Alcalá-Arroyo and Castillo-Ramirez, arXiv:2610.18480v1, Lemma 3.8, supply the local full-memory lazy-action identity. Their Theorem 3.13 constructs examples of strict and equal stabilizer transitions for generator-existence questions; in particular, it already identifies the binary Klein-four obstruction. Those **existence statements are prior work**. The present result counts **every** full-memory lazy rule for every ordered pair of subgroup stabilizers, expresses the counts by Möbius inversion, and derives a sharp universal primitive-coloring proportion. Alcalá-Arroyo and collaborators, arXiv:2610.20329v1, give detailed finite Klein-four monoid counts rather than this all-abelian transition matrix. Castillo-Ramirez and Ruiz-Medina, arXiv:2203.12158, treat relative ranks of equivariant endomorphism monoids, not a census of these specific local-map fibres.

## Limitations
This concerns finite **abelian** groups, full-memory single-active-pattern lazy cellular automata, exact input/output stabilizers, and labeled rules. No assertion is made for nonabelian groups, arbitrary partial neighborhoods, factorization lengths, or inequivalent rules under conjugation. The result is mathematically proved under these hypotheses, but a broader historical-priority search under necklace/aperiodic-coloring terminology could reveal earlier equivalent counting statements. Independent review has not been performed.

## References
1. E. Alcalá-Arroyo and A. Castillo-Ramirez, *When do lazy and invertible cellular automata generate all cellular automata?* arXiv:2610.18480v1 (first public 2026-10-13), https://arxiv.org/html/2610.18480v1 . In particular Lemma 3.8 and Theorem 3.13.
2. E. Alcalá-Arroyo, A. Castillo-Ramirez, H. Ma and W. Zhang, *Generation by lazy and invertible cellular automata over the Klein four-group*, arXiv:2610.20329v1 (2026), https://arxiv.org/abs/2610.20329 . In particular Lemma 2.4 and Section 6.
3. A. Castillo-Ramirez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite G-set*, arXiv:2203.12158 (2022; later revision 2023), https://arxiv.org/pdf/2203.12158 .
