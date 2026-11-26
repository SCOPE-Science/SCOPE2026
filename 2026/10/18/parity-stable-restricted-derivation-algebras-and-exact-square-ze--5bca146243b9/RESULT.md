# Stable natural modules for the even–odd parity isomorphism of truncated derivation algebras

## Finding

Let \(K\) be any characteristic-two field, \(s\ge1\), \(A_n=K[t]/(t^n)\), and \(\mathfrak D_n=\operatorname{Der}_K(A_n)\). Write \(R=K[z]/(z^s)\). The map
\[
\Phi_s:D_{e(t^2)+t g(t^2)}\longmapsto D_{t^2e(t^2)+t g(t^2)},\qquad e,g\in R,
\]
is a restricted Lie algebra isomorphism \(\mathfrak D_{2s}\to\mathfrak D_{2s+1}\), with restricted power given by composition square. More strongly it identifies the associated natural representations after adding a trivial one-dimensional summand to the even module. This is a **single simultaneous** linear equivalence for all derivations, not separate similarity statements for individual operators. Over a splitting field the Jordan form of each odd-module action is obtained by adding precisely one size-one block at eigenvalue zero to the matched even-module action. The ranks of all positive powers agree over \(K\) itself.

## Proof

A derivation of \(A_n\) is determined by \(f=D(t)\), subject to \(nt^{n-1}f=0\); the induced operator is \(D_f=f\partial_t\). Thus \(f\) is unrestricted for length \(2s\) and has zero constant term for length \(2s+1\), giving the displayed bijection. Identify \(A_{2s}\) with \(R\oplus R\) by \((b,c)\mapsto b(t^2)+t c(t^2)\), and the ideal \(tA_{2s+1}\) with the same direct sum by \((b,c)\mapsto t^2b(t^2)+t c(t^2)\). In both cases differentiation of the representative gives \(c(t^2)\); for the odd quotient it is the subsequent multiplication by the allowed coefficient \(t^2e(t^2)+t g(t^2)\) that makes the derivation well-defined. On these coordinates both derivations therefore act by \((b,c)\mapsto(ec,gc)\), with the same truncation \(z^s=0\). The odd module has the remaining direct summand \(K\cdot1\), on which every derivation acts by zero. This proves simultaneous equivalence. Intertwining preserves commutators and squaring, and a derivation annihilating its entire natural module is zero; hence the bijection is restricted. The power-rank and Jordan statements follow from direct sum with the zero operator on a line.

## Context and verification

The ordinary Lie algebra parity isomorphism with the same shift of even exponents appears in *Adjoint-centralizer spectra and a characteristic-two parity isomorphism for truncated polynomial derivations* (Resultary a51032612a86, Proof §4). That calculation describes brackets and the adjoint representation, not the simultaneous splitting on the underlying truncated polynomial modules. The square-zero rank generating polynomial for both parities is explicitly given by *Parity-stable rank varieties of square-zero derivations of truncated polynomial algebras* (Resultary 0ca161a05327, Finding). That census is not a new claim here. The representation statement concerns all derivations, including nonsquare-zero ones, and does not assert any isomorphism of the underlying associative algebras. Older equivalent modular Lie algebra formulations remain possible.

The common coordinate operator above proves the result over any characteristic-two field. The supplied finite-field checker tests the intertwiner entrywise for small truncations, alongside its square-zero rank checks; this does not replace the symbolic argument.
