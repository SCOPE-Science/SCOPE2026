# Characteristic zero exactly governs isotropy detection in differential Ore extensions

Let \(k\) be a field and, for a nonconstant polynomial \(h\in k[x]\), put
\[
A_h=k[x][t;h(x)\partial_x]
   =k\langle x,t\mid tx-xt=h(x)\rangle.
\]
For a \(k\)-derivation \(D\) of \(A_h\), write
\[
\operatorname{Aut}_D(A_h)=\{\rho\in\operatorname{Aut}_k(A_h):\rho D=D\rho\}.
\]
Give \(A_h\) its usual PBW total degree and give an automorphism the maximum degree of its values on \(x,t\).

## Main theorem

For a field \(k\), the following are equivalent.

1. \(\operatorname{char}k=0\).
2. For every \(h\in k[x]\setminus k\) and every \(D\in\operatorname{Der}_k(A_h)\),
   \[
   D\text{ is locally nilpotent}
   \quad\Longleftrightarrow\quad
   \operatorname{Aut}_D(A_h)\text{ contains automorphisms of arbitrarily large degree}.
   \]

Thus the algebraic-closedness hypothesis in Theorem 22 of Baltazar--Lopes--Morales, arXiv:2609.19470v1, is unnecessary for the differential Ore-extension part of their theorem: characteristic zero alone is sufficient. Conversely, characteristic zero is sharp, even if one restricts the non-locally-nilpotent side to locally finite derivations.

## Characteristic-zero extension

Assume \(\operatorname{char}k=0\). The proof of the recent theorem can be descended to an arbitrary field because the two structural inputs used in the differential Ore-extension argument are already available over such fields.

First, Benkart--Lopes--Ondrus determine \(\operatorname{Aut}(A_h)\) over arbitrary fields. If \(N=\deg h\ge1\), every automorphism has the form
\[
\sigma_r\circ\tau_{a,b},
\qquad
\sigma_r(x)=x,\quad \sigma_r(t)=t+r(x),
\]
\[
\tau_{a,b}(x)=ax+b,\qquad
\tau_{a,b}(t)=a^{N-1}t,
\]
where \(a\in k^\times\), \(b\in k\), and \(h(ax+b)=a^Nh(x)\).

Second, Kaygorodov--Lopes--Mashurov prove over an arbitrary characteristic-zero field that
\[
\operatorname{LND}(A_h)
 =\{D_g:g\in k[x]\},
\qquad
D_g(x)=0,\quad D_g(t)=g(x).
\]
Their Section 2 explicitly takes the ground field to be arbitrary of characteristic zero.

For completeness, the part of the isotropy proof where characteristic matters is recorded here.

Write
\[
h(x)=c x^N+d x^{N-1}+\cdots,\qquad c\ne0.
\]
Since \(N\) is invertible in \(k\), the change
\[
X=x+\frac{d}{Nc},\qquad T=c^{-1}t
\]
identifies \(A_h\) with \(A_{h_*}\), where \(h_*\) is monic and has zero \(X^{N-1}\)-coefficient. For such a normalized polynomial, the identity
\[
h_*(aX+b)=a^N h_*(X)
\]
forces \(b=0\) by comparing the \(X^{N-1}\)-coefficient. Hence every automorphism has the normalized form
\[
\rho=\sigma_r\tau_a,
\qquad
\rho(X)=aX,\quad
\rho(T)=a^{N-1}(T+r(X)).
\]
Affine normalization preserves local nilpotence and whether automorphism degrees are bounded.

Suppose now that \(\operatorname{Aut}_D(A_h)\) has unbounded degree. The arbitrary-field automorphism description shows that there are commuting automorphisms \(\rho_n=\sigma_{r_n}\tau_{a_n}\) with \(\deg r_n\to\infty\).

If
\[
D(X)=\sum_{i=0}^m u_i(X)T^i,
\qquad m\ge1,
\]
then comparing the coefficient of \(T^{m-1}\) in \(\rho D(X)=D\rho(X)\) gives
\[
m a^{m(N-1)}u_m(aX)r(X)
 =a u_{m-1}(X)-a^{(m-1)(N-1)}u_{m-1}(aX).
\]
Because \(m\ne0\) in characteristic zero, this bounds \(\deg r\) independently of \(\rho\), a contradiction. Thus \(D(X)\in k[X]\).

If instead \(D(X)=p(X)\ne0\), applying \(D\) to \([T,X]=h(X)\) first shows
\[
D(T)=b(X)T+c(X)
\]
(the coefficient of \(T^{s-1}\) in \([D(T),X]\) would be \(s v_s(X)h(X)\), nonzero in characteristic zero if \(s\ge2\)). Commutation with \(\rho=\sigma_r\tau_a\) then yields
\[
p(X)r'(X)-b(X)r(X)=a^{1-N}c(aX)-c(X). \tag{1}
\]
The right side has degree bounded independently of \(\rho\). If \(d=\deg r\), the derivative term has the expected degree because \(d\ne0\) in \(k\). Comparing the leading degrees in (1) bounds \(d\), except possibly when a single fixed equality between \(d\) and the leading coefficients of \(p,b\) occurs; that exceptional value is itself fixed. Hence \(\deg r\) is again bounded, a contradiction.

Therefore unbounded isotropy forces \(D(X)=0\). The defining relation then gives
\[
[D(T),X]=0.
\]
The standard PBW computation in characteristic zero gives \(C_{A_h}(X)=k[X]\), so \(D(T)=g(X)\). Such a derivation lowers \(T\)-degree and is locally nilpotent.

Conversely, if \(D\) is locally nilpotent, the arbitrary-characteristic-zero classification quoted above gives \(D=D_g\). Every triangular automorphism \(\sigma_r\), \(r\in k[X]\), commutes with \(D_g\), and their degrees are unbounded. This proves the criterion over every characteristic-zero field.

## Sharp positive-characteristic obstruction

Let now \(\operatorname{char}k=p>0\). It already fails for the enveloping-type member
\[
A_x=k\langle x,t\mid tx-xt=x\rangle.
\]
Define
\[
E(x)=x,\qquad E(t)=0.
\]
This is a derivation because
\[
E(tx-xt-x)=[E(t),x]+[t,E(x)]-E(x)=x-x=0.
\]
It is not locally nilpotent, since \(E^n(x)=x\) for every \(n\ge1\). In fact it is locally finite: on the PBW basis,
\[
E(x^i t^j)=i\,x^i t^j,
\]
so every element lies in a finite-dimensional \(E\)-stable subspace (indeed \(E^p=E\)).

For every \(r(x)\in k[x]\), the triangular map
\[
\sigma_r(x)=x,\qquad \sigma_r(t)=t+r(x)
\]
is an automorphism of \(A_x\). It commutes with \(E\) exactly when
\[
E(r(x))=x r'(x)=0.
\]
Hence
\[
\{\sigma_r:r\in k[x],\ \sigma_rE=E\sigma_r\}
 =\{\sigma_r:r\in k[x^p]\}.
\]
In particular, \(\sigma_{x^{mp}}\in\operatorname{Aut}_E(A_x)\) for every \(m\ge1\), and
\[
\deg\sigma_{x^{mp}}=mp\longrightarrow\infty.
\]
Thus a locally finite, non-locally-nilpotent derivation has unbounded isotropy in every positive characteristic. This proves the reverse implication in the field-characteristic classification and exhibits the mechanism: Frobenius creates arbitrarily high-degree polynomials in the kernel of the Euler operator \(x\partial_x\).

## Context and originality boundary

Baltazar--Lopes--Morales prove the unbounded-isotropy characterization for differential Ore extensions under the standing assumption that the base field is algebraically closed of characteristic zero. Their proof uses the automorphism classification and the locally nilpotent derivation classification above. The former was proved over arbitrary fields by Benkart--Lopes--Ondrus, and the latter over arbitrary characteristic-zero fields by Kaygorodov--Lopes--Mashurov. The present characteristic-zero extension isolates that no algebraic-closedness input is needed in the remaining degree argument.

Positive-characteristic behavior of \(A_h\) is known to differ sharply: Kaygorodov--Lopes--Mashurov replace ordinary locally nilpotent derivations by iterative higher derivations, and Bavula gives an explicit positive-characteristic automorphism theory for these Ore extensions. The claim here is narrower: the explicit \(A_x\) Euler derivation above shows that the *specific unbounded-isotropy criterion* cannot survive in any positive characteristic, even after imposing local finiteness on the counterexample.

Originality is asserted only to the best of our knowledge. Targeted searches for the recent theorem together with “arbitrary field”, “positive characteristic”, “isotropy”, and the explicit \(A_x\) construction did not locate this exact field-characteristic boundary. The result is nevertheless close to a very recent preprint and its proof is short once the older arbitrary-field structure theorems are placed beside it, so independent rediscovery or a subsequent revision of that preprint is a material residual risk.

## Limitations

This record concerns only the differential Ore extensions \(A_h\) with \(h\) nonconstant. It does not remove algebraic-closedness assumptions from the first-Weyl-algebra part, the polynomial-plane theorem of Pan, or the quantum cases in arXiv:2609.19470v1. It does not classify positive-characteristic isotropy groups in general. The positive-characteristic statement is a counterexample to the ordinary-derivation criterion, not a statement about iterative higher derivations.

## References

1. R. Baltazar, S. Lopes, O. Morales, *A Characterization of Local Nilpotence for Derivations of Ore Extensions*, arXiv:2609.19470v1 (2026). https://arxiv.org/abs/2609.19470v1
2. I. Kaygorodov, S. A. Lopes, F. Mashurov, *Actions of the additive group Ga on certain noncommutative deformations of the plane*, Communications in Mathematics 29 (2021), 269--279. https://doi.org/10.2478/cm-2021-0024
3. G. Benkart, S. A. Lopes, M. Ondrus, *A Parametric Family of Subalgebras of the Weyl Algebra I. Structure and Automorphisms*, Trans. Amer. Math. Soc. 367 (2015), 1993--2021. https://arxiv.org/abs/1210.4631
4. R. Baltazar, L. Duarte Silva, G. Martini, *On the isotropy of differential Ore extensions*, arXiv:2604.17161 (2026). https://arxiv.org/abs/2604.17161
5. V. V. Bavula, *Isomorphism Problems and Groups of Automorphisms for Ore Extensions K[x][y; f d/dx] (Prime Characteristic)*, Algebras and Representation Theory 27 (2024), 2389--2422. https://doi.org/10.1007/s10468-024-10301-w
