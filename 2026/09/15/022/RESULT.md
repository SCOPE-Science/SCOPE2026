# Gamma0: a rationally realized bicritical portrait outside the completely unobstructed list, with two non-conjugate realizations

## Context

Let d >= 2 and let Gamma be an abstract bicritical dynamic portrait of degree d with at least four postcritical vertices. Saenz-Samji (arXiv:2608.13850) classify the completely unobstructed portraits: Theorem 1.1 lists portraits (1)-(7) such that every Thurston map realizing them is unobstructed (hence rational when hyperbolic); Corollary 6.1 states these are exactly the completely unobstructed portraits. Theorem 1.2(i) states that any such Gamma containing a nonattracting cycle of length at least 2 is realized by some Thurston map with a Levy cycle (hence obstructed). The target asked which Gamma outside (1)-(7) admit a postcritically finite rational realization, which admit none, and when a rational realization is unique up to Moebius conjugacy.

## Definitions

An abstract bicritical portrait of degree d is a finite weighted directed graph with outdegree 1 at each vertex, exactly two critical vertices of local degree d, satisfying the Riemann-Hurwitz count sum(deg-1)=2d-2 and indegree-weight bound d. Vertices are critical or postcritical (forward orbit of a critical vertex). A polynomial portrait has a fixed critical vertex infinity of degree d. It is realized by a Thurston map f if isomorphic to the portrait of f on critical plus postcritical points. It is completely unobstructed if every realizing Thurston map is unobstructed (rational). For a Thurston map the orbifold weight nu(x) is the l.c.m. of local degrees over iterated preimages; chi = 2 - sum_{x in P}(1-1/nu(x)); hyperbolic means chi<0, Euclidean means chi=0. Thurston rigidity uniqueness applies only in the hyperbolic case.

## Result (Gamma0)

Let Gamma0 be the abstract bicritical polynomial portrait of degree 2 with vertices {0, infinity, v1, p, q}, local degrees deg(0)=deg(infinity)=2 and 1 elsewhere, and dynamics 0 -> v1 -> p <-> q (2-cycle), infinity -> infinity. Then:

1. Gamma0 has exactly four postcritical vertices {v1,p,q,infinity} and is not isomorphic to any of portraits (1)-(7) in Saenz-Samji Theorem 1.1.
2. Gamma0 IS realized by a postcritically finite rational map, e.g. f_+(z)=z^2+i, whose 2-cycle p=-1+i <-> q=-i is repelling of multiplier 4+4i (|.|=4sqrt2>1).
3. f_-(z)=z^2-i realizes an abstract portrait isomorphic to Gamma0, but f_+ and f_- are NOT Moebius conjugate (fixed-point multiplier products 4i vs -4i). Hence rational realization outside the unobstructed list need not be unique.
4. The orbifold of f_+ is Euclidean of signature (2,2,2,2) (chi=0), so Thurston rigidity uniqueness does not apply.

Classification consequences: a repelling (hence nonattracting) 2-cycle does not imply rational non-realizability — Theorem 1.2(i) guarantees an obstructed Thurston representative for Gamma0, but an unobstructed rational representative coexists for the same abstract portrait. So containment of a nonattracting cycle is not an obstructed-only criterion. Moebius uniqueness fails outside the completely unobstructed list even when realization exists, explained by the Euclidean orbifold.

## Proof / evidence

Portrait of f_+: critical set {0,infinity}. Orbit: 0 -> i -> -1+i -> -i -> -1+i since i^2+i=-1+i, (-1+i)^2+i=-i, (-i)^2+i=-1+i. With v1=i, p=-1+i, q=-i the values are four distinct points plus fixed infinity, so P={i,-1+i,-i,infinity} and the weighted portrait is Gamma0. Multiplier: f_+'(z)=2z, lambda=(2p)(2q)=4pq=4(-1+i)(-i)=4+4i, |lambda|=4sqrt2>1 repelling. Outside (1)-(7): Gamma0 is polynomial with fixed critical infinity plus a critical-orbit-fed 2-cycle disjoint from criticals; it matches none of (1)-(2) (which have no length-2 nonattracting cycle) nor non-polynomial (3)-(7); formally, it contains a nonattracting 2-cycle so by Theorem 1.2(i) it admits an obstructed representative and by Corollary 6.1 cannot be completely unobstructed. Isomorphism: f_- orbit 0 -> -i -> -1-i -> i -> -1-i gives v1'=-i, p'=-1-i, q'=i with the same shape; phi mapping 0->0, infinity->infinity, i->-i, -1+i->-1-i, -i->i preserves sources, targets, and degrees. Non-conjugacy: for z^2+c fixed points solve z^2-z+c=0, discriminant 1-4c != 0 for c=+-i, multipliers 2z1,2z2 with product 4z1z2=4c; 4i != -4i so multisets differ and no Moebius conjugacy exists. Orbifold: nu(infinity)=2 (preimage infinity degree 2), nu(v1)=2 (preimage 0 degree 2), nu(p)=nu(q)=2 via iterated preimage through 0; chi=2-4(1-1/2)=0 Euclidean.

## Limitations

Settles two target sub-questions negatively by one witness; does not complete the existence/non-existence classification outside (1)-(7), does not characterize all Euclidean vs hyperbolic cases, and makes no claim about the harder test portrait E1 (bounded Groebner/numeric probes recorded only as negative evidence, not non-existence).

## Reproducibility

`output/artifacts/verify_gamma0.py` checks orbit identities, cycle length and disjointness from critical points, repelling multiplier, four-point postcritical set, fixed-point multiplier products 4i vs -4i, the explicit graph isomorphism on every edge, and chi=0. Result: ALL CHECKS PASSED (re-executed by auditor).

## References

- E. Saenz, D. Samji, A classification of bicritical dynamic portraits, arXiv:2608.13850v1 (Aug 2026), Thms 1.1, 1.2, Cor 6.1, Lemma 4.1, Remark 2.1.
- W. Floyd et al., Realizing polynomial portraits (ramification portraits), Ergod. Th. Dynam. Sys. 46 (2026), DOI 10.1017/etds.2026.10279, Thms 1.1, 1.8-1.10.
- T. Lei, Matings of quadratic polynomials (bicritical obstructed iff Levy cycle).
- W. Thurston / Douady-Hubbard topological characterization (hyperbolic uniqueness up to Moebius).
