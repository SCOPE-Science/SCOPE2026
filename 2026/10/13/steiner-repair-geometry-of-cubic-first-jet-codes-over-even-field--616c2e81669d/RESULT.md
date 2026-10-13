# Steiner repair geometry of cubic first-jet codes over even fields

## Finding

Let \(m\ge 2\), \(q=2^m\), and \(F=\mathbb F_q\). For every \(a\in F\), record two separate coordinates \(V_a(f)=v_af(a)\) and \(D_a(f)=w_af^{[1]}(a)\), where \(v_a,w_a\in F^\times\), \(f\in F[X]\) has degree at most three, and \(f^{[1]}\) is its first Hasse derivative. The resulting \(F\)-linear code \(C\subset F^{2q}\) has dimension four.

Its inclusion-minimal dependent coordinate sets (equivalently, supports of minimal dual codewords) of cardinality at most four are **exactly**:

1. The triples \(\{D_a,D_b,D_c\}\) for three pairwise distinct field elements.
2. The quadruples \(\{V_a,V_b,V_c,D_d\}\) for pairwise distinct \(a,b,c\) and the unique \(d\in F\) satisfying
   \[d^2=ab+ac+bc.\]

There are \(\binom{q}{3}\) sets of each type and no minimal dependent sets of size one or two. For any fixed \(d\), the \((q-1)(q-2)/6\) triples \(\{a,b,c\}\) giving a quadruple through \(D_d\) form, under \(a\mapsto(a-d)^{-1}\), precisely the lines of the projective Steiner triple system \(\operatorname{PG}(m-1,2)\) on \(F^\times\).

Consequently, every derivative coordinate has exactly \(\binom{q-1}{2}\) minimal **two-helper** repair sets (other derivative coordinates) and \((q-1)(q-2)/6\) minimal three-helper sets composed entirely of value coordinates. Every value coordinate has exactly \(\binom{q-1}{2}\) minimal **three-helper** repair sets, each comprising two other value coordinates and one derivative coordinate. Derivative coordinates have locality two and value coordinates locality three.

More strongly, counting all possible linear repair sets, of **arbitrary cardinality**, the maximum number of pairwise disjoint repair sets for any value coordinate is exactly
\[\boxed{\frac{q-2}{2}}.\]
All formulas are invariant under arbitrary nonzero coordinate multipliers.

## Assumptions and scope

A repair set for coordinate \(i\) is a subset of other coordinates whose generator columns span the column of \(i\) over \(F\). It is minimal when no proper subset is a repair set. Two sets are disjoint when they share no coordinate. A circuit is an inclusion-minimal linearly dependent subset of the full coordinate-column matroid; circuits containing \(i\) correspond exactly to minimal repair sets for \(i\), after removing \(i\). The claim concerns ordinary coordinatewise Hamming linear dependence, not the NRT distance or the folded block Hamming metric.

The first Hasse derivative satisfies \((X^j)^{[1]}=\binom{j}{1}X^{j-1}\). In characteristic two, if \(f(X)=c_0+c_1X+c_2X^2+c_3X^3\), then \(f^{[1]}(a)=c_1+c_3a^2\). The multiplicity-two construction is also a conventional univariate multiplicity code, up to coordinate multipliers. The parameters \(m\ge2\) and degree at most three are essential to the statements; none of the formulas is asserted for higher degrees, different derivative orders, or odd characteristic.

## Proof

Because multiplication of any generator column by a nonzero scalar changes neither linear dependence supports nor repair-set membership, it suffices to take all multipliers equal to one. Relative to polynomial coefficient basis \(1,X,X^2,X^3\), write the generator columns as
\[E_a=(1,a,a^2,a^3)^\top,\qquad T_a=(0,1,0,a^2)^\top.\]
The four evaluation columns at any four distinct elements have nonzero Vandermonde determinant, so the dimension is four for \(q\ge4\). The \(T_a\) lie in the two-dimensional subspace with first and third components zero; any two distinct \(T_a,T_b\) are independent because the squaring map is injective. Hence exactly the triples of distinct derivative columns are minimal dependent sets of size three.

To exclude other small circuits, observe that the projection onto the first and third components sends \(E_a\) to \((1,a^2)\) and every \(T_a\) to zero. Thus any two distinct evaluation columns remain independent modulo the entire derivative-column span. Every three distinct evaluation columns are independent by their first three Vandermonde rows. It follows that there are no dependent pairs, no three-element circuits involving evaluation columns, no four-element circuit with two evaluation and two derivative columns, and no four-element circuit consisting entirely of evaluation columns. Any set of four with three or more derivatives contains an already dependent derivative triple and so cannot be a four-circuit.

For three distinct \(a,b,c\), their evaluation columns span the kernel of a nonzero row functional \(L\) whose value on \(E_x\) is the cubic \(P(x)=(x-a)(x-b)(x-c)\). The same functional on \(T_d\) equals the first Hasse derivative \(P^{[1]}(d)\). In characteristic two,
\[P^{[1]}(X)=X^2+ab+ac+bc.\]
Squaring permutes \(F\), so there is exactly one \(d\) with \(P^{[1]}(d)=0\). Moreover, \(P^{[1]}(a)=(a-b)(a-c)\ne0\), and likewise for \(b,c\), whence \(d\notin\{a,b,c\}\). The dependent four-set is minimal because its triples are independent. This proves the complete stated circuit classification and the two \(\binom{q}{3}\) totals.

For fixed \(d\), set \(x=a-d\), \(y=b-d\), \(z=c-d\). Each is nonzero, and the defining equation becomes \(xy+xz+yz=0\), or
\[\frac{1}{x}+\frac{1}{y}+\frac{1}{z}=0.\]
Hence \(u=1/x,v=1/y,w=1/z\) are three distinct nonzero vectors of the \(m\)-dimensional vector space \(F\) over \(\mathbb F_2\), with \(u+v+w=0\). Every pair of distinct nonzero vectors determines exactly one such triple, and these are exactly the projective lines of \(\operatorname{PG}(m-1,2)\). Their number is \((q-1)(q-2)/6\). Every pair of distinct other derivatives repairs \(D_d\), yielding \(\binom{q-1}{2}\) two-helper sets. For fixed \(a\), every choice of two distinct other evaluation indices \(b,c\) determines a unique \(d\), yielding \(\binom{q-1}{2}\) distinct three-helper repair sets for \(V_a\). Since no smaller dependent set involves evaluation columns, their locality is three, while derivative locality is two.

It remains to establish the sharp **unrestricted** disjoint-repair bound for a value coordinate. Any repair set for \(V_a\) must contain at least two other value positions: if it contained zero or one \(V_b\), the projection onto the first and third components would require \((1,a^2)\) to lie in the span of \((1,b^2)\) with \(b\ne a\), which is impossible. There are only \(q-1\) other value positions, so the number of pairwise disjoint repair sets is at most \(\lfloor(q-1)/2\rfloor=(q-2)/2\).

This is attained for every \(a\). Choose a primitive element \(g\in F^\times\). For each integer \(i\) from zero to \((q-4)/2\), put
\[b_i=a+g^{2i},\quad c_i=a+g^{2i+1},\quad d_i=a+\sqrt{g^{4i+1}}.\]
These indices satisfy \(d_i^2=ab_i+ac_i+b_ic_i\), so \(\{V_{b_i},V_{c_i},D_{d_i}\}\) repairs \(V_a\). The pairs \(\{b_i,c_i\}\) are disjoint because the exponents range consecutively over \(0,1,\ldots,q-3\), and the \(d_i\) are distinct because \(\gcd(4,q-1)=1\) and squaring is bijective on \(F\). Thus exactly \((q-2)/2\) pairwise disjoint repair sets exist. The upper bound applied to arbitrary sets, so the optimum is global, not just for the displayed three-helper construction. This completes the proof.

## Verification

Run `python3 artifacts/verify.py` with Python 3 and no external packages. It constructs field arithmetic and evaluates all generator columns independently for \(q=4,8,16\), then exhaustively tests **every** coordinate subset of sizes two, three, and four for minimal dependence by finite-field Gaussian elimination. It compares those results with the claimed formulas; checks the fixed-derivative Steiner triples; confirms every value-coordinate repair count; and checks the disjoint constructions at every target. The observed numbers of three-circuits and four-circuits, respectively, are \((4,4)\), \((56,56)\), and \((560,560)\); the script prints `VERIFY_OK` upon success. The computations are finite corroboration, not a substitute for the all-parameter proof above. The general nonzero-multiplier extension is justified algebraically by column rescaling, not enumerated case-by-case.

## Relationship to prior work

Can and Horowitz introduced generalized hyperderivative Reed–Solomon codes and proved NRT-metric MDS, duality, and further structural properties; the earliest verified public version appeared on 28 December 2025 (arXiv:2512.22948). Their explicit Hasse-derivative evaluation map specializes to precisely the code treated here. The theorem above concerns the **ordinary Hamming dual-circuit supports and coordinatewise repair geometry**, rather than their NRT-metric results.

Univariate multiplicity-two codes predate that construction under an equivalent evaluation representation. Camps Moreno and collaborators' work on duals of multiplicity codes (arXiv:2505.14472) includes an explicit univariate dual description, but the relevant theorems and Appendix B do not state the specific cubic characteristic-two circuit enumeration, projective Steiner correspondence, or sharp unrestricted coordinatewise disjoint availability. Li and Wootters establish disjoint repair group properties for **lifted multivariate** multiplicity codes, a different construction and parameter regime. These relationships and the possibility of an older implicit tangent-geometry formulation remain relevant novelty risks; no claim is made that every possible implicit reformulation has been excluded.

## Limitations

Only circuits with at most four coordinates are classified; larger circuits may exist. The exact number of minimal helper sets of a derivative coordinate of cardinality greater than three is not determined here, nor is its unrestricted disjoint-repair optimum. No asymptotic decoding runtime, optimized global erasure correction, Hamming weight distribution, or results for odd characteristic are asserted. The structural proof is mathematical, with finite-field verification through order sixteen only. No independent external validation or audit has been performed.

## References

1. Mahir Bilen Can and Benjamin Horowitz, *Generalized Hyperderivative Reed–Solomon Codes*, arXiv:2512.22948 (first posted 28 December 2025); *Designs, Codes and Cryptography* 94, article 91 (2026), DOI: 10.1007/s10623-026-01849-3. https://arxiv.org/abs/2512.22948 ; https://link.springer.com/article/10.1007/s10623-026-01849-3
2. Eduardo Camps Moreno, Adrián Fidalgo-Díaz, Hiram H. López, Umberto Martínez-Peñas, Diego Ruano, Rodrigo San-José, *Duals of multiplicity codes*, arXiv:2505.14472 (2025), https://arxiv.org/abs/2505.14472 ; https://link.springer.com/article/10.1007/s10623-026-01812-2
3. Ray Li and Mary Wootters, *Lifted Multiplicity Codes and the Disjoint Repair Group Property*, arXiv:1905.02270 (2019), https://arxiv.org/abs/1905.02270
