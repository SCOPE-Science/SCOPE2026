# A vacuous surjectivity hypothesis in a Kasparov-cycle preserver theorem

## Result

Let \(H\) be an infinite-dimensional separable Hilbert space, let
\(q:B(H)\to Q(H)=B(H)/K(H)\) be the Calkin quotient, and fix a unitary
\(U:H\oplus H\to H\). Define
\[
\Phi(T)=U(T\oplus T)U^* \qquad (T\in B(H)).
\]
Then \(\Phi\) is a unital linear map with the following properties.

1. It satisfies the definition of "surjective up to compact operators" printed in
   Sharifi, arXiv:2609.18619v1, namely: for every \(T\in B(H)\) there is
   \(S\in B(H)\) such that \(\Phi(T)-S\in K(H)\).
2. It preserves Kasparov cycles in both directions:
   \[
   q(T)\text{ is unitary}\iff q(\Phi(T))\text{ is unitary}.
   \]
3. It preserves essential spectra exactly:
   \[
   \sigma(q(\Phi(T)))=\sigma(q(T))\qquad(T\in B(H)).
   \]
4. The induced map
   \[
   \Psi:Q(H)\to Q(H),\qquad \Psi(q(T))=q(\Phi(T)),
   \]
   is a proper unital injective *-endomorphism. In particular it is neither a
   *-automorphism nor a *-anti-automorphism.

Consequently, Theorems 2.5, 2.9, and 2.10 of arXiv:2609.18619v1 are false **as
written** under the paper's displayed definition of "surjective up to compact
operators." The obstruction is a reversal in the definition: the displayed
condition \(\Phi(T)-S\in K(H)\) is vacuous, since one may always choose
\(S=\Phi(T)\).

The standard condition used in the linear-preserver literature is instead
\[
\tag{QS}
\forall Y\in B(H)\;\exists X\in B(H):\quad Y-\Phi(X)\in K(H),
\]
equivalently \(B(H)=\operatorname{Ran}\Phi+K(H)\). Under (QS), the amplification
counterexample above is excluded. Moreover, the Kasparov-cycle theorem corresponding
to Theorem 2.5 admits a direct repair: with (QS) in place of the printed condition,
the argument yields a surjective Jordan *-automorphism of the Calkin algebra, and
primality then yields an automorphism or anti-automorphism.

There is a second, independent overstatement in Lemma 2.6: even under the standard
condition (QS) and exact preservation of essential spectra, one need not have
\(\Phi(K(H))=K(H)\). Only the inclusion needed to define the quotient map is forced
by the displayed argument. An algebraic projection along a Hamel complement of
\(K(H)\) gives a counterexample to equality.

## Proof of the amplification counterexample

The map \(\Phi\) is a unital *-monomorphism, and \(\Phi(K(H))\subseteq K(H)\), so it
induces a unital injective *-homomorphism \(\Psi\) on \(Q(H)\). The printed
"surjective up to compact operators" condition holds trivially: for each \(T\),
take \(S=\Phi(T)\).

Because \(\Psi\) is injective,
\[
\Psi(a)^*\Psi(a)=1=\Psi(a)\Psi(a)^*
\]
if and only if
\[
a^*a=1=aa^*.
\]
Thus \(q(T)\) is unitary if and only if \(q(\Phi(T))\) is unitary, proving
bidirectional preservation of Kasparov cycles.

A unital injective *-homomorphism between C*-algebras preserves spectra. Hence
\(\sigma(\Psi(q(T)))=\sigma(q(T))\) for every \(T\), which is exactly the essential
spectrum identity required in Theorem 2.9.

It remains to show that \(\Psi\) is not onto. Relative to \(H\oplus H\), let
\[
P=\begin{pmatrix}I&0\\0&0\end{pmatrix},\qquad
F=\begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]
Every operator \(T\oplus T\) commutes with \(P\), so \(q(UPU^*)\) commutes with the
entire range of \(\Psi\). But
\[
[P,F]=\begin{pmatrix}0&I\\-I&0\end{pmatrix}
\]
is not compact. Therefore \(q(UFU^*)\) does not commute with \(q(UPU^*)\), and hence
\(q(UFU^*)\notin\operatorname{Ran}\Psi\). Thus \(\Psi\) is a proper endomorphism.

## Repair of the Kasparov-cycle theorem

Assume now the standard quotient-surjectivity condition (QS), and let \(\Phi\) be
unital modulo compact operators and preserve Kasparov cycles in both directions.
The elementary \(I\pm K\) and \(I+iK\) argument from the source shows
\(\Phi(K(H))\subseteq K(H)\), so the induced map \(\Psi:Q(H)\to Q(H)\) is well-defined.
Condition (QS) makes \(\Psi\) surjective.

Bidirectional preservation of Kasparov cycles says precisely that \(\Psi\) preserves
and reflects unitaries. A contraction is a linear combination of four unitaries, so
\(\Psi\) is bounded. Expanding \(\Psi(e^{itA})^*\Psi(e^{itA})=1\) at \(t=0\), for
selfadjoint \(A\), gives *-preservation and the Jordan identity
\(\Psi(A^2)=\Psi(A)^2\), hence \(\Psi\) is a Jordan *-homomorphism.

Injectivity can be obtained without the kernel identity used in the source. If
\(\Psi(a)=0\), then \(\Psi(1+a)=\Psi(1-a)=1\). Reflection of unitaries implies
that \(1+a\) and \(1-a\) are both unitary. Therefore
\[
a+a^*+a^*a=0,\qquad -a-a^*+a^*a=0,
\]
so \(a^*a=0\) and \(a=0\). Thus \(\Psi\) is a Jordan *-automorphism. If \(Q(H)\), or
more generally the relevant Calkin algebra, is prime, Herstein's theorem yields the
claimed automorphism/anti-automorphism dichotomy.

## The equality in Lemma 2.6 is too strong

Let \(B(H)=K(H)\oplus V\) be an algebraic direct sum with \(I\in V\), and define
\[
\Theta(k+v)=v\qquad(k\in K(H),\ v\in V).
\]
Then \(\Theta\) is linear and unital, satisfies (QS), and
\(q(\Theta(T))=q(T)\) for every \(T\). Hence it preserves every essential spectrum
exactly. Nevertheless,
\[
\Theta(K(H))=\{0\}\ne K(H).
\]
Thus the equality asserted in Lemma 2.6 does not follow even from the standard
quotient-surjectivity condition plus exact essential-spectrum preservation. The
inclusion \(\Theta(K(H))\subseteq K(H)\) is the appropriate conclusion for the
subsequent quotient construction.

## Context and literature comparison

Sharifi's v1 definition states that for each \(T\) there is \(S\) with
\(\varphi(T)-S\in K(E)\). In contrast, established preserver literature uses the
target-surjectivity form \(T-\varphi(S)\in K(E)\), equivalently
\(B(E)=\operatorname{Im}\varphi+K(E)\). This standard form appears explicitly, for
example, in Hejazian--Aghasizadeh (2012) and Yu--Cao (2023). The distinction is
mathematically decisive: the former condition is automatic for every map, while the
latter says that the induced quotient map is surjective once it is well-defined.

The source paper is a very recent v1 preprint. Searches by title, arXiv identifier,
"surjective up to compact operators," Kasparov-cycle preservation, and Calkin
amplification did not locate a prior published correction of this specific definition
or the counterexample above. Originality is therefore only claimed to the best of our
knowledge.

## Limitations

This record concerns the literal statements in arXiv:2609.18619v1. A future revised
version may correct the definition. The repair proved above addresses the
Kasparov-cycle theorem corresponding to Theorem 2.5; it does not claim a complete
replacement proof for every spectral-preserver statement in the preprint. In
particular, the equality claim in Lemma 2.6 requires separate strengthening of the
hypotheses if equality rather than inclusion is desired.

## References

1. K. Sharifi, *Linear maps preserving Kasparov cycles and the characterization of induced automorphisms*, arXiv:2609.18619v1 (2026). https://arxiv.org/abs/2609.18619
2. S. Hejazian and T. Aghasizadeh, *Equivalence Classes of Linear Mappings on B(M)*, Bull. Malays. Math. Sci. Soc. (2) 35 (2012), no. 3, 627--632. Full-text mirror: https://paperzz.com/doc/6900826/equivalence-classes-of-linear-mappings-on-b-m-
3. W.-Y. Yu and X.-H. Cao, *Linear Maps Preserving the Set of Semi-Weyl Operators*, Mathematics 11 (2023), 2208. https://doi.org/10.3390/math11092208
4. T. Aghasizadeh and S. Hejazian, *Maps preserving semi-Fredholm operators on Hilbert C*-modules*, J. Math. Anal. Appl. 354 (2009), 625--629. https://doi.org/10.1016/j.jmaa.2009.01.032
