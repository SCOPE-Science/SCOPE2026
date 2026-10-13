---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The numerical premises were checked in the full arXiv text of Kanazawa's non-Gorenstein companion example. Proposition 2.7 gives
\[
H_-^3=7,\qquad H_-^2F_-=8,\qquad H_-F_-^2=4,\qquad F_-^3=0,
\]
and Proposition 2.8 gives
\[
\operatorname{Pic}(X_-)/\operatorname{tors}\simeq \mathbf ZH_-\oplus\mathbf ZF_-.
\]
The same section presents the rational even cohomology ring
\[
\mathbf Q[H_-,F_-]/(4H_-^2-8H_-F_-+9F_-^2,\ F_-^3),
\]
which is consistent with the intersection numbers.

For an arbitrary rational divisor
\[
D=aH_-+bF_-,
\]
the square-zero hypothesis implies
\[
D^2F_-=8a(a+b)=0
\]
and
\[
D^2H_-=7a^2+16ab+4b^2=0.
\]
The first equation gives \(a=0\) or \(b=-a\). Substitution into the second gives \(b=0\) in the first case and \(-5a^2=0\) in the second. Hence \(D=0\).

If \(f:X_-\to C\) were a nonconstant morphism to a projective curve, Stein factorization reduces to a surjective morphism with connected fibers to a smooth projective curve. For a positive-degree divisor \(A\) on \(C\), the pullback \(D=f^*A\) is nonzero and satisfies \(D^2=0\), contradicting the preceding calculation.

The full companion source was also checked at its statement that \(X_+\to\mathbf P^1\) is a K3 fibration. Kanazawa's general \([3,-1]\)-block paper was checked at Proposition 3.9 and its fibration comparison. Its statement that the non-Gorenstein minus phase has a single genus-one fibration concerns one-dimensional fibers over a two-dimensional base and therefore does not cover the present theorem.

No numerical experiment, classification assumption, or inaccessible lemma is used. The unproved limit is deliberately narrow: rational maps to curves that are not morphisms on \(X_-\) are not excluded.
