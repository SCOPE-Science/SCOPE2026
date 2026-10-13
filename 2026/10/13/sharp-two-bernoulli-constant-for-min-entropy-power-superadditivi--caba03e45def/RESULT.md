# Sharp two-Bernoulli constant for min-entropy power superadditivity
## Finding
Let \(B_1,B_2\) be independent Bernoulli random variables. For any integer-valued random variable \(X\), write
\[
M(X)=\max_x\Pr\{X=x\},
\qquad
\Delta_\infty(X)=M(X)^{-2}-1.
\]
Then
\[
\Delta_\infty(B_1+B_2)\ge
\frac12\left(\Delta_\infty(B_1)+\Delta_\infty(B_2)\right).
\]
The coefficient \(1/2\) is best possible. Equality holds when both Bernoulli variables are deterministic, and among pairs with positive total individual deficit it holds exactly when both variables are fair. In particular, if the coefficient \(1/2\) fails for a sum of independent Bernoulli variables, at least three summands are necessary.

## Assumptions and scope
A Bernoulli variable may be degenerate. Independence is required. The result concerns the min-entropy limit of Rényi entropy power and exactly two summands; it does not determine the optimal universal min-entropy power constant for three or more Bernoulli summands or for arbitrary integer-valued random variables.

For a Bernoulli variable \(B\), let \(u=M(B)\in[1/2,1]\) be its modal mass and set
\[
r=\frac{1-u}{u}\in[0,1].
\]
Thus \(u=(1+r)^{-1}\). We use the analogous notation \(v\) and \(s\) for the second Bernoulli variable.

## Proof
The desired inequality is equivalent to
\[
M(B_1+B_2)^2\le
\frac{2u^2v^2}{u^2+v^2}.
\]
Indeed, adding \(1\) to both sides of the deficit inequality gives
\[
M(B_1+B_2)^{-2}\ge
\frac12\left(u^{-2}+v^{-2}\right).
\]

There are only two possible orientations of the modal atoms. If the two modal atoms point in the same direction, the three convolution masses, up to reversal, are
\[
uv,\qquad uv(r+s),\qquad uvrs.
\]
Hence
\[
M(B_1+B_2)=uvc,
\qquad c=\max\{1,r+s\}.
\]
Because \(0\le r,s\le1\), both \(1\) and \(r+s\) are at most \(1+r\) and at most \(1+s\). Therefore
\[
\frac{c}{1+r}\le1,
\qquad
\frac{c}{1+s}\le1.
\]

If the modal atoms point in opposite directions, the convolution masses, again up to reversal, are
\[
uvr,\qquad uv(1+rs),\qquad uvs.
\]
Since \(1+rs\ge r,s\), now
\[
M(B_1+B_2)=uvc,
\qquad c=1+rs.
\]
Moreover
\[
1+rs\le1+r,
\qquad
1+rs\le1+s,
\]
so the same two bounds for \(c/(1+r)\) and \(c/(1+s)\) hold.

In either orientation,
\[
\begin{aligned}
M(B_1+B_2)^2(u^2+v^2)
&=u^2v^2c^2(u^2+v^2)\\
&=u^2v^2\left[
\left(\frac{c}{1+r}\right)^2+
\left(\frac{c}{1+s}\right)^2
\right]\\
&\le2u^2v^2,
\end{aligned}
\]
which is exactly the required inequality.

For equality with positive total individual deficit, both displayed ratios must equal \(1\). In the same-orientation case this forces \(r=s=1\); in the opposite-orientation case the conditions \(r(1-s)=0\) and \(s(1-r)=0\) force either \(r=s=0\) or \(r=s=1\). The first possibility is the completely deterministic case. Thus every nontrivial equality case has \(r=s=1\), equivalently both Bernoulli variables are fair.

For two fair Bernoulli variables, each individual deficit equals \(3\), while their sum has maximum point mass \(1/2\) and hence deficit \(3\). The ratio is therefore exactly \(3/6=1/2\), proving sharpness.

## Verification
The proof is algebraic and covers the whole parameter square, including degenerate boundaries. The accompanying `verify.py` performs an exact rational stress test on \(10201\) parameter pairs and verifies the fair-coin equality case. Its output is

`VERIFY_OK ratio=1/2 grid_pairs=10201`

The finite grid is supplemental only; the universal quantifiers are established by the two orientation inequalities in the proof.

## Relationship to prior work
Bobkov, Marsiglietti, and Melbourne introduced the discrete entropy-power deficit \(\Delta_\alpha=N_\alpha-1\) in this setting and proved two-sided entropy-power inequalities for discrete log-concave variables. Their discussion points to Bernoulli summands as a central nonsymmetric test class.

Madiman, Melbourne, and Roberto subsequently proved lower min-entropy power bounds for arbitrary Bernoulli sums and for broader independent integer-valued sums. They also observed that the largest universal coefficient cannot exceed \(1/2\), using two independent fair Bernoulli variables. Their stated lower bounds are strictly below \(1/2\) and do not give the exact heterogeneous two-Bernoulli constant. The present result closes that two-summand Bernoulli subproblem: the fair-pair upper obstruction is also the exact lower constant throughout the full two-parameter Bernoulli family.

Earlier majorization results for sums of integer-valued variables, including fair-binomial and weighted-sum comparisons, do not imply this ratio inequality because the denominator here changes with both individual Bernoulli modal masses.

## Limitations
The theorem does not settle the optimal coefficient when three or more Bernoulli summands are allowed, and it does not settle the universal independent integer-valued problem. A residual literature risk is that the elementary two-parameter inequality may have appeared under concentration-function rather than entropy-power terminology.

## References
1. S. G. Bobkov, A. Marsiglietti, and J. Melbourne, *Concentration functions and entropy bounds for discrete log-concave distributions*, arXiv:2007.11030; DOI:10.1017/S096354832100016X.
2. M. Madiman, J. Melbourne, and C. Roberto, *Bernoulli sums and Rényi entropy inequalities*, arXiv:2103.00896; DOI:10.3150/22-BEJ1511.
3. M. Madiman, L. Wang, and J. O. Woo, *Majorization and Rényi entropy inequalities via Sperner theory*, arXiv:1712.00913; DOI:10.1016/j.disc.2019.03.002.
