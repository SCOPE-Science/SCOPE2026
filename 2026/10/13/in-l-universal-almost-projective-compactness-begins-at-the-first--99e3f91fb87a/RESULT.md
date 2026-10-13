# In L, universal almost-projective compactness begins at the first weakly compact cardinal
## Finding

Assume
\[
V=L
\]
and that a weakly compact cardinal exists. Let
\[
\kappa_*
\]
be the first weakly compact cardinal.

For every regular uncountable cardinal \(\lambda\), define \(\mathsf{PC}(\lambda)\) to mean:

> for every ring \(R\) with \(|R|<\lambda\), every \(\le\!\lambda\)-generated \(\lambda\)-projective left \(R\)-module is projective.

Then
\[
\kappa_*
=
\min\left\{
\lambda:
\lambda\text{ is regular uncountable and }\mathsf{PC}(\lambda)
\right\}.
\]

Moreover, every failure below \(\kappa_*\) is already witnessed over the single countable ring
\[
R=\mathbb Z.
\]

## Assumptions and scope

A \(\le\!\lambda\)-generated \(R\)-module \(M\) is \(\lambda\)-projective if it admits the local projectivity system of Calderoni--Yanowitz. Their Proposition 2.7 gives the equivalent filtration formulation used here: \(M\) is \(\lambda\)-projective exactly when it has a continuous \(\lambda\)-filtration
\[
M=\bigcup_{\alpha<\lambda}M_\alpha
\]
whose stages \(M_\alpha\) are \(<\!\lambda\)-generated projective modules.

The statement is conditional on \(V=L\) and on the existence of a weakly compact cardinal. The minimum is taken only over regular uncountable cardinals.

## Proof

Let \(\kappa_*\) be the first weakly compact cardinal.

### The upper endpoint

Calderoni--Yanowitz prove that if \(\kappa\) is weakly compact and \(M\) is a \(\le\!\kappa\)-generated \(\kappa\)-projective module, then \(M\) is projective.

Applying their theorem at
\[
\kappa=\kappa_*
\]
gives \(\mathsf{PC}(\kappa_*)\). The definition of \(\mathsf{PC}\) imposes the additional harmless restriction
\[
|R|<\kappa_*.
\]

### Every regular cardinal below the endpoint fails

Fix a regular uncountable
\[
\lambda<\kappa_*.
\]

Shelah--Strüngmann prove under \(V=L\) that there exists an almost-free indecomposable minimal abelian group
\[
G
\]
of cardinality \(\lambda\).

Their construction writes \(G\) as the union
\[
G=\bigcup_{\alpha<\lambda}G_\alpha
\]
of an increasing continuous chain. Each \(G_\alpha\) is a free abelian group of cardinality below \(\lambda\). Thus, viewed as \(\mathbb Z\)-modules, the \(G_\alpha\) are \(<\!\lambda\)-generated projective modules.

Consequently
\[
\{G_\alpha:\alpha<\lambda\}
\]
is a \(\lambda\)-filtration of \(G\) by projective modules. Calderoni--Yanowitz's Proposition 2.7 therefore gives
\[
G\text{ is }\lambda\text{-projective}.
\]

Since
\[
|G|=\lambda,
\]
the group \(G\) is \(\le\!\lambda\)-generated.

It remains to see that \(G\) is not projective. Over the principal ideal domain \(\mathbb Z\), projective modules are free. If \(G\) were free, then because its cardinality is uncountable its free rank would be greater than one, so a partition of a basis into two nonempty pieces would give a nontrivial direct-sum decomposition of \(G\). This contradicts the indecomposability of the Shelah--Strüngmann group.

Hence
\[
G
\]
is a \(\le\!\lambda\)-generated \(\lambda\)-projective \(\mathbb Z\)-module which is not projective. Since
\[
|\mathbb Z|<\lambda,
\]
\(\mathsf{PC}(\lambda)\) fails.

As this holds for every regular uncountable
\[
\lambda<\kappa_*,
\]
while \(\mathsf{PC}(\kappa_*)\) holds, the displayed minimum is exactly \(\kappa_*\).

## Verification

The recent source was checked at the exact statements needed for both directions of the transfer.

Calderoni--Yanowitz's Theorem 1.1 states that weak compactness of \(\kappa\) forces every \(\le\!\kappa\)-generated \(\kappa\)-projective module to be projective. Their Proposition 2.7 states that a \(\le\!\kappa\)-generated module is \(\kappa\)-projective exactly when it has a \(\kappa\)-filtration consisting of projective modules. They also recall that over \(\mathbb Z\), projective modules are exactly free abelian groups.

The older lower-bound source was inspected in full text. Shelah--Strüngmann's Main Theorem 4.1 states that, under \(V=L\), for every regular uncountable \(\lambda\) below the first weakly compact cardinal there is an almost-free indecomposable minimal abelian group of cardinality \(\lambda\). In the construction they explicitly form the group as the union of an increasing continuous \(\lambda\)-chain of free groups of smaller cardinality; Theorem 4.2 records that the union is almost-free and indecomposable.

No computation or finite experiment is used. The proof is a direct implication comparison between a new universal projectivity theorem and an older sharp family of abelian-group counterexamples.

## Relationship to prior work

The classical abelian-group theory already identifies weak compactness as a compactness point for almost-free groups, and Shelah--Strüngmann provide counterexamples at every regular uncountable cardinal below the first weakly compact cardinal in \(L\).

Calderoni--Yanowitz extend the positive weakly compact theorem from free modules to almost projective modules over general rings. Their paper does not state the exact \(V=L\) threshold above and does not cite the Shelah--Strüngmann minimal-group construction.

The combination shows that the new universal module theorem is sharp, in \(L\), at every regular uncountable cardinal below the first weakly compact cardinal. The lower obstruction requires no exotic ring: \(\mathbb Z\) alone witnesses every failure.

## Limitations

The threshold statement assumes \(V=L\). It does not claim that the same lower-bound pattern holds in arbitrary models of ZFC.

The statement is restricted to regular uncountable cardinals. Singular-cardinal compactness follows a different classical mechanism and is not part of this minimum assertion.

The property \(\mathsf{PC}(\lambda)\) is formulated for rings of cardinality below \(\lambda\), although Calderoni--Yanowitz's displayed weakly compact theorem is stated more broadly.

No claim is made that weak compactness is characterized by \(\mathsf{PC}(\lambda)\) over ZFC without the \(V=L\) assumption.

## References

[1] Filippo Calderoni and Esmé Yanowitz, “Compactness for almost projective modules,” arXiv:2609.35682v1, first posted 28 September 2026.

[2] Saharon Shelah and Lutz Strüngmann, “Large indecomposable minimal groups,” *The Quarterly Journal of Mathematics* 60 (2009), no. 3, 353–365, DOI 10.1093/qmath/han012; advance publication 10 June 2008.

[3] Paul C. Eklof and Alan H. Mekler, *Almost Free Modules: Set-Theoretic Methods*, revised edition, North-Holland Mathematical Library 65, 2002.
