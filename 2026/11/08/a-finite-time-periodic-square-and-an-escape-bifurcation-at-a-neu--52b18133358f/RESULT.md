# A finite-time periodic square and an escape bifurcation at a neutral border-collision focus

## Finding

For each parameter \(a\geq0\), consider the continuous piecewise-affine map \(F_a:\mathbb R^2\to\mathbb R^2\) given by
\[
F_a(x,y)=\begin{cases}(1+y-ax,0),&x\leq0,\\ (1+y,-x),&x>0.\end{cases}
\]
This is the zero-left-determinant border-collision normal form with \(\mu=1\), \(\tau_L=-a\), \(\tau_R=0\), and \(\delta_R=1\). The right-branch eigenvalues are exactly \(\pm i\), corresponding to rotation number \(1/4\).

**Complete global classification.** Let \(Q=[0,1]\times[-1,0]\). For every \(a\ge0\), the square \(Q\) is forward invariant and \(F_a^4\) is the identity on \(Q\). Its center \((1/2,-1/2)\) is the only fixed point in \(Q\), and all other points of \(Q\) have least period four. Its area is exactly one.

If \(0\le a\le1\), *every* orbit from \(\mathbb R^2\) reaches \(Q\) in finitely many iterations. Thus no unbounded trajectory or periodic orbit outside \(Q\) exists in this parameter range.

If \(a>1\), put \(p=a/(a-1)\). There is precisely one periodic orbit outside \(Q\), the primitive three-cycle
\[
P_a=\{(p,0),(1,-p),(1-p,-1)\}.
\]
Its nonzero return multiplier is \(a>1\) (the other multiplier is zero). Every orbit starting outside \(Q\) either reaches \(Q\) in finite time, eventually reaches \(P_a\), or escapes to infinity in norm. No other bounded non-eventually-periodic orbit exists.

**Exact exterior capture laws.** For an initial section point \((z,0)\) with \(z>1\), let \(N_a(z)\) be the number of three-iterate exterior return blocks before the orbit first reaches \(Q\). For \(0<a<1\),
\[
N_a(z)=\left\lceil\frac{\log((1-a)z+a)}{\log(1/a)}\right\rceil;
\]
for \(a=0\), \(N_0(z)=1\); and at the exact transition \(a=1\),
\[
N_1(z)=\lceil z-1\rceil.
\]
For \(a>1\) and \(1<z<p\),
\[
N_a(z)=\left\lceil\frac{\log\!\big(1/[a-(a-1)z]\big)}{\log a}\right\rceil.
\]
The corresponding number of original map iterates is exactly \(3N_a(z)\). Initial section points \(z<0\) first return to the section after one map iterate at \(z'=1-az\); this reduces their classification to the preceding cases. For \(a>1\), the section points \(z=p\) and \(z>p\) generate the three-cycle and escaping trajectories, respectively; after the preliminary left return, the same alternatives apply to \(z<0\).

In particular, for fixed \(0<a<1\) the capture count is \(\log z/|\log a|+O(1)\) as \(z\to\infty\); at \(a=1\) it is \(z+O(1)\); and for fixed \(a>1\) it diverges as \(\log(1/(p-z))/\log a+O(1)\) when \(z\uparrow p\). The positive fixed point \(p\) of the exterior return map retreats to infinity as \(a\downarrow1\), giving a precise transition from global finite-time periodic capture to an open escaping basin.

**Two-sided critical scaling.** Fix \(s>0\), and take initial section position \(z=s/\varepsilon\) as \(\varepsilon\downarrow0\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon N_{1-\varepsilon}(s/\varepsilon)=\log(1+s),
\qquad
\lim_{\varepsilon\downarrow0}\varepsilon N_1(s/\varepsilon)=s.
\]
For \(0<s<1\), the escaping-side limit also exists:
\[
\lim_{\varepsilon\downarrow0}\varepsilon N_{1+\varepsilon}(s/\varepsilon)=-\log(1-s).
\]
These functions quantify the nonuniform critical slowing on both sides of the global-absorption boundary; they describe the same exterior capture count as the main classification, not a separate dynamical assertion.

## Assumptions and scope

The parameter \(a\) is any real number satisfying \(a\ge0\); there is no boundedness hypothesis on the initial point \((x_0,y_0)\in\mathbb R^2\). The switching convention assigns \(x=0\) to the left formula, although both formulas agree there. Statements of exact exterior capture time assume \(z>1\) and, where relevant, \(z<p\); the section's closed interval \([0,1]\) is already contained in \(Q\). A *three-iterate exterior return block* begins and ends on the horizontal axis and passes through the left half-plane.

The parameter slice is a rational neutral-focus boundary of a five-parameter border-collision normal form. The conclusions are not asserted for general \(\tau_R\), \(\delta_R\), or for nonlinear perturbations.

## Proof

**Quarter-turn core.** Define the globally affine right extension \(R(x,y)=(1+y,-x)\). It is a clockwise quarter-turn about \((1/2,-1/2)\), and direct composition yields
\[
R^2(x,y)=(1-x,-1-y),\qquad R^3(x,y)=(-y,x-1),\qquad R^4(x,y)=(x,y).
\]
The square \(Q\) is invariant under \(R\). The two formulas for \(F_a\) agree at \(x=0\), so \(F_a=R\) everywhere on \(Q\). A quarter-turn has no noncentral fixed point under its first or second iterate. This proves the complete period classification inside \(Q\).

**Reduction of all exterior trajectories.** The four successive first coordinates of an \(R\)-orbit are \(x\), \(1+y\), \(1-x\), and \(-y\). They are all nonnegative if and only if \((x,y)\in Q\). Consequently, a point outside \(Q\) with positive first coordinate encounters the closed left half-plane within at most three iterates; a point already in that half-plane needs no such preliminary iterate. On the next iteration \(F_a\) maps it to the horizontal axis \(\Sigma=\mathbb R\times\{0\}\). Therefore every exterior orbit reaches \(\Sigma\) within at most four iterates, unless it has already entered \(Q\). Because \(Q\) is invariant, it cannot leave after entry.

**Exact return blocks.** For \(z<0\), direct application of the left branch gives
\[
F_a(z,0)=(1-az,0).
\]
For \(z>1\), its next two iterates are \((1,-z)\) and \((1-z,-1)\), and the latter has negative first coordinate. Applying the left branch gives
\[
F_a^3(z,0)=(a(z-1),0).
\]
Set \(H_a(z)=a(z-1)\) on the exterior interval \(z>1\). Every return block in this interval takes exactly three original iterates. Once the section coordinate belongs to \([0,1]\), the orbit has entered \(Q\). This is a stopped return algorithm; at the two section endpoints the unrestricted first-return map has different return times, but that does not affect capture.

**Absorption for \(a\le1\).** If \(a=0\), one exterior block sends any \(z>1\) to zero. If \(a=1\), successive exterior coordinates decrease by exactly one, hence enter \([0,1]\) in \(\lceil z-1\rceil\) blocks. If \(0<a<1\), the affine recurrence satisfies
\[
H_a^n(z)=-\frac{a}{1-a}+a^n\left(z+\frac{a}{1-a}\right).
\]
It decreases while its argument exceeds one and must enter \([0,1]\) after finitely many blocks. The first such \(n\) is the smallest integer satisfying \(a^n((1-a)z+a)\le1\), which gives the stated ceiling formula. Any \(z<0\) first maps to \(1-az\ge1\), so the conclusion extends to the entire axis, hence to the entire plane by exterior reduction.

**The exterior separator for \(a>1\).** The affine map \(H_a\) has the unique fixed point \(p=a/(a-1)>1\), and
\[
H_a^n(z)=p+a^n(z-p)
\]
for every consecutive block on which \(z>1\) remains true. If \(1<z<p\), the iterate decreases strictly until it first reaches \([0,1]\); solving \(p+a^n(z-p)\le1\) gives the third ceiling formula. If \(z=p\), the orbit has the three listed states, each in the strict indicated switching branch. If \(z>p\), the iterates diverge exponentially to \(+\infty\), and every intermediate original-map state also has norm tending to infinity. Points \(z<0\) first pass to \(1-az>1\), which is classified by comparing that number with \(p\). The exterior reduction proves the trichotomy for all planar initial conditions.

For the primitive three-cycle, the derivatives on the first two right steps are \(DR=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), while the final left-step derivative is \(DL=\left(\begin{smallmatrix}-a&1\\0&0\end{smallmatrix}\right)\). Consequently
\[
D(F_a^3)(p,0)=DL\,(DR)^2=
\begin{pmatrix}a&-1\\0&0\end{pmatrix},
\]
whose eigenvalues are \(a\) and zero. The only possible periodic orbits outside \(Q\) must survive the exact section classification without entering \(Q\) or diverging, so are exactly the listed primitive three-cycle. This completes the proof.

**Capture-time asymptotics.** The expressions for \(N_a(z)\) are explicit ceilings of logarithms (or a linear expression for \(a=1\)), and \(0\le\lceil t\rceil-t<1\) except at integers, where equality holds. Taking the indicated large-\(z\) or near-separatrix limits proves the three asymptotic statements. For the scaling limits, substitute \(a=1-\varepsilon\) or \(a=1+\varepsilon\) and \(z=s/\varepsilon\) into the exact logarithmic ceiling formulae. The elementary limits \(\log(1/(1-\varepsilon))/\varepsilon\to1\) and \(\log(1+\varepsilon)/\varepsilon\to1\), together with the ceiling error bounded by one, yield the stated functions. The critical \(a=1\) limit follows immediately from \(N_1(z)=\lceil z-1\rceil\). Finally \(a/(a-1)\to\infty\) as \(a\downarrow1\).

## Verification

The standalone script `verify.py` uses exact rational arithmetic to check 1,144 quarter-turn identities in the invariant square, 616 section returns, 12,496 finite exterior-to-axis/core tests, and 68 capture-count comparisons. It also checks exact primitive three-cycle and affine separator identities. The command is `python3 verify.py`, using only the Python standard library.

These finite tests are not substituted for the universal proof above. The capture-count script uses floating logarithms only to cross-check the explicitly derived ceiling formulas and allows a one-unit rounding discrepancy at exact threshold equalities; the symbolic return and orbit identities are checked exactly.

## Relationship to prior work

Simpson's 2026 study of one-dimensional first returns for the two-dimensional border-collision normal form treats the zero-left-determinant model with a **repelling** right focus, requiring \(\delta_R>1\) and \(\delta_R>\tau_R^2/4\) in Theorems 2.3 and 2.6. The neutral case \(\delta_R=1\) here is not a special case of those theorems. That study also identifies the line \(\delta_R=1\) as the limiting boundary of rational-rotation regions. The present result is a specific exact global analysis at its quarter-turn rational point, not a solution to the general rotation-region conjecture.

Simpson's earlier 2024 preprint (2025 journal version) concerns the broader zero-determinant normal form, but the full text could not be obtained for an exhaustive comparison. Its abstract describes bifurcation regions rather than this exact global absorbing-square/escape classification, so possible stronger or equivalent coverage remains a historical-priority risk. Prior studies of piecewise-affine invariant polygons and irrational neutral-focus return dynamics are related mechanisms, not asserted to be equivalent or ruled out categorically.

## Limitations

The exact statement is confined to the rational unit-determinant focus \((\tau_R,\delta_R)=(0,1)\) and the nonpositive left trace \(\tau_L=-a\). Its finite-time absorption is not robust under generic parameter perturbations. The formula describes capture of deterministic initial states, not a statistical distribution of transient lengths. The classification excludes claims about perturbed systems or the full multi-parameter family. Independent validation and definitive historical priority are outstanding.

## References

1. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901v1 (first public 2026-06-08), later *Qualitative Theory of Dynamical Systems* 25, article 160 (2026), doi:10.1007/s12346-026-01576-z. Full text at https://link.springer.com/article/10.1007/s12346-026-01576-z.
2. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1 (2024-08-08), later *SIAM Journal on Applied Dynamical Systems* 24 (2025), 2205–2245, doi:10.1137/24M1683548.
3. P. Glendinning, *Invariant measures for the n-dimensional border collision normal form*, *International Journal of Bifurcation and Chaos* (2014/2015), contextual related theory; no implication of the precise capture formula is claimed.
