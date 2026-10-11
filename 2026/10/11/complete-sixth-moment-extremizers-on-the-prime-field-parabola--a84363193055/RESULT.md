# Complete sixth-moment extremizers on the prime-field parabola

## Finding
For every prime \(p\ge5\), let \(\omega=\exp(2\pi i/p)\). Equip \(\mathbb F_p\) with normalized counting measure and \(\mathbb F_p^2\) with counting measure, and put
\[
\mathcal E_p f(x,y)=\frac1p\sum_{t\in\mathbb F_p}f(t)\omega^{xt+yt^2}.
\]
The established sharp extension inequality is
\[
\sum_{x,y\in\mathbb F_p}|\mathcal E_p f(x,y)|^6
\leq \left(1+\frac1p-\frac1{p^2}\right)
\left(\frac1p\sum_{t\in\mathbb F_p}|f(t)|^2\right)^3.
\]
**Complete equality classification:** every nonzero equality case, and no other nonzero function, is
\[
f(t)=\lambda\omega^{At+Bt^2}\qquad(t\in\mathbb F_p),
\]
with \(\lambda\in\mathbb C^\times\) and \(A,B\in\mathbb F_p\). There are exactly \(p^2\) projective classes of nonzero equality cases, modulo nonzero complex scalar multiplication. The sharp inequality and necessity of constant modulus are from Theorem 1.3 of González-Riquelme and Oliveira e Silva [1]; the phase rigidity and exact equality count are established below.

## Assumptions and scope
The field is \(\mathbb F_p\) of **prime order** \(p\ge5\). Polynomial expressions in \(t\) and phase exponents are interpreted modulo \(p\). A projective equality class identifies \(f\) and \(cf\) for all \(c\ne0\). The zero function trivially satisfies equality but is omitted from the classification of nonzero extremizers. The extension operator is normalized by \(p^{-1}\), with *unnormalized* target sixth moment, precisely as in [1]. No assertion is made for characteristic \(2\), characteristic \(3\), or arbitrary non-prime fields.

## Proof
**1. The sharp inequality and constant modulus.** Theorem 1.3 of [1] proves the displayed sharp \(L^2\)-to-\(L^6\) inequality and shows that every nonzero extremizer has constant nonzero modulus. Fix such an \(f\) and write \(f(t)=c z_t\), where \(c>0\) and \(|z_t|=1\). It remains to characterize the phases \(z_t\).

**2. Exact fiber identity and equality.** For \((s,r)\in\mathbb F_p^2\), define
\[
\mathcal F_{s,r}=\{(u,v,w)\in\mathbb F_p^3:
 u+v+w=s,\ u^2+v^2+w^2=r\},\quad R_{s,r}=|\mathcal F_{s,r}|,
\]
\[
C_{s,r}(f)=\sum_{(u,v,w)\in\mathcal F_{s,r}}f(u)f(v)f(w).
\]
Character orthogonality gives the exact identity
\[
\sum_{x,y\in\mathbb F_p}|\mathcal E_p f(x,y)|^6
=p^{-4}\sum_{s,r\in\mathbb F_p}|C_{s,r}(f)|^2.
\]
For constant modulus \(c\), the triangle inequality yields \(|C_{s,r}(f)|\le c^3R_{s,r}\) on every fiber. The constant function \(f\equiv c\) achieves equality on *every* fiber and, by [1], achieves the global sharp bound. Thus a constant-modulus extremizer must achieve triangle equality on every nonempty fiber: **all products \(z_u z_v z_w\) belonging to a fixed fiber are equal**. This implication does not require individual fibers to have generic cardinality.

For an independent check of the sharp constant, set \(\varepsilon\) to be the quadratic character of \(-3\) in \(\mathbb F_p\). After writing \(u=s/3+a\), \(v=s/3+b\), and \(w=s/3-a-b\), the fiber equation is
\[
a^2+ab+b^2=\frac{r-s^2/3}{2}.
\]
Completing the square and using the elementary identity \(\sum_{a\in\mathbb F_p}\chi(a^2-h)=-1\) for each nonzero \(h\), where \(\chi\) is the quadratic character, gives
\[
R_{s,r}=\begin{cases}
 p+(p-1)\varepsilon,&r=s^2/3,\\
 p-\varepsilon,&r\ne s^2/3.
\end{cases}
\]
Indeed, the character-sum identity follows by counting the solutions to \((X-Y)(X+Y)=h\), of which there are \(p-1\). It follows directly that
\[
\sum_{s,r}R_{s,r}^2=p\bigl((p+(p-1)\varepsilon)^2+(p-1)(p-\varepsilon)^2\bigr)
=p^4+p^3-p^2.
\]
This reproduces the constant function's sixth-moment value \(1+p^{-1}-p^{-2}\), for every prime \(p\ge5\), independently of any finite numerical sample.

**3. One translated equal-moment relation forces quadratic phases.** The integer triples
\[
(0,3,3)\quad\text{and}\quad(1,1,4)
\]
have equal sums and equal sums of squares: both sums equal \(6\) and both sums of squares equal \(18\). Translating all entries by \(t\in\mathbb F_p\) preserves both equalities. The fiber equality from Step 2 therefore gives, for every \(t\in\mathbb F_p\),
\[
 z_t z_{t+3}^{2}=z_{t+1}^{2}z_{t+4}.\tag{1}
\]
All subscripts are modulo \(p\), so this holds even when some of these residues coincide.

Define unit-modulus multiplicative differences
\[
 u_t=\frac{z_{t+1}}{z_t},\qquad
 v_t=\frac{u_{t+1}}{u_t},\qquad
 w_t=\frac{v_{t+1}}{v_t}
 =\frac{z_{t+3}z_{t+1}^{3}}{z_{t+2}^{3}z_t}.
\]
Equation (1) is equivalent to \(w_tw_{t+1}=1\). Iterating twice gives \(w_{t+2}=w_t\), and \(p\)-periodicity with odd \(p\) implies that all \(w_t\) equal a single \(w\in\{1,-1\}\). On the other hand, telescoping the definition yields \(\prod_{t\in\mathbb F_p}w_t=1\). Because \(p\) is odd, \(w=-1\) is impossible; therefore \(w_t=1\) for every \(t\). Hence \(v_t=\beta\) is independent of \(t\), where \(\beta\in\mathbb T\). The telescoping product of the \(v_t\) gives \(\beta^p=1\). Writing \(u_0=\alpha\), we have \(u_t=\alpha\beta^t\) for the standard representatives \(t=0,\ldots,p-1\). The telescoping product of the \(u_t\) gives \(\alpha^p\beta^{p(p-1)/2}=1\), and therefore \(\alpha^p=1\). A final telescoping step yields
\[
 z_t=z_0\alpha^t\beta^{t(t-1)/2}.
\]
Because \(\alpha\) and \(\beta\) are \(p\)-th roots of unity and \(2\) is invertible modulo \(p\), there are \(A,B\in\mathbb F_p\) with \(\alpha=\omega^{A+B}\), \(\beta=\omega^{2B}\). Consequently \(z_t=z_0\omega^{At+Bt^2}\), proving necessity.

**4. Sufficiency and exact count.** If \(f(t)=\lambda\omega^{At+Bt^2}\), then
\[
\mathcal E_p f(x,y)=\lambda\,\mathcal E_p{\bf1}(x+A,y+B).
\]
Translation permutes the target frequency pairs, so the sharp bound is attained, as it is by the constant function. If two parameter pairs \((A,B)\) and \((A',B')\) give projectively equivalent functions, evaluation at \(t=0\) forces the projective scalar to be \(1\); the polynomial \((A-A')t+(B-B')t^2\) then vanishes for all \(p\ge5\) values of \(t\), and must be identically zero. Thus the pairs are distinct, giving exactly \(p^2\) projective classes.

## Verification
The standalone `checker.py` uses exact integer arithmetic to enumerate all ordered triple fibers for primes \(5,7,11,13,17,19,23\). For each prime it verifies the identity \(\sum R_{s,r}^2=p^4+p^3-p^2\), the translated collision (1), and fiberwise phase alignment for every \((A,B)\in\mathbb F_p^2\). It also confirms that cubic chirps fail fiberwise alignment. These checks corroborate the normalization and proof; the infinite-prime classification is proved in Steps 1–4, not inferred from enumeration. The external sharp-norm and constant-modulus theorem is used explicitly from [1].

## Relationship to prior work
González-Riquelme and Oliveira e Silva [1, Theorem 1.3 and §6] established the sharp parabola sixth moment and necessity of constant modulus, without classifying all complex phases for that one-dimensional parabola. The classification here fills precisely that equality-set gap. Their Theorem 1.2 concerns the distinct two-dimensional paraboloid fourth moment. Biswas, Carneiro, Flock, Oliveira e Silva, Stovall and Tautges [2] studied the finite-field *moment-curve* \(L^2\)-to-\(L^{2d}\) endpoint: in dimension \(d=2\), this is a fourth moment, not the present sixth moment; in dimension \(d=3\), the support is the cubic curve in \(\mathbb F_p^3\). The subsequent work [3] concerns the same \(2d\) endpoint. Known finite-field sphere phase classifications concern different frequency supports and exponents. The new claim is a complete equality characterization, not a new sharp constant.

## Limitations
The nontrivial sharp norm and constant-modulus necessity are imported from the proved theorem [1]; they are not newly rederived here. The argument classifies phases only over prime fields of characteristic at least five, not arbitrary prime-power fields, and does not cover \(p=2,3\). The checker verifies seven small primes only. Possible earlier equivalent classifications under finite-field Strichartz, Freiman phases, or quadratic-chirp terminology remain a bibliographic risk, despite the cited comparisons; no external independent audit is claimed.

## References
[1] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first public 2024-05-26), Theorem 1.3 and §6; https://arxiv.org/abs/2405.16647 and https://arxiv.org/html/2405.16647v2.

[2] C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1 (2025), §§1.2–1.3; https://arxiv.org/html/2508.08377v1.

[3] C. Biswas et al., *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882v1 (2026), abstract; https://arxiv.org/abs/2609.29882.
