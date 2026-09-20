# Review: Explicit root-linear maps for characteristic-two quaternion division algebras

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The quaternion calculations were checked from the standard characteristic-2 presentation `Q=K+Kj`, with `j c = sigma(c) j` and standard involution `bar(c+d j)=sigma(c)+d j`. They give `H=F+Kj` and `A=F`. Modulo `A`, direct multiplication gives the induced scalar action

`(c+d j) . z = c^2 z + b d^2 sigma(z)`.

The dimension argument was checked against the potentially misleading ordinary `F`-dimension of `H/A`: central `t in F` acts on the quotient by `t^2`, so this is a Frobenius-twisted scalar structure rather than the ordinary one. There is therefore no dimension contradiction.

The division hypothesis forces `b notin F^2`; otherwise a rescaling of `j` produces a nonzero square-zero element. For a finite 2-basis containing `b`, separability of `K/F` and pure inseparability of `F/F^2` imply that the 2-basis monomials remain a `K^2`-basis after passage to `K`. Formula (1) then splits this basis into two-dimensional `K^2` blocks that are exactly the `Q`-spans of the proposed basis vectors. The coordinate projections are consequently left-`Q` linear on `H/A`, hence root-linear on `H`, and every root-linear map is obtained uniquely from them.

The imperfection-degree-one specialization was also checked directly: `z=u^2+bv^2` is unique, and the coordinate map sends the quotient action of `c+d j` to left multiplication by `c+d j`. For `F=F_2((t))`, the even/odd Laurent decomposition gives the stated square decomposition. The division assertion for `[1,t)` follows from the standard cyclic-algebra norm criterion: the unramified quadratic extension has norms of even valuation, so `t` is not a norm.

## Originality

PASS, qualified to the best of our knowledge.

The full text of arXiv:2609.20363v1 was inspected at its definition and structural discussion of root-linear maps. It proves that root-linear maps in characteristic `2` are exactly the left-`D` linear maps from `H/A` to `D`. It then singles out quaternion division rings with the standard involution, notes `A=F` and `H` equal to the trace kernel, and states that it has no constructive description of a nonzero root-linear map there. The present result addresses exactly that stated gap for finite 2-rank centers and additionally computes the entire root-linear dual.

Targeted searches for root-linear quaternion maps, the quotient `H/A`, 2-bases/p-bases in this setting, and equivalent Hermitian/involution formulations did not locate the coordinate theorem above. Standard references on characteristic-2 quaternion algebras were used only for the classical presentation and involution. Earlier work on range-compatible maps over fields treats the commutative root-linear phenomenon, not this quaternion coordinate decomposition.

The principal residual risk is older literature on characteristic-2 quaternion algebras, Hermitian forms, or p-bases that may implicitly contain the same semilinear module decomposition without the recent term “root-linear”. The novelty claim is therefore restricted to the explicit module/dual formula and its consequence for the recent range-compatible classification, and is made only to the best of our knowledge.

## Value

PASS.

The source classification is structurally complete but leaves its noncommutative quaternion root-linear term nonconstructive. The result supplies an explicit basis, computes the exact number `2^(r-1)` of quaternion coordinates at finite 2-rank, and turns every nonlocal term in the Hermitian-matrix classification into a finite formula. The local-field example `F_2((t))` gives a particularly concrete square-root/even-odd formula rather than an existence argument.

## Limitations

The finite-rank theorem does not provide a canonical basis: the formulas depend on a quaternion presentation and on a chosen 2-basis of the center. For centers of arbitrary imperfection degree, the same coordinate mechanism works once an explicit 2-basis containing `b` is supplied, but existence of such a global basis may involve choice. No independent validation is asserted.
