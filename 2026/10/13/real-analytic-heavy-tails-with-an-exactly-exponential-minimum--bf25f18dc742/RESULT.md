# Real-analytic heavy tails with an exactly exponential minimum
## Finding
There exist independent nonnegative heavy-tailed random variables \(X_1,X_2\), each supported on \([0,\infty)\), with strictly positive real-analytic hazard rates and strictly positive real-analytic densities on \((0,\infty)\), such that
\[
\min(X_1,X_2)\sim\operatorname{Exp}(1).
\]
An explicit choice is
\[
t(x)=\log\log(x+e^e),\qquad x\ge 0,
\]
\[
h_1(x)=\frac{1}{1+\exp(-2t(x)\sin t(x))},\qquad h_2(x)=1-h_1(x),
\]
and
\[
R_i(x)=\int_0^x h_i(u)\,du,\qquad \overline F_i(x)=\exp(-R_i(x)).
\]
Both hazards satisfy \(0<h_i(x)<1\), are real-analytic on a neighborhood of \([0,\infty)\), and obey \(h_1(x)+h_2(x)=1\). Consequently the factor distributions have no atoms or support gaps, their cumulative hazards have no flat intervals, and their densities
\[
f_i(x)=h_i(x)e^{-R_i(x)}
\]
are strictly positive and real-analytic for \(x>0\).

## Assumptions and scope
Heavy-tailed means that \(\mathbb E e^{\lambda X}=\infty\) for every \(\lambda>0\). The construction concerns two independent factors and the unit-rate exponential target. It is a regularity refinement of the recent minimum-factorization phenomenon, not a claim that ordinary long-tailed, regularly varying, or subexponential factors can have a light-tailed minimum.

## Proof
Because \(t(x)\) is real-analytic and increasing for \(x\ge0\), the functions \(h_1,h_2\) are real-analytic and strictly between \(0\) and \(1\). Their primitives \(R_i\) and the resulting densities are therefore real-analytic on the interior of the half-line. Also,
\[
h_1(x)+h_2(x)=1,
\]
so
\[
R_1(x)+R_2(x)=x.
\]
For independent \(X_1,X_2\),
\[
\mathbb P\{\min(X_1,X_2)>x\}=e^{-R_1(x)}e^{-R_2(x)}=e^{-x},
\]
which proves the exact \(\operatorname{Exp}(1)\) minimum.

It remains to prove that each factor is proper and heavy-tailed. Put
\[
\chi(s)=e^{e^s}-e^e,
\]
so that \(t(\chi(s))=s\). For
\[
A_k=\frac{7\pi}{6}+2\pi k,\qquad B_k=\frac{11\pi}{6}+2\pi k,
\]
we have \(\sin s\le-1/2\) on \([A_k,B_k]\). Hence, for \(x\in[\chi(A_k),\chi(B_k)]\),
\[
h_1(x)\le e^{-t(x)}\le e^{-A_k}.
\]
Writing \(a_k=\chi(A_k)\) and \(b_k=\chi(B_k)\), and using \(h_1\le1\),
\[
\frac{R_1(b_k)}{b_k}
\le
\frac{a_k}{b_k}+e^{-A_k}\left(1-\frac{a_k}{b_k}\right)
\longrightarrow 0.
\]
The ratio \(a_k/b_k\to0\) because \(e^{e^{A_k}}/e^{e^{B_k}}\to0\). Similarly, on
\[
A'_k=\frac{\pi}{6}+2\pi k,\qquad B'_k=\frac{5\pi}{6}+2\pi k
\]
for sufficiently large \(k\), \(\sin s\ge1/2\), so \(h_2(x)\le e^{-t(x)}\le e^{-A'_k}\) on \([\chi(A'_k),\chi(B'_k)]\), and the same argument gives
\[
\liminf_{x\to\infty}\frac{R_2(x)}x=0.
\]
On the complementary-sign intervals, respectively, \(h_1\ge1/2\) and \(h_2\ge1/2\) over intervals whose \(x\)-lengths diverge. Thus \(R_i(x)\to\infty\), so both survivals tend to zero and define proper distributions.

Finally, fix \(\lambda>0\). Along a sequence \(x_m\to\infty\) with \(R_i(x_m)/x_m\to0\),
\[
\mathbb E e^{\lambda X_i}
\ge e^{\lambda x_m}\mathbb P\{X_i\ge x_m\}
=e^{\lambda x_m-R_i(x_m)}\longrightarrow\infty.
\]
Therefore both factors are heavy-tailed.

## Verification
The proof is analytic. The exact-minimum identity follows from addition of cumulative hazards. Properness is checked by explicit intervals on which each hazard is at least \(1/2\). Heavy-tailedness follows from explicit subsequences on which the cumulative-hazard ratio tends to zero and the elementary exponential-moment lower bound above. No finite computation or numerical experiment is used as a proof of an infinite-tail assertion.

## Relationship to prior work
Leipus, Šiaulys, and Konstantinides (2023) gave the first explicit example of two independent heavy-tailed variables with a light-tailed minimum; their displayed tails alternate between different formulas on factorial intervals. Foss, Tarasenko, and Krivtsov (arXiv:2505.08954, first posted 13 May 2025; later Journal of Applied Probability, DOI 10.1017/jpr.2025.10058) proved the phenomenon is universal for targets with right-unbounded support. Their proof explicitly constructs cumulative hazards by “taking turns,” freezing one risk function on alternating intervals while the other follows the target. Foss, Scheutzow, and Tarasenko (arXiv:2603.06452) then characterized the necessary segmented-heavy-tail structure and gave further piecewise cumulative-hazard constructions.

The present statement does not strengthen the universality theorem in target scope. It sharpens the regularity side: even for the canonical exponential target, both heavy-tailed factors can have strictly positive real-analytic hazards and densities, so segmentation need not arise from literal flat pieces, jumps, gaps, or nonsmooth hazards.

## Limitations
The claim is only for an explicit pair of factors with target \(\operatorname{Exp}(1)\). It does not show that every light-tailed target admits real-analytic heavy-tailed factors, nor that the factors belong to long-tailed, regularly varying, or subexponential classes. In fact, the recent segmented-tail theory rules out several standard heavy-tailed subclasses in this setting. A non-indexed note could contain an equivalent smooth or analytic regularization; targeted searches and the inspected primary texts did not locate one.

## References
1. S. Foss, A. Tarasenko, G. Krivtsov, “Any random variable with right-unbounded distributional support is the minimum of independent and very heavy-tailed random variables,” arXiv:2505.08954; Journal of Applied Probability, DOI 10.1017/jpr.2025.10058.
2. S. Foss, M. Scheutzow, A. Tarasenko, “Only Segmented Heavy Tails Can Produce a Light-Tailed Minimum,” arXiv:2603.06452.
3. R. Leipus, J. Šiaulys, D. Konstantinides, “Minimum of heavy-tailed random variables is not heavy tailed,” AIMS Mathematics 8 (2023), 13066–13072, DOI 10.3934/math.2023658.
