# Strictly singular derivations on C*-algebras are compact

## Statement

Let \(A\) be a complex C*-algebra and let \(\delta:A\to A\) be a bounded derivation. Then
\[
\boxed{
\delta\text{ is compact}
\iff \delta\text{ is finitely strictly singular}
\iff \delta\text{ is strictly singular}.
}
\]

More precisely, every noncompact derivation has one of the following two geometric witnesses.

1. If \(\delta\) is not weakly compact, then \(\delta\) fixes an isomorphic copy of \(c_0\).
2. If \(\delta\) is weakly compact but not compact, then \(A\) contains a 1-complemented copy \(E\simeq \ell_2\) on which \(\delta\) is bounded below.

Thus a derivation on a C*-algebra cannot be strictly singular without already being compact, although weakly compact noncompact derivations do exist.

## Proof

### 1. Strict singularity forces weak compactness

A strictly singular operator cannot fix a copy of \(c_0\). By the classical Bessaga--Pełczyński characterization, an operator is unconditionally converging exactly when it does not fix a copy of \(c_0\). Hence a strictly singular
\[
\delta:A\to A
\]
is unconditionally converging.

Pfitzner proved that every C*-algebra has Pełczyński's property (V): every unconditionally converging operator from a C*-algebra into an arbitrary Banach space is weakly compact. Therefore every strictly singular derivation \(\delta:A\to A\) is weakly compact.

The same argument also proves the first witness statement contrapositively: if \(\delta\) is not weakly compact, property (V) implies that \(\delta\) is not unconditionally converging, so it fixes a copy of \(c_0\).

### 2. Structure of weakly compact derivations

Akemann and Wright proved that a derivation \(\delta:A\to A\) is weakly compact if and only if there are pairwise orthogonal ideals
\[
I_n\cong K(H_n)
\]
and an element
\[
d=(d_n)\in \bigoplus_{n}^{c_0} I_n\subset A
\]
such that
\[
\delta=\operatorname{ad} d,
\qquad
\operatorname{ad}d(a)=da-ad.
\]

Assume now that \(\delta\) is weakly compact but not compact. We claim that for some \(n\), \(H_n\) is infinite-dimensional and \(d_n\ne0\).

Indeed, if every component on an infinite-dimensional \(H_n\) vanished, then all nonzero \(d_n\)'s would lie in finite-dimensional ideals. Since \(\|d_n\|\to0\), the derivations
\[
\operatorname{ad}\Big(\sum_{n\le N}d_n\Big)
\]
converge in operator norm to \(\operatorname{ad}d\). Each partial derivation has finite-dimensional range, because its range is contained in a finite sum of finite-dimensional ideals. Hence \(\delta\) would be compact, a contradiction.

Fix therefore an infinite-dimensional \(H\) and a nonzero component
\[
k=d_n\in I_n\cong K(H).
\]
For \(x\in I_n\), orthogonality of the ideals gives
\[
\delta(x)=[k,x].
\]

### 3. A complemented Hilbert witness for a nonzero compact commutator

Choose a unit vector \(y\in H\) such that
\[
a:=\|k^*y\|>0.
\]
Since \(k\) is compact, there is a finite-codimensional closed subspace \(M\subset H\) such that
\[
\|k|_M\|<a/2.
\]
Choose an infinite-dimensional separable closed subspace \(M_0\subset M\). Then \(M_0\simeq\ell_2\).

For \(x\in M_0\), write
\[
\theta_{x,y}(z)=\langle z,y\rangle x.
\]
The space
\[
E:=\{\theta_{x,y}:x\in M_0\}\subset K(H)\cong I_n\subset A
\]
is isometric to \(M_0\), hence to \(\ell_2\). Moreover,
\[
[k,\theta_{x,y}]
=\theta_{kx,y}-\theta_{x,k^*y},
\]
so
\[
\begin{aligned}
\|\delta(\theta_{x,y})\|
&=\|[k,\theta_{x,y}]\|\\
&\ge \|\theta_{x,k^*y}\|-\|\theta_{kx,y}\|\\
&=a\|x\|-\|kx\|\\
&>\frac a2\|x\|.
\end{aligned}
\]
Thus \(\delta\) is bounded below on \(E\).

The copy \(E\) may be chosen 1-complemented in \(A\). Let
\[
p=\theta_{y,y}\in I_n.
\]
Right multiplication by \(p\) is a contractive projection
\[
R_p:A\to Ap=I_np,
\]
and \(I_np\) is isometric to \(H\) via \(x\mapsto\theta_{x,y}\). The orthogonal projection of \(H\) onto \(M_0\) therefore induces a norm-one projection of \(Ap\) onto \(E\); composing with \(R_p\) gives a norm-one projection \(A\to E\).

Consequently every weakly compact noncompact derivation fails strict singularity, with a complemented Hilbert-space witness. Combining this with Step 1 proves
\[
\delta\text{ strictly singular}\Longrightarrow \delta\text{ compact}.
\]

Finally, every compact operator is finitely strictly singular, and every finitely strictly singular operator is strictly singular. Hence the three conditions in the statement are equivalent.

## Relation to known results

Akemann and Wright (1979) determined the structure of compact and weakly compact derivations on C*-algebras. In particular, their Theorem 3.3 gives the restricted direct-sum description used above, while their Theorem 2.2 and Corollary 2.3 characterize compact derivations and show that they are norm limits of finite-rank derivations.

Pfitzner (1994) proved that C*-algebras have Pełczyński's property (V); Krulišová (2017) explicitly restates and quantitatively strengthens this theorem. These results imply that every strictly singular operator whose domain is a C*-algebra is weakly compact, but do not by themselves upgrade a weakly compact derivation to a compact one.

Strict singularity of multiplication and elementary operators has been studied extensively, including work of Lindström--Saksman--Tylli and Mathieu--Tradacete. Those results concern multiplication operators on spaces of operators and do not provide the C*-derivation collapse above in the form located here.

The additional ingredient is the rank-one fiber argument in Step 3: every nonzero inner derivation implemented by a compact operator on an infinite-dimensional elementary ideal is bounded below on a 1-complemented Hilbert subspace. Combined with Akemann--Wright and property (V), this gives the compact/FSS/SS collapse and the \(c_0\)-versus-\(\ell_2\) witness dichotomy.

## Originality and limitations

The originality claim is **to the best of our knowledge**. Searches for exact and synonymous formulations involving strictly singular derivations, finitely strictly singular derivations, inner derivations, commutator maps, weakly compact derivations, and elementary/multiplication operators did not locate the stated equivalence or the witness dichotomy.

The principal residual risk is that the conclusion may occur as an unadvertised corollary in older derivation or elementary-operator literature. Akemann--Wright's 1979 paper was inspected at the theorem/proof level. Krulišová's 2017 statement explicitly confirming Pfitzner's property-(V) theorem was inspected; the full 1994 Pfitzner article was not exhaustively checked for this derivation-specific corollary. The 2005 Lindström--Saksman--Tylli and 2020 Mathieu--Tradacete strict-singularity papers were checked at the statement/nearby-literature level rather than exhaustively line by line.

No claim is made that the Akemann--Wright structure theorem, property (V), or the classical Bessaga--Pełczyński characterization is new. The claimed contribution is the derivation-specific collapse
\[
\mathcal K\cap\mathrm{Der}(A)=\mathcal{FSS}\cap\mathrm{Der}(A)=\mathcal{SS}\cap\mathrm{Der}(A)
\]
and the explicit noncompact witness dichotomy.

## References

1. C. A. Akemann and S. Wright, *Compact and weakly compact derivations of C*-algebras*, Pacific J. Math. **85** (1979), 253--259. https://msp.org/pjm/1979/85-2/pjm-v85-n2-p01-s.pdf
2. H. Pfitzner, *Weak compactness in the dual of a C*-algebra is determined commutatively*, Math. Ann. **298** (1994), 349--371. https://doi.org/10.1007/BF01459739
3. H. Krulišová, *C*-algebras have a quantitative version of Pełczyński's property (V)*, Czechoslovak Math. J. **67** (2017), 937--951. https://doi.org/10.21136/CMJ.2017.0242-16
4. M. Lindström, E. Saksman and H.-O. Tylli, *Strictly singular and cosingular multiplications*, Canad. J. Math. **57** (2005), 1249--1278. https://doi.org/10.4153/CJM-2005-050-7
5. M. Mathieu and P. Tradacete, *Strictly singular multiplication operators on L(X)*, Israel J. Math. **236** (2020), 685--709. https://doi.org/10.1007/s11856-020-1985-0
