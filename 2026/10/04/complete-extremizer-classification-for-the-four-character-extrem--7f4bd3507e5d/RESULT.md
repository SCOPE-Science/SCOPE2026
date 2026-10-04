# Complete extremizer classification for the four-character extreme set in \(\mathbb Z_5\)
## Finding
Let \(E=\{0,1,2,3\}\subset\mathbb Z_5\), let \(\omega=e^{2\pi i/3}\), and write
\[
\mu=\sum_{j=0}^{3}a_j\delta_j.
\]
A nonzero measure \(\mu\) supported exactly on \(E\) is extremal if and only if there are \(c\in\mathbb C\setminus\{0\}\), a fifth root of unity \(t\), and \(\varepsilon\in\{1,2\}\) such that
\[
(a_0,a_1,a_2,a_3)=c\,(1,t\omega^{\varepsilon},t^2\omega^{\varepsilon},t^3).
\]
Thus, after the normalization \(a_0=1\), there are exactly ten extremal measures. Multiplication of the coefficient at \(j\) by a character value \(s^j\), where \(s^5=1\), is transitive on each five-element family, and complex conjugation exchanges the two families.

The support \(E\) was already known to be extremal, hence to have Sidon constant \(2\). The new assertion here is the complete classification of the equality cases on this fixed support, not the value of its Sidon constant.
## Assumptions and scope
The group is \(\mathbb Z_5\), with Fourier transform
\[
\widehat\mu(k)=\sum_{j=0}^{3}a_j e^{-2\pi i jk/5},\qquad k\in\mathbb Z_5.
\]
Extremality is used in the standard Sidon-set sense: a nonzero measure on a finite support \(E\) is extremal when
\[
\|\widehat\mu\|_{\infty}=\frac{\|\mu\|}{\sqrt{|E|}}.
\]
Scaling by a nonzero scalar preserves extremality. The known equality criterion for extremal measures says that the coefficient moduli are constant on the support and the Fourier-transform modulus is constant on the dual group. After dividing by \(a_0\), it therefore suffices to classify unit-modulus triples \((x,y,z)\) for the length-five sequence \((1,x,y,z,0)\) having flat Fourier modulus.
## Proof
Normalize \(a_0=1\), and put \(x=a_1\), \(y=a_2\), \(z=a_3\), so \(|x|=|y|=|z|=1\). Flat Fourier modulus is equivalent, by the cyclic autocorrelation identity, to vanishing of the nonzero cyclic autocorrelations. Up to conjugation there are only two equations:
\[
C_1=x+y\overline{x}+z\overline{y}=0,
\]
\[
C_2=y+z\overline{x}+\overline{z}=0.
\]
The three summands in \(C_1\) all have modulus one. Three unit complex numbers sum to zero exactly when they are a common unit scalar times the three cube roots of unity. Hence there are \(t\in\mathbb T\) and a permutation \((p,q,r)\) of \((0,1,2)\) such that
\[
x=t\omega^p,\qquad y\overline{x}=t\omega^q,\qquad z\overline{y}=t\omega^r.
\]
Consequently
\[
x=t\omega^p,\qquad y=t^2\omega^{p+q},\qquad z=t^3,
\]
because \(p+q+r=3\). Substitution into \(C_2\) gives
\[
0=t^2\bigl(\omega^{p+q}+\omega^{-p}\bigr)+t^{-3}.
\]
Since \((p,q,r)\) is a permutation, \(\omega^{p+q}=\omega^{-r}\), and
\[
\omega^{-r}+\omega^{-p}=-\omega^{-q}.
\]
Thus
\[
t^5=\omega^q.
\]
There is a harmless redundancy in the representation of the three equilateral summands: replacing
\[
(t,p,q,r)
\]
by
\[
(t\omega^q,p-q,0,r-q)
\]
leaves \(x\), \(y\), and \(z\) unchanged. For the new scalar \(t'=t\omega^q\),
\[
(t')^5=t^5\omega^{5q}=\omega^{q}\omega^{2q}=1.
\]
The two remaining residues are \(1\) and \(2\). Therefore every normalized solution is
\[
(1,t'\omega^{\varepsilon},(t')^2\omega^{\varepsilon},(t')^3),
\qquad (t')^5=1,\quad \varepsilon\in\{1,2\}.
\]
Conversely, for either value of \(\varepsilon\) and every fifth root \(t\), the three terms of \(C_1\) are \(t\omega^{\varepsilon}\), \(t\), and \(t\omega^{-\varepsilon}\), so they sum to zero. Also, using \(t^5=1\),
\[
C_2=t^2\bigl(\omega^{\varepsilon}+\omega^{-\varepsilon}+1\bigr)=0.
\]
Hence all four nonzero cyclic autocorrelations vanish, so the Fourier modulus is constant. This proves both necessity and sufficiency.

The two choices of \(\varepsilon\) and the five choices of \(t\) give ten distinct normalized vectors. Character modulation sends \(t\) to another fifth root without changing \(\varepsilon\), while conjugation sends \((t,\varepsilon)\) to \((\overline t,3-\varepsilon)\).
## Verification
The accompanying `verify.py` performs an exact exponent calculation in the group of fifteenth roots of unity. It independently enumerates every branch produced by the equilateral-triple lemma, imposes \(t^5=\omega^q\), and confirms that the resulting normalized coefficient vectors are exactly the ten vectors in the displayed two-family formula. It also verifies that the two nonzero autocorrelation equations reduce in every case to a rotated copy of
\[
1+\omega+\omega^2=0.
\]
The script additionally identifies the two sample measures recorded in the later literature as members of the two classified families.
## Relationship to prior work
Graham and Ramsey proved in 1981 that \(\{0,1,2,3\}\subset\mathbb Z_5\) is an extremal four-element set and classified the possible four-element extremal supports up to their stated support operations. Their Proposition 3.2 is a support-level classification; it does not state a classification of every coefficient vector giving an extremal measure on this support.

Graham's later survey/preprint gives the general criterion that an extremal measure has constant coefficient modulus and constant Fourier modulus. It treats the analogous three-element support in \(\mathbb Z_4\) by explicitly classifying all extremal measures, but for \(\{0,1,2,3\}\subset\mathbb Z_5\) Proposition 7.5 supplies a witness rather than a complete equality-case list. A separate remark records two different witnesses for the same \(\mathbb Z_5\) support: one using third roots and another using fifteenth roots. The theorem above explains that nonuniqueness completely: after fixing the mass at zero, those examples lie in two five-element modulation orbits, and there are no others.

Neuwirth's work on maximum-modulus and Sidon-constant problems for trigonometric trinomials provides nearby phase-extremal context, but concerns three integer frequencies on the continuous circle rather than the complete coefficient classification for this four-point finite cyclic support.
## Limitations
The result is specific to the support \(\{0,1,2,3\}\) in \(\mathbb Z_5\); it does not classify extremal measures on other four-element supports or on complements in larger cyclic groups. The proof uses the special fact that each relevant nonzero cyclic autocorrelation has exactly three unit summands, forcing equilateral cancellation.

The 1981 article is older than the exact day-level electronic source record used for `first_public_date`; its inspected bibliographic records give the 1981 issue and received date but not a verified day on which it first became publicly available. No such day has been inferred. The day-level dated source used here is HAL version 1 of Neuwirth's paper, submitted on 2007-03-08 and carrying primary MSC 42A05.
## References
1. C. C. Graham and L. T. Ramsey, *Sidon sets with extremal Sidon constants*, Proceedings of the American Mathematical Society 83 (1981), 522-526. DOI: 10.1090/S0002-9939-1981-0627683-3.
2. C. C. Graham, *A beastiary of sets having extremal Sidon constant, or, there must be more than one theorem somewhere here*, arXiv:1910.00924v1, 2019-10-01.
3. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, HAL hal-00135804v1, submitted 2007-03-08; Journal d'Analyse Mathematique 104 (2008), 371-396.
