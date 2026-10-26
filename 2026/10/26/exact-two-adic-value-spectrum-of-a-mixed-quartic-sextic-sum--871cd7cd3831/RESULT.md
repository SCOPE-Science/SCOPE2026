# Exact two-adic value spectrum of a mixed quartic–sextic sum

## Finding

Let \(\mathbb Z_2\) be the ring of two-adic integers and set
\[
\mathcal S=\{x^4+y^6:x,y\in\mathbb Z_2\}.
\]
The following **disjoint** union gives its entire value set:
\[
\begin{aligned}
\mathcal S=\{0\}\ \sqcup\ \bigsqcup_{k\ge0}2^{12k}\big(& (1+8\mathbb Z_2)\sqcup(2+8\mathbb Z_2)\\
&\sqcup 2^4(1+16\mathbb Z_2)\sqcup2^4(5+16\mathbb Z_2)\\
&\sqcup 2^6(1+8\mathbb Z_2)\sqcup2^6(5+8\mathbb Z_2)\\
&\sqcup 2^8(1+16\mathbb Z_2)\big).
\end{aligned}
\]
Consequently, the normalized additive Haar measure of this image, equivalently the limit of the proportions of represented classes modulo \(2^n\), is exactly
\[
\boxed{\mu(\mathcal S)=\lim_{n\to\infty}2^{-n}\#\{r\bmod 2^n:r\equiv x^4+y^6\pmod{2^n}\}=\frac{1073}{4095}.}
\]
Every inclusion and equality is valid over the *full* ring \(\mathbb Z_2\); this is a complete criterion for local solubility of \(x^4+y^6=t\) at the prime two. The displayed union also specifies an exact representation criterion for all finite-power residue classes by reduction.

## Assumptions and scope

The variables \(x,y,t\) range over \(\mathbb Z_2\), and \(k\) ranges over all nonnegative integers. The notation \(a+2^e\mathbb Z_2\) means one additive coset; \(2^j(a+2^e\mathbb Z_2)\) means its image under multiplication by \(2^j\). The measure is normalized by \(\mu(\mathbb Z_2)=1\). Finite congruences permit all residue-class inputs, including zero. No assertion is made about positive integral solutions for every integer in a soluble two-adic coset, or about solubility at other primes.

## Proof

**Unit powers.** For an odd two-adic unit \(u\), its square lies in \(1+8\mathbb Z_2\). Conversely, every member of this coset is an odd square: the usual lifting of a square root from modulus eight changes an arbitrary next bit by replacing an odd approximation \(u\) with \(u+2^{e-1}\) at modulus \(2^{e+1}\), for \(e\ge3\). Therefore odd squares are exactly \(1+8\mathbb Z_2\). Squares of this latter coset are exactly \(1+16\mathbb Z_2\), since
\[
(1+8z)^2=1+16(z+4z^2),
\]
and the function \(z\mapsto z+4z^2\) bijects \(\mathbb Z_2\) by Hensel lifting (derivative \(1+8z\) is odd). Thus odd fourth powers equal \(1+16\mathbb Z_2\). Also odd sixth powers equal \(1+8\mathbb Z_2\): the cube map on \(1+8\mathbb Z_2\) is bijective because its induced equation in the parameter \(z\) has derivative congruent to one modulo two.

**Valuation comparison.** First let \(x,y\ne0\), and write \(x=2^a u\), \(y=2^b v\), with \(a,b\ge0\) and odd units \(u,v\). If \(4a=6b\), there is some \(k\ge0\) such that \(a=3k,b=2k\). Then \(x^4+y^6\) runs through exactly \(2^{12k}(2+8\mathbb Z_2)\): both normalized powers are one modulo eight, and every target is obtained by choosing \(u=1\) and varying \(v\).

If \(4a<6b\), set \(d=6b-4a\), which is an even positive integer. For \(d\ge4\), the normalized sum is in \(1+16\mathbb Z_2\), so it is contained in the pure-fourth-power ball at valuation \(4a\). For \(d=2\), solving \(3b-2a=1\) forces \(a=3k+1,b=2k+1\). Normalizing by \(2^{12k+4}\) gives
\[
u^4+4v^6\in5+16\mathbb Z_2.
\]
Every target in that coset occurs, since one may fix \(v=1\) and vary \(u\). Its valuation is \(12k+4\).

If \(6b<4a\), define \(d=4a-6b\). For \(d\ge4\), the normalized value belongs to \(1+8\mathbb Z_2\), the pure-sixth-power ball at valuation \(6b\). If \(d=2\), the equation \(2a-3b=1\) forces \(a=3k+2,b=2k+1\); the normalized sum is
\[
v^6+4u^4\in5+8\mathbb Z_2.
\]
Again every target occurs by taking \(u=1\) and varying \(v\).

If one input is zero, pure fourth powers have valuations \(4a=12k,12k+4,12k+8\); pure sixth powers have valuations \(6b=12k,12k+6\). The valuation-\(12k\) pure fourth coset is contained in the pure sixth coset. Thus the preceding comparisons yield exactly the seven balls displayed, and no others. Conversely, each ball is achieved using either a zero input or one of the explicitly constructed equal/near-equal valuation pairs. Distinct balls have different valuations or different unit residues, and balls from distinct \(k\) cannot intersect.

**Density.** Haar measure of \(2^a(c+2^b\mathbb Z_2)\) is \(2^{-(a+b)}\), while the singleton zero has measure zero. One block of the seven balls has measure
\[
\frac18+\frac18+\frac1{256}+\frac1{256}+\frac1{512}+\frac1{512}+\frac1{4096}=\frac{1073}{4096}.
\]
Scaling by \(2^{12k}\) and summing the geometric series gives
\[
\mu(\mathcal S)=\frac{1073/4096}{1-2^{-12}}=\frac{1073}{4095}.
\]
Finally, \(\mathcal S\) is compact, hence closed. The finite residue-image sets give its nested clopen cylinder neighborhoods. Their normalized counts decrease to \(\mu(\mathcal S)\) by continuity of Haar measure from above, establishing the asserted limit.

## Verification

The accompanying standalone \(\texttt{verify.py}\) computes the entire residue image of \(x^4+y^6\) independently by direct modular fourth/sixth powers for each modulus \(2^n\), \(1\le n\le16\). It separately reduces the seven listed cosets to each modulus and compares **sets**, not just cardinalities. Every check passes. The image cardinalities for successive exponents are
\[
2,3,3,5,10,18,36,68,136,270,538,1074,2148,4295,8587,17173.
\]
These finite tests confirm the derivation at small moduli; the proof above, rather than finite enumeration, establishes the result for all powers and for \(\mathbb Z_2\).

## Relationship to prior work

Arias, Borja and Rubio (2019) study congruence-value sets of diagonal power polynomials and give general recurrence machinery, applying it explicitly to sums and differences of squares and three squares. Arias, Borja and Anaya (2023) refine congruence-counting techniques and give results for sums/differences of *equal* powers. Their inspected proofs and examples do not provide the seven-coset classification or density for the unequal exponent pair \((4,6)\). The present computation concerns an explicitly identified mixed-exponent gap rather than asserting a new general method for all such polynomials.

## Limitations

This is a local statement over \(\mathbb Z_2\) only. It neither guarantees ordinary integer representations of all two-adically soluble integers nor settles local images at odd primes. The originality comparison covers the cited open-access primary works and targeted mathematical-record searches; an earlier unindexed special-purpose computation cannot be excluded, and independent verification has not been performed.

## References

F. Arias, J. Borja, and L. Rubio, “Counting Integers Representable as Images of Polynomials Modulo n,” *Journal of Integer Sequences* **22** (2019), Article 19.6.7, https://cs.uwaterloo.ca/journals/JIS/VOL22/Borja/borja3.pdf . First preprint arXiv:1812.11599.

F. Arias, J. Borja, and S. Anaya, “Counting Integers Representable as Sums of k-th Powers Modulo n,” *Journal of Integer Sequences* **26** (2023), Article 23.8.1, https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf . Published August 28, 2023.
