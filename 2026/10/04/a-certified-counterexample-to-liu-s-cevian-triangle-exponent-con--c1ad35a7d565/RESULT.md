# A certified counterexample to Liu’s Cevian-triangle exponent conjecture at \(k=21/10\)
## Finding
Jian Liu's 2012 Cevian-triangle Conjecture 3.9 asserts, in the notation below, that for every interior point and every \(k\ge 2.1\),
\[
e_1^k+e_2^k+e_3^k\ge 2r^k+(2r_q)^k.
\]
The conjecture already fails at its endpoint \(k=21/10\).

Take
\[
A=(0,0),\qquad B=(1,0),\qquad C=(1,h),\qquad h=\frac1{100},
\]
and let \(P\) have barycentric coordinates
\[
\left(\varepsilon,\frac{1-\varepsilon}2,\frac{1-\varepsilon}2\right),\qquad \varepsilon=\frac3{2000}.
\]
All three barycentric coordinates are positive, so \(P\) is strictly interior. Let \(L=AP\cap BC\), \(M=BP\cap CA\), \(N=CP\cap AB\), set \(e_1=PL\), \(e_2=PM\), \(e_3=PN\), let \(r\) be the inradius of \(ABC\), and let \(r_q\) be the inradius of \(LMN\). Then
\[
e_1^{21/10}+e_2^{21/10}+e_3^{21/10}-2r^{21/10}-(2r_q)^{21/10}<0.
\]
Thus this explicit nondegenerate configuration reverses the proposed inequality.

## Assumptions and scope
The statement concerns ordinary Euclidean triangles and the Cevian triangle of a strictly interior point. No acuteness assumption is imposed in Liu's Conjecture 3.9. The present result disproves the universal assertion at \(k=21/10\); it does not classify which larger exponents, if any, may still be valid.

For a useful one-parameter view, keep the right triangle \(A=(0,0)\), \(B=(1,0)\), \(C=(1,h)\) and set \(\varepsilon=(3/20)h\). For sufficiently small \(h>0\), the point defined by the same barycentric pattern remains interior.

## Proof
Write
\[
q=\frac{1-\varepsilon}{1+\varepsilon}.
\]
The barycentric definition gives
\[
P=\left(1-\varepsilon,\frac{(1-\varepsilon)h}2\right),\quad
L=\left(1,\frac h2\right),\quad
M=(q,qh),\quad N=(q,0).
\]
Therefore
\[
\begin{aligned}
e_1&=\varepsilon\sqrt{1+\frac{h^2}4},\
e_2&=\frac{1-\varepsilon}{2(1+\varepsilon)}
\sqrt{4\varepsilon^2+(1-\varepsilon)^2h^2},\
e_3&=\frac{1-\varepsilon}{2(1+\varepsilon)}
\sqrt{4\varepsilon^2+(1+\varepsilon)^2h^2}.
\end{aligned}
\]
Because \(ABC\) is right with legs \(1\) and \(h\),
\[
r=\frac{1+h-\sqrt{1+h^2}}2.
\]
For \(LMN\), the side \(MN\) has length \(qh\), its altitude from \(L\) is \(1-q\), and hence
\[
[LMN]=\frac12qh(1-q)=\frac{\varepsilon(1-\varepsilon)h}{(1+\varepsilon)^2}.
\]
The other two sides are
\[
LN=\sqrt{(1-q)^2+\frac{h^2}4},\qquad
LM=\sqrt{(1-q)^2+\left(qh-\frac h2\right)^2}.
\]
Consequently
\[
r_q=\frac{2[LMN]}{MN+LN+LM}.
\]
Substituting \(h=1/100\), \(\varepsilon=3/2000\), and \(k=21/10\) into these exact formulas reduces the claimed reversal to comparisons among rational numbers, square roots, and positive tenth roots. The bundled verifier encloses every radical by rational endpoints certified with integer-power comparisons and propagates those intervals monotonically. It obtains the strict enclosure
\[
-1.74207356618004\times10^{-7}
<e_1^{21/10}+e_2^{21/10}+e_3^{21/10}-2r^{21/10}-(2r_q)^{21/10}
<-1.74207356618003\times10^{-7},
\]
so the upper endpoint is already negative.

The same construction is not isolated. If \(\varepsilon=(3/20)h\) and \(h\to0^+\), then
\[
\frac{e_1}h\to\frac3{20},\qquad
\frac{e_2}h,\frac{e_3}h\to\frac{\sqrt{109}}{20},\qquad
\frac rh\to\frac12,
\]
and
\[
\frac{2r_q}h\to\frac3{5+\sqrt{34}}.
\]
Hence the normalized defect tends to
\[
\left(\frac3{20}\right)^{21/10}
+2\left(\frac{\sqrt{109}}{20}\right)^{21/10}
-2\left(\frac12\right)^{21/10}
-\left(\frac3{5+\sqrt{34}}\right)^{21/10},
\]
which the same exact interval procedure encloses in a strictly negative interval around \(-0.00468260451397836\). Continuity therefore gives counterexamples for all sufficiently small positive \(h\).

## Verification
Run `python3 verify.py`. The program uses only the Python standard library. Its acceptance conditions use `fractions.Fraction` and integer comparisons; decimal output is display only. It independently checks the explicit finite configuration and the normalized boundary limit, and terminates with `CERTIFIED_NEGATIVE` only when the exact rational upper endpoints of both defect intervals are negative.

The verification is a finite exact certificate for the displayed counterexample. The asymptotic family additionally uses only the coordinate formulas above and continuity.

## Relationship to prior work
Liu's 2012 article *A pedal triangle inequality with the exponents* introduces the Cevian notation \(e_1,e_2,e_3,r_q\) and states Conjecture 3.9 with the threshold \(k\ge2.1\). The present result addresses precisely that Cevian conjecture by giving a certified counterexample at the threshold itself.

Later literature with closely related titles was checked for implication coverage. Huang's 2018 open-access paper proves two pedal-triangle conjectures from the same general line of work, but its objects and conclusions concern pedal triangles rather than the Cevian inequality above. Yang, Chen, Huang, Wang, and Lin's 2017 paper proves a different parameterized inequality for vertex and sideline distances; its full text does not use the Cevian quantities in the present claim. Published-finding searches for the formula, the exponent threshold, and Cevian aliases returned no statement implying this counterexample.

These searches do not prove absolute novelty. Older or poorly indexed triangle-inequality literature could still contain an equivalent counterexample under different notation.

## Limitations
The result disproves the universal range beginning at \(2.1\), but does not determine the optimal exponent range. It also does not address Liu's Cevian Conjectures 3.7 or 3.8. The original 2012 host currently returned a broken direct PDF link during source checking; the target statement was available through indexed full-text extraction and independent bibliographic metadata, while later plausible full texts were checked separately.

## References
1. Jian Liu, *A pedal triangle inequality with the exponents*, International Journal of Open Problems in Computer Science and Mathematics 5(4) (2012), 16–24. DOI: 10.12816/0006135.
2. Fangjian Huang, *Two inequalities about the pedal triangle*, Journal of Inequalities and Applications 2018:72 (2018). DOI: 10.1186/s13660-018-1661-7.
3. Yong Yang, Shengli Chen, Dong Huang, Xiang Wang, Xiaoguang Lin, *Proof of an inequality conjecture for a point in the plane of a triangle*, Journal of Mathematical Inequalities 11(2) (2017), 399–411. DOI: 10.7153/jmi-11-34.
4. Jian Liu, *On inequality \(R_p<R\) of the pedal triangle*, Mathematical Inequalities & Applications 16(3) (2013), 701–715. DOI: 10.7153/mia-16-53.
