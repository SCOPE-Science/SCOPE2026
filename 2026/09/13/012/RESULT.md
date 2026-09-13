# Exact single-face cascade law for 5D 2-distinct-axes bootstrap percolation, with isoperimetric correction

## Context and motivation

Fix the 5-dimensional torus \(T_n^5=(\mathbb Z/n\mathbb Z)^5\) with two
competing update rules from Bernoulli(\(p\)) product initial data
(infected sites stay infected):

- **Distinct-axes rule (D):** a healthy vertex becomes infected iff its
  infected nearest neighbours span at least two distinct coordinate axes
  (two infected neighbours on the same axis do not suffice).
- **Standard rule (S):** a healthy vertex becomes infected iff it has at
  least two infected nearest neighbours, axes ignored.

Pointwise domination \(P_D\le P_S\) holds because every D-infection is
also an S-infection. The admitted target asked for a full two-sided sharp
window \(p(\log n)^4\in[c_-,c_+]\) with \(c_+/c_-\le1.15\), plus near-certain
rectangular-droplet expansion with aspect \(\gamma=2\) billed as the
axis-isoperimetric optimizer. The target investigation is documented as
blocked: single-slab rates leave a constant per-slab failure gap, and the
\(\gamma=2\) optimizer parenthetical is arithmetically false. What survives
is a self-contained, exactly proved single-face growth law plus the
isoperimetric correction. That is the headline below.

## Definitions

- Layer along \(e_5\): \(L_k=\{x_5=k\}\), a 4D torus of area \(A=n^4\)
  (in general \(A\) = face area of the rectangular face considered).
- For \(v=(y,1)\in L_1\): one below-neighbour \((y,0)\in L_0\) (axis
  \(e_5\)), one above-neighbour \((y,2)\) (same axis \(e_5\)), and 8
  in-layer neighbours along \(e_1,\dots,e_4\).
- \(r=1\) bootstrap on the 4D torus: a healthy site becomes infected iff
  at least one of its 8 in-layer neighbours is infected.

## Result (headline claim)

**Lemma (D-cascade, exact).** Suppose \(L_0\) is fully infected at time
\(0\). Under rule D, in the full dynamics with no idealization of
\(L_2,L_3,\dots\), the layer \(L_1\) evolves exactly as \(r=1\) bootstrap on
the 4D torus: \(v=(y,1)\) becomes infected iff at least one of its 8
in-layer neighbours is infected. Consequently \(L_1\) fills in finite time
iff its initial set \(S=L_1(0)\) is nonempty (within \(\mathrm{diam}\le2n\)
steps when nonempty; never if empty).

**Corollary (exact face-failure law).** Under i.i.d. Bernoulli(\(p\))
initialization of \(L_1\),
\[\mathbb P_D(L_1\ \text{never fills}\mid L_0\ \text{full})=(1-p)^A\]
exactly, with \(-\log\mathbb P(\mathrm{fail})/(pA)\to1\) as \(p\to0\).

**Comparison (S-rule).** Under rule S with \(L_0\) full and a frozen
Bernoulli(\(p\)) above-layer (one-step helper-field idealization), failure
iff both the \(A\) in-layer sites and the \(A\) above sites are empty,
i.e. \((1-p)^{2A}\) with exponent \(-\log P/(pA)\to2\). In the full
S-dynamics the upper layer only gains infections, so \((1-p)^{2A}\) is an
upper bound on the true failure probability. The D-vs-S single-face
exponent split is thus \(1\) vs \(2\).

**Isoperimetric correction (exact arithmetic).** At equal volume \(V\),
the 5D cube of side \(s=V^{1/5}\) has \(F_{\mathrm{cube}}=10V^{4/5}\).
The box \((L,L,L,L,\gamma L)\) with \(\gamma=2\) has
\(F=(8\gamma+2)\gamma^{-4/5}V^{4/5}\), i.e. coefficient
\(18\cdot2^{-4/5}\approx10.3383\) versus \(10.0\): \(3.38\%\) more surface.
Hence the cube, not the \(\gamma=2\) rectangle, is the surface minimizer,
refuting the target's "\(\gamma=2\) (axis-isoperimetric optimizer)"
identification as stated.

## Proof / evidence

*Proof of the cascade lemma.* Fix \(v=(y,1)\). The below-neighbour is
infected (axis \(e_5\) occupied). The above-neighbour lies on the same
axis \(e_5\), so infected or not it contributes no new axis. Rule D needs
\(\ge2\) distinct axes; one is \(e_5\), so \(v\) fires iff at least one of
its 8 in-layer neighbours (axes \(e_1,\dots,e_4\)) is infected. This uses
only \(L_1\) states, so \(L_1\) is closed and equals \(r=1\) bootstrap on
the connected periodic 4D grid. If \(S=\varnothing\), no in-layer counts
ever become positive and nothing fires; if \(S\ne\varnothing\), infection
spreads from any seed along connectivity and covers the finite torus in
finite time. The corollary follows since \(S=\varnothing\) has probability
\((1-p)^A\) under product initialization. Monotone coupling gives
\(P_D\le P_S\). The surface coefficients follow from the displayed
formulae, reproduced in `artifacts/compute_costs.py` and
`artifacts/results_costs.json`. ∎

*Computed verification (evidence, not proof).* Face Monte Carlo in
`artifacts/mc_faces.py` (`artifacts/results_faces.json`, up to \(T=3000\)
trials, Wilson 95% CIs): e.g. \(A=81\), D, \(p=0.03\):
\(\hat P_{\mathrm{fail}}=0.0860\,[0.0745,0.0991]\) vs predicted \(0.0848\);
\(A=256\), D, \(p=0.015\): \(0.0212\,[0.0133,0.0338]\) vs \(0.0209\);
S-configs give exponents \(\approx2.0\) throughout while D-configs give
\(\approx1.0\). All six configs' predictions fall inside or at the edge of
their intervals. A small-torus sweep (\(n=5,6\)) saturates at percolation
estimate \(1.000\) with wide CIs, confirming numerics cannot pin the
admitted sharp window and isolating the obstruction to multi-slab
iteration rather than single-face rates.

## Limitations

Proved: the single-face cascade lemma, exact \((1-p)^A\) face-failure law,
the S-rule comparison bound, and the cube-beats-\(\gamma=2\) surface
correction. Not claimed or proved: any two-sided sharp window, any ratio
bound \(c_+/c_-\le1.15\), any constant separation above
\(\lambda_{\mathrm{std}}(5,2)\), any \(\ge1-n^{-2}\) multi-slab droplet
expansion, any non-existence of spanned boxes below a window, or any
matching first-passage cost. Multi-slab near-certain expansion remains
open and requires new transverse-rescue arguments.

## Reproducibility

Scripts `artifacts/compute_costs.py` and `artifacts/mc_faces.py`
(regenerating `artifacts/results_costs.json` and
`artifacts/results_faces.json`) are copied into the public package. Seeds
are fixed (`default_rng(0)` for faces); Wilson intervals are computed as
documented in the scripts.

## References

- J. Balogh, B. Bollobás, R. Morris, "Bootstrap percolation in high
  dimensions" / "The sharp threshold for bootstrap percolation in all
  dimensions" (arXiv:0907.3097 / arXiv:1010.3326, Trans. Amer. Math. Soc.):
  sharp \(r\)-neighbour thresholds \(p_c\sim(\lambda(d,r)/\log_{r-1}n)^{d-r+1}\);
  standard-rule background the distinct-axes rule is compared against.
- J. Balogh, B. Bollobás, "Bootstrap percolation on the hypercube"
  (Probab. Theory Relat. Fields 2006): adjacent sharp-threshold context.
- A. E. Holroyd, "Sharp metastability threshold for two-dimensional
  bootstrap percolation" (2003): exact-threshold methodology.
- R. H. Schonmann, "On the behavior of some cellular automata related to
  bootstrap percolation" (Ann. Probab. 1992): critical-point classification
  for generalized bootstrap rules, including oriented/anisotropic variants.
