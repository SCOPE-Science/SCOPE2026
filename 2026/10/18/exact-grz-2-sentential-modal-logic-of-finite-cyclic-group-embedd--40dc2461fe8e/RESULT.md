# Exact \(\mathsf{Grz.2}\) sentential modal logic of finite cyclic group embeddings

## Finding
Let \(\mathcal C\) consist of all finite cyclic groups, including the trivial group, with modal accessibility given by existence of an injective group homomorphism. Replace each propositional atom of a normal modal formula by an arbitrary **parameter-free first-order sentence in the ordinary group language**. Interpret \(\Box\) and \(\Diamond\) over all accessible groups in \(\mathcal C\). Then the normal propositional modal logic valid at **every** object under **every such sentential substitution** is exactly
\[
\boxed{\mathsf{Grz.2}.}
\]
Here \(\mathsf{Grz.2}\) is the Grzegorczyk logic with the directedness axiom \(\Diamond\Box p\to\Box\Diamond p\). In particular this theorem does not concern first-order formulas with free parameters, nor arbitrary valuations of propositional atoms on the collection of cyclic groups.

A structural strengthening establishes that for any fixed finite family of first-order group sentences their truth sets on finite cyclic groups factor through a **finite directed partial-order bounded-morphic quotient** of the divisibility frame. Conversely every finite Boolean cube is a bounded-morphic quotient under substitutions by explicit first-order prime-order-element sentences.

## Assumptions and scope
Write \(C_n\) for the group of order \(n\ge1\). Its isomorphism class is completely determined by \(n\), and \(C_n\) embeds into \(C_m\) precisely when \(n\mid m\). We therefore work with the reflexive Kripke frame \((\mathbb N_{>0},\mid)\). For each group sentence \(\sigma\), its propositional valuation is \(V_\sigma=\{n:C_n\models\sigma\}\). A modal formula has finitely many propositional atoms, and each atom receives one fixed sentence throughout the formula. Modal nesting is unrestricted. The theorem asserts validity at all positive integers, not merely at the trivial group.

We use two established theorems as external inputs: (i) the Baur--Monk elimination theorem for module sentences, which represents a first-order sentence as a Boolean combination of cardinality thresholds of primitive-positive-definable quotients; and (ii) the finite-Boolean-lattice completeness characterization of \(\mathsf{Grz.2}\). All intermediate cyclic-group and quotient calculations are proved below.

## Proof
**1. Arithmetic locality of first-order sentences.** Regard each finite cyclic group as the \(\mathbb Z\)-module \(\mathbb Z/n\mathbb Z\). The Baur--Monk theorem says each parameter-free first-order sentence is a Boolean combination of invariant conditions \(I(n)\ge k\), where \(k\) is a fixed positive integer and \(I(n)\) is the size of a quotient of two primitive-positive-definable subgroups of a finite Cartesian power of \(C_n\). Intersecting the two defining subgroups first permits a nested quotient without changing its cardinality.

Every primitive-positive formula is equivalent to an existential system \(M(x,y)=0\) of homogeneous integer linear equations. Let \(B\) be the submatrix consisting of coefficients of the quantified variables \(y\). Its solution projection onto \(x\) has exactly
\[
|\varphi(C_n)|=\frac{|\ker(M\bmod n)|}{|\ker(B\bmod n)|}.
\]
Indeed the kernel of projection on the solution set consists precisely of witness tuples satisfying \(B y=0\). Smith normal form of any integer matrix \(A\), with \(t\) columns, rank \(r\), and nonzero invariant factors \(d_1,\ldots,d_r\), gives
\[
|\ker(A\bmod n)|=n^{t-r}\prod_{j=1}^r\gcd(n,d_j).
\]
The empty matrix and zero-rank cases satisfy the same identity with empty product. Taking ratios for the projected pp sets and for a nested quotient yields
\[
I(n)=n^a\prod_{j=1}^s\gcd(n,d_j)^{\epsilon_j},
\qquad a,\epsilon_j\in\mathbb Z,\quad d_j\ge1.
\]
If \(n\) is a prime larger than every \(d_j\), this expression equals \(n^a\). Because \(I(n)\) is a positive integer for all \(n\), it follows that \(a\ge0\). Every gcd factor lies between \(1\) and the fixed number \(d_j\). If \(a>0\), then \(I(n)\) tends to infinity uniformly as \(n\to\infty\). If \(a=0\), the value \(I(n)\) depends only on the capped valuations \(\min(v_p(n),e_p)\) for finitely many primes \(p\) and finite exponents \(e_p\). It follows by taking a finite conjunction of these bounds and thresholds that for every finite set \(\Sigma\) of first-order group sentences there exist an integer \(N\ge2\), a finite prime set \(P\), and integers \(e_p\ge1\) such that, for \(n\ge N\), the truth of every \(\sigma\in\Sigma\) depends only on
\[
\bigl(\min(v_p(n),e_p)\bigr)_{p\in P}.
\]

**2. Finite directed bounded-morphic quotient.** Enlarge \(P\) to include every prime at most \(N\), and increase each cap so that \(e_p>\log_p N\). Define
\[
\tau(n)=\left(\bigl(\min(v_p(n),e_p)\bigr)_{p\in P},\;\mathbf 1_{n\ge N}\right).
\]
Let \(F\) be the image of \(\tau\), ordered coordinatewise (including the last zero--one coordinate). All tuples with last coordinate one and capped coordinates between zero and their maxima occur: multiply their prescribed prime powers by a sufficiently large prime outside \(P\). Tuples with last coordinate zero encode the individual integers \(n<N\) uniquely, since all their prime factors lie in \(P\) and none of their exponents is capped. Thus \(F\) is a finite partial order, with greatest element \(((e_p)_{p\in P},1)\); in particular it is directed.

The map \(\tau\) is a surjective bounded morphism. Its forth condition follows from \(n\mid m\Rightarrow\tau(n)\le\tau(m)\). For the back condition, fix \(\tau(n)\le(b,\delta)\in F\). If \(\delta=0\), the target corresponds to a unique \(m<N\), and the coordinate comparison ensures \(n\mid m\). If \(\delta=1\), multiply \(n\) by enough powers of primes in \(P\) to attain each requested capped exponent \(b_p\); the coordinate inequality guarantees that no exponent must decrease. If the resulting multiple is below \(N\), multiply it by a sufficiently large prime outside \(P\). The resulting multiple \(m\) satisfies \(\tau(m)=(b,1)\). This proves back as well as forth.

Every sentence in \(\Sigma\) is constant on the fibers of \(\tau\): above \(N\) by arithmetic locality, below \(N\) by injectivity there. Consequently a simultaneous structural induction on all subformulas, using both bounded-morphism conditions at each modal operator, shows that **every modal formula whose atoms are in \(\Sigma\)** has exactly the same truth value at \(n\) as at \(\tau(n)\) with the induced valuation on \(F\). The logic \(\mathsf{Grz.2}\) is valid on every finite directed partial order, so all its theorems survive every first-order sentential substitution on the original divisibility frame.

**3. Every finite Boolean lattice is an observable quotient.** Choose any distinct primes \(q_1,\ldots,q_t\). For each \(i\), let \(\beta_i\) be the parameter-free first-order group sentence stating that there is an element different from the identity whose \(q_i\)-th power is the identity. In \(C_n\), this holds if and only if \(q_i\mid n\). Thus
\[
\pi(n)=\{i\in\{1,\ldots,t\}:C_n\models\beta_i\}
\]
is a surjective bounded morphism from \((\mathbb N_{>0},\mid)\) onto the finite Boolean lattice \((2^{\{1,\ldots,t\}},\subseteq)\). The forth condition is divisibility monotonicity. For the back condition, if \(\pi(n)\subseteq S\), multiply \(n\) by exactly the missing primes \(q_i\) for \(i\in S\setminus\pi(n)\), obtaining a multiple \(m\) with \(\pi(m)=S\).

Any truth assignment to a propositional atom on the finite Boolean lattice is specified by a disjunction of the point formulas
\[
\bigwedge_{i\in S}\beta_i\ \wedge\ \bigwedge_{i\notin S}\neg\beta_i.
\]
So **every** Boolean valuation on the lattice is the image under \(\pi\) of a parameter-free first-order sentential substitution, simultaneously for finitely many atoms. The published finite-Boolean-lattice completeness theorem for \(\mathsf{Grz.2}\) states that any normal modal formula not in \(\mathsf{Grz.2}\) fails under some such valuation at some point in a finite Boolean lattice. Lift that counterexample to a cyclic group using \(\pi\). The formula is not valid under all first-order group-sentence substitutions. Combined with Step 2, this proves exact equality with \(\mathsf{Grz.2}\).

## Verification
A standalone standard-library Python checker accompanies this result. For one nontrivial finite signature system (caps \(4,3,2,2\) on primes \(2,3,5,7\) and cutoff \(N=9\)), it checked \(13{,}418\) explicit bounded-morphism back lifts, \(2{,}020\) prime-button Boolean-cube lifts, and \(1{,}900\) one-equation Smith-identity instances. It exited successfully with `CYCLIC_MODAL_VERIFY_OK`. These are finite consistency tests only. The all-sentences locality theorem uses Baur--Monk and integer Smith normal form, and the exact modal lower bound uses the published finite-Boolean-lattice characterization of \(\mathsf{Grz.2}\).

## Relationship to prior work
Wołoszyn, *Modal group theory* (arXiv:2605.14197, first posted May 13, 2026), studies group embeddings and proves \(\mathsf{S4.2}\) results for substantially larger group classes and substitution settings. The finite-cyclic, parameter-free **sentential** subcategory studied here is mathematically different; unrestricted group embeddings may escape the torsion-prime caps and finite-size distinctions that force our finite partial-order quotients. Wołoszyn, *Grzegorczyk Logic Unlocked* (arXiv:2505.09836), proves that finite Boolean algebras characterize \(\mathsf{Grz.2}\). We use that external theorem rather than claiming it as new. The module-sentence elimination theorem is likewise classical (Baur--Monk, as exposited in Gregory, DOI:10.1112/plms.12403).

The new conclusion is the *exact restricted-category modal validity theorem* and its arithmetic bounded-morphism transfer. The finite Boolean cubes alone give an upper bound on possible validities, not the lower bound; conversely the existence of directed extensions alone supplies only \(\mathsf{S4.2}\), not \(\mathsf{Grz.2}\). Both the arithmetic-locality argument and the cube countervaluation construction are necessary for the equality.

## Limitations
The theorem does not address arbitrary propositional valuations on the full divisibility frame, modal formulas with free group variables or parameters, infinite cyclic groups, all abelian groups, all groups, or arbitrary homomorphisms in place of embeddings. The finite checker is not an exhaustive computation of infinite model semantics. The two cited mathematical inputs (Baur--Monk elimination and finite-Boolean-lattice completeness for \(\mathsf{Grz.2}\)) are used with their established hypotheses. Priority against inaccessible and unindexed equivalent specialized modal-group studies cannot be guaranteed by search alone.

## References
- W. A. Wołoszyn, *Modal group theory*, arXiv:2605.14197, initial public submission May 13, 2026, https://arxiv.org/abs/2605.14197.
- W. A. Wołoszyn, *Grzegorczyk Logic Unlocked*, arXiv:2505.09836, initial public submission May 14, 2025, https://arxiv.org/abs/2505.09836 (finite Boolean-algebra completeness for \(\mathsf{Grz.2}\)).
- L. Gregory, *Decidability of theories of modules over tubular algebras*, *Proceedings of the London Mathematical Society* (2021), DOI:10.1112/plms.12403, Section 2.5 and Theorem 2.13 (Baur--Monk theorem).
- S. Bova and B. Martin, *First-Order Queries on Finite Abelian Groups*, CSL 2015, DOI:10.4230/LIPIcs.CSL.2015.41 (context on finite abelian-group first-order expressibility).
