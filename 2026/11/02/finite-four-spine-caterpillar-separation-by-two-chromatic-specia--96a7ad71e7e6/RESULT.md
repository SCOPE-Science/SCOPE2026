# Finite four-spine caterpillar separation by two chromatic specialization values

## Finding
For each integer \(6\le N\le200\), let \(\mathcal C_{4,N}\) be the isomorphism classes of caterpillars whose (leaf-stripped) spine has exactly four vertices and whose total order is \(N\). If \(T\in\mathcal C_{4,N}\), define the fourth principal specialization of its ordinary chromatic symmetric function by
\[
P_T(z)=\operatorname{ps}_4(X_T)=\sum_{\kappa:V(T)\to\{0,1,2,3\}\atop\kappa\text{ proper}}z^{\sum_{v\in V(T)}\kappa(v)}.
\]
Here \(\operatorname{ps}_4\) substitutes \((1,z,z^2,z^3,0,\ldots)\) into \(X_T\). The following finite separation holds:
\[
T\longmapsto\bigl(P_T(2)\bmod2^{64},\;P_T(3)\bmod2^{64}\bigr)
\]
is injective on \(\mathcal C_{4,N}\) for **every** \(6\le N\le200\). In total, exactly \(31{,}060{,}953\) isomorphism classes are covered, with no collisions at any fixed order.

In particular, \(\operatorname{ps}_4(X_T)\) distinguishes all four-spine caterpillars of order at most \(200\). This is a finite theorem, not a claim of separation for arbitrarily large orders or for caterpillars with other spine lengths.

## Assumptions and scope
A caterpillar of four-spine type \(\alpha=(a,b,c,d)\) has a path of four spine vertices and exactly \(a-1,b-1,c-1,d-1\) attached leaves, respectively, where \(a,d\ge2\) and \(b,c\ge1\). Its order is \(N=a+b+c+d\). These types represent isomorphic trees exactly under reversal \((a,b,c,d)\leftrightarrow(d,c,b,a)\). For enumeration, retain the lexicographically smaller representative.

Colors are the four named integers \(0,1,2,3\); all proper colorings are counted, including colorings using fewer than four colors. The reported residues are unsigned residues in \(\mathbb Z/2^{64}\mathbb Z\), not floating-point approximations and not randomized hashes. The restriction to a fixed order is essential for the stated modular injectivity check; different orders are already distinguished by evaluating the full polynomial at \(z=1\), which gives \(4\cdot3^{N-1}\) on any tree of order \(N\).

## Proof
**Exact specialization recurrence.** Fix an integer \(z\) and set, for \(s\ge1\) and \(j\in\{0,1,2,3\}\),
\[
w_s(j;z)=z^j\left(\sum_{h\ne j}z^h\right)^{s-1}.
\]
The exponent \(s-1\) accounts for the pendant leaves attached to a spine vertex of type \(s\). Conditional on its spine color \(j\), each leaf independently chooses any of the other three colors, so \(w_s\) is its exact chromatic-weight contribution.

For \(\alpha=(a,b,c,d)\), initialize \(u_j^{(1)}=w_a(j;z)\). For \(r=1,2,3\), with \(s_2=b,s_3=c,s_4=d\), update simultaneously by
\[
u_j^{(r+1)}=w_{s_{r+1}}(j;z)\left(\sum_{h=0}^3u_h^{(r)}-u_j^{(r)}\right).
\]
The subtraction forces adjacent spine colors to differ. Summing the four final states gives exactly \(P_{C_\alpha}(z)=\sum_{j=0}^3u_j^{(4)}\), without enumerating leaves individually. The recurrence consists entirely of additions, subtractions and multiplications, hence remains exact upon reduction modulo \(2^{64}\).

**Exhaustive finite certificate.** `verify.cpp` enumerates every quadruple of positive integers with the stated endpoint bounds and \(6\le a+b+c+d\le200\), retaining precisely those lexicographically no larger than their reversals. For every retained tuple, it uses the above four-state recurrence at \(z=2\) and \(z=3\) in unsigned 64-bit arithmetic, then inserts the ordered pair of residues into a map for that fixed order. An insertion fails precisely when an earlier tuple had the **same ordered pair** (map key equality, not merely a hash-bucket collision). The replayed executable reported no repeated keys for any order through \(200\).

For completeness, set \(a'=a-2,d'=d-2,b'=b-1,c'=c-1\). There are
\[
\binom{198}{4}=62{,}117{,}055
\]
ordered nonnegative quadruples of total at most \(194\). Exactly \(4{,}851\) of them are fixed by reversal; these have \(a=d\) and \(b=c\), with \(a+b\le100\). Burnside's two-element count therefore gives
\[
\frac{62{,}117{,}055+4{,}851}{2}=31{,}060{,}953
\]
canonical types, exactly the total reported by the executable. The source code contains complete loop bounds and arithmetic; no omitted or sampled cases enter this proof.

If two distinct types of the same order had identical fourth principal-specialization polynomials, their evaluations at \(2\) and \(3\), and therefore both residue coordinates, would agree. That contradicts the exhaustive injectivity check. This proves the finite theorem. The implication only uses the forward preservation of equality under evaluation, so modular reduction cannot produce a false assertion of separation.

## Verification
The standalone source `verify.cpp` was compiled using `g++ -std=c++17 -O3` and replayed with argument `200`. Its final stdout was:

```
RESULT N<=200 CLASSES=31060953 COLLISIONS=0
```

The program also reported intermediate zero-collision totals through each tenth order. It uses `uint64_t`, whose wraparound implements reduction modulo \(2^{64}\), and compares actual pairs for equality in `std::unordered_map`; no probabilistic collision assumption is used. The independently written `verify_small.py` computes the proper-coloring sum by explicit spine-color tuples and, for all types through order eight, by enumerating entire proper vertex colorings. It completed 40 exact checks and returned `INDEPENDENT_SMALL_OK 40`. The primary certificate, not the small checks, supplies exhaustive coverage of the stated finite domain.

Reproduction requires a C++17 compiler and Python 3. Run `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify 200` and `python3 verify_small.py`. No network access, external dataset, or numerical tolerance is required.

## Relationship to prior work
Bingham, Celano, Commins, Orellana, Pan, and Simone introduced \(\operatorname{ps}_4(Z_T(\mathbf x;t))\) and conjectured that it distinguishes all caterpillars. They also explicitly conjectured the weaker **ordinary** fourth specialization \(\operatorname{ps}_4(X_T)\) distinguishes all caterpillars (their Conjecture 6.2). Section 6 of their arXiv version 1 states computational verification for all caterpillars through order 25 and some families with five spine vertices at orders 30, 35, 40, 45 and 50. These established finite checks do not imply the present full four-spine range through order 200 or the two-residue injective witness.

A prior result concerning four-spine families with equal third \(t\)-chromatic specialization does not imply equality or inequality of their ordinary fourth specializations; different specialization degree and weighting prevent direct implication. The present claim is a new **finite** verification of the ordinary specialization, not an infinite proof of the stated conjecture, and not a claim that the four-spine formula is itself previously unknown.

## Limitations
Only four-spine caterpillars on at most 200 vertices are covered. The two residues are sufficient to distinguish objects in this finite domain but need not be complete invariants outside it; their arithmetic information is not a symbolic reconstruction of the full polynomial. The argument is computer-assisted and depends on the correctness of the supplied compiler and deterministic program, supported by independent small checks. It does not establish the authors' conjecture for all caterpillars or provide a general all-order reconstruction. Historical priority beyond the inspected and searched sources remains a residual uncertainty. No independent mathematical audit has been performed.

## References
1. A. Bingham, K. Celano, P. Commins, R. Orellana, J. Pan, and M. C. Simone, *Principal specializations of the t-chromatic symmetric function*, arXiv:2610.31785v1, first posted 2026-10-22, especially introduction, Section 3 and Section 6, Conjectures 6.1–6.2. https://arxiv.org/pdf/2610.31785v1
2. R. P. Stanley, *A symmetric function generalization of the chromatic polynomial of a graph*, Advances in Mathematics 111 (1995), 166–194. (Definition of the chromatic symmetric function.)
