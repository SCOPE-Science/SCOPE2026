# Exact fiber spectra of quartic-plus-linear maps over finite fields with a unique cube root

## Finding

Let \(q\) be an odd prime power such that \(q\equiv2\pmod3\), and let \(a\in\mathbb F_q^\times\). Define \(f_a:\mathbb F_q\to\mathbb F_q\) by \(f_a(x)=x^4+ax\). For \(j=0,1,2,3,4\), let
\[
N_j=\#\{y\in\mathbb F_q:\#\{x\in\mathbb F_q:f_a(x)=y\}=j\}.
\]
The complete fiber distribution is independent of \(a\), and is exactly

| \(q\bmod24\) | \(N_0\) | \(N_1\) | \(N_2\) | \(N_3\) | \(N_4\) |
|---|---|---|---|---|---|
| \(5\) | \((3q-7)/8\) | \((q+4)/3\) | \((q-1)/4\) | \(0\) | \((q-5)/24\) |
| \(11\) | \((3q-1)/8\) | \((q+1)/3\) | \((q-3)/4\) | \(1\) | \((q-11)/24\) |
| \(17\) | \((3q-3)/8\) | \((q+1)/3\) | \((q-1)/4\) | \(1\) | \((q-17)/24\) |
| \(23\) | \((3q-5)/8\) | \((q+4)/3\) | \((q-3)/4\) | \(0\) | \((q+1)/24\) |

In particular exactly one target has three preimages when \(-2\) is a square in \(\mathbb F_q\), and none otherwise. The cardinality \(q-N_0\) of the value set in prime fields was already computed by Zhi-Hong Sun; it is not asserted here to be new. The contribution is the full five-entry fiber histogram, including all finite-field extensions allowed by the hypotheses.

## Assumptions and scope

Throughout, \(q=p^r\) is odd and \(q\equiv2\pmod3\), so the characteristic satisfies \(p\ge5\); \(a\ne0\). The integer \(q\) lies in exactly one of the residue classes \(5,11,17,23\pmod{24}\). The map acts on the **whole** field, including zero. All targets \(y\in\mathbb F_q\) are counted, including those with no preimages. The distribution concerns distinct roots, not root multiplicities.

Write \(\chi\) for the quadratic character on \(\mathbb F_q^\times\), and define \(d=\gcd(4,q-1)\) and \(\varepsilon=1+\chi(-2)\in\{0,2\}\).

## Proof

**Step 1 (coefficient normalization).** Since \(\gcd(3,q-1)=1\), the map \(u\mapsto u^3\) permutes \(\mathbb F_q^\times\). Given \(a,b\ne0\), choose \(u\) with \(u^3=b/a\). Then \(f_b(ux)=u^4f_a(x)\). Scaling the input and output bijectively leaves every fiber multiplicity unchanged. Hence the numbers \(N_j\) are common to every nonzero coefficient.

**Step 2 (binomial moments).** For each \(a\), let \(m_a(y)=\#f_a^{-1}(y)\) and
\[
B_k(a)=\sum_{y\in\mathbb F_q}\binom{m_a(y)}k\quad (1\le k\le4).
\]
Thus \(B_1(a)=q\). For distinct \(x,z\), the equation \(f_a(x)=f_a(z)\) uniquely determines \(a\):
\[
a=-(x^3+x^2z+xz^2+z^3).
\]
Counting unordered pairs over all coefficients gives
\[
\sum_{a\in\mathbb F_q}B_2(a)=\binom q2.
\]

For three distinct elements \(x,y,z\), there is a (necessarily unique) coefficient \(a\) and a target \(t\) such that they all solve \(T^4+aT-t=0\) if and only if
\[
Q(x,y,z)=x^2+y^2+z^2+xy+xz+yz=0.
\]
Indeed the fourth root, counted with multiplicity, must be \(w=-x-y-z\); the vanishing of the cubic and quadratic coefficients in \((T-x)(T-y)(T-z)(T-w)\) is equivalent to \(Q=0\), after which the polynomial has the required form. The condition is still valid when \(w\) coincides with one of the first three roots. The nondegenerate ternary quadratic form \(Q\) has \(q^2\) zeros, as follows either from diagonalization or the elementary quadratic Gauss-sum count of odd-dimensional nondegenerate forms.

Inside \(Q=0\), each equality plane \(x=y\), \(x=z\), or \(y=z\) has exactly \(1+\varepsilon(q-1)\) zeros: after substituting \(x=y=t\), the equation becomes \((z+t)^2=-2t^2\). Distinct such equality planes intersect the quadric only at the origin (all three variables equal implies \(Q=6x^2\), and the characteristic is at least five). Their union therefore has \(1+3\varepsilon(q-1)\) points. It follows that
\[
\sum_{a\in\mathbb F_q}B_3(a)=\frac{q^2-1-3\varepsilon(q-1)}6.
\]

For four *distinct* roots, the vanishing of the top two elementary symmetric functions is necessary and sufficient for a common quartic \(T^4+aT-t\). Write \(w=-x-y-z\), so this again amounts to \(Q(x,y,z)=0\). Now there are six pair-equality hyperplanes among \(x,y,z,w\), each cutting the quadric in \(1+\varepsilon(q-1)\) points (symmetry permits reducing each to \(x=y\)). Any two pair-equality hyperplanes have no common nonzero point on the quadric: three equal roots give \(Q=6t^2\), and two equal pairs give \(Q=2t^2\), with \(t\) an appropriate parameter. Thus the union has \(1+6\varepsilon(q-1)\) points, giving
\[
\sum_{a\in\mathbb F_q}B_4(a)=\frac{q^2-1-6\varepsilon(q-1)}{24}.
\]
Each triple or quadruple is divided by its number of orderings, and it is counted once because two distinct roots uniquely determine the coefficient \(a\).

**Step 3 (subtract the zero coefficient).** For \(a=0\), the map is \(x\mapsto x^4\). Its target zero has one preimage, and precisely \((q-1)/d\) nonzero targets have \(d\) preimages. Consequently,
\[
B_k(0)=\frac{q-1}{d}\binom dk\qquad(k=2,3,4).
\]
All \(q-1\) nonzero coefficients have the same moments by Step 1. Subtraction and division therefore give, for any \(a\ne0\),
\[
\begin{aligned}
B_2&=\frac{q-d+1}{2},\\
B_3&=\frac{q+1-3\varepsilon-(d-1)(d-2)}6,\\
B_4&=\frac{q+1-6\varepsilon-(d-1)(d-2)(d-3)}{24}.
\end{aligned}
\]

**Step 4 (recover individual fibers).** Binomial-moment inversion and the identity \(\sum_y m_a(y)=q\) imply
\[
\begin{aligned}
N_4&=B_4,\\ N_3&=B_3-4B_4,\\ N_2&=B_2-3B_3+6B_4,\\
N_1&=q-2B_2+3B_3-4B_4,\\ N_0&=B_2-B_3+B_4.
\end{aligned}
\]
For the four possible residue classes modulo \(24\), the pairs \((d,\varepsilon)\) are respectively \((4,0),(2,2),(4,2),(2,0)\). Substitution yields the stated table and the exact three-preimage dichotomy. This completes the proof for **every** admissible prime power and nonzero coefficient.

## Verification

The accompanying standard-library script `verify.py` independently enumerates actual output multiplicities, without using binomial moments or quadratic-form counts. Run with `python verify.py`. It checks every nonzero coefficient for 15 prime fields (orders \(5,11,17,23,29,41,47,53,59,71,83,89,101,113,137\)), all 124 nonzero coefficients over \(\mathbb F_{125}\), and four selected coefficients over \(\mathbb F_{1331}\). The two cubic extension fields are represented by irreducible cubics checked to have no roots. The observed output was `VERIFY_OK primes= 15 cubic_extensions= [(5, 125, 1, 1, 124), (11, 1331, 1, 4, 4)] histogram=PASS`. Such checks are finite corroboration, not the proof of the universal theorem.

## Relationship to prior work

Zhi-Hong Sun [1], especially displayed formula (1.7), already evaluates \(\#f_a(\mathbb F_p)\) for primes \(p\equiv2\pmod3\); that cardinality is explicitly excluded from the novelty claim. Formula (1.7) does not specify how the represented values are distributed among one-, two-, three- and four-preimage targets. The present classification determines all four nonzero fiber classes and extends them from prime fields to odd prime-power fields with \(q\equiv2\pmod3\).

Matera, Pérez and Privitelli [2], Theorems 1.1–1.3 and their interpolation-set framework, study mean value-set cardinalities and their moments in larger polynomial families. Their hypotheses and conclusions do not give a five-bin histogram for the individual map \(T^4+aT\). Their precursor [3] provides general interpolation tools, rather than this particular complete fiber classification. These are statements of the inspected published results, not claims of exhaustive historical priority.

## Limitations

The classification assumes odd \(q\equiv2\pmod3\) and nonzero \(a\). It does not address fields with \(q\equiv1\pmod3\), even characteristic, or general quartics with quadratic terms. Historical literature may contain an equivalent tabulation or imply it through a stronger polynomial-factorization result not identified here. Independent mathematical review has not been performed.

## References

1. Zhi-Hong Sun, "On the number of incongruent residues of \(x^4+ax^2+bx\) modulo \(p\)," *Journal of Number Theory* **119** (2006), 210–241, doi:10.1016/j.jnt.2005.10.012. First available online 2005-12-15. Full text: https://maths.hytc.edu.cn/__local/F/F9/62/93E0759CBCD3FFD65A5BB7F3767_7DBD24B5_40CB9.pdf.
2. G. Matera, M. Pérez, M. Privitelli, "On the value set of small families of polynomials over a finite field, II," arXiv:1310.3293v1 (2013-10-11), https://arxiv.org/abs/1310.3293.
3. G. Matera, M. Pérez, M. Privitelli, "On the value set of small families of polynomials over a finite field, I," arXiv:1306.1744 (2013), https://arxiv.org/abs/1306.1744.
