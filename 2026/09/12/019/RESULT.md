# Girth-8 Ramanujan 2-lift of the Desargues graph via the unique all-unfolding signing

## Context
High-girth Ramanujan graphs sit at the intersection of expander constructions,
the cage problem, and the Marcus–Spielman–Srivastava (Bilu–Linial) signing
program. Generic theory proves Ramanujan 2-lifts exist while ignoring girth,
and high-girth constructions settle for near-Ramanujan bounds on generic
graphs. Joint exact-spectral plus strict-girth certificates on a named base
are virtually absent. The 20-vertex Desargues graph D, realized as the
generalized Petersen graph G(10,3), is the canonical laboratory: it is
connected, bipartite 10+10, cubic, of girth 6, itself the bipartite double
cover of Petersen, with unsigned spectrum
(-3)^1(-2)^4(-1)^5(1)^5(2)^4(3)^1. Its 2-lifts have 40 vertices and inherit
girth at least 6 automatically, so girth 8 is a strictly stronger,
non-automatic demand.

## Definitions
Let D have outer 10-cycle u_0..u_9, spokes (u_i,v_i), inner edges
(v_i,v_{i+3 mod 10}). An edge signing s assigns +/-1 to each of the 30 edges;
switching equivalence leaves 2^{30-20+1}=2048 classes parametrized by signs on
11 co-tree edges. A_s denotes the signed adjacency matrix and
rho(A_s) its spectral radius. The associated 2-lift has vertex set
{0..19} x {0,1} with parallel copies for + edges and crossed copies for -
edges. A base cycle unfolds (lifts to twice its length) iff its signing
parity (number of - edges mod 2) is odd. The lift is bipartite cubic; it is
Ramanujan iff all its new eigenvalues (the signed spectrum) plus the base
nontrivial eigenvalues lie within 2*sqrt(2) ~= 2.828 in absolute value.

## Result
Theorem. There exists an edge signing s of the Desargues graph D with signed
characteristic polynomial x^8(x^2-5)^6, hence signed spectral radius
rho(A_s)=sqrt(5) <= 2*sqrt(2), such that every one of the exactly 20 base
6-cycles has odd signing parity. The associated 40-vertex 2-lift is therefore
a bipartite cubic Ramanujan graph of girth exactly 8: it contains 0
four-cycles, 0 six-cycles, and 60 eight-cycles (e.g. lifted cycle
(0,1,2,3,4,34,17,10)).

The all-unfolding switching class is unique among the 2048 classes (mask 2031
in the filed co-tree coordinates). The signed eigenvalues are 0 with
multiplicity 8 and +/-sqrt(5) each with multiplicity 6.

## Proof / evidence
1. Cycle inventory: two independent enumerations — directed DFS cycle search
and induced-C6 subset test over all C(20,6) vertex sets — agree that D has no
4-cycles and exactly 20 six-cycles (vertex sets filed in
girth_census.json). Exhaustion over all 2048 masks plus a GF(2) solve of the
20x11 parity system proves exactly one switching class unfolds every 6-cycle.
2. Exact spectrum: integer LeVerrier computation over Q yields the signed
characteristic polynomial x^8(x^2-5)^6, verified by exact synthetic division
of s(z)=z^6-30z^5+...+15625 by (z-5)^6. Hence rho=sqrt(5)~2.236. An exact
rational LDL check certifies 141I +/- 50A_s positive definite (minimum pivot
1040721/14881), i.e. rho < 141/50 = 2.82 with 2.82^2=7.9524 < 8, so
rho < 2*sqrt(2).
3. Lift girth: the 40-vertex 2-lift is cubic; exhaustive simple-cycle
enumeration gives 0 four-cycles, 0 six-cycles, 60 eight-cycles, so girth
exactly 8. Its spectrum is the union of the base spectrum (nontrivial part
bounded by 2) and the signed spectrum (bounded by sqrt(5)), all within
2*sqrt(2); bipartiteness removes any -3 issue.
4. Independent replay with a different spanning tree (DFS from vertex 7,
reversed adjacency order), LeVerrier recomputation, exact Bareiss leading
principal minor positivity for all 40 minors, subset-method cycle inventory,
and BFS girth computation reproduces every claim (VERIFY_OK).

## Limitations
The certified headline is the existence claim above. The broader 2048-class
floating-point spectral survey is background only and not part of the exact
certificate. Girth-8 sharpness rests on exhaustive enumeration in the filed
scripts rather than a closed-form argument. The eightfold zero eigenvalue is
recorded as observed structure without a theoretical explanation. Uniqueness
of the all-unfolding class is proved by brute force plus GF(2) solve, not by
a structural theorem.

## Reproducibility
Run in order with stdlib-only Python 3: cycle_census.py (writes
girth_census.json), spectral_lift_certificate.py (writes
spectral_lift_certificate.json), verify_certificate.py (prints VERIFY_OK).
All paths are relative to the artifact directory. Expected outputs: 20
six-cycles with unique mask 2031; charpoly x^8(x^2-5)^6; LDL minimum pivots
1040721/14881; lift counts C4=0, C6=0, C8=60.

## References
- M. Desargues graph data: cubic symmetric on 20 vertices, G(10,3), LCF
[5,-5,9,-9]^5, integral spectrum; MathWorld DesarguesGraph;
House of Graphs entry 1036; Foster/GReGAS census.
- Bilu–Linial signing conjecture; Marcus–Spielman–Srivastava interlacing
existence of Ramanujan 2-lifts (no girth control).
- Hall–Puder–Sawin Ramanujan coverings (general r-cover existence).
- Stanica et al., spectrum of generalized Petersen graphs (unsigned only).
