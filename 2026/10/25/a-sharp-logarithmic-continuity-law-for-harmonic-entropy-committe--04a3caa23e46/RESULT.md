# A sharp logarithmic continuity law for harmonic-entropy committee payments

## Finding
Becker, Greger and Peters introduced a harmonic-entropy potential to optimize voter payment vectors in approval-based multiwinner elections [1]. We determine the **sharp small-error conditioning** of that potential and an exact law for opening a previously absent payment destination. These are properties of the voter-level potential; no new theorem about which committees are core-stable is asserted.

For an integer \(d\ge1\), let \(\Delta^d=\{x\in[0,1]^d:\sum_i x_i=1\}\). Write \(x_{(1)}\ge\cdots\ge x_{(d)}\), \(S_t(x)=\sum_{i=1}^t x_{(i)}\), and, for integers \(\ell\ge0\), define
\[
f_\ell(x)=\max_{1\le t\le d}\frac{S_t(x)}{\ell+t},\qquad F(x)=\sum_{\ell=0}^\infty\left(\frac1{\ell+1}-f_\ell(x)\right).
\]
The series converges. Coordinates represent payments and an unspent reserve, with zero coordinates permitted.

**Theorem (complete binary and sharp general sensitivity).** Let
\[
\omega_d(\delta)=\sup\{ |F(x)-F(y)|:x,y\in\Delta^d,\ \|x-y\|_1\le\delta\}.
\]
For every fixed \(d\ge2\),
\[
\boxed{\omega_d(\delta)=\frac\delta2\log\frac1\delta+O_d(\delta)}\quad(\delta\downarrow0).
\]
In particular the leading constant \(1/2\) is optimal, and \(F\) is not globally Lipschitz on \(\Delta^d\). For the fundamental case of one funded option and a reserve (two coordinates), the complete modulus for \(0\le\delta\le2\) is
\[
\boxed{\omega_2(\delta)=\begin{cases}
0,&\delta=0,\\
eH_{M-1}+M^{-1},&0<\delta\le1,\quad e=\delta/2,\quad M=\lfloor1/e\rfloor,\\
1,&1\le\delta\le2.
\end{cases}}
\]
The two branches coincide at \(\delta=1\).

**Exact marginal-option law.** For every integer \(s\ge1\), every strictly positive \(x\in\Delta^s\), and every
\(0<e\le(1-e)\min_i x_i\), with \(M=\lfloor1/e\rfloor\),
\[
\boxed{F((1-e)x_1,\ldots,(1-e)x_s,e)=(1-e)F(x)+eH_{M-1}+M^{-1}.}
\]
Thus an initially unused destination funded with a small share \(e\), rescaling all old destinations proportionally, has a universal leading bonus
\[
F((1-e)x,e)-F(x)=e\log(1/e)+e(1+\gamma-F(x))+O_x(e^2),
\]
where \(\gamma\) is Euler's constant. The exact identity is conditional: it is not asserted after the new coordinate exceeds an old rescaled coordinate.

## Assumptions and scope
All dimensions are finite. The \(\ell_1\) distance is \(\|x-y\|_1=\sum_i|x_i-y_i|\); \(\delta\) is a **distance bound**, not half this bound. Logarithms in asymptotic formulas are natural. Harmonic numbers are \(H_0=0\) and \(H_m=\sum_{j=1}^{m}j^{-1}\). In the splitting statement \(x\) has positive entries, so its support size is exactly \(s\). Appending zero coordinates does not change \(F\). Payment vectors of a voter consist of payments toward approved selected candidates together with a reserve; the theorem does not assert that the perturbation necessarily remains feasible under every whole-election budget constraint.

## Proof
**1. A finite exact evaluation lemma.** For positive \(z\in\Delta^s\), all sufficiently large \(\ell\) satisfy \(f_\ell(z)=1/(\ell+s)\). Indeed, at level \(1/(\ell+s)\), all \(s\) coordinates exceed the level as soon as \(1/(\ell+s)\le\min_i z_i\); the water-filling identity \(\sum_i(z_i-\tau)_+=\ell\tau\) then gives the unique level [1, Proposition 4.1]. Consequently, when \(f_\ell(z)=1/(\ell+s)\) for every \(\ell\ge L\), telescoping yields
\[
F(z)=H_{L+s-1}-\sum_{\ell=0}^{L-1}f_\ell(z).
\]
This equality permits exact rational evaluation, not numerical truncation.

**2. Exact marginal-option identity.** Sort the positive old coordinates decreasingly, and put \(y=((1-e)x,e)\). The condition \(e\le(1-e)\min x_i\) makes the new coordinate last. Hence, for each integer \(\ell\ge0\),
\[
f_\ell(y)=\max\left\{(1-e)f_\ell(x),\frac1{\ell+s+1}\right\}.
\]
Let \(M=\lfloor1/e\rfloor\) and \(K=M-s-1\). The assumption implies \(M\ge s+1\) and \(\min x_i\ge e/(1-e)\ge1/M\), so \(K\ge0\). For \(\ell\le K\), \(f_\ell(x)\ge1/(\ell+s)\) and \((1-e)/(\ell+s)\ge1/(\ell+s+1)\); therefore \(f_\ell(y)=(1-e)f_\ell(x)\). For \(\ell>K\), we have \(\ell+s\ge M\) and \(\min x_i\ge1/M\), so \(f_\ell(x)=1/(\ell+s)\), and the other branch wins: \(f_\ell(y)=1/(\ell+s+1)\). Subtract the defining series to obtain
\[
F(y)-F(x)=e\sum_{\ell=0}^K f_\ell(x)+\sum_{\ell>K}\left(\frac1{\ell+s}-\frac1{\ell+s+1}\right)
=e\sum_{\ell=0}^K f_\ell(x)+\frac1M.
\]
The finite evaluation lemma with \(L=K+1\) gives \(\sum_{\ell=0}^Kf_\ell(x)=H_{M-1}-F(x)\), establishing the boxed identity. As \(M=1/e+O(1)\), the standard harmonic-number expansion \(H_{M-1}=\log(1/e)+\gamma+O(e)\) and \(1/M=e+O(e^2)\) gives the claimed small-share expansion.

**3. Exact two-coordinate modulus.** Put \(g(p)=F(p,1-p)\), \(0\le p\le1\). Symmetry and concavity of \(F\), established in [1, Lemma 4.4], imply that \(g\) is symmetric about \(1/2\) and nondecreasing and concave on \([0,1/2]\). Every increment of length at most \(e\le1/2\) in \(g\), in either direction or across the midpoint, is therefore bounded by \(g(e)-g(0)\); concavity makes the increment from the boundary maximal. This value is attained at \(p=0\) and \(p=e\), whose corresponding \(\ell_1\) distance is \(2e\). The marginal-option identity with \(s=1\) and \(x=(1)\) gives \(g(e)=eH_{M-1}+1/M\). For \(\delta\ge1\), the universal range \(0\le F\le H_1=1\) is sharp between a vertex and the midpoint, at distance exactly \(1\). Hence the complete binary formula.

**4. Optimal modulus in any fixed dimension.** Write \(e=\delta/2\). Since two probability vectors differ by total variation at most \(e\), any fixed subset mass, and hence any largest-\(t\) partial sum, changes by at most \(e\). Thus
\[
|f_\ell(x)-f_\ell(y)|\le\frac{e}{\ell+1}\qquad(\ell\ge0).
\]
The nonnegative tail of \(F\) beyond the first \(L\) summands lies in \([0,(d-1)/(L+1)]\) by [1, Lemma 4.4]. For all \(x,y\in\Delta^d\),
\[
|F(x)-F(y)|\le eH_L+\frac{d-1}{L+1}.
\]
Choosing \(L=\lceil(d-1)/e\rceil\) gives \(\omega_d(\delta)\le e\log(1/e)+O_d(e)\). For the matching lower bound, compare \((1,0,\ldots,0)\) with \((1-e,e,0,\ldots,0)\), and use zero-coordinate invariance and the exact binary formula: their difference is \(e\log(1/e)+O(e)\). Since \(e=\delta/2\), the sharp coefficient is \(1/2\) when written against \(\delta\log(1/\delta)\).

## Verification
The standalone `verify.py` implements the finite evaluation lemma with exact rational arithmetic. It checked 4,826 nontrivial rational splitting and binary-modulus comparisons, including reciprocal-integer equality cases and a grid search over both binary probability parameters. It also prints illustrative convergence ratios. These finite checks do not replace the universal proof or certify originality.

For example, at total-variation share \(e=1/10\), the new two-destination score is \(F(9/10,1/10)=H_9/10+1/10=0.3828968253968\ldots\). Thus the entropy-based voting potential has a quantifiably singular response near a reserve-only or single-payment vertex, even though the potential remains continuous.

To reproduce: run `python verify.py` with Python 3.10 or later; only the standard library is used.

## Relationship to prior work
Becker, Greger and Peters [1] introduce this particular water-filling harmonic-entropy functional and prove symmetry, concavity, uniform-tail estimates, and an exact gain identity for their water-filling shift. Their accessible full Sections 4–5 do not state the present sharp optimal continuity modulus, binary closed form, or restricted mass-splitting identity. We use their foundational properties explicitly and do not claim the original objective or voting core-existence theorem.

Audenaert [2] proves a sharp continuity inequality for **Shannon/von Neumann entropy**, which is related in motivation but concerns a different entropy functional (uniform values \(\log d\) rather than \(H_{d-1}\)). The known Shannon estimate does not imply the boxed harmonic-entropy formulas; in particular the exact discrete harmonic-number floors and conditional grouping identity must be derived from the water-filling definition.

## Limitations
The theorem describes voter-level potential sensitivity, not continuity of the identity of a winning committee. The splitting identity is conditional on the new payment share being no larger than each rescaled old share; outside that range no unrestricted grouping formula is claimed. The general-dimensional modulus is sharp **to leading logarithmic order**, not a complete finite-\(\delta\) formula for \(d\ge3\). The novelty comparison is based on accessible literature and mathematical record searches; equivalent results under other descriptions cannot be ruled out independently.

## References
[1] P. Becker, M. Greger, and D. Peters, *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912v1, first posted 2026-09-10. https://arxiv.org/html/2609.11912v1

[2] K. M. R. Audenaert, *A Sharp Fannes-type Inequality for the von Neumann Entropy*, arXiv:quant-ph/0610146v1, first posted 2006-10-18. https://arxiv.org/html/quant-ph/0610146v1
