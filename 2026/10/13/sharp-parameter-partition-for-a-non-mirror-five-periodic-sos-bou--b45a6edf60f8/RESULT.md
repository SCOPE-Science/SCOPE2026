# Sharp parameter partition for a non-mirror five-periodic SOS boundary-law branch
## Finding
For the ferromagnetic SOS model on the Cayley tree of order \(k=2\), consider the non-mirror \(q=5\) subcase isolated by Rozikov. A normalized boundary law in this subcase has period block
\[
(x,1,y,y,1),
\]
where
\[
y=\eta_\tau(x)=x^{-2}(2-\tau x+\tau x^2-x^3),\qquad \tau>2.
\]
The source shows that, after excluding the trivial solution \(x=1\), the fixed-point condition is
\[
\zeta_\tau(x)=0,
\]
with
\[
\begin{aligned}
\zeta_\tau(x)={}&(2\tau-1)x^6-(3\tau^2-3\tau+2)x^5+(\tau^3+6\tau-2)x^4\\
&-(\tau^3+2\tau^2+4\tau)x^3+(6\tau^2-4\tau+8)x^2-(12\tau-8)x+8.
\end{aligned}
\]
Define
\[
\tau_-={9-\sqrt5\over2},\qquad \tau_+={9+\sqrt5\over2},
\]
and let \(w_*\) be the unique positive root of
\[
R(w)=w^5-47w^4+697w^3-4384w^2+10816w-9728.
\]
Then
\[
\tau_*=2+\sqrt{w_*}=7.119258320832055213\ldots.
\]
The exact number \(N(\tau)\) of distinct nontrivial positive normalized solutions in this subcase is
\[
N(\tau)=\begin{cases}
0,&2<\tau\le \tau_-,\\
2,&\tau_-<\tau\le \tau_+,\\
4,&\tau_+<\tau<\tau_*,\\
5,&\tau=\tau_*,\\
6,&\tau>\tau_*.
\end{cases}
\]
Every counted root satisfies \(\eta_\tau(x)>0\). At \(\tau_-\) and \(\tau_+\), the changing pair merges with the trivial root \(x=1\). At \(\tau_*\), a genuinely nontrivial positive double root is present, so five distinct nontrivial solutions occur exactly at that parameter. The published \(\tau=8\) example is therefore the final cell of a sharp three-threshold partition rather than an isolated maximal-count parameter.

## Assumptions and scope
The interaction, normalization, and parameter \(\tau=2\cosh(\beta)>2\) are those of Rozikov's SOS model. The claim is restricted to the particular non-mirror five-periodic reduction (2.24)--(2.25), equivalently its renamed companion (2.26). It counts distinct positive normalized boundary-law solutions of that reduction. It does not assert that these exhaust every solution of the full four-variable five-periodic system (2.23), nor does it address extremality, reconstruction, or thermodynamic dominance.

The source proves that for \(x\ne1\), positivity of \(\eta_\tau(x)\) together with \(\zeta_\tau(x)=0\) gives a solution of the reduced system. It also verifies at \(\tau=8\) that all six positive roots of \(\zeta_8\) have positive \(\eta_8\).

## Proof
A direct discriminant calculation gives
\[
\operatorname{disc}_x\zeta_\tau
=4096(\tau^2-9\tau+19)(\tau^2+\tau-1)P_{10}(\tau),
\]
where
\[
P_{10}(\tau)=R((\tau-2)^2).
\]
Equivalently,
\[
\begin{aligned}
P_{10}(\tau)={}&\tau^{10}-20\tau^9+133\tau^8-208\tau^7-1207\tau^6+4628\tau^5\\
&-1764\tau^4-7584\tau^3+176\tau^2+6208\tau-3008.
\end{aligned}
\]
An exact Sturm sequence for \(R\) has three sign variations at \(w=0\) and two at \(w=+\infty\), so \(R\) has exactly one positive real root. Hence the discriminant has exactly three zeros in the physical interval \(\tau>2\): \(\tau_-\), \(\tau_+\), and \(\tau_*\). The factor \(\tau^2+\tau-1\) has no zero there.

The constant term of \(\zeta_\tau\) is \(8\), and its leading coefficient is \(2\tau-1>0\). Thus a positive root cannot enter or leave through \(0\) or \(+\infty\). Away from the three discriminant values all roots are simple, so the number of positive roots is constant on each complementary interval. Exact Sturm counts at the rational sample points \(\tau=3,4,6,8\) are respectively
\[
0,\quad 2,\quad 4,\quad 6.
\]
This establishes the four open-cell counts.

At the first two transition values,
\[
\zeta_\tau(1)=\tau^2-9\tau+19,
\qquad
\partial_x\zeta_\tau(1)=\tau(\tau^2-9\tau+19).
\]
Moreover, at either root of \(\tau^2-9\tau+19\),
\[
\partial_x^2\zeta_\tau(1)=36-8\tau\ne0.
\]
Therefore \(x=1\) is exactly a double root of \(\zeta_\tau\) at \(\tau_-\) and \(\tau_+\). Since \(x=1\) is the already-excluded trivial solution, the nontrivial counts at the endpoints are \(0\) and \(2\), respectively.

The positive root \(w_*\) of \(R\) is simple, so \(\tau_*\) is a simple zero of the discriminant. It is distinct from \(\tau_\pm\); hence \(\zeta_{\tau_*}(1)\ne0\). A simple discriminant zero for this real one-parameter polynomial family gives exactly one double root and all other roots simple. Since the positive-root count changes from four to six across \(\tau_*\), that double root is positive. Consequently there are exactly five distinct nontrivial positive roots at \(\tau_*\).

Finally, positivity of the reconstructed second coordinate cannot be lost along these root branches because
\[
\operatorname{Res}_x\!\left(\zeta_\tau(x),\,2-\tau x+\tau x^2-x^3\right)=64.
\]
Thus no root of \(\zeta_\tau\) can satisfy \(\eta_\tau(x)=0\). The six roots at \(\tau=8\) have positive \(\eta_8\), independently checked by exact rational root isolation in the verifier. Continuing the simple branches through the open cells, and taking nonzero limits at the three collision points, shows that every positive root counted above has \(\eta_\tau(x)>0\).

## Verification
`verify.py` uses only the Python standard library and exact rational arithmetic. It recomputes the discriminant identity at thirty-four distinct integer values; the Sylvester-determinant degree bound makes this an identity certificate. It similarly certifies the constant resultant \(64\), performs exact Sturm counts \(0,2,4,6\) at \(\tau=3,4,6,8\), proves that \(R\) has exactly one positive root, isolates \(\tau_*\) in
\[
7.11925832<\tau_*<7.11925833,
\]
and isolates all six roots of \(\zeta_8\) in disjoint rational intervals while checking positive \(\eta_8\) on each interval.

## Relationship to prior work
Rozikov derives the same reduced system, the polynomial \(\zeta_\tau\), and the positivity requirement \(\eta_\tau(x)>0\). The paper then specializes to \(\tau=8\), where a graph is used to identify six nontrivial positive roots and Theorem 4 records six five-height-periodic non-mirror symmetric gradient Gibbs measures for that example. The paper does not give the parameter partition above or the third algebraic transition \(\tau_*\).

The earlier paper of Henning, Külske, Le Ny, and Rozikov treats four-periodic boundary laws on the binary tree and three-periodic laws for arbitrary order, not this five-periodic equation. Focused searches for the source equation, the exact polynomial \(P_{10}\), the decimal value of \(\tau_*\), and five-periodic threshold aliases did not locate a covering statement.

## Limitations
This is a complete classification only for the source's particular reduced non-mirror five-periodic branch. The full system (2.23) may have additional five-periodic boundary laws. The result counts normalized boundary-law solutions; although the source provides the corresponding GGM construction and identifiability framework, no new global classification of all gradient Gibbs measures is claimed here.

## References
1. U. A. Rozikov, “Mirror Symmetry of Height-Periodic Gradient Gibbs Measures of an SOS Model on Cayley Trees,” arXiv:2203.11446; Journal of Statistical Physics 188 (2022), Article 26, doi:10.1007/s10955-022-02953-z. See equations (2.23)--(2.26), Theorem 4, and Figure 4.
2. F. Henning, C. Külske, A. Le Ny, U. A. Rozikov, “Gradient Gibbs measures for the SOS model with countable values on a Cayley tree,” Electronic Journal of Probability 24 (2019), Paper 104; arXiv:1902.04909.
