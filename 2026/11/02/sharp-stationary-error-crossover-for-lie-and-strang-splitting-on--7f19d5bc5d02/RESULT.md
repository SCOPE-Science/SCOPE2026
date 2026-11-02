# Sharp stationary-error crossover for Lie and Strang splitting on a directed Markov cycle

## Finding

Consider the three-state continuous-time Markov generator with transitions \(1\to2\) of rate \(1\), \(2\to3\) of rate \(2\), and \(3\to1\) of rate \(2\). Its invariant row probability is \(\pi=(1/2,1/4,1/4)\). Decompose the generator into its three single-edge generators in that order. For step size \(h>0\), define the exact-exponential Lie and symmetric Strang one-step transition matrices \(L_h\) and \(S_h\) below.

Put \(q=e^{-h/2}\in(0,1)\). Then their unique invariant row distributions are

\[
\pi_L(q)=\frac{(1+q^2,\ q^4,\ q^4)}{1+q^2+2q^4},
\qquad
\pi_S(q)=\left(\frac{q}{1+q^2},\frac{1-q+q^2-q^3+q^4}{(1+q^2)^2},\frac{q^2}{(1+q^2)^2}\right).
\]

With total-variation distance \(D(\nu,\pi)=\frac12\sum_{j=1}^3|\nu_j-\pi_j|\), the exact stationary discrepancies are

\[
D_L(q)=\frac{(1-q^2)(1+2q^2)}{2(1+q^2+2q^4)},
\qquad
D_S(q)=\frac{(1-q)^2(3q^2+2q+3)}{4(1+q^2)^2}.
\]

There is **exactly one** finite step size at which the long-time accuracy ranking reverses. Specifically, if \(q_*\) is the unique root in \((0,1)\) of

\[
P(q)=10q^7+2q^6+15q^5+3q^4+12q^3+4q^2+3q-1,
\]

then \(q_*=0.22049649387432393\ldots\) and \(h_*=-2\log q_*=3.02374697003674449\ldots\). The Strang stationary law is strictly closer to \(\pi\) for \(0<h<h_*\), equal in total variation at \(h=h_*\), and strictly farther from \(\pi\) for \(h>h_*\). Both schemes preserve nonnegativity and total mass for every \(h>0\), and both converge under repeated steps to their respective stationary laws.

The small- and large-step limits are sharp:

\[
D_L(h)=\frac38h+O(h^2),\qquad
D_S(h)=\frac18h^2+O(h^3),\qquad
\lim_{h\to\infty}D_L(h)=\frac12,\quad
\lim_{h\to\infty}D_S(h)=\frac34.
\]

More generally, for arbitrary positive edge rates \(a,b,c\) in the same directed cycle, the conventional Strang scheme has \(O(h^2)\) stationary total-variation error as \(h\downarrow0\), whereas the corresponding Lie scheme has strictly positive \(O(h)\) leading error. Whenever \(a<b\), the Strang stationary error is strictly larger than the Lie stationary error for all sufficiently large \(h\). The general-rate assertion ensures at least one accuracy reversal, but does **not** assert its uniqueness outside the specified \(1:2:2\) case.

## Assumptions and scope

Probabilities are row vectors and Markov matrices act on the right. Let \(G_1\), \(G_2\), and \(G_3\) be the three \(3\times3\) row-sum-zero generators whose only nonzero off-diagonal entries are, respectively, \((G_1)_{12}=a\), \((G_2)_{23}=b\), and \((G_3)_{31}=c\), with diagonal entries chosen to make row sums zero. Set \(Q=G_1+G_2+G_3\), and denote \(E_j(t)=e^{tG_j}\). The two unmodified operator splittings compared here are

\[
L_h=E_1(h)E_2(h)E_3(h),
\qquad
S_h=E_1(h/2)E_2(h/2)E_3(h)E_2(h/2)E_1(h/2).
\]

The central exact formulas specialize to \((a,b,c)=(1,2,2)\) and hold for every real \(h>0\), in exact arithmetic. This definition is deliberately a product of individual-edge semigroups, not a balanced, equilibrium-corrected, or otherwise modified splitting. Stationary error means the distance between invariant distributions of the discrete schemes and the exact continuous-time process, **not** finite-time trajectory error or one-step local error.

## Proof

**Step 1: Markov and stationary structure.** The exact single-edge semigroup \(E_{i\to j}(t)\) is identity except in row \(i\), where it has diagonal survival \(e^{-\lambda t}\) and transition probability \(1-e^{-\lambda t}\) in column \(j\). Consequently every factor is row-stochastic. For positive rates and \(h>0\), both products contain a connected directed cycle and positive holding probabilities. Each is irreducible and aperiodic, hence has a unique invariant probability and converges to it. The continuous-time stationary flow condition is \(a\pi_1=b\pi_2=c\pi_3\), giving \(\pi=(1/a,1/b,1/c)/U\), where \(U=1/a+1/b+1/c\).

**Step 2: The exact invariant laws.** Insert \(q=e^{-h/2}\) and the rates \(1,2,2\) into the factor matrices. Direct multiplication of their five/three stochastic factors gives the two products. Substituting the displayed \(\pi_L(q)\) and \(\pi_S(q)\) yields, by polynomial cancellation, \(\pi_L(q)L_h=\pi_L(q)\) and \(\pi_S(q)S_h=\pi_S(q)\); both row vectors sum to one. Their entries are strictly positive on \((0,1)\). Independent cofactor evaluation of \(I-L_h\) and \(I-S_h\) yields the same normalized invariant weights (see verification program). These identities prove the claimed formulas by uniqueness.

**Step 3: Absolute values and the exact distance.** For every \(0<q<1\), the Lie deviation at state 1 is positive and its deviations at states 2 and 3 are equal and negative. The Strang deviations at states 1 and 3 are negative, and its deviation at state 2 is positive. In detail,

\[
\pi_{S,1}-\frac12=-\frac{(1-q)^2}{2(1+q^2)},
\quad
\pi_{S,3}-\frac14=-\frac{(1-q^2)^2}{4(1+q^2)^2},
\quad
\pi_{S,2}-\frac14=\frac{(1-q)^2(3q^2+2q+3)}{4(1+q^2)^2}.
\]

The positive deviation equals total variation on a finite probability simplex. Using the corresponding positive Lie deviation gives exactly \(D_L\) and \(D_S\) above.

**Step 4: A single sharp crossover.** Elementary rational subtraction and factorization give

\[
D_S(q)-D_L(q)=\frac{(q-1)P(q)}{4(1+q^2)^2(1+q^2+2q^4)}.
\]

The denominator is positive, and \(q-1<0\). Every coefficient of \(P'(q)\) is strictly positive, so \(P\) increases strictly on \((0,1)\). As \(P(0)=-1\) and \(P(1)=48\), it has one and only one root there. Because \(q=e^{-h/2}\) decreases strictly as \(h\) grows, the comparison signs have precisely the direction stated. Taylor expansion at \(q=1\) and direct substitution at \(q=0\) give the small-step and saturated-step limits.

**Step 5: General-rate reversal mechanism.** Put \(u=e^{-ah}\), \(v=e^{-bh}\), and \(w=e^{-ch}\). The Lie product admits the exact invariant *unnormalized* weights

\[
\left(\frac{1}{1-u},\ \frac{v}{1-v},\ \frac{w}{1-w}\right).
\]

Indeed, multiplying these weights by \(E_1E_2E_3\) returns the same weights. Expanding at \(h=0\), the state-1 stationary deviation is

\[
(\pi_L)_1-\pi_1=\frac{1+\pi_1}{2U}\,h+O(h^2)>0.
\]

Hence Lie stationary total-variation error has a strictly positive linear leading coefficient. In contrast, the symmetric composition has \(S_h=e^{hQ}+O(h^3)\). As \(Q\) has a simple stationary eigenvector and a spectral gap on the zero-sum subspace, stationary perturbation gives \(\pi_S-\pi=O(h^2)\); thus Strang is strictly better for sufficiently small positive \(h\). At the other extreme, every individual-edge semigroup saturates to a deterministic transfer, yielding \(L_h\to{\bf1}\delta_1\) and \(S_h\to{\bf1}\delta_2\) in row convention. Their invariant laws tend to \(\delta_1\) and \(\delta_2\), so their total-variation errors tend to \(1-\pi_1\) and \(1-\pi_2\), respectively. If \(a<b\), then \(\pi_1>\pi_2\), making Strang strictly worse for all sufficiently large \(h\). Continuity then forces at least one crossing.

## Verification

The accompanying \(\texttt{verify.py}\) uses symbolic exact algebra to reconstruct both splitting matrices, verify the invariant equations and their normalization, derive the invariant weights independently through principal cofactors, check every deviation sign identity, factor the exact difference into \((q-1)P(q)\), prove \(P'\) positive by coefficient inspection, and verify the four endpoint coefficients/limits. It also checks the general-rate Lie invariant weights symbolically. A separate set of 300 exact-rational tests evaluates both transition matrices and stationary probability vectors, stochasticity, invariance, and total-variation identities on \(q=j/61\), \(1\le j\le60\). It prints \(q_*\) and \(h_*\) using high-precision root evaluation. Run \(\texttt{python verify.py}\) using \(\texttt{sympy>=1.12}\). These tests are corroboration; Steps 1–5 establish the full all-step theorem analytically.

## Relationship to prior work

Blanes, Iserles, and Macnamara study positivity-preserving integrators for graph-Laplacian ordinary differential equations and Markov-type systems, including novel modified exponentials; their analysis does not provide this conventional edge-exponential Lie/Strang stationary total-variation phase diagram. Gourgoulias, Katsoulakis, and Rey-Bellet analyze long-time errors in stochastic-operator splitting by path-space relative entropy rate, with a finite-state example; their observable and small-step error comparison differ from the all-step invariant-distribution threshold here. Speth, Green, MacNamara, and Strang demonstrate the classical problem of splitting-induced steady-state bias and introduce balanced corrective schemes. The present claim is **not** that stationary bias, positivity preservation, or order-dependent local accuracy were previously unknown; it is the exact global crossover and the precise polynomial/parameter boundary for uncorrected edge splitting.

## Limitations

Only the stated directed three-state cycle is fully classified by a unique crossover threshold. The additional arbitrary-rate result guarantees existence of a crossover under \(a<b\), not its location, number, or monotonicity. No comparison is made with balanced steady-state-corrected integrators, implicit methods, other factor orderings, general networks, or floating-point error. Total-variation ordering of invariant distributions does not imply ordering of finite-time weak error or path-space relative entropy. A relevant earlier balanced-splitting paper could be assessed only from its repository abstract in this investigation, so specialized priority overlap remains possible. The theorem is supported by the presented analytic derivation and exact-algebra checks; independent validation has not been performed.

## References

- S. Blanes, A. Iserles, and S. Macnamara, *Positivity-preserving methods for population models*, first posted 2021-02-16, arXiv:2102.08242; revised journal title *Positivity-preserving methods for ordinary differential equations*, ESAIM: M2AN 56 (2022), 1843–1870. https://arxiv.org/abs/2102.08242
- K. Gourgoulias, M. A. Katsoulakis, and L. Rey-Bellet, *Information metrics for long-time errors in splitting schemes for stochastic dynamics and parallel KMC*, 2015, arXiv:1511.08240. https://arxiv.org/abs/1511.08240
- R. L. Speth, W. H. Green, S. MacNamara, and G. Strang, *Balanced splitting and rebalanced splitting*, SIAM J. Numer. Anal. 51 (2013), 3084–3105, DOI:10.1137/120878641. https://dspace.mit.edu/entities/publication/5a1a78e8-89e8-4ce0-b7d2-35e02fec5fa1
