# Balanced-window law and exact three-approval tie counts for proportional approval voting

## Finding

There are \(n\ge3\) labeled candidates indexed by \(\mathbb Z/n\mathbb Z\) and exactly \(n\) voters. Voter \(i\) approves the consecutive cyclic window \(A_i=\{i,i+1,\ldots,i+d-1\}\), with a common length \(1\le d\le n\). A committee \(W\) contains \(k\) distinct candidates, \(0\le k\le n\). For every strictly increasing, strictly discretely concave Thiele satisfaction function \(f\) through \(d\), the complete set of winning committees is independent of the particular function:

\[
W\text{ wins}\quad\Longleftrightarrow\quad
|W\cap A_i|\in\{q,q+1\}\quad\text{for every }i,
\qquad q=\left\lfloor\frac{dk}{n}\right\rfloor.
\]

With \(r=dk-nq\), the optimum aggregate satisfaction is exactly
\[
(n-r)f(q)+rf(q+1),
\]
where the term multiplied by \(r=0\) is omitted. In particular the criterion and the full optimal set hold for Proportional Approval Voting (PAV), \(f(j)=H_j=\sum_{h=1}^j1/h\) and \(H_0=0\).

When \(d=3\), the number \(N(n,k)\) of distinct **labeled** winning committees has the following closed form. Put \(t=\min(k,n-k)\):

\[
N(n,k)=
\begin{cases}
1,&k=0\text{ or }k=n,\\
\displaystyle\frac{n}{n-2t}\binom{n-2t}{t},&0<3t\le n,\\
\displaystyle\sum_{a=\max(\lceil k/2\rceil,\lceil(n-k)/2\rceil)}^{\min(k,n-k)}\frac{n}{a}\binom{a}{k-a}\binom{a}{n-k-a},&3t>n.
\end{cases}
\]

For \(n=12\), \(d=3\), and \(k=6\), the PAV optimum is \(6H_1+6H_2=15\), attained by exactly \(174\) distinct labeled committees, not just by the evenly spaced ones. More generally, for \(n=6m\) and \(k=3m\), the term \(a=2m\) in the formula alone supplies at least \(3\binom{2m}{m}^2\) different optimal committees, an exponential lower bound on tie multiplicity. This gives an exact many-way tie in a structurally symmetric election.

## Assumptions and scope

All candidates and voters are labeled; indices and windows wrap around the cycle. Each of the \(n\) voters occurs once. The common approval window length is \(d\). The score is \(S_f(W)=\sum_{i=0}^{n-1}f(|W\cap A_i|)\). Assume \(f(0)=0\) and the increments \(\Delta_j=f(j)-f(j-1)\) satisfy \(\Delta_1>\Delta_2>\cdots>\Delta_d>0\). For \(d=1\), this simply says \(\Delta_1>0\). PAV satisfies all assumptions. We allow \(k=0\) and \(k=n\) as algebraic boundary cases; the usual nonempty PAV committee model corresponds to \(1\le k\le n\).

Distinct cyclic rotations of a committee are counted separately whenever they occupy different labeled candidates. No quotient by rotational or reflection symmetry is taken.

## Proof

**1. A sharp discrete concavity bound.** Set \(b_i=|W\cap A_i|\). Each selected candidate lies in exactly \(d\) windows, so
\[
\sum_{i=0}^{n-1}b_i=dk=nq+r,\qquad 0\le r<n.
\]
For integer arguments, strict decrease of the successive increments implies that whenever \(a\ge b+2\),
\[
f(a)+f(b)<f(a-1)+f(b+1).
\]
Repeatedly transferring one unit from a larger count to a smaller count shows
\[
\sum_i f(b_i)\le(n-r)f(q)+rf(q+1),
\]
with equality **if and only if** every \(b_i\) belongs to \(\{q,q+1\}\). The strict inequality makes the equality classification exact, rather than merely sufficient.

**2. Attainability for every admissible triple.** Define a binary mechanical word on all integers by
\[
x_j=\left\lfloor\frac{(j+1)k}{n}\right\rfloor-\left\lfloor\frac{jk}{n}\right\rfloor.
\]
Because \(0\le k\le n\), every \(x_j\in\{0,1\}\). Also \(x_{j+n}=x_j\) and \(\sum_{j=0}^{n-1}x_j=k\). Taking exactly those labeled candidates \(j\bmod n\) with \(x_j=1\), its cyclic length-\(d\) window count equals
\[
\sum_{h=0}^{d-1}x_{i+h}=\left\lfloor\frac{(i+d)k}{n}\right\rfloor-\left\lfloor\frac{ik}{n}\right\rfloor,
\]
which is either \(q\) or \(q+1\). Thus the upper bound is always attained. Combining this construction with strictness proves the claimed **if and only if** statement and independence from the particular strictly concave Thiele weights.

**3. Exact count for three approvals: sparse case.** Let \(d=3\) and \(0<3t\le n\). If \(k\le n/3\), then every winning length-three window has zero or one selected candidate; in the cyclic binary word, any two ones must have at least two zeros between them. If \(k\ge2n/3\), the complement word has the identical property for its \(t=n-k\) zeros. We can count either case by singling out each of the \(t\) minority symbols. The \(t\) ordered intervening majority gaps each contain at least two symbols; the remaining \(n-3t\) symbols can be distributed in
\[
\binom{n-2t-1}{t-1}
\]
ways. There are \(n\) choices for a labeled starting minority position; every binary committee is counted exactly \(t\) times by the choice of distinguished minority position. Therefore
\[
N(n,k)=\frac nt\binom{n-2t-1}{t-1}=\frac{n}{n-2t}\binom{n-2t}{t}.
\]

**4. Exact count for three approvals: middle case.** When \(n/3<k<2n/3\), the balanced-window criterion becomes the simultaneous absence of length-three all-zero and all-one windows. Equivalently, every cyclic run of zeros and every cyclic run of ones has length either one or two. Let \(a\) denote the number of runs of ones, which also equals the number of runs of zeros. The \(a\) one-runs cover \(k\) symbols, and the \(a\) zero-runs cover \(n-k\), so
\[
\max(\lceil k/2\rceil,\lceil(n-k)/2\rceil)\le a\le\min(k,n-k).
\]
Each of the \(a\) one-run lengths is one or two, with \(k-a\) of them two, giving \(\binom{a}{k-a}\) ordered run-length tuples. Similarly, the zero-run lengths give \(\binom{a}{n-k-a}\) tuples. For each ordered pair of tuples there are \(n\) choices of the labeled start position of a one-run. Every labeled committee is counted exactly \(a\) times because it has \(a\) one-run starts. Hence there are
\[
\frac na\binom{a}{k-a}\binom{a}{n-k-a}
\]
committees for the specified \(a\). Summing over the possible values of \(a\) proves the middle-case formula. All counts are integers by the counting argument. The cases \(k=0,n\) each give one committee.

For the example \(n=12,k=6\), the permitted run counts \(a=3,4,5,6\) contribute respectively \(4,108,60,2\), summing to \(174\).

## Verification

The supplied standalone standard-library Python script `verify.py` implements the PAV score with **exact integer scaling** and independently tests all candidate-subset masks for every \(3\le n\le12\), every \(1\le d\le n\), and every \(0\le k\le n\). It compares the actual score to the predicted upper bound, checks the balanced-window equality criterion, and compares the \(d=3\) optimum counts against the closed form. It separately checks \(d=3\) for every \(13\le n\le18\), every size and all candidate subsets, using integer multiples of the first three harmonic numbers. The executed run reported `VERIFY_OK enumerated_binary_committees 606200 domain_first 3 domain_last 18`. These are finite corroborating checks; the four analytical proof steps establish the infinite-domain statements.

To reproduce: run `python3 verify.py` with Python 3.9+ from the directory containing this document and the standalone script. No internet, data files, numerical libraries, or external solvers are required.

## Relationship to prior work

Ai (2026) establishes complexity classifications for membership, uniqueness and counting in **general** PAV elections, motivating exact descriptions of entire winner sets. Janeczko and Faliszewski (2023) investigate the hardness of counting tied approval-winning committees. Lassota and Sornat (2026) and Avramidis et al. (2026) provide winner-determination algorithms on structured interval domains. Those algorithmic and complexity statements do not directly give the all-optima cyclic-window equality criterion, weight-independence, or the closed three-approval tie-count formula. Elementary discrete concavity and circular run counting are classical proof tools and are not claimed as new techniques.

The cited work was compared by mathematical statement and scope. The present profile has one voter at every cyclic position and approval sets of **one fixed length**; in particular it is much narrower than arbitrary circular-arc elections. Earlier unindexed treatment of this highly symmetric case remains a possible priority risk.

## Limitations

The theorem does not assert any winner-set classification for arbitrary voter multiplicities, nonuniform approval-window lengths, general circle-interval preferences or merely weakly concave weights (where additional maximizers can occur). The three-approval counting formula applies only to windows of length three, while the winning-set characterization and score formula apply to every length. The finite checker cannot certify the full mathematical statement independently. No independent scientific audit has been performed.

## References

1. Y. Ai, *The Complexity of Membership, Uniqueness, and Counting for Optimal Proportional Approval Voting Committees* (first public September 8, 2026). https://arxiv.org/abs/2609.08884
2. A. Lassota and K. Sornat, *Algorithms for Structured Elections under Thiele Voting Rules* (July 30, 2026). https://arxiv.org/abs/2607.28575
3. Ł. Janeczko and P. Faliszewski, *Ties in Multiwinner Approval Voting* (May 2, 2023). https://arxiv.org/abs/2305.01769
4. D. Avramidis, A. Lassota, U. Schmidt-Kraepelin and A. Vetta, *Computing Thiele Rules on Interval Elections and their Generalizations* (May 4, 2026). https://arxiv.org/abs/2605.03067
5. P. Manurangsi and K. Sornat, *Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences* (April 7, 2026). https://arxiv.org/abs/2604.05953
