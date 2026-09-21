# Multiplicity-sharp Chebyshev desingularization for univariate moment-SOS

## Result

Consider the Chebyshev construction used by Henrion and Safey El Din for univariate moment-SOS convergence. Let
\[
A:=\operatorname{arsinh}(1),\qquad
V_n(t):=\frac{1-T_n(1-2t)}2,
\]
where \(T_n\) is the Chebyshev polynomial of the first kind. Their odd-multiplicity desingularization uses, for odd \(d\ge1\),
\[
q_{n,d}(t)=\varepsilon_n+t\bigl(1-V_n(t)^{d-1}\bigr),
\qquad
\varepsilon_n=\sinh^2(A/n),
\]
and proves \(q_{n,d}(t)\ge0\) for all \(t\le1\). The same polynomial identity works with a strictly smaller, multiplicity-dependent floor.

For odd \(d\ge3\), define
\[
\boxed{\delta_{n,d}:=
\max_{0\le y\le A}
\sinh^2(y/n)\Bigl(1-\sinh^{2(d-1)}y\Bigr).}
\]
For \(d=1\), set \(\delta_{n,1}=0\). Then
\[
\boxed{q^*_{n,d}(t):=\delta_{n,d}+t\bigl(1-V_n(t)^{d-1}\bigr)\ge0
\quad\text{for every }t\le1,}
\]
and \(\delta_{n,d}\) is the smallest constant for which this statement is true. Thus this is an exact optimization of the additive floor within the Chebyshev ansatz of the source paper, without changing the polynomial degree.

Writing \(W_n(t)=V_n(t)/t\), one retains the exact decomposition
\[
t+\delta_{n,d}=q^*_{n,d}(t)+t^dW_n(t)^{d-1},
\]
with
\[
\deg q^*_{n,d},\ \deg(t^dW_n^{d-1})\le 1+n(d-1).
\]

## Proof of the exact floor

For \(0\le t\le1\), one has \(0\le V_n(t)\le1\), so the nonconstant term in \(q^*_{n,d}\) is nonnegative. For \(t<0\), write
\[
1-2t=\cosh u,\qquad y=\frac{nu}{2}.
\]
Then
\[
|t|=\sinh^2(y/n),\qquad
V_n(t)=-\sinh^2 y.
\]
If \(V_n(t)\le-1\), then \(V_n(t)^{d-1}\ge1\), hence again
\(t(1-V_n(t)^{d-1})\ge0\). The only potentially negative region is therefore
\(-1<V_n(t)<0\), equivalently \(0<y<A\). There,
\[
q^*_{n,d}(t)
=\delta_{n,d}
-\sinh^2(y/n)\Bigl(1-\sinh^{2(d-1)}y\Bigr).
\]
The displayed maximum is therefore both sufficient and necessary. If the floor is lowered below \(\delta_{n,d}\), choosing a maximizing \(y\) produces a negative value. For \(d=1\), the factor \(1-V_n^{d-1}\) vanishes identically, so the exact minimum floor is zero.

For \(d\ge3\), the maximizer is unique and lies in \((0,A)\). Setting \(m=d-1\), it is the unique solution of
\[
\boxed{
1-\sinh^{2m}y
=mn\tanh(y/n)\sinh^{2m-1}y\cosh y.}
\]
Indeed, the logarithmic derivative of the objective is the difference of a strictly decreasing term \(n^{-1}\coth(y/n)\) and a strictly increasing positive term
\(m\sinh^{2m-1}y\cosh y/(1-\sinh^{2m}y)\), with opposite signs at the two endpoints.

## The source floor is the worst-multiplicity envelope

For each fixed \(n\),
\[
0=\delta_{n,1}<\delta_{n,3}<\delta_{n,5}<\cdots<\varepsilon_n,
\qquad
\boxed{\lim_{d\to\infty\atop d\ \mathrm{odd}}\delta_{n,d}=\varepsilon_n.}
\]
Thus the multiplicity-independent floor \(\varepsilon_n\) used in the source paper is exactly the worst-case envelope of the sharp floors as the odd multiplicity tends to infinity. Every fixed finite odd multiplicity admits a strict improvement.

There is also an explicit all-\(n\) multiplicity-sensitive bound. Convexity of \(\sinh\) gives
\(\sinh(y/n)\le \sinh(y)/n\), hence
\[
\boxed{
\delta_{n,d}\le \frac{\beta_d}{n^2},\qquad
\beta_d:=\frac{d-1}{d^{d/(d-1)}}<1
\quad(d\ge3).}
\]
This follows by setting \(z=\sinh^2 y\in[0,1]\) and maximizing
\(z(1-z^{d-1})\), whose maximum is \((d-1)d^{-d/(d-1)}\).

The exact asymptotic constant is sharper still:
\[
\boxed{
\lim_{n\to\infty}n^2\delta_{n,d}
=\kappa_d
:=\max_{0\le y\le A}
y^2\bigl(1-\sinh^{2(d-1)}y\bigr).}
\]
The maximizing point is unique and satisfies
\[
1-\sinh^{2(d-1)}y
=(d-1)y\sinh^{2d-3}y\cosh y.
\]
Moreover \(\kappa_d\) increases strictly with odd \(d\) and
\[
\lim_{d\to\infty}\kappa_d=A^2=\log^2(1+\sqrt2).
\]
For the first three nontrivial multiplicities,
\[
\begin{array}{c|c|c|c}
d & \kappa_d & \beta_d & \kappa_d/A^2\\ \hline
3 & 0.328651937359922 & 0.384900179459751 & 0.423073802487489\\
5 & 0.446859841005665 & 0.534992243981138 & 0.575242895666180\\
7 & 0.511125472514127 & 0.619731451199557 & 0.657972075083032
\end{array}
\]
where \(A^2=0.776819399895696\ldots\). In particular, cubic degeneracy uses only about 42.3% of the source construction's uniform asymptotic floor constant.

## Consequence for the univariate moment-SOS proof

The refinement propagates through the source paper's degree argument unchanged. Suppose a natural generator \(g\) satisfies \(g^d\in Q(p)\) for an odd \(d\), and choose the same positive scaling constant \(C\) as in the source proof so that \(g/C\le1\) on its Archimedean interval. Replacing \(\varepsilon_n\) by \(\delta_{n,d}\) in the preceding identity gives
\[
\boxed{g+C\delta_{n,d}\in Q_{Ln+B}(p)}
\]
for fixed \(L>0,B\ge0\), with the same linear-in-\(n\) degree bound as before.

For a full problem, let \(d_i\) be odd powers that place the natural generators \(g_i^{d_i}\) in the original quadratic module, and let
\[
D=\max_i d_i.
\]
Because \(\delta_{n,d}\) is increasing in \(d\), the source proof may use the common floor \(\delta_{n,D}\) for every generator. With the same fixed polynomial \(\sigma\), scalar majorant \(C'\), and affine certificate order \(Ln+B\) appearing in that proof, one obtains
\[
q+C'\delta_{n,D}\in Q_{Ln+B}(p).
\]
Consequently, for
\[
n(r)=\left\lfloor\frac{r-B}{L}\right\rfloor,
\]
the relaxation error obeys the refined certificate bound
\[
\boxed{e_r\le C'\delta_{n(r),D}.}
\]
If \(D\ge3\), then
\[
e_r\le \frac{C'\beta_D}{n(r)^2},
\]
and the same elementary estimate \(n(r)\ge r/(2L)\) used by the source for sufficiently large \(r\) yields
\[
\boxed{e_r\le \frac{4C'L^2\beta_D}{r^2},}
\]
replacing the corresponding multiplicity-blind factor \(4C'L^2\) by the strict factor \(4C'L^2\beta_D\). More precisely,
\[
\boxed{\limsup_{r\to\infty}r^2e_r\le C'L^2\kappa_D.}
\]
If \(D=1\), the natural generators themselves already lie in the original module and the same argument gives finite convergence rather than merely an asymptotic floor.

These statements sharpen the constants generated by this particular proof mechanism; they do not assert that \(\delta_{n,d}\), \(\beta_d\), or \(\kappa_d\) are globally optimal constants among all possible Positivstellensatz or moment-SOS certificates.

## Verification

`artifacts/verify_floor.py` independently evaluates the unique maximizers by bisection, checks the finite-\(n\) floors against the source floor, evaluates \(\kappa_d\) and \(\beta_d\), and numerically verifies that the sharpened polynomial is nonnegative on a dense grid covering the only potentially negative interval. `artifacts/verification_output.txt` contains the executed output. The analytic proof above is independent of this numerical check.

## Relation to prior literature

Henrion and Safey El Din prove the universal \(O(r^{-2})\) univariate moment-SOS rate and introduce the Chebyshev odd-multiplicity desingularization used here. Their Lemma 5 chooses \(\varepsilon_n\) by bounding \(1-V_n^{d-1}\le1\), making the floor independent of \(d\); their Lemma 7 and Theorem 1 then propagate that uniform floor into the approximate-generator and relaxation-error bounds. The present result optimizes that same one-dimensional Chebyshev construction exactly in \(d\), identifies the source floor as its worst-multiplicity envelope, and carries the sharper floor through the same degree argument.

Augustin's univariate quadratic-module work supplies the structural membership theorem used by the source to obtain odd powers of natural generators, but it predates this Chebyshev construction. Henrion's exact solution of Stengle's example determines the true relaxation error for a particular cubically degenerate problem by different extremal certificates; it does not give the multiplicity-sharp floor above for the general generator-recovery construction.

### References

- D. Henrion and M. Safey El Din, *Convergence rate of the moment-SOS hierarchy for univariate polynomial optimization*, arXiv:2609.20544 (2026). https://arxiv.org/abs/2609.20544
- D. Augustin, *The Membership Problem for finitely generated quadratic modules in the univariate case*, Journal of Pure and Applied Algebra 216 (2012), 2204–2212. https://doi.org/10.1016/j.jpaa.2012.02.004
- D. Henrion, *Solving Stengle's Example in Rational Arithmetic: Exact Values of the Moment-SOS Relaxations*, arXiv:2512.19141 (2025/2026). https://arxiv.org/abs/2512.19141

## Limitations

The floor is proved optimal only within the specific Chebyshev polynomial ansatz \(\delta+t(1-V_n^{d-1})\). The propagated moment-SOS constants remain proof-dependent because the scaling constants, natural-generator representation, Archimedean certificate, and affine degree slope are not optimized. The result does not improve the universal exponent \(2\), which the source proves is sharp, and it does not replace exact problem-specific certificates such as those available for Stengle-type examples. The external originality search found no prior statement of the multiplicity-sharp floor or its envelope/asymptotic laws, but the source preprint is very recent, so simultaneous or not-yet-indexed follow-up work remains a residual risk. Originality is claimed only to the best of our knowledge.
