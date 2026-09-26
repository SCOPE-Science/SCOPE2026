# Independent Audit — 2026-09-22 campaign

**Record:** `2026/09/08/078`  
**Audit performed:** 2026-09-26 UTC  
**Audited source tree:** `d6c48ea2fe61ff88ece573d9440fa0b15027ba63`

## Claim audited

The record specializes the canonical Band–Shapira–Smilansky dihedral Sunada quantum-graph pair to equilateral unit lengths and gives a certified first-ten-generic-mode nodal table, including generic resolution index (n^*_{gen}=1).

## Correctness — PASS

I independently substituted (a=b=c=1) into the stated secular formulas and recomputed the generic roots from
(cos(2k)=\pm\sqrt5/3). The first ten roots are approximately

[
0.3648638281, 1.2059324987, 1.9356601549, 2.7767288255, 3.5064564817,
4.3475251523, 5.0772528085, 5.9183214791, 6.6480491353, 7.4891178059,
]

and each lies strictly inside its committed (8\times10^{-9})-wide bracket. The derivative at a generic root is (F'(k)=-16\cos(2k)), so it is nonzero. Re-evaluating
(g=3\cos(2k)-2) and the sign formulas reproduces the discrete pattern
(1,2,2,1,1,2,2,1,1,2) and metric-difference pattern
(1,0,1,0,1,0,1,0,1,0). Therefore the first generic mode distinguishes the pair and (n^*_{gen}=1).

The singular family (sin(2k)=0) is distinct from the generic family and is explicitly excluded by the record's generic-mode convention.

## Originality — PASS, narrowly scoped

Band–Shapira–Smilansky, *Nodal domains on isospectral quantum graphs: the resolution of isospectrality?* (arXiv:nlin/0608031), already supplies the dihedral pair, secular/transplantation formulas, and asymptotic nodal comparison for the rationally-independent-length regime. Thus neither the graph construction nor the underlying nodal formulas are new here.

The surviving originality is the finite equilateral boundary-case closure: certified low-mode brackets, genericity signs, exact first-ten nodal patterns, and the resulting finite resolution index for (a=b=c=1). I did not identify those equilateral finite-mode data in the covering papers. This is an instance-level certified datum, not a new Sunada or nodal-domain method.

Relevant open-access sources:
- https://arxiv.org/abs/nlin/0608031
- https://arxiv.org/abs/nlin/0105020
- https://arxiv.org/abs/1709.10413
- https://arxiv.org/abs/1110.0158
- https://arxiv.org/abs/1801.05246

## Scientific value — PASS

The equilateral case is a natural commensurate boundary point not covered by the rational-independence argument in the same way. A certified mode table and resolution index provide a concrete benchmark for quantum-graph spectral/nodal implementations and transplantation calculations. The scientific value is modest and instance-specific, but independently reusable.

## Final disposition

**PASS.** All three axes pass, with originality and value limited to the certified equilateral finite-mode benchmark.
