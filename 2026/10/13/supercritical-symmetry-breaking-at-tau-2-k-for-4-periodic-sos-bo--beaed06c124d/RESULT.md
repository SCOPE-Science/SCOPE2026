# Supercritical symmetry breaking at \(\tau_2(k)\) for 4-periodic SOS boundary laws
## Finding
For the ferromagnetic SOS model on the Cayley tree of order \(k\ge2\), consider the 4-periodic boundary laws \(u_{2m}=1\), \(u_{4m-1}=a\), \(u_{4m+1}=b\) satisfying \((a+b-\tau)a^k+\tau a-2=0\) and \((a+b-\tau)b^k+\tau b-2=0\). Let \(\tau_2(k)\) be the larger intersection value singled out in Lemma 3 of Haydarov--Rozikov, and put \(x_k=2k/((k-1)\tau_2(k))\). Then the symmetric solution \((a,b)=(x_k,x_k)\) has a locally supercritical \(a\leftrightarrow b\) pitchfork at \(\tau=\tau_2(k)\). There is \(\varepsilon_k>0\) such that for \(\tau_2(k)<\tau<\tau_2(k)+\varepsilon_k\) exactly two unequal positive solutions lie near \((x_k,x_k)\), exchanged by \(a\leftrightarrow b\), whereas for \(\tau_2(k)-\varepsilon_k<\tau\le\tau_2(k)\) there is no unequal solution in that neighborhood. Moreover
\[
|a-b|=A_k\sqrt{\tau-\tau_2(k)}+O((\tau-\tau_2(k))^{3/2}),
\]
where
\[
A_k=2\sqrt{\frac{3x_k^3(k-1)\,[k-(k+1)x_k^2]}{k\,[3k^2-(3k^2-k+2)x_k^2]}}>0.
\]
The two unequal boundary laws are cyclic shifts of one another and therefore define the same translation-invariant gradient Gibbs measure. In particular, for every \(k\ge4\) this gives a genuinely 4-height-periodic gradient Gibbs measure for all \(\tau\) sufficiently just above \(\tau_2(k)\), a local existence result in the range for which the motivating source leaves the unequal 4-periodic problem open. No global count of unequal solutions away from this bifurcation is asserted.

## Assumptions and scope
The model is the standard ferromagnetic solid-on-solid model on a Cayley tree of order \(k\ge2\), with \(\tau=\theta+\theta^{{-1}}=2\cosh(\beta)>2\). We use the 4-periodic height boundary law of Haydarov and Rozikov,
\[
u_{{2m}}=1,\qquad u_{{4m-1}}=a,\qquad u_{{4m+1}}=b,
\]
whose positive parameters satisfy
\[
(a+b-\tau)a^k+\tau a-2=0,\qquad (a+b-\tau)b^k+\tau b-2=0.
\]
The source defines a second distinguished value \(\tau_2(k)>2(k+1)/(k-1)\) at which its symmetric fixed-point polynomial and unequal-cycle polynomial share a root. The claim here is strictly local near that intersection; it does not classify all 4-periodic solutions for \(k\ge4\).

Put
\[
x=x_k=\frac{{2k}}{{(k-1)\tau_2(k)}}.
\]
At the shared root, the symmetric boundary-law equation and the transverse degeneracy imply
\[
(k-1)x^{{k+1}}-kx^{{k-1}}+1=0,
\]
so
\[
x^{{k-1}}\bigl(k-(k-1)x^2\bigr)=1.
\]
Because \(\tau_2(k)>2(k+1)/(k-1)\), one has \(0<x<k/(k+1)\).

## Proof
Set
\[
s=\frac{{a+b}}2,\qquad d=\frac{{a-b}}2,
\]
and write the sum and divided difference of the two boundary-law equations as
\[
G(s,d,\tau)=(2s-\tau)\frac{{(s+d)^k+(s-d)^k}}2+\tau s-2,
\]
\[
H(s,d,\tau)=(2s-\tau)\frac{{(s+d)^k-(s-d)^k}}{{2d}}+\tau.
\]
The second expression extends analytically through \(d=0\). Both \(G\) and \(H\) are even in \(d\), so with \(u=d^2\) they define analytic functions of \((s,u,\tau)\) near \((x,0,\tau_2(k))\).

At \(u=0\),
\[
G=(2s-\tau)s^k+\tau s-2,
\qquad
H=k(2s-\tau)s^{{k-1}}+\tau.
\]
The equations \(G=H=0\) at the second shared root give \(s=x\) and \(\tau=\tau_2(k)=2k/((k-1)x)\), exactly the intersection described above.

Let
\[
B=k-(k-1)x^2.
\]
Using \(x^{{k-1}}B=1\), the first derivatives with respect to \(s\), \(\tau\), and \(u\) at \((x,0,\tau_2(k))\) simplify to
\[
G_s=\frac{{2x}}B,\qquad
G_\tau=\frac{{x(k-1)(1-x^2)}}B,\qquad
G_u=-\frac{k}{x^2},
\]
\[
H_s=\frac{{2k^2(x^2-1)}}{{x^2B}},\qquad
H_\tau=-\frac{{(k-1)x^2}}B,\qquad
H_u=-\frac{{k(k-2)}}{{3x^3}}.
\]
The \((s,\tau)\)-Jacobian determinant is
\[
\Delta=\frac{{2(k-1)[k-(k+1)x^2]}}{{xB}}>0,
\]
because \(x<k/(k+1)\). Hence the analytic implicit-function theorem gives unique analytic functions \(s(u)\) and \(\tau(u)\) with \(s(0)=x\), \(\tau(0)=\tau_2(k)\), and \(G=H=0\).

Solving the first-order linear system in \(u\) gives
\[
\tau(u)=\tau_2(k)+C_k u+O(u^2),
\]
where
\[
C_k=
\frac{{k\,[3k^2-(3k^2-k+2)x^2]}}
{{3x^3(k-1)[k-(k+1)x^2]}}.
\]
This coefficient is positive. Indeed \(x^2<k/(k+1)\), and therefore
\[
3k^2-(3k^2-k+2)x^2
>
\frac{{2k(2k-1)}}{{k+1}}>0.
\]
Thus \(u\mapsto\tau(u)\) is locally strictly increasing. For \(\tau>\tau_2(k)\) sufficiently close to the threshold there is a unique small \(u>0\), and hence exactly two nearby unequal solutions \(d=\pm\sqrt{u}\); for \(\tau\le\tau_2(k)\) sufficiently close there is no such \(u>0\). Inverting the expansion gives
\[
u=\frac{{\tau-\tau_2(k)}}{{C_k}}+O((\tau-\tau_2(k))^2),
\]
so
\[
|a-b|=2|d|=\frac2{{\sqrt{{C_k}}}}\sqrt{{\tau-\tau_2(k)}}+O((\tau-\tau_2(k))^{{3/2}}),
\]
which is the stated amplitude.

The swapped solutions are obtained by shifting the 4-periodic sequence by two height classes. The standard cyclic-shift identification for height-periodic boundary laws therefore makes them representatives of the same gradient Gibbs measure. Since \(x<1\), the nearby unequal solutions have neither \(a=b\) nor \(a=b=1\), so their minimal height period is four.

## Verification
The accompanying `verify.py` independently checks, for \(2\le k\le40\), the nonunit shared root, the source intersection equation, positivity of \(C_k\), and the predicted square-root amplitude against the original two-variable boundary-law equations at a small positive displacement from \(\tau_2(k)\). It prints a single `VERIFY_OK` line on success. These finite checks corroborate the algebra but are not used as a proof of the all-\(k\) statement.

For orientation, the first three nontrivial intersection values are \(\tau_2(2)=2+2\sqrt5\), \(\tau_2(3)=3\sqrt2\), and \(\tau_2(4)\approx3.4973593139\). The corresponding amplitude for \(k=4\) is \(A_4\approx0.4529497560\).

## Relationship to prior work
Haydarov and Rozikov derive the same 4-periodic system for every \(k\ge2\), identify the two parameter values at which their symmetric and unequal-cycle polynomials intersect, and prove that the larger one satisfies \(\tau_2(k)>2(k+1)/(k-1)\). They then state that the full unequal problem remains open for \(k\ge4\). Their paper does not give a local bifurcation theorem, the sign of the side on which the unequal branch leaves the symmetric branch, or the square-root amplitude above.

Rozikov's later mirror-symmetry classification revisits height periods up to five and the same 4-periodic family. It records explicit or partial results for small \(k\) but does not state the \(\tau_2(k)\) local branch or its normal form. The earlier Henning--Külske--Le Ny--Rozikov paper treats this 4-periodic family fully only on the binary tree and treats arbitrary \(k\) through a different 3-periodic family.

The present result is therefore a local extension, not a replacement for the unresolved global classification. In particular, it supplies a genuinely 4-periodic branch for every \(k\ge4\) immediately above the source's second intersection value.

## Limitations
The theorem is local in \(\tau\) and in \((a,b)\). It neither counts remote unequal solutions nor determines the full phase diagram for \(k\ge4\). It uses the source's existence and uniqueness of \(\tau_2(k)\) as an input and does not re-prove the global root count underlying that lemma. The finite numerical replay is supplementary; the all-\(k\) conclusion rests on the analytic implicit-function argument and the explicit positive coefficient \(C_k\). No independent audit has been performed.

## References
1. F. H. Haydarov and U. A. Rozikov, *Gradient Gibbs measures of a SOS model on Cayley trees: 4-periodic boundary laws*, arXiv:2110.10078v1 (2021), especially equations (2.2), Lemmas 2--3, and Remark 2.
2. U. A. Rozikov, *Mirror symmetry of height-periodic gradient Gibbs measures of a SOS model on Cayley trees*, arXiv:2203.11446 (2022), especially the discussion of 4-periodic height laws and cyclic-shift identifiability.
3. F. Henning, C. Külske, A. Le Ny, and U. A. Rozikov, *Gradient Gibbs measures for the SOS model with countable values on a Cayley tree*, arXiv:1902.04909v1 (2019).
