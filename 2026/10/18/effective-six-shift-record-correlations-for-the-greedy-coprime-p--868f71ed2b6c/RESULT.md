# Effective six-shift record correlations for the greedy coprime permutation

## Finding

Let \(R\) denote the set of record values of the greedy permutation \(f(1)=1\), \(f(2)=3\), \(f(j)\) the least unused positive integer coprime to \(f(j-1)\). For every fixed integer \(t\), the density
\[
Q(t)=\lim_{X\to\infty}\frac1X\#\{r\in\mathbb Z:1\le r\le X,\ r\in R,\ r+t\in R\}
\]
exists and admits a convergent sequence of explicitly computable rational approximations with certified error. At shift six,
\[
\boxed{\frac{1564931}{6096948}<Q(6)\le\frac{414944}{1616615}},
\]
and \(Q(6)>1/4>\kappa^2\), where \(\kappa\) is the ordinary density of \(R\). In particular, the centered six-shift record correlation is strictly positive.

## Assumptions and scope

Records are the turning-point values specified in Basistha--Ionascu, equivalent away from finitely many initial terms to the increasing sequence OEIS A261271. The initial record values from five onwards satisfy the independent recurrence: start \(r=5\); if \(q\) is the least prime not dividing \(r-1\), the next record is \(r-1+q\). An initial discrepancy among finitely many records never affects a natural density. The shift \(t\) is any fixed integer; the quantitative six-shift bound refers to \(t=6\).

Let \(p_1=2,p_2=3,\ldots\) enumerate primes, \(P_n=\prod_{j=1}^{n}p_j\), and for \(n\ge3\) let \(A_n\) consist of the residues modulo \(P_n\) occupied by record values in \([p_{n+1},P_n+1]\). Define \(C_n(t)=\#\{a\in A_n:(a+t)\bmod P_n\in A_n\}\). The one-point record density \(\kappa\) is known to exist; our new assertion concerns joint membership at a shifted pair.

## Proof

**Primorial approximation.** The underlying record recursion implies the translation theorem in Basistha--Ionascu, Theorems 2.8--2.9: within consecutive \(P_n\)-blocks up to the next primorial scale, record indicators repeat on the residue pattern \(A_n\), except for the initial record values between the next consecutive primes. To check the key step directly, observe that for an integer \(u\) in a copied block with \(0<u<P_n\), some prime \(p_j\le p_n\) fails to divide \(u\). Its *least* such prime is unchanged when \(u\) is replaced by \(u+kP_n\). At block boundaries \(u=kP_n\) with \(1\le k<p_{n+1}\), the least nondividing prime is \(p_{n+1}\), again independent of \(k\). Consequently the record recursion repeats the preceding block and the next-scale pattern is obtained by repeating \(A_n\) \(p_{n+1}\) times and deleting precisely those \(s_{n+1}\) initial records in \([p_{n+1},p_{n+2})\). In particular, \(A_{n+1}\) is a subset of the lift of \(A_n\); all sufficiently large genuine record values lie in the periodic residue class set \(A_n\).

Write \(\kappa_n=|A_n|/P_n\). The block argument yields
\[
\kappa_n-\kappa=\sum_{j=n+1}^{\infty}\frac{s_j}{P_j},\qquad s_j=\#(R\cap[p_j,p_{j+1})).
\]
Indeed, the same formula first holds for finite stages by telescoping the exact deleted counts, and the limiting one-point density is established by the primorial-copying theorem. For \(j\ge4\), all records in \([p_j,p_{j+1})\) are odd, so \(s_j\le(p_{j+1}-p_j)/2\). Bertrand's postulate gives \(p_{j+1}<2p_j\), hence
\[
0\le\kappa_n-\kappa<\frac12\sum_{j=n+1}^{\infty}\frac{1}{P_{j-1}}
\le\frac{p_{n+1}}{2(p_{n+1}-1)P_n}.
\]

**Two-point limit.** Let \(B_n\) be the periodic subset of positive integers whose residue lies in \(A_n\). Past a finite initial segment, \(R\subseteq B_n\). The symmetric difference between the indicator of \(R\) and that of \(B_n\) has density exactly \(\kappa_n-\kappa\). For any fixed integer \(t\), the indicators of the pair events at \((r,r+t)\) can disagree only if at least one endpoint is in this difference. The union bound therefore gives, for the limsup and liminf of the pair frequency,
\[
0\le\frac{C_n(t)}{P_n}-\limsup_{X\to\infty}Q_X(t)
\le\frac{C_n(t)}{P_n}-\liminf_{X\to\infty}Q_X(t)
\le2(\kappa_n-\kappa).
\]
As the right side tends to zero, the upper and lower limits coincide and define \(Q(t)\). Thus
\[
0\le\frac{C_n(t)}{P_n}-Q(t)<\frac{p_{n+1}}{(p_{n+1}-1)P_n}.
\]
This holds for each fixed positive, negative, or zero shift.

**Certified six-shift value and covariance.** Exact recurrence enumeration (reproduced by `verify.py`) at \(n=8\) yields
\[
P_8=9699690,\quad |A_8|=2859176,\quad C_8(6)=2489664,\quad p_9=23.
\]
Substituting the error bound gives precisely
\[
\frac{2489664}{9699690}-\frac{23}{22\cdot9699690}<Q(6)\le\frac{2489664}{9699690},
\]
which reduces to the stated enclosure. For \(n=3\), the record residue set is \(A_3=\{1,7,11,13,17,19,23,25,29\}\), hence \(\kappa\le9/30=3/10\). The lower bound for \(Q(6)\) exceeds \(1/4\), while \(\kappa^2\le9/100\). Therefore the six-shift covariance \(Q(6)-\kappa^2\) is strictly positive.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The script generates records independently by their least-nondividing-prime recurrence, forms \(A_n\) for \(3\le n\le8\), checks the exact cardinalities and six-shift pair counts, tests the nested-residue assertion at these finite stages, and checks the rational enclosure. It finishes with `VERIFY_OK`. The mathematical proof of the infinite density and strict error bound is the argument above, not the finite run.

## Relationship to prior work

Basistha and Ionascu, *A special sequence and primorial numbers*, arXiv:2302.02838 (first public version 6 February 2023), establish the greedy record recursion, block translation, and one-point density. The present finding builds on those theorems and concerns simultaneous occupancy at two positions. OEIS A261271 provides the record sequence and its initial values. Residue-class one-point densities distinguish different arithmetic progressions, but do not state the two-point joint density or its strictly positive centered six-shift correlation. The shift six is distinguished by the record support in residues \(1\) and \(5\) modulo six, rather than being an arbitrary selection.

## Limitations

No closed finite expression is claimed for \(Q(6)\); its value is specified by a convergent finite-residue procedure with rigorous rational bounds. The procedure is not claimed computationally optimal, and the bound is not a determination of other shifts' exact values. Only self-review has been performed; no independent mathematical audit is implied.

## References

1. A. K. Basistha and E. J. Ionascu, *A special sequence and primorial numbers*, arXiv:2302.02838, Theorems 2.8, 2.9, 2.12 (first version 2023-02-06): https://arxiv.org/abs/2302.02838 .
2. OEIS Foundation, A261271, *Smallest prime not dividing the previous term minus one*: https://oeis.org/A261271 .
