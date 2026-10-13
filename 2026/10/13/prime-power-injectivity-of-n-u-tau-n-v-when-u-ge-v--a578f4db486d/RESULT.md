# Prime-power injectivity of \(n^u\tau(n)^v\) when \(u\ge v\)
## Finding
For all positive integers \(u,v\) with \(u\ge v\), define
\[
F_{u,v}(n)=n^u\tau(n)^v,
\]
where \(\tau(n)\) is the number of positive divisors of \(n\). Then \(F_{u,v}\) is injective on positive prime powers. Explicitly, for primes \(p,q\) and integers \(a,b\ge1\),
\[
F_{u,v}(p^a)=F_{u,v}(q^b)
\]
implies \(p=q\) and \(a=b\).

The parameter condition cannot simply be removed. For every integer \(t\ge1\),
\[
F_{t,3t}(2^6)=\left(2^6\,7^3\right)^t=21952^t
=\left(7^3\,4^3\right)^t=F_{t,3t}(7^3).
\]
Thus the full parameter ray \(v=3u\) is noninjective on prime powers.

## Assumptions and scope
All variables \(u,v,a,b\) are positive integers, \(u\ge v\), and \(p,q\) are primes. The domain being classified is the set of prime powers \(p^a\) with \(a\ge1\). No claim is made that \(u\ge v\) is necessary for prime-power injectivity for every individual parameter pair; the displayed ray \(v=3u\) shows that unrestricted extension to all positive \(u,v\) is false.

## Proof
For a prime power,
\[
\tau(p^a)=a+1,
\]
so
\[
F_{u,v}(p^a)=p^{au}(a+1)^v.
\]
Suppose
\[
p^{au}(a+1)^v=q^{bu}(b+1)^v. \tag{1}
\]

First assume \(p=q\). For fixed \(p,u,v\), the sequence \(p^{au}(a+1)^v\) is strictly increasing in \(a\), because the ratio of consecutive terms is
\[
p^u\left(\frac{a+2}{a+1}\right)^v>1.
\]
Thus \(a=b\).

Now assume \(p\ne q\). From (1), the factor \(p^{au}\) divides \((b+1)^v\). Hence
\[
v\,\nu_p(b+1)\ge au.
\]
Since \(u\ge v\),
\[
\nu_p(b+1)\ge \left\lceil\frac{au}v\right\rceil\ge a,
\]
and therefore
\[
p^a\mid b+1,\qquad p^a\le b+1.
\]
By symmetry,
\[
q^b\mid a+1,\qquad q^b\le a+1.
\]
Multiplying,
\[
p^a q^b\le(a+1)(b+1). \tag{2}
\]

For every prime \(r\) and integer \(e\ge1\),
\[
r^e\ge2^e\ge e+1.
\]
The second inequality follows by induction, and equality throughout \(r^e=e+1\) is possible only for \((r,e)=(2,1)\). Thus
\[
p^a q^b\ge(a+1)(b+1). \tag{3}
\]
Comparing (2) and (3), equality must hold in both factors. Consequently
\[
(p,a)=(2,1),\qquad(q,b)=(2,1),
\]
contradicting \(p\ne q\). Hence distinct prime bases cannot collide, and the equal-base case already gave \(a=b\). This proves the claim.

For the counter-ray, the base equality
\[
F_{1,3}(2^6)=2^6(6+1)^3=64\cdot343=21952
=343\cdot64=7^3(3+1)^3=F_{1,3}(7^3)
\]
persists after scaling both parameters by any \(t\ge1\), because
\[
F_{t,3t}(n)=F_{1,3}(n)^t.
\]

## Verification
The bundled `verify.py` independently evaluates all parameter pairs with \(1\le v\le u\le6\), all primes below \(100\), and exponents \(1\le a\le20\). It confirms that no two tested prime powers collide and checks the elementary inequality \(2^a\ge a+1\) through \(a=100\). It also verifies ten instances of the exact noninjective ray \(v=3u\), whose base collision value is \(21952\). The recorded output is:

`VERIFY_OK parameter_pairs=21 prime_power_values=10500 stored_values=10500 inequality_checks=100 boundary_collision=21952`

These finite checks are regression tests only. The universal result rests on the valuation and inequality argument above.

## Relationship to prior work
Gabdullin, Iudelevich, and Luca study the image of \(k\mapsto k\tau(k)\), prove its counting order, and explicitly note the global collision \(18\tau(18)=27\tau(27)\). Their full text does not state a restricted injectivity theorem for prime powers. Noppakaew and Pongsriiam define \(D(n)=n\tau(n)\), exhibit the collision \(D(18)=D(27)\), and leave primitive collisions as a problem. In the same paper, Theorem 13 proves that \(n^u\tau(n)^v\) is injective on squarefree integers for every positive \(u,v\). Prime powers of exponent greater than one are not squarefree, so that theorem does not imply the present result. The present statement gives a complementary infinite restricted-injectivity class for the full parameter region \(u\ge v\), and includes \(D\) as \((u,v)=(1,1)\).

OEIS A338382 records values having multiple preimages under \(n\mapsto n\tau(n)\), including collisions in which one preimage may be a prime power, but it does not classify collisions between two prime powers. Exact web and semantic searches for prime-power injectivity, the equivalent equation \(p^{au}(a+1)^v=q^{bu}(b+1)^v\), and aliases using \(d(n)\) returned no implication-equivalent theorem. The closest indexed records concern products with Jordan totients or compositions with divisor-function iterates, which are different functions.

## Limitations
The theorem gives a sufficient parameter region \(u\ge v\); it does not classify which pairs with \(u<v\) are injective on prime powers. The explicit \((1,3)\) collision proves only that a theorem covering every positive pair \((u,v)\) would be false. A broad older reference on divisor-function collision problems cited by OEIS was not inspected in full, leaving a small residual literature risk under different terminology.

## References
1. M. R. Gabdullin, V. V. Iudelevich, and F. Luca, “Numbers of the form \(kf(k)\),” arXiv:2201.09287v1, submitted January 23, 2022.
2. P. Noppakaew and P. Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” *Journal of Integer Sequences* 26 (2023), Article 23.9.1. Published November 2, 2023. Primary MSC 11A25.
3. OEIS A338382, “Numbers \(m\) such that the equation \(m=k\tau(k)\) has more than one solution.”
4. OEIS A000005, divisor-counting function \(\tau(n)\).
