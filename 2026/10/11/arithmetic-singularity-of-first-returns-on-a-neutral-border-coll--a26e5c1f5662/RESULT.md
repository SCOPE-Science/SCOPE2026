# Arithmetic singularity of first returns on a neutral border-collision ellipse

## Finding
Fix real \(\ell\), \(-2<\tau<2\), and let the continuous border-collision map be
\[
F(x,y)=\begin{cases}(\ell x+y+1,0),&x\le0,\\(\tau x+y+1,-x),&x>0.\end{cases}
\]
The first return of \((x,0)\) to the horizontal section is \(N(x)=\inf\{n\ge1:(F^n(x,0))_2=0\}\), with value \(\infty\) for nonreturn. Put \(\phi=\arccos(\tau/2)\in(0,\pi)\), \(\alpha=\phi/(2\pi)\in(0,1/2)\), and \(x_*=1/2\).

**Theorem (neutral-border first-return dichotomy and sharp arithmetic singularity).** If \(\alpha=p/q\) is rational in lowest terms, every real \(x\) returns within \(q\) steps, and \(N(x_*)=q\). If \(\alpha\) is irrational, \(x_*\) is the unique real nonreturning section point, \(N(x)\to\infty\) as \(x\to x_*\) through other points, and every other point returns. More precisely, for \(e=x-x_*\ne0\) write
\[
\varepsilon(e)=\frac1\pi\arctan\!\left(2|e|\tan\frac\phi2\right).
\]
For irrational \(\alpha\), \(N(x_*+e)\) is the smallest integer \(k\ge1\) for which \(\{k\alpha\}\in[1-\varepsilon(e),1)\) if \(e>0\), or \(\{k\alpha\}\in(0,\varepsilon(e)]\) if \(e<0\). In particular,
\[
\alpha\text{ has bounded continued-fraction partial quotients}\quad\Longleftrightarrow\quad
\exists c,C,r>0\ \forall\,0<|e|<r:\ \frac{c}{|e|}\le N(x_*+e)\le\frac{C}{|e|}.
\]
If \(\alpha\) has unbounded partial quotients then \(\liminf_{e\to0,e\ne0}|e|N(x_*+e)=0\). For bounded type, the Lebesgue tail on the natural finite section \([0,1]\) satisfies \(\operatorname{Leb}\{x\in[0,1]:N(x)>n\}=\Theta(1/n)\), and \(\int_0^1N(x)\,dx=\infty\).

## Assumptions and scope
The right branch has trace \(\tau\) and determinant exactly one (neutral elliptic regime); the left branch has determinant zero and arbitrary real trace \(\ell\). The section is the entire real axis with second coordinate zero, and return is counted only after at least one iterate, including equality with the switching line. All results are uniform in \(\ell\) because return timing is determined by right-branch motion up to the first switching hit. The ellipse itself was already described by Sushko and Gardini (2008), and is recalled as geometric context, not proposed as a new invariant.

## Proof
Write \(R(x,y)=(\tau x+y+1,-x)\), \(r=(2-\tau)^{-1}\), and \(c=\cos\phi=\tau/2\). The fixed point of \(R\) is \((r,-r)\), and its linear part has characteristic polynomial \(z^2-\tau z+1\), giving a real-linear conjugacy to rigid rotation through angle \(\phi\) (orientation sign depends on coordinates). The positive-definite quadratic form on centered coordinates \((u,v)=(x-r,y+r)\) is \(u^2+\tau uv+v^2\). In particular, the previously known level ellipse
\[
E_\tau=\{(x,y):x^2+\tau xy+y^2-x+y+1/4=0\}
\]
is invariant. Its horizontal-section intersection is exactly \((x-1/2)^2=0\); its vertical switching-line intersection is \((y+1/2)^2=0\). Positive definiteness and the centered value show \(E_\tau\subseteq\{x\ge0\}\), so \(F|_{E_\tau}=R|_{E_\tau}\) despite the switch; the tangency orbit does not enter the left half-plane.

For an arbitrary initial section coordinate \(x=x_*+e\), let \(X_n\) be the first coordinate of \(R^n(x,0)\). Solve the linear recurrence (or diagonalize \(DR\)) to obtain the exact identity for each integer \(n\ge0\):
\[
X_n=r\big(1-\cos((n+1)\phi)\big)
   +\frac{e\sin((n+1)\phi)}{\sin\phi}.
\tag{1}
\]
Before first return, \(F\) follows \(R\) and has strictly negative second coordinate after every right iterate. Consequently, the first return time is exactly \(N(x)=\min\{k\ge1:X_{k-1}\le0\}\), with the usual infinite convention. For \(e=0\), (1) is nonnegative and vanishes exactly when \(k\alpha\in\mathbb Z\). Thus the distinguished point has return time \(q\) if \(\alpha=p/q\) and never returns if \(\alpha\) is irrational. In the rational case, \(X_{q-1}=0\) for every initial \(x\), proving the universal \(q\)-step bound.

Now assume \(\alpha\) irrational and \(e\ne0\). Put \(\theta=2\pi\{(n+1)\alpha\}\). The identity
\[
X_n=2\sin(\theta/2)\left[r\sin(\theta/2)+\frac{e}{\sin\phi}\cos(\theta/2)\right]
\]
shows (with the equality endpoints included) that \(X_n\le0\) precisely on the one-sided circular interval adjacent to \(0\): for \(e>0\) the arc is \([2\pi(1-\varepsilon(e)),2\pi)\), and for \(e<0\) it is \((0,2\pi\varepsilon(e)]\). This follows since \(\sin\phi>0\) and \(r\sin\phi=[2\tan(\phi/2)]^{-1}\). Density of the irrational rotation guarantees hitting either positive-width arc; continuity in \(e\) for any fixed number of right iterates guarantees \(N(x_*+e)\to\infty\) as \(e\to0\).

It remains to make the arithmetic estimate sharp. Locally, \(\varepsilon(e)\sim(2/\pi)\tan(\phi/2)|e|\). If \(\alpha\) is badly approximable, there is \(\kappa>0\) such that \(\|k\alpha\|\ge\kappa/k\) for all integers \(k\ge1\), establishing the lower bound. For the upper bound, let \(q_j\) be a convergent denominator with \(q_j>2/\varepsilon(e)\) minimal; when all partial quotients are at most \(M\), \(q_j\le (M+1)q_{j-1}\le 2(M+1)/\varepsilon(e)\) up to initial constants. The coprime residues of \(kp_j\pmod{q_j}\) supply, among \(1\le k<q_j\), both residues \(1\) and \(-1\); because \(|k\alpha-kp_j/q_j|<1/q_j\), their irrational fractional parts stay respectively in \((0,2/q_j)\) and \((1-2/q_j,1)\). Hence either one-sided target arc is hit by time \(q_j\), proving the upper bound.

Conversely, if \(\alpha\) is not badly approximable, take positive integers \(k_j\) with \(k_j\|k_j\alpha\|\to0\). Choose \(e_j\) on the side corresponding to the nearer end of the circle, with \(\varepsilon(e_j)=\|k_j\alpha\|\). Then \(N(x_*+e_j)\le k_j\) by the exact arc test and \(|e_j|=O(\|k_j\alpha\|)\), so \(|e_j|N(x_*+e_j)\to0\). This precludes a uniform inverse-distance lower bound.

Finally, bounded-type inverse-distance bounds on a small neighborhood of \(x_*\) imply lower and upper \(1/n\) estimates for the measure of \(N>n\). Away from that neighborhood, the target arcs have widths bounded below, and the dense irrational rotation hits both target arcs in a fixed number of steps uniformly; hence there are no additional long-return contributions. The layer-cake identity for positive-integer-valued \(N\) gives \(\int_0^1 N\,dx=\sum_{n\ge0}\operatorname{Leb}\{N>n\}=\infty\).

## Verification
Run the accompanying standalone Python 3 program \(\texttt{check\_neutral\_return.py}\): it performs 309 finite diagnostics. It checks rational traces \(-1,0,1\) and their exact finite return bounds; the invariant ellipse with rational arithmetic; representative irrational rotations with \(\tau=1/2\); and exact finite section returns against the derived angular arc test for several left traces. This numerical/exact finite checker is a diagnostic only; the irrational and infinitely many return-time claims follow from the proof above. The program uses only Python's standard library and requires no downloaded data.

## Relationship to prior work
Sushko and Gardini (2008), Section 3, equations (8)–(12) and Proposition 1, already derived the invariant switching-tangent ellipse and its periodic-versus-quasiperiodic center dynamics; those facts are explicitly prior, not new here. Simpson (2026), Theorems 2.3 and 2.6, analyzes the zero-left-determinant return map in the **repelling** right-focus region \(\\\(\\delta_R>1\\)\), obtaining finite return-time structure via Farey parents. Its stated hypotheses do not include the neutral boundary \(\\\(\\delta_R=1\\)\). This result treats the missing boundary and gives a unique nonreturning section point, an exact one-sided circle-hitting code, a bounded-type characterization, and a sharp return-time tail. Simpson (2025) surveys broader bifurcation behavior, but an accessible full-text comparison of that paper was unavailable; priority risk remains. Classical continued-fraction rotation estimates are used rather than claimed as new.

## Limitations
The conclusions are confined to \(\delta_L=0\), \(\\\(\\delta_R=1\\)\), \(\mu=1\), and \(-2<\tau_R<2\); they do not classify attracting sets, all return distributions for irrational rotations of unbounded type, or the behavior away from the neutral parameter surface. The order \(\Theta(n^{-1})\) is asserted only for bounded-type rotations and Lebesgue initial sections in \([0,1]\). A priority search cannot exclude every unindexed equivalent argument; the Simpson (2025) full text was not obtained. No independent scientific audit is claimed.

## References
1. D. J. W. Simpson, *One-Dimensional First Return Maps for the Two-Dimensional Border-Collision Normal Form with a Zero Determinant*, first public arXiv version 8 June 2026, arXiv:2606.08901; *Qualitative Theory of Dynamical Systems* 25, 160 (2026), DOI:10.1007/s12346-026-01576-z. Read full open-access text, especially Theorems 2.3, 2.6 and parameter assumptions.
2. I. Sushko and L. Gardini, *Center Bifurcation for Two-Dimensional Border-Collision Normal Form*, *International Journal of Bifurcation and Chaos* 18 (2008), DOI:10.1142/S0218127408020823. Read open author-hosted full PDF, Section 3, equations (8)–(12), Proposition 1.
3. D. J. W. Simpson, *The Two-Dimensional Border-Collision Normal Form with a Zero Determinant*, *SIAM Journal on Applied Dynamical Systems* (2025), DOI:10.1137/24M1683548. Abstract and bibliographic material consulted; full text inaccessible in this review.
4. Standard continued-fraction results: recurrence of irrational circle rotations, best rational approximants, and equivalence of badly approximable numbers with bounded partial quotients.
