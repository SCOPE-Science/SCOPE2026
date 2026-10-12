# A Hermite perturbation lowers the closed one-sigma infinitely-divisible bound to \(e^{-1}\)
## Finding
Let \(\mathcal I\) denote the class of infinitely divisible real random variables with finite second moment, and let
\[
P_{\mathcal I}=\inf_{X\in\mathcal I}\Pr\!\left\{|X-\mathbb EX|\le\sqrt{\operatorname{Var}(X)}\right\}.
\]
Then
\[
P_{\mathcal I}\le e^{-1}.
\]
An explicit approximating family is obtained as follows. For \(0<\varepsilon<2\), take independent random variables
\[
N_\varepsilon\sim\operatorname{Pois}(\varepsilon),
\qquad
M_\varepsilon\sim\operatorname{Pois}(1-\varepsilon/2),
\]
and set
\[
X_\varepsilon=N_\varepsilon+2M_\varepsilon.
\]
Then
\[
\Pr\!\left\{|X_\varepsilon-\mathbb EX_\varepsilon|\le\sqrt{\operatorname{Var}(X_\varepsilon)}\right\}
=e^{-1-\varepsilon/2}\left(1+\frac{3\varepsilon}{2}+\frac{\varepsilon^3}{6}\right),
\]
so this probability converges to \(e^{-1}\) as \(\varepsilon\downarrow0\).

## Assumptions and scope
The class \(\mathcal I\) and the use of a closed one-standard-deviation interval are exactly those in Zhang, Hu, and Sun's measure-concentration problem. No claim is made here about the exact value of \(P_{\mathcal I}\); the result is an improved explicit upper bound.

The family \(X_\varepsilon\) is the classical two-parameter Hermite distribution. Equivalently, its Lévy measure on the positive integers is
\[
\varepsilon\,\delta_1+(1-\varepsilon/2)\,\delta_2.
\]
Hence every member of the family is compound Poisson and therefore infinitely divisible.

## Proof
Because the two Poisson variables are independent,
\[
\mathbb EX_\varepsilon
=\varepsilon+2(1-\varepsilon/2)=2
\]
and
\[
\operatorname{Var}(X_\varepsilon)
=\varepsilon+4(1-\varepsilon/2)=4-\varepsilon.
\]
For \(0<\varepsilon<2\),
\[
1<\sqrt{4-\varepsilon}<2.
\]
Since \(X_\varepsilon\) is integer-valued, the closed one-standard-deviation event is therefore exactly
\[
\left\{|X_\varepsilon-2|\le\sqrt{4-\varepsilon}\right\}
=\{X_\varepsilon\in\{1,2,3\}\}.
\]
Write \(a=\varepsilon\) and \(b=1-\varepsilon/2\). The joint Poisson factor is \(e^{-(a+b)}=e^{-1-\varepsilon/2}\). Direct enumeration of the three attainable totals gives
\[
\Pr\{X_\varepsilon=1\}=e^{-(a+b)}a,
\]
\[
\Pr\{X_\varepsilon=2\}=e^{-(a+b)}\left(\frac{a^2}{2}+b\right),
\]
and
\[
\Pr\{X_\varepsilon=3\}=e^{-(a+b)}\left(\frac{a^3}{6}+ab\right).
\]
Summing and substituting \(b=1-a/2\) yields
\[
\Pr\{1\le X_\varepsilon\le3\}
=e^{-1-\varepsilon/2}\left(1+\frac{3\varepsilon}{2}+\frac{\varepsilon^3}{6}\right).
\]
Taking \(\varepsilon\downarrow0\) gives the limit \(e^{-1}\). Since every \(X_\varepsilon\) belongs to \(\mathcal I\), the defining infimum satisfies \(P_{\mathcal I}\le e^{-1}\).

## Verification
The proof is exact and does not rely on numerical evidence. The bundled script `verify.py` independently checks the moment identities, verifies by direct Poisson summation that the closed one-sigma event is \(\{1,2,3\}\) for deterministic test values of \(\varepsilon\), checks the displayed probability formula, and verifies convergence toward \(e^{-1}\).

The successful terminal line is:
`VERIFY_OK target=0.367879441171442 formula_error<1e-14`.

The finite computations are regression checks only; the universal statement over \(0<\varepsilon<2\) follows from the analytic proof.

## Relationship to prior work
Zhang, Hu, and Sun define \(P_{\mathcal I}\) for all infinitely divisible laws with finite second moments and leave its exact value open. Their Theorem 4.3 uses the symmetric Poisson family to obtain
\[
P_{\mathcal I}\le e^{-1}\sum_{k=0}^{\infty}\frac{1}{2^{2k}(k!)^2}\approx0.46576.
\]
The same paper proves for the strict one-standard-deviation functional that
\[
P_{\mathcal I_0}\le e^{-1}.
\]
The present Hermite perturbation lowers the published closed-interval upper bound to the same numerical level \(e^{-1}\). The source's inspected full text treats geometric, symmetric geometric, Poisson, and symmetric Poisson subfamilies; it does not state this two-jump compound-Poisson construction or the improved closed-interval bound.

The Hermite distribution itself is classical. The new content is the boundary perturbation \(\varepsilon\mapsto(\varepsilon,1-\varepsilon/2)\) that fixes the mean at \(2\), moves the standard-deviation endpoints strictly inside the lattice points \(0\) and \(4\), and turns the limiting closed interval into an effectively strict Poisson-one interval.

## Limitations
The result is an upper bound, not an evaluation of \(P_{\mathcal I}\). The source proves only that \(P_{\mathcal I}\ge P_{\mathcal I_0}>0\), so the present construction does not determine either infimum.

The originality search did not locate a published use of this Hermite family for the one-standard-deviation infimum. Because Hermite distributions and lattice-boundary perturbations are classical objects, an equivalent observation could exist under different terminology; this remains the principal residual originality risk.

## References
1. J. Zhang, Z.-C. Hu, and W. Sun, *On the measure concentration of infinitely divisible distributions*, arXiv:2310.03471v1, first public 2023-10-05; revised arXiv:2310.03471v2; later published in *Acta Mathematica Scientia*.
2. C. D. Kemp and A. W. Kemp, classical work on the Hermite distribution; the representation \(X=N_1+2N_2\) with independent Poisson components is standard.
