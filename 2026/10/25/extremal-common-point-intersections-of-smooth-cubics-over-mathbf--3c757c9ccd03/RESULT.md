# Extremal common-point intersections of smooth cubics over \(\mathbf F_2\)

## Finding
Let \(C,D\subset\mathbf P^2_{\mathbf F_2}\) be **distinct geometrically smooth plane cubic curves**. They share at most five rational points. Equality holds for precisely \(21\) unordered pairs of cubic equations in fixed coordinates. These pairs constitute one orbit under \(\operatorname{PGL}_3(\mathbf F_2)\), whose order is \(168\), with stabilizer order \(8\). Every five-element subset of the seven rational plane points occurs as the common rational point set of exactly one extremal pair.

For every extremal pair, the complete scheme-theoretic intersection has support at **exactly the same five rational points**, and its local intersection multiplicities are \((5,1,1,1,1)\). The multiplicity-five point is the unique third point on the rational line joining the two rational plane points *omitted* by the pair's common point set. The three members of the rational pencil spanned by the cubic forms are the two smooth curves and a reducible cubic comprising the three rational lines concurrent at that distinguished point.

More generally, among \(336\) geometrically smooth plane cubic equations in fixed coordinates, the exact number of unordered pairs with \(k\) common rational points is
\[
(N_0,N_1,N_2,N_3,N_4,N_5)=(12740,22575,14448,5488,1008,21).
\]
These sum to \(56280=\binom{336}{2}\); no smooth pair has more than five rational common points.

## Assumptions and scope
The base field is \(\mathbf F_2\). Smooth means smooth after base change to an algebraic closure, not merely absence of singular rational points. A cubic equation means a nonzero degree-three homogeneous polynomial; because \(\mathbf F_2^*=\{1\}\), distinct equations are distinct cubic curves. All pair counts are unordered and exclude coincident cubics. Scheme intersection length is measured over the algebraic closure. No assertion concerns pairs with a singular member or fields other than \(\mathbf F_2\).

For explicit calculations write \([x:y:z]\) for homogeneous coordinates and order the cubic monomials as
\[
(x^3,y^3,z^3,x^2y,x^2z,xy^2,y^2z,xz^2,yz^2,xyz).
\]
The integer coefficient encoding records these ten coefficients as bits in the displayed order, from least significant to most significant.

## Proof
**Step 1: Upper bound.** Any smooth plane cubic has genus one, so the Hasse--Weil bound gives \(\#C(\mathbf F_2)\le\lfloor 3+2\sqrt2\rfloor=5\). Hence two distinct smooth cubics have at most five common rational points.

**Step 2: Transitive normal form for five-point subsets.** Every five-element subset \(S\) of the seven-point Fano plane is the complement of an unordered pair of distinct rational points. The group \(\operatorname{PGL}_3(\mathbf F_2)=\operatorname{GL}_3(\mathbf F_2)\) acts transitively on pairs of distinct points. Thus it is enough to study the complement of \([0:0:1]\) and \([0:1:1]\), namely
\[
S=\{[1:0:0],[0:1:0],[1:1:0],[1:0:1],[1:1:1]\}.
\]
Solving the five independent binary evaluation equations on the ten cubic coefficients yields a five-dimensional vector space, consisting of exactly \(32\) forms (including zero). The exact rank test in `verify_rank.py` and the independent projective-chart Gröbner test in `verify_groebner.py` both find exactly two geometrically smooth forms among these \(32\):
\[
\begin{aligned}
f&=x^2y+x^2z+xy^2+z^3,\\
g&=x^2y+xy^2+xz^2+z^3.
\end{aligned}
\]
The two coefficient encodings are \(60\) and \(172\). This enumeration is exhaustive; it does not assume geometric smoothness from rational-point tests. For these representatives, direct differentiation provides an additional symbolic proof:
\[
\nabla f=(y^2,x^2,x^2+z^2),\qquad
\nabla g=(y^2+z^2,x^2,z^2).
\]
Neither gradient vanishes at any geometric projective point. In characteristic two, Euler's identity for a cubic implies a geometric singularity is equivalent to the common vanishing of its three partial derivatives.

Because each five-point subset is projectively equivalent to \(S\), exactly one unordered pair of smooth cubics passes through each subset. A pair with five common points is counted for only its own common set. Therefore exactly \(\binom75=21\) extremal unordered pairs exist, and they form one projective orbit with stabilizer order \(168/21=8\).

**Step 3: Pencil and scheme-theoretic intersection.** For the displayed normal form, the third binary pencil member is
\[
f+g=xz(x+z),
\]
the product of three different rational lines meeting at \(p=[0:1:0]\). The restrictions of \(f\) to these lines are
\[
f|_{x=0}=z^3,\qquad f|_{z=0}=xy(x+y),\qquad f|_{x=z}=xy(x+y).
\]
The first line intersects \(C\) only at \(p\), with multiplicity three; each other line meets \(C\) at \(p\) simply and at two further rational points simply. Thus the divisor of the factorized section \(f+g\) on the smooth cubic \(C\) has multiplicity five at \(p\), and multiplicity one at the other four points in \(S\). Since \((f,g)=(f,f+g)\) as ideals, this is exactly the scheme-theoretic complete intersection of \(C\) and \(D\). Its length \(5+1+1+1+1=9\) agrees with Bézout and leaves no additional geometric intersection point. The omitted points lie on \(x=0\) together with \(p\), proving the distinguished-point description. The transitivity established in Step 2 transfers these assertions to all \(21\) extremal pairs.

**Step 4: The complete pair incidence distribution.** For each nonzero ternary cubic coefficient vector, `verify_rank.py` constructs its gradient quadrics and computes the rank of their degree-four multiples. Three homogeneous quadrics have no common geometric projective zero exactly when they form a homogeneous regular sequence; in that case the quotient's Hilbert series is \((1+t)^3\), so its degree-four component vanishes. Conversely, vanishing of the degree-four component implies that all higher components vanish and the gradient ideal has no geometric projective zero. Thus rank \(15\) of the degree-four component is an exact geometric smoothness criterion. Among \(1023\) nonzero forms exactly \(336\) pass. Evaluating these at all seven rational points and comparing the \(\binom{336}{2}=56280\) unordered masks gives the stated six frequencies.

The independent `verify_groebner.py` checks geometric smoothness via Gröbner bases after dehomogenizing each partial derivative in each of the three standard projective charts, and reconstructs the pair histogram from binomial incidence moments \(B_j=\sum_{|T|=j}\binom{n(T)}2\), where \(n(T)\) counts smooth cubics through rational point subset \(T\). Inversion of \(B_j=\sum_{k\ge j}\binom{k}{j}N_k\) yields the same histogram without enumerating cubic pairs directly.

## Verification
Run `python3 verify_rank.py` using Python 3's standard library; run `python3 verify_groebner.py` with SymPy installed. Both scripts assert every claimed census count, the two smooth representatives through \(S\), and the total number of pairs; each terminates with `VERIFY_OK`. Expected machine-readable diagnostics are given in `reference_output.txt`. The scheme multiplicity profile and geometric singularity claims additionally follow by the explicit factorizations and derivatives in Step 3 and Step 2, rather than a finite-field sampling assumption.

## Relationship to prior work
Kaplan--Matei, *Counting Plane Cubic Curves over Finite Fields with a Prescribed Number of Rational Intersection Points* (arXiv:2003.13944), treats the general question of cubic-pair rational intersections. Its main Theorem 1 assumes the field size is strictly greater than two and does not impose smoothness on both cubics. This result concerns the excluded smallest field, imposes geometric smoothness on both, and determines a local scheme intersection multiplicity and the projective pencil orbit; it is not a specialization of that theorem. Asgarli--Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169), investigates pencils all of whose rational members are smooth; the extremal pencil here has a **reducible** third rational member and is not in their all-smooth class. Earlier classifications of individual smooth binary cubics do not alone imply the two-cubic intersection and multiplicity classification.

## Limitations
The exact findings are confined to \(\mathbf F_2\) and distinct geometrically smooth plane cubics. Prior published tables or computations of binary cubic configurations not indexed by the consulted searches might contain an equivalent orbit description; publication priority therefore remains conditional on broader human literature review. No independent audit has been performed. The executable census is exact, but the general mathematical arguments establishing transitivity and local multiplicities remain integral parts of the proof; neither program claims an infinite-field classification.

## References
1. N. Kaplan and V. Matei, *Counting Plane Cubic Curves over Finite Fields with a Prescribed Number of Rational Intersection Points*, arXiv:2003.13944 (first public 2020-03-31), https://arxiv.org/abs/2003.13944.
2. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (first public 2022-03-14), https://arxiv.org/abs/2203.07169.
