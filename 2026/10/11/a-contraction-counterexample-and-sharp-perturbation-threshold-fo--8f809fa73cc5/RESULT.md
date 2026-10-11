# A contraction counterexample and sharp perturbation threshold for continuous \(K\)-\(g\)-fusion frames
## Finding
The perturbation theorem labeled Theorem 4.1 in Alizadeh--Rahimi--Osgooei--Rahmani is false when the controlling operator is a strict contraction. In the notation of that theorem, let
\[
V=\left(\int_\Omega v(\omega)^2\,d\mu(\omega)\right)^{1/2}.
\]
The correct uniform sufficient condition is
\[
\varepsilon V<(1-\lambda_1)\sqrt A,
\]
not the published condition with the extra factor \(\|K\|\). Under this corrected condition the perturbed family has the lower bound
\[
\left(\frac{(1-\lambda_1)\sqrt A-\varepsilon V}{1+\lambda_2}\right)^2
\]
and the upper bound
\[
\left(\frac{(1+\lambda_1)\sqrt B+\varepsilon V\|K\|}{1-\lambda_2}\right)^2.
\]
The strict lower threshold is sharp as a universal condition determined only by \(A\), \(\lambda_1\), \(\varepsilon\), and \(V\).

## Assumptions and scope
Use the source definition of a continuous \(K\)-\(g\)-fusion frame: for a Hilbert space \(H\), a bounded operator \(K\), measurable subspaces \(F(\omega)\), coefficient operators \(\Lambda_\omega\), and weight \(v\), there are \(0<A\le B<\infty\) such that
\[
A\|K^*h\|^2\le X(h)^2\le B\|h\|^2,
\qquad
X(h)^2=\int_\Omega v(\omega)^2\|\Lambda_\omega\pi_{F(\omega)}h\|^2\,d\mu(\omega).
\]
For a perturbation \(\widetilde\Lambda,\widetilde F,\widetilde v\), write
\[
Y(h)^2=\int_\Omega \widetilde v(\omega)^2\|\widetilde\Lambda_\omega\pi_{\widetilde F(\omega)}h\|^2\,d\mu(\omega).
\]
The source perturbation hypothesis is the pointwise inequality
\[
\|a_\omega(h)-b_\omega(h)\|\le
\lambda_1\|a_\omega(h)\|+\lambda_2\|b_\omega(h)\|+\varepsilon v(\omega)\|K^*h\|,
\]
where \(a_\omega(h)=v(\omega)\Lambda_\omega\pi_{F(\omega)}h\) and \(b_\omega(h)=\widetilde v(\omega)\widetilde\Lambda_\omega\pi_{\widetilde F(\omega)}h\), with \(0\le\lambda_1<1\), \(0<\lambda_2<1\), and \(\varepsilon>0\).

## Proof
Minkowski's inequality applied to the source perturbation inequality gives
\[
Y(h)\le (1+\lambda_1)X(h)+\lambda_2Y(h)+\varepsilon V\|K^*h\|.
\]
Using \(X(h)\le\sqrt B\|h\|\) and \(\|K^*h\|\le\|K\|\|h\|\) yields
\[
Y(h)\le
\frac{(1+\lambda_1)\sqrt B+\varepsilon V\|K\|}{1-\lambda_2}\|h\|.
\]
For the lower estimate, the reverse triangle inequality gives
\[
Y(h)\ge (1-\lambda_1)X(h)-\lambda_2Y(h)-\varepsilon V\|K^*h\|.
\]
Since \(X(h)\ge\sqrt A\|K^*h\|\),
\[
(1+\lambda_2)Y(h)\ge
\big((1-\lambda_1)\sqrt A-\varepsilon V\big)\|K^*h\|.
\]
The corrected strict smallness condition makes the coefficient positive and proves the stated lower bound.

To disprove the published statement, let \(\Omega\) be a one-point measure space of mass \(1\), let \(H=\mathbb C\), and set
\[
K=\tfrac12 I,\quad v=\widetilde v=1,\quad F=\widetilde F=H,\quad
\Lambda=I,\quad\widetilde\Lambda=0.
\]
For the original family, \(X(h)^2=|h|^2\). The certified bounds \(A=B=4\) are valid because
\[
4\|K^*h\|^2=|h|^2\le X(h)^2=|h|^2\le4|h|^2.
\]
Choose \(\lambda_1=\lambda_2=\tfrac12\) and \(\varepsilon=\tfrac32\). The pointwise perturbation inequality becomes
\[
|h|\le\tfrac12|h|+\tfrac32\cdot\tfrac12|h|=\tfrac54|h|,
\]
so it holds. The published smallness hypothesis also holds:
\[
(1-\lambda_1)\sqrt A-\varepsilon\|K\|V
=1-\tfrac34=\tfrac14>0.
\]
However, \(Y(h)=0\) for every \(h\), while \(K\ne0\); therefore no positive lower continuous \(K\)-\(g\)-fusion-frame bound exists.

Sharpness of the corrected threshold follows from the same scalar construction. Given \(A>0\) and \(\varepsilon V\ge(1-\lambda_1)\sqrt A\), take a one-point space with weight \(V>0\), choose a sufficiently small scalar \(K=kI\) with \(0<k<1\), and choose \(\Lambda=(\sqrt A\,k/V)I\). Then the original lower inequality is an equality, one may take an upper bound at least \(A\), and \(\widetilde\Lambda=0\) satisfies the perturbation inequality. By choosing \(k\) small enough, the published condition with the extra factor \(\|K\|=k\) also holds whenever its strict inequality is required. Thus no universal theorem with a weaker threshold in these parameters can guarantee a positive lower bound.

## Verification
The counterexample is symbolic and one-dimensional. Substitution verifies the original frame inequalities, the perturbation inequality, and the source's displayed smallness condition exactly. The repaired lower and upper estimates follow directly from the two triangle inequalities above. No finite experiment is used as evidence for an infinite statement.

The source proof itself reaches the inequality
\[
Y(h)\ge(1-\lambda_1)X(h)-\lambda_2Y(h)-\varepsilon V\|K^*h\|,
\]
but then replaces its coefficient by a formula involving \(\|K\|-1\). That replacement is valid as a positive estimate only in an appropriate \(\|K\|>1\) regime. At \(\|K\|=1\) its displayed lower constant becomes zero, and for \(0<\|K\|<1\) the published hypothesis can be too weak, as the counterexample shows.

## Relationship to prior work
The target source is Alizadeh--Rahimi--Osgooei--Rahmani, *Continuous K-G-Fusion Frames in Hilbert Spaces*, DOI 10.26837/jaem.606439. Its Definition 4.1 and Theorem 4.1 contain the pointwise perturbation model, the \(\|K\|\)-weighted smallness condition, and the displayed lower bound involving \(\|K\|-1\).

The same authors' earlier *Continuous K-g-Frames in Hilbert Spaces*, DOI 10.1007/s41980-018-0186-7, has a different perturbation theorem formulated through quadratic operator differences; its lower threshold is of the form \((1-\lambda_1)A-\gamma>0\) and does not imply the present pointwise fusion-frame correction or counterexample.

Nhari--Park--Rossafi, *Continuous K-g-fusion frames in Hilbert C*-modules*, DOI 10.20956/j.v19i2.23961, later proves a module-valued perturbation theorem with the structurally matching threshold \(\varepsilon<(1-\lambda_1)\sqrt A\) for its global perturbation norm. That theorem is in a different setting and includes an additional complemented-range hypothesis; it does not state the failure of the 2021 Hilbert-space theorem or the scalar sharpness construction above.

## Limitations
The correction concerns exactly the perturbation model of Definition 4.1 and the frame bounds supplied as input to Theorem 4.1. It does not claim that the displayed upper bound is optimal. The sharpness statement is universal with respect to the listed scalar parameters: once the corrected strict threshold fails, singleton scalar examples can destroy the lower frame bound. A separate source with an unindexed erratum or informal correction could reduce originality risk, but no such source was located in the checked literature.

## References
1. E. Alizadeh, A. Rahimi, E. Osgooei, M. Rahmani, *Continuous K-G-Fusion Frames in Hilbert Spaces*, TWMS J. App. Eng. Math. 11 (2021), 44--55. DOI 10.26837/jaem.606439. Public PDF: https://jaem.isikun.edu.tr/web/images/articles/vol.11.no.1/05.pdf
2. E. Alizadeh, A. Rahimi, E. Osgooei, M. Rahmani, *Continuous K-g-Frames in Hilbert Spaces*, Bull. Iranian Math. Soc. 45 (2019), 1091--1104. DOI 10.1007/s41980-018-0186-7.
3. F.-d. Nhari, C. Park, M. Rossafi, *Continuous K-g-fusion frames in Hilbert C*-modules*, J. Mat. Stat. Komputasi 19 (2023), 240--265. DOI 10.20956/j.v19i2.23961.
