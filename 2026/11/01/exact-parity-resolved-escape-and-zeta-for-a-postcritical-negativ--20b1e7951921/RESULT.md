# Exact parity-resolved escape and zeta for a postcritical negative-doubling hole

## Finding
Consider the negative-doubling interval map \(T(x)=1-2x\) for \(0\le x<1/2\) and \(T(x)=2-2x\) for \(1/2\le x\le1\), with open hole \(H=(5/12,7/12)\). Write \(S_n=\{x\in[0,1]:T^j(x)\notin H\text{ for }0\le j<n\}\), for integers \(n\ge1\), and \(K=\bigcap_{n\ge1}S_n\). Lebesgue measure is denoted \(\operatorname{Leb}\).

**Theorem.** For every integer \(k\ge0\),
\[
\operatorname{Leb}(S_{2k+1})=\frac76\,2^{-k}-\frac13\,4^{-k}.
\]
For every integer \(k\ge1\),
\[
\operatorname{Leb}(S_{2k})=\frac53\,2^{-k}-\frac23\,4^{-k}.
\]
Thus the exact Lebesgue escape exponent is \(\frac12\log2\). The invariant compact survivor \(K\) has topological entropy \(\frac12\log2\) and Hausdorff dimension \(1/2\). Its periodic-point counts are
\[
\#\operatorname{Fix}(T^{2k+1}|_K)=2\quad(k\ge0),\qquad
\#\operatorname{Fix}(T^{2k}|_K)=2^{k+1}\quad(k\ge1),
\]
and the Artin–Mazur zeta function is
\[
\zeta_K(z)=\exp\!\left(\sum_{n\ge1}\frac{\#\operatorname{Fix}(T^n|_K)}n z^n\right)
=\frac{1+z}{(1-z)(1-2z^2)}.
\]
These exact escape and periodic-orbit data coexist with two conjugate full two-shifts for \(T^2\), whose interval realizations meet at two fixed points.

## Assumptions and scope
The map is defined on the closed unit interval, the hole is *open*, and points on the hole boundary are retained until they subsequently enter the hole. The unique jump value at \(x=1/2\) is irrelevant because that point lies inside the hole. All finite-time sets include the initial time \(j=0\). A periodic point is counted as a distinct physical point, not as a Markov boundary itinerary. Full shift means the one-sided two-symbol shift (the map is noninvertible).

## Proof
**1. Exact Markov structure.** Partition the retained region, using closed intervals with disjoint interiors, in this order:
\[
I_0=[0,1/6],\quad I_1=[1/6,1/3],\quad I_2=[1/3,5/12],\quad I_3=[7/12,2/3],\quad I_4=[2/3,5/6],\quad I_5=[5/6,1].
\]
The hole boundaries are preperiodic: \(5/12\mapsto1/6\mapsto2/3\mapsto2/3\) and \(7/12\mapsto5/6\mapsto1/3\mapsto1/3\). On the interiors of these six intervals, \(T\) has derivative \(-2\) and images consist of whole members of the partition, perhaps together with the hole. Direct evaluation at the interval endpoints gives the adjacency matrix \(A\), where \(A_{ij}=1\) exactly if \(I_j\) is contained in \(T(I_i)\) up to endpoints:
\[
A=\begin{pmatrix}
0&0&0&0&1&1\\
0&0&1&1&0&0\\
0&1&0&0&0&0\\
0&0&0&0&1&0\\
0&0&1&1&0&0\\
1&1&0&0&0&0
\end{pmatrix}.
\]
The interval-length vector is \(\ell=(1/6,1/6,1/12,1/12,1/6,1/6)^{\mathsf T}\). Because every inverse branch contracts by exactly \(1/2\), \(\operatorname{Leb}(S_n)=\ell^{\mathsf T}(A^{\mathsf T}/2)^{n-1}\mathbf1\). Multiple closed-interval representations occur only on finitely many endpoints and do not affect Lebesgue measure.

**2. Escape formulas.** Exact inversion of the six-by-six matrix gives the power series identity
\[
\begin{aligned}
\sum_{n\ge1}\operatorname{Leb}(S_n)z^{n-1}
&=\ell^{\mathsf T}(I-zA^{\mathsf T}/2)^{-1}\mathbf1\\
&=\frac{7/6+(5/6)z}{1-z^2/2}
-\frac{1/3+(1/6)z}{1-z^2/4}.
\end{aligned}
\]
Coefficient extraction gives both asserted identities with their stated quantifiers. The leading surviving mass on even and odd subsequences is a positive constant times \(2^{-n/2}\), proving the escape exponent.

**3. Entropy and dimension.** Direct characteristic-polynomial calculation gives
\[
\det(\lambda I-A)=\lambda^2(\lambda-1)(\lambda+1)(\lambda^2-2).
\]
Thus the largest spectral radius is \(\sqrt2\). Finite-state expanding-branch coding shows \(h_{\mathrm{top}}(T|_K)=\log\sqrt2\): overlapping symbolic descriptions are restricted to finitely many endpoints and their inverse images, and do not change the exponential word growth. Since every surviving inverse branch has contraction ratio \(1/2\), the finite graph-directed system has dimension \(\log\sqrt2/\log2=1/2\). For a direct dimension lower bound, let \(C_A=K\cap(I_1\cup I_4)\) and \(C_B=K\cap(I_2\cup I_3)\). On each of these compact sets, \(T^2\) is topologically conjugate to a one-sided full two-symbol shift: its two inverse branches are disjoint in the indicated pair of intervals and have contraction ratio \(1/4\). Thus each core has Hausdorff dimension \(\log2/\log4=1/2\); the other states consist of transient entry branches and endpoints, so they cannot increase the dimension.

**4. Physical periodic points and zeta.** Algebraic trace of the transition matrix gives \(\operatorname{tr}(A^{2k+1})=0\) for all \(k\ge0\) and \(\operatorname{tr}(A^{2k})=2+2^{k+1}\) for \(k\ge1\). This trace counts cyclic Markov itineraries, not necessarily physical periodic points. The two fixed points \(1/3\) and \(2/3\) lie on partition boundaries and each has two alternating symbolic itineraries of least period two. Therefore both are *omitted* by the odd-length matrix traces but *counted twice* by the even-length traces. No other recurrent boundary point occurs: \(0\leftrightarrow1\), and all remaining partition endpoints land eventually on one of these periodic orbits. Correcting the trace gives \(p_{2k+1}=2\), \(p_{2k}=2^{k+1}\). Inserting these values into \(\exp(\sum p_nz^n/n)\), using the formal series of \(-\log(1-z)\), proves \(\zeta_K(z)=(1+z)/((1-z)(1-2z^2))\).

## Verification
The accompanying `check.py` recomputes the interval images and transfer matrix, its characteristic polynomial, the rational mass generating function, all finite-time survival formulas through step 20, and exact real periodic-point counts through period 12 from rational branch equations. All arithmetic relevant to counts is rational; neither floating-point orbits nor a finite experiment replaces the general proof above. Run `python check.py` in a Python environment with SymPy available.

## Relationship to prior work
Ding, Steiner and Sun (2026, arXiv:2610.03327) establish general survivor languages, plateaux, entropy and dimension staircases for topologically expansive decreasing Lorenz maps and the negative-doubling model. Their general results supply the setting, rather than an evaluated rational survival generating function or periodic-point correction at this specific hole. A previously published exact trichotomy of symmetric negative-doubling holes covers \(0<a\le2/5\); the present parameter is \(a=5/12>2/5\), beyond that theorem's range. Glendinning and Hege (2025/2026) identify boundaries of positive dimension and entropy in related decreasing-branch dynamics; the claim here is an *inside-the-positive-entropy-region* exact finite-time escape and zeta computation. Standard Markov transfer techniques and graph-directed dimension methods are classical and not claimed as new.

## Limitations
The formulas concern the single explicitly stated symmetric hole, not a parameter interval or an optimal threshold. The periodic-point zeta depends on retaining the open-hole boundary; closing the hole would remove some periodic boundary orbits. The entropy is for the compact survivor; the escape exponent is for Lebesgue mass. Historical novelty is a best-knowledge conclusion after relevant searches, not independently certified; a generalized pre-existing transfer calculation could subsume the evaluated result.

## References
- Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327, initially public 2 October 2026, https://arxiv.org/abs/2610.03327.
- P. Glendinning, C. Hege, *The boundary of chaos for piecewise smooth maps and the boundary of positive Hausdorff dimension for survivor sets of open maps*, arXiv:2508.21429, initially public 29 August 2025, https://arxiv.org/abs/2508.21429; Nonlinearity 39 (2026), article 075022.
- P. Glendinning, N. Sidorov, *The doubling map with asymmetrical holes*, arXiv:1302.2486, https://arxiv.org/abs/1302.2486.
