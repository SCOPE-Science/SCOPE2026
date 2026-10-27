# A non-residually-finite but locally virtually abelian automorphism group at quadratic symbolic complexity

## Finding
Let \(X_2=\{x\in\{0,1\}^{\mathbb Z}: |\{j:x_j=1\}|\le2\}\) with the left shift \((\sigma x)_j=x_{j+1}\). Every shift-commuting homeomorphism of \(X_2\) is uniquely a power of the shift followed by a finite-support permutation of the gaps between the two \(1\)'s and independent finite-support integer shifts of the corresponding two-particle orbits. Consequently,
\[
\operatorname{Aut}(X_2)\cong \mathbb Z\times\big(\mathbb Z^{(\mathbb N_{\ge1})}\rtimes\operatorname{Sym}_{\mathrm{fin}}(\mathbb N_{\ge1})\big).
\]
The shift has exact word complexity \(p_{X_2}(n)=1+n+\binom n2\), Cantor--Bendixson rank \(3\), entropy zero, and only one periodic configuration. Its automorphism group is **not residually finite**, but every finitely generated subgroup is **virtually free abelian**, and in particular residually finite.

## Assumptions and scope
All configurations are bi-infinite binary sequences and \(\sigma\) is the left shift. The cardinality restriction is global, allowing zero, one or two occurrences of the symbol \(1\). Write \(o\) for the all-zero configuration, \(u_a\) for the singleton supported at \(\{a\}\), and \(e_{a,d}\) for the pair supported at \(\{a,a+d\}\), with \(a\in\mathbb Z\), \(d\in\mathbb N_{\ge1}\). A function or permutation on positive integers has *finite support* when it differs from its identity/zero value at only finitely many arguments. All automorphisms are continuous bijections commuting with \(\sigma\), with no fixed-radius bound imposed in advance.

## Proof
**1. Topological strata.** Each \(e_{a,d}\) is isolated: prescribing its two \(1\) coordinates forces all other coordinates to vanish on \(X_2\). Conversely, each \(u_a\) is a limit of \(e_{a,d}\) as \(d\to\infty\), and \(o\) is a limit of translates of \(u_a\). Hence the first Cantor--Bendixson derivative is \(X_1=\{o\}\cup\{u_a:a\in\mathbb Z\}\); its derivative is \(\{o\}\), and the next derivative is empty. The only periodic point is \(o\).

**2. Restriction of an automorphism to the derived set.** Let \(h\in\operatorname{Aut}(X_2)\). A homeomorphism preserves Cantor--Bendixson strata, so \(h(o)=o\) and \(h\) permutes the singletons. Since they form one free shift orbit and \(h\sigma=\sigma h\), a unique integer \(k\) satisfies \(h(u_a)=\sigma^k u_a=u_{a-k}\) for all \(a\). Composing with \(\sigma^{-k}\), assume henceforth that \(h\) fixes all singleton configurations.

**3. Every sufficiently large gap is pointwise fixed.** The Curtis--Hedlund--Lyndon local-rule theorem, or uniform continuity and shift equivariance directly, gives a finite radius \(R\ge0\) whose radius-\(R\) neighborhoods determine the output at every site. For \(d>2R\), every such neighborhood in \(e_{a,d}\) contains at most one \(1\). Every one of these neighborhoods also occurs with the same center in either a singleton or \(o\), where \(h\) acts identically. Thus \(h(e_{a,d})=e_{a,d}\) for every \(a\) when \(d>2R\). This is a uniform conclusion over all translations, not a finite experimental extrapolation.

**4. Action on the remaining orbits.** Each isolated configuration belongs to exactly one free shift orbit \(O_d=\{e_{a,d}:a\in\mathbb Z\}\). The homeomorphism preserves isolated points and commutes with the shift, so it permutes these orbits. There are therefore a permutation \(\pi\) of the positive integers and an integer function \(t\), uniquely determined, for which
\[
 h(e_{a,d})=e_{a+t(d),\pi(d)}.
\]
Step 3 implies \(\pi(d)=d\) and \(t(d)=0\) outside a finite set. Conversely, every finite-support permutation \(\pi\) and finite-support integer function \(t\) define a shift-equivariant bijection by this formula and by fixing \(o,u_a\). It and its inverse are continuous: isolated points pose no issue; a convergent sequence toward a singleton eventually either has unchanged large gaps or is already a singleton; a sequence toward \(o\) cannot be moved into a bounded neighborhood by a finite collection of fixed coordinate displacements. More explicitly, the difference from the identity is restricted to finitely many gap orbits and translates their configurations by uniformly bounded distances. Compactness then provides a finite-radius sliding-block realization. This establishes surjectivity onto the described group.

**5. Group law and splitting.** With maps acting on the pair coordinates as \((a,d)\mapsto(a+t(d),\pi(d))\), composition obeys
\[
 (\pi,t)\circ(\rho,u)=\big(\pi\circ\rho,\ d\mapsto u(d)+t(\rho(d))\big).
\]
This is the restricted wreath-product group \(\mathbb Z^{(\mathbb N_{\ge1})}\rtimes\operatorname{Sym}_{\mathrm{fin}}(\mathbb N_{\ge1})\). The global shift is central, and its intersection with the subgroup fixing all singletons is trivial. Step 2 supplies the unique direct-product decomposition.

**6. The finiteness dichotomy.** Finite-support even permutations of positive gap labels embed as \(\operatorname{Alt}_{\mathrm{fin}}(\mathbb N_{\ge1})\), an infinite simple group. A homomorphism from an infinite simple group to a finite group is trivial: any nontrivial homomorphism would be injective, which is impossible. Consequently no finite quotient of \(\operatorname{Aut}(X_2)\) can distinguish a nonidentity even gap permutation; the automorphism group is not residually finite. In contrast, given finitely many automorphisms, take the union \(E\) of the finite supports of their \(\pi\) and \(t\). The subgroup they generate lies in \(\mathbb Z\times(\mathbb Z^E\rtimes\operatorname{Sym}(E))\), a virtually free abelian group. Every finitely generated subgroup is therefore virtually free abelian and residually finite.

Finally, an admissible block of length \(n\) contains zero, one or two \(1\)'s. All \(1+n+\binom n2\) such blocks occur, proving the complexity and zero-entropy statements.

## Verification
Run `python verify.py` with Python 3 and no nonstandard packages. The standalone checker tests five representative finite-gap orbit transformations (four nontrivial and the identity), their explicit inverses and shift commutation on \(4{,}805\) two-particle samples, local-rule consistency on a finite family of windows, and the exact word-complexity formula for \(1\le n\le39\). It reports `VERIFY_OK` on completion. These finite checks are diagnostic; the all-radius classification and residual-finiteness conclusions follow only from the preceding proof.

## Relationship to prior work
Ville Salo, *Periodic points and residual finiteness of automorphism groups of subshifts* (arXiv:2603.16591v1, submitted 17 March 2026), proves a general non-residual-finiteness conclusion after adjoining a full-shift factor when periodic points are not dense, and investigates finitely generated non-residually-finite subgroups in that product setting. The present classification does **not** use an auxiliary full-shift factor and shows a different behavior: non-residual finiteness coexists with local virtual abelianness. Salo and Törmä, *Complexity of Conjugacy, Factoring and Embedding for Countable Sofic Shifts of Rank 2* (arXiv:1408.6695v1, 2014), classify structural features and decision problems for rank-two countable sofic shifts; \(X_2\) has rank three and the present claim is an explicit automorphism-group calculation. Standard facts about finitary alternating groups and sliding-block codes are used as such, not claimed as new.

## Limitations
This is a classification for the one specified two-particle binary shift, not all quadratic-complexity shifts or all rank-three sofic shifts. The inference that no earlier equivalent formula exists is bibliographic rather than a theorem: older countable-subshift literature, including Salo's 2014 dissertation, may contain a differently phrased equivalent result. The existence of a uniform radius for each automorphism does not give one common radius for the entire group. No independent mathematical review has been performed.

## References
1. V. Salo, *Periodic points and residual finiteness of automorphism groups of subshifts*, arXiv:2603.16591v1 (17 March 2026), https://arxiv.org/abs/2603.16591.
2. V. Salo and I. Törmä, *Complexity of Conjugacy, Factoring and Embedding for Countable Sofic Shifts of Rank 2*, arXiv:1408.6695v1 (28 August 2014), https://arxiv.org/abs/1408.6695.
3. V. Salo, *Subshifts with Simple Cellular Automata*, dissertation (2014), https://urn.fi/URN:ISBN:978-952-12-3089-9; consulted at bibliographic/abstract level only.
4. G. A. Hedlund, *Endomorphisms and automorphisms of the shift dynamical system*, Mathematical Systems Theory 3 (1969), 320--375.
