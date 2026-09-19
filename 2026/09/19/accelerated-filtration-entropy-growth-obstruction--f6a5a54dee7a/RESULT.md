# Accelerated filtrations break entropy-growth detection

## Statement

Let \(k\) be a field and \(A=k[x]\). For every \(\lambda\in(0,\infty)\), put
\[
a=e^\lambda,\qquad
f_\lambda(n)=n+\lfloor a^n-1\rfloor\quad(n\ge1),
\]
and define
\[
V_0=0,\qquad
V_n=\operatorname{span}_k\{1,x,\ldots,x^{f_\lambda(n)}\}\quad(n\ge1).
\]

### Theorem A: a polynomial algebra has arbitrary prescribed positive filtration entropy

The family \(\mathcal F_\lambda=\{V_n\}_{n\ge0}\) is a finite-dimensional filtration of \(k[x]\), and
\[
\boxed{\operatorname{h}_{\operatorname{alg}}(k[x],\mathcal F_\lambda)=\lambda.}
\]
The usual degree filtration has entropy \(0\). Moreover, replacing \(a^n\) above by \(e^{n^2}\) gives a finite-dimensional filtration of entropy \(+\infty\). Hence the set of algebraic entropies realized on the single affine algebra \(k[x]\), when all finite-dimensional filtrations in Definition 2.7 of arXiv:2609.18144v1 are allowed, is exactly
\[
\boxed{[0,\infty]}.
\]

Consequently, positivity of algebraic entropy for one arbitrary finite-dimensional filtration does not detect intrinsic exponential growth. In particular, the following statements in arXiv:2609.18144v1 are false with their stated filtration hypotheses:

- Theorem 3.7, which identifies the intrinsic growth and GK dimension with those obtained from an arbitrary finite-dimensional filtration;
- Remark 3.8, since \(\operatorname{GKdim}k[x]=1\) while \(\operatorname{h}_{\operatorname{alg}}(k[x],\mathcal F_\lambda)=\lambda\) can be larger than \(1\);
- Theorem 3.9, since positive entropy need not imply infinite GK dimension;
- Theorem 3.14 and Corollary 3.15, since positive entropy need not imply exponential or non-subexponential intrinsic growth.

The counterexample does not challenge results stated for standard or natural filtrations.

### Theorem B: the quantifier repair

Let \(A\) be an infinite-dimensional affine unital algebra. Then
\[
\boxed{
A\text{ has exponential growth}
\iff
\operatorname{h}_{\operatorname{alg}}(A,\mathcal F)>0
\text{ for every finite-dimensional filtration }\mathcal F.
}
\]

Equivalently, non-exponential affine algebras always admit a zero-entropy finite-dimensional filtration (indeed, a standard one), even though they may admit other finite-dimensional filtrations of positive entropy.

A useful sufficient hypothesis for the one-filtration implication is linear upper control: if \(\mathcal F=\{V_n\}\) is finite dimensional and there is a finite-dimensional standard filtration \(\mathcal S=\{S_n\}\) together with constants \(C,D\ge0\) such that
\[
V_n\subseteq S_{Cn+D}\qquad(n\gg0),
\]
then
\[
\operatorname{h}_{\operatorname{alg}}(A,\mathcal F)>0
\quad\Longrightarrow\quad
A\text{ has exponential growth}.
\]
Thus the obstruction is that the allowed filtration index can be accelerated faster than linearly relative to an intrinsic generating filtration.

## Proof of Theorem A

The function \(f_\lambda\) is strictly increasing, so the \(V_n\) are finite dimensional, strictly increasing, and exhaust \(k[x]\). For \(m,n\ge1\),
\[
(a^n-1)+(a^m-1)\le a^{n+m}-1,
\]
because
\[
a^{n+m}-a^n-a^m+1=(a^n-1)(a^m-1)\ge0.
\]
Using \(\lfloor u\rfloor+\lfloor v\rfloor\le\lfloor u+v\rfloor\), we get
\[
f_\lambda(n)+f_\lambda(m)\le f_\lambda(n+m).
\]
Therefore
\[
V_nV_m\subseteq V_{n+m},
\]
so \(\mathcal F_\lambda\) is a finite-dimensional filtration in the sense used by arXiv:2609.18144v1.

For \(n\ge2\),
\[
\dim(V_n/V_{n-1})
=f_\lambda(n)-f_\lambda(n-1).
\]
Since
\[
a^j-2\le\lfloor a^j-1\rfloor\le a^j-1,
\]
we have
\[
(a-1)a^{n-1}
\le f_\lambda(n)-f_\lambda(n-1)
\le (a-1)a^{n-1}+2.
\]
Hence
\[
\lim_{n\to\infty}
\frac{\log\dim(V_n/V_{n-1})}{n}
=\log a=\lambda.
\]
This proves the prescribed finite entropy.

For the usual degree filtration \(V_n=\operatorname{span}\{1,x,\ldots,x^n\}\), every successive quotient has dimension \(1\), hence entropy \(0\).

For \(+\infty\), set
\[
f_\infty(n)=n+\lfloor e^{n^2}-1\rfloor.
\]
The same argument works because
\[
(e^{n^2}-1)+(e^{m^2}-1)
\le e^{(n+m)^2}-1.
\]
The successive quotient dimensions grow on the order of \(e^{n^2}\), so
\[
\limsup_{n\to\infty}
\frac{\log\dim(V_n/V_{n-1})}{n}=+\infty.
\]

For every \(\lambda>0\), \(\dim V_n\) grows exponentially in the filtration index, while the intrinsic algebra growth of \(k[x]\) is linear and \(\operatorname{GKdim}k[x]=1\). In particular, the associated graded algebra for \(\mathcal F_\lambda\) cannot be finitely generated: it is commutative but has graded entropy \(e^\lambda>1\), whereas a finitely generated commutative algebra has polynomial growth. This pinpoints the missing filtered-graded hypothesis behind the use of the standard GK-dimension comparison.

## Proof of Theorem B

First suppose \(A\) has exponential growth. Let \(\mathcal F=\{V_n\}\) be any finite-dimensional filtration. Choose a finite-dimensional generating subspace \(U\) containing \(1\). Since \(\bigcup_nV_n=A\), there is \(p\ge1\) with \(U\subseteq V_p\). Therefore
\[
\sum_{i=0}^mU^i\subseteq V_{pm}.
\]

Assume for contradiction that \(\operatorname{h}_{\operatorname{alg}}(A,\mathcal F)=0\). Writing
\[
q_n=\dim(V_n/V_{n-1}),
\]
for every \(\varepsilon>0\) we have \(q_n\le e^{\varepsilon n}\) for all sufficiently large \(n\). Hence
\[
\dim V_N=\sum_{j\le N}q_j\le e^{2\varepsilon N}
\]
for all sufficiently large \(N\), after absorbing the finite initial segment.

Exponential intrinsic growth means that for the standard growth function
\[
d_U(m)=\dim\!\left(\sum_{i=0}^mU^i\right)
\]
there exist constants \(c,r>0\) such that \(e^m\le c\,d_U(rm)\) for all sufficiently large \(m\). Combining the inclusions and the preceding bound gives
\[
e^m\le c\,d_U(rm)\le c\,\dim V_{prm}
\le c\,e^{2\varepsilon prm},
\]
which is impossible after choosing \(\varepsilon<1/(2pr)\). Thus every finite-dimensional filtration has positive entropy.

Conversely, suppose every finite-dimensional filtration has positive entropy. In particular a finite-dimensional standard filtration \(\mathcal S=\{S_n\}\) does. Let
\[
s_n=\dim S_n.
\]
Because \(S_nS_m=S_{n+m}\), the sequence \(s_n\) is submultiplicative, so \(\lim_n(\log s_n)/n\) exists. Positive algebraic entropy forces this limit to be positive, since
\[
\dim(S_n/S_{n-1})\le s_n.
\]
Thus \(s_n\) has a positive exponential rate. It also has an exponential upper bound because \(S_1\) is finite dimensional. Therefore the intrinsic growth class of \(A\) is \(\mathcal E_1\), i.e. \(A\) has exponential growth.

For the linear-control statement, if
\[
V_n\subseteq S_{Cn+D},
\]
then positive entropy of \(\mathcal F\) gives a positive exponential lower rate along the standard cumulative dimensions \(S_{Cn+D}\). Submultiplicativity of the standard growth function upgrades this to positive exponential rate, and the finite generating set gives the matching exponential upper bound. Hence \(A\) has exponential growth.

## Why the cited filtered-GK comparison does not apply

Theorem 3.7 of arXiv:2609.18144v1 attributes its unrestricted finite-dimensional-filtration statement to Krause--Lenagan, Proposition 6.6. Standard later citations of that proposition include the additional condition that the associated graded algebra be finitely generated. For example, Petukhov--Sierra explicitly state that for a finite exhaustive filtration with finitely generated associated graded algebra, Proposition 6.6 gives
\[
\operatorname{GKdim}R=\operatorname{GKdim}(\operatorname{gr}R),
\]
and other filtered-algebra references quote the same finite-generation condition. The accelerated filtration above violates that condition.

This also explains the gap in the proof of Theorem 3.14: its invocation of Theorem 3.13 for \(\operatorname{gr}_\mathcal F(A)\) requires the associated graded algebra to be affine/finitely graded, which an arbitrary finite-dimensional filtration does not ensure.

## Relation to prior literature

Bock, Gil Canto, Martín Barquero, Martín González, Ruiz Campos and Sebandal (2024) introduced the filtered-algebra entropy used here and already emphasized that it depends on the filtration. Their Proposition 3.2 shows that the linear reindexing \(W_n=V_{kn}\) multiplies entropy by \(k\), and Remark 3.3 notes that this prevents a filtration-independent supremum for nonzero entropy. They also observed that their zero-preservation results might suggest that entropy zero for one filtration implies entropy zero for every filtration. The family \(\mathcal F_\lambda\) above gives a direct negative answer: the standard filtration of \(k[x]\) has entropy zero while other finite-dimensional filtrations on the same algebra realize every positive value and \(+\infty\).

The classical filtered-GK literature treats equality of GK dimensions under extra hypotheses on the filtration or associated graded algebra. No novelty is claimed for the need for such hypotheses in abstract filtered-graded GK theory.

Targeted searches for polynomial-algebra examples realizing arbitrary filtered entropy, nonlinear/superadditive reindexing in this entropy definition, and a public correction to arXiv:2609.18144v1 did not locate the spectrum \([0,\infty]\), the counterexample above, or the universal-quantifier repair. Originality is claimed only to the best of our knowledge.

## Limitations

The result concerns the filtration-based entropy of Bock et al. and Schwarz--Sebandal, not other notions also called algebraic entropy. It does not refute statements restricted to standard or natural filtrations, nor does it by itself invalidate the Leavitt-path-algebra PI criterion in arXiv:2609.18144v1, where the relevant filtration is standard.

The primary text of Krause--Lenagan, Proposition 6.6, was not independently inspected here; accessible later sources quote it with finite generation of the associated graded algebra. This bibliographic limitation does not affect the explicit counterexample, whose verification uses only the stated definitions.

The entropy-spectrum construction is elementary, so an equivalent reparametrization observation may exist under different terminology in older filtration literature. No independent validation or formal verification is asserted.

## References

1. J. Schwarz and A. Sebandal, *Growth functions of algebras and an application to Leavitt path algebras*, arXiv:2609.18144v1, 16 September 2026. https://arxiv.org/abs/2609.18144v1
2. W. Bock, C. Gil Canto, D. Martín Barquero, C. Martín González, I. Ruiz Campos and A. Sebandal, *Algebraic Entropy of Path Algebras and Leavitt Path Algebras of Finite Graphs*, Results in Mathematics 79 (2024), Article 180. https://doi.org/10.1007/s00025-024-02198-0
3. A. V. Petukhov and S. J. Sierra, *Ideals in the Enveloping Algebra of the Positive Witt Algebra*, Algebras and Representation Theory 21 (2018), 1569--1599. https://doi.org/10.1007/s10468-018-9809-6
4. J. Gómez Torrecillas, *Gelfand-Kirillov dimension of multi-filtered algebras*, Proceedings of the Edinburgh Mathematical Society 42 (1999), 155--168. https://doi.org/10.1017/S0013091500020103
