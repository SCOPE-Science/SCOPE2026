# Askey-pair interlacing breakdown bracket for quasi-orthogonal Jacobi degree 6 at alpha = 0

## Context
Askey conjectured that the zeros of $P_n^{(\\alpha,\\beta)}$ and $P_n^{(\\alpha,\\beta+2)}$ interlace. Driver–Jordaan (SIGMA 12:042, arXiv:1510.08599) study this in the quasi-orthogonal window $\\alpha>-1$, $-2<\\beta<-1$, proving a necessary and sufficient condition (Thm 3.1) but publishing numerics only at $n=5$, $\\alpha=2.35$. Classical interlacing theorems (Szegő Thm 3.3.2, DLMF 18.2(vi)/18.16) require $\\alpha,\\beta>-1$ and do not apply here.

## Definitions
Fix $n=6$, $\\alpha=0$, $\\beta\\in\\{-19/10,-17/10,-3/2,-13/10,-11/10\\}$.
Askey pair: $X_\\beta=P_6^{(0,\\beta)}$ (order-1 quasi-orthogonal), $Y_\\beta=P_6^{(0,\\beta+2)}$ (classical).
$P_n^{(a,b)}$ is the Jacobi polynomial (at $a=0$ the DLMF 18.5.7 prefactors equal 1):
$P_n^{(a,b)}(x)=\\sum_{k=0}^n (-n)_k(n+a+b+1)_k/(k!\\,k!)\\,((1-x)/2)^k$.
Order zeros $x_1<\\dots<x_6$, $y_1<\\dots<y_6$. HOLD means $x_1<y_1<\\dots<x_6<y_6$.
BREAK means otherwise, witnessed here by a closed interval $J$ with exactly two zeros of one member and zero of the other.

## Result
At $(n,\\alpha)=(6,0)$:
- $\\beta=-19/10$: BREAK; $J=[-2043/2000,-1921/2000]$ holds exactly two $X$ zeros, zero $Y$ zeros.
- $\\beta=-17/10$: BREAK; $J=[-2051/2000,-919/1000]$ holds exactly two $X$ zeros, zero $Y$ zeros.
- $\\beta=-3/2$: HOLD ($x_1<y_1<\\dots<x_6<y_6$).
- $\\beta=-13/10$: HOLD.
- $\\beta=-11/10$: HOLD.
Hence the adjacent pair $(-17/10$ BREAK, $-3/2$ HOLD$)$ brackets the quasi-orthogonal Askey-breakdown transition at $(6,0)$.
At every grid $\\beta$, $X_\\beta$ has exactly one zero below $-1$ (first bracket straddles $-1$); all other enclosed zeros lie in $(-1,1)$. No global threshold or monotonicity is claimed.

## Proof / evidence
Machine-checked exact-rational certificate (`output/artifacts/verify.py`, stdlib `Fraction` only, prints `VERIFY_OK`):
- Rebuilds each $X_\\beta,Y_\\beta$ from the defining sum; leading coefficients nonzero (genuine degree 6); $P(1)=1$ and $P(-1)=(-1)^6(b+1)_6/6!$ verified.
- 60 rational brackets (width $1/2000$ or $1/1000$): opposite nonzero endpoint signs (IVT gives ≥1 zero) plus Sturm variation drop $V(lo)-V(hi)=1$ (exactly one simple zero); each Sturm chain has degrees $6,5,4,3,2,1,0$ and total $V(-\\infty)-V(+\\infty)=6$, so the six brackets are complete and all zeros real; brackets verified disjoint and ordered.
- HOLD: strict rational chain $x_{1,lo}<x_{1,hi}<y_{1,lo}<\\dots<x_{6,hi}<y_{6,lo}$ implies $x_i<y_i<x_{i+1}$.
- BREAK: $y_{1,lo}>x_{2,hi}$ ($-37/40>-1921/2000$; $-1819/2000>-919/1000$); $Y$ nonzero at $J$ endpoints with Sturm $Y$-count $0$ on $J$ and $X$-count $2$; any alternation in either order would force a $Y$ zero strictly between the two consecutive $X$ zeros, hence inside $J$ — contradiction.
- Sub-$(-1)$: $X_{1,hi}<-1<X_{2,lo}$ at all five $\\beta$.
Floating-point root approximations were motivation only and carry no proving force.

## Limitations
Finite five-point table at fixed $(n,\\alpha)=(6,0)$ only; continuous threshold location inside $(-1.7,-1.5)$ and any monotonicity not claimed. Uses definitional-sum construction rather than mixed-recurrence route (equally rigorous). Does not reprove the Driver–Jordaan criterion; supplies new certified witnesses.

## Reproducibility
Run `python3 output/artifacts/verify.py` (Python 3 stdlib only). Expected: `VERIFY_OK` plus totals and delta values $\\delta=-1-2(\\beta+1)/(\\beta+14)$.

## References
- K. Driver, K. Jordaan, Zeros of Quasi-Orthogonal Jacobi Polynomials, SIGMA 12 (2016) 042, arXiv:1510.08599. Thm 3.1 ($\\delta<x_{2,n}$ criterion), Remark 3.2 ($n=5$ numerics), Sec 5 (bounds on $x_{1,n}$).
- DLMF §18.16, §18.2(vi); Szegő, Orthogonal Polynomials, Thm 3.3.2 (classical regime $\\alpha,\\beta>-1$).
