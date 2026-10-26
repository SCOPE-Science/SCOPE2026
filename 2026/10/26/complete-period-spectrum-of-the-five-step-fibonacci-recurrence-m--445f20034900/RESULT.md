# Complete period spectrum of the five-step Fibonacci recurrence modulo \(2^k\)

## Finding

For each integer \(k\ge1\), let \(R_k=\mathbb Z/2^k\mathbb Z\) and let the permutation \(T:R_k^5\to R_k^5\) be
\[
T(a,b,c,d,e)=(b,c,d,e,a+b+c+d+e).
\]
The determinant of its companion matrix is \(1\), so every point belongs to one periodic orbit. Put, for \(j\ge0\),
\[
A_j(k)=2^{\min(k,j+2)},\qquad
B_0(k)=2^{2\min(k,1)+\min(k,2)},\qquad
B_j(k)=2^{4\min(k,j)+\min(k,j+2)}\quad(j\ge1).
\]
Let \(c_d(k)\) be the number of distinct cycles of **least** length \(d\). Then
\[
\begin{aligned}
c_1(k)&=A_0(k),\\
c_{2^j}(k)&=\frac{A_j(k)-A_{j-1}(k)}{2^j}&& (1\le j\le k),\\
c_3(k)&=\frac{B_0(k)-A_0(k)}3,\\
c_{3\cdot2^j}(k)&=\frac{B_j(k)-B_{j-1}(k)-A_j(k)+A_{j-1}(k)}{3\cdot2^j}&& (1\le j\le k).
\end{aligned}
\]
All other cycle counts vanish (zero-valued entries within the displayed families are permitted). In particular, the total number of cycles is
\[
\boxed{C(1)=8,\qquad
C(k)=\frac{257\cdot16^k+960k+1408}{720}\quad(k\ge2).}
\]
The first five totals are \(8,96,1468,23400,374292\).

## Assumptions and scope

All congruences in the theorem are modulo the positive power of two \(2^k\); the five initial coordinates range independently over \(R_k\). A cycle and its cyclic rotations are counted once. There is no restriction that an initial vector be primitive or that its coordinates generate the additive group. The formula does not address non-power-of-two moduli. Set \(v_2(m)\) to be the exponent of two dividing a nonzero integer \(m\). The valuation list of a nonsingular integer matrix means the sorted \(2\)-adic valuations of its five Smith invariant factors.

## Proof

Write \(M\) for the integer companion matrix of \(T\), and let \(I\) be the identity. For a matrix with \(2\)-adic Smith valuations \(e_1,\ldots,e_5\), its kernel modulo \(2^k\) has cardinality \(2^{\sum_i\min(k,e_i)}\). We establish the exact Smith data
\[
\begin{array}{c|c}
\text{integer matrix}&\text{Smith valuations}\ 
M^{2^j}-I\quad(j\ge0)&(0,0,0,0,j+2)\\
M^3-I&(0,0,1,1,2)\\
M^{3\cdot2^j}-I\quad(j\ge1)&(j,j,j,j,j+2).
\end{array}
\]

For the first row, the characteristic polynomial is
\[
f(x)=x^5-x^4-x^3-x^2-x-1,
\qquad \bar f(x)=(x+1)(x^2+x+1)^2\in\mathbf F_2[x].
\]
Since \(f(1)=-4\) and \(f'(1)=-5\) is odd, Hensel's lemma produces a unique root \(\alpha\equiv1\pmod2\) in \(\mathbb Z_2\). Taylor expansion at \(1\) gives \(v_2(\alpha-1)=2\). The factor \(x-\alpha\) and its monic degree-four cofactor are coprime over \(\mathbb Z_2[x]\) (the cofactor evaluates to an odd number at \(1\)). By the Chinese remainder theorem, the cyclic companion module splits as one rank-one block with eigenvalue \(\alpha\) and a rank-four block. The latter has no eigenvalue \(1\) after any \(2^j\)-th power reduction modulo two, since its reduced characteristic polynomial is \((x^2+x+1)^2\) and the roots have multiplicative order three. The rank-four difference is therefore invertible over \(\mathbb Z_2\). On the rank-one block the lifting-the-exponent identity is
\[
v_2(\alpha^{2^j}-1)=v_2(\alpha-1)+j=j+2.
\]
This proves the first Smith row for every \(j\ge0\).

For the remaining rows, exact calculation of all square minors of the displayed integer matrices gives:
\[
\begin{array}{c|c}
M^3-I&(0,0,1,1,2)\\
(M^6-I)/2&(0,0,0,0,2)\\
(M^{12}-I)/4&(0,0,0,0,2).
\end{array}
\]
These are finite integer calculations, not numerical approximations: the standalone program in `artifacts/verify.py` recomputes the greatest common divisor of every minor of each size \(1\) through \(5\), and differences of their valuations. To propagate the second and third calculations indefinitely, put \(U_j=(M^{3\cdot2^j}-I)/2^j\) for \(j\ge1\). The identity
\[
U_{j+1}=U_j\bigl(I+2^{j-1}U_j\bigr)
\]
shows integrality inductively; for every \(j\ge2\), the rightmost factor is congruent to \(I\) modulo two and hence invertible over \(\mathbb Z_2\). Therefore all \(U_j\) for \(j\ge2\) share the Smith valuations of \(U_2\). Together with the direct \(j=1\) calculation, this gives \((j,j,j,j,j+2)\) for \(M^{3\cdot2^j}-I\), as required.

The Smith data imply precisely
\[
|\operatorname{Fix}(T^{2^j})|=A_j(k),\qquad
|\operatorname{Fix}(T^{3\cdot2^j})|=B_j(k).
\]
Taking \(j=k\) in the second identity gives \(B_k(k)=2^{5k}\), so \(T^{3\cdot2^k}=I\) on all \(R_k^5\). Every least period therefore divides \(3\cdot2^k\). For each \(j\), subtracting the fixed points of \(T^{2^{j-1}}\) from those of \(T^{2^j}\) counts the points having least period exactly \(2^j\); dividing by that length counts cycles. The analogous subtraction on the \(3\)-part, with inclusion–exclusion for pure powers of two, gives exactly the four displayed cycle-count formulas. This accounts for every possible period.

For completeness, the total-cycle simplification is explicit. When \(k=1\), the counts at lengths \(1,3,6\) are \(2,2,4\), respectively, hence \(C(1)=8\). When \(k=2\), the counts at \(1,3,6,12\) are \(4,4,8,80\), hence \(C(2)=96\). For \(k\ge3\), the pure powers of two contribute \(2k\) cycles; periods \(3\) and \(6\) contribute \(4\) and \(18\). The periods \(3\cdot2^j\), \(2\le j\le k-2\), contribute
\[
\frac{31\cdot2^{4j-3}-2}{3}
\]
cycles each. The two terminal lengths \(3\cdot2^{k-1}\) and \(3\cdot2^k\) contribute \(5\cdot2^{4k-7}\) and \(5\cdot2^{4k-4}\), respectively. Summing the finite geometric series gives
\[
C(k)=2k+22+\sum_{j=2}^{k-2}\frac{31\cdot2^{4j-3}-2}{3}
+5\cdot2^{4k-7}+5\cdot2^{4k-4}
=\frac{257\cdot16^k+960k+1408}{720}.
\]
The sum is empty when \(k=3\). This finishes the proof.

## Verification

The standalone Python 3 standard-library program `artifacts/verify.py` independently recomputes the three finite Smith bases via exact gcds of all minors, plus the \(M-I\) case. It enumerates **all** states and complete cycles for \(k=1,2,3\), checks total state mass and the complete predicted cycle multiplicities, verifies the first five OEIS orbit totals, and recomputes the displayed total formula for additional powers of two. Execute `python3 artifacts/verify.py` from the directory containing the extracted artifact. The finite calculations certify the required base matrices; the Hensel and unit-matrix induction arguments prove the infinite-family statements.

## Relationship to prior work

T. D. Noe's OEIS A106287 (2005) defines and tabulates the total orbit numbers for the five-step recurrence for various moduli; OEIS A106290 records the number of different lengths and specifically identifies six lengths at modulus eight. The table values \(8,96,1468,23400,374292\) are therefore **prior data**, not new discoveries. The finding supplies a universal exact formula for all powers of two and the complete multiplicities for every possible length, rather than simply extending that table. Earlier general matrix-period methods and papers on modular higher-order recurrences motivate the approach but do not establish this exact five-step orbit multiplicity distribution in the source material examined. A 1996 chapter by Waddill on general \(k\)-order recurrences was located only at its abstract; it is a specific unresolved possible priority source.

## Limitations

The claim applies only to the five-step Fibonacci companion map at powers of two. No assertion is made for other step counts, arbitrary moduli, or statistical independence of orbit lengths. Earlier or unlocated results may imply the formulas; originality is assessed only against accessible evidence. The package contains a complete proof and executable finite checks, but it has not undergone independent mathematical audit.

## References

1. T. D. Noe, *Number of orbits of the 5-step recursion mod n*, OEIS A106287, initial entry May 2, 2005, https://oeis.org/A106287.
2. T. D. Noe, *Number of different orbit lengths of the 5-step recursion mod n*, OEIS A106290, initial entry May 2, 2005, https://oeis.org/A106290.
3. M. E. Waddill, *Properties of a k-Order Linear Recursive Sequence Modulo m*, in *Applications of Fibonacci Numbers*, 1996, pp. 505–519, DOI:10.1007/978-94-009-0223-7_41 (abstract inspected; full text not accessed).
4. E. Karaduman, *K-nacci Sequences in Finite Triangle Groups*, *Discrete Dynamics in Nature and Society*, 2009, DOI:10.1155/2009/453750 (group-generator orbit setting, not a five-coordinate affine-ring census).
