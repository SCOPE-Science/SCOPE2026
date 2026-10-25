# Exact producer-weight equilibrium polynomial for exact-two public-goods games on prism networks

## Finding
For each integer \(n\ge3\), let \(G_n=C_n\square K_2\) have vertices \((i,s)\) for \(i\in\mathbb Z/n\mathbb Z\) and \(s\in\{0,1\}\), with edges along each cycle row and across each rung. Every player chooses a binary action. Its unique best response is action 1 (production) if and only if precisely two of its three neighbors choose action 1. Count distinct labeled pure Nash equilibria by number of producing agents. Their exact producer-count polynomial is
\[
P_n(z)=\sum_{j=0}^{\lfloor n/4\rfloor}\frac{n}{n-3j}\binom{n-3j}{j}z^{4j}+2z^n+4\mathbf1_{4\mid n}z^{3n/2}.
\]
The last summand is absent unless \(4\mid n\). In particular, \(P_4(z)=1+6z^4+4z^6\) and \(P_8(z)=1+8z^4+6z^8+4z^{12}\). The number \(P_n(1)\) grows exponentially, with leading rate equal to the unique real root \(\lambda>1\) of \(\lambda^4-\lambda^3-1=0\).

## Assumptions and scope
All vertices and rungs are labeled; each row is a simple \(n\)-cycle, with \(n\ge3\). There are no loops, no asynchronous dynamics assumptions, and no indifference in best responses. A pure Nash equilibrium is precisely an assignment where every player performs its specified unique best response to the three neighbors. The parameter \(z\) marks producers rather than social welfare, and \(\mathbf1_{4\mid n}\) is 1 when 4 divides \(n\) and 0 otherwise.

## Proof
Encode a rung's two binary actions as \(b=(b_0,b_1)\in\{0,1\}^2\). For consecutive rung words \((a,b,c)\), define the local-admissibility predicate
\[
\Phi(a,b,c)=\prod_{s=0}^1\mathbf1\!\left\{b_s=\mathbf1\{a_s+c_s+b_{1-s}=2\}\right\}.
\]
Index a sixteen-state transfer matrix \(T(z)\) by ordered pairs \((a,b)\in(\{0,1\}^2)^2\). The only allowed transition \((a,b)\to(b,c)\) has weight \(z^{b_0+b_1}\Phi(a,b,c)\). Then every length-\(n\) closed walk corresponds bijectively to a labeled cyclic rung assignment obeying all equilibrium equations, and it is weighted by the number of producing vertices. Thus
\[P_n(z)=\operatorname{tr}(T(z)^n)\qquad(n\ge3).\]
A direct determinant identity for this explicitly defined 16-by-16 integer-polynomial matrix is
\[
\det(I-tT(z))=(1-tz)^2(1-z^6t^4)(1-t-z^4t^4). \tag{1}
\]
One fully reproducible exact algebraic proof of (1) is included in `verify_prism.py`: the code computes the determinant by the fraction-free Bareiss algorithm and compares it with the displayed product at all integer pairs \((t,z)\in\{0,1,\ldots,16\}\times\{0,1,\ldots,32\}\). Each side has degree at most 16 in \(t\) and 32 in \(z\) (the matrix has 16 entries in each determinant term, each of producer degree at most 2). Success at these 561 grid points proves the polynomial identity over the rationals by successive univariate interpolation; it is not a conjectural finite-size extrapolation. The program asserts all exact divisions in the determinant algorithm.

For formal power series in \(t\), the general trace-determinant identity gives
\[
\sum_{n\ge1}P_n(z)t^n=-t\frac{\partial}{\partial t}\log\det(I-tT(z)).
\]
The factor \((1-tz)^2\) contributes \(2z^n\) to \(P_n(z)\), and \((1-z^6t^4)\) contributes \(4z^{3n/2}\) if \(4\mid n\), zero otherwise. Finally
\[
-\log(1-t-z^4t^4)=\sum_{r\ge1}\frac{(t+z^4t^4)^r}{r}.
\]
Writing \(j\) for the count of quartic terms and \(r-j\) for the count of linear terms gives degree \(n=r+3j\), hence coefficient \(\binom{n-3j}{j}/(n-3j)\) in the logarithm; multiplication by \(n\) produces the claimed summand. All denominators \(n-3j\) are positive for the indicated range and \(n\ge3\).

For asymptotic growth, at \(z=1\), the last factor has reciprocal roots given by \(\lambda^4-\lambda^3-1=0\). Its companion nonnegative matrix is primitive, because the allowed cycle lengths 3 and 4 have gcd 1. The corresponding positive Perron root \(\lambda>1\) is strictly larger in modulus than all other roots. The other two determinant factors contribute a bounded quantity \(2+4\mathbf1_{4\mid n}\). Thus \(P_n(1)\sim\lambda^n\).

## Verification
Execute `python3 verify_prism.py` in a directory containing that standalone script. It first performs all 561 exact integer determinant comparisons, which certify equation (1) for every complex \(t,z\) by degree bounds. It then independently enumerates all \(349504\) binary profiles over prism networks with \(3\le n\le9\), checks each individual best-response equality directly, and compares the resulting weighted histograms with the formula. Additional displayed values are obtained from the closed form, not asserted to be exhaustive beyond \(n=9\). The transfer-matrix determinant certificate, not those profile samples, establishes the all-size theorem.

## Relationship to prior work
Klimm and Stahlberg (2023), arXiv:2301.11849, introduce and study the complexity of binary public-goods games using per-player binary best-response patterns, including general decreasing patterns and a particular nonmonotone pattern. Their inspected manuscript does not provide the producer-weight equilibrium polynomial of this exact-two rule on prism graphs. The literature's reduction of other game patterns to algebraic constraints is not claimed as new. A related earlier calculation of even-neighbor (parity) equilibrium counts on ladder networks applies a distinct affine best-response pattern and does not imply this exact-two classification. The finite-state transfer-matrix technique is standard; the claim concerns its explicit factorization and complete producer-count law for this particular economically motivated family.

## Limitations
Only strict pure best responses, the exact-two response pattern, and simple labeled prism networks of at least three rungs are covered. This does not establish convergence of asynchronous updates, mixed-equilibrium counts, or welfare optimality. A closely equivalent enumeration might occur in combinatorial transfer-matrix literature under another name; lack of a search match cannot establish absolute novelty. The determinant computation is an exact finite identity certificate, whereas the small-network exhaustive checks alone cannot prove the infinite statement.

## References
1. M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, first public January 27, 2023, arXiv:2301.11849, https://arxiv.org/abs/2301.11849 .
2. Gilboa and Nisan, *The Complexity of Public Goods Games on Networks*, arXiv:2207.04238, https://arxiv.org/abs/2207.04238 (related foundations of general response-pattern models).
