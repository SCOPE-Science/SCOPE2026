# A generic lower-order perturbation criterion for opposite exponential phases

## Finding
Let \\(P,Q,R\\in\\mathbb C[z]\\) be nonconstant polynomials. Write \\(m=\\deg Q\\), \\(k=\\deg R\\), assume \\(1\\le k<m\\), and set
\\[
\\widetilde Q=-Q+R,\\qquad F(z)=\\exp(Q(z))+\\exp(\\widetilde Q(z))+P(z).
\\]
For a polynomial \\(S\\) of degree \\(d\\) with leading coefficient of argument \\(\\beta\\), its fundamental rays are the rays at angles
\\[
\\alpha_j(S)=-\\frac{\\beta}{d}-\\frac{\\pi}{2d}+\\frac{\\pi j}{d},\\qquad 0\\le j<2d.
\\]
Assume that no fundamental ray of \\(Q\\) is a fundamental ray of \\(R\\). Then \\(F\\) has a Baker omitted value at \\(\\infty\\).

Since \\(\\widetilde Q=-Q+R\\) has the same degree as \\(Q\\) and the negative leading coefficient, this gives a generic affirmative subcase of Question 6.1(1) in Das--Ghora--Nayak. For fixed \\(Q\\) and fixed lower degree \\(k\\), the excluded leading-coefficient arguments for \\(R\\) form only a finite set. A concrete instance is
\\[
Q(z)=z^2,\\qquad R(z)=z,\\qquad \\widetilde Q(z)=-z^2+z,
\\]
so \\(\\exp(z^2)+\\exp(-z^2+z)+P(z)\\) has a Baker omitted value for every nonconstant polynomial \\(P\\).

## Assumptions and scope
The statement concerns the Baker omitted value at infinity for an entire exponential polynomial with two exponential terms and one nonconstant polynomial term. It does not settle the resonant lower-order cases in which a fundamental ray of \\(R=Q+\\widetilde Q\\) coincides with a fundamental ray of \\(Q\\), and it does not settle the full version of Question 6.1(1).

The proof uses three results stated and proved or recalled in arXiv:2609.24154v1: the unbounded-curve characterization of a Baker omitted value (Lemma 2.1), the one-exponential theorem \\(A\\exp(S)+B\\) (Theorem 1.1), and the phase-separation Lemma 3.4. The fundamental-sector estimates are those of Lemma 3.2 and the connected asymptotic-ray reduction is Property (13)/Remark 3.1 in the same source.

## Proof
Let
\\[
A(z)=\\exp(Q(z)),\\qquad B(z)=\\exp(\\widetilde Q(z))=\\exp(-Q(z)+R(z)).
\\]
Then
\\[
A(z)B(z)=\\exp(R(z)),\\qquad \\frac{A(z)}{B(z)}=\\exp(2Q(z)-R(z)).
\\]
By Lemma 2.1 of the source it is enough to prove that \\(F(\\gamma)\\) is unbounded for every unbounded continuous curve \\(\\gamma\\).

Consider the fundamental partition associated with \\(Q\\). If \\(\\gamma\\) has an unbounded intersection with a closed fundamental subsector on which \\(\\Re Q(z)\\ge c|z|^m\\), then \\(R(z)=O(|z|^k)\\) with \\(k<m\\), so for all sufficiently large points in that subsector,
\\[
\\Re\\widetilde Q(z)=-\\Re Q(z)+\\Re R(z)\\le-\\frac c2|z|^m.
\\]
Thus \\(|A(z)|\\) grows like \\(\\exp(c|z|^m)\\), while \\(|B(z)|\\) decays exponentially and \\(|P(z)|\\) grows only polynomially. Along an unbounded sequence in that subsector, \\(|F(z)|\\to\\infty\\). The complementary fundamental subsectors satisfy \\(\\Re Q(z)\\le-c|z|^m\\); there \\(\\Re\\widetilde Q(z)\\ge c|z|^m/2\\), and the same argument with \\(A\\) and \\(B\\) interchanged gives unboundedness.

It remains to treat the case in which \\(\\gamma\\) is asymptotic to a fundamental ray of \\(Q\\). Using Property (13) from the source, replace the relevant unbounded portion by a connected set \\(\\gamma^*\\) whose unbounded points lie in an arbitrarily narrow sector around one fundamental-ray angle \\(\\alpha\\), with every sequence in \\(\\gamma^*\\) tending to infinity having argument tending to \\(\\alpha\\). Added connecting pieces, if any, lie on a fixed circle and hence do not affect boundedness.

Because \\(\\alpha\\) is not a fundamental-ray angle of \\(R\\), the leading term of \\(\\Re R(re^{i\\theta})\\) is uniformly separated from zero when \\(\\theta\\) is sufficiently close to \\(\\alpha\\). Hence for some \\(c>0\\) and all sufficiently large \\(z\\in\\gamma^*\\), exactly one of the following two alternatives holds:
\\[
\\Re R(z)\\ge c|z|^k
\\]
or
\\[
\\Re R(z)\\le-c|z|^k.
\\]
The sign is fixed by the chosen ray.

Suppose first that \\(\\Re R(z)\\ge c|z|^k\\), and assume for contradiction that \\(F\\) is bounded on \\(\\gamma^*\\). Since \\(P\\) is polynomial,
\\[
|A(z)+B(z)|=|F(z)-P(z)|=O(|z|^{\\deg P}).
\\]
But
\\[
|A(z)B(z)|=\\exp(\\Re R(z))\\ge\\exp(c|z|^k).
\\]
The polynomial bound for the sum is negligible compared with the square root of this product. Consequently
\\[
\\frac{|A(z)|}{|B(z)|}\\longrightarrow1
\\]
and therefore
\\[
\\frac{A(z)}{B(z)}=\\exp(2Q(z)-R(z))\\longrightarrow-1
\\]
as \\(z\\to\\infty\\) along \\(\\gamma^*\\). The polynomial \\(2Q\\) has the same fundamental rays as \\(Q\\), while \\(\\deg R<m\\). Lemma 3.4 applied to \\(Q_1=2Q\\), \\(Q_2=R\\), and the constant rational map \\(1\\) produces an unbounded sequence on \\(\\gamma^*\\) for which \\(-1\\) is not a limit point of \\(\\exp(2Q-R)\\). This is a contradiction.

Now suppose that \\(\\Re R(z)\\le-c|z|^k\\) and again assume \\(F\\) bounded. Since \\(P\\) is nonconstant, there are constants \\(C_1,C_2>0\\) and \\(d=\\deg P\\) such that for all sufficiently large \\(z\\),
\\[
C_1|z|^d\\le|P(z)|\\le C_2|z|^d.
\\]
Thus \\(|A(z)+B(z)|\\ge C_1|z|^d/2\\) for large \\(z\\in\\gamma^*\\), whereas
\\[
|A(z)B(z)|\\le\\exp(-c|z|^k).
\\]
It follows that the larger of \\(|A(z)|\\) and \\(|B(z)|\\) is at least a fixed multiple of \\(|z|^d\\), while the smaller tends to zero uniformly on the unbounded part. Equality \\(|A(z)|=|B(z)|\\) is therefore impossible there. On each outer connected branch the same exponential is dominant. If infinitely far branches of \\(\\gamma^*\\) are needed, join all branches of one dominance type to the fixed auxiliary circle from Property (13); at least one dominance type yields an unbounded connected curve.

On an unbounded curve where \\(A\\) is dominant, \\(B(z)\\to0\\) and boundedness of \\(F\\) would make \\(A+P=\\exp(Q)+P\\) bounded. This contradicts Theorem 1.1, which says \\(\\exp(Q)+P\\) has a Baker omitted value. If \\(B\\) is dominant, the same argument contradicts Theorem 1.1 for \\(\\exp(\\widetilde Q)+P\\). Therefore \\(F(\\gamma^*)\\), and hence \\(F(\\gamma)\\), is unbounded.

All possibilities for an unbounded curve have been exhausted, so Lemma 2.1 gives that \\(F\\) has a Baker omitted value at \\(\\infty\\).

## Verification
The proof was checked against the exact statements used from arXiv:2609.24154v1. Theorem 1.1 covers \\(\\exp(S)+P\\) for every nonconstant polynomial \\(S\\) and nonconstant polynomial \\(P\\). Lemma 3.4 applies because \\(2Q\\) has degree \\(m\\), \\(R\\) has degree \\(k<m\\), and \\(2Q\\) has exactly the same fundamental rays as \\(Q\\). The transversality hypothesis makes \\(\\Re R\\) have a fixed sign with magnitude comparable to \\(|z|^k\\) on a sufficiently narrow sector about each relevant fundamental ray of \\(Q\\).

The positive-sign case was checked by the product-sum comparison: a polynomial-size sum and an exponentially large product force the two exponential terms to have asymptotically equal moduli and opposite phases. The negative-sign case was checked using the exponentially small product: one exponential must be polynomially large while the other tends to zero, and connectedness prevents dominance switching outside a sufficiently large disk without passing through impossible equal modulus.

No finite experiment, numerical approximation, or exhaustive enumeration is part of the proof.

## Relationship to prior work
Das--Ghora--Nayak prove that \\(\\exp(Q)+\\exp(-Q)+P\\) and \\(\\exp(Q)-\\exp(-Q)+P\\) have Baker omitted value for every nonconstant \\(P,Q\\). Immediately afterward, Question 6.1(1) asks whether \\(-Q\\) may be replaced by a same-degree polynomial whose leading coefficient is the negative of the leading coefficient of \\(Q\\), and more generally by a polynomial with the same fundamental rays as \\(-Q\\).

The present criterion answers a generic lower-order perturbation subfamily of that explicit question. Writing the replacement as \\(\\widetilde Q=-Q+R\\), the new condition is that the lower-order correction \\(R\\) have no fundamental ray in common with \\(Q\\). The source's Theorem 1.2 does not imply this result: that theorem assumes unequal exponential degrees and noncoincident fundamental rays of the two exponential phases, while here \\(Q\\) and \\(\\widetilde Q\\) have equal degree and the same fundamental-ray set.

The earlier Das--Nayak paper proves the one-exponential case and iterated-exponential variants, not the two same-degree opposite-leading-phase statement. The original 2016 Baker-omitted-value paper supplies the general unbounded-curve criterion but no exponential-polynomial classification of this form.

## Limitations
The theorem deliberately excludes the resonant situation in which a fundamental ray of the lower-order correction \\(R\\) is also a fundamental ray of \\(Q\\). In that case the sign of the leading contribution to \\(\\Re R\\) vanishes precisely along the asymptotic direction, so the two-case product argument above no longer closes. The full Question 6.1(1), including those resonances and the more general coincident-fundamental-ray formulation, remains unproved here.

The originality search cannot exclude an unnamed equivalent consequence hidden in the broad classical value-distribution literature on exponential polynomials. The inspected recent source itself nevertheless states the same-degree opposite-leading-coefficient problem as unverified, and targeted searches found no stronger published statement covering the transversality criterion.

## References
1. S. Das, S. Ghora, T. Nayak, *Exponential polynomials with Baker omitted value*, arXiv:2609.24154v1, first public 2026-09-21. In particular Theorem 1.1, Lemmas 2.1 and 3.4, Example 6.1, and Question 6.1.
2. S. Das, T. Nayak, *Sum of the exponential and a polynomial: singular values and Baker wandering domains*, arXiv:2407.14835v1; *Complex Variables and Elliptic Equations* 70 (2025), 1831--1847.
3. T. K. Chakra, G. Chakraborty, T. Nayak, *Baker omitted value*, *Complex Variables and Elliptic Equations* 61 (2016), 1353--1361, doi:10.1080/17476933.2016.1174216.
