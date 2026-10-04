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

The proof was checked symbolically at the level needed for the theorem.

For a Haar-uniform rank-\(q\) orthogonal projection \(U\subset\mathbb R^p\) and any fixed nonzero vector \(x\), rotational invariance reduces \(\|Ux\|^2/\|x\|^2\) to the squared mass of the first \(q\) coordinates of a uniform point on the sphere. Writing that point as a normalized standard Gaussian gives
\[
B=\frac{G_1}{G_1+G_2},
\qquad
G_1\sim\chi_q^2,
\qquad
G_2\sim\chi_{p-q}^2,
\]
with independent chi-square variables. Hence \(B\sim\operatorname{Beta}(q/2,(p-q)/2)\). For \(A=(p/q)B\),
\[
\mathbb E A=1,
\qquad
\operatorname{Var}(A)=\frac{2(p-q)}{q(p+2)}.
\]
Thus at \(q/p\to\alpha\in(0,1)\), \(A\xrightarrow{P}1\) without any moment condition on the random radius multiplying it.

The source proof of Theorem 9.3 was inspected through equation (9.8). Its Steps (i)--(iv) use only the spectral hypothesis at the currently chosen proportional projection and ACI. The next paragraph uses the identity projection solely to turn the projected-energy conclusion into parent-radius recovery. Replacing that paragraph by the Haar calculation above is therefore logically valid under a one-fixed-rank spectral assumption.

The deterministic-orientation hypothesis is enough for Haar randomization because failure of uniform convergence in orientation would select a deterministic violating sequence. Borel measurability follows from continuity of \(P\mapsto x^{\mathsf T}Px\) for each fixed \(x\).

No numerical finite experiment, simulation, or timeout is used to establish an infinite-dimensional conclusion. The remaining limitation is structural: the argument needs ACI and all deterministic orientations of the chosen fixed rank.
