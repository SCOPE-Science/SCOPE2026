# The last exceptional prime in quadratic three-dimensional inverted Kloosterman distinctness

## Finding
For every prime \(p\equiv1\pmod4\) with \(p>9\), put \(F=\mathbb F_{p^2}\), and for \(b\in F^\times\) define the three-dimensional inverted Kloosterman sum
\[
\operatorname{IK}_3(p^2,b)=\sum_{\substack{x_1,x_2,x_3,x_4\in F^\times\\x_1x_2x_3x_4=b\\x_1+x_2+x_3+x_4\ne0}}\zeta_p^{\operatorname{Tr}_{F/\mathbb F_p}((x_1+x_2+x_3+x_4)^{-1})},
\]
where \(\zeta_p=e^{2\pi i/p}\). Then, for all \(b,c\in F^\times\),
\[
\operatorname{IK}_3(p^2,b)=\operatorname{IK}_3(p^2,c)
\quad\Longleftrightarrow\quad c\in\{b,b^p\}.
\]
Its algebraic degree over \(\mathbb Q\) is \((p-1)/4\) when \(\operatorname{Tr}_{F/\mathbb F_p}(b)\ne0\), and \((p-1)/\gcd(8,p-1)\) when the trace is zero. Exactly \((p^2+p-2)/2\) different values occur as the nonzero parameter varies. The genuinely new case is \(p=73\); for that characteristic, the degrees are respectively \(18\) and \(9\), and there are exactly \(2700\) values.

## Assumptions and scope
All primes satisfy \(p>9\) and \(p\equiv1\pmod4\). No claim is made for other characteristics or higher extension degrees. The equality is equality of cyclotomic algebraic integers, not merely equal absolute values. The prior distinctness theorem of Kyselov excludes primes dividing
\[
D_4=2(5)^4-\binom84^2=-3650=-2\cdot5^2\cdot73.
\]
Under the present congruence and size conditions, the only excluded prime is \(73\). Thus only this one characteristic requires a new argument.

## Proof
Fix \(p=73\), let \(F=\mathbb F_{73^2}\), and suppose two sums are equal. Put \(x=b^{-1}\) and \(y=c^{-1}\). Proposition 4.1 of Kyselov (arXiv:2610.25443v1, Section 4) applies whenever \(4\mid p-1\), including \(p=73\). It implies that, for any \(1\le k<(p-1)/4=18\), equality of the two sums forces
\[
\lambda_k(4)\bigl(\operatorname{Tr}(x^k)-\operatorname{Tr}(y^k)\bigr)=0\quad\text{in }\mathbb F_{73},
\]
where \(\lambda_k(4)=[T^k]\log f_4(T)\) and
\[
f_4(T)=\sum_{j\ge0}a_jT^j,\qquad a_j=\frac{((1/4)_j)^4}{((4j)!)^2},\qquad (1/4)_j=\prod_{s=0}^{j-1}(1/4+s).
\]
Every denominator used through degree six is invertible modulo \(73\). Computing the coefficients by \(ka_k=\sum_{j=1}^k j\lambda_j a_{k-j}\), with \(a_0=1\), gives for \(k=0,1,2,3,4,5,6\) respectively
\[
(a_k\bmod73)=(1,18,16,72,25,38,12),\qquad
(\lambda_k\bmod73)=(0,18,0,49,25,52,56).
\]
In particular the coefficients at indices \(1,3,4,6\) are units, despite the vanishing of \(\lambda_2\). Consequently the power traces of \(x\) and \(y\) agree in those four degrees.

Let \(u=\operatorname{Tr}(x)=\operatorname{Tr}(y)\). If \(u\ne0\), set \(N_x=x x^{73}\), \(N_y=y y^{73}\). Since characteristic \(73\ne3\), the identity
\[
\operatorname{Tr}(x^3)=u^3-3uN_x
\]
(and its analogue for \(y\)) together with equality of the cubic traces gives \(N_x=N_y\). Hence \(x\) and \(y\) have the same characteristic polynomial \(X^2-uX+N_x\) over \(\mathbb F_{73}\), so \(y\in\{x,x^{73}\}\).

If \(u=0\), the trace-zero subspace of \(F\) is one-dimensional over \(\mathbb F_{73}\). Thus \(y=tx\) for some \(t\in\mathbb F_{73}^{\times}\). Since \(x^{73}=-x\), both \(x^4\) and \(x^6\) are nonzero elements of \(\mathbb F_{73}\). The fourth- and sixth-power trace identities then imply \(t^4=t^6=1\), so \(t^2=1\) and \(y=x\) or \(y=-x=x^{73}\). Therefore in either case \(c=b\) or \(c=b^{73}\). Conversely, Frobenius substitution in the defining sum gives equality for Frobenius-conjugate parameters (Kyselov, Eq. (1.3)). This proves the omitted characteristic.

For every other prime in the stated family, \(p\nmid D_4\), so Kyselov's Theorem 1.1 proves the same equality criterion. Combining it with the new \(p=73\) case establishes the all-prime assertion. For the degree, the Galois action \(\sigma_a(\operatorname{IK}_3(p^2,b))=\operatorname{IK}_3(p^2,ba^{-4})\) and the just-established equality criterion give stabilizer size \(\gcd(4g_b,p-1)\), where \(g_b=1\) if the trace is nonzero and \(g_b=2\) if it vanishes (cf. Kyselov, Proposition 5.1). Hence the two degree formulas follow. Frobenius orbits on \(F^\times\) consist of \(p-1\) singletons and \((p^2-p)/2\) pairs, giving \((p^2+p-2)/2\) distinct sums.

## Verification
The accompanying `verify_exception73.py` uses only the Python standard library. It computes rational coefficients \(a_k\) and \(\lambda_k\) exactly through \(k=6\) and independently recomputes them directly modulo \(73\). It models \(\mathbb F_{73^2}\) as \(\mathbb F_{73}[u]/(u^2-5)\), verifies that \(5\) is a nonsquare, and exhaustively checks that the four-trace signatures for all \(5328\) nonzero elements distinguish exactly \(2700\) Frobenius orbits. It also checks Galois-stabilizer sizes \(4\) and \(8\). Invoke `python3 verify_exception73.py`; successful execution ends with `CERTIFICATE_OK`. These finite checks validate the arithmetic and orbit-recovery step; they do not independently reprove the published p-adic trace-recovery proposition.

## Relationship to prior work
Kyselov, *Distinctness and algebraic degrees of inverted Kloosterman sums* (arXiv:2610.25443v1, first public October 18, 2026), proved the general quadratic-extension criterion under \(p\nmid D_d\) and its algebraic-degree consequences. In the case \(d=4\), that theorem does not cover \(p=73\). The present argument uses its Proposition 4.1 without the nonvanishing hypothesis on \(\lambda_2\), recovering the missing orbit through traces in degrees \(1,3,4,6\). Lin and Wan, *On algebraic degrees of inverted Kloosterman sums* (arXiv:2407.16229v1), prove their complete degree result for prime fields \(q=p\), and explicitly leave proper extensions as a further question. Lin, *Distinctness of the generalized n-dimensional Kloosterman sums* (arXiv:2607.04177v1), studies a different family of generalized sums with a polynomial/Laurent-polynomial phase. Earlier work of Lin and Wan, *On inverted Kloosterman sums over finite fields* (arXiv:2301.04287v1), supplies complex and \(p\)-adic estimates, not this quadratic parameter classification.

## Limitations
The result relies on Kyselov's published formal trace-recovery proposition for the implication from equality of the inverted sums to equality of selected power traces. Its internal proof is not reproduced here. The new elementary argument resolves only the unique exceptional characteristic within the stated \(d=4\), quadratic-extension theorem; no claim about other dimensions, extension degrees or arbitrary primes is made. The arithmetic certificate is exhaustive for the stated field, but is not a direct evaluation of each inverted Kloosterman sum. Earlier unindexed equivalent arguments cannot be ruled out by literature search alone. Independent mathematical verification has not been performed.

## References
1. Danyil Kyselov, *Distinctness and algebraic degrees of inverted Kloosterman sums*, arXiv:2610.25443v1 (2026), https://arxiv.org/html/2610.25443v1; specifically Theorem 1.1, Proposition 4.1, Proposition 5.1, and Remark 6.2.
2. Xin Lin and Daqing Wan, *On algebraic degrees of inverted Kloosterman sums*, arXiv:2407.16229v1 (2024), https://arxiv.org/html/2407.16229v1; specifically Theorem 1.2 and the open extension-field question.
3. Xin Lin, *Distinctness of the generalized n-dimensional Kloosterman sums*, arXiv:2607.04177v1 (2026), https://arxiv.org/html/2607.04177v1.
4. Xin Lin and Daqing Wan, *On inverted Kloosterman sums over finite fields*, arXiv:2301.04287v1 (2023), https://arxiv.org/abs/2301.04287.
