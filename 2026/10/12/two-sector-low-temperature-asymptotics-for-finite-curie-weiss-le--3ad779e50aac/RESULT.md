# Two-sector low-temperature asymptotics for finite Curie--Weiss Lee--Yang zeros
## Finding
For the Curie--Weiss partition function
\[
Z_n(\beta,h)=\sum_{\sigma\in\{\pm1\}^n}\exp\left(\frac{\beta}{2n}\left(\sum_{j=1}^n\sigma_j\right)^2+h\sum_{j=1}^n\sigma_j\right),
\]
fix an integer \(n\ge2\), put \(h=ix\), and denote the nontrivial positive Lee--Yang zeros in \((0,\pi/2)\) by \(x_{n,k}(\beta)\). Thus \(1\le k\le n/2\) for even \(n\), while \(1\le k\le(n-1)/2\) for odd \(n\); the odd case also has the symmetry-forced zero \(x=\pi/2\). Put
\[
\theta_{n,k}=\frac{(2k-1)\pi}{2n}.
\]
Then the low-temperature limit \(\beta\to\infty\) has the following explicit excitation-sector expansion.

For \(n=2\),
\[
x_{2,1}(\beta)=\frac{\pi}{4}+\frac12e^{-\beta}+O(e^{-3\beta}).
\]
For \(n=3\),
\[
x_{3,1}(\beta)=\frac{\pi}{6}+\frac{\sqrt3}2e^{-4\beta/3}-\frac{\sqrt3}4e^{-8\beta/3}+O(e^{-4\beta}).
\]
For \(n=4\),
\[
x_{4,k}(\beta)=\theta_{4,k}+\sin(2\theta_{4,k})e^{-3\beta/2}+\frac34\sin(4\theta_{4,k})e^{-2\beta}+o(e^{-2\beta}).
\]
For every \(n\ge5\),
\[
x_{n,k}(\beta)=\theta_{n,k}+\sin(2\theta_{n,k})e^{-2(n-1)\beta/n}+\frac{n-1}2\sin(4\theta_{n,k})e^{-4(n-2)\beta/n}+o(e^{-4(n-2)\beta/n}).
\]
In particular, every nontrivial principal zero approaches its zero-temperature lattice point from above with the same leading Arrhenius exponent \(2(n-1)/n\). The exponent is exactly the energy gap from the fully magnetized sector to the one-spin-flip sector. For \(n\ge4\), the next exponential scale is the two-spin-flip gap; at \(n=4\) the zero-magnetization sector is unpaired, which halves the coefficient that the generic paired-sector formula would give.

## Assumptions and scope
The normalization is exactly the Curie--Weiss normalization in Kabluchko, arXiv:2203.05533, Eq. (1.8): inverse temperature \(\beta>0\), unit interaction strength, and dimensionless external field \(h\). The statement is fixed-\(n\) and concerns \(\beta\to\infty\); it is not a thermodynamic-limit statement. For odd \(n\), the fixed zero at \(\pi/2\) is excluded because it has no displacement. The indexing of the moving positive zeros agrees with the simple-zero ordering used in Hou--Jiang--Newman after the change of variables \(t=\beta/(2n)\).

## Proof
Grouping configurations by the number \(j\) of positive spins gives the exact finite sum
\[
Z_n(\beta,ix)=\sum_{j=0}^n {n\choose j}
\exp\left(\frac{\beta}{2n}(n-2j)^2\right)e^{i(n-2j)x}.
\]
Pairing the \(j\) and \(n-j\) terms and dividing by \(2e^{\beta n/2}\) shows, for \(n\ge3\),
\[
F_{n,\beta}(x)=\cos(nx)+nq\cos((n-2)x)+R_{n,\beta}(x),
\qquad q=e^{-2(n-1)\beta/n}.
\]
For \(n=3\), \(R_{3,\beta}\equiv0\). For \(n=4\), direct pairing gives the sharper exact form
\[
F_{4,\beta}(x)=\cos(4x)+4e^{-3\beta/2}\cos(2x)+3e^{-2\beta}.
\]
For \(n\ge5\), the next paired magnetization sector gives
\[
F_{n,\beta}(x)=\cos(nx)+nq\cos((n-2)x)+{n\choose2}r\cos((n-4)x)+o(r),
\qquad r=e^{-4(n-2)\beta/n},
\]
uniformly with the first derivative on a fixed neighborhood of each \(\theta_{n,k}\). This follows directly from the finite number of remaining sectors, whose energy gaps are strictly larger than \(4(n-2)/n\).

Let \(s=(-1)^{k-1}\). At \(\theta=\theta_{n,k}\),
\[
\sin(n\theta)=s,\qquad
\cos((n-2)\theta)=s\sin(2\theta),\qquad
\cos((n-4)\theta)=s\sin(4\theta).
\]
Since \(\partial_x\cos(nx)|_{x=\theta}=-ns\ne0\), the implicit-function theorem produces a unique nearby zero. Writing it as \(\theta+\delta\) and expanding the preceding exact finite sums gives
\[
\delta=q\sin(2\theta)+\frac{n-1}2r\sin(4\theta)+o(r)
\]
for \(n\ge5\), because \({n\choose2}/n=(n-1)/2\) and \(q^2=o(r)\). For \(n=4\), the unpaired central term gives instead
\[
\delta=e^{-3\beta/2}\sin(2\theta)+\frac34e^{-2\beta}\sin(4\theta)+o(e^{-2\beta}).
\]
For \(n=3\), the exact equation \(\cos(3x)+3e^{-4\beta/3}\cos x=0\) yields the displayed two-term expansion by Taylor expansion at \(\pi/6\). For \(n=2\), the exact equation is \(\cos(2x)=-e^{-\beta}\), hence
\[
x_{2,1}(\beta)=\frac\pi4+\frac12\arcsin(e^{-\beta}),
\]
which gives the stated expansion. The Lee--Yang simplicity and ordering results ensure that these local branches are the indexed principal zeros.

## Verification
The proof is analytic and uses only the exact finite partition sum plus the implicit-function theorem. The accompanying `verify.py` independently evaluates the exact finite sum, isolates the relevant real zeros by bisection, and checks convergence of the scaled first and second displacements for representative values \(2\le n\le6\). The numerical replay is corroborative only; no finite computation is used to infer the asymptotic theorem.

## Relationship to prior work
Kabluchko, arXiv:2203.05533, gives the exact Curie--Weiss finite sum and its unitary-Hermite representation, but its Lee--Yang asymptotics concern the large-degree/thermodynamic regime with fixed real inverse temperature. Hou--Jiang--Newman, arXiv:2208.00917, prove for the same complete-graph model (with \(t=\beta/(2n)\)) that the nontrivial positive zeros decrease strictly and converge to \((2k-1)\pi/(2n)\) as the coupling tends to infinity. Their proof identifies the limiting two ground-state terms but does not state a convergence rate or excitation-sector correction. Deger--Flindt, arXiv:2002.01269, analyzes finite-size scaling of Curie--Weiss Fisher and Lee--Yang zeros toward thermodynamic criticality, a different limit. The present result quantifies the fixed-size low-temperature approach and identifies the first two magnetization sectors that control it.

## Limitations
The asymptotics are for fixed \(n\); no uniformity as \(n\to\infty\) is claimed. The result uses the complete-graph Curie--Weiss Hamiltonian with the normalization above and does not extend by this proof to general ferromagnetic graphs. It does not claim that no equivalent expansion exists in unindexed older statistical-mechanics literature. The \(n=4\) coefficient is exceptional because the second excited magnetization sector is the single central sector rather than a pair.

## References
1. Z. Kabluchko, *Lee--Yang zeroes of the Curie--Weiss ferromagnet, unitary Hermite polynomials, and the backward heat flow*, arXiv:2203.05533, first posted 2022-03-10.
2. Q. Hou, J. Jiang, C. M. Newman, *Motion of Lee-Yang zeros*, arXiv:2208.00917, first posted 2022-08-01.
3. A. Deger, C. Flindt, *Lee-Yang theory of the Curie-Weiss model and its rare fluctuations*, arXiv:2002.01269, first posted 2020-02-04.
