# Sharp \(Y\) bound for the four-ring square confinement template

## Statement

Consider the common-width nested-ring model in a square pan of side \(s\). Let the four outer radii be
\[
a>1>b>c>0,
\]
let the common width be \(w>0\), and put
\[
H=a-w.
\]
Write
\[
\rho=\max\left\{\frac{1+b+c}{a},\,b+c,\,\frac cb\right\}.
\]

Call such a four-ring best-fit failure a **canonical quadrant-confinement failure** if the following hold.

1. The full inventory has a witness in which \(a\) and \(1\) are siblings at the square root, while \(b\) and \(c\) are siblings in the circular hole of the ring \(a\).
2. At the pivot \(1\), both the square root and the hole of \(a\) are feasible, and best fit nests \(1\) in that hole; in particular
   \[
   1\le H<\frac s2.
   \]
   The later ring \(c\) is rejected by the greedy placement, hence in particular it does not fit in the hole of the pivot:
   \[
   c>\max(0,1-w).
   \]
3. The root triple \(\{a,b,c\}\) is certified infeasible by Aguilar Martín's quadrant-confinement criterion: for some \(p\ge q\ge0\),
   \[
   p\ge \frac s2-b,\qquad
   p^2+(s-a-b)^2<(a+b)^2,
   \]
   \[
   q^2+(s-a-c)^2<(a+c)^2,\qquad
   p+q\ge s-b-c,
   \]
   and, with \(L=s-c-a-q\),
   \[
   L\ge0,\qquad 2L^2<(b+c)^2.
   \]

Let \(Y\) be the unique positive root of
\[
F(x):=(17+10\sqrt2)x^2+(72+16\sqrt2)x-(112+96\sqrt2)=0.
\]
Numerically,
\[
Y=1.684487745872346\ldots.
\]

**Theorem.** Every canonical quadrant-confinement failure satisfies
\[
\boxed{\rho>Y.}
\]
Aguilar Martín's rational four-ring family from Theorem 38 of arXiv:2609.15554v2 belongs to this class and has \(\rho\to Y\) from above. Therefore
\[
\boxed{\inf_{\mathcal Q}\rho=Y,}
\]
where \(\mathcal Q\) is the class above, and the infimum is not attained.

Thus the constant \(Y\) is not merely a consequence of the balanced limiting ansatz: it is forced by the witness geometry together with the quadrant-confinement certificate throughout this canonical four-ring template.

## Proof

Set
\[
S=b+c,\qquad C=1+\frac1{\sqrt2}=1+\frac{\sqrt2}{2}.
\]

### 1. The witness and the failed pivot force \(a>1+S/2\)

Because \(b\) and \(c\) are sibling disks inside a circular hole of radius \(H\), necessarily
\[
H\ge b+c=S.
\]
Indeed, if their centers are \(x_b,x_c\), then
\[
|x_b-x_c|\le (H-b)+(H-c)=2H-S,
\]
while non-overlap requires \(|x_b-x_c|\ge S\).

Since \(c\) does not fit in the pivot's hole,
\[
c>\max(0,1-w)\ge 1-w,
\]
so \(w>1-c\). Hence
\[
a=H+w>S+1-c=1+b.
\]
Because \(b\ge S/2\),
\[
\boxed{a>1+\frac S2.}
\]

Also \(H<s/2\) and \(H\ge S\), so
\[
\boxed{s>2S.}
\]

### 2. The root witness forces a lower bound on the square side

The disks of radii \(a\) and \(1\) occur as root siblings in the full witness. In a square of side \(s\), each coordinate difference between their centers is at most \(s-a-1\). Therefore their center distance is at most
\[
\sqrt2\,(s-a-1).
\]
Non-overlap requires this to be at least \(a+1\), giving
\[
\sqrt2\,(s-a-1)\ge a+1
\]
and hence
\[
\boxed{s\ge C(a+1).}
\]

### 3. The first two confinement margins imply one scalar inequality

The two strict quadratic inequalities in the confinement certificate give
\[
p<\sqrt{s(2a+2b-s)},\qquad
q<\sqrt{s(2a+2c-s)}.
\]
The radicands are positive because the displayed strict inequalities hold with \(p,q\ge0\).

Using \(p+q\ge s-S\) and concavity of the square root,
\[
\begin{aligned}
s-S
&\le p+q\\
&<\sqrt{s(2a+2b-s)}+\sqrt{s(2a+2c-s)}\\
&\le 2\sqrt{s(2a+S-s)}.
\end{aligned}
\]
Since \(s>2S\), the left side is positive, so squaring is legitimate. Thus
\[
Q(a,S,s):=4s(2a+S-s)-(s-S)^2>0,
\]
or equivalently
\[
\boxed{Q(a,S,s)=8as+6Ss-5s^2-S^2>0.}
\]

Notably, this lower-bound argument does not use the final \(L\)-inequality of the confinement lemma; the two quadratic margins and their coupling already force the threshold.

### 4. \(Q>0\) is impossible when \(S\le Y\)

First note that \(F\) is strictly increasing on \([0,\infty)\), since
\[
F'(x)=2(17+10\sqrt2)x+72+16\sqrt2>0.
\]
Also \(F(0)<0\), while
\[
F(7/4)=\frac{1057}{16}-\frac{299\sqrt2}{8}>0,
\]
for example from \(\sqrt2<3/2\). Hence
\[
0<Y<\frac74<2.
\]

Assume for contradiction that \(S\le Y\).

For fixed \(a,S\),
\[
\frac{\partial Q}{\partial s}=8a+6S-10s.
\]
On \(s\ge C(a+1)\),
\[
\frac{\partial Q}{\partial s}
\le (8-10C)a+6S-10C.
\]
Since \(8-10C<0\), \(a>1+S/2\), \(S<2\), and \(1<C<2\),
\[
\frac{\partial Q}{\partial s}
<
8-20C+(10-5C)S
<
28-30C<0.
\]
Therefore \(Q\) decreases with \(s\) throughout the admissible region. From \(Q(a,S,s)>0\) and \(s\ge C(a+1)\),
\[
Q_0(a,S):=Q(a,S,C(a+1))>0.
\]

A direct expansion gives
\[
\frac{\partial Q_0}{\partial a}
=(6+3\sqrt2)S+(1-2\sqrt2)a-(7+6\sqrt2).
\]
Because \(1-2\sqrt2<0\) and \(a>1+S/2\),
\[
\frac{\partial Q_0}{\partial a}
<
\frac{(13+4\sqrt2)S-(12+16\sqrt2)}2.
\]
For \(S\le Y<7/4\), the right side is smaller than
\[
\frac12\left(\frac{43}{4}-9\sqrt2\right)<0;
\]
the last inequality follows, for instance, by squaring the positive quantities:
\((43/4)^2< (9\sqrt2)^2\).

Thus \(Q_0\) is strictly decreasing for \(a\ge1+S/2\), and
\[
0<Q_0(a,S)
<
Q_0\!\left(1+\frac S2,S\right).
\]
Another direct expansion yields
\[
Q_0\!\left(1+\frac S2,S\right)
=\frac18 F(S).
\]
But \(F\) is increasing and \(S\le Y\), so \(F(S)\le F(Y)=0\), a contradiction.

Therefore
\[
S>Y.
\]
Since \(S=b+c\) is the tail ratio after the pivot \(1\),
\[
\rho\ge S>Y.
\]
This proves the lower bound.

### 5. Sharpness

Aguilar Martín's Theorem 38 takes, for \(t>Y/2\) and small \(\eta>0\),
\[
a=1+t+2\eta,\qquad b=t+\eta,\qquad c=t-\eta,
\]
\[
w=1-t+2\eta,\qquad H=2t,\qquad s=C(a+1),
\]
with a suitable quadrant-confinement certificate. The full witness has \(\{a,1\}\) at the root and \(\{b,c\}\) in the hole of \(a\); best fit nests \(1\), later places \(b\) at the root, and rejects \(c\). The source proves
\[
\rho=2t.
\]
Taking rational perturbations with \(t\downarrow Y/2\) gives strict legal failures with
\[
\rho\downarrow Y.
\]
Together with the strict lower bound, this proves
\[
\inf_{\mathcal Q}\rho=Y
\]
and non-attainment.

## Significance

The source paper proves \(\tau_\square\le Y\) but explicitly states that no optimality of \(Y\) is asserted, including over the parameters of its confinement criterion. Its accompanying square-limit note likewise leaves open a lower bound forcing \(\rho\ge Y\) for the broader slipped/confinement family.

The theorem above establishes that lower bound for the canonical four-ring branch in which the full witness splits as a root pair plus a pair in the large hole, best fit nests the unit pivot, and the failing root triple is certified by the quadrant-confinement lemma. It explains why the balanced polynomial defining \(Y\) reappears after optimizing over the entire parameter freedom of this branch.

## Limitations

This does **not** prove the global square threshold \(\tau_\square=Y\). A smaller counterexample could use a different witness forest, a different pivot/order, a root-triple obstruction not captured by the quadrant-confinement criterion, or more than four rings. The exact global square threshold therefore remains open.

Originality is asserted only to the best of our knowledge. The source paper is very recent, so rapid revisions or unindexed follow-up work remain a residual risk.

## References

1. Javier Aguilar Martín, *Greedy Packing of Nested Rings: The Golden Threshold, Placement Rules, and a Tribonacci Floor*, arXiv:2609.15554v2 (2026). https://arxiv.org/abs/2609.15554
2. Javier Aguilar Martín, *Una familia aproximante y una cota algebraica para el cuadrado*, accompanying source note `docs/drafts/cuadrado_limite.md` in the Calamares repository (2026). https://github.com/JaviMaligno/calamares/blob/main/docs/drafts/cuadrado_limite.md
