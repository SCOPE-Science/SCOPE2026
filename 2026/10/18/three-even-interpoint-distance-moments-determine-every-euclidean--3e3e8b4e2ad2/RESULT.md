# Three even interpoint-distance moments determine every Euclidean triangle with sharp cubic-root stability

## Finding
Let \(T\) be any nondegenerate Euclidean triangle. Draw two independent points \(X,Y\) uniformly from its area, and put \(m_j=\mathbb E\|X-Y\|^{2j}\), for \(j=1,2,3\). Write \(a,b,c\) for the **squared** lengths of its three sides and \(s_1=a+b+c\), \(s_2=ab+bc+ca\), \(s_3=abc\). Then
\[
 m_1=\frac{s_1}{18},\qquad
 m_2=\frac{s_1^2-2s_2}{60},\qquad
 m_3=\frac{23s_1^3}{4200}-\frac{31s_1s_2}{2100}+\frac{s_3}{210}.
\]
In particular, **all** nondegenerate Euclidean triangles, including acute, right, obtuse, isosceles and equilateral ones, are determined up to Euclidean congruence by these three moments. Two moments do not suffice, even if the triangle's area is also known.

For triangles with all squared side lengths at most \(1\), let \(a_1\le a_2\le a_3\) and \(b_1\le b_2\le b_3\) be the respective sorted squared side lengths of \(T\) and \(T'\), and let \(\delta=\max_{1\le j\le3}|m_j(T)-m_j(T')|\). The uniform inverse bound
\[
\max_{1\le i\le3}|a_i-b_i|\le 100\,\delta^{1/3}
\]
holds; no exponent strictly greater than \(1/3\) works uniformly, even near equilateral triangles.

## Assumptions and scope
Triangles are compact, full-dimensional planar Euclidean triangles of strictly positive area, and the samples are independent with normalized two-dimensional Lebesgue measure. Translation, rotation and reflection are immaterial. The stability estimate uses an absolute scale normalization: **both** triangles have each squared side length in \((0,1]\). The moments are of Euclidean interpoint distance rather than projection width, chord length or the distance from a specified vertex.

## Proof
**1. Exact moments.** Translate one vertex to the origin and call the other two vertex vectors \(u,v\). Write a uniform point as \(Su+Tv\), where \((S,T)\) has constant density \(2\) on \(\{(s,t):s,t\ge0,\ s+t\le1\}\). Consequently for integers \(p,q\ge0\),
\[
 \mathbb E(S^pT^q)=\frac{2p!q!}{(p+q+2)!}.
\]
For an independent copy \((S',T')\), define \(U=S-S'\), \(V=T-T'\), and \(A=\|u\|^2\), \(B=\|v\|^2\), \(C=\langle u,v\rangle\). Thus
\[
\|X-Y\|^2=AU^2+BV^2+2CUV.
\]
For any nonnegative integers \(r,t\), the independent-copy expansion yields the **finite exact formula**
\[
\mathbb E(U^rV^t)=\sum_{i=0}^{r}\sum_{k=0}^{t}(-1)^{r-i+t-k}\binom ri\binom tk\frac{2i!k!}{(i+k+2)!}\frac{2(r-i)!(t-k)!}{(r-i+t-k+2)!}.
\]
Apply the multinomial theorem to \((AU^2+BV^2+2CUV)^j\), for \(j=1,2,3\), insert this identity, and collect terms. Since the squared sides are \(a=A\), \(b=B\), \(c=A+B-2C\), elementary simplification gives precisely the three formulas in the Finding. All sums are finite rational identities, and the accompanying checker independently executes the rational expansion and verifies all three polynomial identities using exact interpolation.

**2. Inversion.** The measured moments recover the three elementary symmetric functions without division by a vanishing shape parameter:
\[
 s_1=18m_1,\qquad
 s_2=\frac{s_1^2-60m_2}{2},\qquad
 s_3=210m_3-\frac{23s_1^3}{20}+\frac{31s_1s_2}{10}.
\]
Hence \(a,b,c\) are exactly the unordered real roots, with multiplicities, of
\[
 z^3-s_1z^2+s_2z-s_3=0.
\]
They are positive and satisfy the triangle inequalities because they arose from a nondegenerate triangle. The side-side-side congruence theorem reconstructs \(T\), including all repeated-root cases. Heron's identity also gives
\[
16\operatorname{area}(T)^2=4s_2-s_1^2=324m_1^2-120m_2,
\]
so even the first two moments already fix area.

**3. Optimal number of initial moments.** Squared side triples \((1,4,4)\) and \((2,2,5)\) define genuine noncongruent triangles, with corresponding side lengths \((1,2,2)\) and \((\sqrt2,\sqrt2,\sqrt5)\): in each case the strict Gram determinant \(4ab-(a+b-c)^2\) is \(15>0\). Both have \(s_1=9\), \(s_2=24\), hence \((m_1,m_2)=(1/2,11/20)\), and even the same area \(\sqrt{15}/4\). Their third moments differ by \(4/210=2/105\). A single moment is consequently insufficient as well.

**4. Uniform inverse stability.** Under the squared-side upper bound \(1\), one has \(0<s_1\le3\), \(0<s_2\le3\). For two triangles at moment discrepancy \(\delta\), the inverse formulas imply
\[
 |\Delta s_1|\le18\delta,\quad |\Delta s_2|\le84\delta,\quad
 |\Delta s_3|\le1718\delta.
\]
Indeed, \(|\Delta(s_1^3)|\le486\delta\), \(|\Delta(s_1s_2)|\le306\delta\); inserting these bounds gives \(|\Delta s_3|\le(210+23\cdot486/20+31\cdot306/10)\delta<1718\delta\). Let \(p\) and \(q\) be the resulting monic squared-side cubics. On \(|z|\le2.02\),
\[
 |p(z)-q(z)|\le(18\cdot2.02^2+84\cdot2.02+1718)\delta<2000\delta.
\]
If \(0<\delta<1/4000\), let \(r=(4000\delta)^{1/3}<1\). Choose a radius \(r'\) in \((r,1.02r)\) that avoids the finitely many pairwise root-disc tangencies. Each component of the union of the three disks centered at roots of \(p\) with radius \(r'\) is a Jordan region with boundary in \(|z|\le2.02\). On each component boundary \(|p(z)|\ge(r')^3>4000\delta>|p(z)-q(z)|\), so Rouché's theorem gives equal root counts in each component. Each component has diameter at most \(6r'\), because it comprises at most three radius-\(r'\) disks. Matching the real, sorted roots within corresponding components therefore gives
\[
 \max_i|a_i-b_i|\le6r'<6\cdot1.02\cdot4000^{1/3}\delta^{1/3}<100\delta^{1/3}.
\]
If \(\delta=0\), uniqueness already proves equality. If \(\delta\ge1/4000\), the trivial squared-side bound \(\max_i|a_i-b_i|\le1<100\delta^{1/3}\) suffices.

**5. Sharp exponent.** For \(\varepsilon\in(0,1/10)\), take squared side triples
\[
 (1+\varepsilon,1+\varepsilon,1-2\varepsilon),\qquad
 (1-\varepsilon,1-\varepsilon,1+2\varepsilon),
\]
and divide every entry in both triples by \(1+2\varepsilon\). All resulting triangles are nondegenerate, and their squared side lengths do not exceed \(1\). The two triples have identical \(s_1\) and \(s_2\) but differ in \(s_3\) by \(4\varepsilon^3/(1+2\varepsilon)^3\). Their sole differing measured moment has absolute difference \(2\varepsilon^3/(105(1+2\varepsilon)^3)\), whereas the maximum difference between sorted squared side lengths is \(2\varepsilon/(1+2\varepsilon)\). Thus a uniform exponent greater than \(1/3\) is impossible as \(\varepsilon\downarrow0\).

## Verification
Run `python3 CHECKER.py` with Python 3 standard library. It checks the three exact polynomial identities at \(8+27+64=99\) rational nodes: each side is separately of degree at most \(j\) in \(A,B,C\), so equality on a full \((j+1)^3\) integer tensor grid proves equality as a polynomial for **all** real inputs, not merely the sampled inputs. The same script checks the two-moment collision, inverse reconstruction, Heron determinant, and a rational-parameter sharpness family. Expected output consists of two `PASS` lines. The complex-root estimate in Step 4 is proved analytically above; the checker does not replace that proof.

As an independent published benchmark, Bäsel's exact equilateral triangle moments for circumradius \(R\) give \(\mathbb E\|X-Y\|^6=747R^6/1400\). Our formula with each squared side \(3R^2\) agrees exactly. The two arbitrary-triangle counterexamples and the stability mechanism do not rely on any finite numerical sampling.

## Relationship to prior work
O'Hara studies identification of **generic** polygonal domains from the **entire** interpoint-distance law/Riesz energy function; the accessible statement does not provide a finite three-moment inverse for **every** triangle, nor the optimal modulus. Tong–Ahmadi–Pan obtain **forward** point-distance distributions in arbitrary triangles, and Tong–Pan extend forward calculations to polygonal domains. Bäsel calculates moments for **regular** polygons, including the equilateral triangle; regular-polygon formulas alone do not recover a scalene triangle from three measurements. A parallelogram moment reconstruction theorem concerns a different sampling geometry and does not imply the triangle formulas. The present claim is solely the finite triangular inverse with a sharp stability exponent, not first discovery of the distance distribution.

## Limitations
The inversion is proved for nondegenerate planar triangles and the particular consecutive even orders \(2,4,6\); it does not address general polygons, noisy distributions without moment estimates, or arbitrary alternative moment selections. Stability concerns **squared** side lengths after the stated common absolute upper bound; ordinary side lengths near degeneracy require separate analysis. Priority against unindexed historical literature is not certified. The motivating 2026 manuscript could not be inspected in full; the published abstract permits the stated comparison but leaves residual overlap risk.

## References
1. Jun O'Hara, *Identification of generic polygonal domains by integral-geometric invariants*, arXiv:2608.02288 (first public version August 3, 2026), https://arxiv.org/abs/2608.02288.
2. Fei Tong, Maryam Ahmadi, Jianping Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498 (November 29, 2013), https://arxiv.org/html/1312.2498v1.
3. Uwe Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815 (January 11, 2021), https://arxiv.org/html/2101.03815v1.
4. Fei Tong, Jianping Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407 (January 21, 2016), https://arxiv.org/abs/1602.03407.
