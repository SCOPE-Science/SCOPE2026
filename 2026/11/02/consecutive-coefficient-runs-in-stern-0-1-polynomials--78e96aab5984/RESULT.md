# Consecutive-coefficient runs in Stern (0,1)-polynomials

## Finding

For the Dilcher–Stolarsky Stern \((0,1)\)-polynomials \(P_n(x)\), every maximal run of consecutive nonzero coefficients has length at most three, and this is optimal: \(P_5(x)=1+x+x^2\).

For each integer \(r\ge2\), let \(R_{r,j}\) be the total number of maximal runs consisting of exactly \(j\) consecutive coefficient-one exponents, counted separately in every polynomial \(P_n(x)\) with \(1\le n\le2^r\). Put \(h=3^{r-2}\). Then

\[
R_{r,1}=2h+1,\qquad R_{r,2}=\frac{h+1}{2},\qquad R_{r,3}=\frac{h-1}{2},\qquad R_{r,j}=0\quad(j\ge4).
\]

The limiting frequencies of run lengths one, two, and three, among all maximal runs in the first \(2^r\) polynomials, are respectively \(2/3\), \(1/6\), and \(1/6\). These are exact all-index and all-dyadic-scale assertions, not extrapolations.

## Assumptions and scope

Define \(P_0(x)=0\), \(P_1(x)=1\), and, for \(n\ge1\),

\[
P_{2n}(x)=P_n(x^2),\qquad P_{2n+1}(x)=xP_n(x^2)+P_{n+1}(x^2).
\]

All coefficients lie in \(\{0,1\}\). Write \(E_n=\{j\ge0:[x^j]P_n(x)=1\}\), and \(s(n)=|E_n|\), with \(E_0=\varnothing\). A *run* is a maximal nonempty interval of consecutive nonnegative integers contained in \(E_n\). Runs of different polynomials are counted independently. No other definitions of Stern polynomials are used.

## Proof

**1. Residue separation and sharp maximum.** Two iterations of the defining recurrence give, for every integer \(t\ge0\),

\[
P_{4t+1}(x)=P_{t+1}(x^4)+(x+x^2)P_t(x^4),
\]
\[
P_{4t+3}(x)=(1+x)P_{t+1}(x^4)+x^3P_t(x^4).
\]

Thus every \(P_{4t+1}\) has zero coefficients at exponents congruent to \(3\pmod4\), and every \(P_{4t+3}\) has zero coefficients at exponents congruent to \(2\pmod4\). The supports of even-indexed polynomials consist only of even exponents. Hence no polynomial contains four consecutive occupied exponents. Since \(P_5=1+x+x^2\), the bound three is attained.

**2. Overlap parameters.** For \(t\ge0\), define

\[
I_t=|E_t\cap E_{t+1}|,\qquad J_t=|\{j\in E_t:j+1\in E_{t+1}\}|.
\]

The first displayed polynomial has exactly \(s(t)+I_t\) adjacent occupied pairs and \(I_t\) occupied triples. Indeed the only adjacent pairs have residue patterns \((1,2)\) or \((0,1)\pmod4\), with the latter requiring membership in the intersection. The second displayed polynomial has exactly \(s(t+1)+J_t\) adjacent pairs and \(J_t\) triples: its adjacent pairs are the \((0,1)\) pairs from \(E_{t+1}\), and the \((3,0)\) pairs crossing a four-block boundary from \(E_t\) to \(E_{t+1}\). Every crossing pair extends to a triple \((3,0,1)\). These cases are disjoint and exhaustive.

The support recurrence gives the disjoint decompositions

\[
E_{2u}=2E_u,\qquad E_{2u+1}=2E_{u+1}\sqcup(2E_u+1).
\]

Consequently, for every \(u\ge0\),

\[
I_{2u}=I_u,\quad I_{2u+1}=s(u+1),\quad
J_{2u}=s(u),\quad J_{2u+1}=J_u.
\]

In particular \(I_0=J_0=0\). No cancellation is possible because the displayed supports lie in distinct parity classes.

**3. Dyadic summation.** The usual Stern counting recurrence is

\[
s(0)=0,\ s(1)=1,\ s(2u)=s(u),\ s(2u+1)=s(u)+s(u+1).
\]

Set \(S_k=\sum_{u=0}^{2^k-1}s(u)\). Its recurrence is \(S_0=0\) and \(S_{k+1}=3S_k+1\); the boundary term is \(s(2^k)=1\). Hence

\[
S_k=\frac{3^k-1}{2},\qquad
\sum_{u=0}^{2^k-1}\bigl(s(u)+s(u+1)\bigr)=3^k.
\]

Put \(U_k=\sum_{t=0}^{2^k-1}(I_t+J_t)\). Grouping even and odd indices in the four overlap recurrences gives

\[
U_0=0,\quad U_{k+1}=U_k+3^k,\quad U_k=\frac{3^k-1}{2}.
\]

Every polynomial indexed by \(1\le n\le2^r\), apart from the even-indexed ones (which have no adjacent pair), is uniquely either \(4t+1\) or \(4t+3\), with \(0\le t<2^{r-2}\). Therefore the aggregate number of adjacent pairs and aggregate number of triples are

\[
A_r=3^{r-2}+U_{r-2}=\frac{3^{r-1}-1}{2},\qquad
B_r=U_{r-2}=\frac{3^{r-2}-1}{2}.
\]

The aggregate number of occupied coefficients equals

\[
C_r=\sum_{n=1}^{2^r}s(n)=\frac{3^r+1}{2}.
\]

Since no run exceeds length three, every triple belongs to exactly one run of length three, every run of length two contributes one adjacent pair, and every run of length three contributes two adjacent pairs. Consequently

\[
R_{r,3}=B_r,\quad R_{r,2}=A_r-2B_r,\quad R_{r,1}=C_r-2A_r+B_r.
\]

Substitution yields precisely the three claimed formulas. Their sum is \(3^{r-1}+1\). Dividing each by this sum and letting \(r\) tend to infinity gives the stated frequencies.

## Verification

The standalone script `verify.py` reconstructs all supports for \(1\le n\le4096\), independently checks each support against the Lucas-parity characterization

\[
[x^j]P_n(x)=1\iff 0\le2j\le n-1\ \text{and}\ j\mathbin{\&}(n-1-2j)=0,
\]

where \(\mathbin{\&}\) is bitwise AND, and enumerates every maximal run independently. It verifies the sharp maximum and all formulas at \(2\le r\le12\). Execute `python3 verify.py` with Python 3, without dependencies. The script's finite checks corroborate but do not replace the proof for arbitrary indices.

## Relationship to prior work

Beck and Dilcher (2021) study the coefficient matrix of the same polynomial family, including row/column/antidiagonal totals and a Thue–Morse inverse; their inspected sections do not give maximal consecutive-coefficient run lengths. Dilcher and Ericksen (2015), Proposition 5.2, compute a generating product for the *sum* of many Stern polynomials; it determines aggregate coefficients at each fixed exponent, but not the distribution of co-occurring neighboring exponents *within individual polynomials*. Their section on finer polynomial structure concerns periodic truncations and shift identities. Dilcher and Ericksen (2014) investigate factorization, cyclotomic factors and zeros; their explicit small-index table gives examples but no all-index run classification in the inspected text. The 2007 foundational article was accessible only in publisher preview, so undiscovered implicit coverage remains possible. None of these antecedents is claimed new.

## Limitations

The results concern the Dilcher–Stolarsky \((0,1)\)-polynomials, not the different Klavžar-type Stern polynomials. Only consecutive occupied coefficient exponents, maximality within each polynomial, and dyadic-prefix statistics are classified; arbitrary sparse-gap patterns and individual-polynomial run enumerators are not determined here. The literature comparison is not a guarantee of absolute priority; the complete 2007 foundational text was not accessed. The proof is mathematical and the included finite checker is supporting evidence; independent mathematical audit has not been performed.

## References

1. G. Beck and K. Dilcher, *A Matrix Related to Stern Polynomials and the Prouhet–Thue–Morse Sequence*, arXiv:2106.10400v1 (first public 2021-06-19), https://arxiv.org/abs/2106.10400.
2. K. Dilcher and L. Ericksen, *Hyperbinary Expansions and Stern Polynomials*, Electron. J. Combin. 22(2) (2015), #P2.24, DOI:10.37236/4822.
3. K. Dilcher and L. Ericksen, *Reducibility and irreducibility of Stern (0,1)-polynomials*, Commun. Math. 22 (2014), 77–102, https://dml.cz/handle/10338.dmlcz/143908.
4. K. Dilcher and K. B. Stolarsky, *A polynomial analogue to the Stern sequence*, Int. J. Number Theory 3 (2007), 85–103, DOI:10.1142/S179304210700081X. Full text not inspected.
