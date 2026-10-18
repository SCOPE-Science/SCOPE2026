# First-order modal logic of finite cyclic groups under subgroup embeddings is Grz.2

## Finding
Let \(\mathscr C=\{C_n:n\geq1\}\) denote finite cyclic groups up to isomorphism, and set \(C_n\preceq C_m\) precisely when \(n\mid m\). Atoms of the propositional modal language are assigned arbitrary first-order sentences of the additive group language, with \(\Box\) quantifying over all accessible cyclic groups. The resulting exact structure modal logic is
\[
\operatorname{ML}_{\mathrm{FO}}(\mathscr C,\preceq)=\mathsf{Grz.2}.
\]
Here \(\mathsf{Grz.2}\) is the normal logic extending \(\mathsf{S4}\) by the Grzegorczyk axiom \(\Box(\Box(p\to\Box p)\to p)\to p\) and the directedness axiom \(\Diamond\Box p\to\Box\Diamond p\). A stronger finite-state assertion holds: **every finite family** of first-order group sentences factors through one finite directed partial order by a surjective bounded morphism of the whole divisibility frame.

## Assumptions and scope
The class includes the trivial group \(C_1\), and consists only of **finite cyclic** groups, not all abelian groups or all finite abelian groups. Each propositional letter has one fixed parameter-free first-order group sentence as its interpretation at every world. The accessibility arrow points toward *larger* groups, so \(C_n\preceq C_m\) if and only if \(n\mid m\). Isomorphic groups are identified. No arbitrary set-theoretic valuations are allowed in the structure-modal validity claim.

## Proof
**Lemma 1 (finite profile of first-order sentences).** For any finite list \(\Theta\) of first-order sentences about abelian groups, there are an integer \(N\geq1\), finitely many primes \(P\), and exponents \(h_p\geq1\) such that for all \(n,m>N\), if \(\min(v_p(n),h_p)=\min(v_p(m),h_p)\) for every \(p\in P\), then \(C_n\) and \(C_m\) agree on every sentence in \(\Theta\).

*Proof of Lemma 1.* Baur–Monk elimination, in the explicit finite-abelian-group form documented by Bova and Martin, replaces any sentence by a Boolean combination of inequalities \([\phi(C_n):\phi(C_n)\cap\psi(C_n)]\geq k\), where \(\phi,\psi\) are unary primitive-positive formulas. For a unary pp formula \(\phi(x)\), write its homogeneous system of linear equations as \(A\mathbf y+\mathbf b x=0\). Integer Smith reduction of \(A\) gives finitely many conditions \(d_i y_i+c_i x=0\) and \(c_j x=0\) over \(C_n\). The former has a solution exactly when \(\gcd(d_i,n)\mid c_i x\), and the latter exactly when \(n\mid c_jx\). Consequently the solution subgroup is \(\phi(C_n)=L_\phi(n)C_n\), with \(L_\phi(n)\mid n\); here \(L_\phi(n)\) is the least common multiple of the numbers
\[
\frac{\gcd(d_i,n)}{\gcd(c_i,d_i,n)}
\quad\text{and}\quad
\frac{n}{\gcd(c_j,n)}.
\]
Zero constraints contribute \(1\). At a prime \(p\), the exponent of \(L_\phi(n)\) is the maximum of finitely many functions of \(a=v_p(n)\) of the forms \(\max(0,\min(a,b)-c)\) and \(\max(0,a-c)\). Apart from finitely many primes, it equals either \(0\) or \(a\), uniformly, and for each exceptional prime it is eventually either a constant or \(a\) plus a constant. Thus there are \(\delta_\phi\in\{0,1\}\) and a sufficiently divisible positive integer \(D\) such that
\[
L_\phi(n)=n^{\delta_\phi}\,F_\phi(\gcd(n,D)),
\]
where \(F_\phi\) is a positive rational-valued function on the finite divisor set of \(D\). Increase \(D\) as needed for an entire finite list of pp formulas. Since \(\phi(C_n)\cap\psi(C_n)\) is again unary pp, its subgroup-index ratio has the form
\[
[\phi(C_n):\phi(C_n)\cap\psi(C_n)]
=n^{\varepsilon}\,F(\gcd(n,D)),
\]
where \(\varepsilon=\delta_{\phi\wedge\psi}-\delta_\phi\). This exponent cannot be negative: outside the finitely many prime divisors of \(D\), a negative exponent would give a nonintegral subgroup index for cyclic groups of sufficiently large prime order. Thus \(\varepsilon\in\{0,1\}\). If \(\varepsilon=0\), an inequality with this index depends only on \(\gcd(n,D)\); if \(\varepsilon=1\), it holds for every sufficiently large \(n\), because the positive function \(F\) has finitely many values and hence a positive minimum. Taking common cutoffs and primes over all invariant inequalities establishes the assertion. \(\square\)

**Lemma 2 (finite directed quotient with a back condition).** Fix the finite list \(\Theta\) and choose \(N,P,(h_p)\) as in Lemma 1. Enlarge \(P\) to include every prime at most \(N\), and enlarge \(h_p\) so that the small orders \(n\leq N\) have full, uncapped valuations. Write \(t(n)=(\min(v_p(n),h_p))_{p\in P}\). Form a finite poset \(F\) whose elements are distinct symbols \(s_n\) for \(1\leq n\leq N\) and all tuples \(\ell_t\) with \(0\leq t_p\leq h_p\). Put \(s_n\leq s_m\) exactly when \(n\mid m\), \(s_n\leq\ell_t\) exactly when \(t(n)\leq t\) coordinatewise, and \(\ell_t\leq\ell_u\) exactly when \(t\leq u\) coordinatewise; there are no \(\ell_t\leq s_n\) arrows. This is a finite partial order, with a common upper world \(\ell_{(h_p)}\). Define \(f(n)=s_n\) when \(n\leq N\), and \(f(n)=\ell_{t(n)}\) otherwise. The map is onto: realize any tuple using appropriate prime powers and multiply by an auxiliary prime above \(N\) outside \(P\). It preserves divisibility. To lift \(f(n)\leq\ell_t\), multiply \(n\) by precisely the missing powers of the finitely many selected primes, then, if necessary, by a fresh large prime to ensure the order exceeds \(N\); this gives a multiple \(m\) with \(f(m)=\ell_t\). Small-to-small arrows lift by choosing \(m\) itself. Thus \(f\) is a surjective bounded morphism. Lemma 1 says each member of \(\Theta\) is constant on each fibre.

**Lower bound on validities.** Take any modal formula and any interpretation of its finitely many atoms by sentences \(\Theta\). By Lemma 2 this Kripke model is the inverse image under a bounded morphism of a model on the **finite directed partial order** \(F\). The bounded-morphism truth lemma applies to every subformula, including nested modalities. Every finite directed poset validates \(\mathsf{Grz.2}\): it is finite and antisymmetric (so validates Grz), and it is reflexive, transitive and directed (so validates S4 and .2). Hence every theorem of \(\mathsf{Grz.2}\) is valid for every first-order structure valuation.

**Upper bound on validities.** Given \(r\geq1\), choose distinct primes \(p_1,\ldots,p_r\). The map
\[
g_r(n)=\{i\in[r]:p_i\mid n\}
\]
is a surjective bounded morphism onto the Boolean lattice \((\mathcal P([r]),\subseteq)\). For the back condition, multiply \(n\) by those \(p_i\) whose coordinates are requested but absent. For each \(i\), the first-order sentence \(\beta_i\) asserting that the group has a nonzero element annihilated by \(p_i\) is true in \(C_n\) exactly when \(p_i\mid n\). Every subset of the finite Boolean cube can therefore be defined by a Boolean combination of the \(\beta_i\); accordingly every propositional valuation on the cube pulls back to a permissible first-order sentence valuation on the cyclic groups. The published characterization of Grz.2 by **all finite Boolean lattices** (Wołoszyn, *Grzegorczyk Logic Unlocked*, Theorem 18) then implies that every modal formula outside \(\mathsf{Grz.2}\) has a first-order cyclic-group counterinterpretation. Combining the two bounds proves the equality. \(\square\)

## Verification
The standalone `verify.py` uses independently specified finite posets to test Grz and .2 on every valuation of Boolean cubes of rank up to three; it checks the prime-divisibility quotient lifting property for many cyclic orders, constructs a finite directed-quotient prototype with a small-order exceptional layer and verifies its order and back condition, and directly enumerates two unary pp subgroups to check their indices. Run `python3 verify.py` to obtain `VERIFY_OK`. These are finite consistency checks only; the infinite result rests on the Smith-normal-form argument, Baur–Monk elimination, and the cited modal completeness theorem.

## Relationship to prior work
Berger, Block and Löwe (2023) prove that the full class of **all abelian groups** under subgroup embedding has structure modal logic \(\mathsf{S4.2}\), and explicitly use the prime-torsion sentences as independent buttons. Their additional switching constructions use groups unavailable in the finite cyclic subclass. The Baur–Monk theorem (as documented for finite abelian groups by Bova and Martin, 2015) supplies the elimination into pp subgroup indices, but does not discuss this modal classification. Wołoszyn's later characterization identifies the modal logic of finite Boolean lattices as \(\mathsf{Grz.2}\), but does not classify the first-order modal logic of cyclic-group subgroup embeddings. The new combination is the finite **directed bounded-morphism quotient for arbitrary first-order group sentences**, yielding the strict strengthening from \(\mathsf{S4.2}\) to \(\mathsf{Grz.2}\). The latter strengthening is genuine: the full divisibility frame with unrestricted propositional valuations fails Grz, as witnessed by the valuation asserting that \(v_2(n)\) is odd, which alternates indefinitely along successive powers of two.

## Limitations
The theorem is limited to pure first-order **sentence** substitutions and finite cyclic groups. It does not claim Grz.2 for unrestricted propositional valuations, all finite abelian groups, or richer arithmetic languages naming prime divisors or group orders. The group-theoretic elimination theorem and the modal finite-Boolean completeness theorem are used as established published inputs, not reproved from scratch. The classification has not undergone an independent external audit. An equivalent result in unindexed modal model theory, or in the 2018 thesis cited by Berger et al., remains a potential bibliographic overlap risk.

## References
1. S. Berger, A. C. Block and B. Löwe, *The modal logic of abelian groups*, Algebra Universalis **84**, article 25 (published online 2023-07-26), DOI: https://doi.org/10.1007/s00012-023-00821-9. Primary MSC 03B45.
2. S. Bova and B. Martin, *First-Order Queries on Finite Abelian Groups*, CSL 2015, LIPIcs **41**, 41–59, DOI: https://doi.org/10.4230/LIPIcs.CSL.2015.41 (Baur–Monk invariant-sentence reduction).
3. W. A. Wołoszyn, *Grzegorczyk Logic Unlocked*, arXiv:2505.09836, section 6 and Theorem 18, https://arxiv.org/abs/2505.09836 (finite Boolean lattice completeness). This later source supplies a tool, not the source date assigning the research direction.
