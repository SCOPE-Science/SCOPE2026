# Exact theta-step positivity horizons on complete multipartite diffusion networks

## Finding
Let \(r\ge2\), let \(p_1,\ldots,p_r\ge2\) be integers, let \(N=\sum_{i=1}^r p_i\), and let \(s=\min_i p_i\). The unweighted complete multipartite graph \(G=K_{p_1,\ldots,p_r}\) has graph Laplacian \(L\), with an edge of conductance one between vertices in different classes and no edges inside a class. For \(0\le\theta\le1\) and step \(h\ge0\), consider the diffusion \(\theta\)-step
\[
T_{\theta,h}=(I+\theta hL)^{-1}(I-(1-\theta)hL).
\]
It is stochastic (entrywise nonnegative with all row sums one) for exactly the steps \(0\le h\le H_{N,s}(\theta)\), where
\[
H_{N,s}(\theta)=\begin{cases}
\infty,&\theta\ge 1-1/N,\\[2mm]
\displaystyle\frac{2}{\sqrt{B^2+4A\theta}-B},&0\le\theta<1-1/N,
\end{cases}
\]
with \(A=(N-s)[N(1-\theta)-1]>0\) and \(B=\theta(2N-s)-(N-s)\). This expression is valid at \(\theta=0\), giving \(H_{N,s}(0)=1/(N-s)\).

The full sharp horizon depends only on the vertex count \(N\) and the smallest class size \(s\), not on the number or other sizes of classes. For \(\theta<1-1/N\), the first zero diagonal entries at \(h=H_{N,s}(\theta)\) occur precisely at vertices belonging to classes of size \(s\); for each fixed admissible \(N,\theta\), the horizon strictly increases with \(s\). In particular, for Crank–Nicolson (\(\theta=1/2\)),
\[
H_{N,s}(1/2)=\frac{s+\sqrt{s^2+4(N-s)(N-2)}}{(N-s)(N-2)}.
\]
For sequences of such graphs with \(N\to\infty\), \(s/N\to\alpha\in[0,1/2]\), and any fixed \(0\le\theta<1\),
\[
\lim_{N\to\infty}N H_{N,s}(\theta)=\frac{1}{(1-\theta)(1-\alpha)}.
\]

## Assumptions and scope
Every part size is an integer at least two and there are at least two parts; thus \(N\ge4\), \(2\le s\le N/2\). All cross-class edges have unit conductance, and the symmetric combinatorial Laplacian is unnormalized. The step is the one-step implicit-explicit \(\theta\) discretization of \(\dot u=-Lu\), with \(\theta=0\) forward Euler, \(\theta=1/2\) Crank–Nicolson, and \(\theta=1\) backward Euler. Stochasticity concerns the complete end-step matrix acting on arbitrary nonnegative data, not just selected initial data or intermediate stages. There are no self-loops in the graph, but the numerical update may have a positive diagonal. The asymptotic statement holds along any integer family obeying these constraints.

## Proof
Write \(t=\theta h\) and \(R_t=(I+tL)^{-1}\). The constant eigenspace of \(L\) has eigenvalue zero. For each part of size \(p\), its internal zero-sum vectors form an eigenspace of eigenvalue \(N-p\). The remaining vectors constant on each part and orthogonal to the global constant vector form an eigenspace of eigenvalue \(N\). These spaces are mutually orthogonal and exhaustive. The orthogonal projectors have diagonal weights \(1/N\), \((p-1)/p\), and \((N-p)/(Np)\), respectively, at a vertex in a part of size \(p\). Thus that vertex has resolvent diagonal
\[
R_p(t)=\frac1N+\frac{p-1}{p[1+(N-p)t]}+\frac{N-p}{Np[1+Nt]}.
\]
For \(p>q\), direct subtraction and cancellation yields
\[
R_p(t)-R_q(t)=\frac{t(p-q)[1+(N-1)t]}{[1+Nt][1+(N-p)t][1+(N-q)t]}.
\]
Consequently, at any positive \(t\), exactly the vertices in the smallest parts minimize the diagonal resolvent entries.

For \(\theta>0\), \(I+tL\) is a nonsingular graph-Laplacian \(M\)-matrix, hence \(R_t\) is entrywise nonnegative. The algebraic identity
\[
T_{\theta,h}=\frac{R_t-(1-\theta)I}{\theta}
\]
shows that every off-diagonal entry of \(T_{\theta,h}\) is nonnegative. Since \(L\mathbf1=0\), all its row sums equal one. Therefore the exact stochasticity test is \(R_s(t)\ge1-\theta\). For \(\theta=0\), direct inspection of \(T_{0,h}=I-hL\) gives the same sharp restriction from the maximum degree \(N-s\).

Combining the three projector contributions over a common denominator gives, for any part size \(p\),
\[
(T_{\theta,h})_{vv}=\frac{1+[\theta(2N-p)-(N-p)]h-\theta(N-p)[N(1-\theta)-1]h^2}{[1+\theta Nh][1+\theta(N-p)h]}.
\]
This polynomial quotient also specializes continuously and correctly to \(\theta=0\). Each denominator is positive. Since \(R_s(t)\ge1/N\), if \(\theta\ge1-1/N\), stochasticity holds for every \(h\). If instead \(\theta<1-1/N\), then \(A=(N-s)[N(1-\theta)-1]>0\) and the smallest-class numerator becomes \(1+Bh-A\theta h^2\). For \(\theta>0\) it starts positive, is strictly concave, and has exactly one positive root, namely the displayed \(H_{N,s}(\theta)\). At \(\theta=0\) it equals \(1-(N-s)h\), with unique positive root \(1/(N-s)\); the radical formula agrees because \(B=-(N-s)\). Before that root every diagonal is nonnegative; afterwards at least one smallest-class diagonal is negative. The resolvent ordering proves the exact limiting vertex classes, including simultaneous ties.

At fixed \(N\) and \(0<\theta<1-1/N\), the strictly increasing comparison \(R_p(t)>R_q(t)\) for \(p>q\) implies the crossing time of the level \(1-\theta\) strictly increases with class size; the same follows immediately for \(\theta=0\). Substituting \(\theta=1/2\) and rationalizing the positive quadratic root yields the Crank–Nicolson formula.

For the asymptotic assertion, set \(h=c/N\) and pass to a subsequence with \(s/N\to\alpha\). For fixed \(\theta>0\), the projector expression satisfies
\[
R_s(\theta c/N)\longrightarrow\frac{1}{1+\theta(1-\alpha)c}.
\]
This remains valid when \(\alpha=0\): in that case the two nonconstant projector contributions have the same asymptotic denominator, even if \(s\) stays bounded. The unique solution of \(1/[1+\theta(1-\alpha)c]=1-\theta\) is \(c=1/[(1-\theta)(1-\alpha)]\). Monotonicity and continuity of the limiting function bracket the unique finite crossing and prove convergence of the scaled horizons. At \(\theta=0\), the exact forward-Euler horizon gives the same limit directly.

## Verification
The standalone `verify.py` uses exact `fractions.Fraction` Gauss–Jordan inversion. For all complete multipartite part-size profiles with \(N\le10\), at least two parts and sizes at least two, it constructs the full Laplacian and compares the calculated resolvent diagonals with the projector formula, row sums with one, and the actual entrywise sign of the full \(\theta\)-step with the claimed quadratic/critical threshold test. Tested \(\theta\) values are \(0,1/5,1/2,2/3,3/4,9/10,1\), and tested steps are \(0,1/7,1/2,1,3/2,3,7\). The program completed `VERIFY_OK 29662 exact rational assertions`. An independent symbolic simplification checked the resolvent difference identity and the diagonal polynomial identity. These finite and symbolic checks support but do not prove all integer orders: the projector and \(M\)-matrix arguments above are the infinite-family proof. Execute `python3 verify.py` with Python 3 and no third-party packages.

## Relationship to prior work
General time-stepping positivity and cone invariance are developed by Horváth (2004), while Schatz, Thomée, and Wahlbin (2010) analyze positivity of the \(\theta\)-method for finite-element discretizations. Jin, Lazarov, Thomée, and Zhou (2015) investigate nonnegativity for subdiffusion discretizations. These works give broader frameworks or sufficient conditions, not the displayed exact complete-multipartite threshold.

The publicly available paper *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026) proves the general diagonal-resolvent positivity criterion, and its complete-graph case. That general principle is prior work and is not claimed here. The present claim evaluates the resolvent for an arbitrary unweighted multipartite graph, proves that only the minimum part size controls the complete all-\(\theta\) threshold, and gives an explicit radical and limiting-vertex classification. In particular, the general criterion does not itself state the sharp explicit formula or the collapse of the entire partition to \(N,s\).

## Limitations
The theorem excludes singleton parts, unequal cross-edge conductances, normalized Laplacians, nonreversible generators, nonlinear diffusion and positivity of internal integration stages. It concerns exact arithmetic, so entries equal to zero at the threshold may appear slightly negative under floating-point evaluation. Explicit projector evaluation is elementary once the graph's full spectrum is written down; equivalent formulas could be present in unpublished, difficult-to-index or other graph-diffusion literature. Only the stated restricted family and full end-step matrix are classified. No independent mathematical audit has been performed.

## References
1. Z. Horváth, *Positively invariant cones of dynamical systems under Runge–Kutta and Rosenbrock-type discretization*, Proc. Appl. Math. Mech. 4 (2004), 688–689. DOI: 10.1002/pamm.200410325. First published 27 December 2004.
2. A. H. Schatz, V. Thomée, L. B. Wahlbin, *On Positivity and Maximum-Norm Contractivity in Time Stepping Methods for Parabolic Equations*, Comput. Methods Appl. Math. 10 (2010), 421–443. DOI: 10.2478/cmam-2010-0025.
3. B. Jin, R. Lazarov, V. Thomée, Z. Zhou, *On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations*, arXiv:1510.02825v1 (9 October 2015).
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, publicly available mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
