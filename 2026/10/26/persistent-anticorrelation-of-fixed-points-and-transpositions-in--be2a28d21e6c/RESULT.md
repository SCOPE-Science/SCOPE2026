# Persistent anticorrelation of fixed points and transpositions in a random transposition walk

## Finding

Start a random walk at the identity permutation on \(n\) labeled elements. At each integer step choose uniformly from the \(\binom n2\) unordered pairs of distinct labels and transpose that pair, independently between steps. Let \(F_t\) count fixed points (one-cycles) and \(Q_t\) count disjoint cycles of length two after \(t\) steps.

**Theorem.** For every integer \(n\ge6\) and every integer \(t\ge0\), define
\[
a=\frac{(n-3)(n-4)}{n(n-1)},\qquad
b=\frac{(n-3)(n-5)}{(n-1)^2},\qquad
c=\frac{n-7}{n-1}.
\]
Then
\[
\operatorname{Cov}(F_t,Q_t)
=\frac{(n-1)(n-2)}{12}
\left[-2n a^t+3(n-1)b^t-(n-3)c^t\right]. \tag{1}
\]
Consequently, \(\operatorname{Cov}(F_t,Q_t)=0\) at \(t=0,1\), and
\[
\operatorname{Cov}(F_t,Q_t)<0\qquad\text{for every integer }t\ge2.
\]
Here a zero eigenvalue raised to its zeroth power means \(0^0=1\), as required by the identity operator at zero steps. The threshold \(n=6\) is sharp in the following sense: \(\operatorname{Cov}(F_3,Q_3)=6/25>0\) for \(n=5\) under precisely the same transposition rule.

## Assumptions and scope

The walk is discrete time, starts at the identity, and draws a uniformly random **nonidentity** transposition each step. A shuffle that permits selecting the same label twice, or a continuous-time Poisson clock, has different exact formulas and is not covered by (1). A transposition acts on the current permutation by composition; since the increments are sampled uniformly from a conjugacy class, left and right composition produce the same class-function moments. All covariance statements refer to the same time \(t\), not two different times. The primary setting is the symmetric group with \(n\ge6\).

## Proof

Write \(\chi_\lambda\) for the irreducible character indexed by partition \(\lambda\vdash n\) and \(d_\lambda\) for its dimension. Abbreviate the five distinct partitions
\[
V=(n-1,1),\quad W=(n-2,2),\quad U=(n-2,1,1),\quad X=(n-3,3),\quad Y=(n-3,1,1,1).
\]
They are valid, distinct partitions for all \(n\ge6\).

**Character reduction.** The natural permutation representation gives \(F=1+\chi_V\). Counting unordered pairs of labels fixed as a set, then separating pairs fixed pointwise from two-cycles, gives
\[
2Q=1+\chi_W-\chi_U.
\]
Indeed, the character of the action on unordered pairs is \(\binom F2+Q=1+\chi_V+\chi_W\); the character of the exterior square of the natural permutation representation is \(\binom F2-Q=\chi_V+\chi_U\), and subtraction yields the displayed identity. Equivalently, the same equality follows from the standard character polynomials of these two partitions.

We need the nontrivial product \(FQ\). Multiplication by the natural permutation character \(F\) is induction followed by restriction from \(S_n\) to \(S_{n-1}\). The ordinary remove-one-box/add-one-box branching rule gives
\[
\operatorname{Ind}\operatorname{Res}(\chi_W)=2\chi_W+\chi_X+\chi_{(n-3,2,1)}+\chi_V+\chi_U,
\]
\[
\operatorname{Ind}\operatorname{Res}(\chi_U)=2\chi_U+\chi_{(n-3,2,1)}+\chi_Y+\chi_V+\chi_W.
\]
Subtracting these two identities, and multiplying \(2Q\) by \(F\), yields the exact mixed-character identity
\[
2FQ=1+\chi_V+\chi_W-\chi_U+\chi_X-\chi_Y. \tag{2}
\]
The expansions, including the shared intermediate partition \((n-3,2,1)\), remain valid at \(n=6\).

**One-step spectral eigenvalues.** The uniform average over all transpositions is central. Schur's lemma and the Frobenius transposition-ratio formula give, for every irreducible character,
\[
\mathbb E[\chi_\lambda(\pi_t)]=d_\lambda\rho_\lambda^t,
\qquad\rho_\lambda=\frac{\sum_{i\ge1}\lambda_i(\lambda_i-2i+1)}{n(n-1)}.
\]
The hook-length formula and these ratios give the following complete table:

| Partition | Dimension | Eigenvalue |
| --- | --- | --- |
| \(V\) | \(n-1\) | \((n-3)/(n-1)\) |
| \(W\) | \(n(n-3)/2\) | \((n-4)/n\) |
| \(U\) | \((n-1)(n-2)/2\) | \((n-5)/(n-1)\) |
| \(X\) | \(n(n-1)(n-5)/6\) | \(a\) |
| \(Y\) | \((n-1)(n-2)(n-3)/6\) | \(c\) |

Notice that \(\rho_V\rho_W=\rho_X=a\) and \(\rho_V\rho_U=b\). From \(F=1+\chi_V\) and \(2Q=1+\chi_W-\chi_U\), calculate \(\mathbb E F\) and \(\mathbb E Q\). From (2), calculate \(\mathbb E(FQ)\). Subtracting their product cancels the constant and three single-character terms, leaving
\[
\operatorname{Cov}(F_t,Q_t)
=\tfrac12[(d_X-d_Vd_W)a^t+d_Vd_Ub^t-d_Yc^t],
\]
which simplifies to (1).

**Strict sign and sharpness.** A direct rational identity is
\[
3(n-1)b=2na+(n-3)c. \tag{3}
\]
For \(n\ge7\), \(0\le c<b<a<1\), and the weights \(2n/[3(n-1)]\) and \((n-3)/[3(n-1)]\) are strictly positive and sum to one. Thus (3) expresses \(b\) as a proper convex combination of two distinct endpoints. For every integer \(t\ge2\), strict convexity of \(x\mapsto x^t\) on \([0,1]\) implies
\[
3(n-1)b^t<2na^t+(n-3)c^t,
\]
proving (1) is negative.

For the remaining case \(n=6\), \(a=1/5\), \(b=3/25\) and \(c=-1/5\). The bracket in (1) becomes \(-15a^t+15b^t<0\) for every even \(t\ge2\), and \(-9a^t+15b^t<0\) for every odd \(t\ge3\), since \(b/a=3/5\) and \((3/5)^t<3/5\). Equation (3) or the direct formula gives zero at \(t=0,1\). The claimed \(n=5\) counterexample follows by exact enumeration of the \(\binom52^3\) three-step transposition sequences, giving \(6/25\). This completes the proof.

## Verification

The standalone standard-library program `verify.py` performs independent exact-integer enumeration of complete Markov-walk distributions for \(n=5,6,7\) through respectively \(4,7,7\) steps. It computes mixed moments and covariance as rational numbers, compares every \(n\ge6\) case to (1), and verifies the \(n=5,t=3\) boundary example. It independently implements the hook-length dimension formula and Frobenius transposition ratio, checking the five representation pairs for every \(6\le n\le40\). A further grid of exact-rational formulas tests \(2\le t\le20\) for each of those \(n\). The stored output `checks.txt` records the results.

The finite checks are diagnostics; the proof of the unbounded parameter range is the branching calculation and strict-convexity argument above.

## Relationship to prior work

Diaconis and Shahshahani [3] establish the central random-transposition character/Fourier framework and analyze mixing, using a *lazy* version with identity steps, rather than the non-lazy walk here. Alon and Kozma [1] establish exact irreducible-character decompositions of individual cycle-length count functions in interchange processes. Berestycki and Kozma [2] calculate exact expectations of individual cycle-length counts and their transitions in a continuous-time process. Bernstein [4] addresses mixing and character eigenvalues for a different random-involution walk. These tools motivate the present calculation, but the inspected statements do not assert or imply the all-step negative sign of the mixed \(F_t,Q_t\) covariance; deriving that sign additionally requires the specific mixed-character reduction and strict Jensen inequality (3). Conversely (1) supplies no general joint law of all cycle counts, no negative association of the full cycle vector, and no general result for other random walks.

## Limitations

The strict sign is proved only for the stated non-lazy discrete-time uniform-transposition walk for \(n\ge6\). Small support can behave differently; at \(n=5,t=3\) the covariance is positive. Equation (1) does not classify conditional dependence, independence, or joint distributions, and does not extend automatically to lazy or continuous-time random-transposition dynamics. Historical priority beyond the inspected sources remains open to independent assessment, particularly because character methods are classical and could have been used in older unpublished calculations.

## References

1. G. Alon and G. Kozma, “The probability of long cycles in interchange processes,” arXiv:1009.3723v1 (public 20 September 2010), Theorem 3. https://arxiv.org/abs/1009.3723
2. N. Berestycki and G. Kozma, “Cycle structure of the interchange process and representation theory,” arXiv:1205.4753v1 (21 May 2012), Theorem 1 and §2.1. https://arxiv.org/abs/1205.4753
3. P. Diaconis and M. Shahshahani, “Generating a random permutation with random transpositions,” Z. Wahrscheinlichkeitstheorie verw. Gebiete 57 (1981), 159–179, §2–4. https://doi.org/10.1007/BF00535487
4. M. Bernstein, “A random walk on the symmetric group generated by random involutions,” arXiv:1606.09588v1 (30 June 2016), §1–3. https://arxiv.org/abs/1606.09588
