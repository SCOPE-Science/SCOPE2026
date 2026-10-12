# Exact prime-conductor index of \(\zeta+c\zeta^{-1}\)
## Finding
Let \(p\) be an odd prime, let \(\zeta\) be a primitive \(p\)-th root of unity, and let \(c\in\mathbb Z\). Put
\[
u_c=\zeta+c\zeta^{-1}.
\]
For every \(c\neq1\), the element \(u_c\) generates the full cyclotomic field \(K=\mathbb Q(\zeta)\), and its order has the exact index
\[
[\mathcal O_K:\mathbb Z[u_c]]
 = |1-c|\,|1-c^p|^{(p-3)/2}.
\]
Hence \(u_c\) is a power-basis generator of \(K\) exactly in the following cases: \(c=0\) for every odd prime \(p\), together with the exceptional case \((p,c)=(3,2)\). For \(c=1\), the element \(u_c=\zeta+\zeta^{-1}\) instead generates the maximal real subfield, so the full-field index formula does not apply.

## Assumptions and scope
The prime \(p\) is odd, \(\zeta\) has exact order \(p\), and \(c\) is an integer. The statement concerns the additive cyclotomic family \(\zeta+c\zeta^{-1}\). No assertion is made here for composite conductor, for nonintegral \(c\), or for the index of \(\mathbb Z[u_c]\) in a proper subfield when \(c=1\).

The motivating 2026 paper studies \(u=\zeta+c\zeta^{-1}\) for general conductor and proves that whenever \(\mathbb Q(u)\) is a proper subfield of \(\mathbb Q(\zeta)\), its ring of integers is \(\mathbb Z[u]\). The result here resolves the complementary full-field case at prime conductor by computing the exact index, rather than only deciding whether the field is proper.

## Proof
For \(1\le a,b\le p-1\), write
\[
u_a=\zeta^a+c\zeta^{-a}.
\]
A direct factorization gives
\[
u_a-u_b=(\zeta^a-\zeta^b)\bigl(1-c\zeta^{-a-b}\bigr).
\]
If \(a\neq b\) and \(u_a=u_b\), then \(c=\zeta^{a+b}\). Since \(c\in\mathbb Z\) and \(\zeta^{a+b}\) is a \(p\)-th root of unity, oddness of \(p\) forces \(c=1\). Thus for \(c\neq1\) the \(p-1\) conjugates \(u_a\) are distinct, so \([\mathbb Q(u_c):\mathbb Q]=p-1\) and \(\mathbb Q(u_c)=K\).

Because \(\mathcal O_K=\mathbb Z[\zeta]\), the discriminant-index identity and the two Vandermonde products give
\[
[\mathcal O_K:\mathbb Z[u_c]]
 =\left|\prod_{1\le a<b\le p-1}
 \frac{u_a-u_b}{\zeta^a-\zeta^b}\right|
 =\left|\prod_{1\le a<b\le p-1}
 \bigl(1-c\zeta^{-a-b}\bigr)\right|.
\]
It remains to count pair sums modulo \(p\). Among unordered two-element subsets of \(\mathbb F_p^\times\), the residue \(a+b=0\) occurs \((p-1)/2\) times, while each fixed nonzero residue occurs \((p-3)/2\) times. Therefore
\[
\prod_{1\le a<b\le p-1}(1-c\zeta^{-a-b})
=(1-c)^{(p-1)/2}
 \prod_{t=1}^{p-1}(1-c\zeta^{-t})^{(p-3)/2}.
\]
For \(c\neq1\), the cyclotomic product identity
\[
\prod_{t=1}^{p-1}(1-c\zeta^t)=\frac{1-c^p}{1-c}
\]
then yields
\[
[\mathcal O_K:\mathbb Z[u_c]]
=|1-c|\,|1-c^p|^{(p-3)/2}.
\]

For \(p=3\), the second exponent is zero, so index one is equivalent to \(|1-c|=1\), namely \(c=0\) or \(c=2\). For \(p\ge5\), index one first forces \(|1-c|=1\), hence \(c\in\{0,2}\); the choice \(c=2\) has \(|1-2^p|>1\), leaving only \(c=0\). Finally, when \(c=1\), complex conjugation identifies \(u_a=u_{-a}\), and the standard real-cyclotomic result gives \(\mathbb Z[\zeta+\zeta^{-1}]=\mathcal O_{\mathbb Q(\zeta+\zeta^{-1})}\).

## Verification
The proof is symbolic and valid for every odd prime. A supplementary exact/computational checker, `verify.py`, independently checks the pair-sum multiplicities for every odd prime below \(100\), the stated index-one classification for a finite parameter box, and numerical Vandermonde ratios for representative primes and coefficients. These checks are consistency tests; they are not substituted for the infinite proof.

## Relationship to prior work
The 2026 paper *Monogenity of the irreducible factors of (k,t)-Fibonacci and (k,t)-Lucas polynomials* introduces the same general element \(u=\zeta+c\zeta^{-1}\). Its Proposition 2.1 proves monogeneity when \(\mathbb Q(u)\) is a proper subfield, and Lemma 2.4 characterizes properness through collisions among conjugates. Its subsequent applications focus on \(c=1\) and \(c=-1\) in root-of-unity situations. The exact prime-conductor index in the complementary full-field case, and the resulting complete classification of which integer \(c\) make this particular \(u_c\) a power-basis generator, are not stated there.

Washington's standard cyclotomic result covers the boundary \(c=1\) by identifying the full ring of integers of the maximal real subfield. Shah and Nakahara study monogenesis for certain index-two imaginary abelian subfields; that setting does not give the full-field index above for arbitrary integer \(c\).

## Limitations
The proof uses primeness of the conductor twice: all nontrivial powers of \(\zeta\) are Galois conjugates, and the pair-sum multiplicities have only the zero/nonzero dichotomy. Composite conductors can have a more complicated orbit structure and are not covered. The literature comparison is targeted rather than exhaustive; an older equivalent formula under different terminology remains a residual bibliographic risk.

## References
1. *Monogenity of the irreducible factors of (k,t)-Fibonacci and (k,t)-Lucas polynomials*, arXiv:2609.38844v1 (2026), especially Proposition 2.1 and Lemma 2.4.
2. L. C. Washington, *Introduction to Cyclotomic Fields*, 2nd ed., Graduate Texts in Mathematics 83, Springer, 1997, Proposition 2.16 as cited in the 2026 paper for the maximal real subfield.
3. S. I. A. Shah and T. Nakahara, *Monogenesis of the rings of integers in certain imaginary abelian fields*, Nagoya Math. J. 168 (2002), 85–92.
