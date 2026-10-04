# Exact Ptolemy constant of the regular octagonal plane
## Finding
For the real regular octagonal plane \(X=(\mathbb R^2,N)\), where \(N(x,y)=\max\{|x|,|y|,(|x|+|y|)/\sqrt2\}\), the Ptolemy constant is exactly \(C_{\mathrm{Pt}}(X)=4-2\sqrt2\).

Here
\[
C_{\mathrm{Pt}}(X)=
\sup_{x,y,z\in X\setminus\{0\},\;x,y,z\ \mathrm{pairwise\ distinct}}
\frac{N(x-y)N(z)}{N(x-z)N(y)+N(z-y)N(x)}.
\]

## Assumptions and scope
The scalar field is real. The norm is
\[
N(x,y)=\max\left\{|x|,|y|,\frac{|x|+|y|}{\sqrt2}\right\}.
\]
Its unit sphere has the eight vertices obtained from
\[
(1,\sqrt2-1)
\]
by coordinate swaps and sign changes, so the unit ball is a regular octagon.

## Proof
Let
\[
E(x,y)=\sqrt{x^2+y^2}.
\]
Both \(\max\{|x|,|y|\}\le E(x,y)\) and \((|x|+|y|)/\sqrt2\le E(x,y)\), hence
\[
N(v)\le E(v)
\]
for every \(v\in\mathbb R^2\).

For the reverse comparison, by sign and coordinate symmetries it is enough to take \(a\ge b\ge0\), put \(t=b/a\in[0,1]\), and assume \(a>0\). Then
\[
\frac{N(a,b)}{E(a,b)}
=
\frac{\max\{1,(1+t)/\sqrt2\}}{\sqrt{1+t^2}}.
\]
The two branches meet at
\[
s=\sqrt2-1.
\]
On \([0,s]\), the ratio is \((1+t^2)^{-1/2}\), which is decreasing. On \([s,1]\), its square is
\[
\frac{(1+t)^2}{2(1+t^2)},
\]
whose derivative is positive for \(t<1\). Therefore the global minimum occurs at \(t=s\). Writing
\[
c^2=\frac1{1+s^2}=\frac{2+\sqrt2}{4}=\cos^2\!\left(\frac\pi8\right),
\]
we obtain the sharp norm comparison
\[
cE(v)\le N(v)\le E(v).
\]

For admissible \(x,y,z\), Euclidean Ptolemy now gives
\[
\begin{aligned}
N(x-y)N(z)
&\le E(x-y)E(z)\\
&\le E(x-z)E(y)+E(z-y)E(x)\\
&\le c^{-2}\bigl(N(x-z)N(y)+N(z-y)N(x)\bigr).
\end{aligned}
\]
Thus
\[
C_{\mathrm{Pt}}(X)\le c^{-2}=4-2\sqrt2.
\]

For equality, let \(s=\sqrt2-1\) and choose
\[
x=(-1,s),\qquad y=(s,-1),\qquad z=(-2,-2).
\]
Directly from the norm,
\[
N(x)=N(y)=1,
\]
\[
N(x-y)=2,\qquad N(z)=2\sqrt2,
\]
and
\[
N(x-z)=N(z-y)=1+\sqrt2.
\]
Consequently the Ptolemy ratio equals
\[
\frac{(2)(2\sqrt2)}{(1+\sqrt2)+(1+\sqrt2)}
=
4-2\sqrt2.
\]
The upper and lower bounds coincide.

## Verification
The proof establishes the infinite upper bound by an exact Euclidean comparison, not by sampling. The sharp comparison factor is obtained by a complete one-variable minimization after exhausting the norm symmetries. The lower-bound triple is nonzero and pairwise distinct, and every displayed norm value follows directly from the defining maximum.

As a separate symbolic check, the transition value \(s=\sqrt2-1\) gives
\[
\frac1{1+s^2}=\frac{2+\sqrt2}{4},
\qquad
\left(\frac{2+\sqrt2}{4}\right)^{-1}=4-2\sqrt2,
\]
and the explicit ratio simplifies to the same number.

## Relationship to prior work
Zuo's 2012 paper develops comparison criteria for Ptolemy constants of absolute normalized norms and computes several concrete examples, including max-combinations involving Euclidean, \(\ell_1\), and \(\ell_\infty\) norms. The inspected full text does not state a regular-octagonal example. For the present associated function
\[
\psi(t)=\max\left\{1-t,t,\frac1{\sqrt2}\right\},
\]
the Euclidean comparison ratio \(\psi_2/\psi\) is maximized at the branch transition rather than at \(t=1/2\), so the relevant midpoint criterion from that paper does not give the equality above.

Komuro, Saito, and Tanaka explicitly use
\[
\max\left\{|x|,|y|,2^{-1/2}(|x|+|y|)\right\}
\]
as the regular-octagonal norm while studying the James constant \(\sqrt2\). Their inspected full text contains no Ptolemy calculation.

Zuo's 2018 paper studies the broader family
\[
\max\{\|\cdot\|_p,\lambda\|\cdot\|_q\}.
\]
The regular octagon is the endpoint \((p,q,\lambda)=(\infty,1,1/\sqrt2)\). In the inspected Example 1, the displayed mixed-regime exact formula is stated only for \(\lambda>1/\sqrt2\), not at this endpoint. The general symmetric comparison theorem in the same paper also does not force the present value: with Euclidean comparison, its required range condition exceeds the regular octagon's James-function maximum.

## Limitations
The claim is only the Ptolemy constant of this single classical planar norm. It does not assert an exact formula for neighboring max-norm parameters.

A 2015 article devoted to additional sufficient conditions for Ptolemy constants of absolute normalized norms is a plausible comparison source. Its abstract and bibliographic material were inspected, but a readable full text was not obtained through bounded lawful access attempts. This is retained as a residual originality risk rather than treated as evidence of noncoverage.

The current ledger already contains an exact Euclidean Banach--Mazur distance for a one-parameter Lorentz-predual octagonal family that includes this regular octagon. That earlier distance result supplies a compatible Euclidean comparison factor but does not state or imply the sharp Ptolemy lower bound proved here.

## References
1. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, 107 (2012). DOI: 10.1186/1029-242X-2012-107.
2. Z. Zuo, “A Reconsideration on the Ptolemy Constant of Absolute Normalized Norms,” Acta Mathematica Sinica, Chinese Series 58 (2015), 337–344. DOI: 10.12386/A2015sxxb0033.
3. N. Komuro, K.-S. Saito, and R. Tanaka, “On the class of Banach spaces with James constant \(\sqrt2\),” Mathematische Nachrichten 289 (2016), 1005–1020. DOI: 10.1002/mana.201500238.
4. Z.-F. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” Mathematical Inequalities & Applications 21 (2018), 945–956. DOI: 10.7153/mia-2018-21-64.
