# Characteristic-two counterexamples to Murray's Frobenius-form norm converse

## Result

Murray's 2005 Theorem 15 gives a necessary central-norm condition for two Frobenius forms to be homothetic, and Conjecture 16 proposes the converse. As stated, the converse fails in characteristic two, already for the two-dimensional algebra of dual numbers.

More generally, let \(k\) be any field of characteristic \(2\), let \(d\ge 1\), and set
\[
R_d=k[t]/(t^{2d}).
\]
Define
\[
\lambda\!\left(\sum_{i=0}^{2d-1}a_i t^i\right)=a_{2d-1},
\qquad
B(r,s)=\lambda(rs).
\]
Let \(u=1+t\in R_d^\times\), and define the second Frobenius form
\[
B_u(r,s)=B(r,su).
\]

Then:

1. \(R_d\) is a commutative local symmetric Frobenius \(k\)-algebra with residue field \(k\).
2. The Nakayama automorphism of \(B\) is \(\sigma=\mathrm{Id}\), hence has order \(n=1\).
3. Murray's norm condition holds:
   \[
   N_\sigma(u)=u\in Z(R_d).
   \]
4. Nevertheless, \(B\) and \(B_u\) are not homothetic.

Consequently, Conjecture 16 in Murray's paper is false as stated, even for commutative local symmetric Frobenius algebras. The family above supplies counterexamples in every positive even dimension. The case \(d=1\), namely \(k[t]/(t^2)\), is dimension-minimal.

## Proof

The form \(B\) is associative because
\[
B(rs,w)=\lambda(rsw)=B(r,sw).
\]
In the basis
\[
1,t,\ldots,t^{2d-1},
\]
its Gram matrix is the reverse identity matrix, since
\[
B(t^i,t^j)=1\quad\Longleftrightarrow\quad i+j=2d-1.
\]
Thus \(B\) is nondegenerate, so \(R_d\) is Frobenius. Since \(R_d\) is commutative, \(B\) is symmetric and its Nakayama automorphism is the identity. The maximal ideal is \((t)\), and \(R_d/(t)\cong k\).

The element \(u=1+t\) is a unit because \(t\) is nilpotent. Since \(\sigma=\mathrm{Id}\) has order \(1\), Murray's norm is simply
\[
N_\sigma(u)=u,
\]
which is central because \(R_d\) is commutative.

It remains to separate the homothety classes. First, \(B\) is alternating. If
\[
r=\sum_{i=0}^{2d-1}a_i t^i,
\]
then in characteristic \(2\)
\[
r^2=\sum_{i=0}^{2d-1}a_i^2t^{2i}.
\]
Only even powers of \(t\) occur, so the coefficient of the odd power \(t^{2d-1}\) vanishes. Hence
\[
B(r,r)=\lambda(r^2)=0
\]
for every \(r\in R_d\).

By contrast, put \(r=t^{d-1}\). Then
\[
B_u(r,r)
=
\lambda\!\left(t^{2d-2}(1+t)\right)
=
\lambda(t^{2d-2}+t^{2d-1})
=
1.
\]
Thus \(B_u\) is not alternating.

Alternation is invariant under Murray's homothety relation. Indeed, if
\[
C'(r,s)=\alpha C(Vr,Vs)
\]
for some \(\alpha\in k^\times\) and \(V\in\operatorname{Aut}_k(R_d)\), then \(C(v,v)=0\) for all \(v\) implies
\[
C'(r,r)=\alpha C(Vr,Vr)=0
\]
for all \(r\). Therefore an alternating form cannot be homothetic to a nonalternating one. Hence \(B\) and \(B_u\) are not homothetic.

For \(d=1\), with basis \(1,t\),
\[
[B]=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
[B_u]=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix},
\]
so the obstruction is already visible in dimension \(2\).

Finally, dimension \(1\) cannot contain a counterexample under the residue-field hypothesis: a one-dimensional unital \(k\)-algebra with \(R/\mathfrak m\cong k\) is \(k\), and any two nondegenerate bilinear forms on a one-dimensional \(k\)-space are homothetic. Thus dimension \(2\) is minimal.

## Relation to the 2005 result

Murray proves the central-norm implication in Theorem 15 and explicitly conjectures its converse in Conjecture 16. In the symmetric local case, Lemma 8 and Theorem 10 establish the desired converse under the hypothesis \(\operatorname{char}k\ne2\). Conjecture 16 itself does not retain that characteristic restriction.

The counterexamples above show that characteristic \(2\) is a genuine obstruction, not merely an artifact of the proof of the symmetric-local theorem. Any corrected general converse must at least exclude characteristic \(2\) or incorporate additional congruence data capable of detecting alternation.

## Limitations

- This result only refutes Conjecture 16 as stated in characteristic \(2\). It does not settle a corrected converse in characteristic different from \(2\), nor the general nonsymmetric case.
- The originality claim is to the best of our knowledge. Targeted searches for the conjecture, its central-norm formulation, characteristic-two counterexamples, dual-number examples, and truncated-polynomial examples did not locate a published correction or this counterexample family. A differently phrased or unindexed antecedent remains possible.

## References

1. W. Murray, *Bilinear Forms on Frobenius Algebras*, Journal of Algebra **293** (2005), 89–101. DOI: https://doi.org/10.1016/j.jalgebra.2005.07.031. Author manuscript: https://arxiv.org/abs/1401.6486.
2. B. Fauser, *Some Graphical Aspects of Frobenius Structures*, arXiv:1202.6380 (2012), later published as a book chapter in *Quantum Physics and Linguistics* (Oxford University Press, 2013).
