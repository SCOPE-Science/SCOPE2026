# Rare-return coding and singular expansion scales in polygonal border-collision attractors

## Finding

Consider the countable family of two-dimensional polygonal border-collision attractors constructed by Glendinning and Wong (2010/2011). For every sufficiently large integer \(n\) to which their Theorem 2 applies, its explicit convex Markov partition has a **four-excursion renewal structure**: from cell \(M_2\) there are exactly two first-return paths of length \(n+1\) and exactly two of length \(n+2\). Consequently its *symbolic* periodic-path zeta function and entropy are
\[
\zeta^{\mathrm{sym}}_n(z)=\frac{1}{1-2z^{n+1}-2z^{n+2}},\qquad h^{\mathrm{sym}}_n=\log\lambda_n,
\]
where \(\lambda_n>1\) is the unique real solution of \(\lambda_n^{n+2}=2(\lambda_n+1)\). The entropy is strictly decreasing in \(n\), and, with \(m=n+2\),
\[
 h^{\mathrm{sym}}_n=\frac{\log4}{m}+\frac{\log4}{2m^2}+O(m^{-3}).
\]
For the canonical parameters in the same family, the two branch Jacobian determinants exhibit sharply different singular limits:
\[
 D_{R,n}-1=\frac{8\pi^2}{m^3}+O(m^{-5}),\qquad
 |D_{L,n}|=\frac{m^2}{4\pi^2}+O(1).
\]
Thus \(h_n^{\mathrm{sym}}/\log D_{R,n}\sim (\log4)m^2/(8\pi^2)\). Despite area expansion in both branches for sufficiently large \(n\), the natural itinerary complexity decays to zero at rate \(1/n\) while the right-branch area expansion vanishes cubically and the left-branch determinant diverges quadratically.

For the unique measure of maximal entropy on the Markov *symbolic shift*, each individual first-return path of length \(\ell\) has probability \(\lambda_n^{-\ell}\). The short-return probability is \(\lambda_n/(\lambda_n+1)\), the long-return probability is \(1/(\lambda_n+1)\), and the exact mean return time to \(M_2\) is \(n+1+1/(\lambda_n+1)\).

## Assumptions and scope

For real \(T_L,T_R,D_L,D_R\), let
\[
 F(x,y)=\begin{cases}(T_Lx+y+1,-D_Lx),&x\le0,\\(T_Rx+y+1,-D_Rx),&x\ge0.\end{cases}
\]
Set \(m=n+2\), \(\theta_n=2\pi/m\), and let \(r_n>1\) solve
\[
 2r_n^{n+1}\cos\theta_n-r_n^n-1=0.
\]
Set \(T_R=2r_n\cos\theta_n\), \(D_R=r_n^2\), \(E=1+r_n^2-2r_n\cos\theta_n\),
\[
 D_L=-r_n^{2-n}/E,\qquad T_L=(r_n^2-2r_n\cos\theta_n)/(Er_n^n).
\]
These are exactly the parameters in the primary construction. The statements concern sufficiently large \(n\), as in its rigorous theorem; the source's suggested cutoff \(n\ge6\) is numerical, not asserted here as an independently proved universal cutoff. The symbolic zeta counts periodic *itineraries*, not physical periodic points on partition boundaries, and \(h_n^{\mathrm{sym}}\) is the entropy of the finite-state Markov coding. No unproved identification with full dynamical topological entropy is made.

## Proof

**1. Parameter reduction.** The source defines \(q_n=r_n^{n+1}\sin(n\theta_n)/\sin\theta_n\). Since \(n\theta_n=2\pi-2\theta_n\), the defining root equation gives \(q_n=-2r_n^{n+1}\cos\theta_n=-(r_n^n+1)\). The source's parameter equations (28) therefore reduce to the displayed formulas for \(T_L,D_L\). Its equations (17), (25), (26), (28) and Theorem 2 supply the invariant polygon and convex Markov cells \(M_0,\ldots,M_{n+3}\), whenever \(n\) is sufficiently large. No numerical polygon construction is assumed.

**2. Four renewal paths.** The covering relations in the source's equation (29), with \(F(M_{k-1})=M_k\) for \(1\le k\le n\), are, in directed-graph notation,
\[
0\to1\to\cdots\to n;\quad n\to n+1,n+2;\quad n+1,n+2\to n+3,0;\quad n+3\to2.
\]
Starting at vertex \(2\), every nontrivial first return first passes through \(3,\ldots,n\), chooses either \(n+1\) or \(n+2\), and then chooses either the route through \(n+3\) or the route through \(0,1\). The four possibilities have lengths \(n+1,n+1,n+2,n+2\). Every directed cycle meets vertex \(2\), because deleting that vertex leaves an acyclic graph. Thus periodic symbolic paths are exactly cyclic concatenations of these four excursions.

**3. Zeta and entropy.** The first-return generating polynomial is \(B_n(z)=2z^{n+1}+2z^{n+2}\). Renewal decomposition, equivalently the finite matrix determinant lemma, gives \(\det(I-zA_n)=1-B_n(z)\). By \(\log\det(I-zA_n)=-\sum_{k\ge1}\mathrm{tr}(A_n^k)z^k/k\), the stated symbolic zeta follows. The Perron root solves \(\lambda^{n+2}-2\lambda-2=0\); it is unique above one because this polynomial is negative at one and strictly increasing for \(\lambda\ge1\). For fixed \(\lambda>1\), increasing \(n\) increases its left-hand side, proving strict decrease of \(\lambda_n\). The first-return measure maximizing entropy has independent excursion choices with probabilities \(\lambda_n^{-(n+1)}\) for either short route and \(\lambda_n^{-(n+2)}\) for either long route; they sum to one by the root equation. The displayed probabilities and return mean follow, and its entropy per original step equals \(\log\lambda_n\).

With \(h=\log\lambda_n\), the root equation becomes
\[
 (m-\tfrac12)h=\log4+\log\cosh(h/2).
\]
The bounds \(0<\log\cosh(h/2)<h/2\) imply
\[
 \frac{\log4}{m-1/2}<h<\frac{\log4}{m-1},
\]
so \(h=O(m^{-1})\). Taylor expansion of \(\log\cosh(h/2)=h^2/8+O(h^4)\) yields \(h=(\log4)/m+(\log4)/(2m^2)+O(m^{-3})\).

**4. Branch contrast.** Write \(r_n=1+\delta_n\) and \(\theta_n=2\pi/m\). For sufficiently large \(n\), the function \(g_n(r)=2r^{n+1}\cos\theta_n-r^n-1\) has \(g_n(1)=-(4\pi^2/m^2)+O(m^{-4})\), derivative \(g_n'(1)=m+O(m^{-1})\), and is strictly increasing on \([1,\infty)\). Comparing \(g_n\) at \(1\) and \(1+C/m^3\), for fixed \(C>4\pi^2\), first gives \(\delta_n=O(m^{-3})\). Taylor's theorem then refines this to \(\delta_n=4\pi^2/m^3+O(m^{-5})\). Hence \(D_R=r_n^2=1+8\pi^2/m^3+O(m^{-5})\). Finally,
\[
 E=(r_n-1)^2+2r_n(1-\cos\theta_n)=4\pi^2/m^2+O(m^{-4}),
\]
while \(r_n^{2-n}=1+O(m^{-2})\). Therefore \(|D_L|=r_n^{2-n}/E=m^2/(4\pi^2)+O(1)\). Comparing the displayed entropy and determinant expansions proves the ratio limit.

## Verification

The standalone `verify.py` reconstructs the exact transition matrix for multiple finite \(n\), checks both characteristic and zeta polynomials symbolically, and checks the large-\(n\) scaling numerically at increased precision. It is a reproducibility check, not a substitute for the all-\(n\) renewal and asymptotic proofs above. The exact symbolic calculation gives
\[
 \det(tI-A_n)=t^2(t^{n+2}-2t-2).
\]

## Relationship to prior work

Glendinning and Wong (2010/2011) construct the polygonal attractors, give the parameter equations and their Markov covering graph, and prove topological transitivity and dense periodic points for sufficiently large \(n\). Those constructions and claims are prior art. The new quantitative claim extracts an exact four-excursion renewal law, the symbolic zeta/maximum-entropy return distribution, and the *joint* large-index scales of coding entropy and right/left Jacobian determinants. Glendinning (2014) treats absolutely continuous invariant measures and open parameter sets, not these exact return and asymptotic formulas.

## Limitations

No physical-orbit Artin–Mazur zeta, total topological entropy of the planar map, or independent measure of maximal entropy for the planar dynamics is asserted. Symbolic itinerary multiplicities at partition boundaries can differ from physical periodic-point multiplicities. The theorem applies to the rigorously established sufficiently large indices and is not a proof of the numerical conjecture that \(n\ge6\) always suffices. The asymptotic estimates concern this special countable parameter sequence, not generic nearby maps.

## References

1. P. Glendinning and C. H. Wong, *Two dimensional attractors in the border collision normal form*, MIMS EPrint 2010.100, repository first deposited 2010-11-17, https://eprints.maths.manchester.ac.uk/1544/1/robust2d.pdf ; *Nonlinearity* **24** (2011), 995–1010, doi:10.1088/0951-7715/24/4/001.
2. P. Glendinning, *Invariant measures for the n-dimensional border collision normal form*, *International Journal of Bifurcation and Chaos* (2014); open manuscript https://eprints.maths.manchester.ac.uk/2252/1/glendinningijbcv2.pdf.
