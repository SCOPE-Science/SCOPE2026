# Four exact prime-density classes for eight-divisible orders of split elliptic curves

## Finding
Let \(E/\mathbb Q\) be an elliptic curve given by
\[
E: y^2=(x-r_1)(x-r_2)(x-r_3),\qquad r_1<r_2<r_3,\quad r_i\in\mathbb Q.
\]
For odd primes \(p\) of good reduction, let \(N_p=\#E(\mathbb F_p)\). The natural density of primes for which \(8\mid N_p\) exists and belongs to the **complete four-value spectrum**
\[
\boxed{\left\{\tfrac12,\tfrac58,\tfrac34,1\right\}}.
\]
All four values occur: respectively, the curves \(y^2=x(x-2)(x-4)\), \(y^2=x(x-2)(x-5)\), \(y^2=x(x-1)(x-3)\), and \(y^2=x(x-9)(x-25)\) attain them. The integer model associated with the \(D(8)\)-triple \(\{1,8,17\}\), namely
\[
Y^2=(X+1088)(X+136)(X+64),
\]
has density \(3/4\).

## Assumptions and scope
All three roots are distinct rationals. Multiplication by a rational square and an integral change of variables yield good integral models outside finitely many primes; excluding those primes does not change natural densities. Define the strictly positive rational differences
\[
\alpha=r_2-r_1,\qquad \beta=r_3-r_2,\qquad \gamma=r_3-r_1=\alpha+\beta.
\]
Let \(R\le(\mathbb F_2)^3\) be the relation space
\[
R=\{(e_1,e_2,e_3)\in\{0,1\}^3:\alpha^{e_1}\beta^{e_2}\gamma^{e_3}\in\mathbb Q^{\times2}\}.
\]
Here an exponent triple is also encoded by the integer \(k=e_1+2e_2+4e_3\) between \(0\) and \(7\). No claim is made for non-split cubics or for density questions at higher powers of two.

## Proof
**1. Point-order reduction to halving rational two-torsion.** For an odd good prime, all four points of \(E[2]\) are rational over \(\mathbb F_p\), so \(4\mid N_p\). The finite abelian group \(E(\mathbb F_p)\) has two-primary subgroup of rank exactly two: it contains \((\mathbb Z/2)^2\), and an elliptic curve in odd characteristic has only four geometric two-torsion points. Thus \(8\mid N_p\) exactly when it contains an element of order four; doubling such an element produces a nonzero two-torsion point.

For a split cubic over a field of odd characteristic, the classical two-descent halving criterion says that \((r_i,0)\) is twice a rational point if and only if both \(r_i-r_j\) and \(r_i-r_k\), for \(\{i,j,k\}=\{1,2,3\}\), are squares in that field (Bekker--Zarhin, Theorem 2.1). With the Legendre character \(\chi_p\) let
\[
a=\chi_p(\alpha),\quad b=\chi_p(\beta),\quad c=\chi_p(\gamma),\quad m=\chi_p(-1).
\]
The three possible halving conditions are respectively \((ma=mc=1)\), \((a=mb=1)\), and \((b=c=1)\). Therefore
\[
8\mid N_p\quad\Longleftrightarrow\quad
(ma=1\wedge mc=1)\ \vee\ (a=1\wedge mb=1)\ \vee\ (b=1\wedge c=1).\tag{1}
\]
In the middle condition \(r_2-r_1=\alpha\) and \(r_2-r_3=-\beta\); the other two conditions have the analogous signs. This verifies the sign normalization in (1).

**2. Frobenius signs and their exact frequencies.** The multiquadratic field \(L=\mathbb Q(\sqrt\alpha,\sqrt\beta,\sqrt\gamma)\) has degree \(2^{3-\dim R}\). Its Galois character triples \((a,b,c)\in\{\pm1\}^3\) are exactly those satisfying
\[
a^{e_1}b^{e_2}c^{e_3}=1\quad\text{for every }(e_1,e_2,e_3)\in R.
\]
Because \(\alpha,\beta,\gamma>0\), the field \(L\) is totally real. Hence \(i\notin L\), and adjoining \(i\) gives an independent sign \(m\in\{\pm1\}\). The abelian form of Chebotarev's density theorem (equivalently, the corresponding multiquadratic-character equidistribution theorem) makes all \(2^{4-\dim R}\) permissible quadruples \((a,b,c,m)\) equally frequent among unramified rational primes. Equation (1) therefore proves the existence of the natural density and evaluates it by counting the successful sign quadruples.

**3. Exhaustive classification of relation spaces.** There are exactly \(16\) vector subspaces of \((\mathbb F_2)^3\): one zero subspace, seven lines, seven planes, and the full space. Directly inserting their character constraints into (1) produces the following exhaustive finite table (the notation for a relation space lists the integer codes of all its members):

| Relation space(s) \(R\) | Density |
| --- | --- |
| \(\{0\}\) | \(5/8\) |
| \(\{0,1\},\{0,2\},\{0,4\},\{0,5\},\{0,6\}\) | \(3/4\) |
| \(\{0,3\},\{0,7\}\) | \(1/2\) |
| \(\{0,1,2,3\},\{0,1,6,7\},\{0,2,5,7\},\{0,3,5,6\}\) | \(3/4\) |
| \(\{0,1,4,5\},\{0,2,4,6\}\) | \(1\) |
| \(\{0,3,4,7\}\) | \(1/2\) |
| \(\{0,1,2,3,4,5,6,7\}\) | \(1\) |

For instance, when \(R=\{0\}\), ten of sixteen \((a,b,c,m)\) quadruples meet (1), giving \(5/8\); when \(R=\{0,3,4,7\}\), two of four permissible quadruples do, giving \(1/2\). This list is exhaustive independently of whether every abstract relation space is realized by positive \(\alpha,\beta,\gamma=\alpha+\beta\).

**4. Attainment.** For the four curves listed in the Finding section, \((\alpha,\beta,\gamma)\) equals \((2,2,4)\), \((2,3,5)\), \((1,2,3)\), and \((9,16,25)\), respectively. Their relation spaces are, in order, \(\{0,3,4,7\}\), \(\{0\}\), \(\{0,1\}\), and all eight codes. Thus their densities are \(1/2,5/8,3/4,1\), proving the entire asserted spectrum.

For the recent \(D(8)\)-triple example, the roots are \(-1088,-136,-64\), so \((\alpha,\beta,\gamma)=(952,72,1024)\). The first two numbers have independent nonsquare rational classes, while \(1024\) is a rational square. Therefore \(R=\{0,4\}\), and the density is \(3/4\). \(\square\)

## Verification
The standalone script `checker.py` enumerates **all sixteen** binary relation subspaces; explicitly counts their admissible quadratic-character patterns and the successes of (1); checks the four realization models and the \(D(8)\) example; and independently compares (1) against exact elliptic-curve point counts for every odd good prime at most \(1031\). It tests \(852\) curve-prime pairs and finishes with `CERTIFICATE_OK`. The sixteen-subspace enumeration certifies a finite combinatorial step; the assertion about infinitely many primes uses the proof of Chebotarev equidistribution, not those finite point counts.

## Relationship to prior work
Chuysurichay, Jaidee, Panraksa, and Sukhonwimolmal (2026, arXiv:2610.03121v1) record \(1640\) specific prime reductions of curves associated with \(D(n)\)-triples. They explicitly note that their bounded census supplies no asymptotic density. They prove the general four-divisibility and provide the roots of the worked \(D(8)\)-example. Bekker and Zarhin (2017, arXiv:1702.02255) give the two-divisibility criterion used in step 1; that result does not state the classified prime-density spectrum. Gekeler (2006) averages group-structure probabilities over varying elliptic curves over finite prime fields, rather than fixing one rational curve and varying its primes. The distinct new assertion here is the exhaustive four-value classification of \(\delta_8(E)\), with realization of every value and an exact density for the motivating example.

## Limitations
The proof assumes three rational roots, only tests divisibility by eight, and gives no rate of convergence of the prime proportions. The same theorem may be derivable from previously known more general torsion-image or multiquadratic splitting-density frameworks, even if an exact four-value formulation was not found. No claim is made about cryptographic security, prime subgroup factors, higher two-power divisibility, or stronger conditional asymptotics.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa, and T. Sukhonwimolmal, *Split-Cubic Curves from \(D(n)\)-Triples: A Bounded Finite-Field Census*, arXiv:2610.03121v1 (first public 2026-10-02), https://arxiv.org/html/2610.03121v1.
2. M. Bekker and Yu. G. Zarhin, *The divisibility by 2 of rational points on elliptic curves*, arXiv:1702.02255 (2017), https://arxiv.org/abs/1702.02255.
3. E.-U. Gekeler, *The distribution of group structures on elliptic curves over finite prime fields*, Documenta Mathematica 11 (2006), 119–142, DOI 10.4171/DM/206.
4. Chebotarev density theorem, specialized to composita of quadratic extensions of \(\mathbb Q\) (standard input to step 2).
