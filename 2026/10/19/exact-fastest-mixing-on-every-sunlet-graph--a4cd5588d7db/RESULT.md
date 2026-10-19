# Exact fastest mixing on every sunlet graph

## Finding
For each integer \(n\ge 3\), form the *sunlet* \(S_n=C_n\odot K_1\): attach one pendant vertex \(u_j\) to each rim vertex \(v_j\) of an \(n\)-cycle (indices modulo \(n\)). Among **all** symmetric, entrywise-nonnegative, row-stochastic transition matrices \(P\) whose off-diagonal support is contained in the edges of \(S_n\), the minimum second-largest eigenvalue modulus is
\[
\boxed{\mu_n^*=\frac{2(1+x_n)}{x_n^2+2x_n+2},\qquad x_n=\sqrt{1-\cos(2\pi/n)}=\sqrt2\sin(\pi/n).}
\]
It is attained by assigning the same probability \(p_n\) to every pendant edge (in either direction) and the same probability \(q_n\) to every rim edge (in either direction), where
\[
\boxed{p_n=\frac{x_n(x_n+1)}{x_n^2+2x_n+2},\qquad
q_n=\frac{x_n+2}{2(x_n^2+2x_n+2)}.}
\]
The holding probability is \(1-p_n\) at each pendant and **zero** at each rim vertex. This pair of orbit probabilities is the **unique optimizer among dihedrally invariant** chains. No assertion of uniqueness among arbitrary nonsymmetric chains is made. The exact optimal absolute spectral gap is
\[
1-\mu_n^*=\frac{x_n^2}{x_n^2+2x_n+2}\sim\frac{\pi^2}{n^2}\quad(n\to\infty).
\]
In contrast, the optimal absolute spectral gap on the bare \(n\)-cycle is asymptotic to \(2\pi^2/n^2\) [2]. Thus attaching one leaf to every site halves the leading optimal spectral gap.

## Assumptions and scope
The state space is the \(2n\) vertices \(\{v_0,\ldots,v_{n-1},u_0,\ldots,u_{n-1}\}\), with allowed edges \(v_jv_{j+1}\) and \(v_ju_j\), along with self-loops. Every allowed transition probability may be set to zero. Require \(P=P^\mathsf T\), \(P\mathbf1=\mathbf1\), and entrywise \(P\ge0\). Set \(J=(2n)^{-1}\mathbf1\mathbf1^\mathsf T\); define \(\mu(P)=\lVert P-J\rVert_2\). This convention correctly gives \(\mu(P)=1\) for disconnected/reducible symmetric chains. Here \(n\ge3\), so the rim is a simple cycle; no assertion concerns asymmetric, nonreversible, differently stationed, or genuinely time-inhomogeneous transitions. The claim optimizes the SLEM, not the nonasymptotic total-variation mixing time at an arbitrary cutoff.

## Proof
**1. Global symmetry reduction.** Every dihedral symmetry of the rim permutes the pendants in tandem. For each feasible \(P\), average its conjugates over this finite group. The average \(\overline P\) remains symmetric, stochastic, nonnegative, and supported on the graph. Since \(P\mapsto\lVert P-J\rVert_2\) is convex and invariant under such conjugation, \(\mu(\overline P)\le\mu(P)\). Hence a global optimum has two orbit probabilities \(p\ge0\) (pendants) and \(q\ge0\) (rim), with exactly
\[
0\le p\le1,\qquad 0\le q\le(1-p)/2.
\]
Their pendant and rim holding probabilities are \(1-p\) and \(1-p-2q\), respectively. This reduction proves that optimizing the two-orbit family gives the global optimum value, but does not imply that every global optimizer is invariant.

**2. Spectrum.** Fourier transform simultaneously in the \(n\) rim and pendant coordinates. At frequency \(k\in\{0,\ldots,n-1\}\), with \(t_k=1-\cos(2\pi k/n)\), the transformed matrix is the real symmetric block
\[
B_k=\begin{pmatrix}1-p&p\\p&1-p-2qt_k\end{pmatrix},
\quad \lambda_k^{\pm}=1-p-qt_k\pm\sqrt{p^2+q^2t_k^2}.
\]
The zero-frequency eigenvalues are \(1\) and \(1-2p\). Put \(t=t_1=1-\cos(2\pi/n)\), so \(0<t\le3/2\); define \(x=\sqrt t\), \(a=t/2=x^2/2\). For every feasible pair, \(\mu(P)\ge\lambda_1^+\). If \(p>0\), its derivative with respect to \(q\) is strictly negative:
\[
\frac{\partial \lambda_1^+}{\partial q}=-t+\frac{q t^2}{\sqrt{p^2+q^2t^2}}<0.
\]
For \(p=0\), \(\lambda_1^+=1\). Hence, for every feasible pair,
\[
\mu(P)\ge \phi(p):=(1-a)(1-p)+\sqrt{p^2+a^2(1-p)^2},
\]
with equality in the intermediate bound only when \(q=(1-p)/2\), except at the irrelevant boundary \(p=0\).

**3. Solve a strictly convex scalar problem.** The Euclidean norm of the affine vector \((p,a(1-p))\) is strictly convex as a function of \(p\in[0,1]\) because \(a>0\) and these vectors never lie on one ray as \(p\) varies. Thus \(\phi\) is strictly convex. Its one-sided endpoint derivatives are \(\phi'(0)=-1\) and \(\phi'(1)=a>0\), giving one interior minimizer. Write \(d=x^2+2x+2\) and propose
\[
p_* =\frac{x(x+1)}d,\qquad q_* =\frac{x+2}{2d}=\frac{1-p_*}{2}.
\]
Direct expansion gives
\[
p_*^2+q_*^2x^4=x^2/4,\qquad
p_*-a^2(1-p_*)=(1-a)x/2.
\]
These are precisely the square-root identity and the unsquared stationarity equation \(\phi'(p_*)=0\). Thus the unique minimizer is \(p_*\), and
\[
\min_{0\le p\le1}\phi(p)=\phi(p_*)=(1-a)(1-p_*)+x/2=\frac{2(1+x)}d=:\mu_*.
\]
This is a global lower bound for *every* feasible chain, including the nonsymmetric ones by Step 1.

**4. Attainment: no hidden negative eigenvalue.** At \((p_*,q_*)\), \(\lambda_k^+\) decreases as \(t_k\) increases, because its derivative is \(-q_*+q_*^2t_k/\sqrt{p_*^2+q_*^2t_k^2}<0\). All nonzero frequencies have \(t_k\ge t\), so \(\lambda_k^+\le\lambda_1^+=\mu_*\). The minus eigenvalues also decrease with \(t_k\). Since \(t_k\le2\),
\[
\lambda_k^-\ge\lambda^-(2)=1-p_*-2q_*-\sqrt{p_*^2+4q_*^2}=-\sqrt{p_*^2+(1-p_*)^2}.
\]
The exact identity
\[
\mu_*^2-\big(p_*^2+(1-p_*)^2\big)=\frac{x(x+2)(2-x^2)}{d^2}>0
\]
holds because \(0<x^2\le3/2<2\); hence every minus eigenvalue is greater than \(-\mu_*\). Finally \(1-2p_*=(2-x^2)/d\) is positive and \(\mu_*-(1-2p_*)=x(x+2)/d>0\). Thus \(\mu(P_*)=\mu_*\), completing global optimality. Equality in Steps 2–3 forces \(p=p_*\) and \(q=q_*\) within the invariant two-parameter family, proving the stated uniqueness only in that family.

**5. Asymptotics.** From \(x=\sqrt2\sin(\pi/n)\), \(x\sim\sqrt2\pi/n\). Consequently \(p_*\sim\pi/(\sqrt2 n)\), \(q_*=1/2-p_*/2\to1/2\), and \(1-\mu_*=x^2/d\sim\pi^2/n^2\). Boyd et al. [2] give cycle gap \(2\pi^2/n^2\); taking the ratio yields \(1/2\).

## Verification
The accompanying standalone `check_sunlet.py` independently constructs the full \(2n\)-state symmetric stochastic matrix and compares its nontrivial numerical eigenvalue moduli to the formula for \(n=3,\ldots,30\) and \(n=32,40,48,64,90\). It additionally tests randomly selected two-orbit competitors and checks the crucial rational algebraic identities *symbolically* in an indeterminate \(x\). Run from the directory containing both files using `OPENBLAS_NUM_THREADS=1 python check_sunlet.py`; dependencies are Python 3, NumPy and SymPy. In the present reproduction the program reported 233 independently constructed full-matrix spectra and 4950 competitor checks passing. These finite experiments are supplementary; Steps 1–5 constitute the proof for all integers \(n\ge3\).

## Relationship to prior work
Boyd, Diaconis and Xiao [1] introduce the general symmetric fastest-mixing Markov chain convex program. Boyd, Diaconis, Parrilo and Xiao [2] establish symmetry reduction and compute exact optima for cycles and wheels (their sections 3.1.1 and 5.4.3). A wheel is a cycle plus *one universal hub*, not the sunlet's \(n\) separate leaves. Neither its Fourier blocks nor its optimized parameters imply the displayed all-\(n\) sunlet law. Later geometric FMMC bounds [3] address optimal *orders* and conductance, not exact SLEM or orbit-probability formulas. Standard definitions of the sunlet \(C_n\odot K_1\) appear in [4]. The new content is the exact sunlet extremal law, its global optimality, orbitwise uniqueness, saturated-rim property and factor-two asymptotic comparison—not the generic convexity or Fourier decomposition principles.

## Limitations
The result does not enumerate possible additional nonsymmetric optimal chains. It does not optimize cutoff-dependent total-variation distance, directed/nonreversible walks or nonuniform stationary measures. The originality comparison covers accessible FMMC and graph-specific work but cannot exclude every unindexed mathematical equivalence. The theorem does not assert algorithmic advantages over numerical SDP solutions at a fixed graph size.

## References
[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689. DOI `10.1137/S0036144503423264`. Lawful full text: `https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf`.

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:`0709.0955` (first submitted 2007-09-06), SIAM Journal on Optimization **20** (2009), 792–819. Preprint `https://arxiv.org/pdf/0709.0955`.

[3] S. Olesker-Taylor, L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, arXiv:`2111.05816` (2021), Probability Theory and Related Fields **188** (2024), 1017–1062. `https://arxiv.org/abs/2111.05816`.

[4] E. W. Weisstein, *Sunlet Graph*, MathWorld, `https://mathworld.wolfram.com/SunletGraph.html` (graph terminology only).
