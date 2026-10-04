# Semiprojective ideals of \(C(X)\): the clopen-ANR classification

## Finding

Let \(X\) be a compact metric space and let \(J\) be a closed lattice ideal of \(C(X)\). Then \(J\) is semiprojective if and only if either \(J=0\), or there is a nonempty clopen absolute neighbourhood retract \(U\subseteq X\) such that \(J=\{f\in C(X):f|_{X\setminus U}=0\}\). Equivalently, for closed \(F\subseteq X\), the ideal \(I_F=\{f\in C(X):f|_F=0\}\) is semiprojective exactly when \(X\setminus F=\varnothing\) or \(X\setminus F\) is a clopen absolute neighbourhood retract. If \(X\setminus F\) is not closed, then \(c_0\) is a contractive lattice retract of \(I_F\). In particular, for the middle-third Cantor set \(K\subset[0,1]\), \(I_K\) is not semiprojective.

This gives a sharp topological boundary for semiprojectivity at the level of closed ideals. The obstruction is not merely that an open support can fail to be an absolute neighbourhood retract: whenever the support is not closed, the ideal already contains the non-semiprojective lattice \(c_0\) as a contractive retract. For the middle-third Cantor set \(K\subset[0,1]\), the support \([0,1]\setminus K\) is open and not closed, so the corresponding ideal \(I_K\) is not semiprojective.

## Assumptions and scope

All Banach lattices are real. Let \(X\) be compact metric. For a closed set \(F\subseteq X\), write

\[
I_F=\{f\in C(X): f|_F=0\},\qquad U=X\setminus F.
\]

Every closed lattice ideal \(J\) of \(C(X)\) is of the form \(I_F\): take

\[
F=\{x\in X:g(x)=0\text{ for every }g\in J\}.
\]

For completeness, if \(f\in I_F\) and \(\varepsilon>0\), the compact set \(K_\varepsilon=\{x:|f(x)|\ge\varepsilon\}\) is contained in \(X\setminus F\). Finitely many elements of \(J\) have absolute values whose lattice supremum \(g\in J_+\) is strictly positive on \(K_\varepsilon\). After scaling, \(g\) dominates \(|f|\) on \(K_\varepsilon\). Clipping \(f\) between \(-g\) and \(g\) gives an element of \(J\) within \(\varepsilon\) of \(f\), so closedness gives \(f\in J\).

The published inputs are: semiprojectivity passes to contractive lattice retracts; \(c_0\) is not semiprojective; and for compact metric \(Y\), \(C(Y)\) is semiprojective exactly when \(Y\) is an absolute neighbourhood retract.

## Proof

Assume first that \(U=X\setminus F\) is not closed. Choose

\[
p\in \overline U\setminus U\subseteq F.
\]

Because \(X\) is metric and \(p\in\overline U\), choose distinct points \(x_n\in U\) with \(x_n\to p\) and, after passing to a subsequence,

\[
d(x_{n+1},p)<\frac14 d(x_n,p)\qquad(n\ge1).
\]

Since \(U\) is open, choose radii \(r_n>0\) satisfying

\[
r_n<\min\left\{\frac12 d(x_n,F),\frac14 d(x_n,p)\right\}.
\]

The balls \(B(x_n,r_n)\) have closures contained in \(U\). They are pairwise disjoint: if \(m>n\), then

\[
d(x_n,x_m)\ge d(x_n,p)-d(x_m,p)>\frac34d(x_n,p),
\]

whereas

\[
r_n+r_m<\frac14d(x_n,p)+\frac14d(x_m,p)<\frac5{16}d(x_n,p).
\]

By normality, choose \(h_n\in C(X)\) with

\[
0\le h_n\le1,\qquad h_n(x_n)=1,\qquad \operatorname{supp}h_n\subset B(x_n,r_n).
\]

Thus every \(h_n\) belongs to \(I_F\), and their supports are pairwise disjoint. Define

\[
i:c_0\longrightarrow I_F,\qquad i(a)=\sum_{n=1}^\infty a_n h_n.
\]

The series converges uniformly because the tail norm is at most \(\sup_{n>N}|a_n|\). Pairwise disjointness gives

\[
\|i(a)\|_\infty=\sup_n|a_n|=\|a\|_\infty,
\qquad |i(a)|=i(|a|),
\]

so \(i\) is an isometric lattice homomorphism. Define

\[
r:I_F\longrightarrow c_0,\qquad r(f)=(f(x_n))_n.
\]

Since \(x_n\to p\in F\) and \(f(p)=0\), the sequence \((f(x_n))\) lies in \(c_0\). The map \(r\) is a contractive lattice homomorphism, and the disjoint supports give \(h_m(x_n)=\delta_{mn}\). Hence

\[
r\circ i=\operatorname{id}_{c_0}.
\]

Therefore \(c_0\) is a contractive lattice retract of \(I_F\). If \(I_F\) were semiprojective, retract permanence would make \(c_0\) semiprojective, contradicting the published non-semiprojectivity of \(c_0\). Thus \(I_F\) is not semiprojective whenever \(U\) is not closed.

Now suppose \(U\) is clopen. Restriction to \(U\), with inverse given by extension by zero across \(F\), is a lattice isometric isomorphism

\[
I_F\cong C(U).
\]

Because \(U\) is compact metric, the published \(C(Y)\)-classification yields that \(I_F\) is semiprojective exactly when \(U\) is an absolute neighbourhood retract. The case \(U=\varnothing\), equivalently \(I_F=0\), is semiprojective trivially.

Combining this with the closed-ideal correspondence proves the classification. For the middle-third Cantor set \(K\subset[0,1]\), the complement is not closed, so the retract construction applies and \(I_K\) is not semiprojective.

## Verification

The proof uses no finite sampling or numerical computation. The only non-elementary inputs are three explicit statements from the primary source: Theorem A for \(C(Y)\), Proposition 2.6 for contractive retracts, and Corollary 5.8 for \(c_0\). The retract itself is constructed explicitly and all norm and lattice identities are checked above.

The special case \(I_K\) directly addresses the uncertainty stated in Remark 5.19 of the primary source: that remark records that it was unclear whether the Cantor-set ideal is semiprojective. The present argument shows that it is not.

## Relationship to prior work

Kania and Niwiński introduce semiprojectivity for Banach lattices and prove that \(C(Y)\) is semiprojective exactly when compact metric \(Y\) is an absolute neighbourhood retract. They also prove retract permanence and that \(c_0\) is not semiprojective. Their concluding discussion exhibits an exact sequence involving the Cantor-set ideal \(I_K\) and explicitly leaves the semiprojectivity of \(I_K\) unresolved.

The finding combines those published ingredients with an explicit disjoint-bump retract construction at every nonclosed open support. Targeted searches did not locate a published statement giving this closed-ideal classification or resolving the cited \(I_K\) uncertainty. Search non-detection is not a proof of novelty, especially because the underlying semiprojectivity notion is recent.

## Limitations

The classification is for closed lattice ideals of \(C(X)\) with \(X\) compact metric. It does not classify ideals in arbitrary Banach lattices, nonclosed ideals, or nonmetrizable \(C(X)\)-spaces. It also does not settle the general extension-permanence question for semiprojectivity; it only shows that the particular Cantor pullback discussed in the source has a non-semiprojective kernel.

The disjoint-bump construction is elementary and may have antecedents in other contexts. The originality claim here is limited to the semiprojectivity implication and resulting ideal classification relative to the inspected literature.

## References

1. T. Kania and M. Niwiński, *Semiprojective Banach lattices*, arXiv:2604.10624v1, first public version 12 April 2026. Relevant items: Theorem A, Proposition 2.6, Corollary 5.8, and Remark 5.19.
