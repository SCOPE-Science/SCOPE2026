# Three-shell Parseval sampling for the quadratic Walsh band: arithmetic classification and Pell nonuniqueness

## Finding

Fix an integer \(n\ge4\). Let \(\Omega_n=\{-1,1\}^n\), let \(\chi_I(x)=\prod_{i\in I}x_i\), and let
\[
\mathcal W_{\le2}=\operatorname{span}\{\chi_I: I\subseteq[n],\ |I|\le2\}.
\]
For an attainable coordinate sum \(s\in\{-n,-n+2,\dots,n\}\), write \(X_s=\{x:\sum_i x_i=s\}\). A three-shell sampling measure is a probability measure placing a strictly positive *total* weight \(w_s\) uniformly on each of exactly three distinct shells \(X_a,X_b,X_c\), with \(a<b<c\). We require the exact Parseval/orthonormality identity
\[
\sum_{s\in\{a,b,c\}}\frac{w_s}{|X_s|}
\sum_{x\in X_s}P(x)\overline{Q(x)}
=2^{-n}\sum_{x\in\Omega_n}P(x)\overline{Q(x)}
\quad(P,Q\in\mathcal W_{\le2}).
\tag{1}
\]

**Complete arithmetic classification.** Identity (1) holds if and only if the three attainable shell sums satisfy
\[
\boxed{ab+ac+bc=-(3n-2),\qquad abc=-n(a+b+c).}\tag{2}
\]
For every such triple the uniquely determined shell weights are
\[
\boxed{w_a=\frac{n+bc}{(a-b)(a-c)},\quad
w_b=\frac{n+ac}{(b-a)(b-c)},\quad
w_c=\frac{n+ab}{(c-a)(c-b)}.}\tag{3}
\]
Remarkably, **all three weights in (3) are automatically strictly positive**: no further inequalities are necessary. Two or fewer entire shells cannot satisfy (1). Thus three is the smallest possible number of complete shells in this quadratic-band setting whenever a design exists.

**Explicit exhaustive arithmetic decision procedure.** Loop once through each attainable \(a\). A valid triple must have \(a^2\ne n\) and
\[
u=-\frac{2a(n-1)}{a^2-n}\in\mathbb Z,\quad
v=-(3n-2)-au,\quad \Delta=u^2-4v>0.
\tag{4}
\]
It occurs precisely when \(\Delta\) is a perfect square and the integers
\[
b=\frac{u-\sqrt\Delta}{2},\qquad c=\frac{u+\sqrt\Delta}{2}
\]
are attainable shell sums with \(a<b<c\). This enumerates *every* admissible triple without repetition in \(n+1\) candidate evaluations (not counting integer-arithmetic bit complexity). Simultaneous negation of all three shell sums is cube inversion.

**Two structural families and the first multiplicity transition.** A valid triple containing either cube pole \(\pm n\) exists exactly in dimensions \(n=r^2+1\) with integer \(r\ge2\). Up to cube inversion it is
\[
(a,b,c)=(-n,1-r,1+r),\qquad
(w_a,w_b,w_c)=\left(\frac{2}{n^2+n+2},\frac{n}{2(n+1-r)},\frac{n}{2(n+1+r)}\right).
\tag{5}
\]
A symmetric triple \((-2r,0,2r)\) exists exactly when \(r\ge2\), \(3\nmid r\), and \(n=(4r^2+2)/3\). An additional non-polar family, for even \(s\ge8\) with \(3\nmid s\), has
\[
n=(s^2-1)/3,\qquad(a,b,c)=(-s-1,-1,s-1).
\tag{6}
\]
The **first** dimension with two inequivalent triple designs under cube inversion is \(n=65\): their shell sums are
\[
(-65,-7,9)\quad\text{and}\quad(-15,-1,13),
\]
with respective weights \((1/2146,65/116,65/148)\) and \((13/98,65/98,10/49)\). Exact exhaustive integer arithmetic from (4) proves that no dimension \(4\le n\le64\) has two inversion-inequivalent admissible triples. More strongly, **infinitely many dimensions have both inequivalent types**: start \((s,r)=(14,8)\) and iterate
\[
(s',r')=(2s+3r,s+2r).
\tag{7}
\]
Then \(s^2-3r^2=4\), \(n=r^2+1=(s^2-1)/3\), and (5) and (6) give distinct positive three-shell designs in every resulting dimension \(65,901,12545,174725,\ldots\).

## Assumptions and scope

All claims concern integer \(n\ge4\), complex-valued Walsh polynomials of degree at most two, and **permutation-invariant probability measures supported on unions of complete Hamming shells**. A shell with sum \(s\) consists of \(\binom n{(n-s)/2}\) vertices, so its individual-vertex mass is \(w_s/\binom n{(n-s)/2}\). The shell weights are real, strictly positive, and sum to one. Equality (1) is an identity for all polynomial pairs and is stronger than injective restriction. It does not assert minimum vertex count, minimum number of points among arbitrary nonuniform samplers, or a unique design in every dimension. The index \(r\) in (5) and in the symmetric family is a positive integer, whereas \(s\) in (6) is an even positive integer.

## Proof

**1. Reduction to four unbiased moments.** The products of two basis Walsh characters obey \(\chi_I\overline{\chi_J}=\chi_{I\triangle J}\). For \(|I|,|J|\le2\), their symmetric differences realize exactly every subset size \(0,1,2,3,4\), as \(n\ge4\). By permutation invariance, the average of each character of degree \(t\) depends only on \(t\). The degree-\(t\) elementary Walsh sum \(\sum_{|I|=t}\chi_I(x)\), evaluated at a point with coordinate sum \(S=\sum_i x_i\), is the degree-\(t\) Krawtchouk polynomial in \(S\); its leading coefficient is \(1/t!\), and the change of basis between these four sums and \(1,S,S^2,S^3,S^4\) is triangular and invertible. Thus (1) is equivalent to equality of the first four moments of \(S\) under the three-shell measure with those under uniform cube measure. Since independent fair signs satisfy
\[
\mathbb E S=0,\quad\mathbb E S^2=n,\quad
\mathbb E S^3=0,\quad\mathbb E S^4=3n^2-2n,\tag{8}
\]
(1) is equivalent to a positive degree-four quadrature supported on the three values \(a,b,c\), for the symmetric binomial law of \(S\).

**2. All three-node degree-four quadratures.** Put \(\mu\) for the full-cube law of \(S\), and \(Q(T)=(T-a)(T-b)(T-c)=T^3-\sigma_1T^2+\sigma_2T-\sigma_3\). A three-node interpolation rule \(\sum_jw_jf(a_j)=\int f\,d\mu\), with its weights exact on degrees at most two, is exact through degree four if and only if
\[
\int Q(T)\,d\mu=\int TQ(T)\,d\mu=0.
\tag{9}
\]
Indeed, every polynomial of degree at most four divides uniquely as \(Q(T)L(T)+R(T)\), \(\deg L\le1\), \(\deg R\le2\); the remainder is interpolated exactly at the three nodes. Substitution of (8) into (9) yields \(-n\sigma_1-\sigma_3=0\) and \(3n^2-2n+n\sigma_2=0\), which are exactly (2). Each weight is the expectation of its quadratic Lagrange interpolation basis polynomial, giving (3), and hence uniqueness.

**3. Automatic strict positivity and the three-shell lower bound.** Let \(L_j(T)=\prod_{i\ne j}(T-a_i)/(a_j-a_i)\) be a degree-two cardinal polynomial for any distinct admissible nodes. Exactness through degree four gives
\[
w_j=\sum_iw_iL_j(a_i)^2=\int L_j(T)^2\,d\mu(T)>0.
\]
The strict inequality follows because the full binomial law has \(n+1\ge5\) distinct atoms with positive masses, whereas \(L_j\) is a nonzero quadratic and cannot vanish on all these atoms. Analogously, the \(3\times3\) moment Gram matrix of \(1,T,T^2\) is strictly positive definite under \(\mu\). A quadrature supported on at most two nodes has moment Gram rank at most two, a contradiction. This proves the three-shell minimum in the asserted class.

**4. Complete effective enumeration.** Set \(u=b+c\), \(v=bc\). The two equations (2) become \(au+v=-(3n-2)\) and \(av=-n(a+u)\). Eliminating \(v\) gives \((a^2-n)u=-2a(n-1)\), so \(a^2=n\) would imply \(a(n-1)=0\), impossible for \(n\ge4\) and \(a^2=n>0\). Consequently (4) is necessary. The roots \(b,c\) of \(T^2-uT+v\) must be the displayed discriminant roots, and the order, parity, integrality and bound tests in (4) are precisely the conditions for an attainable strictly ordered triple. They are also sufficient by the elimination and steps 1–3. Therefore looping over the \(n+1\) attainable first nodes is exhaustive, with no unverified infinite-domain enumeration.

**5. Pole, symmetry, and interior families.** For the negative pole \(a=-n\), equations (2) force \(b+c=2\), \(bc=2-n\), so \(b,c=1\pm\sqrt{n-1}\). Attainability and distinctness are equivalent to \(n=r^2+1\), integer \(r\ge2\); (3) simplifies to (5). Positive-pole solutions are exactly their reflected triples. A symmetric triple \((-d,0,d)\) forces \(d^2=3n-2\); parity of the shell sums requires even \(d=2r\), and integrality of \(n=(4r^2+2)/3\) is equivalent to \(3\nmid r\). Conversely these parameters produce valid shell sums for every \(r\ge2\). For (6), substituting \((-s-1,-1,s-1)\) gives \(\sigma_1=-3\), \(\sigma_2=3-s^2=-(3n-2)\), and \(\sigma_3=s^2-1=3n=-n\sigma_1\). Even \(s\ge8\) not divisible by three makes \(n\) a positive odd integer and all three nodes interior attainable values. Positivity follows from step 3.

**6. First multiple orbit and infinite coexistence.** The executable exact-integer checker `verify.py` implements (4) and, independently, a pair-node enumeration using \(c=-n(a+b)/(ab+n)\), with explicit handling of zero denominators. It compares *all* outputs for every \(4\le n\le250\), validates (2), exact weights and degree-four moments, and checks that every \(4\le n\le64\) yields no more than one pair of inverse triples; at \(n=65\) it finds precisely the two inverse pairs displayed above. The dimensions admitting triples among \(4\le n\le64\) are exactly \(5,6,10,17,21,22,26,33,34,37,50\), with at most one inversion-orbit in each. The pair-node procedure handles its potential zero denominator without dropping solutions: if \(ab+n=0\) and \(a+b=0\), then \(a^2=n\) and the second equation in (2) would force \(n=1\), contradicting \(n\ge4\). This is a finite exhaustive certificate for the first transition, grounded in the proved necessary-and-sufficient integer decision procedure; it makes no infinite inference from finite samples. Finally (7) preserves \(s^2-3r^2=4\) because \((2s+3r)^2-3(s+2r)^2=s^2-3r^2\), preserves evenness of \(s,r\), and preserves \(3\nmid s\); both coordinates increase strictly from \((14,8)\). Hence the pole triple and non-polar triple remain simultaneously available in infinitely many dimensions. They cannot be related by inversion because inversion preserves whether a support contains a pole.

## Verification

Execute `python3 verify.py` in any standard Python 3 interpreter. The included `verify_output.txt` is the observed output. The verifier compares two logically distinct exact-integer enumerations of admissible triples in every dimension \(4\le n\le250\); checks every resulting weight using rational arithmetic, moment equations, and all Walsh degrees one through four; independently compares \(740\) explicit Walsh Gram entries in dimensions five and six; verifies the finite \(n\le64\) uniqueness-orbit claim; and evaluates the infinite-family formulas over large finite parameter samples and the first twenty Pell iterates. It reports `VERIFY_OK`. The proofs for arbitrary \(n\) are steps 1–5 and the algebraic Pell invariance in step 6, not a claimed extrapolation from these tests.

## Relationship to prior work

Bannai, Bannai, Tanaka, and Zhu (arXiv:2006.02054v1, first public 2020-06-03) develop weighted relative designs on **two shells**, with tightness and Hahn/Hermite polynomial constraints. Their studied combinatorial structure motivates the present complete-shell Fourier sampling question, but their inspected introductory statements and principal results do not give positive **three-complete-shell** degree-four cubature, the arithmetic parameter classification (2)–(4), or Pell nonuniqueness. Gavrilyuk, Suda, and Vidali (arXiv:1809.07553v1, 2018) study **unweighted tight** orthogonal arrays of strength four, not per-shell positive probability weights over three complete shells. Carlet, Kiss, and Nagy (2022) likewise address unweighted binary orthogonal arrays and their simplicity.

A related published result, *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells* (published-finding corpus, 2026-10-11), provides the full spectrum and exceptional eigenvalue coincidences for **one** interior Hamming shell. Its resonances at dimensions \(n=r^2+1\) are mathematically relevant, and are not claimed anew. A single-shell Gram-spectrum theorem, however, neither establishes a three-shell weighted Parseval identity nor implies the integer three-node quadrature classification or its first multi-orbit/Pell coexistence assertions without additional arguments. An earlier two-shell theorem for the **linear** Walsh band does not imply the quadratic-band fourth-moment conditions, and is not asserted here. General three-node moment quadrature and Lagrange interpolation are classical tools and are explicitly treated as antecedents, not original discoveries; the distinct results here are the complete integer-shell classification, positivity, and arithmetically sharp multiplicity phenomenon.

## Limitations

The classification pertains only to sampling measures uniform within each of exactly three *complete* Hamming layers on the binary cube, not to arbitrary weighted subsets, four or more shells, or higher polynomial bands. The node criterion is an algorithmic classification for all dimensions; it does not assert a simple closed congruence characterization of every dimension admitting a design. The minimal number of *shells* does not establish minimum number of *sampled vertices*. The first nonuniqueness threshold relies on a self-contained exhaustive integer enumeration of a finite range with independently checked elimination formulas; it is not established solely by a short symbolic exclusion theorem. The overlap assessment is best-knowledge, and an older differently indexed equivalent three-shell binomial cubature enumeration could exist. This result has no independent external audit.

## References

1. E. Bannai, E. Bannai, H. Tanaka, and Y. Zhu, *Tight relative t-designs on two shells in hypercubes, and Hahn and Hermite polynomials*, arXiv:2006.02054v1 (2020-06-03), https://arxiv.org/abs/2006.02054.
2. A. L. Gavrilyuk, S. Suda, and J. Vidali, *On tight 4-designs in Hamming association schemes*, arXiv:1809.07553v1 (2018-09-20), https://arxiv.org/abs/1809.07553.
3. C. Carlet, G. Kiss, and G. P. Nagy, *Simplicity conditions for binary orthogonal arrays*, Designs, Codes and Cryptography (2022), https://doi.org/10.1007/s10623-022-01105-4.
4. *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, published mathematical result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95.
