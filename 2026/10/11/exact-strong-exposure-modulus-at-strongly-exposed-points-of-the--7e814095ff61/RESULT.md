# Exact strong-exposure modulus at strongly exposed points of the binary tree space
## Finding
Let \(X_T\) be the real binary tree space built on the infinite binary tree \(T\), with norm
\[
\|z\|=\sup_{A\text{ a chain in }T}\sum_{t\in A}|z(t)|.
\]
Lõo and Perreau prove that \(x\in S_{X_T}\) is strongly exposed exactly when there is a finite maximal antichain \(\alpha\subset T\) such that \(|x(s)|=1\) for every \(s\in\alpha\). If \(N=|\alpha|\), their canonical exposing functional is
\[
f_\alpha=\frac1N\sum_{s\in\alpha}\operatorname{sgn}(x(s))e_s^*.
\]
For \(\delta>0\), define
\[
\rho_{x,f_\alpha}(\delta)=\sup\{\|y-x\|:y\in B_{X_T},\ f_\alpha(y)>1-\delta\}.
\]
Then
\[
\rho_{x,f_\alpha}(\delta)=\min\{2,2N\delta\}.
\]
The estimate is sharp for every \(\delta>0\), including the transition value \(\delta=1/N\), where the supremum equals \(2\) although it need not be attained inside the strict slice.

## Assumptions and scope
The scalar field is real, as in the focal source. The tree is the infinite binary tree used there, and \(\alpha\) is a finite maximal antichain. The claim concerns the specific norm-one exposer \(f_\alpha\) displayed above. It does not assert that this exposer is optimal among all possible exposing functionals for \(x\), and it does not address arbitrary denting points.

Maximality of \(\alpha\) implies that every node of \(T\) is comparable with some element of \(\alpha\), and every branch meets \(\alpha\) in exactly one point. Because \(|x(s)|=1\) for \(s\in\alpha\) and \(\|x\|=1\), the norm definition forces \(x(t)=0\) for every \(t\notin\alpha\). Thus \(\operatorname{supp}x=\alpha\).

## Proof
Fix \(y\in B_{X_T}\) with \(f_\alpha(y)>1-\delta\). For each \(s\in\alpha\), write
\[
\varepsilon_s=1-\operatorname{sgn}(x(s))y(s).
\]
Since \(|y(s)|\le1\), each \(\varepsilon_s\ge0\), and the slice condition gives
\[
\sum_{s\in\alpha}\varepsilon_s
=N\bigl(1-f_\alpha(y)\bigr)<N\delta.
\]
Take any chain and extend it to a branch \(\beta\). Let \(s\) be the unique point of \(\beta\cap\alpha\). Since \(x\) vanishes off \(\alpha\),
\[
\sum_{t\in\beta}|y(t)-x(t)|
=|y(s)-x(s)|+\sum_{t\in\beta\setminus\{s\}}|y(t)|.
\]
The condition \(y\in B_{X_T}\) gives
\[
\sum_{t\in\beta\setminus\{s\}}|y(t)|\le1-|y(s)|.
\]
Set \(a=\operatorname{sgn}(x(s))y(s)\in[-1,1]\). Then
\[
|y(s)-x(s)|+1-|y(s)|=(1-a)+1-|a|\le2(1-a)=2\varepsilon_s.
\]
Therefore every chain satisfies
\[
\sum |y(t)-x(t)|<2N\delta,
\]
and hence
\[
\|y-x\|\le\min\{2,2N\delta\}.
\]
The extra bound \(2\) is the diameter bound for the unit ball.

For sharpness, fix \(s\in\alpha\) and a strict descendant \(t\succ s\). For any
\[
0<\varepsilon<\min\{1,N\delta\},
\]
define \(y_\varepsilon\) by keeping all coordinates of \(x\) on \(\alpha\setminus\{s\}\), replacing \(x(s)\) with \((1-\varepsilon)x(s)\), putting \(y_\varepsilon(t)=\varepsilon\), and setting all other coordinates to zero. Every branch through \(s\) has total absolute mass at most \(1\), and branches through other members of \(\alpha\) have mass \(1\), so \(\|y_\varepsilon\|=1\). Moreover,
\[
f_\alpha(y_\varepsilon)=1-\frac\varepsilon N>1-\delta,
\]
while the chain \(\{s,t\}\) gives
\[
\|y_\varepsilon-x\|=2\varepsilon.
\]
If \(N\delta\le1\), let \(\varepsilon\uparrow N\delta\). If \(N\delta>1\), let \(\varepsilon\uparrow1\). These two limits attain the upper bound as a supremum and prove
\[
\rho_{x,f_\alpha}(\delta)=\min\{2,2N\delta\}.
\]

## Verification
The proof is symbolic. Its critical points are: maximal antichains meet every branch exactly once; the source norm bounds the total absolute mass on each branch by \(1\); a norm-one strongly exposed point with modulus-one coordinates on \(\alpha\) has no support outside \(\alpha\); and the explicit perturbation \(y_\varepsilon\) stays in the unit sphere. No finite enumeration, numerical optimization, or asymptotic extrapolation is used.

The first-public date and primary classification are taken from the arXiv record for version 1: 13 March 2026, primary MSC2020 46B04. The source's full text was inspected at the definition of \(X_T\) and Proposition 3.2, where the qualitative strong-exposure characterization and the canonical functional \(f_\alpha\) are stated.

## Relationship to prior work
Lõo and Perreau prove that the displayed \(f_\alpha\) strongly exposes \(x\), and use the resulting strongly exposed points to prove that \(B_{X_T}\) is dentable. Their Proposition 3.2 does not state a quantitative exposure radius, a dependence on \(|\alpha|\), or a sharp transition at \(\delta=1/N\). The exact formula above refines that qualitative statement without changing the space or the exposing functional.

Targeted searches for quantitative strong-exposure moduli, slice radii, maximal-antichain dependence, and the exact factor \(2N\delta\) found no implication-equivalent result for this binary tree space. General literature on strongly exposing functionals concerns existence, density, or residuality and does not supply this object-specific sharp radius.

## Limitations
The result is for the canonical exposing functional attached to a strongly exposed point. It does not compare all exposing functionals for the same point, does not compute the diameter of the whole slice, and does not extend automatically to the modified or countably branching tree spaces. Older literature may use different terminology for quantitative strong exposure, so an equivalent formulation outside the searched terminology remains a residual originality risk.

## References
1. M. Lõo and Y. Perreau, *A Banach space with an unconditional basis which is not slicely countably determined*, arXiv:2603.12947v1 (2026), especially the definition of \(X_T\) and Proposition 3.2.
2. M. Jung, M. Martín, and A. Rueda Zoca, *Residuality in the set of norm attaining operators between Banach spaces*, Journal of Functional Analysis 284 (2023), 109746, for general background on strongly exposing functionals.
