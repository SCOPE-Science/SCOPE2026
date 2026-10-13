# The sharp four-draw three-species occupancy probability

## Finding
For any infinitely exchangeable random sequence on a standard Borel space, let \(K_4\) count distinct values among the first four observations. Then
\[
\Pr(K_4=3)\le\frac{72}{125}.
\]
Five equally likely values, sampled independently, attain equality. Among finitely supported i.i.d. laws, they are the unique maximizers up to relabeling. The result is a sharp universal constraint on the single-collision occupancy event, not a characterization of the full law of \(K_4\).

## Assumptions and scope
The underlying state space is standard Borel, so an infinitely exchangeable sequence admits a de Finetti representation by random directing probability measures. The probability measures may have finitely or countably many atoms and an arbitrary diffuse component. The theorem does *not* cover a merely four-exchangeable vector without an infinite extension. Write \(p_i\) for positive atomic masses of an i.i.d. directing law and \(s_r=\sum_i p_i^r\) for \(r\ge2\); necessarily \(\sum_i p_i\le1\). A diffuse component is understood to produce no exact ties in independent observations.

## Proof
**Exact occupancy identity.** Exactly three distinct values in four draws means one repeated pair and two mutually different singleton values. Fix the repeated atomic value with mass \(p_i\), choose the pair of positions in \(\binom42=6\) ways, and then select two different values avoiding that atom. Their probability is \((1-p_i)^2-\sum_{j\ne i}p_j^2\), even if a diffuse component is present. Thus, with absolutely convergent sums,
\[
q:=\Pr(K_4=3)=6\sum_i p_i^2\left[(1-p_i)^2-\sum_{j\ne i}p_j^2\right]
=6\left(s_2-2s_3+2s_4-s_2^2\right).
\]

**Two-mass deformation.** First assume the i.i.d. law is supported on finitely many atoms. Hold all masses except two, \(a,b\ge0\), fixed, write \(s=a+b\), \(t=ab\), and put \(R_2\) equal to the sum of squares of the other masses. Substituting \(a^2+b^2=s^2-2t\), \(a^3+b^3=s^3-3st\), and \(a^4+b^4=s^4-4s^2t+2t^2\) into the identity cancels the quadratic terms in \(t\). Exactly,
\[
\frac{q}{6}=C+ct,\qquad c=-2+6s-4s^2+4R_2,
\]
where \(C\) does not depend on the split. In particular, merging \(a,b\) to \(s,0\) changes \(q\) by \(-6cab\), whereas equalization maximizes \(ab\) at \(a=b=s/2\).

**Maximizing a finite parent.** On every simplex of at most \(m\) atoms the polynomial \(q\) attains a maximum. Select one such maximizer with the smallest number of positive masses. If two positive masses are unequal, then \(c>0\) makes their equalization strictly better, \(c<0\) makes merging strictly better, and \(c=0\) permits merging without loss and reduces the support. All three contradict the choice. Hence some maximizing law is uniform on its positive support. If it has \(r\) atoms, the exact occupancy probability is
\[
q_r=\frac{6(r-1)(r-2)}{r^3}\quad(r\in\mathbb N).
\]
For real \(x>0\), the derivative of the rational extension is \(6(-x^2+6x-6)/x^4\). It rises from the integer \(r=3\) to \(r=5\), then decreases for all \(r\ge5\), since \(3+\sqrt3<5\). The nearby values are \(q_4=9/16\), \(q_5=72/125\), and \(q_6=5/9\); cases \(r\le2\) give zero. Therefore \(q_r\le72/125\) for all positive integers \(r\), proving the universal bound for any finite parent.

**Finite-support equality.** Suppose a nonuniform finite parent reaches \(72/125\). For any unequal positive pair the same deformation argument forces \(c=0\), since otherwise equalization or merging increases the value. Merge such a pair: the value remains maximal, and support decreases. Repeat until the masses are all equal. The preceding paragraph forces the final law to be uniform on exactly five atoms. But the final flat merge would split one mass \(s=1/5\) while leaving four masses \(1/5\), for which \(R_2=4/25\) and \(c=-8/25<0\). The strict splitting loss \(6cab<0\) contradicts that flat merge. Thus the original law was already uniform on five atoms.

**General i.i.d. parent.** Enumerate the atomic masses. Keep the first \(M\) masses and replace the remaining total mass by \(N\) new equally weighted atoms. This produces a finite probability distribution. For each \(r\in\{2,3,4\}\), its atomic power sum is \(\sum_{i\le M}p_i^r+N^{1-r}(1-\sum_{i\le M}p_i)^r\). Letting \(N\to\infty\) and then \(M\to\infty\) gives \(s_r\); hence the occupancy identity and finite bound pass to the limit. This handles both infinitely many atoms and a diffuse component.

**Infinite exchangeability.** By de Finetti, conditional on the directing probability law the four draws are i.i.d. Apply the bound conditionally and take expectations. A deterministic directing law uniform on five atoms gives equality.

## Verification
The accompanying `verify.py` uses only Python's standard library and `fractions.Fraction`. It compares the analytic occupancy polynomial against explicit enumeration for 126 rational parent vectors, checks the two-mass identity on 36 exact cases, and checks the uniform-family formula and bound through \(r=100\). Running `python verify.py` prints `VERIFY_OK compositions=126 pair_split=36 m_uniform=100 max=72/125`. These finite checks corroborate the algebra, not the infinite-universe proof, which is fully analytic above.

## Relationship to prior work
Zhu's 2021 preprint, published in 2022, establishes sharp two-species occupancy bounds and the complete three-draw law, and asks for higher-dimensional feasible occupancy laws. His 2022 thesis discusses Yakubovich's extreme-vertex theorem for the hull of uniform-sampling laws, while recording the full-law description for four draws as unresolved. Those results alone do not establish that *arbitrary* four-draw i.i.d. occupancy distributions lie in the uniform-law convex hull and therefore do not entail this specific sharp three-species coordinate bound. Here the mass-deformation argument proves that bound directly, without the stronger convex-hull conjecture. The statement concerns only a single four-draw coordinate; it is not a proof of the full convex-hull conjecture.

## Limitations
The bound requires infinite exchangeability, not merely finite exchangeability. The equality uniqueness argument is asserted only for finitely supported i.i.d. parents. Equivalence to an older result under an alternative occupancy optimization or symmetric-polynomial name is a bibliographic risk; the cited literature is not exhaustive. No numerical computation is used as a universal proof.

## References
1. Theodore Zhu, *The distribution of the number of distinct values in a finite exchangeable sequence*, arXiv:2103.07518v1, first public 2021-03-12; *Electronic Journal of Probability* 27 (2022), DOI 10.1214/22-EJP815. Full text: https://arxiv.org/pdf/2103.07518 .
2. Theodore Zhu, *Some Problems on the Convex Geometry of Probability Measures*, doctoral thesis (2022), Chapter 2 Sections 2.0 and 2.3. https://escholarship.org/content/qt8001f519/qt8001f519.pdf . Thesis records Yuri Yakubovich's 2021 unpublished extreme-vertex result as prior work.
