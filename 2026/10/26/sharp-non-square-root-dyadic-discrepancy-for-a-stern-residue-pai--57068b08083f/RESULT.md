# Sharp non-square-root dyadic discrepancy for a Stern residue pair modulo nine

## Finding
Define Stern's diatomic sequence by \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\) for \(n\ge1\). For each integer \(k\ge0\), write
\[
C_k=\#\{0\le n<2^k:(s(n),s(n+1))\equiv(1,2)\pmod 9\}.
\]
Then
\[
\limsup_{k\to\infty}\left|C_k-\frac{2^k}{72}\right|^{1/k}=\rho=1.439066724563126\ldots>\sqrt2,
\]
where \(\rho\) is the common modulus of the two roots of largest absolute value of
\[
q(X)=X^6+2X^5+3X^4+2X^3+X^2+3.
\]
In particular the discrepancy is \(O(k\rho^k)\), and it is *not* \(O((\sqrt2)^k)\); the optimal exponent in a dyadic root-growth sense is \(\log_2\rho=0.5251334864\ldots\), strictly greater than one-half. The limit superior is deliberately used: no uniform lower bound at every \(k\) is asserted.

## Assumptions and scope
All counts are over ordinary nonnegative integers and simultaneous consecutive Stern values modulo exactly \(9\). A dyadic level \(k\) represents precisely the half-open initial interval \([0,2^k)\), not arbitrary intervals \([0,N)\). All spectral algebra is over rational integers, so the root-growth conclusion is independent of floating-point eigensolvers. The density \(1/72\) is established in prior work; the contribution here is its exact sharp dyadic discrepancy exponent for one specified nonzero primitive residue pair.

## Proof
Let \(V\) be the \(72\) ordered pairs \((a,b)\in(\mathbb Z/9\mathbb Z)^2\) with \(\gcd(a,b,9)=1\). The Stern identities give the two transitions
\[
U_0(a,b)=(a,a+b),\qquad U_1(a,b)=(a+b,b)\pmod9.
\]
Let the integer matrix \(M\), indexed by \(V\), have \(M_{v,w}\) equal to the number of these two transitions from \(v\) to \(w\). Starting with \((s(0),s(1))=(0,1)\), induction on binary digits gives
\[
C_k=e_{(0,1)}^{\mathsf T}M^k e_{(1,2)}.
\]
Both transitions permute \(V\); hence every row and every column sums to \(2\). The characteristic polynomial, computed **exactly over \(\mathbb Z\)** by the accompanying standalone checker, factors as
\[
\begin{aligned}
P(X)={}&X^{14}(X-2)(X-1)^{17}(X+1)^6\\
&\cdot(X^2-2X+2)^2(X^2+X+2)^3 q(X)^2h(X)^2,
\end{aligned}
\]
with
\[
h(X)=X^6-X^5+X^4-X^3+2X^2-4X+8.
\]
The checker constructs each entry of \(M\) from the two explicit rules, computes this characteristic polynomial by exact symbolic arithmetic, and checks equality with the displayed factors.

The factor \(X-2\) is simple. Since every row and column sums to \(2\), its left and right eigenvectors are constant and its rank-one spectral projection is the all-ones matrix divided by \(72\). The eigenvalue \(2\) thus contributes exactly \(2^k/72\) to \(C_k\). To bound the other eigenvalues strictly, use the following **rational root-location certificates**. Each displayed Gaussian rational center is obtained by dividing the listed real and imaginary integer coordinates by \(100000\):
\[
\begin{aligned}
q:&\quad(-118967,\pm75338),\;(-38416,\pm138684),\;(57383,\pm63346),\\
h:&\quad(-104307,\pm95499),\;(28600,\pm138499),\;(125707,\pm64790).
\end{aligned}
\]
Each disk of radius \(1/1000\) about a specified center contains exactly one root of the corresponding polynomial. Here is the exact verification argument implemented in the checker. For every center \(c\), direct rational evaluation gives \(|p(c)|<1/1000\) and \(|p'(c)|>10\). On \(|z-c|=1/1000\), using \(|c|<3/2\), the sum of Taylor terms of orders at least two is bounded by
\[
\sum_{j=2}^{\deg p}\sum_{l=j}^{\deg p}|p_l|{l\choose j}(3/2)^{l-j}(1/1000)^j<1/1000.
\]
Therefore the linear term has modulus \(>1/100\), while the other terms have combined modulus \(<1/500\); Rouché's theorem proves one root per disk. All six disks for either polynomial are mutually disjoint, so each list locates all six roots. Rational squared-modulus comparisons give a dominant conjugate pair of \(q\)-roots of modulus \(\rho\) in \((1.438,1.441)\), while every other root of \(q\) and of \(h\) has modulus \(<1.416\). The remaining factors have roots of modulus at most \(\sqrt2\). Thus the only roots with modulus \(\rho\) are the two displayed dominant conjugates, and every non-Perron eigenvalue has modulus at most \(\rho\).

It remains to establish that the dominant factor is actually seen by the scalar counting sequence: a matrix's characteristic polynomial alone cannot do so. First, \(q\) is irreducible in \(\mathbb Q[X]\), as certified by the irreducibility of its reduction modulo \(17\). Define \(R(X)=P(X)/q(X)^2\) and let \(E\) act on scalar sequences by \((EC)_k=C_{k+1}\). Exact integer matrix powering, using only the transition rules, gives the nonzero certificate
\[
(R(E)C)_0=116619264\neq0.
\]
Consequently the minimal annihilating polynomial of \((C_k)\) is not a divisor of \(R\). Because it divides \(P\), it must contain \(q\) as a factor. Its rationality and irreducibility of \(q\) imply that the scalar generating function has contributions from **all** six conjugate roots of \(q\), in particular those of modulus \(\rho\). Removing the simple \(2\)-eigenmode does not remove \(q\). The standard root-growth identity for nonzero linear recurrences (equivalently, Cauchy–Hadamard applied to the reduced rational generating function) now gives the asserted limsup \(\rho\). Repeated factors may add polynomial factors in \(k\), absorbed in \(O(k\rho^k)\). This completes the proof.

## Verification
Run the bundled \(\texttt{check\_stern9.py}\) with Python 3 and SymPy. The program independently constructs all \(72\) states, verifies the transfer matrix and polynomial factorization exactly, checks the reduction of \(q\) modulo \(17\), evaluates the nonzero scalar certificate, applies rational Rouché bounds to all twelve roots, and directly enumerates Stern pairs for dyadic levels \(0\le k<12\). The program printed PASS when run on the bundled file. The root-location inequalities and polynomial equalities are exact, not tests of approximate eigenvalues; the initial dyadic counts are illustrative checks only.

## Relationship to prior work
Deshouillers and Schinzel proved the modular joint distribution of consecutive Stern values and described the finite-state automaton, including the uniform density over primitive residue pairs (2019, DOI below). Their inspected full eight-page paper does not specify the present modulus-nine characteristic factor, sharp dyadic discrepancy exponent, or the nonzero scalar mode certificate. Bettin, Drappeau, and Spiegelhofer study a different distributional statistic of Stern values—normality of their logarithms—with a transfer-operator viewpoint; their preprint first appeared on 18 April 2017. Neither result implies this explicit pair-count spectral statement. Standard finite-automaton transfer matrices are used as a method, but no qualitative Perron–Frobenius statement alone determines the claimed sharp rate. Comparisons with accessible prior claims and relevant mathematical-record searches found no equivalent result; this is not a certification of publication priority.

## Limitations
Only the fixed residue pair \((1,2)\) modulo \(9\) and dyadic initial blocks are treated. The result does not give sharp error bounds for arbitrary \(N\), a single constant multiplying \(\rho^k\), or a classification of other moduli/pairs. The exact certificate requires SymPy for reproducibility; the mathematical proof states the certificate computations explicitly. Earlier unindexed work or an indirect implication from a general spectral classification remains an originality risk. Independent mathematical audit has not been performed.

## References
- J.-M. Deshouillers and A. Schinzel, “The modular distribution of Stern's sequence,” *Banach Center Publications* 118 (2019), 37–44, DOI: 10.4064/bc118-3. Full text: https://www.impan.pl/shop/en/publication/transaction/download/product/113097
- S. Bettin, S. Drappeau, and L. Spiegelhofer, “Statistical distribution of the Stern sequence,” arXiv:1704.05253, publicly submitted 18 April 2017; *Commentarii Mathematici Helvetici* 94 (2019), 241–271. DOI: 10.4171/CMH/460. https://arxiv.org/abs/1704.05253
