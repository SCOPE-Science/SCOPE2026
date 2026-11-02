# Prime-index Apéry polynomials are irreducible at non-Wieferich primes

## Finding
For every odd prime \(p\) satisfying \(\nu_p(2^{p-1}-1)=1\), every integer \(r\ge2\), and every integer \(s\ge1\) not divisible by \(p\), define
\[
 B_{p,r,s}(X)=\sum_{k=0}^p \binom pk^r\binom{p+k}{k}^{s}X^k.
\]
Then \(B_{p,r,s}\) is irreducible over \(\mathbb Q\). In fact the explicitly scaled affine translation
\[
 H_{p,r,s}(Y)=2^{sp}B_{p,r,s}\bigl((Y-1)/2^s\bigr)
\]
is Eisenstein at \(p\).

In particular, \(B_{p,2,1}\) and \(B_{p,2,2}\) are respectively the two commonly studied Apéry polynomials at prime index \(p\). Thus the theorem establishes their irreducibility at every odd base-two non-Wieferich prime, without assuming or implying that there are infinitely many such primes.

## Assumptions and scope
Here \(p\) is an odd prime, \(r,s\) are ordinary integers with \(r\ge2\), \(s\ge1\), \(p\nmid s\). The arithmetic condition \(\nu_p(2^{p-1}-1)=1\) means that \(2^{p-1}\not\equiv1\pmod{p^2}\); this excludes base-two Wieferich primes such as \(1093\). All polynomials have coefficients in \(\mathbb Z\). The statement treats irreducibility over \(\mathbb Q\) of polynomial families indexed by primes, not integrality, congruences for polynomial values, or composite indices.

## Proof
Put \(q=2^s\) and \(L=\binom{2p}{p}^{s}\). Expanding the substitution gives an integer polynomial
\[
 H(Y)=\sum_{k=0}^p\binom pk^{r}\binom{p+k}{k}^{s}
 q^{p-k}(Y-1)^k.
\]
The initial summand is \(q^p\), the top summand is \(L(Y-1)^p\), and every intermediate summand indexed by \(1\le k\le p-1\) is coefficientwise divisible by \(p^2\), because \(p\mid\binom pk\) and \(r\ge2\).

We first show \(\binom{2p}{p}\equiv2\pmod{p^2}\). The exact rational-product identity
\[
 \binom{2p}{p}=2\prod_{j=1}^{p-1}\left(1+\frac pj\right)
\]
holds in the ring of \(p\)-integral rational numbers. Modulo \(p^2\), the product is \(1+p\sum_{j=1}^{p-1}j^{-1}\). Pairing \(j\) with \(p-j\) proves \(\sum j^{-1}\equiv0\pmod p\) for odd \(p\). Consequently \(L\equiv2^s=q\pmod{p^2}\).

Reducing the explicit expression for \(H\) modulo \(p\) and using the freshman's-dream identity gives
\[
 H(Y)\equiv q^p+L(Y-1)^p
 \equiv q+q(Y^p-1)=qY^p\pmod p.
\]
Because \(p\nmid q\), the leading coefficient \(L\) is a unit modulo \(p\); every nonleading coefficient vanishes modulo \(p\).

The constant term satisfies
\[
 H(0)\equiv q^p-L
 \equiv 2^s\bigl(2^{s(p-1)}-1\bigr)\pmod{p^2}.
\]
Write \(2^{p-1}=1+pc\) with \(p\nmid c\). Since \(p\nmid s\), the binomial theorem yields
\[
 2^{s(p-1)}-1=(1+pc)^s-1\equiv spc\not\equiv0\pmod{p^2}.
\]
Thus \(p\mid H(0)\) and \(p^2\nmid H(0)\). Eisenstein's criterion at \(p\) applies to \(H\), and \(H\) is irreducible over \(\mathbb Q\). The invertible rational affine change \(X=(Y-1)/q\), together with multiplication by \(q^p\ne0\), preserves reducibility and irreducibility over \(\mathbb Q\). Therefore \(B_{p,r,s}\) is irreducible. \(\square\)

## Verification
Run `python3 verify_apery.py` with the Python standard library. The script directly constructs all coefficients of \(B\) and \(H\) for odd primes up to \(43\), exponents \(r\in\{2,3,4\}\), \(s\in\{1,2,3,4,5\}\) with \(p\nmid s\), and tests every Eisenstein coefficient, the constant coefficient modulo \(p^2\), and five independent evaluations of the affine identity. The executable checks also verify the excluded arithmetic boundary at \(p=1093\). The final reproducible output is `CHECK_OK cases=189 coefficients=4350 evaluation_identities=945 Wieferich_boundary_1093=confirmed`.

Finite tests are corroboration only. The universal assertion for all allowable primes and exponents follows from the exact symbolic argument above, not enumeration or a primality conjecture.

## Relationship to prior work
The Apéry polynomial families and weighted-index congruences were studied by Guo and Zeng (arXiv:1101.0983), Sun (arXiv:1101.1946), and Pan (arXiv:1108.1546); those sources concentrate on polynomial congruence sums. Sun explicitly records the general irreducibility conjectures for the \((r,s)=(2,1)\) and \((2,2)\) families in OEIS A005258 and A005259 (comments dated 2013-03-21). The present result proves a stated arithmetic subfamily of **both** conjectures, rather than settling their full assertions. Its arithmetic mechanism is an affine Eisenstein transformation controlled by the base-two Fermat quotient; these particular prime-index conclusions were not identified in the inspected primary sources.

## Limitations
No conclusion is made for prime \(p=2\), base-two Wieferich primes, indices that are not prime, or exponents \(s\equiv0\pmod p\); lack of coverage is not a claim of reducibility. The theorem does not establish the infinitude of non-Wieferich primes. Broader polynomial-irreducibility literature might contain an equivalent instance not found in the source comparison. No independent mathematical audit has been performed.

## References
1. V. J. W. Guo and J. Zeng, *Proof of some conjectures of Z.-W. Sun on congruences for Apéry polynomials*, arXiv:1101.0983, initial public version 2011-01-05, https://arxiv.org/abs/1101.0983.
2. Z.-W. Sun, *Congruences involving Apéry numbers*, arXiv:1101.1946, initial public version 2011-01-10, https://arxiv.org/abs/1101.1946.
3. H. Pan, *On congruences for Apéry polynomials*, arXiv:1108.1546, initial public version 2011-08-07, https://arxiv.org/abs/1108.1546.
4. OEIS A005258, conjectural irreducibility of \(a_n(X)\), comment by Zhi-Wei Sun 2013-03-21, https://oeis.org/A005258.
5. OEIS A005259, conjectural irreducibility of \(A_n(X)\), comment by Zhi-Wei Sun 2013-03-21, https://oeis.org/A005259.
