# Fixed-point normal form for finite-chain preconditionals
## Finding

Let
\[
C_n=\{0<1<\cdots<n-1\}
\]
be the \(n\)-element bounded chain, and let \(\to\) be a preconditional in the sense of Chen's algebraic semantics for the systems \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\).

For each antecedent \(a\in C_n\), define the row map
\[
q_a(b)=a\to b,
\]
its row summit
\[
r_a=q_a(a),
\]
and the set of fixed points strictly below the antecedent
\[
S_a=\{x<a:q_a(x)=x\}.
\]

Then \(\to\) is a preconditional if and only if the following finite data satisfy the displayed conditions.

First,
\[
a\le r_a\le n-1.
\]

The top row is forced:
\[
r_{n-1}=n-1,
\qquad
S_{n-1}=\{0,\ldots,n-2\}.
\]

For every \(a\), the whole row is recovered from \(S_a,r_a\) by
\[
q_a(b)=
\min\bigl((S_a\cup\{r_a\})\cap[b,n-1]\bigr)
\qquad(b\le a),
\]
and
\[
q_a(b)=r_a
\qquad(b\ge a).
\]

Finally, for every
\[
b<a,
\]
the rows must satisfy
\[
S_b\subseteq S_a,
\]
and exactly one of the following two compatibility clauses applies:
\[
r_b<a
\Longrightarrow
r_b\in S_a,
\]
\[
r_b\ge a
\Longrightarrow
r_a\le r_b.
\]

This is a complete normal form for all preconditionals on a finite chain.

It has a particularly clean consequence for the two stronger algebraic classes introduced by Chen.

For every
\[
n\ge2,
\]
the \(\mathsf T\)-algebra and \(\mathsf F\)-algebra expansions of \(C_n\) coincide, and their exact number is
\[
\boxed{(n-2)!}.
\]

Thus the first counts are
\[
1,1,2,6,24,120,\ldots
\]
for chain sizes
\[
2,3,4,5,6,7,\ldots.
\]

The Heyting implication is only one member once
\[
n\ge4.
\]

For reference, the normal form also yields the exact numbers of unrestricted preconditionals on \(C_n\):
\[
\boxed{
1,2,8,47,359,3344,36530,455907
}
\]
for
\[
n=1,\ldots,8.
\]

## Assumptions and scope

A preconditional is a binary operation on a bounded lattice satisfying Chen's Definition 3.1, equivalently Holliday's preconditional axioms.

The two derived rules used below are Chen's Lemma 3.2:

\[
b\le c
\Longrightarrow
a\to b\le a\to c,
\]
and
\[
a\to b=a\to(a\wedge b).
\]

A \(\mathsf T\)-algebra additionally satisfies conditional identity
\[
a\to a=1
\]
and semicomplementation
\[
a\wedge(a\to0)=0.
\]

An \(\mathsf F\)-algebra additionally satisfies double-negation inflation
\[
a\le\neg\neg a,
\qquad
\neg a:=a\to0.
\]

The theorem classifies expansions of the fixed labelled chain. Since a finite chain has only the identity lattice automorphism, the same numbers count isomorphism classes with chain reduct \(C_n\).

No claim is made about preconditionals on arbitrary finite lattices or about the number of relational frames representing a given chain algebra.

## Proof

Fix a preconditional on \(C_n\).

### Each row is a ceiling map onto its fixed points

Chen's consequent monotonicity gives
\[
b\le c
\Longrightarrow
q_a(b)\le q_a(c).
\]

His identity
\[
a\to b=a\to(a\wedge b)
\]
immediately gives
\[
q_a(b)=q_a(a)=r_a
\qquad(b\ge a).
\]

The lower-bound axiom
\[
a\wedge b\le a\to b
\]
gives
\[
b\le q_a(b)
\qquad(b\le a),
\]
and in particular
\[
a\le r_a.
\]

The importation axiom with the same antecedent twice yields
\[
q_a(q_a(c))\le q_a(c).
\]

If
\[
q_a(c)\le a,
\]
the lower-bound axiom applied to \(q_a(c)\) gives the reverse inequality, so
\[
q_a(q_a(c))=q_a(c).
\]

If
\[
q_a(c)>a,
\]
then the row is already constant above \(a\), so
\[
q_a(q_a(c))=r_a.
\]
Monotonicity also gives
\[
q_a(c)\le r_a,
\]
while importation gives
\[
r_a\le q_a(c).
\]
Hence again
\[
q_a(q_a(c))=q_a(c).
\]

Thus every value of \(q_a\) is a fixed point.

There are no fixed points strictly between \(a\) and \(r_a\), because every input at least \(a\) is sent to \(r_a\). There are no fixed points above \(r_a\) either. Hence
\[
\operatorname{Fix}(q_a)=S_a\cup\{r_a\}.
\]

If \(b\le a\), then \(q_a(b)\) is a fixed point at least \(b\). If \(y\) is any fixed point with
\[
y\ge b,
\]
monotonicity gives
\[
q_a(b)\le q_a(y)=y.
\]
Therefore \(q_a(b)\) is the least fixed point above \(b\), proving the row formula.

For the top antecedent \(n-1\), the first preconditional axiom and the lower-bound axiom give
\[
(n-1)\to b=b.
\]
So the top-row data are forced as claimed.

### Importation is exactly the cross-row compatibility

Let
\[
b<a.
\]

Take
\[
x\in S_b.
\]
Then
\[
q_b(x)=x.
\]
The importation axiom for the pair \(a,b\) gives
\[
q_a(x)\le x.
\]
Since \(x<b<a\), the lower-bound axiom gives
\[
x\le q_a(x).
\]
Thus
\[
q_a(x)=x,
\]
so
\[
S_b\subseteq S_a.
\]

Now apply the same inequality to the summit
\[
r_b=q_b(b).
\]
We obtain
\[
q_a(r_b)\le r_b.
\]

If
\[
r_b<a,
\]
the lower-bound axiom forces equality, hence
\[
r_b\in S_a.
\]

If
\[
r_b\ge a,
\]
the row formula gives
\[
q_a(r_b)=r_a,
\]
hence
\[
r_a\le r_b.
\]

This proves necessity of all normal-form conditions.

Conversely, suppose data \(S_a,r_a\) satisfy those conditions and define the rows by the displayed ceiling formula.

The lower-bound axiom is immediate. Each row is nondecreasing, so the consequent-decrease axiom and consequent monotonicity hold, and the equality
\[
a\to b=a\to(a\wedge b)
\]
holds by construction. The top row is the identity.

It remains to check importation. Put
\[
d=a\wedge b.
\]
Every value of \(q_d\) lies in
\[
S_d\cup\{r_d\}.
\]

For a value in \(S_d\), nesting gives membership in \(S_a\), so \(q_a\) fixes it.

For \(r_d\), if
\[
r_d<a,
\]
the compatibility rule puts \(r_d\) in \(S_a\), so it is fixed. If
\[
r_d\ge a,
\]
the other compatibility rule gives
\[
q_a(r_d)=r_a\le r_d.
\]

Therefore
\[
q_a(q_d(c))\le q_d(c)
\]
for every \(c\), which is exactly the remaining importation axiom. The normal form is sufficient.

### The factorial \(\mathsf T=\mathsf F\) specialization

Now impose conditional identity. Since
\[
r_a=q_a(a),
\]
we get
\[
r_a=n-1
\]
for every \(a\).

For
\[
a>0,
\]
semicomplementation on a chain says
\[
\min(a,q_a(0))=0,
\]
so
\[
q_a(0)=0,
\]
equivalently
\[
0\in S_a.
\]

With every summit equal to \(n-1\), the summit compatibility clause is automatic. The only remaining cross-row condition is
\[
S_0\subseteq S_1\subseteq\cdots\subseteq S_{n-1}.
\]

Also,
\[
S_0=\varnothing,
\qquad
S_1=\{0\},
\qquad
S_{n-1}=\{0,\ldots,n-2\}.
\]

For each
\[
j\in\{1,\ldots,n-2\},
\]
nesting implies that \(j\) has a unique first stage
\[
t_j=\min\{a:j\in S_a\}.
\]
Because \(j\) cannot occur before it is below the antecedent and must occur by the top row,
\[
t_j\in\{j+1,\ldots,n-1\}.
\]

Conversely, arbitrary independent choices of these first-entry stages define a unique nested family \(S_a\).

Hence the number of choices is
\[
\prod_{j=1}^{n-2}(n-1-j)
=
(n-2)!.
\]

Finally, in every such \(\mathsf T\)-expansion,
\[
\neg0=n-1
\]
and
\[
\neg a=0
\qquad(a>0).
\]
Thus
\[
a\le\neg\neg a
\]
holds automatically. Every \(\mathsf T\)-chain is already an \(\mathsf F\)-chain.

## Verification

The bundled checker performs two independent finite replays.

First, for
\[
n\le3,
\]
it exhaustively scans every binary operation on the \(n\)-element chain and tests the five preconditional axioms literally. It obtains
\[
1,2,8
\]
preconditionals and
\[
1,1,1
\]
\(\mathsf T\)- and \(\mathsf F\)-expansions for
\[
n=1,2,3.
\]

Second, it enumerates the normal-form data through
\[
n=8,
\]
constructs the corresponding operations, and tests the original axioms directly. The unrestricted counts are
\[
1,2,8,47,359,3344,36530,455907.
\]

For every
\[
2\le n\le8,
\]
the \(\mathsf T\)- and \(\mathsf F\)-counts agree with
\[
(n-2)!.
\]

The finite replay corroborates the symbolic proof; the classification for arbitrary finite \(n\) does not rely on extrapolation from these counts.

## Relationship to prior work

Chen introduces algebraic semantics for three systems: \(\mathsf K\)-algebras are bounded lattices with a preconditional; \(\mathsf T\)-algebras additionally satisfy conditional identity and semicomplementation; and \(\mathsf F\)-algebras additionally satisfy double-negation inflation. The paper proves strong completeness and the finite model property for the stronger systems.

The checked full text contains no finite-chain specialization. In particular, there is no occurrence of “chain,” and it does not enumerate preconditionals on finite linearly ordered lattices.

Holliday's earlier work introduces preconditionals and proves general algebraic and relational representation results. The checked material likewise does not provide a finite-chain fixed-point normal form or factorial enumeration of the conditional-identity classes.

The present result uses the new paper's precise \(\mathsf K/\mathsf T/\mathsf F\) hierarchy and extracts its complete behavior on the simplest nontrivial finite lattice family. The equality
\[
\mathsf T=\mathsf F
\]
on chains is not a general theorem: the extra double-negation condition is meaningful on arbitrary lattices.

Targeted searches for finite-chain preconditionals, chain \(\mathsf T\)- and \(\mathsf F\)-algebras, fixed-point normal forms, and factorial counts did not locate an equivalent result.

## Limitations

The factorial formula is specific to finite chains and to the \(\mathsf T/\mathsf F\) axioms of the source.

The unrestricted \(\mathsf K\)-normal form is complete, but no simple closed formula for the number of all \(\mathsf K\)-expansions is claimed. The displayed first eight counts come from exact enumeration of the normal form.

The theorem does not imply a complexity improvement for the source's decision procedures.

The result classifies algebraic expansions, not relational representations; a single chain preconditional may admit multiple representing frames.

## References

[1] Zhicheng Chen, “Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations,” arXiv:2607.20221, first posted 22 July 2026.

[2] Wesley H. Holliday, “Preconditionals,” arXiv:2402.02296, first posted 3 February 2024.

[3] Wesley H. Holliday, “A Fundamental Non-Classical Logic,” *Logics* 1 (2023), 56–79. DOI:10.3390/logics1010004.
