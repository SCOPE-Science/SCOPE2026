# A sharp unrepresented-voter bound for three-deletion reverse sequential PAV

## Finding

Consider reverse sequential Proportional Approval Voting (RevSeqPAV) with exactly three deletions: an approval election with \(k\ge 2\) winning seats and exactly \(k+3\) candidates. Write \(W\) for a possible final \(k\)-member committee. For every unelected candidate \(c\), let
\[
U(c,W)=\bigl|\{i:c\in A_i,\ A_i\cap W=\varnothing\}\bigr|.
\]
For every nonempty electorate of \(n\) voters, **the sharp bound, allowing any legitimate tie-breaking, is**
\[
\boxed{\max_{c\notin W}\frac{U(c,W)}{n}\le B_k:=\frac{2(2k+1)}{(3k+1)(k+2)}.}
\]
For each integer \(k\ge2\) an integer-weighted approval profile and a legitimate tie-breaking attain equality. Consequently **every** such outcome satisfies justified representation (JR) for \(2\le k\le5\); this is best possible in seat count because for \(k=6\) there is a nine-candidate, 252-voter profile on which **every** tie-breaking follows three strict deletion choices and violates JR. For every \(k\ge6\), a violating outcome exists with some legitimate tie-breaking. The single-seat case also satisfies JR, independently of this quantitative formula.

## Assumptions and scope

An approval ballot \(A_i\) is any subset (possibly empty) of the labeled candidate set. The PAV score of \(S\) is \(\sum_i H_{|A_i\cap S|}\), with \(H_0=0\) and \(H_t=\sum_{j=1}^t 1/j\) for positive integers \(t\). RevSeqPAV repeatedly removes a candidate of *minimum* score loss until \(k\) remain. If several candidates tie, any tied deletion is legitimate. All statements about the upper bound hold for **every** such deletion history; equality is an existence statement. JR means that if at least \(n/k\) voters have a commonly approved candidate, then some member of that group approves an elected candidate.

In the remainder, relabel the deleted candidates in temporal order \(d_0,d_1,d_2\), and let the other \(k\) candidates be \(W\). At deletion stage \(j\in\{0,1,2\}\), a voter's ballot has the binary pattern \(r\in\{0,\ldots,7\}\) for \(d_0,d_1,d_2\), and it approves \(b\in\{0,\ldots,k\}\) winners. Here \(r_s\in\{0,1\}\) is bit \(s\) of \(r\). Set \(t_j=b+\sum_{s=j}^2r_s\). Define
\[
u_j(s)=\begin{cases}r_s/t_j,&t_j>0,\\0,&t_j=0,\end{cases}
\quad
u_j(w)=\begin{cases}b/(kt_j),&t_j>0,\\0,&t_j=0.\end{cases}
\]
Here \(u_j(w)\) is the voter's contribution to the *average* current marginal loss over elected winners, not a single voter's utility. Summing \(u_j(s)\) over all voters equals the marginal score loss of \(d_s\); summing \(u_j(w)\) equals the average loss across \(W\). We abbreviate the five per-ballot differences
\[
\begin{aligned}
g_{01}&=u_0(0)-u_0(1),&g_{02}&=u_0(0)-u_0(2),\\
g_{1w}&=u_1(1)-u_1(w),&g_{12}&=u_1(1)-u_1(2),\\
g_{2w}&=u_2(2)-u_2(w).
\end{aligned}
\]
Because the three indicated candidates really were removed by RevSeqPAV, **each of these five gaps, summed over all voters, is nonpositive**. Empty ballots contribute zero to every gap.

## Proof

**1. A pointwise dual certificate for the first deletion.** Put \(Q=(3k+1)(k+2)\). For one ballot, let \(I_0=1\) if it approves \(d_0\) and no final winner, and \(I_0=0\) otherwise. The following five nonnegative coefficients are valid for every integer \(k\ge2\):
\[
\begin{aligned}
\lambda_{01}&=\frac{2(k-1)}{3k+1},&
\lambda_{02}&=\frac{2(k+1)}{3k+1},\\
\lambda_{1w}&=\frac{2k(k-1)}{Q},&
\lambda_{12}&=\frac{2(k-1)}{Q},&
\lambda_{2w}&=\frac{2k}{3k+1}.
\end{aligned}
\]
For every possible ballot,
\[
I_0\le B_k+\lambda_{01}g_{01}+\lambda_{02}g_{02}+
\lambda_{1w}g_{1w}+\lambda_{12}g_{12}+\lambda_{2w}g_{2w}.\tag{1}
\]
To verify this *for all* allowed \(k\) and \(b\), subtract \(I_0\) from the right side and multiply by \(Q\). The table gives the resulting nonnegative residual. Bit patterns are written as the integer \(r=r_0+2r_1+4r_2\).

| \(r\) | \(b=0\) | \(1\le b\le k\) |
|---:|---|---|
| 0 | \(2(2k+1)\) | \(0\) |
| 1 | \(k(k+5)\) | \(4k(k+2)/(b+1)\) |
| 2 | \(2(k+2)\) | \(0\) |
| 3 | \(0\) | \(2(k+2)(2bk+3k-1)/((b+1)(b+2))\) |
| 4 | \(0\) | \(0\) |
| 5 | \(0\) | \(2(k+2)(2bk+3k+1)/((b+1)(b+2))\) |
| 6 | \((k+1)(k+2)\) | \(2(k+1)(k+2)/((b+1)(b+2))\) |
| 7 | \(0\) | \(2(k+2)(2bk+3k+1)/((b+1)(b+2))\) |

These identities follow by inserting the definitions of \(t_j\) and \(u_j\), including the zero-denominator cases. Every entry is nonnegative. Sum (1) over all \(n\) voters and use the five nonpositive aggregate gaps and the nonnegative multipliers: \(U(d_0,W)\le nB_k\).

**2. The later deletions.** With \(I_j=1\) if a ballot approves \(d_j\) and no winner, one has the following pointwise inequalities for \(j=1,2\):
\[
I_1\le\frac1{k+1}+\frac{k}{k+1}(g_{12}+g_{2w}),\qquad
I_2\le\frac1{k+1}+\frac{k}{k+1}g_{2w}.\tag{2}
\]
For \(b=0\), if \(r_1=1\) then \(g_{12}+g_{2w}=1\); if \(r_2=1\) then \(g_{2w}=1\). For \(b\ge1\), direct division by \(t_1,t_2\) gives both \(g_{12}+g_{2w}\ge-1/k\) and \(g_{2w}\ge-1/k\), which proves (2), while other \(b=0\) ballots also satisfy them. Summing gives \(U(d_1,W),U(d_2,W)\le n/(k+1)\). Since
\[
B_k-\frac1{k+1}=\frac{k(k-1)}{(3k+1)(k+2)(k+1)}\ge0,
\]
the claimed bound holds for every deleted candidate.

**3. Exact sharpness for all seat counts.** For \(k\ge2\), let \(Q=(3k+1)(k+2)\), let the candidates be \(x,a,b,w_1,\dots,w_k\), and take \(n=kQ\) voters with these *integer* ballot multiplicities:

| Ballot | Multiplicity |
|---|---:|
| \(\{w_j\}\), for each \(j=1,\dots,k\) | \(k(k+3)\) per \(j\) |
| \(\{a\}\cup(W\setminus\{w_j\})\), for each \(j\) | \(k^2\) per \(j\) |
| \(\{b\}\cup(W\setminus\{w_j\})\), for each \(j\) | \(k^2\) per \(j\) |
| \(\{x,a\}\) | \(2k^2\) |
| \(\{x,b\}\) | \(2k^2\) |
| \(\{x,a,b\}\) | \(2k\) |

For normalized marginal losses (each divided by \(n\)), the three early deleted candidates are tied at \(2/[3(k+2)]\) initially, while every winner has loss \(1/(k+2)\). After removal of \(x\), the two remaining deleted candidates and every winner tie at \(1/(k+2)\). After removing \(a\), candidate \(b\) and every winner tie at \((3k+2)/Q\). Therefore the order \(x,a,b\) is legitimate, leaving exactly \(W\). The \(2k^2+2k^2+2k\) voters with no approved winner all approve \(x\), hence their fraction is exactly \(2(2k+1)/Q=B_k\). This attains the bound with finite integer multiplicities.

**4. Strict six-seat violation and the boundary.** For \(k=6\) use \(x,a,b,w_1,\ldots,w_6\) and a smaller, tie-independent 252-voter profile:

| Ballot | Number of voters |
|---|---:|
| \(\{w_j\}\) for each \(j\) | 14 each |
| \(\{a\}\cup(W\setminus\{w_j\})\) for each \(j\) | 11 each |
| \(\{b\}\cup(W\setminus\{w_j\})\) for each \(j\) | 10 each |
| \(\{x,a\}\) | 19 |
| \(\{x,b\}\) | 21 |
| \(\{x,a,b\}\) | 2 |

The *unique* minimum-score-loss candidate at the successive stages is, respectively, \(x\), \(a\), and \(b\). Its exact loss and the smallest competing loss are \((62/3,127/6)\), then \((31,63/2)\), then \((33,100/3)\). Thus the final winners are all six \(w_j\), independently of tie-breaking. Exactly \(19+21+2=42=252/6\) voters unanimously approve \(x\) and approve none of the winners, violating JR.

JR fails precisely when some removed \(c\) has \(U(c,W)\ge n/k\). For \(k=2,3,4,5\), the upper bound satisfies \(B_k<1/k\), because the inequality reduces to \(k^2-5k-2<0\). For every integer \(k\ge6\) the reverse inequality holds, and the sharp family above therefore supplies a JR-violating outcome. At \(k=1\), JR would require that *every* voter approve a common candidate but none approve the sole winner, which cannot occur: an unsupported candidate has zero marginal loss and is always deleted before a supported candidate survives. This finishes the classification.

## Verification

The bundled `verify.py` uses only Python's standard library and checks, with exact rational arithmetic: the pointwise inequalities (1) and (2) for 79 seat counts \(2\le k\le80\), all ballot patterns and all winner approval counts; the integer sharpness construction and its three permissible deletions for 59 seat counts \(2\le k\le60\); and all three strict marginal inequalities in the 252-voter example. Run `python verify.py` from the extracted directory. The program's finite checks corroborate the calculation but the unbounded theorem rests on the residual identities and explicit algebraic construction above, not on finite testing.

## Relationship to prior work

Aziz's *A Note on Justified Representation Under the Reverse Sequential PAV Rule* proves JR for at most two deletions and presents a JR failure with \(k\ge5\) and at least seven deletions. Papasotiropoulos's 2026 *Reverse Sequential Proportional Approval Voting Rule: Proportionality and Approximation Guarantees* strengthens the two-deletion guarantee to EJR, gives a three-deletion EJR failure with 12 winners, and proves a general approximate-EJR bound. Those results do not imply the exact three-deletion unrepresented-group cap or the JR seat-count threshold. In particular, an EJR violation need not violate JR. The present theorem concerns precisely three deletions and the *completely unrepresented* cohesive-group size, not the full EJR axiom.

## Limitations

The exact fraction \(B_k\) is a worst-case extremum over all elections and permitted tie-breakings, not a prediction about typical electorates. The extremal family may rely on ties, though the 252-voter \(k=6\) failure is strict. No minimum-voter-count claim, classification of all extremizers, or result for four or more deletions is made. The novelty comparison depends on accessible and indexed literature; absence of an equivalent claim in searches does not establish global publication priority. Independent mathematical audit has not been performed.

## References

1. Georgios Papasotiropoulos, *Reverse Sequential Proportional Approval Voting Rule: Proportionality and Approximation Guarantees*, arXiv:2609.35331v1, first posted September 28, 2026. https://arxiv.org/html/2609.35331v1
2. Haris Aziz, *A Note on Justified Representation Under the Reverse Sequential PAV Rule*, 2017 manuscript. https://cgi.cse.unsw.edu.au/~haziz/invseqpav.pdf
