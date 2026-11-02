# A fifth-order prefix law for the \(3\)-adic Cantor multiplier \(31\)

## Finding
Let \(\mathbb Z_3\) denote the ternary-adic integers, and let \(\Sigma\) be the set whose base-three digits all belong to \(\{0,1\}\). Define
\[
X=\Sigma\cap31^{-1}\Sigma,
\]
and let \(a_n\) be the number of different length-\(n\) ternary prefixes occurring in \(X\), including \(a_0=1\). Then
\[
(a_0,a_1,a_2,a_3,a_4)=(1,2,3,5,7),\quad
 a_n=a_{n-1}+a_{n-4}+a_{n-5}\quad(n\ge5).
\]
The exact generating series is
\[
\sum_{n\ge0}a_nz^n=\frac{(1+z)(1+z^2+z^3)}{1-z-z^4-z^5}.
\]
If \(\beta\) is the unique positive real root greater than one of \(t^5-t^4-t-1\), then
\[
\dim_H X=\log_3\beta\approx0.3673051288896,
\qquad \beta\approx1.4970940487628.
\]
The recurrence is statewise on the full ten-state multiplication-carry automaton, not merely an experimentally guessed identity for its initial state.

## Assumptions and scope
The ambient space has the standard \(3\)-adic metric. Digits are read from least significant to most significant, and every prefix counted must extend to an infinite allowed digit sequence. The multiplier \(31=(1011)_3=3^3+3+1\) is the first ternary integer with three digits \(1\) not in a single consecutive block, a natural next case after the homogeneous families \((1^k)_3\) and \((10^{k-1}1)_3\) treated in the foundational literature. All equalities are exact for every integer \(n\ge0\). The dimension statement is a Hausdorff dimension in \(\mathbb Z_3\), not a real-line or box-counting assertion.

## Proof
Write \(x=\sum_{i\ge0}b_i3^i\) with \(b_i\in\{0,1\}\). To calculate \(31x\) one digit at a time, let \(c\) be the incoming nonnegative carry. A choice \(b\in\{0,1\}\) is permitted exactly when
\[
(31b+c)\bmod3\in\{0,1\},
\qquad c'=\lfloor(31b+c)/3\rfloor.
\]
Starting at carry zero, the reachable carry states are exactly \(0,1,3,4,5,10,11,12,14,15\). Their complete labeled transitions \(c\xrightarrow{b}c'\) are

| \(c\) | Allowed transitions |
|---|---|
| 0 | \(0\xrightarrow{0}0\), \(0\xrightarrow{1}10\) |
| 1 | \(1\xrightarrow{0}0\) |
| 3 | \(3\xrightarrow{0}1\), \(3\xrightarrow{1}11\) |
| 4 | \(4\xrightarrow{0}1\) |
| 5 | \(5\xrightarrow{1}12\) |
| 10 | \(10\xrightarrow{0}3\) |
| 11 | \(11\xrightarrow{1}14\) |
| 12 | \(12\xrightarrow{0}4\), \(12\xrightarrow{1}14\) |
| 14 | \(14\xrightarrow{1}15\) |
| 15 | \(15\xrightarrow{0}5\), \(15\xrightarrow{1}15\) |

Each state has a directed path to state zero, which has a self-loop. Therefore every finite admissible prefix extends to an infinite one; there is no dead-end overcounting.

Let \(A\) be the adjacency matrix indexed by the above ten states, with an entry counting digit-labeled transitions, and \(\mathbf1\) the all-ones column. Define \(v_j=A^j\mathbf1\). Directly evaluating five powers from the displayed transitions gives the **ten coordinate equalities**
\[
\boxed{v_5-v_4-v_1-v_0=\mathbf0.}
\]
This finite identity is reproduced by the standalone exact-integer verifier. Multiplying by \(A^{n-5}\), for each \(n\ge5\), proves \(A^n\mathbf1=A^{n-1}\mathbf1+A^{n-4}\mathbf1+A^{n-5}\mathbf1\). Since \(a_n\) is the coordinate at state zero of \(A^n\mathbf1\), it obeys the claimed recurrence. The first five such coordinates are \(1,2,3,5,7\). Multiplying their generating function by \(1-z-z^4-z^5\) gives \(1+z+z^2+2z^3+z^4=(1+z)(1+z^2+z^3)\), proving the rational identity.

The characteristic equation of the recurrence is \(t^5-t^4-t-1=0\). For \(t>1\), its left side is strictly increasing: the derivative is \(t^3(5t-4)-1>0\); the values at one and two have opposite signs. Its root \(\beta>1\) is the unique positive root there. The denominator \(1-z-z^4-z^5\) has its unique positive zero at \(z=\beta^{-1}\); positivity and the presence of the \(z\) term imply no smaller-modulus singularity. Because the numerator is positive at this zero, the exponential prefix-growth rate is \(\beta\). Equivalently, the automaton has Perron growth \(\beta\). The standard graph-directed/\(3\)-adic path-set dimension theorem of Abram and Lagarias then yields \(\dim_H X=\log_3\beta\).

## Verification
Run `python3 verify.py` with Python's standard library. It regenerates the finite carry graph directly from \(31\), compares every edge with the displayed table, checks all ten coordinates of \(A^5\mathbf1-A^4\mathbf1-A\mathbf1-\mathbf1\), verifies the first 16 prefix counts and independently enumerates all \(2^n\) digit candidates for every \(0\le n\le12\), testing multiplication by \(31\) modulo \(3^n\) without using the carry graph. A successful replay prints `VERIFY_OK`. This is an exact finite certificate for the infinite recurrence because the matrix identity propagates to all powers; the enumeration alone would not establish it.

## Relationship to prior work
Abram and Lagarias (2013) introduced and proved the finite automaton method for \(\Sigma\cap M^{-1}\Sigma\) and the dimension formula in terms of its Perron eigenvalue. They explicitly solve the homogeneous ternary-digit families \(M=(1^k)_3\) and \(M=(10^{k-1}1)_3\). Abram, Bolshakov and Lagarias (2015) study two further structured infinite families. These general tools are used here, not claimed as original. Neither inspected paper states the ten-state carry graph, the statewise fifth-order identity or the prefix recurrence for the first gapped three-one multiplier \(M=(1011)_3=31\). The new explicit arithmetic instance is therefore distinguished from the known existence of an effective general procedure. Its modest scope and residual priority risk are acknowledged.

## Limitations
This is a specific exact multiplier result, not a classification of all three-nonzero-digit multipliers, and it does not improve known bounds on the exceptional set for powers of two. The generic prior algorithm can in principle compute every multiplier, so the amount of independent novelty lies in this previously unrecorded low-order renewal identity and the explicit recurrence. No independent validation or universal priority guarantee is asserted.

## References
Abram, W. and Lagarias, J. C., *Intersections of multiplicative translates of 3-adic Cantor sets*, 2013 preprint, arXiv:1308.3133, https://arxiv.org/abs/1308.3133; J. Fractal Geom. 1 (2014), 349–390.

Abram, W. C., Bolshakov, A. and Lagarias, J. C., *Intersections of multiplicative translates of 3-adic Cantor sets II: two infinite families*, 2015 preprint, arXiv:1508.05967, https://arxiv.org/abs/1508.05967.
