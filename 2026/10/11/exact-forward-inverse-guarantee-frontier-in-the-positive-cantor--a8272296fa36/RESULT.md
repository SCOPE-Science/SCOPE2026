# Exact forward/inverse guarantee frontier in the positive Cantor–Bernstein construction
## Finding
Let \(C_+(a,b,c)\) and \(C_-(a,b,c)\) denote the two norm guarantees in the proof of the positive Cantor–Bernstein theorem of Laguna-Ricart, Martínez-Cervantes, Rondoš and Salguero-Alarcón. For \(a,b>1\) and \(c>0\), they are
\[
C_+(a,b,c)=1+\max\{c(1+a),b\},
\]
\[
C_-(a,b,c)=\frac{2b}{c(b-1)}+\max\left\{\frac{2b-1}{b-1},\frac{b}{c(b-1)(a-1)}\right\}.
\]
For a prescribed forward guarantee \(R>2\), define
\[
F(R)=\inf\{C_-(a,b,c):a,b>1,\ c>0,\ C_+(a,b,c)\le R\}.
\]
Then
\[
\boxed{F(R)=\begin{cases}
\dfrac{9}{R-2},&2<R\le3,\\[4pt]
2+\dfrac{5}{R-2}+\dfrac{2}{(R-2)^2},&R\ge3.
\end{cases}}
\]
The infimum is a minimum. For \(2<R\le3\), the unique minimizing parameters are
\[
a=2,\qquad b=R-1,\qquad c=\frac{R-1}{3}.
\]
For \(R\ge3\), the unique minimizing parameters are
\[
a=1+\frac1{R-2},\qquad b=R-1,\qquad c=\frac{(R-1)(R-2)}{2R-3}.
\]
At \(R=3\) the two formulas agree. Moreover, \(F(R)\downarrow2\) as \(R\to\infty\), while \(R F(R)\) has the unique global minimum
\[
\min_{R>2} R F(R)=9+6\sqrt3
\]
at \(R=3+\sqrt3\). Thus the balanced product constant in the source is the distinguished minimum point of a complete one-sided guarantee frontier, with an exact branch transition at \(R=3\).

## Assumptions and scope
The source theorem concerns real Banach lattices satisfying its positive contractive-retract hypotheses. The present statement optimizes only the explicit proof bounds \(C_+\) and \(C_-\). It does not assert that these bounds equal the actual norm of the constructed positive isomorphism or the actual regular norm of its inverse.

The parameter domain is \(a,b>1\), \(c>0\). A forward budget is feasible exactly for \(R>2\), since \(C_+>2\) on the parameter domain and values arbitrarily close to \(2\) are attainable as limits.

## Proof
Fix \(R>2\) and put \(d=R-2>0\). Then \(C_+\le R\) is equivalent to
\[
b\le d+1,\qquad c(1+a)\le d+1.
\]
For fixed \(a,c\), all occurrences of \(b/(b-1)\) and \((2b-1)/(b-1)\) decrease with \(b>1\), so \(C_-\) decreases as \(b\) increases. For fixed \(a,b\), its first term is strictly decreasing in \(c\), while the second term inside the maximum is nonincreasing in \(c\). Hence every minimizer saturates both budget constraints:
\[
b=d+1,\qquad c=\frac{d+1}{1+a}.
\]
Substitution reduces the problem to
\[
F(R)=\frac1d\inf_{a>1}\left(2(1+a)+\max\left\{2d+1,\frac{1+a}{a-1}\right\}\right).
\]
Set \(g(a)=(1+a)/(a-1)\). The two terms inside the maximum cross at
\[
a_*=1+\frac1d.
\]
On the branch where \(g(a)\ge2d+1\), the numerator
\[
h_1(a)=2(1+a)+g(a)
\]
has derivative
\[
h_1'(a)=2-\frac2{(a-1)^2}.
\]
Thus \(h_1\) decreases on \((1,2)\), has its unique minimum at \(a=2\), and increases on \((2,\infty)\). On the other branch the numerator
\[
h_2(a)=2(1+a)+2d+1
\]
is strictly increasing.

If \(0<d\le1\), then \(a_*\ge2\), so the unique global minimizer is \(a=2\). The numerator is \(9\), yielding \(F(R)=9/d=9/(R-2)\). If \(d\ge1\), then \(a_*\le2\); the first branch decreases up to \(a_*\) and the second increases from \(a_*\). Hence the unique minimizer is the crossing, and
\[
F(R)=\frac{2d+5+2/d}{d}=2+\frac5d+\frac2{d^2}.
\]
Back-substitution gives the stated minimizing triples.

For the product, the first branch gives \(R F(R)=9+18/d\), decreasing to \(27\) as \(d\uparrow1\). On the second branch,
\[
R F(R)=2d+9+\frac{12}{d}+\frac4{d^2}.
\]
Its derivative vanishes exactly when
\[
d^3-6d-4=(d+2)(d-(1+\sqrt3))(d-(1-\sqrt3))=0.
\]
The only root with \(d\ge1\) is \(d=1+\sqrt3\), and the derivative changes from negative to positive there. Therefore \(R=3+\sqrt3\) is the unique global product minimizer, with value \(9+6\sqrt3\).

## Verification
The source formulas and parameter domain were checked from the full text. The reduction was replayed algebraically and by direct substitution into the original formulas. At \(R=2.1,2.5,3,4,3+\sqrt3,10\), the displayed minimizers satisfy \(C_+=R\) and reproduce the corresponding closed form for \(F(R)\). These numerical substitutions are stress tests only; the proof is analytic for all \(R>2\).

At the transition \(R=3\), both branches give \((a,b,c)=(2,2,2/3)\) and \(F(3)=9\). The second branch gives \(F(R)\to2\) directly. The product minimizer follows from the exact cubic factorization, not numerical root finding.

## Relationship to prior work
The source paper derives \(C_+\) and \(C_-\) and minimizes their product, obtaining \(9+6\sqrt3\). It does not state the best inverse guarantee for a prescribed forward budget, the two-branch formula, the \(R=3\) transition, or the limiting inverse-guarantee floor \(2\).

A public result based on the same source determines exact inverse regular norms for the two elementary sequence isomorphisms used earlier in the construction. That local result does not optimize the composed three-parameter guarantees in the positive Cantor–Bernstein theorem and does not imply the present frontier.

Kania and Lewicki obtain the same product constant in a different quantitative decomposition theorem for ordinary Banach spaces. Their proof optimizes a symmetric one-parameter family; it does not give this positive/regular one-sided frontier.

## Limitations
The result is an exact optimization of the published proof guarantees, not a lower bound for all positive isomorphisms satisfying the same retract hypotheses. In particular, \(F(R)\) is not claimed to be the exact Banach-lattice isomorphism tradeoff for the underlying spaces. A different construction could improve both sides.

The originality comparison covered the focal full text, the closest same-source public database result, the Kania–Lewicki comparator, targeted formula searches, and the available owned ledgers. An equivalent conditional optimization could still exist under different terminology outside the inspected literature.

## References
1. J. Laguna-Ricart, G. Martínez-Cervantes, J. Rondoš, and A. Salguero-Alarcón, *A positive version of Miljutin's Theorem*, arXiv:2609.14148v1, first submitted 2026-09-12.
2. T. Kania and G. Lewicki, *\((\lambda^+)\)-injective Banach spaces*, arXiv:2603.09710v1, first submitted 2026-03-10.
