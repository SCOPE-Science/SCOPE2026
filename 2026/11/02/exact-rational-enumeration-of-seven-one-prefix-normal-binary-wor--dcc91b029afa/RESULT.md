# Exact rational enumeration of seven-one prefix-normal binary words

## Finding

For a binary word \(w=w_1\cdots w_n\), let \(|w|_1\) count its ones. It is *prefix normal* (with respect to ones) if every contiguous factor of length \(j\) has at most \(\sum_{i=1}^{j} w_i\) ones, for each \(1\le j\le n\). Write \(p_7(n)\) for the number of length-\(n\) prefix-normal binary words containing exactly seven ones (and set \(p_7(n)=0\) for \(n<7\)). Then, as an identity of formal power series,

\[
\sum_{n\ge0}p_7(n)z^n=
\frac{z^7 H(z)}{(1-z)(1-z^3)(1-z^4)^2(1-z^6)^3},
\]

where the coefficients of \(H(z)\), from degree zero through eighteen, are

```
1, 3, 9, 17, 35, 48, 76, 85, 108, 103, 108, 85, 76, 48, 35, 17, 9, 3, 1
```

The counting function \(p_7(n)\) is a quasipolynomial of degree six and **least quasiperiod twelve** on the range \(n\ge7\). Its leading asymptotic is

\[
p_7(n)=\frac{289}{2488320}n^6+O(n^5).
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); words are indexed linear words, not necklaces. The number of ones is fixed at seven, with arbitrary numbers of zeros and all finite lengths allowed. Prefix normality compares every ordinary (non-cyclic) factor with the initial prefix of the same length. The enumeration includes all such words and no additional primitivity or minimality restrictions.

## Proof

**Step 1: Convert words into gap inequalities.** Every prefix-normal word with seven ones begins with a one. Write its seven ones in order, let \(g_1,\ldots,g_6\ge1\) denote the distances between consecutive ones, and let \(\ell\ge0\) count trailing zeros. Such a word is prefix normal if and only if, for each \(1\le h\le5\) and each \(1\le i\le6-h\),

\[
\sum_{j=1}^h g_j\le\sum_{j=i+1}^{i+h}g_j.
\]

Indeed, an occurrence of \(h+1\) ones in an interval of given length is shortest when it spans \(h\) consecutive gaps. Comparing all such spans to the first \(h+1\) ones gives the displayed inequalities; these span inequalities, in turn, compare every factor's ones with the corresponding prefix. In particular \(g_1\) is a minimum gap. Set \(a=g_1\ge1\) and \((x,y,z,t,v)=(g_2-a,g_3-a,g_4-a,g_5-a,g_6-a)\). The complete irredundant list, after the nonnegativity constraints, is

\[
y+z\ge x,\qquad z+t\ge x,\qquad t+v\ge x,\qquad z+t+v\ge x+y.
\]

To check completeness: the inequalities for \(h=1\) give all nonnegative offsets; those for \(h=2\) reduce to the first three displayed inequalities, and \(h=3\) adds only the fourth. All \(h=4,5\) comparisons are implied by nonnegativity and these inequalities. For example, \(x+y\le z+t+v\) already compares the first three gaps with the final three, while all other constraints with longer blocks cancel to one of the above or a sum thereof. Direct expansion also verifies the equivalence.

The word length is \(n=1+6a+x+y+z+t+v+\ell\). Let \(C\subseteq\mathbb R^5\) be the pointed rational cone cut out by the nine inequalities just stated (five nonnegativity and four additional). Its integer-point generating function, graded by coordinate sum, is

\[
G(z)=\sum_{(x,y,z_0,t,v)\in C\cap\mathbb Z^5}
 z^{x+y+z_0+t+v}.
\]

The variable \(z_0\) here is a coordinate; \(z\) in the power series is the formal variable. Summing the unrestricted offset \(\ell\) and positive minimum gap \(a\) gives

\[
\sum_{n\ge0}p_7(n)z^n=\frac{z^7G(z)}{(1-z)(1-z^6)}.
\]

**Step 2: Bound the exact numerator by the extremal rays.** The primitive extremal rays of \(C\), in the offset-coordinate order \((x,y,z_0,t,v)\), are exactly

```
(0,0,0,0,1)  (0,0,0,1,0)  (0,0,1,0,0)
(0,1,0,0,1)  (0,1,0,1,0)  (0,1,1,0,0)
(1,0,1,0,1)  (1,0,1,1,0)
(1,1,0,1,1)  (1,1,0,2,0)  (1,1,1,0,1)
(2,1,1,1,1)  (2,1,1,2,0)
```

Their coordinate sums, including repetitions, are \(1,1,1,2,2,2,3,3,4,4,4,6,6\), with total \(39\). To prove the enumeration is exhaustive, intersect every choice of four out of the nine supporting hyperplanes, compute its signed vector of \(4\)-by-\(4\) minors, discard dependent intersections and infeasible signs, and divide each feasible vector by its coordinate gcd. Any extremal ray of a pointed full-dimensional polyhedral cone in \(\mathbb R^5\) has at least four linearly independent active supporting hyperplanes. The script `verify.py` performs this exhaustive, integer-only calculation and checks that these thirteen rays are exactly the result.

Triangulate the cone using its extreme rays and choose half-open boundary conventions to partition its lattice points into simplicial cones. In each simplicial cone, every lattice point lies uniquely in a fundamental parallelepiped translated by nonnegative integer multiples of the primitive generators. The parallelepiped representative has nonnegative coordinate sum at most the sum of its five generator degrees; a half-open boundary cannot enlarge that bound. Consequently, with

\[
D(z)=(1-z)^3(1-z^2)^3(1-z^3)^2(1-z^4)^3(1-z^6)^2,
\]

\(D(z)G(z)\) is a polynomial of degree at most \(39\). This is an exact finite-determination bound for the infinite counting problem. No assumption of a numerical recurrence is used.

**Step 3: An exact finite integer identity.** Define

\[
K(z)=(1-z)^3(1-z^2)^3(1-z^3)(1-z^4).
\]

The verifier directly enumerates every integer point in \(C\) whose coordinate sum is at most \(39\), by bounded nested integer loops with the nine cone inequalities. Exact coefficient convolution verifies all forty coefficients, degrees zero through 39, of the identity

\[
D(z)G(z)=K(z)H(z).
\]

Since the left side is rigorously a polynomial of degree at most 39, these forty exact coefficients determine it globally; they are not a finite sample used to infer an infinite theorem. The right side has degree \(34\). Cancelling the polynomial identity \(D=K(1-z^3)(1-z^4)^2(1-z^6)^2\) gives

\[
G(z)=\frac{H(z)}{(1-z^3)(1-z^4)^2(1-z^6)^2},
\]

and Step 1 yields the claimed generating function.

**Step 4: Exact least quasiperiod and leading term.** The denominator has only twelfth roots of unity as possible poles. Hence its coefficients are eventually quasipolynomial with period dividing twelve and degree at most six. In fact the numerator \(H(z)\) has remainder \(z\) modulo \(z^2+1\), and remainder \(1\) modulo \(z^2-z+1\). Thus the generating function retains genuine poles at primitive fourth and sixth roots of unity, forcing any quasiperiod to be divisible by both four and six. There is a pole of order seven at \(z=1\), because \(H(1)=867\). All terms of the sequence for \(n\ge7\) follow the same quasipolynomial, and its least period is twelve. Finally the order-seven pole has leading coefficient

\[
\frac{H(1)}{6!\,(1\cdot3\cdot4^2\cdot6^3)}=\frac{289}{2488320}.
\]

## Verification

Run `python3 verify.py` using Python's standard library. It independently recomputes all thirteen primitive rays by exact determinants, all coefficient identities through the rigorous degree cutoff of 39, and forty extra coefficients as a consistency check. It checks the numerator's cyclotomic remainders and evaluates the formula against direct complete enumeration of prefix-normal words with seven ones at every length from 7 through 18, inclusive. The actual successful output was

```
VERIFY_OK rays=13 degrees_sum=39 coeffs=71 word_lengths=7..18
density7_counts_n7_to18 1,4,13,31,71,134,249,417,688,1062,1628,2367
numerator_H 1,3,9,17,35,48,76,85,108,103,108,85,76,48,35,17,9,3,1
```

The all-length conclusion depends on the cone triangulation degree bound and exact finite coefficient identity, not on the extra experimental checks.

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada [1] established rationality for every fixed number of ones and explicitly computed the fixed-density generating functions through six ones; they reported not computing the higher densities. Their gap formulation motivates the present seven-one calculation, but rationality alone does not imply the concrete numerator, denominator, least quasiperiod or leading constant above. Later Gray-code generation work [2] provides algorithms for listing prefix-normal words, not this density-seven rational function. Weighted prefix-normality [3] extends the notion to weighted alphabets and does not provide the specific seven-one enumeration. Relevant published research records were searched for fixed-density, seven-one and rational-generating-function equivalents; no covering claim was located. Search absence alone is not proof of priority.

## Limitations

The result is for exactly seven ones in binary *linear* prefix-normal words; it does not give a uniform formula in the density parameter or classify individual words in every coefficient class. An unindexed or differently formulated equivalent enumeration remains possible, and no independent audit is claimed. The half-open-cone argument uses standard rational-polyhedral lattice-point methods; finite verification exhausts the stated cone-coefficient certificate rather than substituting finite experiments for the infinite identity.

## References

[1] Burcsi, Fici, Lipták, Ruskey and Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first public 2016-11-28, https://arxiv.org/abs/1611.09017. In particular its gap criterion and section on fixed-density generating functions.

[2] *Generating a Gray code for prefix normal words*, arXiv:2003.03222, https://arxiv.org/abs/2003.03222.

[3] *Weighted Prefix Normal Words: Mind the Gap*, arXiv:2005.09281, https://arxiv.org/abs/2005.09281.
