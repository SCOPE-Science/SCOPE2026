# Sperner-sharp counterframe size for finite achronal-width axioms

## Finding

Goldblatt and Hodkinson define modal axioms \(U_n\) whose frame condition says, in the monomodal case, that no world has an achronal family of more than \(n\) successors, where a family is achronal when the future sets of its members are pairwise incomparable by inclusion.

Restrict attention to finite **strict partial-order** Kripke frames, so the accessibility relation \(R\) is irreflexive and transitive. For every \(n\ge1\), the smallest frame in this class that invalidates \(U_n\) has exactly
\[
\boxed{N_n=n+2+q_n}
\]
worlds, where
\[
\boxed{q_n=\min\left\{q\ge0:\binom{q}{\lfloor q/2\rfloor}\ge n+1\right\}.}
\]
Thus the first values of \(N_n\), for \(n=1,2,\ldots\), are
\[
5,7,9,10,11,13,14,15,16,18,19,20,21,22,23,24,25,26,27,29,\ldots.
\]
Moreover, the central-binomial estimate gives
\[
q_n=\log_2 n+\frac12\log_2\log_2 n+O(1),
\]
and hence
\[
\boxed{N_n=n+\log_2 n+\frac12\log_2\log_2 n+O(1).}
\]

## Assumptions and scope

The statement concerns ordinary one-relation Kripke frames with a finite underlying set. “Strict partial order” means that \(R\) is irreflexive and transitive. No reflexivity, density, branching, or linearity assumption is imposed. The minimum is the same whether or not one requires the counterframe to be rooted, because the extremal construction below is rooted and the lower bound applies to every finite strict partial-order frame.

Goldblatt and Hodkinson's paper supplies the modal axiom \(U_n\), the notion of achronality, and the exact relational characterization of \(U_n\)-validity. The sharp finite-size calculation below is a further combinatorial consequence of that characterization.

## Proof

For a world \(v\), write
\[
R(v)=\{w:vRw\}.
\]
Suppose a finite irreflexive transitive frame invalidates \(U_n\). By the Goldblatt--Hodkinson frame condition, there are a world \(x\) and distinct successors
\[
Y=\{y_0,\ldots,y_n\}\subseteq R(x)
\]
such that the \(n+1\) future sets \(R(y_i)\) are pairwise incomparable under inclusion.

First, the worlds in \(Y\) are pairwise \(R\)-incomparable. Indeed, if \(y_iRy_j\), transitivity gives
\[
R(y_j)\subseteq R(y_i),
\]
contradicting achronality.

Now put
\[
Z=R(x)\setminus Y.
\]
Transitivity gives \(R(y_i)\subseteq R(x)\). The preceding paragraph shows that no member of \(Y\) can lie in \(R(y_i)\). Consequently
\[
R(y_i)\subseteq Z
\qquad(0\le i\le n).
\]
Thus the \(n+1\) sets \(R(y_i)\) form an antichain in the Boolean lattice \(\mathcal P(Z)\). Sperner's theorem therefore yields
\[
n+1\le \binom{|Z|}{\lfloor |Z|/2\rfloor},
\]
so \(|Z|\ge q_n\). Since irreflexivity gives \(x\notin R(x)\), the worlds \(x\), the \(n+1\) members of \(Y\), and the members of \(Z\) are disjoint. Hence
\[
|F|\ge 1+(n+1)+q_n=n+2+q_n.
\]

For equality, let \(q=q_n\), let \(Z\) be a \(q\)-element set, and choose \(n+1\) distinct subsets
\[
A_0,\ldots,A_n\subseteq Z
\]
all of cardinality \(\lfloor q/2\rfloor\). Such a choice exists by the definition of \(q_n\), and the \(A_i\) are pairwise inclusion-incomparable.

Take the world set
\[
\{x,y_0,\ldots,y_n\}\cup Z
\]
and define \(R\) by
\[
xRy_i\quad(0\le i\le n),
\qquad
xRz\quad(z\in Z),
\qquad
y_iRz\quad\Longleftrightarrow\quad z\in A_i,
\]
with no other arrows. This relation is irreflexive and transitive: the only nontrivial two-step paths are \(xRy_iRz\), and the required edge \(xRz\) is already present. Also
\[
R(y_i)=A_i,
\]
so the \(y_i\) form an achronal family of size \(n+1\) above \(x\). The frame therefore invalidates \(U_n\) and has exactly \(n+2+q_n\) worlds.

Finally, the standard estimate
\[
\binom{q}{\lfloor q/2\rfloor}=\Theta\!\left(\frac{2^q}{\sqrt q}\right)
\]
implies, after inversion at level \(n+1\), that
\[
q_n=\log_2 n+\frac12\log_2\log_2 n+O(1).
\]

## Verification

A standalone exact replay constructs the extremal frame for every \(1\le n\le500\), checks irreflexivity, transitivity, rootedness, and pairwise incomparability of the \(n+1\) future sets, and verifies the exact central-binomial threshold. It additionally checks the threshold inequalities for every \(1\le n\le10000\). The replay reports

`VERIFY_OK 20520 exact assertions`

and reproduces the first twenty minima
\[
5,7,9,10,11,13,14,15,16,18,19,20,21,22,23,24,25,26,27,29.
\]

The computation is only a finite sanity check. The theorem for every \(n\) follows from the symbolic Sperner lower bound and the explicit central-layer construction above.

## Relationship to prior work

Goldblatt and Hodkinson introduce finite achronal width, define the axioms \(U_n\), and prove their Kripke-frame correspondence: \(U_n\) bounds the size of achronal successor families. Sperner's theorem gives the classical maximum size of an antichain in a Boolean lattice. Combining these two facts inside the special but natural class of strict partial-order frames yields the exact smallest counterframe size above.

Targeted searches for the result under “finite achronal width,” “strict partial order,” “minimal counterframe,” “Sperner,” “central binomial,” and \(U_n\) terminology located the achronal-width source and general combinatorial material, but no statement of this exact minimum or its asymptotic overhead. The result should therefore be understood as a short sharp consequence of known ingredients, with some residual risk of uncatalogued folklore.

## Limitations

The theorem is specific to irreflexive transitive frames. For arbitrary Kripke frames, a successor's future set need not remain inside the root's future set, so the Boolean-lattice reduction used in the lower bound does not apply in this form. The result also concerns the size of a smallest frame invalidating \(U_n\), not formula length, proof complexity, or the size of a smallest model for arbitrary formulas extending the logic.

## References

1. Robert Goldblatt and Ian Hodkinson, *Canonicity in Power and Modal Logics of Finite Achronal Width*, arXiv:2207.12596; *Review of Symbolic Logic* 17 (2024), DOI: 10.1017/S1755020323000060.
2. Emanuel Sperner, “Ein Satz über Untermengen einer endlichen Menge,” *Mathematische Zeitschrift* 27 (1928), 544–548.
