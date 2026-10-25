# The two primitive six-cycles of five-free Fibonacci dynamics

## Finding

For positive integers \(u,v\), define the five-free Fibonacci update
\[
T(u,v)=\left(v,\frac{u+v}{5^{\nu_5(u+v)}}\right),
\]
where \(\nu_5(t)\) is the largest exponent \(e\ge0\) such that \(5^e\mid t\). A periodic orbit is **primitive** when the gcd of all its entries is one. Rotations of an orbit's cyclic word describe the same orbit.

**Theorem.** Every positive integer pair satisfying \(T^6(u,v)=(u,v)\) lies on exactly one of the following two families of cyclic words:
\[
 c(1,1,2,3,1,4),\qquad c(7,2,9,11,4,3),
 \qquad c\in\mathbb Z_{>0},\ \gcd(c,5)=1.
\]
Conversely, each displayed cyclic word, and every cyclic rotation of it, satisfies the five-free recurrence and has least period exactly six. Consequently, there are exactly two primitive positive cycles of period six up to rotation; no positive period-one, period-two, or period-three cycle exists. In particular six is the smallest positive cycle length (the parity argument below also excludes periods four and five).

The two primitive words were separately exhibited in the original literature; the new assertion is their **exhaustiveness for all positive starting pairs, without a size bound**.

## Assumptions and scope

We consider the deterministic recurrence on \(\mathbb Z_{>0}^2\) with the indicated complete removal of factors of five at each update. The theorem classifies periodic points whose period divides six. It does not classify all longer cycles, nor the fate of arbitrary nonperiodic initial pairs. The zero pair and signed initial data are outside the theorem.

## Proof

Suppose \(a_0,a_1,\ldots,a_5\) is a positive six-periodic word, indices taken modulo six. Each \(a_i\) is nonzero modulo five, since every output of the recurrence is a five-adic unit. Put
\[
 e_i=\nu_5(a_i+a_{i+1}),\qquad x_i=5^{e_i},
 \qquad x_i a_{i+2}=a_i+a_{i+1}.
\]
At least one exponent is positive; otherwise the ordinary Fibonacci recurrence strictly increases the pair and cannot return to its starting state.

Define the integer matrices
\[
 B_i=\begin{pmatrix}-1&x_i\\1&0\end{pmatrix},
 \qquad P=B_0B_1B_2B_3B_4B_5.
\]
The recurrence says that \(P(a_0,a_1)^{\mathsf T}=(a_0,a_1)^{\mathsf T}\). Since \(\det P=\prod_i x_i\), the trace must satisfy \(\operatorname{tr}P=1+\prod_i x_i\). Multiplying these six explicit matrices gives the polynomial identity
\[
\begin{aligned}
\operatorname{tr}P={}&1+\sum_{i=0}^{5}x_i
+x_0x_2+x_0x_3+x_0x_4+x_1x_3+x_1x_4+x_1x_5\\
&+x_2x_4+x_2x_5+x_3x_5+x_0x_2x_4+x_1x_3x_5.
\end{aligned}
\]
Thus, with \(Q(x)\) denoting the sum of the six singleton, nine pair, and two triple monomials on the right (excluding its leading constant), the necessary identity is
\[
 Q(x)=\prod_{i=0}^{5}x_i. \tag{1}
\]

First restrict the **support** of positive exponents, without bounding those exponents. Let \(b_i=1\) if \(e_i>0\), and \(b_i=0\) otherwise; let \(y_i=1-b_i\). As at least one exponent is positive, reduction of (1) modulo five gives
\[
 \sum_i y_i+\sum_{(i,j)\in E}y_i y_j+y_0y_2y_4+y_1y_3y_5\equiv0\pmod5,
\]
where \(E=\{(0,2),(0,3),(0,4),(1,3),(1,4),(1,5),(2,4),(2,5),(3,5)\}\). This is a finite, **exhaustive** test of all \(2^6=64\) binary words; the table gives one representative of each rotation orbit, its orbit size, and the residue of the displayed sum. A one in a representative marks a positive exponent.

| Exponent-support word | Rotations | Residue modulo five |
|:--|--:|--:|
| `000000` | 1 | 2 |
| `000001` | 6 | 2 |
| `000011` | 6 | 2 |
| `000101` | 6 | 4 |
| `000111` | 6 | 4 |
| `001001` | 3 | 3 |
| `001011` | 6 | 0 |
| `001101` | 6 | 0 |
| `001111` | 6 | 2 |
| `010101` | 2 | 2 |
| `010111` | 6 | 3 |
| `011011` | 3 | 3 |
| `011111` | 6 | 1 |
| `111111` | 1 | 0 |

The rotation counts sum to 64, so the table is complete. Only the rotation classes `001011`, `001101`, and `111111` survive.

If all six exponents are positive, then all \(x_i\ge5\), and dividing \(Q(x)\) by \(\prod_i x_i\) gives the strict bound
\[
 \frac{Q(x)}{\prod_i x_i}
 \le \frac6{5^5}+\frac9{5^4}+\frac2{5^3}<1,
\]
contradicting (1). Hence, after cyclic rotation, the support is either `001011` or `001101`.

For `001011`, write its three nonunit \(x_i\)'s in order as \(A,B,C\). Equation (1) is
\[
 f(A,B,C)=-ABC+2AB+AC+2A+3B+4C+5=0.
\]
For `001101` it is
\[
 g(A,B,C)=-ABC+AC+4A+2BC+3B+2C+5=0.
\]
Here \(A,B,C\in\{5,25,125,\ldots\}\). Both polynomials vanish at \((5,5,5)\); all three partial derivatives of both are strictly negative throughout \([5,\infty)^3\). For \(f\), their respective upper bounds are \(-8,-12,-16\); for \(g\), they are \(-16,-12,-8\). These bounds follow directly by substituting the lower bounds \(A,B,C\ge5\) into each derivative. Therefore equation (1) forces
\[
 A=B=C=5.
\]
In particular, **every** division in a six-cycle is by precisely five, never by a higher power.

It remains to solve the six linear recurrence equations. For support `001011`, the first two give \(a_2=a_0+a_1\) and \(a_3=a_0+2a_1\). The remaining equations give \(a_0=a_1\), hence the unique positive rational ray is \((1,1,2,3,1,4)\). For support `001101`, the analogous equations give \(2a_0=7a_1\), hence the unique positive rational ray is \((7,2,9,11,4,3)\). Both primitive tuples have gcd one, so every positive integral solution on either ray is a positive integral multiple. As every term of a periodic word is a five-adic unit, the multiplier is coprime to five.

Conversely, direct substitution shows that the cyclic sums for the first primitive tuple, in order, are \((2,3,5,4,5,5)\), and for the second they are \((9,11,20,15,7,10)\). Removing all factors of five produces exactly the next cyclic terms, and multiplication by a five-adic unit preserves every division exponent. Neither word repeats at a smaller period. Thus all and only the asserted six-cycles occur.

Finally, for any positive periodic five-free orbit, division by its gcd's largest power of two does not change the recurrence, and it produces at least one odd term. Modulo two the recurrence becomes the Fibonacci update on a nonzero state, whose least period is three. Hence every positive cycle length is divisible by three. Our two six-periodic words have least period six, and the classification excludes period three, proving that no shorter positive cycle exists.

## Verification

The accompanying dependency-free `VERIFY.py` proves the displayed symbolic trace identity coefficientwise in a six-variable integer polynomial ring; checks the complete 64-state rotation-support table; confirms the strict all-six-exponent bound and the two polynomial forms; verifies both cycles' exact five-adic divisions; and computes rank five for both six-equation rational systems. Run with `python3 VERIFY.py`. This finite certificate supplies the exhaustive binary-support step and independent arithmetic checks; the inequalities and linear-algebra argument above provide the unbounded proof.

## Relationship to prior work

Avila and Khovanova, *Free Fibonacci Sequences* (first public arXiv version March 18, 2014), introduce and analyze this exact recurrence. Their Section 9 displays both primitive six-cycles, establishes an elementary common-divisor normalization, and states that they found no additional cycles; it does not establish an exhaustive six-period classification. Their Lemma 28 restricts lengths of cycles for odd divisors to multiples of three, but leaves six-cycle uniqueness unresolved. OEIS A214684 (entry originating July 25, 2012) tabulates the first primitive cycle, not the complete set of primitive periodic pairs. The new conclusion is an exhaustive theorem, not a new example or a consequence of those observations.

## Limitations

Only positive periodic words of period dividing six are classified. Longer primitive cycles may exist, and neither convergence to cycles nor divergence for general initial pairs is decided. The completeness proof combines a 64-state exhaustive finite support calculation with analytical monotonicity and exact linear recurrences; checking finitely many initial pairs would not establish it. Independent mathematical review has not been performed.

## References

1. B. Avila and T. Khovanova, *Free Fibonacci Sequences*, arXiv:1403.4614v1 (March 18, 2014), especially Sections 2 and 9. https://arxiv.org/abs/1403.4614
2. B. Avila and T. Khovanova, *Free Fibonacci Sequences*, Journal of Integer Sequences 17 (2014), Article 14.8.5. https://cs.uwaterloo.ca/journals/JIS/VOL17/Avila/avila4.html
3. OEIS A214684, *Five-free Fibonacci numbers*, initial entry July 25, 2012. https://oeis.org/A214684
