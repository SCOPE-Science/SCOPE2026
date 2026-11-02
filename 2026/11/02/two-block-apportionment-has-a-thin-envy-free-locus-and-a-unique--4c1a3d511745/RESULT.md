# Two-block apportionment has a thin envy-free locus and a unique four-party minimum-envy lottery

## Finding

Consider quota-respecting, ex-ante proportional randomized rounding of a fixed integer house size, with exactly two distinct integer lower quotas. Within each of the two equal-floor blocks, sort fractional quota residues in nondecreasing order. The following linked statements hold:

1. For **any two block sizes**, there is an envy-free lottery if and only if the uniquely determined distributions of the numbers rounded up in the two blocks are reflections of one another around the prescribed total number of round-ups. If it exists, the envy-free lottery is unique. If at least three parties are present and exactly two floor blocks occur, the set of envy-free residue vectors has Lebesgue measure zero in every full-dimensional fixed-floor quota chamber.
2. For the **smallest balanced multi-floor configuration**, four parties in two blocks of two and precisely two seats to round up, the unique lottery minimizing the expected number of envious ordered pairs also uniquely minimizes the probability of any envy. If the ordered residues are \(0\le a\le b<1\) and \(0\le c\le d<1\), with \(a+b+c+d=2\), then both minima equal

\[
\boxed{\left|b+c-1\right|}.
\]

Thus exact zero envy occurs in this four-party chamber precisely on \(b+c=1\). Its off-boundary minimum is a linear, exactly measurable envy cost rather than merely an infeasibility decision.

## Assumptions and scope

There are \(N=m+t\ge3\) labeled parties, two **distinct** nonnegative integer lower quotas, one used by exactly \(m\ge1\) parties and the other by exactly \(t\ge1\) parties, and a prescribed integer house size \(H\). Each party's standard quota is its lower quota plus a fractional residue in \([0,1)\). The sum of all residues is an integer \(k\), with \(1\le k\le N-1\). The residues of each block are ordered nondecreasingly, using a fixed index tie-break if necessary. Every realization chooses precisely \(k\) parties to round up, each by exactly one seat. Every party's marginal probability of being rounded up must equal its residue.

An ordered envy pair consists of a party with at least as large a standard quota but fewer realized seats than another. Under the fixed tie-break convention of the cited model, an inversion occurs in a block whenever a lower-ranked party is rounded up but a higher-ranked party of the *same* lower quota is not. Parties in different floor blocks cannot produce a strict seat inversion. We count such ordered pairs; in the four-party case the count is between zero and two. The event of any envy means the count is positive.

For the measure-zero assertion, vary residues continuously within an open, full-dimensional fixed-floor and within-block ordering chamber of the hyperplane \(\sum_i r_i=k\), dimension \(N-1\). No probability assertion is made for finite integer-vote samples or for conditioning on a lower-dimensional quota distribution.

## Proof

**Block-count marginal law.** Let a block contain \(s\) parties with residues \(0\le r_1\le\cdots\le r_s<1\). Zero envy in a deterministic outcome forces the rounded-up set to be a suffix: the \(L\) parties of highest residue for some \(L\in\{0,\ldots,s\}\). If the lottery is envy-free, ex-ante proportionality forces

\[
\Pr(L=0)=1-r_s,\qquad
\Pr(L=\ell)=r_{s-\ell+1}-r_{s-\ell}\quad(1\le\ell\le s),
\]

where \(r_0=0\). This follows from \(\Pr(L\ge\ell)=r_{s-\ell+1}\) by subtraction. Denote this completely determined law by \(P_s(\ell)\), extended as zero outside its support. It is nonnegative, sums to one, and has mean \(\sum_{j=1}^s r_j\).

**Two-block reflection and uniqueness.** Write the block round-up counts as \(L_A,L_B\). Since every realization selects exactly \(k\) extra seats, \(L_A+L_B=k\) almost surely. Hence \(P_m(\ell)=P_t(k-\ell)\) for every integer \(\ell\). Conversely, if all these equalities hold, choose \(L_A=\ell\) with probability \(P_m(\ell)\), put \(L_B=k-\ell\), and select the corresponding highest-residue suffix in each block. This is an envy-free quota-respecting and ex-ante proportional lottery. There is no choice in the law of \(L_A\), and the deterministic selected set is uniquely determined by the pair of block counts; the envy-free lottery is therefore unique.

**Geometric consequence.** The only allowed count pairs for a zero-envy lottery are \((\ell,k-\ell)\) with

\[
\max(0,k-t)\le\ell\le\min(m,k).
\]

If \(s\) is the number of such integer pairs, the simplex of lotteries supported on these outcomes has dimension at most \(s-1\le\min(m,t)\le N-2\). The map from lottery weights to the \(N\) residues is affine. Its image therefore has dimension at most \(N-2\), whereas the full quota hyperplane has dimension \(N-1\). Consequently the zero-envy set has relative Lebesgue measure zero in every full-dimensional fixed-floor chamber.

**Sharp four-party optimizer.** Label the parties \(1,2\) (first block, residues \(a,b\)) and \(3,4\) (second block, residues \(c,d\)). Let \(p_{ij}\) be the probability that exactly parties \(i,j\) get the two extra seats. Every feasible lottery satisfies

\[
\begin{aligned}
a&=p_{12}+p_{13}+p_{14},\\
b&=p_{12}+p_{23}+p_{24},\\
c&=p_{13}+p_{23}+p_{34},\\
d&=p_{14}+p_{24}+p_{34},
\end{aligned}
\qquad \sum_{i<j}p_{ij}=1.
\]

Subtracting the normalization gives the exact, lottery-independent identity

\[
 b+c-1=p_{23}-p_{14}.
\]

The expected number of within-block envy pairs equals \(2p_{13}+p_{14}+p_{23}\), since selecting \(\{1,3\}\) creates two inversions. The probability of any envy equals \(p_{13}+p_{14}+p_{23}\). Both are bounded below by \(\lvert p_{23}-p_{14}\rvert=\lvert b+c-1\rvert\).

For \(b+c\ge1\), set

\[
(p_{12},p_{13},p_{14},p_{23},p_{24},p_{34})
=(a,0,0,b+c-1,1-a-c,1-b).
\]

For \(b+c\le1\), set

\[
(p_{12},p_{13},p_{14},p_{23},p_{24},p_{34})
=(1-d,0,1-b-c,0,b+d-1,c).
\]

All components are nonnegative: \(a+c\le(b+a+c+d)/2=1\), and similarly \(b+d\ge1\); the remaining inequalities are immediate from the branch condition and \(0\le r_i<1\). Direct substitution verifies normalization and every prescribed marginal. In either branch \(p_{13}=0\) and one of \(p_{14},p_{23}\) is zero, attaining both lower bounds.

For equality in either lower bound, necessarily \(p_{13}=0\) and \(\min(p_{14},p_{23})=0\). The identity \(p_{23}-p_{14}=b+c-1\) then fixes both. The four marginal equations uniquely determine \(p_{12},p_{24},p_{34}\), proving **uniqueness** of the minimizer for either objective, including the zero-envy case.

## Verification

The standalone `check_exact.py` uses only Python's standard library, rational arithmetic and independent enumeration of every basic feasible solution of the six-outcome linear program. It tests all nondecreasing four-residue tuples with denominators \(6\), \(12\), and \(18\), sum exactly \(2\), including rational boundary cases. For each tuple it separately verifies both objectives, the explicit optimizer, every marginal and the predicted unique optimal value. The check covers \(1{,}398\) rational profiles. The proof above is valid for all real residues and all stated block sizes; finite tests are not a proof of an infinite assertion.

A strictly ordered example with floors \((0,0,1,1)\) and residues \((3/20,17/20,1/4,3/4)\) has house size \(4\). Its unique optimal lottery has weights \((3/20,0,0,1/10,3/5,3/20)\) on \((12,13,14,23,24,34)\), and its exact minimum expected envy and probability of any envy are both \(1/10\).

## Relationship to prior work

La Commare, Tucker-Foltz and Verdugo (2026), *Envy-free Randomized Apportionment*, introduce the quota-respecting ex-ante proportional model, within-block envy, a network-flow feasibility criterion (Proposition 4.2), and a general optimization LP (Theorem 4.3). Their Section 4.2 includes a single compatible four-party two-block worked example with residues \((0.4,0.8)\) and \((0.2,0.6)\). The new characterization gives the explicit general two-block reflection test, proves generic nullity of the zero-envy locus, and yields the symbolic **unique** minimum-envy lottery and exact minimum for every admissible four-party two-by-two input, including incompatible inputs. Their general LP can solve those instances numerically; its existence is acknowledged and no new polynomial-time solvability claim is made.

Earlier work on randomized quota rounding, including Correa et al. (2024), studies monotonicity and dependence properties rather than this two-block optimal-environment phase boundary.

## Limitations

The structural criterion assumes exactly two distinct lower-quota blocks and strict quota/ex-ante proportionality. It does not characterize instances with three or more blocks, nor distributions with total round-ups outside the stated range. The exact minimum formula and uniqueness of the positive-envy optimizer are stated only for two blocks of size two and two round-ups, not for arbitrary block cardinalities. The measure-zero conclusion is relative to continuous full-dimensional quota chambers and does not mean envy-free solutions are impossible at rational or integer voting profiles. Equal residues use the cited model's fixed index tie-break; a different policy for exact population ties changes the definition of envy. No claim of independent validation or of exhaustive historical priority is made.

## References

- Francesco La Commare, Jamie Tucker-Foltz, Victor Verdugo, *Envy-free Randomized Apportionment*, arXiv:2610.24217v1, first public October 16, 2026. https://arxiv.org/pdf/2610.24217
- José Correa, Paul Gölz, Ulrike Schmidt-Kraepelin, Jamie Tucker-Foltz, Víctor Verdugo, *Monotone Randomized Apportionment*, arXiv:2405.03687, 2024. https://arxiv.org/abs/2405.03687
