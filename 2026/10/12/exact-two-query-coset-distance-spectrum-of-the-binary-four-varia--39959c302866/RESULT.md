# Exact two-query coset-distance spectrum of the binary four-variable first-order Reed–Muller code

## Finding

Let \(C=\operatorname{RM}_2(1,4)\) be the binary linear \([16,5,8]\) code of affine functions on \(\mathbb F_2^4\). For two binary received words, charge one unit per coordinate where at least one residual word is nonzero. For every ordered pair of cosets of \(C\), let its *joint coset distance* be the smallest such charge after independently adding one codeword to each received word. The complete distribution of these distances is

\[
\begin{aligned}
P_C(z)={}&1+48z+1080z^2+15120z^3+144585z^4\\
&+858144z^5+2359602z^6+798000z^7\\
&+17388z^8+336z^9.
\end{aligned}
\]

Thus the second generalized covering radius is exactly \(R_2(C)=9\). Exactly \(336\) of the \(2^{22}=4{,}194{,}304\) ordered two-row cosets have joint distance nine. This is an exact finite classification of the joint nearest-support distance, not a statement about all lengths or higher-order Reed–Muller families.

## Assumptions and scope

Coordinates are the sixteen binary vectors \(x\in\mathbb F_2^4\), labeled by integers \(0,\ldots,15\) in binary. All sums below are in characteristic two. Define

\[
C=\bigl\{\bigl(a_0+\textstyle\sum_{i=0}^{3}a_{i+1}x_i\bigr)_{x\in\mathbb F_2^4}: a_i\in\mathbb F_2\bigr\}.
\]

For \(u,v\in\mathbb F_2^{16}\), define

\[
d_2((u,v),C^2)=\min_{c,d\in C}
\bigl|\operatorname{supp}(u+c)\cup\operatorname{supp}(v+d)\bigr|.
\]

This quantity depends only on the ordered cosets \((u+C,v+C)\); let \(P_C(z)=\sum_{(u+C,v+C)}z^{d_2((u,v),C^2)}\), and let \(R_2(C)\) be its largest occurring exponent. The exponent is *not* the sum of the two ordinary Hamming coset distances. Equivalently, after identifying \(\mathbb F_2^2\) with \(\mathbb F_4\) additively, it is the Hamming coset distance for the scalar extension of \(C\) to \(\mathbb F_4\). The scalar-extension interpretation does not turn the sixteen binary evaluation points into the full four-variable \(\mathbb F_4\) grid.

## Proof

**1. Quotient and parity checks.** Let \(P=\{0,1,2,4,8\}\) and \(N=\{3,5,6,7,9,10,11,12,13,14,15\}\). The values of an affine function at \(P\) determine all its sixteen values. In fact, for each \(x\in N\), every \(c\in C\) satisfies

\[
c_x+\bigl(1+\operatorname{wt}(x)\bmod 2\bigr)c_0
+\sum_{i:x_i=1}c_{2^i}=0.
\]

Here \(\operatorname{wt}(x)\) is the number of nonzero bits in the four-bit index \(x\); the parenthesized coefficient is interpreted in \(\mathbb F_2\). These eleven equations give an \(11\)-row parity-check matrix \(H\) whose restriction to columns indexed by \(N\) is the identity. Thus \(H\) has rank eleven, its kernel equals \(C\), and there are \(2^{11}\) ordinary cosets and \(2^{22}\) ordered pairs. Denote the column of \(H\) at position \(j\) by \(h_j\in\mathbb F_2^{11}\).

**2. Exhaustive recurrence.** Represent a two-row syndrome by \(s=(s_1,s_2)\in\mathbb F_2^{11}\times\mathbb F_2^{11}\). Write \(e_j=(h_j,0)\) and \(f_j=(0,h_j)\). Let \(D_j(s)\) be the minimum number of nonzero columns in a two-row error array supported among coordinate positions \(0,\ldots,j-1\), subject to syndrome \(s\). Set \(D_0(0)=0\) and \(D_0(s)=+\infty\) for \(s\ne0\). At each of the sixteen coordinates, the column is one of \((0,0),(1,0),(0,1),(1,1)\), giving the exact recurrence

\[
D_{j+1}(s)=\min\bigl\{D_j(s),\ 1+D_j(s+e_j),\ 1+D_j(s+f_j),\ 1+D_j(s+e_j+f_j)\bigr\}.
\]

Induction on \(j\) proves this recurrence enumerates **every** feasible error array on the first \(j\) coordinates and finds its minimum support. At \(j=16\), any two matrices having the same pair of syndromes differ by an element of \(C^2\); hence \(D_{16}(s)\) equals the required joint coset distance. There are exactly \(2^{22}\) states to enumerate, not a sample of states.

**3. Evaluation of the finite recurrence.** The supplied standalone `verify.cpp` enumerates all sixteen stages over all \(2^{22}\) states using unsigned integer syndrome masks. Counting the terminal values gives, for distances \(0\) through \(9\) respectively,

\[
(1,48,1080,15120,144585,858144,2359602,798000,17388,336).
\]

All remaining distances have count zero. The counts sum to \(2^{22}\); the largest attained distance is nine. A concrete distance-nine pair has first row supported on \(\{3,6,9,10,11,13\}\) and second row supported on \(\{3,5,6,7,11,12\}\). Its syndrome pair, in the increasing \(N\)-coordinate convention, is \((373,207)\). The same executable independently evaluates the minimum over **all** \(32^2\) pairs of affine row-codeword shifts for every one of the \(2^{22}\) coset pairs, reproducing the identical distance for each pair and the entire histogram. Its pruning uses only the rigorous lower bound \(\max\{d_1(u+C,C),d_1(v+C,C)\}\) and the fact that a union cannot be smaller than either of its components. Thus no branch capable of improving a minimum is omitted.

**4. Low-weight consistency check.** Every nonconstant affine function on four binary variables has weight eight, and the all-one function has weight sixteen. The induced quaternary scalar-extension code therefore also has minimum nonzero column weight eight. For error supports of sizes zero through three, no two distinct coset representatives can collide: their difference would have support at most six. The first four histogram coefficients must consequently equal \(\binom{16}{j}3^j\) for \(0\le j\le3\), namely \(1,48,1080,15120\), as found independently.

## Verification

Compile and execute the complete exact checker using a C++17 compiler:

```sh
g++ -O3 -std=c++17 verify.cpp -o verify
./verify
```

The checked output is:

```text
VERIFY_OK
code=[16,5,8]_2; number_of_two_row_cosets=4194304
R_2=9; distance_9_cosets=336; witness_syndrome=(373,207)
distribution=1,48,1080,15120,144585,858144,2359602,798000,17388,336
```

The checker first constructs and tests all thirty-two affine codewords and the eleven parity checks, performs the sixteen-stage syndrome recurrence, then independently enumerates all \(2^{11}\times2^{11}\) canonical coset pairs with direct minimization over affine shifts. It compares every computed distance and the two distributions. This finite exhaustive computation, together with the recurrence proof, is the certificate for the finite numerical statement; mere partial enumeration would not suffice.

## Relationship to prior work

The generalized covering radius was introduced by Elimelech, Firer, and Schwartz for joint retrieval cost. Elimelech, Wei, and Schwartz analyzed Reed–Muller generalized covering radii; their Table I lists exact formulas for order zero, order two below the variable count, and the two highest orders, while the first-order, four-variable case falls in their nonexact-bounds regime. Yu and Schwartz proved a general second-order packing–covering inequality and related bounds in a September 2026 paper; their inspected formulas do not give this joint coset-distance distribution. Ozeki and earlier work classify ordinary deep holes and ordinary coset weight distributions for the same binary code; those are one-row invariants, not the two-row minimum union-support distribution computed here.

Luo, Zhou, Mesnager, Sagar, and Yan study second generalized radii of selected cyclic codes and extensions. Their 2026 publisher abstract was accessible, but not their complete paper; its possible implications for the radius-nine *consequence* remain a source-access risk. No inspected published statement gives this full ten-coefficient joint coset-distance distribution. Equivalence with an ordinary quaternary scalar-extension covering problem was explicitly included in the overlap comparison.

## Limitations

The claim concerns only \(\operatorname{RM}_2(1,4)\) and two simultaneous rows. Its proof uses exhaustive exact computation of \(2^{22}\) states, not a closed form for arbitrary variable count. It does not classify the equivalence orbits of the \(336\) farthest coset pairs or establish higher-order covering radii. Availability of selected relevant sources is incomplete, and the absence of a matching indexed statement is not a proof of global novelty. Independent scientific audit has not been performed.

## References

1. D. Elimelech, M. Firer, M. Schwartz, “The Generalized Covering Radii of Linear Codes,” *IEEE Transactions on Information Theory* **67** (2021), 8070–8085. https://arxiv.org/abs/2012.06467
2. D. Elimelech, H. Wei, M. Schwartz, “On the Generalized Covering Radii of Reed–Muller Codes,” *IEEE Transactions on Information Theory* **68** (2022), 4378–4391. https://arxiv.org/abs/2107.09902
3. W. Yu, M. Schwartz, “On the Generalized Packing and Covering Radii of Codes,” publicly posted 13 September 2026, arXiv:2609.14477v1. https://arxiv.org/abs/2609.14477
4. M. Ozeki, “A Study of Deep Holes in the First-Order Reed–Muller Codes,” *Designs, Codes and Cryptography* **63** (2012), 451–481. https://www.researchgate.net/publication/268676260_A_study_of_deep_holes_in_the_first-order_Reed-Muller_codes
5. R. Luo, Z. Zhou, S. Mesnager, V. Sagar, H. Yan, “Determining the Exact Value of the Second-Order Generalized Covering Radius of Two Classes of Binary Cyclic Codes,” *Designs, Codes and Cryptography* **94** (2026), article 71. https://doi.org/10.1007/s10623-025-01799-2
