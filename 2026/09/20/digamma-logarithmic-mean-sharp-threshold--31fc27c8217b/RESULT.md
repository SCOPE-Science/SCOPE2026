# Sharp two-sided threshold for a digamma logarithmic-mean inequality

**Same-model review: passed. Independent audit: not yet performed.**

Let
\[
L(a,b)=\frac{b-a}{\log b-\log a}\qquad(0<a<b)
\]
and
\[
F(a,b)=(L(a,b)-a)\psi(a)+(b-L(a,b))\psi(b)
-(b-a)\psi(\sqrt{ab}),
\]
where \(\psi=\Gamma'/\Gamma\) is the digamma function. Let \(\alpha_0\) be the
unique positive zero of
\[
5\psi'(x)+3x\psi''(x)=0.
\]
Numerically, \(\alpha_0\approx0.5615593996\).

## Result

For every \(0<a<b\),
\[
0<a<b\le \alpha_0 \quad\Longrightarrow\quad F(a,b)<0,
\]
whereas the complementary large-parameter theorem of Alzer and Kwong gives
\[
\alpha_0\le a<b \quad\Longrightarrow\quad F(a,b)>0.
\]
Consequently, the two best constants requested in Matejíčka's 2018 Open
Problem 2 coincide:
\[
\boxed{b_0=b_1=\alpha_0}.
\]

Matejíčka proved the first inequality for \(b<0.4\) and asked for its largest
admissible endpoint \(b_0\), together with the smallest lower endpoint \(b_1\)
for the reversed inequality. Alzer and Kwong later proved
\(b_1=\alpha_0\). The theorem above supplies the missing sharp value of
\(b_0\).

## Proof of the missing small-parameter inequality

Write \(b=at\) with \(t>1\), and put
\[
\Lambda(t)=\frac{t-1}{\log t},
\]
\[
U(a,t)=(\Lambda(t)-1)\psi(a)+(t-\Lambda(t))\psi(at)
-(t-1)\psi(a\sqrt t).
\]
Then \(F(a,at)=aU(a,t)\).

Two facts proved by Alzer and Kwong will be used:

1. for every fixed \(t>1\), \(a\mapsto U(a,t)\) is strictly increasing on
   \((0,\infty)\);
2. if \(f(x)=5\psi'(x)+3x\psi''(x)\), then \(f(x)<0\) on
   \((0,\alpha_0)\).

Thus, if \(at=b\le\alpha_0\),
\[
U(a,t)\le U(\alpha_0/t,t).
\]
It remains to prove that the right-hand side is strictly negative.

Set
\[
A=\frac{\alpha_0}{t},\qquad
G=\frac{\alpha_0}{\sqrt t},\qquad B=\alpha_0.
\]
Since \(t-1=(\Lambda-1)+(t-\Lambda)\),
\[
U(\alpha_0/t,t)
=-(\Lambda-1)\bigl(\psi(G)-\psi(A)\bigr)
 +(t-\Lambda)\bigl(\psi(B)-\psi(G)\bigr).
\tag{1}
\]

### Growth of \(x\psi'(x)\) below \(\alpha_0\)

Let
\[
P(x)=x\psi'(x).
\]
Because \(\psi'(x)>0\), the inequality
\(5\psi'(x)+3x\psi''(x)<0\) gives, for \(0<x<\alpha_0\),
\[
\frac{d\log P(x)}{d\log x}
=1+\frac{x\psi''(x)}{\psi'(x)}<-\frac23.
\tag{2}
\]
Put \(h=\frac12\log t>0\) and
\[
p(s)=P(\alpha_0e^{-s}),\qquad s\ge0.
\]
From (2),
\[
\frac d{ds}\log p(s)>\frac23\qquad(s>0).
\]
Hence, for \(0\le s\le h\),
\[
p(s+h)>e^{2h/3}p(s)=t^{1/3}p(s).
\]
Since \(d\psi(x)/d\log x=P(x)\),
\[
\begin{aligned}
\psi(G)-\psi(A)
 &=\int_h^{2h}p(s)\,ds\\
 &>t^{1/3}\int_0^h p(s)\,ds\\
 &=t^{1/3}\bigl(\psi(B)-\psi(G)\bigr).
\end{aligned}
\tag{3}
\]

### The matching logarithmic-mean inequality

For every \(t>1\),
\[
\frac{t-\Lambda(t)}{\Lambda(t)-1}<t^{1/3}.
\tag{4}
\]
Indeed, write \(t=r^3\), \(r>1\). Inequality (4) is equivalent to
\[
\log r<
\frac{(r^3-1)(r+1)}{3r(r^2+1)}.
\]
If
\[
H(r)=\frac{(r^3-1)(r+1)}{3r(r^2+1)}-\log r,
\]
then
\[
H'(r)=
\frac{(r-1)^4(r^2+r+1)}{3r^2(r^2+1)^2}>0
\qquad(r>1),
\]
and \(H(1)=0\). This proves (4).

Combining (3) and (4) yields
\[
(\Lambda-1)\bigl(\psi(G)-\psi(A)\bigr)
>(t-\Lambda)\bigl(\psi(B)-\psi(G)\bigr).
\]
Equation (1) therefore gives
\[
U(\alpha_0/t,t)<0.
\]
By monotonicity in \(a\),
\[
U(a,t)<0\qquad\text{whenever }at\le\alpha_0,
\]
and hence \(F(a,b)<0\) for all \(0<a<b\le\alpha_0\).

## Sharpness and completion of the 2018 problem

Alzer and Kwong proved \(F(a,b)>0\) for every
\(\alpha_0\le a<b\), and proved that \(\alpha_0\) is the best possible lower
endpoint for that direction. Thus \(b_1=\alpha_0\).

The same theorem also makes the newly proved upper endpoint sharp. If
\(B>\alpha_0\), choose \(a=\alpha_0\) and any
\(b\in(\alpha_0,B]\). Then \(F(a,b)>0\), so the inequality required in the
definition of \(b_0\) fails. Therefore \(b_0\le\alpha_0\), while the result
above gives \(b_0\ge\alpha_0\). Hence
\[
b_0=b_1=\alpha_0.
\]

## Relation to prior literature and originality

Matejíčka (2018) explicitly asked for the best constants \(b_0,b_1\), recording
only \(b_0\ge0.4\) and \(b_1\le2\). Alzer and Kwong (2023) proved the sharp
large-parameter direction \(b_1=\alpha_0\), and also established the two
structural facts used above: the sign change of
\(5\psi'+3x\psi''\) at \(\alpha_0\) and strict monotonicity of \(U(a,t)\) in
\(a\).

To the best of our knowledge, the complementary statement
\(F(a,b)<0\) for every \(b\le\alpha_0\), and hence the identity
\(b_0=b_1=\alpha_0\), has not previously been published. Searches of the
named 2018 problem, the defining equation for \(\alpha_0\), the exact
logarithmic-mean inequality, and subsequent digamma mean-value literature
did not identify an earlier statement of this sharp small-parameter
endpoint.

## Limitations

The proof relies on the published Alzer--Kwong sign lemma and monotonicity
theorem for \(U(a,t)\); those results are not reproved here. The originality
assessment is necessarily "to the best of our knowledge": a differently
phrased or poorly indexed prior solution of the \(b_0\) half may exist.
The result determines the global endpoint constants but does not classify
the sign of \(F(a,b)\) throughout the remaining mixed region
\(a<\alpha_0<b\).

## References

1. L. Matejíčka, *Notes on three conjectures involving the digamma and
   generalized digamma functions*, Journal of Inequalities and Applications
   **2018**, 342 (2018). DOI:
   https://doi.org/10.1186/s13660-018-1936-z
2. H. Alzer and M. K. Kwong, *Mean Value Inequalities for the Digamma
   Function*, Analysis Mathematica **49** (2023), 1--17. DOI:
   https://doi.org/10.1007/s10476-023-0206-6
