# Three exact 2-adic image balls for all iterated Chebyshev doubling maps

## Finding

Define \(f(X)=X^2-2\) and \(F_r=f^{\circ r}\), for every integer \(r\ge2\). These are first-kind Dickson polynomials: \(F_r(X)=D_{2^r}(X,1)=2T_{2^r}(X/2)\). Let the integer centers \(c_r\) be given by \(c_2=194\) and \(c_{r+1}=c_r^2-2\).

For every \(r\ge2\), there is an exact disjoint union of three full balls in the ring of 2-adic integers:

\[
F_r(\mathbb Z_2)=\left(-1+2^{r+2}\mathbb Z_2\right)\sqcup\left(2+2^{2r+3}\mathbb Z_2\right)\sqcup\left(c_r+2^{2r+5}\mathbb Z_2\right).
\]

The third center satisfies \(\nu_2(c_r-2)=2r+2\), so the two even balls are distinct, although their residues coincide at lower precision. In particular, if \(V(r,k)\) denotes the number of distinct values of \(F_r\) modulo \(2^k\), then for every integer \(k\ge1\),

\[
V(r,k)=2^{\max(0,k-r-2)}+\begin{cases}1,&k\le2r+2,\\2^{\max(0,k-2r-3)}+2^{\max(0,k-2r-5)},&k\ge2r+3.\end{cases}
\]

For all \(k\ge2r+5\) this yields the exact, stabilized density

\[
\frac{V(r,k)}{2^k}=2^{-r-2}+2^{-2r-3}+2^{-2r-5}.
\]

The nested images also satisfy \(\bigcap_{r\ge2}F_r(\mathbb Z_2)=\{-1,2\}\).

## Assumptions and scope

All statements are for the fixed integer polynomial \(f(X)=X^2-2\), iteration orders \(r\ge2\), and moduli \(2^k\) with \(k\ge1\). The codomain \(\mathbb Z_2\) denotes 2-adic integers and \(a+2^m\mathbb Z_2\) is a full residue ball, not merely an upper bound on the image. Image cardinalities are counts of distinct output residues, not numbers of input preimages. There is no assumption about primality of the input or about an asymptotic limit in place of finite-level equality.

## Proof

**1. Two surjectivity facts.** The squares of odd 2-adic integers are exactly \(1+8\mathbb Z_2\). Necessity is immediate modulo eight. Conversely, if an odd square is constructed modulo \(2^j\) for \(j\ge3\), switching a chosen square root \(z\) to \(z+2^{j-1}\) changes its square by \(2^jz\) modulo \(2^{j+1}\); since \(z\) is odd, one may choose the next binary digit of the target. This recursive lifting produces a 2-adic square root of every element of \(1+8\mathbb Z_2\).

If \(a\) is odd and \(b\) is even, then \(u\mapsto au+bu^2\) permutes \(\mathbb Z_2\). Indeed,
\[
(au+bu^2)-(av+bv^2)=(u-v)\left(a+b(u+v)\right),
\]
whose second factor is odd. Therefore the map is an isometry modulo every \(2^j\), hence bijective at every finite level and on the inverse limit \(\mathbb Z_2\).

**2. The base at fourfold Dickson degree.** Direct expansion gives \(F_2(X)=X^4-4X^2+2\). Every 2-adic input belongs to exactly one of the classes: odd; twice an odd; four times an odd; or divisible by eight.

For odd \(x\), write \(x^2=1+8u\) with arbitrary \(u\in\mathbb Z_2\). Then
\[
F_2(x)=-1+16(-u+4u^2),
\]
so this class has image exactly \(-1+16\mathbb Z_2\).

For \(x=2t\) with odd \(t\), write \(t^2=1+8u\). Then
\[
F_2(2t)=2+128(u+8u^2),
\]
whose image is exactly \(2+128\mathbb Z_2\).

For \(x=4v\) with odd \(v\), write \(v^2=1+8u\). Then
\[
F_2(4v)=194+512(7u+32u^2),
\]
whose image is exactly \(194+512\mathbb Z_2\).

Finally, for \(x=8w\),
\[
F_2(8w)=2+256w^2(16w^2-1)\in2+128\mathbb Z_2.
\]
This proves the asserted complete three-ball decomposition at \(r=2\). The balls are disjoint because one consists of odd numbers and the other two have centers differing by \(192\), of 2-adic valuation six, less than the shallower even-ball exponent seven.

**3. Exact propagation of balls.** For \(m\ge4\) and odd \(a\),
\[
f(a+2^m u)=a^2-2+2^{m+1}\left(au+2^{m-1}u^2\right).
\]
By step 1, \(f(a+2^m\mathbb Z_2)=a^2-2+2^{m+1}\mathbb Z_2\) exactly. For \(a\equiv2\pmod8\) and \(m\ge7\),
\[
f(a+2^m u)=a^2-2+2^{m+2}\left(\frac a2u+2^{m-2}u^2\right),
\]
with odd linear and even quadratic coefficients. Thus this even ball maps exactly onto \(a^2-2+2^{m+2}\mathbb Z_2\).

The three base centers are \(-1\), \(2\), \(c_2=194\), with \(f(-1)=-1\), \(f(2)=2\), and \(f(c_r)=c_{r+1}\). As \(c_r\equiv2\pmod8\), the first ball gains one exponent per iteration and the other two gain two exponents per iteration. Induction yields precisely the claimed exponents \(r+2\), \(2r+3\), and \(2r+5\), proving equality and surjectivity of all three balls for every \(r\ge2\).

Furthermore,
\[
c_{r+1}-2=(c_r-2)(c_r+2).
\]
Since \(\nu_2(c_2-2)=\nu_2(192)=6\) and \(c_r\equiv2\pmod8\) implies \(\nu_2(c_r+2)=2\), induction gives \(\nu_2(c_r-2)=2r+2\). This is strictly less than each of the even-ball exponents, so their disjointness is exact.

**4. Exact reduction and cardinality.** Every polynomial image over \(\mathbb Z/2^k\mathbb Z\) is exactly the reduction of its image over \(\mathbb Z_2\), by compatibility and surjectivity of the reduction on inputs. A ball \(a+2^m\mathbb Z_2\) reduces to one residue when \(k\le m\) and to \(2^{k-m}\) residues when \(k>m\). The odd ball is disjoint from both even balls at every precision. Because \(\nu_2(c_r-2)=2r+2\), the two even balls reduce to the same single residue for \(k\le2r+2\). For \(k\ge2r+3\), they have disjoint reductions. Adding their counts gives the displayed piecewise formula, including all boundary values of \(k\).

For \(k\ge2r+5\), all three ball counts have stabilized at their geometric sizes, giving the asserted density formula. Since \(\nu_2(c_r-2)\to\infty\), the two even balls contract toward \(2\); the odd ball contracts toward \(-1\). These two points are fixed by \(f\), belong to every image, and no other 2-adic number belongs to every image. This proves the final intersection identity.

## Verification

The accompanying standalone Python 3 script `verify_dickson_2adic_images.py` uses no dependencies. It computes the iterated polynomial from its defining recurrence, directly enumerates all input residues and compares the complete image SET (not merely cardinality) against the three predicted balls for every \(2\le r\le9\) and \(1\le k\le16\), and for \(2\le r\le5\) and \(k\in\{17,18\}\). It also checks the center valuation through \(r=14\) and exact density arithmetic. On the checked package the output is:

```
VERIFY_OK grid_cases= 128 deep_cases= 8 maximum_r=14 maximum_direct_modulus=262144 image_sets_exact=True density_arithmetic=True
```

These finite tests do not establish the infinite theorem; steps 1--4 supply the unrestricted proof and its exact boundaries.

## Relationship to prior work

Classical first-kind Dickson polynomials and their compositional identity \(D_m(D_n(X,1),1)=D_{mn}(X,1)\) are known. Chou--Gomez-Calderon--Mullen (1988) determine Dickson value-set cardinalities over **finite fields**, not over 2-power residue rings. Bremser--Gomez-Calderon (1991) investigate Dickson value sets over **Galois rings** and report general estimates and some preimage counts; this is the principal historical-priority risk, because its full text was not available for comparison. Ralph (1995) gives general value-set inequalities over integer residue rings, without an inspected exact value-set decomposition for these iterates. Cheng--Hill--Wan (2011) analyze exact value-set counting algorithms and complexity for finite fields. Qu--Ding (2014) investigate permutation behavior of second-kind Dickson polynomials over integer residue rings, a different invariant and polynomial family. Shang (2023) proves general non-permutation polynomial value-set upper bounds and gives extremal examples; those results do not imply the present exact three-ball calculation. The present claim is specifically the exact three-ball decomposition, all finite-level image counts, and limiting fixed-point image for **first-kind** dyadic iterates. It does not claim to introduce Dickson polynomials or 2-adic lifting methods.

## Limitations

This classification is for the fixed Chebyshev parameter \(1\), iteration degree \(2^r\), and characteristic-zero dyadic residue rings; it does not cover arbitrary Dickson degrees, Galois-ring extensions of higher residue-field degree, other primes, or full fiber multiplicity distributions. The inaccessible full text of Bremser--Gomez-Calderon (1991) leaves a nonzero risk of a hidden equivalent specialization. The result has only self-review; no independent validation has been performed.

## References

1. W. S. Chou, J. Gomez-Calderon, and G. L. Mullen, "Value sets of Dickson polynomials over finite fields," *J. Number Theory* 30 (1988), 334--344. DOI: https://doi.org/10.1016/0022-314X(88)90006-6.
2. P. S. Bremser and J. Gomez-Calderon, "Value sets of Dickson polynomials over Galois rings," *J. Number Theory* 38 (1991), 240--250. DOI: https://doi.org/10.1016/0022-314X(91)90087-R (abstract examined; full text not available).
3. W. J. Ralph, "The value set of polynomials over \(\mathbb Z_m\) and the combinatorics of sequences," *Mathematika* 42 (1995), 190--198. DOI: https://doi.org/10.1112/S0025579300011487.
4. Q. Cheng, J. Hill, and D. Wan, "Counting Value Sets: Algorithm and Complexity," arXiv:1111.1224v1, first public November 4, 2011, https://arxiv.org/abs/1111.1224.
5. Qu and Ding, "Dickson polynomials of the second kind that permute \(\mathbb Z_m\)," *SIAM J. Discrete Math.* (2014), DOI: https://doi.org/10.1137/130942589.
6. S. Shang, "Value sets of non-permutation polynomials over the residue class rings of integers," arXiv:2310.20226v1 (2023), https://arxiv.org/abs/2310.20226.
