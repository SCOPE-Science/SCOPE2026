# Exact escape-time phase transition for symmetric negative-doubling holes

## Finding

Let \(T:[0,1]\setminus\{1/2\}\longrightarrow[0,1]\) be the piecewise-affine map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\ 2-2x,&1/2<x\le1.\end{cases}
\]
For any \(0<a<1/2\), remove the open interval \(H_a=(a,1-a)\) and retain \(S_a=[0,a]\cup[1-a,1]\). Write \(m\) for Lebesgue measure and, for each integer \(n\ge0\), set
\[
E_n(a)=\{x\in S_a:T^j(x)\in S_a\text{ for }0\le j\le n\}.
\]
Endpoint itineraries have zero Lebesgue measure; no value of the map at the excluded discontinuity is needed.

**Exact finite-time survival law.** For every real \(0<a\le2/5\) and every integer \(n\ge0\),
\[
\boxed{\displaystyle m(E_n(a))=\frac{2a+2n(3a-1)_+}{2^n},\qquad (u)_+=\max\{u,0\}.}
\]
Thus the survival law is purely geometric when \(0<a\le1/3\), but has a nonzero linear prefactor at every \(1/3<a\le2/5\). Its exponential escape rate is \(\log2\) throughout, whereas the polynomial correction switches sharply at \(a=1/3\).

Choose the initial state uniformly on \(S_a\) and let \(\tau=\inf\{j\ge1:T^j(x)\in H_a\}\). Then, for all integers \(n\ge0\),
\[
\boxed{\displaystyle \Pr(\tau>n)=2^{-n}\left(1+\frac{n(3a-1)_+}{a}\right),\qquad
\mathbb E\tau=\begin{cases}2,&0<a\le1/3,\\8-2/a,&1/3\le a\le2/5.\end{cases}}
\]
For \(1/3<a\le2/5\), the one-step conditional escape probability after surviving \(n\) steps equals
\[
\Pr(\tau=n+1\mid\tau>n)=\frac12-\frac{3a-1}{2[a+n(3a-1)]},
\]
so it approaches \(1/2\) from below at the exact order \(1/n\).

**Sharp upper parameter boundary.** For every \(2/5<a<1/2\), the exact two-step mass is \(m(E_2(a))=6a-2\); this exceeds the extension of the boxed formula by \((5a-2)/2>0\). Thus \(2/5\) is the maximal upper endpoint of the displayed all-time phase law.

## Assumptions and scope

The dynamical space is the closed interval, not the quotient circle. The points \(0\) and \(1\) are distinct and interchange under \(T\). The open hole retains its two endpoints; these choices affect some periodic orbits but not Lebesgue escape probabilities. All survival statements concern the initially normalized restriction of Lebesgue measure, not an invariant or conditionally invariant probability. There is no claim of a uniform escape formula for asymmetric holes, \(a>2/5\), or nonlinear decreasing Lorenz maps. Both equality parameters \(a=1/3\) and \(a=2/5\) are included.

## Proof

Write \(L(y)=(1-y)/2\) and \(R(y)=1-y/2\) for the two inverse branches. Each sends a measurable interval into a half-interval and halves its length. The basic recursion is
\[
E_{n+1}(a)=S_a\cap\left(L(E_n(a))\cup R(E_n(a))\right),
\]
with all interval decompositions interpreted up to Lebesgue-null endpoints.

**Small holes in parameter space: \(0<a\le1/3\).** The first surviving preimage consists precisely of the two outer intervals \([0,a/2]\) and \([1-a/2,1]\). Their only surviving inverse branches alternate between the two ends: for any \(0<b\le a\), the inverse image of \([0,b]\) inside \(S_a\) is \([1-b/2,1]\), and the inverse image of \([1-b,1]\) inside \(S_a\) is \([0,b/2]\). The potentially competing branches lie in the hole because \(a\le1/3\). Induction gives \(E_n=[0,a/2^n]\cup[1-a/2^n,1]\) up to endpoints and hence \(m(E_n)=2a/2^n\).

**Four-block regime: \(1/3\le a\le2/5\).** Define four pairwise interior-disjoint closed blocks, ordered left to right:
\[
B_L=[0,a/2],\qquad C_L=[(1-a)/2,a],\qquad
C_R=[1-a,(1+a)/2],\qquad B_R=[1-a/2,1].
\]
Direct intersection with the two inverse branches gives \(E_1=B_L\cup C_L\cup C_R\cup B_R\). The inverse images of the four blocks that remain in \(S_a\) satisfy the following complete transition table:
\[
\begin{array}{c|c}
\text{target block}&\text{surviving inverse branches and destination blocks}\\\hline
B_L&R(B_L)\subseteq B_R\\
C_L&L(C_L)\subseteq C_L,\ R(C_L)\subseteq B_R\\
C_R&L(C_R)\subseteq B_L,\ R(C_R)\subseteq C_R\\
B_R&L(B_R)\subseteq B_L.
\end{array}
\]
For example, \(L(B_L)=[(2-a)/4,1/2]\) does not intersect \(S_a\) in positive measure because \((2-a)/4\ge a\) is equivalent to \(a\le2/5\). Its reflected counterpart \(R(B_R)=[1/2,(2+a)/4]\) is likewise disjoint from \(S_a\) in positive measure. The remaining inclusions are elementary endpoint inequalities; the two core-to-core inclusions require \(a\ge1/3\). Every inverse image listed in the table is disjoint from all others up to endpoints, since the two branches are injective with disjoint domains and the target blocks have disjoint interiors. The table thus applies to every measurable subset of each block, at every depth—not merely to whole blocks.

Let \(b_n=m(E_n\cap B_L)=m(E_n\cap B_R)\) and \(c_n=m(E_n\cap C_L)=m(E_n\cap C_R)\), where equality in each pair follows from reflection symmetry. For \(n\ge1\), the table yields the **exact** recurrences
\[
c_{n+1}=\frac12c_n,\qquad b_{n+1}=\frac12(b_n+c_n),\qquad
c_1=\frac{3a-1}{2},\quad b_1=\frac a2.
\]
Therefore
\[
c_n=\frac{3a-1}{2^n},\qquad b_n=\frac{a+(n-1)(3a-1)}{2^n},
\]
and summing the four block masses gives
\[
m(E_n)=2(b_n+c_n)=\frac{2a+2n(3a-1)}{2^n},\qquad n\ge1.
\]
At \(n=0\) this agrees with \(m(S_a)=2a\); at \(a=1/3\) the core blocks degenerate to points and the formula coincides with the first regime. The linear factor arises from a nontrivial length-two Jordan chain for the eigenvalue \(1/2\) in the finite-volume transfer recurrence when \(3a-1>0\); no finite experiment is used to infer this infinite-time property.

**Entrance law and sharpness.** Since \(\{\tau>n\}=E_n\) under normalized initial Lebesgue measure, divide by \(2a\) to obtain the tail. The tail-sum identity \(\mathbb E\tau=\sum_{n\ge0}\Pr(\tau>n)\), together with \(\sum_{n\ge0}2^{-n}=2\) and \(\sum_{n\ge0}n2^{-n}=2\), proves the mean. The hazard follows from the exact ratio of consecutive tails.

For \(2/5<a<1/2\), the same four blocks describe \(E_1\), but the two previously forbidden branches now have positive intersections with \(S_a\):
\[
m(L(B_L)\cap S_a)=m(R(B_R)\cap S_a)=\frac{5a-2}{4}.
\]
All six previously allowed inverse-branch contributions still lie in their surviving blocks, and hence
\[
m(E_2)=\frac{14a-4}{4}+2\cdot\frac{5a-2}{4}=6a-2.
\]
The positive extra term gives the asserted sharp boundary.

## Verification

A standalone Python 3 standard-library checker, `verify_escape.py`, independently iterates interval inverse images using `fractions.Fraction`. It compares exactly computed finite-time survivor measures against the closed formula for nine rational parameters spanning both phases and both critical boundaries, for every horizon \(0\le n\le34\) (315 checks). It separately checks the strict upper-edge correction for four rational parameters in \((2/5,1/2)\). Output: `VERIFY_OK closed_form_cases= 315 upper_edge_cases= 4 max_exact_horizon=34`. The analytical block transition table establishes the quantified theorem for all real parameters and all horizons.

## Relationship to prior work

Ding, Steiner and Sun [1] establish symbolic admissibility, survivor-space plateaux and dimension/entropy properties for the negative-doubling map and decreasing Lorenz maps. The previously published symmetric-hole orbit census [2] identifies the precise orbit-birth parameters \(1/3\) and \(2/5\), along with zero topological entropy and the Artin–Mazur zeta function. Those orbit data do **not** determine finite-time Lebesgue escape: the zeta function is identical for every \(1/3<a<2/5\), whereas the proven survival probabilities vary linearly with \(a\) at every time. The parity-sensitive plateau-width identity [3] concerns widths in *hole-parameter space*, not the measure of initial conditions escaping in *phase space*. General work on escape rates for expanding Markov maps [4] motivates the transfer method but does not state these exact universal parameter-dependent horizon laws. These are mathematical nonimplication comparisons; they do not establish absolute historical priority.

## Limitations

The result is specific to the symmetric hole for the negative-doubling map and normalized Lebesgue initial data. The two-step sharpness statement is not a classification of escape for every \(a>2/5\). The universal proof depends on the four-block geometric inequalities; computer checks establish only finite instances. Escape exponent \(\log2\) alone is not claimed as novel; the contribution is the exact all-time tail, its sharp polynomial-prefactor transition and the parameter-specific boundary. Closely related generic Markov-hole methods may yield this law after further specialization, and equivalent unpublished or differently worded prior calculations cannot be excluded.

## References

[1] Y. Ding, W. Steiner and Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, first public 2026-10-02, https://arxiv.org/abs/2610.03327 .

[2] *A three-phase periodic-orbit and zeta trichotomy for symmetric negative-doubling holes* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-three-phase-periodic-orbit-and-zeta-trichotomy-for-symmetric-n--8027a957802c .

[3] *Exact parity law for negative-doubling survivor-plateau address widths* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-parity-law-for-negative-doubling-survivor-plateau-address--195a748d0893 .

[4] C. Haritha and N. Agarwal, *Product of expansive Markov maps with hole*, Discrete and Continuous Dynamical Systems 39 (2019), 5743–5774, doi:10.3934/dcds.2019252 .
