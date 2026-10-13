# Exactly two Gaussian central-mass crossings for the standardized exponential
## Finding
Let \(X\sim\operatorname{Exp}(1)\), set \(Z=X-1\), and let \(G\sim N(0,1)\). Both \(Z\) and \(G\) have mean zero and variance one. Define
\[
D(c)=\Pr\{|Z|\le c\}-\Pr\{|G|\le c\},\qquad c>0.
\]
Then \(D\) has exactly two positive zeros. The first is the unique \(c_-\in(0,1)\) satisfying
\[
\frac{2}{e}\sinh c_-=2\Phi(c_-)-1,
\]
and the second is the unique \(c_+>1\) satisfying
\[
2\bigl(1-\Phi(c_+)\bigr)=e^{-1-c_+}.
\]
Numerically,
\[
c_-=0.4961685495956\ldots,\qquad
c_+=1.9329872875286\ldots.
\]
The complete sign pattern is
\[
D(c)<0\quad(0<c<c_-),
\]
\[
D(c)>0\quad(c_-<c<c_+),
\]
and
\[
D(c)<0\quad(c>c_+).
\]

## Assumptions and scope
The exponential law has rate one, hence mean one and variance one. The function \(\Phi\) denotes the standard normal cdf and
\[
\phi(c)=\frac{1}{\sqrt{2\pi}}e^{-c^2/2}
\]
its density. The theorem is a complete all-radius comparison for the shape-one Gamma member. It does not claim the corresponding crossing structure for arbitrary Gamma shape.

The equality at \(c=0\) is excluded from the phrase “positive zeros.”

## Proof
For \(0<c\le1\), the interval \([1-c,1+c]\) lies in the support of \(X\), so
\[
\Pr\{|Z|\le c\}
=
e^{-(1-c)}-e^{-(1+c)}
=
\frac{2}{e}\sinh c.
\]
Therefore
\[
D(c)=\frac{2}{e}\sinh c-\bigl(2\Phi(c)-1\bigr),
\qquad 0<c\le1,
\]
and
\[
D'(c)=2\left(e^{-1}\cosh c-\phi(c)\right).
\]
Set
\[
R_-(c)=\frac{e^{-1}\cosh c}{\phi(c)}.
\]
Then
\[
\frac{d}{dc}\log R_-(c)=\tanh c+c>0.
\]
Also \(R_-(0)=\sqrt{2\pi}/e<1\), while \(R_-(1)>1\). Hence \(D'\) changes sign exactly once on \((0,1)\): first negative, then positive. Since \(D(0)=0\), the function initially becomes negative.

At \(c=1\),
\[
D(1)=2\overline\Phi(1)-e^{-2}>0.
\]
For completeness, the standard Mills lower bound
\[
\overline\Phi(x)>\frac{x}{1+x^2}\phi(x),\qquad x>0,
\]
gives \(2\overline\Phi(1)>\phi(1)>e^{-2}\). Thus, after its unique minimum, \(D\) crosses zero exactly once before \(1\). This zero is \(c_-\), and the sign pattern on \((0,1]\) follows.

For \(c\ge1\), the lower endpoint \(1-c\) has reached the boundary of the exponential support. Hence
\[
\Pr\{|Z|\le c\}=1-e^{-1-c},
\]
and therefore
\[
D(c)=2\overline\Phi(c)-e^{-1-c}.
\]
Its derivative is
\[
D'(c)=e^{-1-c}-2\phi(c).
\]
Set
\[
R_+(c)=\frac{e^{-1-c}}{2\phi(c)}.
\]
For \(c>1\),
\[
\frac{d}{dc}\log R_+(c)=c-1>0.
\]
Moreover \(R_+(1)<1\), while \(R_+(c)\to\infty\). Thus \(D'\) changes sign exactly once on \((1,\infty)\): first negative, then positive.

We already know \(D(1)>0\). On the other hand, the upper Mills bound
\[
\overline\Phi(c)<\frac{\phi(c)}{c}
\]
shows
\[
\frac{2\overline\Phi(c)}{e^{-1-c}}
<
\frac{2}{c\sqrt{2\pi}}\exp\left(1+c-\frac{c^2}{2}\right)
\longrightarrow0.
\]
Consequently \(D(c)<0\) for all sufficiently large \(c\), and \(D(c)\to0\) from below. Because \(D\) first decreases and then increases on \((1,\infty)\), it crosses zero exactly once there. This zero is \(c_+\), and \(D(c)<0\) for every \(c>c_+\).

The displayed equations for \(c_-\) and \(c_+\) are precisely the two zero equations in the two support regimes.

## Verification
The bundled `verify.py` evaluates the two zero equations by bisection with the Python standard library. It verifies the certified decimal brackets
\[
0.49616854<c_-<0.49616856
\]
and
\[
1.93298728<c_+<1.93298730,
\]
checks the source-highlighted radii \(c=1/2\), \(c=1\), and \(c=2\), and checks the sign profile on a deterministic grid.

A successful replay ends with
`VERIFY_OK c_minus=0.496168549596 c_plus=1.932987287529 D1=0.181975224626`.

The numerical checks do not establish uniqueness; uniqueness and the global sign pattern follow from the analytic derivative-ratio arguments in the proof.

## Relationship to prior work
Sun, Hu, and Sun proved that every Gamma law has strictly more mass than the standard normal within one of its own standard deviations. In the same paper they explicitly warn that replacing the radius \(1\) by a general positive radius can fail: for the shape-one Gamma law they give a positive comparison at radius \(1/2\) and a negative comparison at radius \(2\). The theorem above turns those isolated comparisons for the exponential boundary member into a complete all-radius sign diagram.

Their earlier variation-comparison paper studies the one-standard-deviation inequality for many infinitely divisible distributions. Its inspected open preprint fixes the comparison radius at one and does not state an all-radius exponential crossover theorem.

Targeted published-record searches for the exact model, both numerical crossover values, the hyperbolic-sine zero equation, and “two crossings” terminology did not locate a statement implying the complete sign classification.

## Limitations
The result is restricted to the standardized shape-one Gamma law. The proof uses the support breakpoint at one and does not by itself determine how many Gaussian central-mass crossings occur for other Gamma shapes.

The two decimal constants are numerical evaluations of uniquely defined roots; they are not closed forms. Search noncoverage is evidence rather than proof of bibliographic uniqueness, and an equivalent elementary comparison may exist under terminology unrelated to variation comparison.

## References
1. P. Sun, Z.-C. Hu, and W. Sun, “The infimum values of two probability functions for the Gamma distribution,” *Journal of Inequalities and Applications* 2024, article 5 (2024), DOI: 10.1186/s13660-024-03081-w.
2. P. Sun, Z.-C. Hu, and W. Sun, “Variation comparison between infinitely divisible distributions and the normal distribution,” arXiv:2304.11459 (2023); *Statistical Papers* 65 (2024), 4405–4429, DOI: 10.1007/s00362-024-01561-1.
