# Normal-subgroup antichains force homomorphic modal branching
## Finding
Let \(G\) be a group whose normal-subgroup lattice contains a finite antichain \(N_1,\ldots,N_r\) with \(r\ge 2\). For every ordered pair \(i\ne j\), choose \(a_{ij}\in N_i\setminus N_j\), use these elements as parameters, and define
\[
\theta_i:=\bigwedge_{j\ne i}(a_{ij}=e)\ \wedge\ \bigwedge_{j\ne i}(a_{ji}\ne e).
\]
Under the modal semantics in which accessibility is arbitrary group homomorphism, \(G\models\Diamond\theta_i\) for every \(i\), but for every \(i\ne j\) no homomorphic future satisfying \(\theta_i\) can have a further future satisfying \(\theta_j\). Equivalently,
\[
G\not\models\Diamond(\theta_i\wedge\Diamond\theta_j)\qquad(i\ne j).
\]
Consequently the standard \(\mathsf{S4.3}\) axiom
\[
(\Diamond p\wedge\Diamond q)\to
\bigl(\Diamond(p\wedge\Diamond q)\vee\Diamond(q\wedge\Diamond p)\bigr)
\]
fails at \(G\) with parameters whenever the normal-subgroup lattice of \(G\) is not a chain. In particular, every nontrivial finite abelian group other than a cyclic \(p\)-group fails this axiom with parameters. For \(G=(C_p)^n\), the one-dimensional subgroups give an antichain of size \((p^n-1)/(p-1)\), hence that many pairwise future-incompatible accessible parameter states.

The construction is quantitative: a normal-subgroup antichain of size \(r\) yields \(r\) simultaneously reachable formulas \(\theta_1,\ldots,\theta_r\) that are pairwise future-incompatible. This is compatible with convergence: different branches may still have a common later homomorphic image where none of the \(\theta_i\) holds.

## Assumptions and scope
Possibility \(\Diamond\varphi[\bar a]\) is interpreted by the existence of an arbitrary group homomorphism carrying the parameters \(\bar a\) to their images in a target group. Parameters are transported along further homomorphisms. The substitution language therefore contains ordinary group equations and inequalities with the displayed parameters.

An antichain means that \(N_i\not\subseteq N_j\) and \(N_j\not\subseteq N_i\) whenever \(i\ne j\). Hence \(N_i\setminus N_j\) is nonempty for every ordered pair \(i\ne j\), so the parameters \(a_{ij}\) exist.

The conclusion is an obstruction: it proves failure of the \(\mathsf{S4.3}\) axiom \(.3\). It does not claim that groups whose normal-subgroup lattice is a chain validate \(\mathsf{S4.3}\), nor does it determine the entire parameter-validity logic of any finite nontrivial group.

## Proof
Fix the antichain \(N_1,\ldots,N_r\) and the parameters \(a_{ij}\in N_i\setminus N_j\). For each \(i\), consider the quotient homomorphism
\[
q_i:G\longrightarrow G/N_i.
\]
If \(j\ne i\), then \(a_{ij}\in N_i\), so \(q_i(a_{ij})=e\). On the other hand \(a_{ji}\notin N_i\), so \(q_i(a_{ji})\ne e\). Therefore \(G/N_i\) satisfies
\[
\theta_i=\bigwedge_{j\ne i}(a_{ij}=e)\ \wedge\ \bigwedge_{j\ne i}(a_{ji}\ne e),
\]
with every parameter interpreted as its quotient image. Thus \(G\models\Diamond\theta_i\) for every \(i\).

Now fix \(i\ne j\), and suppose a homomorphic future \(H\) of \(G\) satisfies \(\theta_i\). In \(H\), the image of \(a_{ij}\) is \(e\). Every further group homomorphism preserves this equality, so in every homomorphic future of \(H\) the image of \(a_{ij}\) is still \(e\). But \(\theta_j\) contains the conjunct \(a_{ij}\ne e\), because \(a_{ij}\) appears among the incoming parameters \(\{a_{kj}:k\ne j\}\). Hence no future of \(H\) can satisfy \(\theta_j\). Therefore
\[
G\not\models\Diamond(\theta_i\wedge\Diamond\theta_j)
\]
for all \(i\ne j\).

Taking two distinct indices \(i,j\), both \(\Diamond\theta_i\) and \(\Diamond\theta_j\) hold at \(G\), while both disjuncts in the consequent of the displayed axiom \(.3\) fail. Hence that axiom is not valid at \(G\) with these parameters.

For a finite abelian group, normal subgroups are just subgroups. Its subgroup lattice is a chain exactly when the group is cyclic of prime-power order: two different prime divisors give incomparable prime-order subgroups, while a noncyclic finite abelian \(p\)-group has at least two distinct subgroups of order \(p\); conversely the subgroups of a cyclic \(p\)-group form a chain. This gives the stated finite-abelian corollary.

Finally, in \(G=(C_p)^n\), the one-dimensional subspaces are pairwise incomparable normal subgroups, and their number is
\[
\frac{p^n-1}{p-1}.
\]
Applying the construction to all of them gives the quantitative branching statement.

## Verification
The proof was checked directly at the level of kernels and transported parameters. The critical point is asymmetric parameter choice: \(a_{ij}\in N_i\setminus N_j\) is killed by the quotient modulo \(N_i\) but survives the quotient modulo \(N_j\). Equality with the identity is preserved by every later homomorphism, which is exactly what prevents a \(\theta_i\)-state from later becoming a \(\theta_j\)-state.

The argument uses no enumeration, probabilistic experiment, or unproved finite search. The finite-abelian corollary uses only the standard classification of when a finite abelian subgroup lattice is linearly ordered. The elementary-abelian count is the standard count of one-dimensional subspaces of an \(n\)-dimensional vector space over \(\mathbf F_p\).

## Relationship to prior work
Wołoszyn's 2026 paper introduces the arbitrary-homomorphism semantics used here, proves the universal lower bound \(\mathsf{S4.2}\) for parameter-validities, notes that \(a=e\) is an unpushed button at every nontrivial group, and obtains exact \(\mathsf{S4.2}\) for uniformly prime-indivisible groups by a different family of divisibility buttons. Its relevant validity section does not state a normal-subgroup antichain criterion, does not discuss \(\mathsf{S4.3}\), and does not give the finite-abelian consequence above.

The general control-statement theory of modal model theory explains why branching witnesses are informative for modal upper bounds, but it does not identify ordinary normal-subgroup antichains as such witnesses for the homomorphism semantics. Berger, Block, and Löwe compute \(\mathsf{S4.2}\) for abelian groups under subgroup embeddings, which is a different accessibility relation and does not imply the quotient-based parameter statement here.

The new structural point is that no global independence theorem for buttons is needed: pairwise incomparability in the normal-subgroup lattice already produces, by quotients, an arbitrarily large finite family of reachable states that are pairwise future-incompatible.

## Limitations
The theorem supplies a modal branching obstruction, not an exact parameter-validity classification. In particular, it leaves open what happens to axiom \(.3\) for groups with a chain of normal subgroups. Large antichains give many pairwise future-incompatible states, but the theorem does not assert the stronger independence condition for buttons used in exact \(\mathsf{S4.2}\) control arguments.

Originality is assessed to the best of the inspected literature and database searches. The underlying quotient observation is elementary, so an equivalent unstated observation could exist in related modal-model-theory discussions.

## References
1. Wojciech Aleksander Wołoszyn, “Modal group theory: homomorphisms,” arXiv:2605.15169v1, first public version 14 May 2026, DOI 10.48550/arXiv.2605.15169.
2. Joel David Hamkins and Wojciech Aleksander Wołoszyn, “Modal model theory,” *Notre Dame Journal of Formal Logic* 65(1), 2024, DOI 10.1215/00294527-2024-0001.
3. Sören Berger, Alexander Christensen Block, and Benedikt Löwe, “The modal logic of abelian groups,” *Algebra Universalis* 84, 2023, DOI 10.1007/s00012-023-00821-9.
