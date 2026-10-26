# Sharp positivity recovery and transient amplification on unbalanced complete bipartite graphs

## Finding
Let \(2\le a\le b\) be integers, let \(N=a+b\), and let \(L\) be the **unnormalized** combinatorial Laplacian of the simple complete bipartite graph \(K_{a,b}\). On real coordinatewise ordered vertex data, set \(T(t)=\exp(-tL^2)\), for \(t\ge0\). Write \([z]_+=\max\{z,0\}\).

Define
\[
H_A(t)=a+b e^{-N^2t}-N e^{-b^2t},\qquad
H_B(t)=b+a e^{-N^2t}-N e^{-a^2t}.
\]
Each has exactly one strictly positive zero, denoted \(\tau_A\), respectively \(\tau_B\). These cutoffs are ordered:
\[
0<\tau_A\le\tau_B,\quad\text{with strict inequality if }a<b.
\]
Between time zero and \(\tau_A\), precisely the off-diagonal matrix entries within either part are negative. Between \(\tau_A\) and \(\tau_B\), precisely those within the larger part are negative. At \(\tau_B\) all entries are nonnegative; every entry is strictly positive at every later time. Thus
\[
T(t)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad t=0\text{ or }t\ge\tau_B.
\]

For **every** \(t\ge0\), the exact sharp coordinatewise operator norm is determined solely by rows indexed by the larger vertex part:
\[
\boxed{\ \|T(t)\|_{\ell^\infty\to\ell^\infty}
=1+\frac{2(b-1)}{bN}\left[N e^{-a^2t}-b-ae^{-N^2t}\right]_+.\ }
\]
If \(a<b\), rows from the larger part strictly dominate the other rows whenever the norm exceeds one; when \(a=b\), they tie. The function of time has a **unique** strict peak at
\[
\theta_B=\frac{\log(N/a)}{N^2-a^2}
=\frac{\log(1+b/a)}{b(b+2a)}.
\]
Its sharp value, attained by a sign vector in \(\ell^\infty\), is
\[
\boxed{\ \max_{t\ge0}\|T(t)\|_{\infty\to\infty}
=1+\frac{2(b-1)}{N}
\left[\frac{b+2a}{N}
\left(\frac aN\right)^{a^2/[b(b+2a)]}-1\right].\ }
\]

Fix \(a\ge2\) and let \(b\to\infty\). If \(c_*>0\) is the unique **positive** solution of \(e^{c_*}=1+2c_*\), then four sharp scale limits hold:
\[
\boxed{\quad b^2\tau_A\longrightarrow c_*,\qquad
ab\tau_B\longrightarrow1,\qquad
\frac{b^2\theta_B}{\log(b/a)}\longrightarrow1,\qquad
b\left(\max_t\|T(t)\|_{\infty\to\infty}-1\right)\longrightarrow2a.\quad}
\]
These distinguish within-small-part recovery, transient peak, and final recovery on three parametrically separated time scales, although the maximum coordinatewise amplification converges to one.

## Assumptions and scope
Both part sizes are at least two and all cross-part edges have conductance one. The Laplacian is \(L=D-A\), not the normalized or random-walk Laplacian. Matrix positivity refers to every coordinate and every nonnegative input; the norm uses the **unweighted** vertex \(\ell^\infty\) norm. The result is valid for every integer pair \(2\le a\le b\) and all real times \(t\ge0\). No conclusion is asserted for arbitrary bipartite graphs, different conductance patterns, or other powers of \(L\).

## Proof
**1. Complete spectral kernel.** Let \(A\) and \(B\) denote the vertex parts. The four mutually orthogonal spectral projectors of \(L\) are: \(P_0=N^{-1}{\bf1}{\bf1}^{\top}\), the zero-sum projector \(P_A=I_A-J_A/a\) supported on \(A\), the analogous \(P_B=I_B-J_B/b\), and \(P_N=I-P_0-P_A-P_B\). Their Laplacian eigenvalues are, respectively, \(0,b,a,N\). Therefore
\[
T(t)=P_0+e^{-b^2t}P_A+e^{-a^2t}P_B+e^{-N^2t}P_N.
\]
For distinct vertices in \(A\), the entry is \(H_A(t)/(aN)\); for distinct vertices in \(B\), it is \(H_B(t)/(bN)\). Each cross-part entry is \((1-e^{-N^2t})/N>0\) for \(t>0\). Diagonal entries are strictly positive sums of nonnegative spectral-projector diagonal entries. Since \(T(t){\bf1}={\bf1}\), the absolute sum of a row is one plus twice the mass of its negative entries.

**2. Exactly one sign recovery for each part.** Each \(H\) vanishes at zero and has derivative \(-abN\) there. For instance,
\[
H_A'(t)=Nb^2e^{-b^2t}\left[1-\frac Nb e^{-(N^2-b^2)t}\right].
\]
This derivative changes once from negative to positive, at \(\theta_A=\log(N/b)/(N^2-b^2)\). Since \(H_A(t)\to a>0\), there is exactly one positive zero \(\tau_A>\theta_A\). Interchanging \(a,b\) establishes the same assertions for \(H_B\), with minimum at \(\theta_B\).

**3. Ordering the two cutoffs.** For fixed \(N\) and any \(q\in(0,N)\), define \(\tau(q)>0\) by
\[
N(1-e^{-q^2\tau})=q(1-e^{-N^2\tau}).
\]
The preceding derivative argument proves existence and uniqueness. Put \(g_q(t)=(1-e^{-q^2t})/q\). Let \(c_*>0\) solve \(e^{c_*}=1+2c_*\); it is unique because \(e^x-1-2x\) is strictly convex, decreases initially and diverges to infinity. At \(t=c_*/q^2\), set \(u=q/N\in(0,1)\). The function \(u\mapsto u(1-e^{-c_*/u^2})\) increases strictly for \(u<1\), since its derivative is \(1-(1+2c_*/u^2)e^{-c_*/u^2}>0\). Hence \(g_q(c_*/q^2)>g_N(c_*/q^2)\), and uniqueness of the crossing gives \(q^2\tau(q)<c_*\).

Now take \(0<p<q<N\) and evaluate at \(t=\tau(q)\). For \(0<x\le q\), one has \(x^2t<c_*\), so
\[
\frac{\partial g_x(t)}{\partial x}
=\frac{(1+2x^2t)e^{-x^2t}-1}{x^2}>0.
\]
It follows that \(g_p(t)<g_q(t)=g_N(t)\), whence \(\tau(p)>\tau(q)\). Choosing \(p=a,q=b\) gives \(\tau_B=\tau(a)\ge\tau(b)=\tau_A\), strictly when \(a<b\).

**4. Dominance of larger-part rows.** For \(a<b\), let the *signed* negative masses from the two row types be
\[
U(t)=\frac{a-1}{aN}\left[Ne^{-b^2t}-a-be^{-N^2t}\right],\quad
V(t)=\frac{b-1}{bN}\left[Ne^{-a^2t}-b-ae^{-N^2t}\right].
\]
The row norms equal \(1+2[U(t)]_+\) and \(1+2[V(t)]_+\). Set \(D(t)=V(t)-U(t)\), \(\alpha=(b-1)/b\), \(\beta=(a-1)/a\), and
\[
\delta=\beta b-\alpha a=(b-a)\left(1-\frac N{ab}\right)>0.
\]
Direct subtraction gives
\[
D(t)=-\frac{b-a}{N}+\alpha e^{-a^2t}-\beta e^{-b^2t}+\frac\delta N e^{-N^2t}.
\]
Here \(D(0)=0\), \(D'(0)=b-a>0\), and \(D(t)\to-(b-a)/N<0\). Multiplying its derivative by \(e^{a^2t}\) yields
\[
G(t)=-\alpha a^2+\beta b^2e^{-(b^2-a^2)t}-\delta N e^{-(N^2-a^2)t}.
\]
The derivative of \(G\) is the difference of a negative slower-decaying exponential and a positive faster-decaying exponential. It is either everywhere negative or changes once from positive to negative. Since \(G(0)>0\) and \(G(\infty)<0\), \(G\), and hence \(D'\), changes sign exactly once from positive to negative. Thus \(D\) rises then falls and has a unique positive zero. At \(t=\tau_A\), \(U=0\) but \(V>0\) because \(\tau_A<\tau_B\), so \(D(\tau_A)>0\); its positive zero occurs **after** \(\tau_A\). Thus \(V>U>0\) for \(0<t<\tau_A\), only \(V\) is positive for \(\tau_A\le t<\tau_B\), and both positive parts vanish thereafter. This proves the single-row-type sharp norm formula. When \(a=b\), the two row types agree by symmetry.

**5. Exact peak and three scale limits.** The bracket in the norm formula is positive exactly on \((0,\tau_B)\) and has one maximum at \(\theta_B\). Its stationarity identity is \(e^{-(N^2-a^2)\theta_B}=a/N\), which reduces the maximum to the claimed closed form. Equality in the induced \(\ell^\infty\) norm is realized by taking the signs of the entries of any maximizing matrix row as an input vector.

For \(b\to\infty\) at fixed \(a\), substitute \(t=s/b^2\) in \(H_A(t)/a\). Uniformly for \(s\) in compact sets this converges to \(1-(1+2s)e^{-s}\), whose unique positive root is \(c_*\), giving \(b^2\tau_A\to c_*\). Substitute \(t=s/(ab)\) in \(H_B(t)/a\). Uniformly for positive \(s\) in compact subsets this converges to \(s-1\), giving \(ab\tau_B\to1\). The formula for \(\theta_B\) immediately gives \(b^2\theta_B/\log(b/a)\to1\). Finally, the peak bracket is \(a/b+o(1/b)\); multiplying its prefactor gives the asserted amplification limit.

## Verification
The accompanying standalone standard-library script `verify_bipartite.py` computes all four rational spectral projectors, checks orthogonality and their exact reconstruction of \(L\), and compares the resulting heat kernel with an independent truncated power-series matrix exponential on 25 graph sizes and five times each. It checks row sums, within-part entries, positivity of cross-part entries, norm formulas, dominant part, temporal maxima, and threshold signs. Large-contrast test cases check consistency with the asymptotic limits. On execution the script reports `ALL CHECKS PASSED: 41930 assertions`. The proof above, not the finite tests, establishes universal and asymptotic statements.

## Relationship to prior work
Daners, Glück and Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices* (arXiv:1511.05294, first posted 2015-11-17), develop spectral positivity conditions and finite-dimensional semigroup criteria but do not give these exact graph-specific thresholds, norm, and scale laws in the inspected sections. The public paper *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups* (2026) proves a general no-gap result for at most three spectral values; the unequal complete bipartite Laplacian has four distinct eigenvalues and that theorem neither yields its positivity horizon nor its sharp maximum-norm transient. Gazzola and Grunau (2008) establish eventual local positivity for a continuous-space biharmonic heat equation, not a finite unweighted biclique calculation.

## Limitations
No assertion is made for weighted or normalized graph Laplacians, other graph families, or higher powers than \(L^2\). The exact norm formula is specific to the unweighted complete bipartite graph. The comparison with the 2008 continuous-space biharmonic article used its openly available abstract; its full text was not inspected. Another equivalent earlier derivation could exist under graph-filter, bi-Laplacian, or exponential-matrix terminology, so historical priority remains subject to wider independent examination.

## References
[1] D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294 (first public version 2015-11-17); https://arxiv.org/abs/1511.05294 . Relevant open full text: https://ar5iv.labs.arxiv.org/html/1511.05294 . Primary classification: 47D06.

[2] *A three-spectral-value barrier for gaps in positivity times of self-adjoint semigroups* (2026), public mathematical record; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-three-spectral-value-barrier-for-gaps-in-positivity-times-of-s--da21753d4271 .

[3] F. Gazzola, H.-C. Grunau, *Eventual local positivity for a biharmonic heat equation in \(\mathbb R^n\)*, Discrete Contin. Dyn. Syst. Ser. S 1 (2008), 83–87, doi:10.3934/dcdss.2008.1.83; https://www.aimsciences.org/article/doi/10.3934/dcdss.2008.1.83 .
