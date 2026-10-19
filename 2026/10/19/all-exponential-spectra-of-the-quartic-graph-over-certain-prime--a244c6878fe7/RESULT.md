# All exponential spectra of the quartic graph over certain prime-square rings

## Finding

Let \(p\ge5\) be prime and \(p\equiv2\pmod3\), and let \(R=\mathbb Z/p^2\mathbb Z\). The quartic graph
\[
S_p=\{(x,x^4):x\in R\}\subset R^2
\]
has the following **complete** family of orthogonal exponential bases. A subset \(\Lambda\subset R^2\) of cardinality \(p^2\) is a spectrum of \(S_p\) if and only if there are a unique residue \(c\in\{0,\ldots,p-1\}\) and a unique function \(\beta:\mathbb F_p\to\mathbb F_p\) such that
\[
\Lambda=\Lambda_{c,\beta}=\big\{\big(a,c+p\beta(a\bmod p)\big):a\in R\big\}.
\]
Consequently there are exactly \(p^{p+1}\) distinct labeled frequency spectra. Precisely \(p^3\) of them are affine lines over \(R\) that project bijectively onto the first coordinate; the remaining \(p^{p+1}-p^3\) are nonlinear frequency graphs. In particular, choosing \(\beta(r)=r^2\) produces a nonlinear spectral basis for every such prime.

## Assumptions and scope

All frequencies and points lie in the finite additive abelian group \(R^2\). The character at frequency \((a,b)\) is
\[
\chi_{a,b}(u,v)=\exp\!\left(\frac{2\pi i(au+bv)}{p^2}\right).
\]
A spectrum is a **set** of exactly \(|S_p|=p^2\) pairwise orthogonal restrictions of these characters to \(S_p\), with the counting inner product. There is no quotient by translations, dilations, or linear equivalences in the enumeration. Expressions such as \(a\bmod p\) designate the reduction map to \(\mathbb F_p\); the second frequency coordinate uses the fixed integer representative \(c\) from the indicated range.

## Proof

**1. A complete zero-set lemma.** Define \(F(a,b)=\sum_{x\in R}\chi_{a,b}(x,x^4)\). We first prove that \(F(a,b)=0\) precisely when
\[
\big(b\equiv0\pmod p,\ a\not\equiv0\pmod p\big)
\quad\text{or}\quad
\big(b=0\text{ in }R,\ a\equiv0\pmod p,\ a\ne0\text{ in }R\big).
\tag{1}
\]
If at least one of \(a,b\) is not divisible by \(p\), write \(x=r+ps\) for \(r,s\in\mathbb F_p\), using standard representatives. Exact binomial expansion modulo \(p^2\) gives
\[
F(a,b)=p\!\sum_{\substack{r\in\mathbb F_p\\a+4br^3\equiv0\pmod p}}
 \exp\!\left(\frac{2\pi i(ar+br^4)}{p^2}\right).
\tag{2}
\]
Because \(p\equiv2\pmod3\), cubing permutes \(\mathbb F_p\), and because \(p\ne2\), equation \(a+4br^3=0\) has exactly one root when \(b\not\equiv0\pmod p\). Thus (2) is nonzero in that case. When \(b\equiv0\pmod p\) and \(a\not\equiv0\pmod p\), there are no roots and (2) is zero.

It remains to analyze \(a=pA,b=pB\), with \(A,B\in\mathbb F_p\). Then
\[
F(pA,pB)=p\sum_{r\in\mathbb F_p}\exp\!\left(\frac{2\pi i(Ar+Br^4)}p\right).
\tag{3}
\]
A sum of exactly \(p\) powers of a primitive \(p\)-th root vanishes if and only if all \(p\) exponents occur once: its nonnegative integer count polynomial of degree below \(p\) must be a multiple of the minimal polynomial \(1+X+\cdots+X^{p-1}\). Hence (3) vanishes exactly when \(r\mapsto Ar+Br^4\) permutes \(\mathbb F_p\).

**2. The quartic permutation obstruction.** We show that for \(p\equiv2\pmod3\), a polynomial \(Br^4+Ar\) permutes \(\mathbb F_p\) if and only if \(B=0\) and \(A\ne0\). Write \(p=6h+5\) with \(h\ge0\) and set
\[
u=\left\lceil\frac h2\right\rceil,\qquad j=3u+1,\qquad k=2h+1-u.
\]
Direct substitution (separating even and odd \(h\)) shows \(1\le j<p-1\), \(0\le k\le j\), \(j+3k=p-1\), and \(4j<2(p-1)\). Expanding and using the power-sum identity \(\sum_{r\in\mathbb F_p}r^m=-1\) for positive \(m\) divisible by \(p-1\) and zero otherwise, yields
\[
\sum_{r\in\mathbb F_p}(Br^4+Ar)^j
=-\binom jk B^k A^{j-k}\quad\text{in }\mathbb F_p.
\tag{4}
\]
No other binomial term can have a positive exponent divisible by \(p-1\), because exponents are \(j+3t\) for \(0\le t\le j\) and lie strictly between \(0\) and \(2(p-1)\). Since \(j<p\), the binomial coefficient is nonzero. If \(h\) is even, \(j=k\), and (4) is nonzero whenever \(B\ne0\). If \(h\) is odd, \(j-k=2\), and it is nonzero whenever \(AB\ne0\). Finally, if \(A=0\) and \(B\ne0\), the map \(r\mapsto Br^4\) fails to be injective since \(p-1\) is even. A permutation would have zero \(j\)-th power sum for \(1\le j<p-1\); all \(B\ne0\) cases are thereby excluded. The case \(B=0\) is a permutation exactly when \(A\ne0\). Combined with (2)-(3), this proves (1) without numerical assumptions.

**3. Structure and count of spectra.** For distinct \((a,b),(a',b')\in\Lambda\), character orthogonality on the graph is equivalent to \(F(a-a',b-b')=0\). Formula (1) forces all second coordinates \(b\) to have the same reduction \(c\) modulo \(p\). Moreover, for any two frequencies whose first coordinates are congruent modulo \(p\), formula (1) forces their second coordinates to be **equal in \(R\)**. Within each residue class of first coordinates, there are therefore at most \(p\) distinct possible frequencies. A spectrum contains \(p^2\) frequencies and has \(p\) possible first-coordinate residue classes. Thus every class contains exactly \(p\) frequencies, their first coordinates exhaust that entire class in \(R\), and the second coordinate is constant on each class, of the form \(c+p\beta(r)\). This proves necessity and uniqueness of the stated parametrization.

Conversely, any two distinct points of \(\Lambda_{c,\beta}\) with different first-coordinate residues have difference satisfying the first alternative in (1), while any two with the same first-coordinate residue have difference satisfying the second. Hence its \(p^2\) character restrictions are orthogonal and form a basis. There are \(p\) choices of \(c\) and \(p^p\) functions \(\beta\), giving \(p^{p+1}\) distinct spectra.

An affine line over \(R\) projecting bijectively onto the first coordinate must have a second-coordinate function \(b(a)=d+ta\). Its reduction modulo \(p\) is constant, forcing \(t\equiv0\pmod p\). Thus \(t=pT\), and such a line appears exactly when \(\beta(r)=D+Tr\), where \(D,T\in\mathbb F_p\). There are \(p^2\) such functions and \(p\) choices of \(c\), hence \(p^3\) affine spectra. The function \(r\mapsto r^2\) is not affine on \(\mathbb F_p\) for \(p\ge5\), furnishing nonaffine examples.

## Verification

Run `python3 check_quartic.py` using only the Python standard library. The script independently computes exact Fourier zeros by comparing integer coefficient counts modulo the cyclotomic polynomial \(\Phi_{p^2}\) for \(p\in\{5,11,17\}\). It verifies every one of the \(p^4\) frequency differences, a nonlinear spectrum for each tested prime, and the binomial moment obstruction for \(p\in\{5,11,17,23\}\). See `check_quartic.stdout` for the reproduced output. Finite checks corroborate the symbolic proof; only the latter establishes the infinitely many-prime statement.

## Relationship to prior work

The Fourier restriction framework for residue rings in Hickman and Wright (2018) concerns harmonic analysis modulo arbitrary integers but does not classify spectral bases of this quartic graph. Shi (2019) establishes a spectral-set theorem for the different ambient group \(\mathbb Z_{p^2}\times\mathbb Z_p\) and develops general Fourier-zero/equidistribution methods; it does not settle the present group \(R^2\) or its exact quartic frequency spectra. Related calculations for cubic and quadratic polynomial graphs at prime-square order do not imply the quartic permutation obstruction in step 2; the cubic graph can have additional admissible non-horizontal slopes. The exact quartic spectrum count and nonlinear graph classification are the distinguishing assertions.

## Limitations

The argument assumes primes \(p\ge5\) satisfying \(p\equiv2\pmod3\). No claim is made for primes \(p\equiv1\pmod3\), for modulus \(p^k\) with \(k>2\), or for a generic quartic polynomial. The proof classifies character frequencies for the graph in the stated coordinates, not its tilings or arbitrary spectral-set classifications. No assertion of independent external verification is made; bibliographic equivalence with an unindexed polynomial-graph treatment remains possible.

## References

- Jonathan Hickman and James Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176, initially public 2018-01-09. https://arxiv.org/abs/1801.03176
- Ruxi Shi, *Equi-distributed property and spectral set conjecture on \(\mathbb Z_{p^2}\times\mathbb Z_p\)*, arXiv:1906.11717, initially public 2019-06-27. https://arxiv.org/abs/1906.11717
