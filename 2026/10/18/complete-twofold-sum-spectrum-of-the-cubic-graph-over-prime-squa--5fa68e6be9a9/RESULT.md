# Complete twofold-sum spectrum of the cubic graph over prime-square rings

## Finding
For every prime \(p\ge5\), write \(R=\mathbb Z/p^2\mathbb Z\), and let \(C=\{(t,t^3):t\in R\}\subset R^2\). Define the ordered twofold-sum multiplicity
\[
r(x,y)=\#\{(a,b)\in R^2:a+b=x,\ a^3+b^3=y\}.
\]
The **complete** distribution of \(r\) over all \(p^4\) ordered targets \((x,y)\in R^2\) is

| Multiplicity | Number of targets |
|---:|---:|
| \(0\) | \(p^4-\frac{(p^2-p)^2+(p-1)^2}{2}-p^2\) |
| \(2\) | \(\frac{(p^2-p)^2}{2}\) |
| \(p\) | \(p^2-1\) |
| \(2p\) | \(\frac{(p-1)^2}{2}\) |
| \(p^2\) | \(1\) |

In particular the twofold sumset and ordered additive energy satisfy, respectively,
\[
|C+C|=\frac{p^4-2p^3+4p^2-2p+1}{2},\qquad
E(C)=\#\{(a,b,c,d)\in R^4:(a,a^3)+(b,b^3)=(c,c^3)+(d,d^3)\}
=6p^4-8p^3+3p^2.
\]
For the normalized extension sum \(\mathcal E 1(X,Y)=p^{-2}\sum_{t\in R}e^{2\pi i(Xt+Yt^3)/p^2}\), one consequently has the exact **constant-input** fourth moment
\[
\sum_{(X,Y)\in R^2}|\mathcal E 1(X,Y)|^4=6-\frac8p+\frac3{p^2}.
\]
This statement makes no assertion about the sharp \(L^2\to L^4\) operator norm for arbitrary coefficient functions.

## Assumptions and scope
Throughout, \(p\ge5\) is prime, the coefficient ring is exactly \(R=\mathbb Z/p^2\mathbb Z\), \(a,b,x,y\) range over \(R\), and \(\#\) counts ordered elements without quotienting by symmetry. Powers, reductions, and divisions by units are all performed in \(R\). In the Fourier identity, the ambient frequency group is \(R^2\) with counting measure; coefficients on \(C\) carry normalization \(1/|R|=p^{-2}\). No claim is made for \(p=2\), \(p=3\), higher prime powers, other polynomial graphs, or nonconstant extension data.

## Proof
Fix a target \((x,y)\). The first equation forces \(b=x-a\), and direct algebra gives
\[
a^3+(x-a)^3=\frac{x^3+3x(2a-x)^2}{4}.
\]
Since \(2\) and \(3\) are units in \(R\), the substitution \(u=2a-x\) is bijective. Consequently
\[
r(x,y)=\#\{u\in R:3xu^2=4y-x^3\}.\tag{1}
\]

**Unit first coordinate.** There are \(p^2-p\) unit values of \(x\). For each, division by \(3x\) makes (1) the square-root equation \(u^2=\Delta\), where \(\Delta=(4y-x^3)/(3x)\) runs bijectively over \(R\) as \(y\) does. Exactly \((p^2-p)/2\) values of \(\Delta\) are unit squares, each with exactly two square roots: every nonzero square in \(\mathbb F_p\) has two simple roots, each lifting uniquely by elementary Hensel lifting to a root modulo \(p^2\). The single value \(\Delta=0\) has exactly \(p\) roots, the elements divisible by \(p\). No other \(\Delta\) has a root: a square is either a unit with nonzero square reduction or divisible by \(p^2\). Therefore each unit \(x\) contributes \((p^2-p)/2\) targets with \(r=2\) and one with \(r=p\).

**Nonzero nonunit first coordinate.** Write \(x=pv\), where \(v\in\mathbb F_p^\times\), giving \(p-1\) distinct values. Here \(x^3=0\) in \(R\). By (1), \(r(x,y)=0\) unless \(y\) is divisible by \(p\), say \(y=pw\). Reduction of (1) modulo \(p\) yields \(3v u^2=4w\) in \(\mathbb F_p\). For \(w=0\), there is one root modulo \(p\) and thus exactly \(p\) lifts \(u\) modulo \(p^2\); for exactly \((p-1)/2\) nonzero \(w\) the reduction is a nonzero square and has two roots, each admitting \(p\) lifts. Hence each such \(x\) contributes one target with \(r=p\) and \((p-1)/2\) targets with \(r=2p\), and no others.

**Zero first coordinate.** Equation (1) becomes \(0=4y\). It has \(p^2\) roots exactly at \((x,y)=(0,0)\), and none for \(y\ne0\).

The three cases partition all \(x\in R\), and their nonzero multiplicities are distinct since \(p\ge5\). Summing the contributions gives the displayed complete histogram, including the zero count by subtraction from \(p^4\). The number of targets with \(r>0\) is
\[
\frac{(p^2-p)^2}{2}+(p^2-1)+\frac{(p-1)^2}{2}+1=\frac{p^4-2p^3+4p^2-2p+1}{2}.
\]
Likewise the sum of squared multiplicities is
\[
4\frac{(p^2-p)^2}{2}+p^2(p^2-1)+4p^2\frac{(p-1)^2}{2}+p^4
=6p^4-8p^3+3p^2.
\]
Finally, finite-group character orthogonality applied to the expanded fourth power gives \(\sum_{R^2}|\mathcal E1|^4=p^{-4}\sum_{R^2}r(x,y)^2\), proving the moment identity.

## Verification
The accompanying file `verify.py` independently constructs every ordered pair \((a,b)\) for each \(p\in\{5,7,11,13,17\}\), bins its sum \((a+b,a^3+b^3)\bmod p^2\), and checks the predicted full histogram, total multiplicity and energy using integers only. The saved `verification_output.txt` is the matching output of that program. These finite tests corroborate the algebraic proof for all primes \(p\ge5\) but do not substitute for it. The empty fibers are included explicitly, and no floating-point computation is used.

## Relationship to prior work
González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields* (first posted 26 May 2024), develop the convolution-fiber viewpoint in sharp extension problems over finite **fields**; their primary theorems treat parabola, paraboloid and conic models, not the present cubic graph over the nonreduced ring \(\mathbb Z/p^2\mathbb Z\). Existing studies of exponential spectra of this cubic graph concern orthogonal Fourier bases, a different invariant: a spectrum classification does not yield the targetwise ordered two-sum multiplicities above. Known exact finite-field cubic-graph extension results do not imply this prime-square ring histogram, since reduction modulo \(p\) neither fixes the lifting counts nor distinguishes the \(p\), \(2p\), and \(p^2\) singular fiber strata.

## Limitations
The theorem concerns the precise prime-square level and constant-input fourth moment; it is **not** a sharp extension inequality for arbitrary inputs. Its square-root classification relies on the invertibility of \(2\) and \(3\), and needs reanalysis at those characteristics and at thicker prime-power rings. Search-based originality is provisional rather than proof of absolute priority; an unlocated equivalent prime-square cubic-convolution calculation is a residual risk.

## References
1. Cristian González-Riquelme and Diogo Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first posted 2024-05-26. https://arxiv.org/abs/2405.16647 .
2. *All exponential spectra of the cubic graph over prime-square cyclic rings*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-all-exponential-spectra-of-the-cubic-graph-over-prime-square-cyc--a783058468ac (related orthogonal-basis classification, not a two-sum census).
3. *Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b (field case only).
