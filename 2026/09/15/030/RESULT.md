# Universal conjugacy-class exponent 3 fails for PSp_6(q), q = 3 mod 4: the case q = 3

## Context

For a finite group G and a conjugacy class C, let e_G(C) = min{k >= 1 : 1 in C^k}
and e(G) = max_C e_G(C), the conjugacy-class exponent. A long-standing
question, sharpened by Bastos-Silveira-Schneider and by Garonzi-Montiijo-Zalesski,
asks which finite simple groups satisfy e(G) = 3. For symplectic groups
PSp(2n,q) with q not 3 mod 4, all classes are real and e(G) = 2; for q = 3 mod 4
the bound e(G) <= 6 holds for n > 4 and e(PSp_4(q)) = 3, while whether
e(PSp_6(q)) = 3 for 4 | (q+1) was explicitly left open.

## Definitions

Let G = PSp_6(3) = S_6(3), of order 4585351680 = 3^9 (3^2-1)(3^4-1)(3^6-1)/2,
with 74 conjugacy classes. For g in class C, the Frobenius class-multiplication
formula states that the number of triples (x,y,z) in C^3 with xyz = 1 equals
|C|^3/|G| * S(g), where S(g) = sum_{chi in Irr(G)} chi(g)^3/chi(1).
Hence 1 in C^3 if and only if S(g) != 0.

## Result

The universal claim that e(G) = 3 for all G = PSp_6(q) with q an odd prime
power, q = 3 mod 4, is FALSE. For q = 3, the group PSp_6(3) has conjugacy
classes C with 1 not in C^3, hence e(PSp_6(3)) >= 4. Concretely, with GAP
CTblLib/ATLAS numbering of the 74 classes: class 12 (element order 4,
centralizer order 2304, real) and classes 17, 18 (an inverse pair of elements
of order 6, centralizer order 15552) satisfy S(g) = 0 exactly. The other 71
classes have S(g) != 0. Therefore the cutoff e(G) = 3 fails universally.

## Proof / evidence

The ordinary character table of S_6(3) was reconstructed from the archived GAP
Character Table Library segment (74 centralizer orders; power maps for
2,3,5,7,13; 49 stored irreducible rows plus 25 [GALOIS,[a,2]] markers). Each
marker was verified to follow final-table character a directly, and the omitted
conjugate row was generated accordingly: complex conjugation for the E(3)
markers, and E(13)^k -> E(13)^{2k} for the E(13) quadratic-Gauss-period pair
72/73, whose values are the two residue/nonresidue period sums, real and
interchanged by squaring. All entries lie in Z[E(3),E(13)], embedded in
Q(zeta_39) via E(3) = zeta_39^13, E(13) = zeta_39^3. Each chi(g)^3/chi(1) was
expanded as an exact Fraction-coefficient polynomial in zeta_39 modulo
x^39-1, and S(g) = 0 was decided by the exact Galois-trace test: S(g) = 0 iff
Tr(S(g) zeta_39^j) = 0 for all j = 0..38, with Tr(zeta_39^e) =
mu(m) phi(39)/phi(m), m = 39/gcd(39,e). Classes 12, 17, 18 have all 39 traces
zero; every other class has nonzero trace t_0. Validation: column
orthogonality sum_chi |chi(g)|^2 = |C_G(g)| holds for all 74 classes (max
relative error 4.1e-16) and the row inner products form the identity matrix;
S(1) sanity gives t_0 = 24|G|; power maps confirm orders 4, 6, 6, reality of
class 12, and the 17/18 inverse pair; independent complex-float evaluation
gives |S| < 2e-14 for classes 12/17/18 versus |S| >= 0.217 elsewhere. By the
Frobenius formula, S(g) = 0 implies no triple in C^3 multiplies to 1.

## Limitations

This disproves the universal claim over all q = 3 mod 4 via the single case
q = 3. It does not determine e(PSp_6(q)) for q > 3, nor the exact value of
e(PSp_6(3)) beyond >= 4. Input character values are inherited from GAP
CTblLib/ATLAS data, self-consistency-verified here via both orthogonality
relations; the S(g) = 0 deductions use only exact rational arithmetic.

## Reproducibility

Run `python3 output/artifacts/certify_S63.py` (exact trace certificate; reads
copies of the segment/irr inputs in output/artifacts/) and
`python3 output/artifacts/verify_float.py` (independent float check). The exact
script takes a few minutes; the float script seconds. Full per-class trace
outcomes are in output/artifacts/S63_trace_results.json.

## References

- Garonzi, Montiijo, Zalesski, On the conjugacy class exponent of the
  nonabelian simple groups, arXiv:2506.22268v2.
- Guralnick, Malle, Tiep, Products of conjugacy classes in finite and
  algebraic simple groups, Adv. Math. 2013 (arXiv:1202.2627).
- GAP Character Table Library / ATLAS of Finite Groups, table S6(3)
  (ctosymp1.tbl origin); ATLAS online page for S6(3).
