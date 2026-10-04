# Parity of finite line counts on complete intersections

## Finding
Let \(X\subset \mathbb P^n_{\mathbb C}\) be a general complete intersection of multidegree \(\mathbf d=(d_1,\ldots,d_s)\), with every \(d_i\ge 2\), and suppose the expected dimension of its Fano scheme of lines is zero:
\[
\sum_{i=1}^s(d_i+1)=2n-2.
\]
Let \(N(\mathbf d;n)\) denote the intersection-theoretic number of lines, equivalently the degree of the zero-dimensional Fano scheme for a general transverse member. Then
\[
N(\mathbf d;n)\equiv 1\pmod 2
\quad\Longleftrightarrow\quad
 d_1,\ldots,d_s\text{ are all odd}.
\]
Consequently, for a general real complete intersection satisfying the same zero-dimensional condition and having all defining degrees odd, at least one of its complex lines is real.

## Assumptions and scope
The base field for the enumerative statement is \(\mathbb C\). Generality is used so that the Fano scheme has the expected zero dimension and the top-Chern-class degree is the enumerative line count. The real corollary concerns general complete intersections defined over \(\mathbb R\); complex conjugation acts on the finite line scheme.

## Proof
For one defining equation of degree \(d\), put
\[
q_d(x)=\prod_{j=0}^d\bigl((d-j)+jx\bigr).
\]
The line case of Debarre--Manivel's degree formula gives
\[
N(\mathbf d;n)= [x^{n-1}](1-x)\prod_{i=1}^s q_{d_i}(x).
\]
This is the one-variable specialization of their Grassmannian coefficient formula for \(F_1(X)\).

If some \(d_i\) is even, then the \(j=0\) and \(j=d_i\) factors of \(q_{d_i}(x)\) are \(d_i\) and \(d_i x\). Hence every coefficient of \(q_{d_i}(x)\), and therefore the displayed coefficient defining \(N(\mathbf d;n)\), is even. Thus \(N(\mathbf d;n)\) is even.

Now assume every \(d_i\) is odd. Modulo \(2\), for each \(j\), the factor \((d_i-j)+jx\) is \(1\) when \(j\) is even and \(x\) when \(j\) is odd. There are exactly \((d_i+1)/2\) odd integers in \(\{0,\ldots,d_i\}\), so
\[
q_{d_i}(x)\equiv x^{(d_i+1)/2}\pmod 2.
\]
The zero-dimensional condition therefore yields
\[
\prod_iq_{d_i}(x)\equiv x^{n-1}\pmod 2.
\]
Since \(1-x\equiv1+x\pmod2\), the coefficient of \(x^{n-1}\) in \((1-x)x^{n-1}\) is \(1\). Hence the line count is odd.

For the real corollary, nonreal complex lines occur in conjugate pairs. An odd finite complex line count therefore leaves at least one conjugation-fixed, hence real, line.

## Verification
The standalone exact-arithmetic checker `artifacts/verify_ci_line_parity.py` reconstructs the coefficient formula directly. It first reproduces the standard complete-intersection Calabi--Yau threefold line counts \(2875,1280,1053,720,512\) for multidegrees \((5)\), \((4,2)\), \((3,3)\), \((3,2,2)\), and \((2,2,2,2)\). It then exhausts every nondecreasing multidegree with \(d_i\ge2\), \(3\le n\le12\), and \(\sum_i(d_i+1)=2n-2\). The replay checked 209 cases, of which 55 have all degrees odd, and found no parity discrepancy. The finite computation is regression evidence only; the proof above is uniform in all admissible dimensions and multidegrees.

## Relationship to prior work
Debarre and Manivel give the general coefficient formula for degrees of Fano schemes of linear spaces on complete intersections; their formula is the sole enumerative input used here. Their later paper on real complete intersections proves nonemptiness of real Fano schemes for odd multidegrees under a strict dimension inequality. For lines, that strict inequality excludes the zero-dimensional boundary considered here, while the parity computation above handles that boundary exactly.

For hypersurfaces, Grünberg and Moree proved that the finite number of lines on a general hypersurface of degree \(2n-3\) in \(\mathbb P^n\) is odd, together with stronger congruences. That is the special case \(s=1\) of the odd-degree direction above. The statement here also gives the converse and treats arbitrary complete-intersection multidegrees.

## Limitations
The result concerns lines, not higher-dimensional linear spaces. It determines parity, not the exact enumerative count. Generality/transversality is required to identify the top-Chern-class degree with a reduced finite set of geometric lines. For special complete intersections the Fano scheme may be nonreduced or positive-dimensional, and the geometric wording must then be replaced by the intersection-theoretic degree. No claim is made about the number of real lines beyond existence forced by odd parity.

## References
1. O. Debarre and L. Manivel, *Schémas de Fano*, arXiv:alg-geom/9611033, first public version 1996-11-26; published as *Sur la variété des espaces linéaires contenus dans une intersection complète*, Math. Ann. 312 (1998), 549--574, especially Theorem 4.3.
2. O. Debarre and L. Manivel, *Sur les intersections complètes réelles*, C. R. Acad. Sci. Paris Sér. I Math. 331 (2000), 887--892.
3. D. B. Grünberg and P. Moree, *Sequences of enumerative geometry: congruences and asymptotics*, arXiv:math/0610286 (2006), especially the hypersurface line-count congruences.
