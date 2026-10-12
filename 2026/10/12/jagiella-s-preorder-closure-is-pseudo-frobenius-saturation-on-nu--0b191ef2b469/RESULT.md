# Jagiella's preorder closure is pseudo-Frobenius saturation on numerical-semigroup orders
## Finding

Let \(H\subseteq\mathbb N\) be a numerical semigroup. Define a translation-invariant partial order on \(\omega\) by
\[
P_H(x,y)
\quad\Longleftrightarrow\quad
x\le y\ \text{ and }\ y-x\in H.
\]
For a preorder \(P\), Jagiella defines an extension by
\[
P^+(x,y)
\quad\Longleftrightarrow\quad
\operatorname{Up}_{<_{P}}(y)
\subseteq
\operatorname{Up}_{<_{P}}(x).
\]
Then
\[
\boxed{(P_H)^+=P_{H\cup\operatorname{PF}(H)}}
\]
where \(\operatorname{PF}(H)\) is the pseudo-Frobenius set of \(H\). For \(H=\mathbb N\), take \(\operatorname{PF}(H)=\varnothing\).

Therefore, if
\[
H_0=H,
\qquad
H_{i+1}=H_i\cup\operatorname{PF}(H_i),
\]
and
\[
P_0=P_H,
\qquad
P_{i+1}=P_i^+,
\]
then
\[
P_i=P_{H_i}
\]
for every \(i\ge0\).

If \(H\ne\mathbb N\), every nonterminal stage adds at least its Frobenius number. Hence the iteration reaches \(\mathbb N\) in finitely many strict rounds. Writing
\[
\ell(H)=\min\{i:H_i=\mathbb N\},
\]
one has
\[
\ell(H)\le g(H)
\]
and the exact identity
\[
\boxed{
 g(H)=\sum_{i<\ell(H)} t(H_i)
}
\]
where \(g(H)=|\mathbb N\setminus H|\) is the genus and
\[
t(H_i)=|\operatorname{PF}(H_i)|
\]
is the type.

Thus, for the canonical translation-invariant definable orders in the \((\omega,\le)\) example, Jagiella's abstract upper-cone extension is exactly simultaneous pseudo-Frobenius saturation, and its finite stabilization has an exact numerical-semigroup accounting.

## Assumptions and scope

A numerical semigroup is an additive submonoid
\[
H\subseteq\mathbb N
\]
with finite complement. Its positive part is
\[
H_+=H\setminus\{0\}.
\]
For \(H\ne\mathbb N\), its pseudo-Frobenius set is
\[
\operatorname{PF}(H)
=
\{d\in\mathbb N\setminus H:
 d+s\in H\text{ for every }s\in H_+\}.
\]
The type is the cardinality of this set.

Jagiella's Section 4 considers relations of exactly the form \(P_H\) for cofinite subsets \(H\subseteq\mathbb N\), and records that such a relation is a partial order exactly when \(H\) is an additive submonoid. The result here concerns these exact translation-invariant representatives. It does not assert that arbitrary finite perturbations of them have the same step-by-step closure dynamics.

## Proof

Fix a numerical semigroup \(H\). The strict upper cone of \(x\) in \(P_H\) is
\[
\operatorname{Up}_{<_{P_H}}(x)=x+H_+.
\]
We determine exactly when
\[
\operatorname{Up}_{<_{P_H}}(y)
\subseteq
\operatorname{Up}_{<_{P_H}}(x).
\]

First suppose \(y<x\). Let
\[
m=\min H_+.
\]
Then
\[
y+m\in y+H_+.
\]
But
\[
(y+m)-x=m-(x-y)<m.
\]
If this difference is nonpositive, it is not in \(H_+\); if it is positive, it is a positive integer strictly below the least positive element \(m\) of \(H\), so again it is not in \(H_+\). Therefore
\[
y+m\notin x+H_+.
\]
Hence upper-cone inclusion is impossible when \(y<x\).

Now suppose \(y\ge x\), and put
\[
d=y-x\ge0.
\]
Translation gives
\[
 y+H_+\subseteq x+H_+
\quad\Longleftrightarrow\quad
 d+H_+\subseteq H_+.
\]
If \(d\in H\), the right-hand inclusion follows from additive closure. If \(d\notin H\), then \(d\) is a gap, and the condition
\[
d+s\in H
\quad\text{for every }s\in H_+
\]
is exactly the definition of
\[
d\in\operatorname{PF}(H).
\]
Because every such sum is positive, membership in \(H\) is equivalent to membership in \(H_+\) here. Thus
\[
P_H^+(x,y)
\quad\Longleftrightarrow\quad
x\le y\text{ and }y-x\in H\cup\operatorname{PF}(H),
\]
which proves
\[
(P_H)^+=P_{H\cup\operatorname{PF}(H)}.
\]

The numerical-semigroup literature records that adjoining all pseudo-Frobenius numbers preserves the numerical-semigroup property. Hence the same argument applies inductively and gives
\[
(P_H)_i=P_{H_i}
\]
for every finite \(i\).

If \(H_i\ne\mathbb N\), its Frobenius number is a pseudo-Frobenius number, so
\[
H_i\subsetneq H_{i+1}.
\]
Every strict step removes at least one of the finitely many initial gaps. Consequently the first terminal index \(\ell(H)\) exists and obeys
\[
\ell(H)\le g(H).
\]
At each nonterminal stage, precisely the \(t(H_i)\) pseudo-Frobenius gaps are adjoined, so
\[
g(H_{i+1})=g(H_i)-t(H_i).
\]
Telescoping from \(H_0=H\) to \(H_{\ell(H)}=\mathbb N\), whose genus is zero, yields
\[
g(H)=\sum_{i<\ell(H)}t(H_i).
\]

## Verification

The proof uses only two load-bearing external facts.

First, Jagiella defines the extension \(P\mapsto P^+\) by reverse inclusion of strict upper cones, proves it extends a preorder, and iterates it to obtain a finite-stabilization criterion. In the later \((\omega,\le)\) example, the paper represents definable Type-\(\omega\) orders, up to finite perturbation, by relations determined by cofinite additive submonoids of \(\mathbb N\).

Second, standard numerical-semigroup theory defines pseudo-Frobenius gaps by the condition
\[
d+H_+\subseteq H,
\]
and records that adjoining the pseudo-Frobenius set gives another numerical semigroup. The cited 2025 open-access article states this explicitly and also records that adjoining \(r\) pseudo-Frobenius gaps lowers genus by exactly \(r\).

Everything else is the direct upper-cone calculation above. No finite experiment is used as evidence for the infinite statement.

## Relationship to prior work

Jagiella's paper develops the preorder extension and, separately, gives the cofinite-additive-submonoid description of the translation-invariant orders occurring in the basic \((\omega,\le)\) example. The paper does not identify the resulting extension step with pseudo-Frobenius saturation; searches of the full text found no pseudo-Frobenius or numerical-semigroup formulation.

Jiménez--Urroz and Tornero study numerical semigroups and use pseudo-Frobenius adjunction as a controlled enlargement operation. Their paper also develops a distinct Apéry-saturation process for computing MED closure. That process is not Jagiella's upper-cone operation and does not supply the model-theoretic identification above.

The present statement connects these two descriptions exactly: the abstract model-theoretic closure has a standard semigroup-theoretic name and invariant, while the genus and type give a quantitative decomposition of its stabilization.

## Limitations

The exact identity
\[
(P_H)^+=P_{H\cup\operatorname{PF}(H)}
\]
is proved for the translation-invariant representatives \(P_H\). A definable order that is merely almost equal to such a representative can have altered finite upper cones, so no equality of finite-stage dynamics is claimed for arbitrary finite perturbations.

The iteration studied here saturates all pseudo-Frobenius gaps at each round. It is not asserted to coincide with MED closure or with the Apéry-saturation algorithm from the numerical-semigroup literature.

The bound \(\ell(H)\le g(H)\) is universal but not claimed to be optimal as a function of genus alone.

## References

[1] Grzegorz Jagiella, “On canonicity of almost linear minimal orders,” arXiv:2609.36313v2, first posted 28 September 2026.

[2] Jorge Jiménez--Urroz and José M. Tornero, “On the computation of the MED closure of a numerical semigroup,” *Semigroup Forum* 111 (2025), 144--162, published 7 July 2025.
