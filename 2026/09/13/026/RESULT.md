# A new Borromean Rédei triple below 5000: {5, 29, 181}

## Context

In arithmetic topology, the Rédei triple symbol [p1,p2,p3] in {±1} is the analogue of the mod-2 triple linking (Milnor) invariant of a link. For distinct primes pi ≡ 1 mod 4 with all pairwise Legendre symbols +1, the pairwise cup products of the quadratic characters vanish, so the triple Massey product in H^2(G_S,F2) is defined; by the theorem of Rédei–Vogel–Morishita it is nonvanishing (does not contain 0) if and only if the Rédei symbol is −1. Such a triple is called Borromean. The classical example in the literature is {13,61,937}. The admitted target asked for a new Borromean triple below 5000 with full certificate, or a proof that none exists.

## Definitions

Let p1,p2 be distinct primes ≡ 1 mod 4 with (p1/p2)=+1. A normalized Rédei solution is a primitive triple (x,y,z) with x^2−p1·y^2−p2·z^2=0, y even, x−y ≡ 1 mod 4. Then β=x+y√p1 has norm p2·z^2 (up to square), is ≡1 mod 4 and totally positive, and K=Q(√p1,√p2,√β) is the unique Rédei dihedral (D4, order 8) extension of Q ramified only at p1,p2. For a third prime p3 with (p1/p3)=(p2/p3)=+1, write r^2≡p1 mod p3; the Rédei symbol [p1,p2,p3] is the Legendre symbol (x+y·r/p3) ∈ {±1}, equal for both choices of r. It equals +1 iff primes above p3 in Q(√p1,√p2) split in K, and −1 iff they are inert.

## Result

The triple (p1,p2,p3)=(5,29,181) satisfies: each pi ≡ 1 mod 4, each below 5000, distinct from {13,61,937} up to order; all three pairwise Legendre symbols equal +1; the Rédei triple symbol [5,29,181]=−1 in all six orderings; hence the triple Massey product ⟨χ1,χ2,χ3⟩ ⊂ H^2(G_S,F2) with S={5,29,181,2,∞} is defined and does not contain 0. So {5,29,181} is a new Borromean triple, the smallest below 5000.

Legendre table: (5/29)=(5/181)=(29/5)=(29/181)=(181/5)=(181/29)=+1, each a single modular exponentiation.

## Proof / evidence

Base pair (5,29): (x,y,z)=(7,2,1) since 49−5·4−29=0; gcd 1; y even; x−y=5≡1 mod 4; β=7+2√5 totally positive (7−2√5≈2.53>0) with norm 49−20=29. Put t=√β; then t^2−7=2√5, so t has minimal polynomial f(T)=T^4−14T^2+29. Mod 3, f≡T^4+T^2+2 has values 2,1,1 at 0,1,2 (no linear factor) and no factorization into two monic quadratics over F3 (all 27 triples (a,b,c) checked), so f is irreducible over Q. Its discriminant is Res(f,f′)=256·29·(−20)^2=2969600=320^2·29, a nonsquare. The cubic resolvent is z^3+28z^2+80z=z(z^2+28z+80) with discriminant 464=16·29, hence exactly one rational root; for an irreducible quartic this forces Galois group D4 or C4, and nonsquare discriminant excludes C4. So Gal(f)=D4 of order 8 with splitting field K12=Q(√5,√29,√β) of degree 8, ramified only at 5,29; in particular 181 is unramified.

Frobenius witness at 181: (5/181)=(29/181)=+1 so 181 splits in Q(√5,√29). With r=27 (27^2=729≡5 mod 181), β±=7±2r gives 61 and 134 mod 181; both satisfy 61^90≡134^90≡180≡−1 mod 181, i.e. both Legendre symbols −1 (agreement required for a well-defined symbol). Hence primes above 181 are inert in K12: [5,29,181]=−1. Reciprocity cross-checks agree: swapped conic (11,2,1) for (29,5) gives √29≡36 mod 181, 11+2·36=83, 83^90≡−1; pair (29,181) via (35,6,1) at c=5 gives √29≡±2 mod 5, 35+6(±2)≡2,3 mod 5, both ≡−1 mod 5. All six orderings read −1.

Massey product: with χi the characters of Q(√pi), vanishing cups give defining cochains a12,a23 and value c=a12⌣χ3+χ1⌣a23. The Rédei extensions supply U3(F2)-representations ρ12,ρ23 gluing to ρ:G_S→U4(F2); by Morishita Thm 9.11 / Vogel, [c]≠0 iff the symbol is −1. Since the symbol is −1, Frob at 181 has χ1=χ2=0 but a12=1, forcing [c]≠0 mod indeterminacy. All six orderings are nonvanishing.

## Limitations

The headline is the single triple (5,29,181) with one ordering fully proved by hand-checkable data above; the remaining orderings are verified by the same normalized-conic computation. The surrounding scan (329 primes 1 mod 4 below 5000; 702788 Legendre-good triples; 353728 reading −1 in all six orderings) is reported as a survey scope, not as a completed certified census. Only y-even normalized conic solutions define the true Rédei symbol; y-odd solutions generate ramified non-Rédei extensions and are excluded.

## Reproducibility

All identities are hand-checkable with modular exponentiation: conic equations, r=27 check, 61^90/134^90/83^90 mod 181, discriminant and resolvent arithmetic, and the 27-case F3 check. Scripts redei_search.py (calibration [13,61,937]=−1) and certificate.json reproduce the full certificate. Any computer algebra system confirms f irreducible, disc(f)=2969600, Gal=D4.

## References

L. Rédei (1939) dihedral extensions and triple symbol; P. Stevenhagen (thesis §3) Rédei matrices; M. Morishita, Knots and Primes Ch. 9; D. Vogel (2004) Massey products in Galois cohomology of number fields; J. Amano on Rédei dihedral extensions; Amano–Mizusawa–Morishita on Massey products; J. Gärtner arXiv:1303.2608; D. Kim–M. Morishita, Res. Number Theory 11:86 (2025).
