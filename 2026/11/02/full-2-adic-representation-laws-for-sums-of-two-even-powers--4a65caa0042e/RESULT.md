# Full \(2\)-adic representation laws for sums of two even powers

## Finding

Let \(k\ge4\) be **any even integer**. Write \(s=\nu_2(k)\), \(h=s+2\), and \(K=2^{s+1}\). For integers \(r\ge1\) and \(0\le a<2^r\), define the ordered representation multiplicity

\[
R_{k,r}(a)=\#\{(x,y)\in(\mathbb Z/2^r\mathbb Z)^2:x^k+y^k\equiv a\pmod{2^r}\}.
\]

This gives **every fiber size**, for every even exponent and every dyadic modulus, by the following complete recurrence. Set \(R_{k,0}(0)=1\). For \(r=1\), \(R_{k,1}(0)=R_{k,1}(1)=2\). For \(2\le r<h\), the only nonzero values occur at \(a=0,1,2\), where they are respectively

\[
R_{k,r}(0)=2^{2r-2},\qquad R_{k,r}(1)=2^{2r-1},\qquad R_{k,r}(2)=2^{2r-2}.
\]

For every \(r\ge h\), the exhaustive rule is

\[
R_{k,r}(a)=
\begin{cases}
2^{s+1+r},&a\equiv1\pmod{2^h},\\
2^{s+r},&a\equiv2\pmod{2^h},\\
2^{2(k-1)}R_{k,r-k}(a/2^k),&r\ge k\text{ and }2^k\mid a,\\
2^{2r-2},&h\le r<k\text{ and }a=0,\\
0,&\text{otherwise}.
\end{cases}
\]

The cases do not overlap because \(h\le k\). In particular the rule terminates with an exact nonnegative integer at every input.

Equivalently, let \(X,Y\) be independent Haar-uniform \(2\)-adic integers, and let \(U(C)\) denote normalized additive Haar measure on a nonempty dyadic coset \(C\subset\mathbb Z_2\). The **complete output distribution** is

\[
\boxed{\mathcal L(X^k+Y^k)=\sum_{j=0}^{\infty}4^{-j}\left(\tfrac12 U(2^{jk}(1+2^h\mathbb Z_2))+\tfrac14 U(2^{jk}(2+2^h\mathbb Z_2))\right).}
\]

The disjoint cylinders in this mixture have respective probabilities \(2^{-2j-1}\) and \(2^{-2j-2}\). Consequently, its distribution is absolutely continuous relative to Haar measure \(\lambda\), with density \(2^{s+1+j(k-2)}\) on the first cylinder and \(2^{s+j(k-2)}\) on the second. The point \(0\) has probability zero. The measure of the **representable \(2\)-adic output set** is exactly

\[
\boxed{\lambda(\operatorname{image}(x^k+y^k))=\frac{2^{1-h}}{1-2^{-k}}.}
\]

The output-law assertion and the finite-fiber assertion are two forms of the same classification, not separate independent claims.

## Assumptions and scope

All residues and representations are taken in \(\mathbb Z/2^r\mathbb Z\); zero summands and ordered pairs are allowed. Here \(k\) is an arbitrary fixed even integer at least four, \(r\) any positive integer, and \(a\) any residue modulo \(2^r\). The exponent is allowed to have an odd factor. The \(2\)-adic law is on all of \(\mathbb Z_2\) with normalized Haar probability, with no conditioning on primitivity. No assertion concerns integer solutions to \(x^k+y^k=a\) in the ordinary integers.

## Proof

**1. Uniform odd powers.** For every \(r\ge3\), the unit group modulo \(2^r\) consists of \(\pm5^t\) for \(0\le t<2^{r-2}\). Indeed, \(\nu_2(5^{2^j}-1)=j+2\) for all \(j\ge0\), proving that \(5\) generates the subgroup of units congruent to \(1\pmod4\); multiplying by \(-1\) gives every odd unit. Since \(k\) is even and \(s=\nu_2(k)\), for every \(r\ge h=s+2\) the map \(u\mapsto u^k\) on odd residues has kernel size \(2^{s+1}=K\), with image the full additive congruence class \(1+2^h(\mathbb Z/2^r\mathbb Z)\). Its fibers all have exactly \(K\) elements. Thus a Haar-uniform odd \(2\)-adic integer raised to the \(k\)-th power is Haar-uniform on the additive cylinder \(1+2^h\mathbb Z_2\).

**2. The three parity cases.** Since \(k\ge h\), every even \(z\) has \(z^k\equiv0\pmod{2^h}\). The disjoint events that \((X,Y)\) have opposite parity, are both odd, or are both even have probabilities \(1/2,1/4,1/4\), respectively. In the first event the output is uniform on \(1+2^h\mathbb Z_2\), since adding an independent element of \(2^k\mathbb Z_2\) preserves its uniform distribution. In the second event the output is uniform on \(2+2^h\mathbb Z_2\), by convolution with an independent uniform element of \(2^h\mathbb Z_2\). In the third event, writing \(X=2X'\) and \(Y=2Y'\), the pair \((X',Y')\) is again independent Haar-uniform and the output is \(2^k(X'^k+Y'^k)\). This proves the renewal identity

\[
\mu_k=\tfrac12U(1+2^h\mathbb Z_2)+\tfrac14U(2+2^h\mathbb Z_2)+\tfrac14(\times2^k)_*\mu_k.
\]

Iterating it gives the displayed mixture. The omitted remainder has mass \(4^{-j}\) after \(j\) iterations and therefore vanishes; the total probability is \(\sum_{j\ge0}(1/2+1/4)4^{-j}=1\). The two cylinders at any given level have valuations \(jk\) and \(jk+1\), so all displayed cylinders are mutually disjoint.

**3. Finite-fiber rule.** For \(r\ge h\), if one variable is odd and the other even, a fiber exists exactly when \(a\equiv1\pmod{2^h}\). Choosing the even variable in \(2^{r-1}\) ways and then the odd variable in \(K\) ways, and accounting for both orders, gives \(2^rK=2^{s+1+r}\). If both variables are odd, the fiber exists exactly when \(a\equiv2\pmod{2^h}\); choose the first odd variable in \(2^{r-1}\) ways and then the other in \(K\) ways, giving \(2^{s+r}\). If both are even and \(r<k\), their sum vanishes modulo \(2^r\), giving exactly \(2^{2r-2}\) representations of zero. If both are even and \(r\ge k\), they contribute only when \(2^k\mid a\). Write \(x=2u,y=2v\), with \(u,v\) each modulo \(2^{r-1}\). The congruence becomes \(u^k+v^k\equiv a/2^k\pmod{2^{r-k}}\), and each lower solution lifts in precisely \(2^{k-1}\) ways for each coordinate. Thus its contribution is \(2^{2(k-1)}R_{k,r-k}(a/2^k)\). These are all cases. For \(r<h\), odd powers are \(1\) and even powers \(0\) modulo \(2^r\), so counting the four parity combinations gives the stated small-modulus initialization, with the separate \(r=1\) collision of residues \(0\) and \(2\).

**4. Densities.** The normalized Haar measure of either cylinder \(2^{jk}(c+2^h\mathbb Z_2)\) is \(2^{-jk-h}\). Dividing its mixture mass by that measure gives the two displayed Radon–Nikodym densities. Their total integral is one, so there is no residual singular or atomic mass. The cylinders cover the image of \(x^k+y^k\) on \(\mathbb Z_2^2\) except the point zero, which belongs to the image but has Haar measure zero. Summing their Haar measures gives \(2\sum_{j\ge0}2^{-jk-h}=2^{1-h}/(1-2^{-k})\). This completes the proof.

## Verification

Run the standalone Python 3 artifact `verify.py` with no external dependencies: `python3 verify.py`. Its first check enumerates the power-residue multiplicities and computes the exact circular self-convolution for every even exponent in \(\{4,6,8,10,12,14,20\}\) and every modulus \(2^r\) with \(1\le r\le10\), checking **all** residue fibers against the recurrence and checking the mass \(\sum_aR_{k,r}(a)=2^{2r}\). Independent nested pair enumeration also checks small cases. Direct enumeration is finite corroboration only; the algebraic group argument and exhaustive parity decomposition prove all exponents and moduli.

As an example, for \(k=4\) the image occupies Haar measure \(2/15\). The full distribution, unlike its support measure, records the exact unequal fiber weights on the congruence cylinders \(1\) and \(2\) modulo \(16\) and on all their dyadic rescalings.

## Relationship to prior work

Arias, Borja, and Anaya (2023), particularly Proposition 14, Theorem 24, and Proposition 26, study the number \(\alpha(2^r)\) of output residues *having at least one representation* for \(x^k+y^k\), including explicit cases \(k=4\) and \(k=6\). Their statistic is the support cardinality \(\#\{a:R_{k,r}(a)>0\}\). That statistic cannot determine the values of the fibers or the probability weights, whereas the present law does determine their statistic as a corollary. The earlier paper of Arias, Borja, and Rubio (2019) treats images of modular polynomial maps, particularly sums of squares, likewise not the even-exponent dyadic fiber distribution. Zhao, Zhao, and Niu (2020) enumerate quartic solutions over finite fields of **odd** characteristic; their result does not address \(\mathbb Z/2^r\mathbb Z\).

## Limitations

This result counts representations modulo powers of two, not representations of fixed positive integers by ordinary integer powers. The exponent \(k=2\), odd exponents, other primes, and more than two summands are excluded. The class probabilities in the \(2\)-adic mixture are singularly concentrated at large valuations, but no finite probability mass is assigned to zero. A full bibliographic priority claim is not made: general local-zeta or \(2\)-adic pushforward formulas could encode an equivalent statement not identified in the inspected literature. The finite verifier is not a substitute for the infinite proof or an independent external audit.

## References

1. F. Arias, J. Borja, and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), article 23.8.1, first published 2023-08-28. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.html
2. F. Arias, J. Borja, and L. Rubio, *Counting Integers Representable as Images of Polynomials Modulo n*, Journal of Integer Sequences **22** (2019), article 19.6.7; arXiv:1812.11599. https://arxiv.org/abs/1812.11599
3. J. Zhao, Y. Zhao, and Y. Niu, *On the number of solutions of two-variable diagonal quartic equations over finite fields*, AIMS Mathematics **5** (2020), 2979–2991, DOI:10.3934/math.2020192. https://doi.org/10.3934/math.2020192
