# Eight-point quadratic phaseless interpolation: the orthogonal-circle obstruction

## Finding

Let \(\zeta=\exp(2\pi i/5)\). Choose any three pairwise distinct points \(w_1,w_2,w_3\in\mathbb C\) with \(|w_j|\ne1\), and put
\[
\Omega=\{1,\zeta,\zeta^2,\zeta^3,\zeta^4,w_1,w_2,w_3\}.
\]
There is a unique generalized circle \(\mathcal C\) (an ordinary circle or a straight line) through the three additional points. For all polynomials \(p,q\in\mathbb C[z]\) of degree at most two, the implication
\[
\bigl(|p(z)|=|q(z)|\text{ for every }z\in\Omega\bigr)
\Longrightarrow p=\tau q\text{ for some }|\tau|=1
\]
holds **if and only if** \(\mathcal C\) is *not orthogonal* to the unit circle. For a straight line, orthogonality means passing through the origin.

Equivalently, write the unique generalized circle equation, up to nonzero real scaling, as
\[
\mathcal C=\{z:a+t|z|^2+2\operatorname{Re}(uz)=0\},
\quad a,t\in\mathbb R,\quad u\in\mathbb C.
\]
Then the complete necessary-and-sufficient condition is simply \(a\ne t\). The configuration has eight points and no universal complex quadratic phase-retrieval configuration with fewer than eight magnitude evaluations exists. For example, the three anchors \(0,2,2i\) give an optimal-size recovering set; the three anchors \(0,2,3\) give a nonrecovering set.

## Assumptions and scope

Measurements are pointwise *magnitudes*, not signed or complex polynomial values. The result includes zero polynomials, lower-degree polynomials, and arbitrary complex coefficients. The five initial points are the fifth roots of unity. The three anchors need only be distinct and strictly off the unit circle; they may be collinear, and may lie inside or outside the unit disk. Orthogonality of two genuine intersecting circles is in the usual Euclidean sense; the line case is defined above.

## Proof

**1. The first five intensities determine a circular autocorrelation.** Write \(v(z)=(1,z,z^2)^T\). A Hermitian difference \(H=xx^*-yy^*\), with \(x=(\overline{a_0},\overline{a_1},\overline{a_2})^T\) for the coefficients of \(p\) and similarly for \(q\), obeys \(v(z)^*Hv(z)=|p(z)|^2-|q(z)|^2\). For \(|z|=1\), this difference is a real trigonometric polynomial of degree at most two. Five distinct fifth roots of unity determine all five Fourier coefficients, so vanishing at the five measured roots is equivalent to vanishing on the *entire* unit circle. Conversely, every Hermitian \(H\) vanishing on that circle is, uniquely,
\[
H=\begin{pmatrix}
 a&u&0\\
 \overline u&t-a&-u\\
 0&-\overline u&-t
\end{pmatrix},\qquad a,t\in\mathbb R,\;u\in\mathbb C.
\tag{1}
\]
(The zero coefficients at circular Fourier frequencies two and one give the indicated off-diagonal constraints; the zero constant coefficient gives \(H_{00}+H_{11}+H_{22}=0\).) Direct expansion yields the factorization
\[
v(z)^*Hv(z)=(1-|z|^2)\bigl(a+t|z|^2+2\operatorname{Re}(uz)\bigr).
\tag{2}
\]

**2. The remaining kernel is a single generalized circle.** Since \(|w_j|\ne1\), the three additional measurements vanish exactly when
\[
a+t|w_j|^2+2\operatorname{Re}(uw_j)=0
\quad(j=1,2,3).
\tag{3}
\]
Three *distinct* points uniquely determine a generalized circle. In real variables \(u=U+iV\), \(w_j=x_j+iy_j\), equations (3) have coefficient rows \((1,x_j^2+y_j^2,2x_j,-2y_j)\) and rank exactly three: three collinear points force their unique straight line, while noncollinear points force their unique genuine circle. Hence the Hermitian measurement kernel is the real span of the unique nonzero matrix (1) associated with \(\mathcal C\).

**3. The determinant detects precisely the right-angle obstruction.** Direct expansion of (1) gives
\[
\det H=(t-a)(|u|^2-at).
\tag{4}
\]
The second factor is *strictly positive*. Indeed, if \(t\ne0\), completing the square in (3) produces a genuine circle with center \(-\overline u/t\) and radius \(R>0\), hence \(|u|^2-at=t^2R^2>0\); if \(t=0\), (3) is a genuine straight line and \(u\ne0\), so the factor is \(|u|^2>0\). Thus the kernel generator is nonsingular exactly when \(a\ne t\). For a genuine circle, \(a=t\) is equivalent to \(|\text{center}|^2=R^2+1\), the usual orthogonality condition with the unit circle. For a line, \(a=t=0\) exactly means that the line passes through the origin.

**4. Why determinant zero is exactly phase ambiguity.** The intensity measurements determine a quadratic polynomial modulo unit phase if and only if the Hermitian measurement kernel has no nonzero matrix of rank at most two. One direction follows because the difference of two rank-one coefficient matrices has rank at most two. Conversely, a nonzero rank-at-most-two Hermitian kernel matrix cannot be positive or negative semidefinite: if its evaluations vanish at the five unit-circle points, those five evaluation vectors span \(\mathbb C^3\), and a semidefinite matrix vanishing on a spanning set must be zero. Every remaining such matrix has one positive and one negative eigenvalue; its positive-minus-negative rank-one spectral decomposition supplies two non-phase-equivalent polynomials with identical sample magnitudes. Combining with (4) proves the classification, including every degenerate coefficient case.

**5. Eight is globally minimal.** The real vector space of Hermitian \(3\times3\) matrices has dimension nine. With at most seven intensity measurements its linear measurement kernel has dimension at least two. Choose independent Hermitian elements \(H_1,H_2\) of the kernel. The continuous function \(\theta\mapsto\det(\cos\theta H_1+\sin\theta H_2)\) is odd under \(\theta\mapsto\theta+\pi\), so it vanishes somewhere. The resulting matrix is nonzero and singular. If the measurement vectors span \(\mathbb C^3\), it cannot be semidefinite, as above, and therefore gives a genuine rank-two ambiguity. If they fail to span, nonidentifiability is immediate. Thus no seven or fewer intensity measurements can retrieve every vector of \(\mathbb C^3\) up to phase.

**6. Examples.** For anchors \(0,2,2i\) the circle equation is \(|z|^2-2\operatorname{Re}z-2\operatorname{Im}z=0\), which has \(a=0,t=1,u=-1+i\); (4) equals \(2\), so these eight points recover all quadratics. For anchors \(0,2,3\), the generalized circle is the real axis, which is orthogonal to the unit circle. The distinct polynomials \(p(z)=z+i(1+z^2)\) and \(q(z)=z-i(1+z^2)\) have equal magnitudes for every \(|z|=1\) and every real \(z\); this independently witnesses failure.

## Verification

The accompanying `CHECKER.py` checks the lifted Hermitian factorization and determinant by exact symbolic algebra, verifies the rank-three anchor constraints in eleven representative ordinary-circle and line configurations (including an exactly orthogonal circle), and checks the explicit line ambiguity. Execute `python CHECKER.py` with SymPy installed. The stored verification output is `verification_output.txt`. These finite exact checks corroborate, but do not replace, the universal proof above.

## Relationship to prior work

Bodmann and Hammen (2013), Theorem 2.3, construct minimal-redundancy magnitude measurements for polynomials using two carefully chosen circles; that sufficient construction and its underlying circular trigonometric interpolation are prior work. Chalendar and Partington (2024), Theorem 2.16, classify qualitative phase retrieval for complete pairs of circles or lines among analytic functions, including rational-angle obstructions. Grohs, Liehr, and Rathmair (2022) study multi-window sampled STFT phase retrieval through Fock-space sampling and finite frames. The present exact claim instead classifies *all* triples of off-circle additional points after a fixed five-point circular aperture, identifies the degree-two right-angle boundary, and establishes its optimal eight-point budget. Previously established sufficient special configurations do not imply this necessary-and-sufficient three-anchor criterion.

## Limitations

Only complex polynomials of degree at most two and five roots-of-unity reference samples are covered; stability and conditioning under noisy measurements are not bounded here. Nothing is asserted about an arbitrary choice of eight sample sites or polynomial degrees above two. Bibliographic priority remains subject to further comparison with unindexed results; an exact match was not established in the inspected primary texts. No independent mathematical audit has been performed.

## References

- B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487, 22 February 2013, Theorem 2.3, https://arxiv.org/pdf/1302.5487.
- P. Grohs, L. Liehr, and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620, first publicly submitted 21 July 2022, https://arxiv.org/pdf/2207.10620.
- I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, first publicly submitted 24 March 2024, Theorems 2.6 and 2.16, https://arxiv.org/pdf/2403.16255.
