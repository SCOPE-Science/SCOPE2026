# Thirty-five four-round theories of prime cyclic addition structures

## Finding
For each prime \(p\), let \(C_p\) have universe \(\mathbb Z/p\mathbb Z\), a named constant \(0\), and a ternary relation \(R(a,b,c)\) holding just when \(a+b=c\). Write \(C_p\equiv_4 C_q\) when the structures satisfy the same first-order sentences of quantifier rank at most four. Define
\[
E=\{p\text{ prime}:p\le131\}\cup\{157,191\}.
\]
Then for all primes \(p,q\),
\[
C_p\equiv_4 C_q\quad\Longleftrightarrow\quad
(p=q\in E)\ \lor\ (p,q\notin E).
\]
There are exactly **35** four-round theories: 34 singleton classes and one infinite class. The infinite class starts at prime \(137\), skips \(157\) and \(191\), and contains every prime at least \(193\). The smallest representatives are the 34 members of \(E\) and \(137\). The optimal maximum cardinality of a smallest representative is \(191\).

## Assumptions and scope
The statement concerns **prime-order** cyclic additive groups in the finite **relational** language \(\{0,R\}\). Equality is available. No binary function symbol for addition and no order relation are present. Quantifier rank is standard nesting depth, with arbitrary Boolean operations and quantifier alternations. It is not a result about composite groups or about functional group language, where terms carry additional information at rank zero.

## Proof
**Exact finite-type recursion.** Let \(\operatorname{At}_p(\bar a)\) be the complete atomic diagram of an ordered tuple, recording equalities, named zero, and all triples satisfying \(R\) among tuple coordinates. Define recursively
\[
T_{p,0}(\bar a)=\operatorname{At}_p(\bar a),\qquad
T_{p,s+1}(\bar a)=\big(\operatorname{At}_p(\bar a),
\{T_{p,s}(\bar a,b):b\in C_p\}\big).
\]
Induction on \(s\) shows that equal types across structures are exactly equivalence for all formulas of rank at most \(s\) with the displayed free variables. This is also the usual back-and-forth/Ehrenfeucht–Fraïssé characterization. The sets are sets, not multisets, because first-order quantifiers do not count multiplicities of indistinguishable extensions without additional variables. Multiplication of all tuple entries by a nonzero scalar is an automorphism of \(C_p\), so the verifier computes each orbit only once. It evaluates \(T_{p,4}(())\) exactly.

**Fourth-move candidates.** For a triple \((a,b,c)\) over any odd prime field, every atomic relation involving a new element \(z\) either imposes no condition on \(z\) or fixes it to one of the values in
\[
F(a,b,c)=\{0,a,b,c\}\cup\{u+v,u-v:u,v\in\{a,b,c\}\}
\cup\{u/2:u\in\{a,b,c\}\}.
\]
As formal rational linear forms this set has 19 members. If \(z\) avoids them all, its atomic extension diagram is the generic diagram determined by the original triple. Thus the 1-type of a triple is determined by its original atomic diagram and the collision pattern of those 19 forms, together with the existence of a generic fourth element. For every prime \(p\ge193\), such a generic element exists.

**Rational arrangement bound.** Differences of the 19 formal forms, reduced to primitive integer coefficient vectors, yield exactly 60 distinct central hyperplanes in the three selected coordinates. After normalizing a nonzero first coordinate and writing the second selected coordinate as \(r\), 46 distinct affine-linear rational functions \(z=h(r)\) describe the possible special third coordinates; hyperplanes independent of \(z\) give exceptional values of \(r\). Adding every pairwise intersection of these functions produces exactly 93 exceptional rational slopes, all enumerated by the accompanying verification script using exact rational arithmetic.

The prime divisors of nonzero cross-determinants of distinct exceptional slopes are precisely
\[
\{p\text{ prime}:p\le131\}\cup\{157,191\}.
\]
All rational denominators used in the construction have prime factors among the small listed primes. Consequently, for primes \(p\ge193\), all 93 exceptional slopes remain distinct modulo \(p\), all 46 special third-coordinate functions have the same collision structure at corresponding slopes, and the same is true for the 19 fourth-coordinate forms. The generic second-coordinate choice exists because \(p>93\); the generic third-coordinate choice exists because \(p>46\); the generic fourth-coordinate choice exists because \(p>19\).

**Uniform four-move strategy.** Across any two primes at least \(193\), Duplicator first matches zero/nonzero status. For the second selection, normalize a nonzero coordinate to 1, and match its ratio either with the corresponding exceptional rational slope or with another generic slope. When the first coordinate is zero, permute coordinates to normalize the nonzero one; if both are zero, the analogous repeated-zero cases are immediate. At the third selection, match the corresponding special \(h(r)\) class or choose a generic coordinate. The arrangement analysis ensures the two triples have identical collision diagrams for \(F\). At the fourth selection, match its \(F\)-class, or use a generic value. Hence every atomic relation is preserved and Duplicator wins. Therefore \(C_p\equiv_4 C_q\) whenever \(p,q\ge193\).

**Finite boundary and sharpness.** The exact recursion was evaluated for every prime through \(193\) with orbit normalization and for additional primes \(197\) and \(211\). Its 35 distinct root types place every prime in \(E\) alone and all other tested primes in one class. This exhausts the finite boundary because the uniform argument already covers all primes at least \(193\). In particular, the primes \(157\) and \(191\) have exceptional two-parameter rank-two extension profiles, whereas \(137\) and \(193\) agree. Each distinct root type is separated by some rank-four sentence by the type recursion. The largest least representative is \(191\), proving sharpness.

## Verification
Run `python3 verify_rank4_cyclic.py` with Python 3.9 or later. The program uses only the standard library. It enumerates complete atomic diagrams, computes quantifier types by exact set recursion, validates the 19/60/46/93 rational arrangement counts and the complete exceptional-prime list, and checks the finite class partition. An independently structured, orbit-free enumeration checks primes \(2,3,5,7,11,13\). All calculations use integer modular arithmetic or exact fractions; no floating-point approximations enter the theorem. The full finite type calculation can be executed in stages when individual runtimes are restricted; the supplied program performs the checks together.

## Relationship to prior work
Gomaa (2007, Chapter 3, especially Section 3.4 and Theorem 3.3) and Gomaa (2010) establish logarithmic upper/lower depth claims for identifying finite abelian and prime cyclic groups. The new theorem supplies an exact **rank-four partition** of all prime orders, rather than asymptotic bounds. In particular, its separating type for orders \(157\) and \(193\) conflicts with the claimed general lower bound of Gomaa's Theorem 3.3. The latter proof reduces a winning strategy to a single fixed closed binder; the exact rank-four back-and-forth calculation allows an alternating strategy that distinguishes the availability of extension-pattern families without any fixed short binder. This is a substantive conflict requiring independent review, not an invocation of the older lower bound as corroboration. Earlier work gives an exact rank-three partition; it does not imply the rank-four partition. Published work improving addition-chain bounds is concerned with upper bounds, not with the exact classification given here.

## Limitations
The finite cutoff depends on the relational signature; no claim is made for a functional addition symbol or for composite orders. The proof of the infinite tail relies on the stated finite rational-arrangement enumeration; its standalone generator is essential evidence and should be rerun before independent adoption. The finite boundary classification uses exhaustive finite arithmetic, not manually printed separating formulas. The claim conflicts with a published lower bound, so an independent audit focused on the rank-four characteristic types and the claimed binder reduction is especially important. No independent mathematical audit has been performed.

## References
1. Walid Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland, publicly deposited 2007-07-06. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 ; see Chapter 3, Section 3.4, pp. 60–75.
2. Walid Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116. https://doi.org/10.1142/S0218196710006047 .
3. O. Pikhurko and O. Verbitsky, graph logical-complexity survey, 2010; general EF-game background. See also L. Libkin, *Elements of Finite Model Theory* (2004).
