# An exact robustness interval for the Pommerenke counterexample

## Finding

Let \(\Sigma\) be the class of normalized functions meromorphic and univalent in the exterior disk
\[
\Delta^*=\{z\in\mathbb C:|z|>1\}.
\]
Guo and Hu's 2026 counterexample to Pommerenke's Problem 6.10 uses
\[
F(z)=z+\frac{\alpha}{z}
\]
and a function \(G\) determined by
\[
G'(z)=(1-\beta z^{-3})^{2/3},
\]
with
\[
q=\frac13-\frac16 i,
\qquad
w=1-q^3,
\qquad
r=\frac{399}{400},
\]
\[
\alpha=\frac89+\frac49 i,
\qquad
\beta=\frac{w}{r^3}.
\]
Both \(F\) and \(G\) are convex members of \(\Sigma\).

For
\[
H_\lambda
=
\lambda F+(1-\lambda)G,
\qquad
0<\lambda<1,
\]
put
\[
z_0=\frac{400}{399}.
\]
Then
\[
\operatorname{Re}\!\left(
1+\frac{z_0H_\lambda''(z_0)}{H_\lambda'(z_0)}
\right)
=
\frac{P(\lambda)}{Q(\lambda)},
\]
where
\[
P(\lambda)
=
15391097599\lambda^2
-
17772056000\lambda
+
2956000000
\]
and
\[
Q(\lambda)
=
2868678401\lambda^2
+
2046392000\lambda
+
500000000.
\]

The denominator is strictly positive for
\[
0\le\lambda\le1.
\]
The two roots of \(P\) are
\[
\lambda_\pm
=
\frac{
8886028000
\pm
18000\sqrt{103288299735}
}{
15391097599
},
\]
namely
\[
\lambda_-
=
0.201486508538006998\ldots
\]
and
\[
\lambda_+
=
0.953210606835668308\ldots.
\]

Therefore the same point \(z_0\) violates the strict exterior-convexity criterion for every
\[
\lambda\in[\lambda_-,\lambda_+].
\]
Consequently,
\[
H_\lambda\in\Sigma
\quad\text{but}\quad
H_\lambda\ \text{is not exterior convex}
\]
throughout that entire interval.

Its length is
\[
\lambda_+-\lambda_-
=
0.751724098297661310\ldots.
\]
Thus the source's isolated value
\[
\lambda=\frac35
\]
lies inside a broad exact robustness window rather than representing a finely tuned counterexample.

## Assumptions and scope

The parameters, branch choice for \(G'\), and the exterior-convexity criterion are exactly those used in the 2026 source.

For a locally univalent normalized function \(h\in\Sigma\), exterior convexity is equivalent to
\[
\operatorname{Re}\!\left(
1+\frac{zh''(z)}{h'(z)}
\right)>0
\]
for every \(z\in\Delta^*\).

The statement does not claim that \(H_\lambda\) is convex for
\[
\lambda\notin[\lambda_-,\lambda_+].
\]
It identifies the exact set of mixture weights for which the source's fixed test point \(z_0\) certifies failure.

## Proof

At
\[
z_0=\frac1r,
\]
the source construction gives
\[
G'(z_0)=q^2,
\qquad
F'(z_0)=1-\alpha r^2,
\]
and
\[
z_0F''(z_0)=2\alpha r^2,
\qquad
z_0G''(z_0)=\frac{2w}{q}.
\]

Define
\[
D_\lambda
=
H_\lambda'(z_0)
=
\lambda(1-\alpha r^2)
+
(1-\lambda)q^2
\]
and
\[
N_\lambda
=
H_\lambda'(z_0)+z_0H_\lambda''(z_0).
\]
Then
\[
N_\lambda
=
\lambda(1+\alpha r^2)
+
(1-\lambda)
\left(
\frac2q-q^2
\right).
\]
Hence
\[
\operatorname{Re}\!\left(
1+\frac{z_0H_\lambda''(z_0)}{H_\lambda'(z_0)}
\right)
=
\frac{
\operatorname{Re}(N_\lambda\overline{D_\lambda})
}{
|D_\lambda|^2
}.
\]

Exact rational arithmetic gives
\[
\operatorname{Re}(N_\lambda\overline{D_\lambda})
=
\frac{P(\lambda)}{25920000000}
\]
and
\[
|D_\lambda|^2
=
\frac{Q(\lambda)}{25920000000},
\]
with \(P,Q\) as stated above.

All coefficients of \(Q\) are positive, so
\[
Q(\lambda)>0
\]
on \([0,1]\). The discriminant of \(P\) is
\[
133861636456560000000
=
36000^2\cdot103288299735.
\]
Thus its roots are exactly \(\lambda_-\) and \(\lambda_+\). Since the leading coefficient of \(P\) is positive,
\[
P(\lambda)\le0
\]
exactly on
\[
[\lambda_-,\lambda_+].
\]
At interior points the real part is negative; at the two endpoints it is zero. In either case the strict exterior-convexity criterion fails at \(z_0\).

It remains only to record that every mixture still belongs to \(\Sigma\). The source's Laurent expansion has one \(F\)-tail term with weighted size \(|\alpha|\), while the weighted \(G\)-tail has total size
\[
1-(1-|\beta|)^{2/3}.
\]
For general \(0<\lambda<1\), the weighted tail sum is therefore
\[
\lambda|\alpha|
+
(1-\lambda)
\left[
1-(1-|\beta|)^{2/3}
\right]
<
\lambda+(1-\lambda)
=
1.
\]
The same weighted Laurent-tail criterion used in the source proves that \(H_\lambda\) is injective on \(\Delta^*\) for every \(0<\lambda<1\). Thus the whole family lies in \(\Sigma\), while the displayed interval is certified nonconvex.

## Verification

The exact polynomial identity was independently replayed from the source parameters using rational complex arithmetic in the included checker.

At
\[
\lambda=\frac35,
\]
the formula reduces to
\[
-\frac{54160961609}{69013985609}
=
-0.784782405059894966\ldots,
\]
which exactly matches the source's published test value.

The checker also verifies the exact discriminant, the two interval endpoints, positivity of \(Q\) on \([0,1]\), and the weighted-tail inequality for representative symbolic bounds. No finite sampling is used to infer the sign interval: it follows from the exact quadratic.

## Relationship to prior work

Guo and Hu resolve Pommerenke's long-standing question by giving one explicit pair \(F,G\) and choosing
\[
\lambda=\frac35.
\]
Their proof evaluates the curvature criterion at \(z_0=400/399\) and obtains a strictly negative rational real part. Their concluding discussion explains the failure through the complex phase in the derivative-weighted curvature identity.

The source does not vary \(\lambda\), state a robustness interval, or compute the exact two crossing weights. The calculation here keeps the same pair and same test point but treats the mixing parameter symbolically, converting an isolated counterexample into a quantitatively robust one-parameter family.

The 2019 edition of the function-theory problem collection still recorded no progress on Problem 6.10; the 2026 paper is the first negative solution identified in the searches. Targeted searches for the source identifier together with interval, robustness, mixture-weight, and curvature-crossing formulations did not locate a published parameter calibration equivalent to the finding.

## Limitations

The interval is exact for the obstruction detected at the fixed point \(z_0=400/399\). A mixture outside this interval may still fail convexity at another point.

The theorem does not classify all \(\lambda\) for which this particular pair \(F,G\) is exterior convex.

No claim is made about all convex pairs in \(\Sigma\); the result quantitatively calibrates the explicit Guo--Hu pair.

## References

1. Y. Guo and X. Hu, *A Counterexample to a Problem of Pommerenke on Convex Functions in the Class \(\Sigma\)*, arXiv:2609.04279v1, 2026.
2. Ch. Pommerenke, *Über einige Klassen meromorpher schlichter Funktionen*, Mathematische Zeitschrift 78 (1962), 263--284.
3. W. K. Hayman and E. F. Lingham, *Research Problems in Function Theory: Fiftieth Anniversary Edition*, Springer, 2019, Problem 6.10.
